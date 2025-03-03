# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.4.10.2734
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from readarr.models.add_book_options import AddBookOptions
from readarr.models.author_metadata_lazy_loaded import AuthorMetadataLazyLoaded
from readarr.models.links import Links
from readarr.models.ratings import Ratings
from typing import Optional, Set
from typing_extensions import Self

class Book(BaseModel):
    """
    Book
    """ # noqa: E501
    id: Optional[StrictInt] = None
    author_metadata_id: Optional[StrictInt] = Field(default=None, alias="authorMetadataId")
    foreign_book_id: Optional[StrictStr] = Field(default=None, alias="foreignBookId")
    foreign_edition_id: Optional[StrictStr] = Field(default=None, alias="foreignEditionId")
    title_slug: Optional[StrictStr] = Field(default=None, alias="titleSlug")
    title: Optional[StrictStr] = None
    release_date: Optional[datetime] = Field(default=None, alias="releaseDate")
    links: Optional[List[Links]] = None
    genres: Optional[List[StrictStr]] = None
    related_books: Optional[List[StrictInt]] = Field(default=None, alias="relatedBooks")
    ratings: Optional[Ratings] = None
    last_search_time: Optional[datetime] = Field(default=None, alias="lastSearchTime")
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    monitored: Optional[StrictBool] = None
    any_edition_ok: Optional[StrictBool] = Field(default=None, alias="anyEditionOk")
    last_info_sync: Optional[datetime] = Field(default=None, alias="lastInfoSync")
    added: Optional[datetime] = None
    add_options: Optional[AddBookOptions] = Field(default=None, alias="addOptions")
    author_metadata: Optional[AuthorMetadataLazyLoaded] = Field(default=None, alias="authorMetadata")
    author: Optional[AuthorLazyLoaded] = None
    editions: Optional[EditionListLazyLoaded] = None
    book_files: Optional[BookFileListLazyLoaded] = Field(default=None, alias="bookFiles")
    series_links: Optional[SeriesBookLinkListLazyLoaded] = Field(default=None, alias="seriesLinks")
    __properties: ClassVar[List[str]] = ["id", "authorMetadataId", "foreignBookId", "foreignEditionId", "titleSlug", "title", "releaseDate", "links", "genres", "relatedBooks", "ratings", "lastSearchTime", "cleanTitle", "monitored", "anyEditionOk", "lastInfoSync", "added", "addOptions", "authorMetadata", "author", "editions", "bookFiles", "seriesLinks"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Book from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of author_metadata
        if self.author_metadata:
            _dict['authorMetadata'] = self.author_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of editions
        if self.editions:
            _dict['editions'] = self.editions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of book_files
        if self.book_files:
            _dict['bookFiles'] = self.book_files.to_dict()
        # override the default output from pydantic by calling `to_dict()` of series_links
        if self.series_links:
            _dict['seriesLinks'] = self.series_links.to_dict()
        # set to None if foreign_book_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_book_id is None and "foreign_book_id" in self.model_fields_set:
            _dict['foreignBookId'] = None

        # set to None if foreign_edition_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_edition_id is None and "foreign_edition_id" in self.model_fields_set:
            _dict['foreignEditionId'] = None

        # set to None if title_slug (nullable) is None
        # and model_fields_set contains the field
        if self.title_slug is None and "title_slug" in self.model_fields_set:
            _dict['titleSlug'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if release_date (nullable) is None
        # and model_fields_set contains the field
        if self.release_date is None and "release_date" in self.model_fields_set:
            _dict['releaseDate'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if related_books (nullable) is None
        # and model_fields_set contains the field
        if self.related_books is None and "related_books" in self.model_fields_set:
            _dict['relatedBooks'] = None

        # set to None if last_search_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_search_time is None and "last_search_time" in self.model_fields_set:
            _dict['lastSearchTime'] = None

        # set to None if clean_title (nullable) is None
        # and model_fields_set contains the field
        if self.clean_title is None and "clean_title" in self.model_fields_set:
            _dict['cleanTitle'] = None

        # set to None if last_info_sync (nullable) is None
        # and model_fields_set contains the field
        if self.last_info_sync is None and "last_info_sync" in self.model_fields_set:
            _dict['lastInfoSync'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Book from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "authorMetadataId": obj.get("authorMetadataId"),
            "foreignBookId": obj.get("foreignBookId"),
            "foreignEditionId": obj.get("foreignEditionId"),
            "titleSlug": obj.get("titleSlug"),
            "title": obj.get("title"),
            "releaseDate": obj.get("releaseDate"),
            "links": [Links.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "genres": obj.get("genres"),
            "relatedBooks": obj.get("relatedBooks"),
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "lastSearchTime": obj.get("lastSearchTime"),
            "cleanTitle": obj.get("cleanTitle"),
            "monitored": obj.get("monitored"),
            "anyEditionOk": obj.get("anyEditionOk"),
            "lastInfoSync": obj.get("lastInfoSync"),
            "added": obj.get("added"),
            "addOptions": AddBookOptions.from_dict(obj["addOptions"]) if obj.get("addOptions") is not None else None,
            "authorMetadata": AuthorMetadataLazyLoaded.from_dict(obj["authorMetadata"]) if obj.get("authorMetadata") is not None else None,
            "author": AuthorLazyLoaded.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "editions": EditionListLazyLoaded.from_dict(obj["editions"]) if obj.get("editions") is not None else None,
            "bookFiles": BookFileListLazyLoaded.from_dict(obj["bookFiles"]) if obj.get("bookFiles") is not None else None,
            "seriesLinks": SeriesBookLinkListLazyLoaded.from_dict(obj["seriesLinks"]) if obj.get("seriesLinks") is not None else None
        })
        return _obj

from readarr.models.author_lazy_loaded import AuthorLazyLoaded
from readarr.models.book_file_list_lazy_loaded import BookFileListLazyLoaded
from readarr.models.edition_list_lazy_loaded import EditionListLazyLoaded
from readarr.models.series_book_link_list_lazy_loaded import SeriesBookLinkListLazyLoaded
# TODO: Rewrite to not use raise_errors
Book.model_rebuild(raise_errors=False)

