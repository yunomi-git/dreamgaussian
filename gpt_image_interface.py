import numpy as np
import torch
import matplotlib.pyplot as plt
from lang_sam import LangSAM
from PIL import Image
from api_key import api_key
from openai import OpenAI
import requests
from diffusers import StableDiffusionInpaintPipeline
import os

cached_image = {
    "a cat doing an ollie on a skateboard": "dalle/a realistic image of a cat doing a ollie on a skateboard. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose/1",
    "a carabiner": "dalle/a realistic image of a carabiner. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose/6"
}

def get_next_numeric_name(folder):
    folder_contents = os.listdir(folder)
    if len(folder_contents) == 0:
        return str(0)
    content_values = [int(name[:name.find(".")]) for name in folder_contents if name[:name.find(".")].isdigit()]
    next_name = max(content_values) + 1
    return str(next_name)

def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30 / 255, 144 / 255, 255 / 255, 0.6])
    h, w = mask.shape[0], mask.shape[1]
    # h, w = mask.shape[-2:]
    # mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)


def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))

def grab_mask_over_image(mask, image_path, bw):
    image = Image.open(image_path).convert("RGBA")
    image = np.array(image)
    if bw:
        image[:] = np.array([0, 0, 0, 255])
        image[mask] = np.array([255, 255, 255, 255])
    else:
        image[mask, 3] = 0
    im = Image.fromarray(np.uint8(image))
    return im


class Masker:
    def __init__(self):
        self.model = LangSAM()
        self.client = OpenAI(api_key=api_key)
        self.pipe = StableDiffusionInpaintPipeline.from_pretrained(
            "runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16
        )
        self.pipe = self.pipe.to("cuda")

    def get_mask(self, image_path, prompt, enlarge_ratio=1.0, invalid_threshold=0.5):
        image = Image.open(image_path).convert("RGB")
        masks, boxes, _, _ = self.model.predict(image, prompt)

        # box is xyz
        # masks is
        h, w = masks[0].shape[-2:]
        image_area = h * w
        # Combine the masks together
        combined_mask = None
        for mask in masks:
            reshaped = mask.reshape(h, w, 1)
            # Check if mask is too large
            if torch.sum(reshaped) * 1.0 / image_area > invalid_threshold:
                continue
            if combined_mask is None:
                combined_mask = mask.clone().detach()
            else:
                combined_mask = torch.logical_or(combined_mask, mask)

        combined_boxes = torch.full((h, w), fill_value=False)
        for box in boxes:
            box = box.int()
            w_box, h_box = box[2] - box[0], box[3] - box[1]
            center_w = 0.5 * (box[2] + box[0])
            center_h = 0.5 * (box[3] + box[1])
            if w_box * h_box * 1.0 / image_area > invalid_threshold:
                continue
            # Expand all
            box[1] = int(max(0, center_h - h_box * enlarge_ratio / 2.0))
            box[3] = int(min(w, center_h + h_box * enlarge_ratio / 2.0))
            box[0] = int(max(0, center_w - w_box * enlarge_ratio / 2.0))
            box[2] = int(min(h, center_w + w_box * enlarge_ratio / 2.0))
            combined_boxes[box[1]:box[3], box[0]:box[2]] = True

        return combined_mask, combined_boxes


    def request_image(self, prompt, size=1024, save=False):
        print("Fetching image")
        image_response = self.client.images.generate(
            model='dall-e-3',
            n=1,
            size=str(size) + "x" + str(size),  # "'1024x1024',
            prompt=prompt,
            response_format="url"
        )
        print("Retrieving image")
        image_url = image_response.data[0].url

        img_data = requests.get(image_url).content
        editted_image_path = "out_pictures/dalle_edits/orig_image.png"
        with open(editted_image_path, 'wb') as handler:
            handler.write(img_data)

        return editted_image_path

    def request_text(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system",
                       "content": prompt}]
        )
        answer = response.choices[0].message.content
        return answer

    def edit_image(self, image_path, orig_prompt, edit_prompt, invalid_threshold=0.5, use_stable_diffusion=True, edit_num=0):
        # get the object of the prompt
        mask_prompt = self.request_text("Which word is the object of the phrase \"" + edit_prompt + "\"? Respond only with a single word.")
        print("Looking for:", mask_prompt, "in image", image_path)
        # do the mask
        mask, box = self.get_mask(image_path, mask_prompt, enlarge_ratio=1.5, invalid_threshold=invalid_threshold)

        # save the mask in a temp location
        if use_stable_diffusion:
            use_bw = True
        else:
            use_bw = False
        masked_image = grab_mask_over_image(box, image_path, bw=use_bw)
        mask_path = image_path[:image_path.rfind(".")] + "_masked" + str(edit_num) + ".png"
        # mask_path = "out_pictures/dalle_edits/masked_temp.png"
        masked_image.save(mask_path)

        # Edit the image
        full_prompt = orig_prompt + ". " + edit_prompt
        editted_image_path = image_path[:image_path.rfind(".")] + "_edit" + str(edit_num) + ".png"

        if use_stable_diffusion:
            # These should be PIL images
            init_image = Image.open(image_path).convert("RGB")
            image = self.pipe(prompt=edit_prompt, image=init_image, mask_image=masked_image, strength=0.75).images[0]
            image.save(editted_image_path)
        else:
            response = self.client.images.edit(
                model="dall-e-2",
                image=open(image_path, "rb"),
                mask=open(mask_path, "rb"),
                prompt=full_prompt,
                n=1,
                size="1024x1024"
            )
            image_url = response.data[0].url
            img_data = requests.get(image_url).content # This is bytes

            with open(editted_image_path, 'wb') as handler:
                handler.write(img_data)
        return box, editted_image_path


def edit_existing_image(same_image=False):
    masker = Masker()

    # image_path = "out_pictures/Experiments/cartoon/cat_on_pancake.png"
    image_path = cached_image["a carabiner"] + ".png"
    orig_prompt = "a carabiner"
    # image_path = "out_pictures/saved_images/cat ice cream.png"
    # orig_prompt = "A cat sitting on a stack of pancakes."

    continuously_edit_image(image_path, masker, orig_prompt, same_image=same_image)


def continuously_edit_image(image_path, masker, orig_prompt, same_image=False):
    while True:
        edit_prompt = input("What edits do you want: ")
        orig_image = Image.open(image_path).convert("RGB")

        mask, editted_image_path = masker.edit_image(image_path=image_path, orig_prompt=orig_prompt,
                                                 edit_prompt=edit_prompt, invalid_threshold=0.5, use_stable_diffusion=False)
        fig, axs = plt.subplots(1, 2)
        ax = axs[0]
        ax.imshow(orig_image)
        show_mask(mask, ax)
        ax.axis('off')

        image = Image.open(editted_image_path).convert("RGB")
        ax = axs[1]
        ax.imshow(image)
        ax.axis('off')
        fig.suptitle(f"{edit_prompt}", fontsize=18)
        plt.show()

        if not same_image:
            image_path = editted_image_path

def generate_and_edit():
    masker = Masker()

    orig_prompt = input("Give a prompt for a picture: ")
    new_image_path = masker.request_image(prompt=orig_prompt)

    fig, ax = plt.subplots()
    image = Image.open(new_image_path).convert("RGB")
    ax.imshow(image)
    ax.axis('off')
    fig.suptitle(f"{orig_prompt}", fontsize=18)
    plt.show()

    # Ask for edits
    image_path = new_image_path

    continuously_edit_image(image_path, masker, orig_prompt)

if __name__=="__main__":
    # generate_and_edit()

    edit_existing_image(same_image=True)
    # for i, (mask, box) in enumerate(zip([masks], [boxes])):
    #     plt.figure(figsize=(10,10))
    #     plt.imshow(image)
    #     # show_mask(mask, plt.gca())
    #     show_mask(box, plt.gca())
    #
    #     plt.axis('off')
    #     plt.show()

