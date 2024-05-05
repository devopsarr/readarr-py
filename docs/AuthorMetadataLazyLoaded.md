# AuthorMetadataLazyLoaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**AuthorMetadata**](AuthorMetadata.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.author_metadata_lazy_loaded import AuthorMetadataLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorMetadataLazyLoaded from a JSON string
author_metadata_lazy_loaded_instance = AuthorMetadataLazyLoaded.from_json(json)
# print the JSON string representation of the object
print(AuthorMetadataLazyLoaded.to_json())

# convert the object into a dict
author_metadata_lazy_loaded_dict = author_metadata_lazy_loaded_instance.to_dict()
# create an instance of AuthorMetadataLazyLoaded from a dict
author_metadata_lazy_loaded_from_dict = AuthorMetadataLazyLoaded.from_dict(author_metadata_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


