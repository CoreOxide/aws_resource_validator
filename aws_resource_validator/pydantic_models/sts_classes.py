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
from aws_resource_validator.pydantic_models.sts_constants import *

class PolicyDescriptorType(BaseValidatorModel):
    arn: Optional[str] = None


class ProvidedContext(BaseValidatorModel):
    ProviderArn: Optional[str] = None
    ContextAssertion: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class AssumedRoleUser(BaseValidatorModel):
    AssumedRoleId: str
    Arn: str


class Credentials(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DecodeAuthorizationMessageRequest(BaseValidatorModel):
    EncodedMessage: str


class FederatedUser(BaseValidatorModel):
    FederatedUserId: str
    Arn: str


class GetAccessKeyInfoRequest(BaseValidatorModel):
    AccessKeyId: str


class GetSessionTokenRequest(BaseValidatorModel):
    DurationSeconds: Optional[int] = None
    SerialNumber: Optional[str] = None
    TokenCode: Optional[str] = None


class AssumeRoleWithSAMLRequest(BaseValidatorModel):
    RoleArn: str
    PrincipalArn: str
    SAMLAssertion: str
    PolicyArns: Optional[Sequence[PolicyDescriptorType]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None


class AssumeRoleWithWebIdentityRequest(BaseValidatorModel):
    RoleArn: str
    RoleSessionName: str
    WebIdentityToken: str
    ProviderId: Optional[str] = None
    PolicyArns: Optional[Sequence[PolicyDescriptorType]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None


class AssumeRootRequest(BaseValidatorModel):
    TargetPrincipal: str
    TaskPolicyArn: PolicyDescriptorType
    DurationSeconds: Optional[int] = None


class AssumeRoleRequest(BaseValidatorModel):
    RoleArn: str
    RoleSessionName: str
    PolicyArns: Optional[Sequence[PolicyDescriptorType]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None
    Tags: Optional[Sequence[Tag]] = None
    TransitiveTagKeys: Optional[Sequence[str]] = None
    ExternalId: Optional[str] = None
    SerialNumber: Optional[str] = None
    TokenCode: Optional[str] = None
    SourceIdentity: Optional[str] = None
    ProvidedContexts: Optional[Sequence[ProvidedContext]] = None


class GetFederationTokenRequest(BaseValidatorModel):
    Name: str
    Policy: Optional[str] = None
    PolicyArns: Optional[Sequence[PolicyDescriptorType]] = None
    DurationSeconds: Optional[int] = None
    Tags: Optional[Sequence[Tag]] = None


class AssumeRoleResponse(BaseValidatorModel):
    Credentials: Credentials
    AssumedRoleUser: AssumedRoleUser
    PackedPolicySize: int
    SourceIdentity: str
    ResponseMetadata: ResponseMetadata


class AssumeRoleWithSAMLResponse(BaseValidatorModel):
    Credentials: Credentials
    AssumedRoleUser: AssumedRoleUser
    PackedPolicySize: int
    Subject: str
    SubjectType: str
    Issuer: str
    Audience: str
    NameQualifier: str
    SourceIdentity: str
    ResponseMetadata: ResponseMetadata


class AssumeRoleWithWebIdentityResponse(BaseValidatorModel):
    Credentials: Credentials
    SubjectFromWebIdentityToken: str
    AssumedRoleUser: AssumedRoleUser
    PackedPolicySize: int
    Provider: str
    Audience: str
    SourceIdentity: str
    ResponseMetadata: ResponseMetadata


class AssumeRootResponse(BaseValidatorModel):
    Credentials: Credentials
    SourceIdentity: str
    ResponseMetadata: ResponseMetadata


class DecodeAuthorizationMessageResponse(BaseValidatorModel):
    DecodedMessage: str
    ResponseMetadata: ResponseMetadata


class GetAccessKeyInfoResponse(BaseValidatorModel):
    Account: str
    ResponseMetadata: ResponseMetadata


class GetCallerIdentityResponse(BaseValidatorModel):
    UserId: str
    Account: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class GetSessionTokenResponse(BaseValidatorModel):
    Credentials: Credentials
    ResponseMetadata: ResponseMetadata


class GetFederationTokenResponse(BaseValidatorModel):
    Credentials: Credentials
    FederatedUser: FederatedUser
    PackedPolicySize: int
    ResponseMetadata: ResponseMetadata


