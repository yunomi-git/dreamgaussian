from openai import OpenAI
from api_key import api_key
import openai
import requests
import os
import datetime

use_gui = True
method = "image_sai_custom"

prompt = ""
img_name = "Experiments/cartoon/bunny_pancake"
size = 1024 # NEED TO ALTER THE YAML FILE MANUALLY

append_name = "_" + method + "_" + str(size) + ""
convert_to_grayscale = False

if convert_to_grayscale:
  append_name += "_gray"

def quote(x):
  return "\"" + x + "\""

bashCommand = "python process.py " + quote(img_name + ".png") + " --size " + str(size)
if convert_to_grayscale:
  bashCommand += " --grayscale True"
os.system(bashCommand)

def optimize(version):
  if version == 1:
    bashCommand = "python main.py"
  else:
    bashCommand = "python main2.py"
  bashCommand += " --config configs/" + method + ".yaml input=" + quote(img_name + "_rgba.png") + " save_path=" + quote(img_name + append_name + "/output")
  if prompt is not None:
    bashCommand += " prompt=" + "\"" + prompt + "\""
  if use_gui:
    bashCommand += " gui=True"
  print("Running:")
  print(bashCommand)
  os.system(bashCommand)

optimize(1)
# optimize(2)