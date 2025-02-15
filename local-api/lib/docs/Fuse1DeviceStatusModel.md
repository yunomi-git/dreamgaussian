# Fuse1DeviceStatusModel


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
**is_remote_print_enabled** | **bool** |  | 
**estimated_print_time_remaining_ms** | **int** |  | 
**bed_temperature_c** | **float** |  | 
**powder_level** | **str** |  | 
**printing_layer** | **int** |  | 
**printing_guid** | **str** |  | 
**cylinder_material_code** | **str** |  | 
**cylinder_serial** | **str** |  | 
**printer_material_code** | **str** |  | 
**powder_credit_g** | **float** |  | 

## Example

```python
from formlabs_local_api.models.fuse1_device_status_model import Fuse1DeviceStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of Fuse1DeviceStatusModel from a JSON string
fuse1_device_status_model_instance = Fuse1DeviceStatusModel.from_json(json)
# print the JSON string representation of the object
print(Fuse1DeviceStatusModel.to_json())

# convert the object into a dict
fuse1_device_status_model_dict = fuse1_device_status_model_instance.to_dict()
# create an instance of Fuse1DeviceStatusModel from a dict
fuse1_device_status_model_from_dict = Fuse1DeviceStatusModel.from_dict(fuse1_device_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


