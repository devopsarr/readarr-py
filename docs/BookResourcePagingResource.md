# BookResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[BookResource]**](BookResource.md) |  | [optional] 

## Example

```python
from readarr.models.book_resource_paging_resource import BookResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookResourcePagingResource from a JSON string
book_resource_paging_resource_instance = BookResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print(BookResourcePagingResource.to_json())

# convert the object into a dict
book_resource_paging_resource_dict = book_resource_paging_resource_instance.to_dict()
# create an instance of BookResourcePagingResource from a dict
book_resource_paging_resource_form_dict = book_resource_paging_resource.from_dict(book_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


