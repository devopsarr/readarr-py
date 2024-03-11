# AuthorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_metadata_id** | **int** |  | [optional] 
**status** | [**AuthorStatusType**](AuthorStatusType.md) |  | [optional] 
**ended** | **bool** |  | [optional] [readonly] 
**author_name** | **str** |  | [optional] 
**author_name_last_first** | **str** |  | [optional] 
**foreign_author_id** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**next_book** | [**Book**](Book.md) |  | [optional] 
**last_book** | [**Book**](Book.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**remote_poster** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**metadata_profile_id** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**clean_name** | **str** |  | [optional] 
**sort_name** | **str** |  | [optional] 
**sort_name_last_first** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**added** | **datetime** |  | [optional] 
**add_options** | [**AddAuthorOptions**](AddAuthorOptions.md) |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**statistics** | [**AuthorStatisticsResource**](AuthorStatisticsResource.md) |  | [optional] 

## Example

```python
from readarr.models.author_resource import AuthorResource

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorResource from a JSON string
author_resource_instance = AuthorResource.from_json(json)
# print the JSON string representation of the object
print(AuthorResource.to_json())

# convert the object into a dict
author_resource_dict = author_resource_instance.to_dict()
# create an instance of AuthorResource from a dict
author_resource_form_dict = author_resource.from_dict(author_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


