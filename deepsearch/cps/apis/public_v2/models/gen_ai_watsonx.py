# coding: utf-8

"""
    Deep Search (DS) API

    API for Deep Search.  **WARNING**: This API is subject to change without warning!

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from deepsearch.cps.apis.public_v2.models.gen_ai_watsonx_config import GenAIWatsonxConfig
from deepsearch.cps.apis.public_v2.models.gen_aiaws_bedrock_proj_params import GenAIAWSBedrockProjParams
from typing import Optional, Set
from typing_extensions import Self

class GenAIWatsonx(BaseModel):
    """
    GenAI integration for watsonx settings
    """ # noqa: E501
    kind: Optional[StrictStr] = 'watsonx'
    config: GenAIWatsonxConfig
    proj_params: Optional[GenAIAWSBedrockProjParams] = None
    __properties: ClassVar[List[str]] = ["kind", "config", "proj_params"]

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
        """Create an instance of GenAIWatsonx from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proj_params
        if self.proj_params:
            _dict['proj_params'] = self.proj_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenAIWatsonx from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kind": obj.get("kind") if obj.get("kind") is not None else 'watsonx',
            "config": GenAIWatsonxConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "proj_params": GenAIAWSBedrockProjParams.from_dict(obj["proj_params"]) if obj.get("proj_params") is not None else None
        })
        return _obj


