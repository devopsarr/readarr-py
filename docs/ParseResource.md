# ParseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**parsed_book_info** | [**ParsedBookInfo**](ParsedBookInfo.md) |  | [optional] 
**author** | [**AuthorResource**](AuthorResource.md) |  | [optional] 
**books** | [**List[BookResource]**](BookResource.md) |  | [optional] 

## Example

```python
from readarr.models.parse_resource import ParseResource

# TODO update the JSON string below
json = "{}"
# create an instance of ParseResource from a JSON string
parse_resource_instance = ParseResource.from_json(json)
# print the JSON string representation of the object
print(ParseResource.to_json())

# convert the object into a dict
parse_resource_dict = parse_resource_instance.to_dict()
# create an instance of ParseResource from a dict
parse_resource_from_dict = ParseResource.from_dict(parse_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


