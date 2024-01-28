# coding: utf-8

"""
    Readarr

    Readarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from readarr.models.add_book_options import AddBookOptions
from readarr.models.author_resource import AuthorResource
from readarr.models.book_statistics_resource import BookStatisticsResource
from readarr.models.edition_resource import EditionResource
from readarr.models.links import Links
from readarr.models.media_cover import MediaCover
from readarr.models.ratings import Ratings

class BookResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    title: Optional[str]
    author_title: Optional[str]
    series_title: Optional[str]
    disambiguation: Optional[str]
    overview: Optional[str]
    author_id: Optional[int]
    foreign_book_id: Optional[str]
    foreign_edition_id: Optional[str]
    title_slug: Optional[str]
    monitored: Optional[bool]
    any_edition_ok: Optional[bool]
    ratings: Optional[Ratings]
    release_date: Optional[datetime]
    page_count: Optional[int]
    genres: Optional[List]
    author: Optional[AuthorResource]
    images: Optional[List]
    links: Optional[List]
    statistics: Optional[BookStatisticsResource]
    added: Optional[datetime]
    add_options: Optional[AddBookOptions]
    remote_cover: Optional[str]
    editions: Optional[List]
    grabbed: Optional[bool]
    __properties = ["id", "title", "authorTitle", "seriesTitle", "disambiguation", "overview", "authorId", "foreignBookId", "foreignEditionId", "titleSlug", "monitored", "anyEditionOk", "ratings", "releaseDate", "pageCount", "genres", "author", "images", "links", "statistics", "added", "addOptions", "remoteCover", "editions", "grabbed"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BookResource:
        """Create an instance of BookResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in editions (list)
        _items = []
        if self.editions:
            for _item in self.editions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['editions'] = _items
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if author_title (nullable) is None
        if self.author_title is None:
            _dict['authorTitle'] = None

        # set to None if series_title (nullable) is None
        if self.series_title is None:
            _dict['seriesTitle'] = None

        # set to None if disambiguation (nullable) is None
        if self.disambiguation is None:
            _dict['disambiguation'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if foreign_book_id (nullable) is None
        if self.foreign_book_id is None:
            _dict['foreignBookId'] = None

        # set to None if foreign_edition_id (nullable) is None
        if self.foreign_edition_id is None:
            _dict['foreignEditionId'] = None

        # set to None if title_slug (nullable) is None
        if self.title_slug is None:
            _dict['titleSlug'] = None

        # set to None if release_date (nullable) is None
        if self.release_date is None:
            _dict['releaseDate'] = None

        # set to None if genres (nullable) is None
        if self.genres is None:
            _dict['genres'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if links (nullable) is None
        if self.links is None:
            _dict['links'] = None

        # set to None if added (nullable) is None
        if self.added is None:
            _dict['added'] = None

        # set to None if remote_cover (nullable) is None
        if self.remote_cover is None:
            _dict['remoteCover'] = None

        # set to None if editions (nullable) is None
        if self.editions is None:
            _dict['editions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BookResource:
        """Create an instance of BookResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return BookResource.parse_obj(obj)

        _obj = BookResource.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "author_title": obj.get("authorTitle"),
            "series_title": obj.get("seriesTitle"),
            "disambiguation": obj.get("disambiguation"),
            "overview": obj.get("overview"),
            "author_id": obj.get("authorId"),
            "foreign_book_id": obj.get("foreignBookId"),
            "foreign_edition_id": obj.get("foreignEditionId"),
            "title_slug": obj.get("titleSlug"),
            "monitored": obj.get("monitored"),
            "any_edition_ok": obj.get("anyEditionOk"),
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "release_date": obj.get("releaseDate"),
            "page_count": obj.get("pageCount"),
            "genres": obj.get("genres"),
            "author": AuthorResource.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "links": [Links.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "statistics": BookStatisticsResource.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None,
            "added": obj.get("added"),
            "add_options": AddBookOptions.from_dict(obj.get("addOptions")) if obj.get("addOptions") is not None else None,
            "remote_cover": obj.get("remoteCover"),
            "editions": [EditionResource.from_dict(_item) for _item in obj.get("editions")] if obj.get("editions") is not None else None,
            "grabbed": obj.get("grabbed")
        })
        return _obj

