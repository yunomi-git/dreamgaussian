# PrintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer** | **str** | Printer serial name, IP address, or Fleet Control Queue ID | 
**job_name** | **str** |  | 
**find_printer_timeout_seconds** | **int** | Number of seconds to wait to find the given printer. | [optional] [default to 30]
**print_now** | **bool** | If true, the job should be printed immediately if the printer&#39;s \&quot;ready_to_print_now\&quot; status is true. Attempting to print now on a printer that does not support it will result in an error. If false, the job should be uploaded to the printer&#39;s local queue. Not including this value will default to printing now if the printer is in a ready state, and queueing the job otherwise.  | [optional] 

## Example

```python
from formlabs_local_api.models.print_request import PrintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintRequest from a JSON string
print_request_instance = PrintRequest.from_json(json)
# print the JSON string representation of the object
print(PrintRequest.to_json())

# convert the object into a dict
print_request_dict = print_request_instance.to_dict()
# create an instance of PrintRequest from a dict
print_request_from_dict = PrintRequest.from_dict(print_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


