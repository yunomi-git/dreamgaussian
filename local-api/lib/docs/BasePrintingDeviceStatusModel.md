# BasePrintingDeviceStatusModel


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
**ready_to_print_now** | **bool** | If the default behavior for newly uploaded jobs is to start printing them automatically. If false, uploaded jobs will be added to the printing queue. | 

## Example

```python
from formlabs_local_api.models.base_printing_device_status_model import BasePrintingDeviceStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of BasePrintingDeviceStatusModel from a JSON string
base_printing_device_status_model_instance = BasePrintingDeviceStatusModel.from_json(json)
# print the JSON string representation of the object
print(BasePrintingDeviceStatusModel.to_json())

# convert the object into a dict
base_printing_device_status_model_dict = base_printing_device_status_model_instance.to_dict()
# create an instance of BasePrintingDeviceStatusModel from a dict
base_printing_device_status_model_from_dict = BasePrintingDeviceStatusModel.from_dict(base_printing_device_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


