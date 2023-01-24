# BookFileListLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[BookFile]**](BookFile.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.book_file_list_lazy_loaded import BookFileListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of BookFileListLazyLoaded from a JSON string
book_file_list_lazy_loaded_instance = BookFileListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print BookFileListLazyLoaded.to_json()

# convert the object into a dict
book_file_list_lazy_loaded_dict = book_file_list_lazy_loaded_instance.to_dict()
# create an instance of BookFileListLazyLoaded from a dict
book_file_list_lazy_loaded_form_dict = book_file_list_lazy_loaded.from_dict(book_file_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


