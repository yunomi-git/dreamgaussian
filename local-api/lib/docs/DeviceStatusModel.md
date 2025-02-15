# DeviceStatusModel


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
**dashboard_group_id** | **str** |  | 
**dashboard_queue_id** | **str** |  | 
**queue_paused** | **bool** |  | 
**has_form_auto** | **bool** |  | 
**supported_machine_type_ids** | **List[str]** |  | 
**printers** | [**List[FleetControlPrinterGroupDeviceStatusModelAllOfPrinters]**](FleetControlPrinterGroupDeviceStatusModelAllOfPrinters.md) |  | 
**is_remote_print_enabled** | **bool** |  | 
**estimated_print_time_remaining_ms** | **int** |  | 
**tank_id** | **str** |  | 
**tank_material_code** | **str** |  | 
**cartridge_data** | [**Dict[str, Form4FamilyDeviceStatusModelAllOfCartridgeData]**](Form4FamilyDeviceStatusModelAllOfCartridgeData.md) |  | 
**form_auto_status** | **str** |  | 
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
from formlabs_local_api.models.device_status_model import DeviceStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatusModel from a JSON string
device_status_model_instance = DeviceStatusModel.from_json(json)
# print the JSON string representation of the object
print(DeviceStatusModel.to_json())

# convert the object into a dict
device_status_model_dict = device_status_model_instance.to_dict()
# create an instance of DeviceStatusModel from a dict
device_status_model_from_dict = DeviceStatusModel.from_dict(device_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


