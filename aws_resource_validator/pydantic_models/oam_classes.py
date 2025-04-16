from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.oam_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateSinkInput(BaseValidatorModel):
    Name: str
    Tags: Optional[Mapping[str, str]] = None


class DeleteLinkInput(BaseValidatorModel):
    Identifier: str


class DeleteSinkInput(BaseValidatorModel):
    Identifier: str


class GetLinkInput(BaseValidatorModel):
    Identifier: str


class GetSinkInput(BaseValidatorModel):
    Identifier: str


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


class ListAttachedLinksInput(BaseValidatorModel):
    SinkIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAttachedLinksItem(BaseValidatorModel):
    Label: Optional[str] = None
    LinkArn: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None


class ListLinksInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLinksItem(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Label: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None
    SinkArn: Optional[str] = None


class ListSinksInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSinksItem(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class PutSinkPolicyInput(BaseValidatorModel):
    Policy: str
    SinkIdentifier: str


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class CreateSinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSinkPolicyOutput(BaseValidatorModel):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


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


class ListAttachedLinksOutput(BaseValidatorModel):
    Items: List[ListAttachedLinksItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLinksOutput(BaseValidatorModel):
    Items: List[ListLinksItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSinksOutput(BaseValidatorModel):
    Items: List[ListSinksItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateLinkInput(BaseValidatorModel):
    LabelTemplate: str
    ResourceTypes: Sequence[ResourceTypeType]
    SinkIdentifier: str
    LinkConfiguration: Optional[LinkConfiguration] = None
    Tags: Optional[Mapping[str, str]] = None


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


class UpdateLinkInput(BaseValidatorModel):
    Identifier: str
    ResourceTypes: Sequence[ResourceTypeType]
    LinkConfiguration: Optional[LinkConfiguration] = None


class UpdateLinkOutput(BaseValidatorModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfiguration
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


