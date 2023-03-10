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





class HistoryEventType(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    UNKNOWN = 'unknown'
    GRABBED = 'grabbed'
    AUTHOR_FOLDER_IMPORTED = 'authorFolderImported'
    BOOK_FILE_IMPORTED = 'bookFileImported'
    DOWNLOAD_FAILED = 'downloadFailed'
    BOOK_FILE_DELETED = 'bookFileDeleted'
    BOOK_FILE_RENAMED = 'bookFileRenamed'
    BOOK_IMPORT_INCOMPLETE = 'bookImportIncomplete'
    DOWNLOAD_IMPORTED = 'downloadImported'
    BOOK_FILE_RETAGGED = 'bookFileRetagged'
    DOWNLOAD_IGNORED = 'downloadIgnored'

