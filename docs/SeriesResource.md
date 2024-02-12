# SeriesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**links** | [**List[SeriesBookLinkResource]**](SeriesBookLinkResource.md) |  | [optional] 

## Example

```python
from readarr.models.series_resource import SeriesResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesResource from a JSON string
series_resource_instance = SeriesResource.from_json(json)
# print the JSON string representation of the object
print SeriesResource.to_json()

# convert the object into a dict
series_resource_dict = series_resource_instance.to_dict()
# create an instance of SeriesResource from a dict
series_resource_form_dict = series_resource.from_dict(series_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


