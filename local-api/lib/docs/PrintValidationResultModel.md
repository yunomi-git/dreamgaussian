# PrintValidationResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_model_results** | [**Dict[str, PrintValidationResultModelPerModelResultsValue]**](PrintValidationResultModelPerModelResultsValue.md) | A map of model IDs to their print validation results. | [optional] 

## Example

```python
from formlabs_local_api.models.print_validation_result_model import PrintValidationResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of PrintValidationResultModel from a JSON string
print_validation_result_model_instance = PrintValidationResultModel.from_json(json)
# print the JSON string representation of the object
print(PrintValidationResultModel.to_json())

# convert the object into a dict
print_validation_result_model_dict = print_validation_result_model_instance.to_dict()
# create an instance of PrintValidationResultModel from a dict
print_validation_result_model_from_dict = PrintValidationResultModel.from_dict(print_validation_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


