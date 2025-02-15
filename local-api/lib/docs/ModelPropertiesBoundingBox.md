# ModelPropertiesBoundingBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_corner** | [**ScenePositionModel**](ScenePositionModel.md) |  | [optional] 
**max_corner** | [**ScenePositionModel**](ScenePositionModel.md) |  | [optional] 

## Example

```python
from formlabs_local_api.models.model_properties_bounding_box import ModelPropertiesBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPropertiesBoundingBox from a JSON string
model_properties_bounding_box_instance = ModelPropertiesBoundingBox.from_json(json)
# print the JSON string representation of the object
print(ModelPropertiesBoundingBox.to_json())

# convert the object into a dict
model_properties_bounding_box_dict = model_properties_bounding_box_instance.to_dict()
# create an instance of ModelPropertiesBoundingBox from a dict
model_properties_bounding_box_from_dict = ModelPropertiesBoundingBox.from_dict(model_properties_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


