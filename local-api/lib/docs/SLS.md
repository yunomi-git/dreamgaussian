# SLS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_powder_ml** | **float** |  | 
**total_powder_kg** | **float** |  | 
**total_sintered_powder_ml** | **float** |  | 
**total_sintered_powder_kg** | **float** |  | 
**mass_packing_density** | **float** |  | 

## Example

```python
from formlabs_local_api.models.sls import SLS

# TODO update the JSON string below
json = "{}"
# create an instance of SLS from a JSON string
sls_instance = SLS.from_json(json)
# print the JSON string representation of the object
print(SLS.to_json())

# convert the object into a dict
sls_dict = sls_instance.to_dict()
# create an instance of SLS from a dict
sls_from_dict = SLS.from_dict(sls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


