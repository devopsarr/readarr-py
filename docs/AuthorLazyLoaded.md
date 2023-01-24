# AuthorLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Author**](Author.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.author_lazy_loaded import AuthorLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorLazyLoaded from a JSON string
author_lazy_loaded_instance = AuthorLazyLoaded.from_json(json)
# print the JSON string representation of the object
print AuthorLazyLoaded.to_json()

# convert the object into a dict
author_lazy_loaded_dict = author_lazy_loaded_instance.to_dict()
# create an instance of AuthorLazyLoaded from a dict
author_lazy_loaded_form_dict = author_lazy_loaded.from_dict(author_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


