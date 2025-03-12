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


class CreateChallengeRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteChallengeRequestTypeDef(BaseValidatorModel):
    ChallengeArn: str


class DeleteConnectorRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str


class GetChallengeMetadataRequestTypeDef(BaseValidatorModel):
    ChallengeArn: str


class GetChallengePasswordRequestTypeDef(BaseValidatorModel):
    ChallengeArn: str


class GetConnectorRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str


class IntuneConfigurationTypeDef(BaseValidatorModel):
    AzureApplicationId: str
    Domain: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChallengeMetadataRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConnectorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
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


class ListChallengeMetadataRequestPaginateTypeDef(BaseValidatorModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class CreateConnectorRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    MobileDeviceManagement: Optional[MobileDeviceManagementTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ConnectorSummaryTypeDef(BaseValidatorModel):
    pass


class ListConnectorsResponseTypeDef(BaseValidatorModel):
    Connectors: List[ConnectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ConnectorTypeDef(BaseValidatorModel):
    pass


class GetConnectorResponseTypeDef(BaseValidatorModel):
    Connector: ConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


