# TagDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**delay_profile_ids** | **List[int]** |  | [optional] 
**import_list_ids** | **List[int]** |  | [optional] 
**notification_ids** | **List[int]** |  | [optional] 
**restriction_ids** | **List[int]** |  | [optional] 
**indexer_ids** | **List[int]** |  | [optional] 
**download_client_ids** | **List[int]** |  | [optional] 
**author_ids** | **List[int]** |  | [optional] 

## Example

```python
from readarr.models.tag_details_resource import TagDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of TagDetailsResource from a JSON string
tag_details_resource_instance = TagDetailsResource.from_json(json)
# print the JSON string representation of the object
print(TagDetailsResource.to_json())

# convert the object into a dict
tag_details_resource_dict = tag_details_resource_instance.to_dict()
# create an instance of TagDetailsResource from a dict
tag_details_resource_from_dict = TagDetailsResource.from_dict(tag_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


