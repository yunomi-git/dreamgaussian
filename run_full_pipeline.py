from openai import OpenAI
from api_key import api_key
import openai
import requests
import os
import datetime
import speech_playground
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import trimesh_util
import trimesh
import trimesh_obj
from process import remove_background
import grab_pictures

use_gui = True
use_voice = False
do_print = False
size = 1024
method = "image_sai_custom"
client = OpenAI(api_key=api_key)

if use_voice:
  print(">Initializing. Wait...")
  print(">Waiting for Hello")
  speech_playground.wait_for_speech(5)
  speech_playground.speak_text("Hey, what can I make for you?")
  main_request = speech_playground.grab_speech(10)
  print("You requested a " + main_request)
  speech_playground.speak_text("You wanted a " + main_request + ". You got it!")
else:
  main_request = "cat sitting on bowl of ice cream."

# prompt = "a cartoon image of " + main_request + ". do not add background"
prompt = "a dslr isotropic image of " + main_request + ". do not add background"
# def request_image(prompt):
#   print("Fetching image")
#   image_response = client.images.generate(
#     model='dall-e-3',
#     n=1,
#     size='1024x1024',
#     prompt=prompt,
#     response_format="url"
#   )
#   print("Retrieving image")
#   image_url = image_response.data[0].url
#
#   img_data = requests.get(image_url).content
#   image_path = 'dalle_output/dalle_image.png'
#   with open(image_path, 'wb') as handler:
#       handler.write(img_data)
#   # Show the image
#   img = mpimg.imread(image_path)
#   plt.imshow(img)
#   plt.show()

cur_time = datetime.datetime.now()
save_name = "dalle_" + cur_time.strftime("%d_%m_%H_%M") + "_" + main_request
img_name = "dalle_output/dalle_image"

def quote(x):
  return "\"" + x + "\""

def generate_3d(version, source_img, size=1024):
  if version == 1:
    bashCommand = "python main.py"
  else:
    bashCommand = "python main2.py"
  bashCommand += (" --config configs/" + method + ".yaml input=" + quote(source_img)
                  + " save_path=" + quote(save_name + "/output") + 'ref_size=' + str(size))
  if prompt is not None:
    bashCommand += " prompt=" + quote(prompt)
  if use_gui:
    bashCommand += " gui=True"

  print("Running:")
  print(bashCommand)
  os.system(bashCommand)

if __name__=="__main__":
  print("> Generating Image")
  img_path = grab_pictures.request_image(prompt, size=size)
  img_path = remove_background(img_path, size=size)
  # bashCommand = "python process.py " + quote(img_name + ".png")
  # os.system(bashCommand)

  print("> Processing and generating 3D...")
  generate_3d(1, source_img=img_path, size=size)
  generated_output_path = "logs/" + save_name + "/output_mesh.obj"
  mesh = trimesh.load(generated_output_path)
  trimesh_util.show_mesh(mesh)

  print("> Processing to add details")
  new_mesh = trimesh_obj.modify_obj_with_color(obj_path=generated_output_path,
                                    edge_weight=0.5, show_progress=False)
  trimesh_util.show_mesh(new_mesh)
  processed_output_path = "logs/" + save_name + "/processed_mesh.obj"
  new_mesh.export(processed_output_path)

  if do_print:
    from form_pipeline import run_preform_slice

    print("> Slicing")
    run_preform_slice(processed_output_path,
                      output_dir_path="logs/" + save_name+"/", do_print=do_print)
