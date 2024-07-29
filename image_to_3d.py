import os

use_gui = False
method = "image_sai"

prompt = ""
img_name = "Experiments/hardware/hammer1"
size = 1024
yaml_args = {
  "ref_size": 1024,
  "percent_dense": 0.15,
  # "num_pts": 10000
}

append_name = "_" + method
for key in list(yaml_args.keys()):
  append_name += "_" + key + str(yaml_args[key])
convert_to_grayscale = False

if convert_to_grayscale:
  append_name += "_gray"

def quote(x):
  return "\"" + x + "\""

bashCommand = "python process.py " + quote(img_name + ".png") + " --size " + str(size)
if convert_to_grayscale:
  bashCommand += " --grayscale True"
os.system(bashCommand)

def optimize(version, yaml_args):
  if version == 1:
    bashCommand = "python main.py"
  else:
    bashCommand = "python main2.py"
  bashCommand += " --config configs/" + method + ".yaml input=" + quote(img_name + "_rgba.png") + " save_path=" + quote(img_name + append_name + "/output")
  for key in list(yaml_args.keys()):
    bashCommand += " " + key + "=" + str(yaml_args[key])
  if prompt is not None:
    bashCommand += " prompt=" + "\"" + prompt + "\""
  if use_gui:
    bashCommand += " gui=True"
  print("Running:")
  print(bashCommand)
  os.system(bashCommand)

optimize(1, yaml_args)
# optimize(2)