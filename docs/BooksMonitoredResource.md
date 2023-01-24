# BooksMonitoredResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 

## Example

```python
from readarr.models.books_monitored_resource import BooksMonitoredResource

# TODO update the JSON string below
json = "{}"
# create an instance of BooksMonitoredResource from a JSON string
books_monitored_resource_instance = BooksMonitoredResource.from_json(json)
# print the JSON string representation of the object
print BooksMonitoredResource.to_json()

# convert the object into a dict
books_monitored_resource_dict = books_monitored_resource_instance.to_dict()
# create an instance of BooksMonitoredResource from a dict
books_monitored_resource_form_dict = books_monitored_resource.from_dict(books_monitored_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


