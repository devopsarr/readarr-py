# BlacklistResourcePagingResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**filters** | [**List[PagingResourceFilter]**](PagingResourceFilter.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[BlacklistResource]**](BlacklistResource.md) |  | [optional] 

## Example

```python
from readarr.models.blacklist_resource_paging_resource import BlacklistResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of BlacklistResourcePagingResource from a JSON string
blacklist_resource_paging_resource_instance = BlacklistResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print BlacklistResourcePagingResource.to_json()

# convert the object into a dict
blacklist_resource_paging_resource_dict = blacklist_resource_paging_resource_instance.to_dict()
# create an instance of BlacklistResourcePagingResource from a dict
blacklist_resource_paging_resource_form_dict = blacklist_resource_paging_resource.from_dict(blacklist_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


