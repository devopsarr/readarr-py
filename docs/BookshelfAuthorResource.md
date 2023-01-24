# BookshelfAuthorResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**books** | [**List[BookResource]**](BookResource.md) |  | [optional] 

## Example

```python
from readarr.models.bookshelf_author_resource import BookshelfAuthorResource

# TODO update the JSON string below
json = "{}"
# create an instance of BookshelfAuthorResource from a JSON string
bookshelf_author_resource_instance = BookshelfAuthorResource.from_json(json)
# print the JSON string representation of the object
print BookshelfAuthorResource.to_json()

# convert the object into a dict
bookshelf_author_resource_dict = bookshelf_author_resource_instance.to_dict()
# create an instance of BookshelfAuthorResource from a dict
bookshelf_author_resource_form_dict = bookshelf_author_resource.from_dict(bookshelf_author_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


