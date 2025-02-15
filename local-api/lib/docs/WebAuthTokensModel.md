# WebAuthTokensModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token for the user | [optional] 
**refresh_token** | **str** | The refresh token for the user | [optional] 

## Example

```python
from formlabs_local_api.models.web_auth_tokens_model import WebAuthTokensModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthTokensModel from a JSON string
web_auth_tokens_model_instance = WebAuthTokensModel.from_json(json)
# print the JSON string representation of the object
print(WebAuthTokensModel.to_json())

# convert the object into a dict
web_auth_tokens_model_dict = web_auth_tokens_model_instance.to_dict()
# create an instance of WebAuthTokensModel from a dict
web_auth_tokens_model_from_dict = WebAuthTokensModel.from_dict(web_auth_tokens_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


