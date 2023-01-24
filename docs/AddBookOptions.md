# AddBookOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_type** | [**BookAddType**](BookAddType.md) |  | [optional] 
**search_for_new_book** | **bool** |  | [optional] 

## Example

```python
from readarr.models.add_book_options import AddBookOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AddBookOptions from a JSON string
add_book_options_instance = AddBookOptions.from_json(json)
# print the JSON string representation of the object
print AddBookOptions.to_json()

# convert the object into a dict
add_book_options_dict = add_book_options_instance.to_dict()
# create an instance of AddBookOptions from a dict
add_book_options_form_dict = add_book_options.from_dict(add_book_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


