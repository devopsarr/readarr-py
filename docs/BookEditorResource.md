# BookEditorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**delete_files** | **bool** |  | [optional] 
**add_import_list_exclusion** | **bool** |  | [optional] 

## Example

```python
from readarr.models.book_editor_resource import BookEditorResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookEditorResource from a JSON string
book_editor_resource_instance = BookEditorResource.from_json(json)
# print the JSON string representation of the object
print BookEditorResource.to_json()

# convert the object into a dict
book_editor_resource_dict = book_editor_resource_instance.to_dict()
# create an instance of BookEditorResource from a dict
book_editor_resource_form_dict = book_editor_resource.from_dict(book_editor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


