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

class PolicyDescriptorTypeTypeDef(BaseValidatorModel):
    arn: Optional[str] = None


class ProvidedContextTypeDef(BaseValidatorModel):
    ProviderArn: Optional[str] = None
    ContextAssertion: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class AssumedRoleUserTypeDef(BaseValidatorModel):
    AssumedRoleId: str
    Arn: str


class CredentialsTypeDef(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DecodeAuthorizationMessageRequestTypeDef(BaseValidatorModel):
    EncodedMessage: str


class FederatedUserTypeDef(BaseValidatorModel):
    FederatedUserId: str
    Arn: str


class GetAccessKeyInfoRequestTypeDef(BaseValidatorModel):
    AccessKeyId: str


class GetSessionTokenRequestTypeDef(BaseValidatorModel):
    DurationSeconds: Optional[int] = None
    SerialNumber: Optional[str] = None
    TokenCode: Optional[str] = None


class AssumeRoleWithSAMLRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    PrincipalArn: str
    SAMLAssertion: str
    PolicyArns: Optional[Sequence[PolicyDescriptorTypeTypeDef]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None


class AssumeRoleWithWebIdentityRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    RoleSessionName: str
    WebIdentityToken: str
    ProviderId: Optional[str] = None
    PolicyArns: Optional[Sequence[PolicyDescriptorTypeTypeDef]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None


class AssumeRootRequestTypeDef(BaseValidatorModel):
    TargetPrincipal: str
    TaskPolicyArn: PolicyDescriptorTypeTypeDef
    DurationSeconds: Optional[int] = None


class AssumeRoleRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    RoleSessionName: str
    PolicyArns: Optional[Sequence[PolicyDescriptorTypeTypeDef]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TransitiveTagKeys: Optional[Sequence[str]] = None
    ExternalId: Optional[str] = None
    SerialNumber: Optional[str] = None
    TokenCode: Optional[str] = None
    SourceIdentity: Optional[str] = None
    ProvidedContexts: Optional[Sequence[ProvidedContextTypeDef]] = None


class GetFederationTokenRequestTypeDef(BaseValidatorModel):
    Name: str
    Policy: Optional[str] = None
    PolicyArns: Optional[Sequence[PolicyDescriptorTypeTypeDef]] = None
    DurationSeconds: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class AssumeRoleResponseTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssumeRoleWithSAMLResponseTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    Subject: str
    SubjectType: str
    Issuer: str
    Audience: str
    NameQualifier: str
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssumeRoleWithWebIdentityResponseTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    SubjectFromWebIdentityToken: str
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    Provider: str
    Audience: str
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssumeRootResponseTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef


class DecodeAuthorizationMessageResponseTypeDef(BaseValidatorModel):
    DecodedMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessKeyInfoResponseTypeDef(BaseValidatorModel):
    Account: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCallerIdentityResponseTypeDef(BaseValidatorModel):
    UserId: str
    Account: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSessionTokenResponseTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFederationTokenResponseTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    FederatedUser: FederatedUserTypeDef
    PackedPolicySize: int
    ResponseMetadata: ResponseMetadataTypeDef


