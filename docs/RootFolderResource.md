# RootFolderResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**default_metadata_profile_id** | **int** |  | [optional] 
**default_quality_profile_id** | **int** |  | [optional] 
**default_monitor_option** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 
**default_tags** | **List[int]** |  | [optional] 
**is_calibre_library** | **bool** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**url_base** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**library** | **str** |  | [optional] 
**output_format** | **str** |  | [optional] 
**output_profile** | **str** |  | [optional] 
**use_ssl** | **bool** |  | [optional] 
**accessible** | **bool** |  | [optional] 
**free_space** | **int** |  | [optional] 
**total_space** | **int** |  | [optional] 

## Example

```python
from readarr.models.root_folder_resource import RootFolderResource

# TODO update the JSON string below
json = "{}"
# create an instance of RootFolderResource from a JSON string
root_folder_resource_instance = RootFolderResource.from_json(json)
# print the JSON string representation of the object
print RootFolderResource.to_json()

# convert the object into a dict
root_folder_resource_dict = root_folder_resource_instance.to_dict()
# create an instance of RootFolderResource from a dict
root_folder_resource_form_dict = root_folder_resource.from_dict(root_folder_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


