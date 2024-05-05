# SeriesBookLinkListLazyLoaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SeriesBookLink]**](SeriesBookLink.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.series_book_link_list_lazy_loaded import SeriesBookLinkListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesBookLinkListLazyLoaded from a JSON string
series_book_link_list_lazy_loaded_instance = SeriesBookLinkListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print(SeriesBookLinkListLazyLoaded.to_json())

# convert the object into a dict
series_book_link_list_lazy_loaded_dict = series_book_link_list_lazy_loaded_instance.to_dict()
# create an instance of SeriesBookLinkListLazyLoaded from a dict
series_book_link_list_lazy_loaded_from_dict = SeriesBookLinkListLazyLoaded.from_dict(series_book_link_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


