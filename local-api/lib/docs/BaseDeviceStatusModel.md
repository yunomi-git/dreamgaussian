# BaseDeviceStatusModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**product_name** | **str** |  | 
**status** | **str** |  | 
**is_connected** | **bool** |  | 
**connection_type** | **str** |  | 
**ip_address** | **str** |  | 
**firmware_version** | **str** |  | 

## Example

```python
from formlabs_local_api.models.base_device_status_model import BaseDeviceStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDeviceStatusModel from a JSON string
base_device_status_model_instance = BaseDeviceStatusModel.from_json(json)
# print the JSON string representation of the object
print(BaseDeviceStatusModel.to_json())

# convert the object into a dict
base_device_status_model_dict = base_device_status_model_instance.to_dict()
# create an instance of BaseDeviceStatusModel from a dict
base_device_status_model_from_dict = BaseDeviceStatusModel.from_dict(base_device_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


