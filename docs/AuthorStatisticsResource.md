# AuthorStatisticsResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_file_count** | **int** |  | [optional] 
**book_count** | **int** |  | [optional] 
**available_book_count** | **int** |  | [optional] 
**total_book_count** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**percent_of_books** | **float** |  | [optional] [readonly] 

## Example

```python
from readarr.models.author_statistics_resource import AuthorStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorStatisticsResource from a JSON string
author_statistics_resource_instance = AuthorStatisticsResource.from_json(json)
# print the JSON string representation of the object
print AuthorStatisticsResource.to_json()

# convert the object into a dict
author_statistics_resource_dict = author_statistics_resource_instance.to_dict()
# create an instance of AuthorStatisticsResource from a dict
author_statistics_resource_form_dict = author_statistics_resource.from_dict(author_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


