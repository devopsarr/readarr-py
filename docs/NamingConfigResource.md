# NamingConfigResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**rename_books** | **bool** |  | [optional] 
**replace_illegal_characters** | **bool** |  | [optional] 
**standard_book_format** | **str** |  | [optional] 
**author_folder_format** | **str** |  | [optional] 
**include_author_name** | **bool** |  | [optional] 
**include_book_title** | **bool** |  | [optional] 
**include_quality** | **bool** |  | [optional] 
**replace_spaces** | **bool** |  | [optional] 
**separator** | **str** |  | [optional] 
**number_style** | **str** |  | [optional] 

## Example

```python
from readarr.models.naming_config_resource import NamingConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of NamingConfigResource from a JSON string
naming_config_resource_instance = NamingConfigResource.from_json(json)
# print the JSON string representation of the object
print NamingConfigResource.to_json()

# convert the object into a dict
naming_config_resource_dict = naming_config_resource_instance.to_dict()
# create an instance of NamingConfigResource from a dict
naming_config_resource_form_dict = naming_config_resource.from_dict(naming_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


