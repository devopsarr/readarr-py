# BookLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Book**](Book.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.book_lazy_loaded import BookLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of BookLazyLoaded from a JSON string
book_lazy_loaded_instance = BookLazyLoaded.from_json(json)
# print the JSON string representation of the object
print BookLazyLoaded.to_json()

# convert the object into a dict
book_lazy_loaded_dict = book_lazy_loaded_instance.to_dict()
# create an instance of BookLazyLoaded from a dict
book_lazy_loaded_form_dict = book_lazy_loaded.from_dict(book_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


