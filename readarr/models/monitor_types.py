# coding: utf-8

"""
    Readarr

    Readarr API docs  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class MonitorTypes(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    ALL = 'all'
    FUTURE = 'future'
    MISSING = 'missing'
    EXISTING = 'existing'
    LATEST = 'latest'
    FIRST = 'first'
    var_NONE = 'none'
    UNKNOWN = 'unknown'

