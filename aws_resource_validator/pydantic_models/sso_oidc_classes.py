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
from aws_resource_validator.pydantic_models.sso_oidc_constants import *

class CreateTokenRequestRequestTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    grantType: str
    deviceCode: Optional[str] = None
    code: Optional[str] = None
    refreshToken: Optional[str] = None
    scope: Optional[Sequence[str]] = None
    redirectUri: Optional[str] = None
    codeVerifier: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateTokenWithIAMRequestRequestTypeDef(BaseModel):
    clientId: str
    grantType: str
    code: Optional[str] = None
    refreshToken: Optional[str] = None
    assertion: Optional[str] = None
    scope: Optional[Sequence[str]] = None
    redirectUri: Optional[str] = None
    subjectToken: Optional[str] = None
    subjectTokenType: Optional[str] = None
    requestedTokenType: Optional[str] = None
    codeVerifier: Optional[str] = None

class RegisterClientRequestRequestTypeDef(BaseModel):
    clientName: str
    clientType: str
    scopes: Optional[Sequence[str]] = None
    redirectUris: Optional[Sequence[str]] = None
    grantTypes: Optional[Sequence[str]] = None
    issuerUrl: Optional[str] = None
    entitledApplicationArn: Optional[str] = None

class StartDeviceAuthorizationRequestRequestTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    startUrl: str

class CreateTokenResponseTypeDef(BaseModel):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTokenWithIAMResponseTypeDef(BaseModel):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    issuedTokenType: str
    scope: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterClientResponseTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    clientIdIssuedAt: int
    clientSecretExpiresAt: int
    authorizationEndpoint: str
    tokenEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeviceAuthorizationResponseTypeDef(BaseModel):
    deviceCode: str
    userCode: str
    verificationUri: str
    verificationUriComplete: str
    expiresIn: int
    interval: int
    ResponseMetadata: ResponseMetadataTypeDef

