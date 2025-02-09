# BookResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**author_title** | **str** |  | [optional] 
**series_title** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**author_id** | **int** |  | [optional] 
**foreign_book_id** | **str** |  | [optional] 
**foreign_edition_id** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**any_edition_ok** | **bool** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**release_date** | **datetime** |  | [optional] 
**page_count** | **int** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**author** | [**AuthorResource**](AuthorResource.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**statistics** | [**BookStatisticsResource**](BookStatisticsResource.md) |  | [optional] 
**added** | **datetime** |  | [optional] 
**add_options** | [**AddBookOptions**](AddBookOptions.md) |  | [optional] 
**remote_cover** | **str** |  | [optional] 
**editions** | [**List[EditionResource]**](EditionResource.md) |  | [optional] 

## Example

```python
from readarr.models.book_resource import BookResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookResource from a JSON string
book_resource_instance = BookResource.from_json(json)
# print the JSON string representation of the object
print(BookResource.to_json())

# convert the object into a dict
book_resource_dict = book_resource_instance.to_dict()
# create an instance of BookResource from a dict
book_resource_from_dict = BookResource.from_dict(book_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


