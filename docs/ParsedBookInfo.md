# ParsedBookInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_title** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_title_info** | [**AuthorTitleInfo**](AuthorTitleInfo.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**release_date** | **str** |  | [optional] 
**discography** | **bool** |  | [optional] 
**discography_start** | **int** |  | [optional] 
**discography_end** | **int** |  | [optional] 
**release_group** | **str** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**release_version** | **str** |  | [optional] 
**release_title** | **str** |  | [optional] 

## Example

```python
from readarr.models.parsed_book_info import ParsedBookInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParsedBookInfo from a JSON string
parsed_book_info_instance = ParsedBookInfo.from_json(json)
# print the JSON string representation of the object
print ParsedBookInfo.to_json()

# convert the object into a dict
parsed_book_info_dict = parsed_book_info_instance.to_dict()
# create an instance of ParsedBookInfo from a dict
parsed_book_info_form_dict = parsed_book_info.from_dict(parsed_book_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


