# ImportListExclusionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foreign_id** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 

## Example

```python
from readarr.models.import_list_exclusion_resource import ImportListExclusionResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListExclusionResource from a JSON string
import_list_exclusion_resource_instance = ImportListExclusionResource.from_json(json)
# print the JSON string representation of the object
print(ImportListExclusionResource.to_json())

# convert the object into a dict
import_list_exclusion_resource_dict = import_list_exclusion_resource_instance.to_dict()
# create an instance of ImportListExclusionResource from a dict
import_list_exclusion_resource_from_dict = ImportListExclusionResource.from_dict(import_list_exclusion_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


