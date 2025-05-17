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


# This class is the input for the 'create_challenge' function.
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


# This class is the input for the 'delete_challenge' function.
class DeleteChallengeRequest(BaseValidatorModel):
    ChallengeArn: str


# This class is the input for the 'delete_connector' function.
class DeleteConnectorRequest(BaseValidatorModel):
    ConnectorArn: str


# This class is the input for the 'get_challenge_metadata' function.
class GetChallengeMetadataRequest(BaseValidatorModel):
    ChallengeArn: str


# This class is the input for the 'get_challenge_password' function.
class GetChallengePasswordRequest(BaseValidatorModel):
    ChallengeArn: str


# This class is the input for the 'get_connector' function.
class GetConnectorRequest(BaseValidatorModel):
    ConnectorArn: str


class IntuneConfiguration(BaseValidatorModel):
    AzureApplicationId: str
    Domain: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_challenge_metadata' function.
class ListChallengeMetadataRequest(BaseValidatorModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_connectors' function.
class ListConnectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the output for the 'create_challenge' function.
class CreateChallengeResponse(BaseValidatorModel):
    Challenge: Challenge
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_connector' function.
class CreateConnectorResponse(BaseValidatorModel):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_challenge_metadata' function.
class GetChallengeMetadataResponse(BaseValidatorModel):
    ChallengeMetadata: ChallengeMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_challenge_password' function.
class GetChallengePasswordResponse(BaseValidatorModel):
    Password: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_challenge_metadata' function.
class ListChallengeMetadataResponse(BaseValidatorModel):
    Challenges: List[ChallengeMetadataSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
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


# This class is the input for the 'create_connector' function.
class CreateConnectorRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    MobileDeviceManagement: Optional[MobileDeviceManagement] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'list_connectors' function.
class ListConnectorsResponse(BaseValidatorModel):
    Connectors: List[ConnectorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_connector' function.
class GetConnectorResponse(BaseValidatorModel):
    Connector: Connector
    ResponseMetadata: ResponseMetadata