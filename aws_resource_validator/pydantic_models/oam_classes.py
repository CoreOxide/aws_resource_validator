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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateSinkInputTypeDef(BaseValidatorModel):
    Name: str
    Tags: Optional[Mapping[str, str]] = None


class DeleteLinkInputTypeDef(BaseValidatorModel):
    Identifier: str


class DeleteSinkInputTypeDef(BaseValidatorModel):
    Identifier: str


class GetLinkInputTypeDef(BaseValidatorModel):
    Identifier: str


class GetSinkInputTypeDef(BaseValidatorModel):
    Identifier: str


class GetSinkPolicyInputTypeDef(BaseValidatorModel):
    SinkIdentifier: str


class LogGroupConfigurationTypeDef(BaseValidatorModel):
    Filter: str


class MetricConfigurationTypeDef(BaseValidatorModel):
    Filter: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAttachedLinksInputTypeDef(BaseValidatorModel):
    SinkIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAttachedLinksItemTypeDef(BaseValidatorModel):
    Label: Optional[str] = None
    LinkArn: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None


class ListLinksInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLinksItemTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Label: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None
    SinkArn: Optional[str] = None


class ListSinksInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSinksItemTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class PutSinkPolicyInputTypeDef(BaseValidatorModel):
    Policy: str
    SinkIdentifier: str


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class CreateSinkOutputTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSinkOutputTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSinkPolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutSinkPolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadataTypeDef


class LinkConfigurationTypeDef(BaseValidatorModel):
    LogGroupConfiguration: Optional[LogGroupConfigurationTypeDef] = None
    MetricConfiguration: Optional[MetricConfigurationTypeDef] = None


class ListAttachedLinksInputPaginateTypeDef(BaseValidatorModel):
    SinkIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLinksInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSinksInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttachedLinksOutputTypeDef(BaseValidatorModel):
    Items: List[ListAttachedLinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLinksOutputTypeDef(BaseValidatorModel):
    Items: List[ListLinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSinksOutputTypeDef(BaseValidatorModel):
    Items: List[ListSinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateLinkInputTypeDef(BaseValidatorModel):
    LabelTemplate: str
    ResourceTypes: Sequence[ResourceTypeType]
    SinkIdentifier: str
    LinkConfiguration: Optional[LinkConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateLinkOutputTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetLinkOutputTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLinkInputTypeDef(BaseValidatorModel):
    Identifier: str
    ResourceTypes: Sequence[ResourceTypeType]
    LinkConfiguration: Optional[LinkConfigurationTypeDef] = None


class UpdateLinkOutputTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


