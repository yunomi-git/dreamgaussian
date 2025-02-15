# GetAllOperations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of operations | [optional] 
**operations** | [**List[GetAllOperations200ResponseOperationsInner]**](GetAllOperations200ResponseOperationsInner.md) |  | [optional] 

## Example

```python
from formlabs_local_api.models.get_all_operations200_response import GetAllOperations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllOperations200Response from a JSON string
get_all_operations200_response_instance = GetAllOperations200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllOperations200Response.to_json())

# convert the object into a dict
get_all_operations200_response_dict = get_all_operations200_response_instance.to_dict()
# create an instance of GetAllOperations200Response from a dict
get_all_operations200_response_from_dict = GetAllOperations200Response.from_dict(get_all_operations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


