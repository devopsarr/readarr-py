# MetadataProfileLazyLoaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**MetadataProfile**](MetadataProfile.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.metadata_profile_lazy_loaded import MetadataProfileLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataProfileLazyLoaded from a JSON string
metadata_profile_lazy_loaded_instance = MetadataProfileLazyLoaded.from_json(json)
# print the JSON string representation of the object
print(MetadataProfileLazyLoaded.to_json())

# convert the object into a dict
metadata_profile_lazy_loaded_dict = metadata_profile_lazy_loaded_instance.to_dict()
# create an instance of MetadataProfileLazyLoaded from a dict
metadata_profile_lazy_loaded_from_dict = MetadataProfileLazyLoaded.from_dict(metadata_profile_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


