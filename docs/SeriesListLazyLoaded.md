# SeriesListLazyLoaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Series]**](Series.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.series_list_lazy_loaded import SeriesListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesListLazyLoaded from a JSON string
series_list_lazy_loaded_instance = SeriesListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print SeriesListLazyLoaded.to_json()

# convert the object into a dict
series_list_lazy_loaded_dict = series_list_lazy_loaded_instance.to_dict()
# create an instance of SeriesListLazyLoaded from a dict
series_list_lazy_loaded_form_dict = series_list_lazy_loaded.from_dict(series_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


