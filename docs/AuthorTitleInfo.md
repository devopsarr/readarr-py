# AuthorTitleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**title_without_year** | **str** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from readarr.models.author_title_info import AuthorTitleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorTitleInfo from a JSON string
author_title_info_instance = AuthorTitleInfo.from_json(json)
# print the JSON string representation of the object
print AuthorTitleInfo.to_json()

# convert the object into a dict
author_title_info_dict = author_title_info_instance.to_dict()
# create an instance of AuthorTitleInfo from a dict
author_title_info_form_dict = author_title_info.from_dict(author_title_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


