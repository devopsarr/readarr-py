# BookshelfResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authors** | [**List[BookshelfAuthorResource]**](BookshelfAuthorResource.md) |  | [optional] 
**monitoring_options** | [**MonitoringOptions**](MonitoringOptions.md) |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 

## Example

```python
from readarr.models.bookshelf_resource import BookshelfResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookshelfResource from a JSON string
bookshelf_resource_instance = BookshelfResource.from_json(json)
# print the JSON string representation of the object
print(BookshelfResource.to_json())

# convert the object into a dict
bookshelf_resource_dict = bookshelf_resource_instance.to_dict()
# create an instance of BookshelfResource from a dict
bookshelf_resource_from_dict = BookshelfResource.from_dict(bookshelf_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


