# BookFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**date_added** | **datetime** |  | [optional] 
**original_file_path** | **str** |  | [optional] 
**scene_name** | **str** |  | [optional] 
**release_group** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**media_info** | [**MediaInfoModel**](MediaInfoModel.md) |  | [optional] 
**edition_id** | **int** |  | [optional] 
**calibre_id** | **int** |  | [optional] 
**part** | **int** |  | [optional] 
**author** | [**AuthorLazyLoaded**](AuthorLazyLoaded.md) |  | [optional] 
**edition** | [**EditionLazyLoaded**](EditionLazyLoaded.md) |  | [optional] 
**part_count** | **int** |  | [optional] 

## Example

```python
from readarr.models.book_file import BookFile

# TODO update the JSON string below
json = "{}"
# create an instance of BookFile from a JSON string
book_file_instance = BookFile.from_json(json)
# print the JSON string representation of the object
print BookFile.to_json()

# convert the object into a dict
book_file_dict = book_file_instance.to_dict()
# create an instance of BookFile from a dict
book_file_form_dict = book_file.from_dict(book_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


