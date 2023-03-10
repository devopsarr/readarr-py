# coding: utf-8

"""
    Readarr

    Readarr API docs  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from readarr.models.author_status_type import AuthorStatusType
from readarr.models.links import Links
from readarr.models.media_cover import MediaCover
from readarr.models.ratings import Ratings

class AuthorMetadata(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    foreign_author_id: Optional[str]
    title_slug: Optional[str]
    name: Optional[str]
    sort_name: Optional[str]
    name_last_first: Optional[str]
    sort_name_last_first: Optional[str]
    aliases: Optional[List]
    overview: Optional[str]
    disambiguation: Optional[str]
    gender: Optional[str]
    hometown: Optional[str]
    born: Optional[datetime]
    died: Optional[datetime]
    status: Optional[AuthorStatusType]
    images: Optional[List]
    links: Optional[List]
    genres: Optional[List]
    ratings: Optional[Ratings]
    __properties = ["id", "foreignAuthorId", "titleSlug", "name", "sortName", "nameLastFirst", "sortNameLastFirst", "aliases", "overview", "disambiguation", "gender", "hometown", "born", "died", "status", "images", "links", "genres", "ratings"]

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
    def from_json(cls, json_str: str) -> AuthorMetadata:
        """Create an instance of AuthorMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
        # set to None if foreign_author_id (nullable) is None
        if self.foreign_author_id is None:
            _dict['foreignAuthorId'] = None

        # set to None if title_slug (nullable) is None
        if self.title_slug is None:
            _dict['titleSlug'] = None

        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if sort_name (nullable) is None
        if self.sort_name is None:
            _dict['sortName'] = None

        # set to None if name_last_first (nullable) is None
        if self.name_last_first is None:
            _dict['nameLastFirst'] = None

        # set to None if sort_name_last_first (nullable) is None
        if self.sort_name_last_first is None:
            _dict['sortNameLastFirst'] = None

        # set to None if aliases (nullable) is None
        if self.aliases is None:
            _dict['aliases'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if disambiguation (nullable) is None
        if self.disambiguation is None:
            _dict['disambiguation'] = None

        # set to None if gender (nullable) is None
        if self.gender is None:
            _dict['gender'] = None

        # set to None if hometown (nullable) is None
        if self.hometown is None:
            _dict['hometown'] = None

        # set to None if born (nullable) is None
        if self.born is None:
            _dict['born'] = None

        # set to None if died (nullable) is None
        if self.died is None:
            _dict['died'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if links (nullable) is None
        if self.links is None:
            _dict['links'] = None

        # set to None if genres (nullable) is None
        if self.genres is None:
            _dict['genres'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthorMetadata:
        """Create an instance of AuthorMetadata from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AuthorMetadata.parse_obj(obj)

        _obj = AuthorMetadata.parse_obj({
            "id": obj.get("id"),
            "foreign_author_id": obj.get("foreignAuthorId"),
            "title_slug": obj.get("titleSlug"),
            "name": obj.get("name"),
            "sort_name": obj.get("sortName"),
            "name_last_first": obj.get("nameLastFirst"),
            "sort_name_last_first": obj.get("sortNameLastFirst"),
            "aliases": obj.get("aliases"),
            "overview": obj.get("overview"),
            "disambiguation": obj.get("disambiguation"),
            "gender": obj.get("gender"),
            "hometown": obj.get("hometown"),
            "born": obj.get("born"),
            "died": obj.get("died"),
            "status": obj.get("status"),
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "links": [Links.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "genres": obj.get("genres"),
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None
        })
        return _obj

