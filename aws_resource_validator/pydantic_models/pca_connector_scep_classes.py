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

class ChallengeMetadataSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class ChallengeMetadata(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class Challenge(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Password: Optional[str] = None


class OpenIdConfiguration(BaseValidatorModel):
    Issuer: Optional[str] = None
    Subject: Optional[str] = None
    Audience: Optional[str] = None


class CreateChallengeRequest(BaseValidatorModel):
    ConnectorArn: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteChallengeRequest(BaseValidatorModel):
    ChallengeArn: str


class DeleteConnectorRequest(BaseValidatorModel):
    ConnectorArn: str


class GetChallengeMetadataRequest(BaseValidatorModel):
    ChallengeArn: str


class GetChallengePasswordRequest(BaseValidatorModel):
    ChallengeArn: str


class GetConnectorRequest(BaseValidatorModel):
    ConnectorArn: str


class IntuneConfiguration(BaseValidatorModel):
    AzureApplicationId: str
    Domain: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChallengeMetadataRequest(BaseValidatorModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConnectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class CreateChallengeResponse(BaseValidatorModel):
    Challenge: Challenge
    ResponseMetadata: ResponseMetadata


class CreateConnectorResponse(BaseValidatorModel):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetChallengeMetadataResponse(BaseValidatorModel):
    ChallengeMetadata: ChallengeMetadata
    ResponseMetadata: ResponseMetadata


class GetChallengePasswordResponse(BaseValidatorModel):
    Password: str
    ResponseMetadata: ResponseMetadata


class ListChallengeMetadataResponse(BaseValidatorModel):
    Challenges: List[ChallengeMetadataSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class MobileDeviceManagement(BaseValidatorModel):
    Intune: Optional[IntuneConfiguration] = None


class ListChallengeMetadataRequestPaginate(BaseValidatorModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class CreateConnectorRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    MobileDeviceManagement: Optional[MobileDeviceManagement] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ConnectorSummary(BaseValidatorModel):
    pass


class ListConnectorsResponse(BaseValidatorModel):
    Connectors: List[ConnectorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Connector(BaseValidatorModel):
    pass


class GetConnectorResponse(BaseValidatorModel):
    Connector: Connector
    ResponseMetadata: ResponseMetadata


