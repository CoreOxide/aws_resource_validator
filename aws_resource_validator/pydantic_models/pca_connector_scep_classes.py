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
from aws_resource_validator.pydantic_models.pca_connector_scep_constants import *

class ChallengeMetadataSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ChallengeMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ChallengeTypeDef(BaseModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Password: Optional[str] = None

class OpenIdConfigurationTypeDef(BaseModel):
    Issuer: Optional[str] = None
    Subject: Optional[str] = None
    Audience: Optional[str] = None

class CreateChallengeRequestRequestTypeDef(BaseModel):
    ConnectorArn: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteChallengeRequestRequestTypeDef(BaseModel):
    ChallengeArn: str

class DeleteConnectorRequestRequestTypeDef(BaseModel):
    ConnectorArn: str

class GetChallengeMetadataRequestRequestTypeDef(BaseModel):
    ChallengeArn: str

class GetChallengePasswordRequestRequestTypeDef(BaseModel):
    ChallengeArn: str

class GetConnectorRequestRequestTypeDef(BaseModel):
    ConnectorArn: str

class IntuneConfigurationTypeDef(BaseModel):
    AzureApplicationId: str
    Domain: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChallengeMetadataRequestRequestTypeDef(BaseModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateChallengeResponseTypeDef(BaseModel):
    Challenge: ChallengeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorResponseTypeDef(BaseModel):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChallengeMetadataResponseTypeDef(BaseModel):
    ChallengeMetadata: ChallengeMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChallengePasswordResponseTypeDef(BaseModel):
    Password: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChallengeMetadataResponseTypeDef(BaseModel):
    Challenges: List[ChallengeMetadataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MobileDeviceManagementTypeDef(BaseModel):
    Intune: Optional[IntuneConfigurationTypeDef] = None

class ListChallengeMetadataRequestListChallengeMetadataPaginateTypeDef(BaseModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ConnectorSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    Type: Optional[ConnectorTypeType] = None
    MobileDeviceManagement: Optional[MobileDeviceManagementTypeDef] = None
    OpenIdConfiguration: Optional[OpenIdConfigurationTypeDef] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    Endpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ConnectorTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    Type: Optional[ConnectorTypeType] = None
    MobileDeviceManagement: Optional[MobileDeviceManagementTypeDef] = None
    OpenIdConfiguration: Optional[OpenIdConfigurationTypeDef] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    Endpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class CreateConnectorRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    MobileDeviceManagement: Optional[MobileDeviceManagementTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ListConnectorsResponseTypeDef(BaseModel):
    Connectors: List[ConnectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetConnectorResponseTypeDef(BaseModel):
    Connector: ConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

