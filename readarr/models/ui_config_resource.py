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


from typing import Any, Dict, Optional
from pydantic import BaseModel

class UiConfigResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    first_day_of_week: Optional[int]
    calendar_week_column_header: Optional[str]
    short_date_format: Optional[str]
    long_date_format: Optional[str]
    time_format: Optional[str]
    show_relative_dates: Optional[bool]
    enable_color_impaired_mode: Optional[bool]
    ui_language: Optional[int]
    theme: Optional[str]
    __properties = ["id", "firstDayOfWeek", "calendarWeekColumnHeader", "shortDateFormat", "longDateFormat", "timeFormat", "showRelativeDates", "enableColorImpairedMode", "uiLanguage", "theme"]

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
    def from_json(cls, json_str: str) -> UiConfigResource:
        """Create an instance of UiConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if calendar_week_column_header (nullable) is None
        if self.calendar_week_column_header is None:
            _dict['calendarWeekColumnHeader'] = None

        # set to None if short_date_format (nullable) is None
        if self.short_date_format is None:
            _dict['shortDateFormat'] = None

        # set to None if long_date_format (nullable) is None
        if self.long_date_format is None:
            _dict['longDateFormat'] = None

        # set to None if time_format (nullable) is None
        if self.time_format is None:
            _dict['timeFormat'] = None

        # set to None if theme (nullable) is None
        if self.theme is None:
            _dict['theme'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UiConfigResource:
        """Create an instance of UiConfigResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UiConfigResource.parse_obj(obj)

        _obj = UiConfigResource.parse_obj({
            "id": obj.get("id"),
            "first_day_of_week": obj.get("firstDayOfWeek"),
            "calendar_week_column_header": obj.get("calendarWeekColumnHeader"),
            "short_date_format": obj.get("shortDateFormat"),
            "long_date_format": obj.get("longDateFormat"),
            "time_format": obj.get("timeFormat"),
            "show_relative_dates": obj.get("showRelativeDates"),
            "enable_color_impaired_mode": obj.get("enableColorImpairedMode"),
            "ui_language": obj.get("uiLanguage"),
            "theme": obj.get("theme")
        })
        return _obj

