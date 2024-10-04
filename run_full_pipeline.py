from openai import OpenAI
from api_key import api_key
import os
import datetime
import numpy as np
import speech_playground
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
# method = "imagedream_custom"
client = OpenAI(api_key=api_key)

def augment_prompt(orig_prompt):
    # prompt = "a cartoon image of " + main_request + ". do not add background"
    # prompt = "a dslr isotropic image of " + main_request + ". do not add background"
    prompt = "a realistic image of " + orig_prompt + ". Do not add any other objects. The view should be isotropic. Do not add a background. Put it in a default pose"
    return prompt

def get_request_voice():
    print(">Initializing. Wait...")
    speaker = speech_playground.Speaker()
    speaker.calibrate()
    speaker.speak_text("I am now on standby.")
    print(">Waiting for Hello")
    speaker.wait_for_speech(60)
    speaker.speak_text("Hey, what can I make for you?")
    request = speaker.grab_speech(10)
    print("You requested a " + request)
    speaker.speak_text("You wanted a " + request + ". You got it!")
    return request

def quote(x):
    return "\"" + x + "\""

def generate_3d(version, source_img, size=1024, prompt=None):
    if version == 1:
        bashCommand = "python main.py"
    else:
        bashCommand = "python main2.py"
    bashCommand += (" --config configs/" + method + ".yaml input=" + quote(source_img)
                    + " save_path=" + quote(save_name + "/output") + ' ref_size=' + str(size) + " automatic_start=True ")
    if prompt is not None:
        bashCommand += " prompt=" + quote(prompt)
    if use_gui:
        bashCommand += " gui=True"

    print("Running:")
    print(bashCommand)
    os.system(bashCommand)

if __name__=="__main__":
    if use_voice:
        main_request = get_request_voice()
    else:
        main_request = "a carabiner"

    prompt = augment_prompt(main_request)

    cur_time = datetime.datetime.now()
    save_name = "dalle_" + cur_time.strftime("%d_%m_%H_%M") + "_" + main_request

    print("> Generating Image")
    img_path = grab_pictures.request_image(prompt, size=size)
    img_path = remove_background(img_path, size=size)

    print("> Processing and generating 3D...")
    generate_3d(1, source_img=img_path, size=size)
    generated_output_path = "logs/" + save_name + "/output_mesh.obj"
    mesh = trimesh.load(generated_output_path)
    mesh = trimesh_util.get_transformed_mesh_trs(mesh, orientation=[np.pi/2, -np.pi/2, 0])
    trimesh_util.show_mesh(mesh)

    print("> Processing to add details")
    new_mesh = trimesh_obj.modify_obj_with_color(obj_path=generated_output_path,
                                      edge_weight=0.2, show_progress=False)
    # new_mesh = trimesh_util.get_largest_submesh(new_mesh)
    new_mesh = trimesh_util.get_transformed_mesh_trs(new_mesh, orientation=[np.pi/2, -np.pi/2, 0])
    # trimesh_util.show_mesh(new_mesh)
    processed_output_path = "logs/" + save_name + "/processed_mesh.obj"
    new_mesh.export(processed_output_path)

    if do_print:
      from form_pipeline import run_preform_slice

      print("> Slicing")
      run_preform_slice(processed_output_path,
                        output_dir_path="logs/" + save_name+"/", do_print=do_print)
