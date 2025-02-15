# DirectionVectorsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**z_direction** | **List[float]** | 3D unit vector in model space saying which piece of the model will point \&quot;up\&quot; in scene space.  | 
**x_direction** | **List[float]** | 3D unit vector in model space, perpendicular to Z direction, saying which piece of the model will point \&quot;right\&quot; in scene space.  | 

## Example

```python
from formlabs_local_api.models.direction_vectors_model import DirectionVectorsModel

# TODO update the JSON string below
json = "{}"
# create an instance of DirectionVectorsModel from a JSON string
direction_vectors_model_instance = DirectionVectorsModel.from_json(json)
# print the JSON string representation of the object
print(DirectionVectorsModel.to_json())

# convert the object into a dict
direction_vectors_model_dict = direction_vectors_model_instance.to_dict()
# create an instance of DirectionVectorsModel from a dict
direction_vectors_model_from_dict = DirectionVectorsModel.from_dict(direction_vectors_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


