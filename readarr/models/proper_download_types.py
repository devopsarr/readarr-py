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





class ProperDownloadTypes(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    PREFER_AND_UPGRADE = 'preferAndUpgrade'
    DO_NOT_UPGRADE = 'doNotUpgrade'
    DO_NOT_PREFER = 'doNotPrefer'

