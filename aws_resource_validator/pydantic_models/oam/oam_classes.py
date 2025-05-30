from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.oam.oam_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_sink' function.
class CreateSinkInput(BaseValidatorModel):
    Name: str
    Tags: Optional[Dict[str, str]] = None


class DeleteLinkInput(BaseValidatorModel):
    Identifier: str


class DeleteSinkInput(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_link' function.
class GetLinkInput(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_sink' function.
class GetSinkInput(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_sink_policy' function.
class GetSinkPolicyInput(BaseValidatorModel):
    SinkIdentifier: str


class LogGroupConfiguration(BaseValidatorModel):
    Filter: str


class MetricConfiguration(BaseValidatorModel):
    Filter: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_attached_links' function.
class ListAttachedLinksInput(BaseValidatorModel):
    SinkIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAttachedLinksItem(BaseValidatorModel):
    Label: Optional[str] = None
    LinkArn: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None


# This class is the input for the 'list_links' function.
class ListLinksInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLinksItem(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Label: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None
    SinkArn: Optional[str] = None


# This class is the input for the 'list_sinks' function.
class ListSinksInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSinksItem(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'put_sink_policy' function.
class PutSinkPolicyInput(BaseValidatorModel):
    Policy: str
    SinkIdentifier: str


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the output for the 'create_sink' function.
class CreateSinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sink' function.
class GetSinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sink_policy' function.
class GetSinkPolicyOutput(BaseValidatorModel):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_sink_policy' function.
class PutSinkPolicyOutput(BaseValidatorModel):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadata


class LinkConfiguration(BaseValidatorModel):
    LogGroupConfiguration: Optional[LogGroupConfiguration] = None
    MetricConfiguration: Optional[MetricConfiguration] = None


class ListAttachedLinksInputPaginate(BaseValidatorModel):
    SinkIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLinksInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSinksInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_attached_links' function.
class ListAttachedLinksOutput(BaseValidatorModel):
    Items: List[ListAttachedLinksItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_links' function.
class ListLinksOutput(BaseValidatorModel):
    Items: List[ListLinksItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_sinks' function.
class ListSinksOutput(BaseValidatorModel):
    Items: List[ListSinksItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_link' function.
class CreateLinkInput(BaseValidatorModel):
    LabelTemplate: str
    ResourceTypes: List[ResourceTypeType]
    SinkIdentifier: str
    LinkConfiguration: Optional[LinkConfiguration] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_link' function.
class CreateLinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfiguration
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_link' function.
class GetLinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfiguration
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_link' function.
class UpdateLinkInput(BaseValidatorModel):
    Identifier: str
    ResourceTypes: List[ResourceTypeType]
    LinkConfiguration: Optional[LinkConfiguration] = None


# This class is the output for the 'update_link' function.
class UpdateLinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfiguration
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
