# BookStatisticsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_file_count** | **int** |  | [optional] 
**book_count** | **int** |  | [optional] 
**total_book_count** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**percent_of_books** | **float** |  | [optional] [readonly] 

## Example

```python
from readarr.models.book_statistics_resource import BookStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookStatisticsResource from a JSON string
book_statistics_resource_instance = BookStatisticsResource.from_json(json)
# print the JSON string representation of the object
print(BookStatisticsResource.to_json())

# convert the object into a dict
book_statistics_resource_dict = book_statistics_resource_instance.to_dict()
# create an instance of BookStatisticsResource from a dict
book_statistics_resource_from_dict = BookStatisticsResource.from_dict(book_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


