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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from readarr.models.apply_tags import ApplyTags
from readarr.models.new_item_monitor_types import NewItemMonitorTypes
from typing import Optional, Set
from typing_extensions import Self

class AuthorEditorResource(BaseModel):
    """
    AuthorEditorResource
    """ # noqa: E501
    author_ids: Optional[List[StrictInt]] = Field(default=None, alias="authorIds")
    monitored: Optional[StrictBool] = None
    monitor_new_items: Optional[NewItemMonitorTypes] = Field(default=None, alias="monitorNewItems")
    quality_profile_id: Optional[StrictInt] = Field(default=None, alias="qualityProfileId")
    metadata_profile_id: Optional[StrictInt] = Field(default=None, alias="metadataProfileId")
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    tags: Optional[List[StrictInt]] = None
    apply_tags: Optional[ApplyTags] = Field(default=None, alias="applyTags")
    move_files: Optional[StrictBool] = Field(default=None, alias="moveFiles")
    delete_files: Optional[StrictBool] = Field(default=None, alias="deleteFiles")
    __properties: ClassVar[List[str]] = ["authorIds", "monitored", "monitorNewItems", "qualityProfileId", "metadataProfileId", "rootFolderPath", "tags", "applyTags", "moveFiles", "deleteFiles"]

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
        """Create an instance of AuthorEditorResource from a JSON string"""
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
        # set to None if author_ids (nullable) is None
        # and model_fields_set contains the field
        if self.author_ids is None and "author_ids" in self.model_fields_set:
            _dict['authorIds'] = None

        # set to None if monitored (nullable) is None
        # and model_fields_set contains the field
        if self.monitored is None and "monitored" in self.model_fields_set:
            _dict['monitored'] = None

        # set to None if quality_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.quality_profile_id is None and "quality_profile_id" in self.model_fields_set:
            _dict['qualityProfileId'] = None

        # set to None if metadata_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_profile_id is None and "metadata_profile_id" in self.model_fields_set:
            _dict['metadataProfileId'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthorEditorResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorIds": obj.get("authorIds"),
            "monitored": obj.get("monitored"),
            "monitorNewItems": obj.get("monitorNewItems"),
            "qualityProfileId": obj.get("qualityProfileId"),
            "metadataProfileId": obj.get("metadataProfileId"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "tags": obj.get("tags"),
            "applyTags": obj.get("applyTags"),
            "moveFiles": obj.get("moveFiles"),
            "deleteFiles": obj.get("deleteFiles")
        })
        return _obj


