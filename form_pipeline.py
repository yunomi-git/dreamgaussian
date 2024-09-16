"""
Demo application that batches all STL files in a folder into .form files.

Usage: python3 demo-batch.py ~/Documents/folder-of-stl-files

Author: @jhaip
"""

import os
import formlabs
from formlabs.models.auto_orient_post_request import AutoOrientPostRequest

# def create_scene(preform):
#     return preform.api.scene_post({
#         "machine_type": "FORM-4-0",
#         "material_code": "FLGPGR05",
#         "slice_thickness": 0.1,
#         "print_setting": "DEFAULT",
#     })

def create_scene(preform):
    return preform.api.scene_post({
        "machine_type": "FORM-3-0",
        "material_code": "FLGPGR05",
        "slice_thickness": 0.1,
        "print_setting": "DEFAULT",
    })

def run_preform_slice(object_path, output_dir_path, do_print=False):
    # pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.app/Contents/MacOS/PreFormServer"
    pathToPreformServer = "C:\\Users\\nomiy\MyProgramFiles\PreForm_Server\PreformServer.exe"

    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
        create_scene(preform)

        # file = open(object_path, "r")

        units = "DETECTED"
        if object_path.endswith(".obj"):
            units = "INCHES"
        print(f"Importing {object_path}")
        new_model = preform.api.scene_import_model_post({
            "file": object_path,
            "repair_behavior": "REPAIR",
            "units": units
        })
        new_model_id = new_model.model_id

        print(f"Model ID: {new_model_id}")
        print(f"Auto orienting {new_model_id}")
        preform.api.auto_orient_post(AutoOrientPostRequest.from_dict({"models": [new_model_id]}))
        print(f"Auto supporting {new_model_id}")
        preform.api.auto_support_post(AutoOrientPostRequest.from_dict({"models": [new_model_id]}))
        print(f"Auto layouting all")
        try:
            preform.api.auto_layout_post_with_http_info(
                AutoOrientPostRequest.from_dict({"models": "ALL"})
            )
        except formlabs.exceptions.ServiceException as e:
            if e.status == 500 and e.data.error == "AUTO_LAYOUT_FAILED":
                print("Not all models can fit, removing model")
                create_scene(preform)

        save_path = os.path.join(output_dir_path, f"output.form")
        preform.api.save_form_post(save_path)
        print(f"Saving to {save_path}")

        if do_print:
            preform.api.v1_print_post(printer="Diesel-M-EVT6-028", job_name="Dalle_print")

# def send_file_to_print(printer_name, output_file, prompt):
#     pathToPreformServer = "C:\\Users\\nomiy\MyProgramFiles\PreForm_Server\PreformServer.exe"
#
#     with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
#         create_scene(preform)
#         formlabs.api.default_api.
#     formlabs.api.default_api.v1_print_post({
#         "printer": "Diesel-M-EVT6-028",
#         "job_name": "Dalle_" + prompt
#     })
