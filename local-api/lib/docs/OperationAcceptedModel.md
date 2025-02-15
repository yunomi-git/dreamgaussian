# OperationAcceptedModel

Response to requests with `?async=true`, which return immediately, and whose ongoing progress can be queried with GET to /operations/<operationId>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** | Randomly-generated UUID for this operation | [optional] 

## Example

```python
from formlabs_local_api.models.operation_accepted_model import OperationAcceptedModel

# TODO update the JSON string below
json = "{}"
# create an instance of OperationAcceptedModel from a JSON string
operation_accepted_model_instance = OperationAcceptedModel.from_json(json)
# print the JSON string representation of the object
print(OperationAcceptedModel.to_json())

# convert the object into a dict
operation_accepted_model_dict = operation_accepted_model_instance.to_dict()
# create an instance of OperationAcceptedModel from a dict
operation_accepted_model_from_dict = OperationAcceptedModel.from_dict(operation_accepted_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


