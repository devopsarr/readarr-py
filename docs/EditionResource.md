# EditionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**book_id** | **int** |  | [optional] 
**foreign_edition_id** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**isbn13** | **str** |  | [optional] 
**asin** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**is_ebook** | **bool** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**publisher** | **str** |  | [optional] 
**page_count** | **int** |  | [optional] 
**release_date** | **datetime** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**monitored** | **bool** |  | [optional] 
**manual_add** | **bool** |  | [optional] 
**remote_cover** | **str** |  | [optional] 

## Example

```python
from readarr.models.edition_resource import EditionResource

# TODO update the JSON string below
json = "{}"
# create an instance of EditionResource from a JSON string
edition_resource_instance = EditionResource.from_json(json)
# print the JSON string representation of the object
print(EditionResource.to_json())

# convert the object into a dict
edition_resource_dict = edition_resource_instance.to_dict()
# create an instance of EditionResource from a dict
edition_resource_from_dict = EditionResource.from_dict(edition_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


