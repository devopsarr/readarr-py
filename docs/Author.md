# Author


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_metadata_id** | **int** |  | [optional] 
**clean_name** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**last_info_sync** | **datetime** |  | [optional] 
**path** | **str** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**added** | **datetime** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**metadata_profile_id** | **int** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**add_options** | [**AddAuthorOptions**](AddAuthorOptions.md) |  | [optional] 
**metadata** | [**AuthorMetadataLazyLoaded**](AuthorMetadataLazyLoaded.md) |  | [optional] 
**quality_profile** | [**QualityProfileLazyLoaded**](QualityProfileLazyLoaded.md) |  | [optional] 
**metadata_profile** | [**MetadataProfileLazyLoaded**](MetadataProfileLazyLoaded.md) |  | [optional] 
**books** | [**BookListLazyLoaded**](BookListLazyLoaded.md) |  | [optional] 
**series** | [**SeriesListLazyLoaded**](SeriesListLazyLoaded.md) |  | [optional] 
**name** | **str** |  | [optional] 
**foreign_author_id** | **str** |  | [optional] 

## Example

```python
from readarr.models.author import Author

# TODO update the JSON string below
json = "{}"
# create an instance of Author from a JSON string
author_instance = Author.from_json(json)
# print the JSON string representation of the object
print Author.to_json()

# convert the object into a dict
author_dict = author_instance.to_dict()
# create an instance of Author from a dict
author_form_dict = author.from_dict(author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


