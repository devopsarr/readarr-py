# BlacklistResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_id** | **int** |  | [optional] 
**book_ids** | **List[int]** |  | [optional] 
**source_title** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**indexer** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**author** | [**AuthorResource**](AuthorResource.md) |  | [optional] 

## Example

```python
from readarr.models.blacklist_resource import BlacklistResource

# TODO update the JSON string below
json = "{}"
# create an instance of BlacklistResource from a JSON string
blacklist_resource_instance = BlacklistResource.from_json(json)
# print the JSON string representation of the object
print BlacklistResource.to_json()

# convert the object into a dict
blacklist_resource_dict = blacklist_resource_instance.to_dict()
# create an instance of BlacklistResource from a dict
blacklist_resource_form_dict = blacklist_resource.from_dict(blacklist_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


