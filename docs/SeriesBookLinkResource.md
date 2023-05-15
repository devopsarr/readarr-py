# SeriesBookLinkResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**position** | **str** |  | [optional] 
**series_position** | **int** |  | [optional] 
**series_id** | **int** |  | [optional] 
**book_id** | **int** |  | [optional] 

## Example

```python
from readarr.models.series_book_link_resource import SeriesBookLinkResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesBookLinkResource from a JSON string
series_book_link_resource_instance = SeriesBookLinkResource.from_json(json)
# print the JSON string representation of the object
print SeriesBookLinkResource.to_json()

# convert the object into a dict
series_book_link_resource_dict = series_book_link_resource_instance.to_dict()
# create an instance of SeriesBookLinkResource from a dict
series_book_link_resource_form_dict = series_book_link_resource.from_dict(series_book_link_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


