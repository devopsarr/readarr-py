# MetadataProfileResource


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
**ignored** | **List[str]** |  | [optional] 

## Example

```python
from readarr.models.metadata_profile_resource import MetadataProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataProfileResource from a JSON string
metadata_profile_resource_instance = MetadataProfileResource.from_json(json)
# print the JSON string representation of the object
print(MetadataProfileResource.to_json())

# convert the object into a dict
metadata_profile_resource_dict = metadata_profile_resource_instance.to_dict()
# create an instance of MetadataProfileResource from a dict
metadata_profile_resource_form_dict = metadata_profile_resource.from_dict(metadata_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


