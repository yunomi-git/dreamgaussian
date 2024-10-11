from openai import OpenAI
from api_key import api_key
import os
import datetime
import numpy as np
import speech_playground
import trimesh_util
import trimesh
import trimesh_obj
from process import remove_background, to_rgba
import grab_pictures
import gpt_image_interface
import matplotlib.pyplot as plt
from PIL import Image

use_gui = True
use_voice = False
use_cached_image = True
do_continuous_edit = False
do_print = False
remove_bg = True

size = 1024
method = "image_sai_custom"
# method = "imagedream_custom"
# client = OpenAI(api_key=api_key)

cached_image = {
    "a cat doing an ollie on a skateboard": "dalle/a realistic image of a cat doing a ollie on a skateboard. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose/1",
    # "a carabiner": "dalle/a realistic image of a carabiner. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose/6",
    "philips": "dalle/a realistic image of a philips head screwdriver bit. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose/3", #3
    "tweezers": "dalle/a realistic image of precision tweezers with an angled tip. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose/12",
    # "keychain": "dalle/a realistic image of a keychain in the shape of a dragon. Do not add any other objects. The view should be isotropic. Do not add a background/1", # 1 keychain is good
    # "dragon": "dalle/a realistic image of a hook in the shape of a dragon. Do not add any other objects. The view should be isotropic. Do not add a background/6", # 0, 7, 4. 6
    "carabiner": "dalle/a realistic image of carabiner in the shape of a dragon with two slots. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose/14",
    "flat": "dalle/a realistic image of flat head screwdriver bit. Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose. do not add shadow/4"

}

def augment_prompt(orig_prompt):
    # prompt = "a cartoon image of " + orig_prompt + ". Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose"
    # prompt = "a cartoon image of " + main_request + ". do not add background"
    # prompt = "a dslr isotropic image of " + main_request + ". do not add background"
    prompt = "a realistic image of " + orig_prompt + ". Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose"
    return prompt

def get_request_voice():
    speaker.speak_text("I am now on standby.")
    print(">Waiting for Hello")
    speaker.wait_for_speech(60)
    speaker.speak_text("Hey, what can I make for you?")
    request = speaker.grab_speech(10)
    request = masker.request_text("what is the object of the verb \"make\" in the phrase \"" + request + "\"")
    print("You requested a " + request)
    speaker.speak_text("You wanted a " + request + ". You got it!")
    return request

def request_edits(use_voice):
    if use_voice:
        speaker.speak_text("How does this look?")
        user_response = speaker.grab_speech(max_time=20)
    else:
        user_response = input("How does this look?: ")

    return user_response

def quote(x):
    return "\"" + x + "\""

def generate_3d(version, source_img, save_name, size=1024, prompt=None, iters=500):
    if version == 1:
        bashCommand = "python main.py"
    else:
        bashCommand = "python main2.py"
    bashCommand += (" --config configs/" + method + ".yaml input=" + quote(source_img)
                    + " save_path=" + quote(save_name + "/output") + #' iters=' + str(iters) +
                    ' ref_size=' + str(size) + " automatic_start=True ")
    if prompt is not None:
        bashCommand += " prompt=" + quote(prompt)
    if use_gui:
        bashCommand += " gui=True"

    print("Running:")
    print(bashCommand)
    os.system(bashCommand)
    return "logs/" + save_name + "/output_mesh.obj"

if __name__=="__main__":
    print(">Initializing. Wait...")
    if use_voice:
        speaker = speech_playground.Speaker()
        speaker.calibrate()
    masker = gpt_image_interface.Masker()

    if use_voice:
        main_request = get_request_voice()
    else:
        main_request = "tweezers"

        prompt = augment_prompt(main_request)

        cur_time = datetime.datetime.now()
        save_name = "dalle_" + cur_time.strftime("%d_%m_%H_%M") + "_" + main_request

    if not use_cached_image:
        print("> Generating Image")
        orig_img_path = grab_pictures.request_image(prompt, size=size)
    else:
        orig_img_path = cached_image[main_request] + ".png"
    img_path = remove_background(orig_img_path, size=size)


    print("> Processing and generating 3D...")
    generated_output_path = generate_3d(1, save_name=save_name, source_img=img_path, size=size)
    mesh = trimesh.load(generated_output_path)
    mesh = trimesh_util.get_transformed_mesh_trs(mesh, orientation=[np.pi/2, -np.pi/2, 0])
    trimesh_util.show_mesh(mesh)

    # Now do edit chain
    edit_image_input_path = orig_img_path
    edit_num = 0
    if do_continuous_edit:
        while True:
            # Ask for make a new mesh
            # Get the request to make the new image
            edit_prompt = request_edits(use_voice) # "How does this look"
            if edit_prompt == "done":
                break
            # Make the new image
            # fig, ax = plt.subplots()
            # orig_image = Image.open(edit_image_input_path).convert("RGB")
            # ax.imshow(orig_image)
            # ax.axis('off')
            # plt.show()

            if use_cached_image:
                orig_img_path = cached_image[main_request] + "_edit" + str(edit_num) + ".png"

            _, editted_image_path = masker.edit_image(image_path=edit_image_input_path, orig_prompt=prompt,
                                                         edit_prompt=edit_prompt, invalid_threshold=0.5,
                                                         use_stable_diffusion=False, edit_num=edit_num)
            print("editted path", editted_image_path)
            edit_image_input_path = editted_image_path
            editted_image_path = remove_background(editted_image_path, size=size)
            edit_num += 1
            # Now get the 3d object
            generated_output_path = generate_3d(1, save_name=save_name + "_edit" + str(edit_num), source_img=editted_image_path, size=size)
            # Show it off
            # How do i show it while still getting a response?




    print("> Processing to add details")
    new_mesh = trimesh_obj.modify_obj_with_color(obj_path=generated_output_path,
                                      edge_weight=0.2, show_progress=False)
    # new_mesh = trimesh_util.get_largest_submesh(new_mesh)
    new_mesh = trimesh_util.get_transformed_mesh_trs(new_mesh, orientation=[np.pi/2, -np.pi/2, 0], scale=2)
    if "large" in main_request:
        new_mesh = trimesh_util.get_transformed_mesh_trs(new_mesh, scale=2)

    # trimesh_util.show_mesh(new_mesh)
    processed_output_path = "logs/" + save_name + "/processed_mesh.obj"
    new_mesh.export(processed_output_path)

    if do_print:
      from form_pipeline import run_preform_slice

      print("> Slicing")
      run_preform_slice(processed_output_path,
                        output_dir_path="logs/" + save_name+"/", do_print=do_print)
