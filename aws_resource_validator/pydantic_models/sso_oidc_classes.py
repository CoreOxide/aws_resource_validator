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
from aws_resource_validator.pydantic_models.sso_oidc_constants import *

class CreateTokenRequestRequestTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    grantType: str
    deviceCode: Optional[str] = None
    code: Optional[str] = None
    refreshToken: Optional[str] = None
    scope: Optional[Sequence[str]] = None
    redirectUri: Optional[str] = None
    codeVerifier: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateTokenWithIAMRequestRequestTypeDef(BaseValidatorModel):
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

class RegisterClientRequestRequestTypeDef(BaseValidatorModel):
    clientName: str
    clientType: str
    scopes: Optional[Sequence[str]] = None
    redirectUris: Optional[Sequence[str]] = None
    grantTypes: Optional[Sequence[str]] = None
    issuerUrl: Optional[str] = None
    entitledApplicationArn: Optional[str] = None

class StartDeviceAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    startUrl: str

class CreateTokenResponseTypeDef(BaseValidatorModel):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTokenWithIAMResponseTypeDef(BaseValidatorModel):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    issuedTokenType: str
    scope: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterClientResponseTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    clientIdIssuedAt: int
    clientSecretExpiresAt: int
    authorizationEndpoint: str
    tokenEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeviceAuthorizationResponseTypeDef(BaseValidatorModel):
    deviceCode: str
    userCode: str
    verificationUri: str
    verificationUriComplete: str
    expiresIn: int
    interval: int
    ResponseMetadata: ResponseMetadataTypeDef

