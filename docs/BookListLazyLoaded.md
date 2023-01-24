# BookListLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Book]**](Book.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.book_list_lazy_loaded import BookListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of BookListLazyLoaded from a JSON string
book_list_lazy_loaded_instance = BookListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print BookListLazyLoaded.to_json()

# convert the object into a dict
book_list_lazy_loaded_dict = book_list_lazy_loaded_instance.to_dict()
# create an instance of BookListLazyLoaded from a dict
book_list_lazy_loaded_form_dict = book_list_lazy_loaded.from_dict(book_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


