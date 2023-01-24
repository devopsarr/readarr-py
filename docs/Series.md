# Series


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foreign_series_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**numbered** | **bool** |  | [optional] 
**work_count** | **int** |  | [optional] 
**primary_work_count** | **int** |  | [optional] 
**link_items** | [**SeriesBookLinkListLazyLoaded**](SeriesBookLinkListLazyLoaded.md) |  | [optional] 
**books** | [**BookListLazyLoaded**](BookListLazyLoaded.md) |  | [optional] 
**foreign_author_id** | **str** |  | [optional] 

## Example

```python
from readarr.models.series import Series

# TODO update the JSON string below
json = "{}"
# create an instance of Series from a JSON string
series_instance = Series.from_json(json)
# print the JSON string representation of the object
print Series.to_json()

# convert the object into a dict
series_dict = series_instance.to_dict()
# create an instance of Series from a dict
series_form_dict = series.from_dict(series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


