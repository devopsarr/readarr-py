# Book


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_metadata_id** | **int** |  | [optional] 
**foreign_book_id** | **str** |  | [optional] 
**foreign_edition_id** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**release_date** | **datetime** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**related_books** | **List[int]** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**clean_title** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**any_edition_ok** | **bool** |  | [optional] 
**last_info_sync** | **datetime** |  | [optional] 
**added** | **datetime** |  | [optional] 
**add_options** | [**AddBookOptions**](AddBookOptions.md) |  | [optional] 
**author_metadata** | [**AuthorMetadataLazyLoaded**](AuthorMetadataLazyLoaded.md) |  | [optional] 
**author** | [**AuthorLazyLoaded**](AuthorLazyLoaded.md) |  | [optional] 
**editions** | [**EditionListLazyLoaded**](EditionListLazyLoaded.md) |  | [optional] 
**book_files** | [**BookFileListLazyLoaded**](BookFileListLazyLoaded.md) |  | [optional] 
**series_links** | [**SeriesBookLinkListLazyLoaded**](SeriesBookLinkListLazyLoaded.md) |  | [optional] 

## Example

```python
from readarr.models.book import Book

# TODO update the JSON string below
json = "{}"
# create an instance of Book from a JSON string
book_instance = Book.from_json(json)
# print the JSON string representation of the object
print Book.to_json()

# convert the object into a dict
book_dict = book_instance.to_dict()
# create an instance of Book from a dict
book_form_dict = book.from_dict(book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


