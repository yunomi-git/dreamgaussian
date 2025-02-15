# UploadFirmwareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer** | **str** | Local network IP address, or machine serial name to upload firmware to | 
**file_path** | **str** | Local file path to the firmware .formware or .formware2 file | 

## Example

```python
from formlabs_local_api.models.upload_firmware_request import UploadFirmwareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadFirmwareRequest from a JSON string
upload_firmware_request_instance = UploadFirmwareRequest.from_json(json)
# print the JSON string representation of the object
print(UploadFirmwareRequest.to_json())

# convert the object into a dict
upload_firmware_request_dict = upload_firmware_request_instance.to_dict()
# create an instance of UploadFirmwareRequest from a dict
upload_firmware_request_from_dict = UploadFirmwareRequest.from_dict(upload_firmware_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


