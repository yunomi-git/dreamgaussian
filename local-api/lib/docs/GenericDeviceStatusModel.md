# GenericDeviceStatusModel


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
from formlabs_local_api.models.generic_device_status_model import GenericDeviceStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDeviceStatusModel from a JSON string
generic_device_status_model_instance = GenericDeviceStatusModel.from_json(json)
# print the JSON string representation of the object
print(GenericDeviceStatusModel.to_json())

# convert the object into a dict
generic_device_status_model_dict = generic_device_status_model_instance.to_dict()
# create an instance of GenericDeviceStatusModel from a dict
generic_device_status_model_from_dict = GenericDeviceStatusModel.from_dict(generic_device_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


