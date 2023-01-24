# RetagBookResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_id** | **int** |  | [optional] 
**book_id** | **int** |  | [optional] 
**track_numbers** | **List[int]** |  | [optional] 
**book_file_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**changes** | [**List[TagDifference]**](TagDifference.md) |  | [optional] 

## Example

```python
from readarr.models.retag_book_resource import RetagBookResource

# TODO update the JSON string below
json = "{}"
# create an instance of RetagBookResource from a JSON string
retag_book_resource_instance = RetagBookResource.from_json(json)
# print the JSON string representation of the object
print RetagBookResource.to_json()

# convert the object into a dict
retag_book_resource_dict = retag_book_resource_instance.to_dict()
# create an instance of RetagBookResource from a dict
retag_book_resource_form_dict = retag_book_resource.from_dict(retag_book_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


