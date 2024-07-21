from datetime import datetime
from pydantic import BaseModel
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateSinkInputRequestTypeDef(BaseModel):
    Name: str
    Tags: Optional[Mapping[str, str]] = None

class DeleteLinkInputRequestTypeDef(BaseModel):
    Identifier: str

class DeleteSinkInputRequestTypeDef(BaseModel):
    Identifier: str

class GetLinkInputRequestTypeDef(BaseModel):
    Identifier: str

class GetSinkInputRequestTypeDef(BaseModel):
    Identifier: str

class GetSinkPolicyInputRequestTypeDef(BaseModel):
    SinkIdentifier: str

class LogGroupConfigurationTypeDef(BaseModel):
    Filter: str

class MetricConfigurationTypeDef(BaseModel):
    Filter: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAttachedLinksInputRequestTypeDef(BaseModel):
    SinkIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAttachedLinksItemTypeDef(BaseModel):
    Label: Optional[str] = None
    LinkArn: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None

class ListLinksInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLinksItemTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Label: Optional[str] = None
    ResourceTypes: Optional[List[str]] = None
    SinkArn: Optional[str] = None

class ListSinksInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSinksItemTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class PutSinkPolicyInputRequestTypeDef(BaseModel):
    Policy: str
    SinkIdentifier: str

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateSinkOutputTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSinkOutputTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSinkPolicyOutputTypeDef(BaseModel):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSinkPolicyOutputTypeDef(BaseModel):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadataTypeDef

class LinkConfigurationTypeDef(BaseModel):
    LogGroupConfiguration: Optional[LogGroupConfigurationTypeDef] = None
    MetricConfiguration: Optional[MetricConfigurationTypeDef] = None

class ListAttachedLinksInputListAttachedLinksPaginateTypeDef(BaseModel):
    SinkIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLinksInputListLinksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSinksInputListSinksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedLinksOutputTypeDef(BaseModel):
    Items: List[ListAttachedLinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListLinksOutputTypeDef(BaseModel):
    Items: List[ListLinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSinksOutputTypeDef(BaseModel):
    Items: List[ListSinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateLinkInputRequestTypeDef(BaseModel):
    LabelTemplate: str
    ResourceTypes: Sequence[ResourceTypeType]
    SinkIdentifier: str
    LinkConfiguration: Optional[LinkConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateLinkOutputTypeDef(BaseModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinkOutputTypeDef(BaseModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLinkInputRequestTypeDef(BaseModel):
    Identifier: str
    ResourceTypes: Sequence[ResourceTypeType]
    LinkConfiguration: Optional[LinkConfigurationTypeDef] = None

class UpdateLinkOutputTypeDef(BaseModel):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

