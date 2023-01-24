# RenameBookResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_id** | **int** |  | [optional] 
**book_id** | **int** |  | [optional] 
**book_file_id** | **int** |  | [optional] 
**existing_path** | **str** |  | [optional] 
**new_path** | **str** |  | [optional] 

## Example

```python
from readarr.models.rename_book_resource import RenameBookResource

# TODO update the JSON string below
json = "{}"
# create an instance of RenameBookResource from a JSON string
rename_book_resource_instance = RenameBookResource.from_json(json)
# print the JSON string representation of the object
print RenameBookResource.to_json()

# convert the object into a dict
rename_book_resource_dict = rename_book_resource_instance.to_dict()
# create an instance of RenameBookResource from a dict
rename_book_resource_form_dict = rename_book_resource.from_dict(rename_book_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


