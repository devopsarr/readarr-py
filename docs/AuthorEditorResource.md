# AuthorEditorResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**metadata_profile_id** | **int** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**move_files** | **bool** |  | [optional] 
**delete_files** | **bool** |  | [optional] 

## Example

```python
from readarr.models.author_editor_resource import AuthorEditorResource

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorEditorResource from a JSON string
author_editor_resource_instance = AuthorEditorResource.from_json(json)
# print the JSON string representation of the object
print AuthorEditorResource.to_json()

# convert the object into a dict
author_editor_resource_dict = author_editor_resource_instance.to_dict()
# create an instance of AuthorEditorResource from a dict
author_editor_resource_form_dict = author_editor_resource.from_dict(author_editor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


