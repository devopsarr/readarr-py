# SeriesBookLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**position** | **str** |  | [optional] 
**series_position** | **int** |  | [optional] 
**series_id** | **int** |  | [optional] 
**book_id** | **int** |  | [optional] 
**is_primary** | **bool** |  | [optional] 
**series** | [**SeriesLazyLoaded**](SeriesLazyLoaded.md) |  | [optional] 
**book** | [**BookLazyLoaded**](BookLazyLoaded.md) |  | [optional] 

## Example

```python
from readarr.models.series_book_link import SeriesBookLink

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesBookLink from a JSON string
series_book_link_instance = SeriesBookLink.from_json(json)
# print the JSON string representation of the object
print SeriesBookLink.to_json()

# convert the object into a dict
series_book_link_dict = series_book_link_instance.to_dict()
# create an instance of SeriesBookLink from a dict
series_book_link_form_dict = series_book_link.from_dict(series_book_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


