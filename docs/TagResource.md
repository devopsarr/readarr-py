# TagResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from readarr.models.tag_resource import TagResource

# TODO update the JSON string below
json = "{}"
# create an instance of TagResource from a JSON string
tag_resource_instance = TagResource.from_json(json)
# print the JSON string representation of the object
print(TagResource.to_json())

# convert the object into a dict
tag_resource_dict = tag_resource_instance.to_dict()
# create an instance of TagResource from a dict
tag_resource_from_dict = TagResource.from_dict(tag_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


