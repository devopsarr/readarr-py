# AuthorMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foreign_author_id** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_name** | **str** |  | [optional] 
**name_last_first** | **str** |  | [optional] 
**sort_name_last_first** | **str** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**overview** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**hometown** | **str** |  | [optional] 
**born** | **datetime** |  | [optional] 
**died** | **datetime** |  | [optional] 
**status** | [**AuthorStatusType**](AuthorStatusType.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 

## Example

```python
from readarr.models.author_metadata import AuthorMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorMetadata from a JSON string
author_metadata_instance = AuthorMetadata.from_json(json)
# print the JSON string representation of the object
print AuthorMetadata.to_json()

# convert the object into a dict
author_metadata_dict = author_metadata_instance.to_dict()
# create an instance of AuthorMetadata from a dict
author_metadata_form_dict = author_metadata.from_dict(author_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


