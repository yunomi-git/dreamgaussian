# UserInformationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**persistent_id** | **str** |  | [optional] 

## Example

```python
from formlabs_local_api.models.user_information_model import UserInformationModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserInformationModel from a JSON string
user_information_model_instance = UserInformationModel.from_json(json)
# print the JSON string representation of the object
print(UserInformationModel.to_json())

# convert the object into a dict
user_information_model_dict = user_information_model_instance.to_dict()
# create an instance of UserInformationModel from a dict
user_information_model_from_dict = UserInformationModel.from_dict(user_information_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


