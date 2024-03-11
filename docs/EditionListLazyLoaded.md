# EditionListLazyLoaded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Edition]**](Edition.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from readarr.models.edition_list_lazy_loaded import EditionListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of EditionListLazyLoaded from a JSON string
edition_list_lazy_loaded_instance = EditionListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print(EditionListLazyLoaded.to_json())

# convert the object into a dict
edition_list_lazy_loaded_dict = edition_list_lazy_loaded_instance.to_dict()
# create an instance of EditionListLazyLoaded from a dict
edition_list_lazy_loaded_form_dict = edition_list_lazy_loaded.from_dict(edition_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


