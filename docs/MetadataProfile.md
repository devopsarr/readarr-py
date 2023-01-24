# MetadataProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**min_popularity** | **float** |  | [optional] 
**skip_missing_date** | **bool** |  | [optional] 
**skip_missing_isbn** | **bool** |  | [optional] 
**skip_parts_and_sets** | **bool** |  | [optional] 
**skip_series_secondary** | **bool** |  | [optional] 
**allowed_languages** | **str** |  | [optional] 
**min_pages** | **int** |  | [optional] 
**ignored** | **str** |  | [optional] 

## Example

```python
from readarr.models.metadata_profile import MetadataProfile

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataProfile from a JSON string
metadata_profile_instance = MetadataProfile.from_json(json)
# print the JSON string representation of the object
print MetadataProfile.to_json()

# convert the object into a dict
metadata_profile_dict = metadata_profile_instance.to_dict()
# create an instance of MetadataProfile from a dict
metadata_profile_form_dict = metadata_profile.from_dict(metadata_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


