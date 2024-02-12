# AddAuthorOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 
**books_to_monitor** | **List[str]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**search_for_missing_books** | **bool** |  | [optional] 

## Example

```python
from readarr.models.add_author_options import AddAuthorOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AddAuthorOptions from a JSON string
add_author_options_instance = AddAuthorOptions.from_json(json)
# print the JSON string representation of the object
print AddAuthorOptions.to_json()

# convert the object into a dict
add_author_options_dict = add_author_options_instance.to_dict()
# create an instance of AddAuthorOptions from a dict
add_author_options_form_dict = add_author_options.from_dict(add_author_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


