# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.4.10.2734
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ImportListType(str, Enum):
    """
    ImportListType
    """

    """
    allowed enum values
    """
    PROGRAM = 'program'
    GOODREADS = 'goodreads'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ImportListType from a JSON string"""
        return cls(json.loads(json_str))


