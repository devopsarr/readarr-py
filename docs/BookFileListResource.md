# BookFileListResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_file_ids** | **List[int]** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 

## Example

```python
from readarr.models.book_file_list_resource import BookFileListResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookFileListResource from a JSON string
book_file_list_resource_instance = BookFileListResource.from_json(json)
# print the JSON string representation of the object
print BookFileListResource.to_json()

# convert the object into a dict
book_file_list_resource_dict = book_file_list_resource_instance.to_dict()
# create an instance of BookFileListResource from a dict
book_file_list_resource_form_dict = book_file_list_resource.from_dict(book_file_list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


