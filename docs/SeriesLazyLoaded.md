# SeriesLazyLoaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Series**](Series.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.series_lazy_loaded import SeriesLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesLazyLoaded from a JSON string
series_lazy_loaded_instance = SeriesLazyLoaded.from_json(json)
# print the JSON string representation of the object
print(SeriesLazyLoaded.to_json())

# convert the object into a dict
series_lazy_loaded_dict = series_lazy_loaded_instance.to_dict()
# create an instance of SeriesLazyLoaded from a dict
series_lazy_loaded_from_dict = SeriesLazyLoaded.from_dict(series_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


