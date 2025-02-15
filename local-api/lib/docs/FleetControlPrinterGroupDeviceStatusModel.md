# FleetControlPrinterGroupDeviceStatusModel


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

## Example

```python
from formlabs_local_api.models.fleet_control_printer_group_device_status_model import FleetControlPrinterGroupDeviceStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of FleetControlPrinterGroupDeviceStatusModel from a JSON string
fleet_control_printer_group_device_status_model_instance = FleetControlPrinterGroupDeviceStatusModel.from_json(json)
# print the JSON string representation of the object
print(FleetControlPrinterGroupDeviceStatusModel.to_json())

# convert the object into a dict
fleet_control_printer_group_device_status_model_dict = fleet_control_printer_group_device_status_model_instance.to_dict()
# create an instance of FleetControlPrinterGroupDeviceStatusModel from a dict
fleet_control_printer_group_device_status_model_from_dict = FleetControlPrinterGroupDeviceStatusModel.from_dict(fleet_control_printer_group_device_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


