# EditionLazyLoaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Edition**](Edition.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.edition_lazy_loaded import EditionLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of EditionLazyLoaded from a JSON string
edition_lazy_loaded_instance = EditionLazyLoaded.from_json(json)
# print the JSON string representation of the object
print(EditionLazyLoaded.to_json())

# convert the object into a dict
edition_lazy_loaded_dict = edition_lazy_loaded_instance.to_dict()
# create an instance of EditionLazyLoaded from a dict
edition_lazy_loaded_from_dict = EditionLazyLoaded.from_dict(edition_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


