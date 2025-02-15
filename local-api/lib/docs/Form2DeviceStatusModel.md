# Form2DeviceStatusModel


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
**estimated_print_time_remaining_ms** | **int** |  | 
**tank_id** | **str** |  | 
**tank_material_code** | **str** |  | 
**cartridge_data** | [**Dict[str, Form4FamilyDeviceStatusModelAllOfCartridgeData]**](Form4FamilyDeviceStatusModelAllOfCartridgeData.md) |  | 

## Example

```python
from formlabs_local_api.models.form2_device_status_model import Form2DeviceStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of Form2DeviceStatusModel from a JSON string
form2_device_status_model_instance = Form2DeviceStatusModel.from_json(json)
# print the JSON string representation of the object
print(Form2DeviceStatusModel.to_json())

# convert the object into a dict
form2_device_status_model_dict = form2_device_status_model_instance.to_dict()
# create an instance of Form2DeviceStatusModel from a dict
form2_device_status_model_from_dict = Form2DeviceStatusModel.from_dict(form2_device_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


