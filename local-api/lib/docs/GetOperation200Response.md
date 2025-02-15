# GetOperation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Operation ID. | [optional] 
**status** | **str** | Current status of the operation. | [optional] 
**progress** | **float** | Progress of the operation (0.0 to 1.0). | [optional] 
**result** | **object** | Result of the operation, if succeeded or failed. Matches the schema of the operation or its error response. | [optional] 

## Example

```python
from formlabs_local_api.models.get_operation200_response import GetOperation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOperation200Response from a JSON string
get_operation200_response_instance = GetOperation200Response.from_json(json)
# print the JSON string representation of the object
print(GetOperation200Response.to_json())

# convert the object into a dict
get_operation200_response_dict = get_operation200_response_instance.to_dict()
# create an instance of GetOperation200Response from a dict
get_operation200_response_from_dict = GetOperation200Response.from_dict(get_operation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


