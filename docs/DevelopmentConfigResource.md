# DevelopmentConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**metadata_source** | **str** |  | [optional] 
**console_log_level** | **str** |  | [optional] 
**log_sql** | **bool** |  | [optional] 
**log_rotate** | **int** |  | [optional] 
**filter_sentry_events** | **bool** |  | [optional] 

## Example

```python
from readarr.models.development_config_resource import DevelopmentConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of DevelopmentConfigResource from a JSON string
development_config_resource_instance = DevelopmentConfigResource.from_json(json)
# print the JSON string representation of the object
print(DevelopmentConfigResource.to_json())

# convert the object into a dict
development_config_resource_dict = development_config_resource_instance.to_dict()
# create an instance of DevelopmentConfigResource from a dict
development_config_resource_from_dict = DevelopmentConfigResource.from_dict(development_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


