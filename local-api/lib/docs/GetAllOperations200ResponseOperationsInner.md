# GetAllOperations200ResponseOperationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Operation ID. | [optional] 
**status** | **str** | Current status of the operation. | [optional] 
**progress** | **float** | Progress of the operation (0.0 to 1.0). | [optional] 

## Example

```python
from formlabs_local_api.models.get_all_operations200_response_operations_inner import GetAllOperations200ResponseOperationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllOperations200ResponseOperationsInner from a JSON string
get_all_operations200_response_operations_inner_instance = GetAllOperations200ResponseOperationsInner.from_json(json)
# print the JSON string representation of the object
print(GetAllOperations200ResponseOperationsInner.to_json())

# convert the object into a dict
get_all_operations200_response_operations_inner_dict = get_all_operations200_response_operations_inner_instance.to_dict()
# create an instance of GetAllOperations200ResponseOperationsInner from a dict
get_all_operations200_response_operations_inner_from_dict = GetAllOperations200ResponseOperationsInner.from_dict(get_all_operations200_response_operations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


