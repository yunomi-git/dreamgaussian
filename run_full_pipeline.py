from openai import OpenAI
from api_key import api_key
import openai
import requests
import os
import datetime

use_gui = False
method = "imagedream"
client = OpenAI(api_key=api_key)

prompt = "cat on a stack of pancakes"
def request_image(prompt):
  print("Fetching image")
  image_response = client.images.generate(
    model='dall-e-3',
    n=1,
    size='1024x1024',
    prompt=prompt,
    response_format="url"
  )
  print("Retrieving image")
  image_url = image_response.data[0].url

  img_data = requests.get(image_url).content
  with open('dalle_output/dalle_image.png', 'wb') as handler:
      handler.write(img_data)

cur_time = datetime.datetime.now()
save_name = "dalle_" + cur_time.strftime("%d_%m_%H_%M") + "_" + prompt

img_name = "dalle_output/dalle_image"

def quote(x):
  return "\"" + x + "\""

def optimize(version):
  if version == 1:
    bashCommand = "python main.py"
  else:
    bashCommand = "python main2.py"
  bashCommand += " --config configs/" + method + ".yaml input=" + quote(img_name + "_rgba.png") + " save_path=" + quote(save_name + "/output")
  if prompt is not None:
    bashCommand += " prompt=" + quote(prompt)
  if use_gui:
    bashCommand += " gui=True"
  print("Running:")
  print(bashCommand)
  os.system(bashCommand)

request_image(prompt)
bashCommand = "python process.py " + quote(img_name + ".png")
os.system(bashCommand)
optimize(1)
