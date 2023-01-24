# BookFileResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_id** | **int** |  | [optional] 
**book_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**date_added** | **datetime** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**quality_weight** | **int** |  | [optional] 
**media_info** | [**MediaInfoResource**](MediaInfoResource.md) |  | [optional] 
**quality_cutoff_not_met** | **bool** |  | [optional] 
**audio_tags** | [**ParsedTrackInfo**](ParsedTrackInfo.md) |  | [optional] 

## Example

```python
from readarr.models.book_file_resource import BookFileResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookFileResource from a JSON string
book_file_resource_instance = BookFileResource.from_json(json)
# print the JSON string representation of the object
print BookFileResource.to_json()

# convert the object into a dict
book_file_resource_dict = book_file_resource_instance.to_dict()
# create an instance of BookFileResource from a dict
book_file_resource_form_dict = book_file_resource.from_dict(book_file_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


