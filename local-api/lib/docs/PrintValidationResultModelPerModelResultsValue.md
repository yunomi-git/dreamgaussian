# PrintValidationResultModelPerModelResultsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cups** | **int** | The number of cups in the model | [optional] 
**unsupported_minima** | **int** | The number of unsupported minima in the model | [optional] 
**undersupported** | **bool** | Whether the model is undersupported | [optional] 
**has_seamline** | **bool** | Whether the model has a seamline | [optional] 

## Example

```python
from formlabs_local_api.models.print_validation_result_model_per_model_results_value import PrintValidationResultModelPerModelResultsValue

# TODO update the JSON string below
json = "{}"
# create an instance of PrintValidationResultModelPerModelResultsValue from a JSON string
print_validation_result_model_per_model_results_value_instance = PrintValidationResultModelPerModelResultsValue.from_json(json)
# print the JSON string representation of the object
print(PrintValidationResultModelPerModelResultsValue.to_json())

# convert the object into a dict
print_validation_result_model_per_model_results_value_dict = print_validation_result_model_per_model_results_value_instance.to_dict()
# create an instance of PrintValidationResultModelPerModelResultsValue from a dict
print_validation_result_model_per_model_results_value_from_dict = PrintValidationResultModelPerModelResultsValue.from_dict(print_validation_result_model_per_model_results_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


