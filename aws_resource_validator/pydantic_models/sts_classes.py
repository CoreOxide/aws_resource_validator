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
from aws_resource_validator.pydantic_models.sts_constants import *

class PolicyDescriptorTypeTypeDef(BaseModel):
    arn: Optional[str] = None

class ProvidedContextTypeDef(BaseModel):
    ProviderArn: Optional[str] = None
    ContextAssertion: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AssumedRoleUserTypeDef(BaseModel):
    AssumedRoleId: str
    Arn: str

class CredentialsTypeDef(BaseModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DecodeAuthorizationMessageRequestRequestTypeDef(BaseModel):
    EncodedMessage: str

class FederatedUserTypeDef(BaseModel):
    FederatedUserId: str
    Arn: str

class GetAccessKeyInfoRequestRequestTypeDef(BaseModel):
    AccessKeyId: str

class GetSessionTokenRequestRequestTypeDef(BaseModel):
    DurationSeconds: Optional[int] = None
    SerialNumber: Optional[str] = None
    TokenCode: Optional[str] = None

class AssumeRoleWithSAMLRequestRequestTypeDef(BaseModel):
    RoleArn: str
    PrincipalArn: str
    SAMLAssertion: str
    PolicyArns: Optional[Sequence[PolicyDescriptorTypeTypeDef]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None

class AssumeRoleWithWebIdentityRequestRequestTypeDef(BaseModel):
    RoleArn: str
    RoleSessionName: str
    WebIdentityToken: str
    ProviderId: Optional[str] = None
    PolicyArns: Optional[Sequence[PolicyDescriptorTypeTypeDef]] = None
    Policy: Optional[str] = None
    DurationSeconds: Optional[int] = None

class AssumeRoleRequestRequestTypeDef(BaseModel):
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

class GetFederationTokenRequestRequestTypeDef(BaseModel):
    Name: str
    Policy: Optional[str] = None
    PolicyArns: Optional[Sequence[PolicyDescriptorTypeTypeDef]] = None
    DurationSeconds: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class AssumeRoleResponseTypeDef(BaseModel):
    Credentials: CredentialsTypeDef
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeRoleWithSAMLResponseTypeDef(BaseModel):
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

class AssumeRoleWithWebIdentityResponseTypeDef(BaseModel):
    Credentials: CredentialsTypeDef
    SubjectFromWebIdentityToken: str
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    Provider: str
    Audience: str
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class DecodeAuthorizationMessageResponseTypeDef(BaseModel):
    DecodedMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessKeyInfoResponseTypeDef(BaseModel):
    Account: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCallerIdentityResponseTypeDef(BaseModel):
    UserId: str
    Account: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionTokenResponseTypeDef(BaseModel):
    Credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFederationTokenResponseTypeDef(BaseModel):
    Credentials: CredentialsTypeDef
    FederatedUser: FederatedUserTypeDef
    PackedPolicySize: int
    ResponseMetadata: ResponseMetadataTypeDef

