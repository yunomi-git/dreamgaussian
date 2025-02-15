import formlabs_local_api as formlabs
from formlabs_local_api import Manual, ManualLayerThicknessMm, SceneTypeModel, DiscoverDevicesRequest
import pathlib
import sys
import requests
import os
import json
def create_form_file():
    if sys.platform == 'win32':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer/PreFormServer.exe"
    elif sys.platform == 'darwin':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.app/Contents/MacOS/PreFormServer"
    else:
        print("Unsupported platform")
        sys.exit(1)
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
        # print("discovering devices")
        preform.api.create_scene(SceneTypeModel(Manual(
            machine_type="FORM-4-0",
            material_code="FLGPGR05",
            layer_thickness_mm=ManualLayerThicknessMm("0.1"),
            print_setting="DEFAULT",
        )))
        print("Scene created")

        print("Loading Model")
        # Load model
        model_path = "C:\\Users\\nomiy\\MyProgramFiles\\dreamgaussian\\stls\\dragon_carabiner.form"
        requests.request(
            "POST",
            "http://localhost:44388/load-form/",
            json={
                "file": model_path
            },
        ).raise_for_status()
        print("Model loaded")

        print("Sending to printer")
        requests.request(
            "POST",
            "http://localhost:44388/scene/print/",
            json={
                "printer": "Form4-SuccinctEel",
                "job_name": "carabiner",
            },
        ).raise_for_status()
        print(f"Job upload complete")

def run_preform_slice(object_path, output_dir_path):
    if sys.platform == 'win32':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer/PreFormServer.exe"
    elif sys.platform == 'darwin':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.app/Contents/MacOS/PreFormServer"
    else:
        print("Unsupported platform")
        sys.exit(1)
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
        # print("discovering devices")
        preform.api.create_scene(SceneTypeModel(Manual(
            machine_type="FORM-4-0",
            material_code="FLGPGR05",
            layer_thickness_mm=ManualLayerThicknessMm("0.1"),
            print_setting="DEFAULT",
        )))
        print("Scene created")


        units = "DETECTED"
        if object_path.endswith(".obj"):
            units = "INCHES"
        print(f"Importing {object_path}") # TODO make sure this is absolute path
        response = requests.request(
            "POST",
            "http://localhost:44388/scene/import-model/",
            json={
                "file": object_path,
                "repair_behavior": "REPAIR",
                "units": units

            },
        )
        response.raise_for_status()
        # new_model_id = response["id"]
        print(f"Model ID: ")

        print(f"Auto orienting ")
        response = requests.request(
            "POST",
            "http://localhost:44388/scene/auto-orient/",
            json={
                "models": "ALL"
            },
        )
        response.raise_for_status()

        print(f"Auto supporting ")
        response = requests.request(
            "POST",
            "http://localhost:44388/scene/auto-support/",
            json={
                "models": "ALL"
            },
        )
        response.raise_for_status()

        print(f"Auto layouting all")
        response = requests.request(
            "POST",
            "http://localhost:44388/scene/auto-layout/",
            json={
                "models": "ALL"
            },
        )
        response.raise_for_status()


        save_path = os.path.join(output_dir_path, f"output.form")
        print(f"Saving to {save_path}")
        response = requests.request(
            "POST",
            "http://localhost:44388/scene/save-form/",
            json={
                "file": save_path
            },
        )
        response.raise_for_status()

        return save_path

        # print("Sending to printer")
        # requests.request(
        #     "POST",
        #     "http://localhost:44388/scene/print/",
        #     json={
        #         "printer": "Form4-SuccinctEel",
        #         "job_name": "carabiner",
        #     },
        # ).raise_for_status()
        # print(f"Job upload complete")

def send_to_printer(form_file):
    if sys.platform == 'win32':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer/PreFormServer.exe"
    elif sys.platform == 'darwin':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.app/Contents/MacOS/PreFormServer"
    else:
        print("Unsupported platform")
        sys.exit(1)
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
        # print("discovering devices")
        preform.api.create_scene(SceneTypeModel(Manual(
            machine_type="FORM-4-0",
            material_code="FLGPGR05",
            layer_thickness_mm=ManualLayerThicknessMm("0.1"),
            print_setting="DEFAULT",
        )))
        print("Scene created")

        print("Loading Model")
        # Load model
        # model_path = "C:\\Users\\nomiy\\MyProgramFiles\\dreamgaussian\\stls\\dragon_carabiner.form"
        requests.request(
            "POST",
            "http://localhost:44388/load-form/",
            json={
                "file": form_file
            },
        ).raise_for_status()
        print("Model loaded")

        print("Sending to printer")
        requests.request(
            "POST",
            "http://localhost:44388/scene/print/",
            json={
                "printer": "Form4-SuccinctEel",
                "job_name": "carabiner",
            },
        ).raise_for_status()
        print(f"Job upload complete")

if __name__ == "__main__":
    run_preform_slice()