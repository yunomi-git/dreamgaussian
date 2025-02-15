# UsernameAndPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from formlabs_local_api.models.username_and_password import UsernameAndPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UsernameAndPassword from a JSON string
username_and_password_instance = UsernameAndPassword.from_json(json)
# print the JSON string representation of the object
print(UsernameAndPassword.to_json())

# convert the object into a dict
username_and_password_dict = username_and_password_instance.to_dict()
# create an instance of UsernameAndPassword from a dict
username_and_password_from_dict = UsernameAndPassword.from_dict(username_and_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


