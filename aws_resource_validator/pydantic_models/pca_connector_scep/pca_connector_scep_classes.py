from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    Tags: Optional[Dict[str, str]] = None


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
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


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


class ConnectorSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    Type: Optional[ConnectorTypeType] = None
    MobileDeviceManagement: Optional[MobileDeviceManagement] = None
    OpenIdConfiguration: Optional[OpenIdConfiguration] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    Endpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class Connector(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    Type: Optional[ConnectorTypeType] = None
    MobileDeviceManagement: Optional[MobileDeviceManagement] = None
    OpenIdConfiguration: Optional[OpenIdConfiguration] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    Endpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class CreateConnectorRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    MobileDeviceManagement: Optional[MobileDeviceManagement] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListConnectorsResponse(BaseValidatorModel):
    Connectors: List[ConnectorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetConnectorResponse(BaseValidatorModel):
    Connector: Connector
    ResponseMetadata: ResponseMetadata