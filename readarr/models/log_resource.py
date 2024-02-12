# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class LogResource(BaseModel):
    """
    LogResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    time: Optional[datetime] = None
    exception: Optional[StrictStr] = None
    exception_type: Optional[StrictStr] = Field(default=None, alias="exceptionType")
    level: Optional[StrictStr] = None
    logger: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    method: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "time", "exception", "exceptionType", "level", "logger", "message", "method"]

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
        """Create an instance of LogResource from a JSON string"""
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
        # set to None if exception (nullable) is None
        # and model_fields_set contains the field
        if self.exception is None and "exception" in self.model_fields_set:
            _dict['exception'] = None

        # set to None if exception_type (nullable) is None
        # and model_fields_set contains the field
        if self.exception_type is None and "exception_type" in self.model_fields_set:
            _dict['exceptionType'] = None

        # set to None if level (nullable) is None
        # and model_fields_set contains the field
        if self.level is None and "level" in self.model_fields_set:
            _dict['level'] = None

        # set to None if logger (nullable) is None
        # and model_fields_set contains the field
        if self.logger is None and "logger" in self.model_fields_set:
            _dict['logger'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if method (nullable) is None
        # and model_fields_set contains the field
        if self.method is None and "method" in self.model_fields_set:
            _dict['method'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LogResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "time": obj.get("time"),
            "exception": obj.get("exception"),
            "exceptionType": obj.get("exceptionType"),
            "level": obj.get("level"),
            "logger": obj.get("logger"),
            "message": obj.get("message"),
            "method": obj.get("method")
        })
        return _obj


