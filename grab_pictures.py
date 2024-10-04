from openai import OpenAI
from api_key import api_key
import requests
import os
from pathlib import Path
from process import remove_background


def request_image(prompt, size=1024):
  print("Fetching image")
  image_response = client.images.generate(
    model='dall-e-3',
    n=1,
    size=str(size) + "x" + str(size),#"'1024x1024',
    prompt=prompt,
    response_format="url"
  )
  print("Retrieving image")
  image_url = image_response.data[0].url

  img_data = requests.get(image_url).content
  folder = 'dalle/' + prompt + "/"
  Path(folder).mkdir(parents=True, exist_ok=True)
  next_name = get_next_numeric_name(folder)
  image_path = folder + next_name + ".png"

  with open(image_path, 'wb') as handler:
      handler.write(img_data)
  return image_path

def get_next_numeric_name(folder):
    folder_contents = os.listdir(folder)
    if len(folder_contents) == 0:
        return str(0)
    content_values = [int(name[:name.find(".")]) for name in folder_contents if name[:name.find(".")].isdigit()]
    next_name = max(content_values) + 1
    return str(next_name)

if __name__=="__main__":
    use_gui = True
    use_voice = True
    do_print = False
    method = "image_sai_custom"
    client = OpenAI(api_key=api_key)

    main_request = "a carabiner"
    prompt = "Give me an image of " + main_request + ". The view should be isotropic. The background should be purely white. It should be manufactureable from plastic"

    for i in range(4):
        out_path = request_image(prompt)
        remove_background(out_path)