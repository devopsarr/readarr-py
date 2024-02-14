# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.3.18.2411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from readarr.models.links import Links
from readarr.models.media_cover import MediaCover
from readarr.models.ratings import Ratings
from typing import Optional, Set
from typing_extensions import Self

class EditionResource(BaseModel):
    """
    EditionResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    book_id: Optional[StrictInt] = Field(default=None, alias="bookId")
    foreign_edition_id: Optional[StrictStr] = Field(default=None, alias="foreignEditionId")
    title_slug: Optional[StrictStr] = Field(default=None, alias="titleSlug")
    isbn13: Optional[StrictStr] = None
    asin: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    format: Optional[StrictStr] = None
    is_ebook: Optional[StrictBool] = Field(default=None, alias="isEbook")
    disambiguation: Optional[StrictStr] = None
    publisher: Optional[StrictStr] = None
    page_count: Optional[StrictInt] = Field(default=None, alias="pageCount")
    release_date: Optional[datetime] = Field(default=None, alias="releaseDate")
    images: Optional[List[MediaCover]] = None
    links: Optional[List[Links]] = None
    ratings: Optional[Ratings] = None
    monitored: Optional[StrictBool] = None
    manual_add: Optional[StrictBool] = Field(default=None, alias="manualAdd")
    remote_cover: Optional[StrictStr] = Field(default=None, alias="remoteCover")
    grabbed: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "bookId", "foreignEditionId", "titleSlug", "isbn13", "asin", "title", "language", "overview", "format", "isEbook", "disambiguation", "publisher", "pageCount", "releaseDate", "images", "links", "ratings", "monitored", "manualAdd", "remoteCover", "grabbed"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EditionResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # set to None if foreign_edition_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_edition_id is None and "foreign_edition_id" in self.model_fields_set:
            _dict['foreignEditionId'] = None

        # set to None if title_slug (nullable) is None
        # and model_fields_set contains the field
        if self.title_slug is None and "title_slug" in self.model_fields_set:
            _dict['titleSlug'] = None

        # set to None if isbn13 (nullable) is None
        # and model_fields_set contains the field
        if self.isbn13 is None and "isbn13" in self.model_fields_set:
            _dict['isbn13'] = None

        # set to None if asin (nullable) is None
        # and model_fields_set contains the field
        if self.asin is None and "asin" in self.model_fields_set:
            _dict['asin'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if overview (nullable) is None
        # and model_fields_set contains the field
        if self.overview is None and "overview" in self.model_fields_set:
            _dict['overview'] = None

        # set to None if format (nullable) is None
        # and model_fields_set contains the field
        if self.format is None and "format" in self.model_fields_set:
            _dict['format'] = None

        # set to None if disambiguation (nullable) is None
        # and model_fields_set contains the field
        if self.disambiguation is None and "disambiguation" in self.model_fields_set:
            _dict['disambiguation'] = None

        # set to None if publisher (nullable) is None
        # and model_fields_set contains the field
        if self.publisher is None and "publisher" in self.model_fields_set:
            _dict['publisher'] = None

        # set to None if release_date (nullable) is None
        # and model_fields_set contains the field
        if self.release_date is None and "release_date" in self.model_fields_set:
            _dict['releaseDate'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if remote_cover (nullable) is None
        # and model_fields_set contains the field
        if self.remote_cover is None and "remote_cover" in self.model_fields_set:
            _dict['remoteCover'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EditionResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "bookId": obj.get("bookId"),
            "foreignEditionId": obj.get("foreignEditionId"),
            "titleSlug": obj.get("titleSlug"),
            "isbn13": obj.get("isbn13"),
            "asin": obj.get("asin"),
            "title": obj.get("title"),
            "language": obj.get("language"),
            "overview": obj.get("overview"),
            "format": obj.get("format"),
            "isEbook": obj.get("isEbook"),
            "disambiguation": obj.get("disambiguation"),
            "publisher": obj.get("publisher"),
            "pageCount": obj.get("pageCount"),
            "releaseDate": obj.get("releaseDate"),
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "links": [Links.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "monitored": obj.get("monitored"),
            "manualAdd": obj.get("manualAdd"),
            "remoteCover": obj.get("remoteCover"),
            "grabbed": obj.get("grabbed")
        })
        return _obj


