# ManualImportUpdateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**author_id** | **int** |  | [optional] 
**book_id** | **int** |  | [optional] 
**foreign_edition_id** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**release_group** | **str** |  | [optional] 
**indexer_flags** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 
**additional_file** | **bool** |  | [optional] 
**replace_existing_files** | **bool** |  | [optional] 
**disable_release_switching** | **bool** |  | [optional] 
**rejections** | [**List[Rejection]**](Rejection.md) |  | [optional] 

## Example

```python
from readarr.models.manual_import_update_resource import ManualImportUpdateResource

# TODO update the JSON string below
json = "{}"
# create an instance of ManualImportUpdateResource from a JSON string
manual_import_update_resource_instance = ManualImportUpdateResource.from_json(json)
# print the JSON string representation of the object
print(ManualImportUpdateResource.to_json())

# convert the object into a dict
manual_import_update_resource_dict = manual_import_update_resource_instance.to_dict()
# create an instance of ManualImportUpdateResource from a dict
manual_import_update_resource_from_dict = ManualImportUpdateResource.from_dict(manual_import_update_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


