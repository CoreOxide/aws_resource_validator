from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ChallengeMetadataSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ChallengeMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ChallengeTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Password: Optional[str] = None

class OpenIdConfigurationTypeDef(BaseValidatorModel):
    Issuer: Optional[str] = None
    Subject: Optional[str] = None
    Audience: Optional[str] = None

class CreateChallengeRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteChallengeRequestRequestTypeDef(BaseValidatorModel):
    ChallengeArn: str

class DeleteConnectorRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str

class GetChallengeMetadataRequestRequestTypeDef(BaseValidatorModel):
    ChallengeArn: str

class GetChallengePasswordRequestRequestTypeDef(BaseValidatorModel):
    ChallengeArn: str

class GetConnectorRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str

class IntuneConfigurationTypeDef(BaseValidatorModel):
    AzureApplicationId: str
    Domain: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChallengeMetadataRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateChallengeResponseTypeDef(BaseValidatorModel):
    Challenge: ChallengeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorResponseTypeDef(BaseValidatorModel):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChallengeMetadataResponseTypeDef(BaseValidatorModel):
    ChallengeMetadata: ChallengeMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChallengePasswordResponseTypeDef(BaseValidatorModel):
    Password: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChallengeMetadataResponseTypeDef(BaseValidatorModel):
    Challenges: List[ChallengeMetadataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MobileDeviceManagementTypeDef(BaseValidatorModel):
    Intune: Optional[IntuneConfigurationTypeDef] = None

class ListChallengeMetadataRequestListChallengeMetadataPaginateTypeDef(BaseValidatorModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ConnectorSummaryTypeDef(BaseValidatorModel):
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

class ConnectorTypeDef(BaseValidatorModel):
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

class CreateConnectorRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    MobileDeviceManagement: Optional[MobileDeviceManagementTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ListConnectorsResponseTypeDef(BaseValidatorModel):
    Connectors: List[ConnectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetConnectorResponseTypeDef(BaseValidatorModel):
    Connector: ConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

