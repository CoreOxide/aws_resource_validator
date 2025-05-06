from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sso_oidc.sso_oidc_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CreateTokenRequest(BaseValidatorModel):
    clientId: str
    clientSecret: str
    grantType: str
    deviceCode: Optional[str] = None
    code: Optional[str] = None
    refreshToken: Optional[str] = None
    scope: Optional[List[str]] = None
    redirectUri: Optional[str] = None
    codeVerifier: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateTokenWithIAMRequest(BaseValidatorModel):
    clientId: str
    grantType: str
    code: Optional[str] = None
    refreshToken: Optional[str] = None
    assertion: Optional[str] = None
    scope: Optional[List[str]] = None
    redirectUri: Optional[str] = None
    subjectToken: Optional[str] = None
    subjectTokenType: Optional[str] = None
    requestedTokenType: Optional[str] = None
    codeVerifier: Optional[str] = None


class RegisterClientRequest(BaseValidatorModel):
    clientName: str
    clientType: str
    scopes: Optional[List[str]] = None
    redirectUris: Optional[List[str]] = None
    grantTypes: Optional[List[str]] = None
    issuerUrl: Optional[str] = None
    entitledApplicationArn: Optional[str] = None


class StartDeviceAuthorizationRequest(BaseValidatorModel):
    clientId: str
    clientSecret: str
    startUrl: str


class CreateTokenResponse(BaseValidatorModel):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    ResponseMetadata: ResponseMetadata


class CreateTokenWithIAMResponse(BaseValidatorModel):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    issuedTokenType: str
    scope: List[str]
    ResponseMetadata: ResponseMetadata


class RegisterClientResponse(BaseValidatorModel):
    clientId: str
    clientSecret: str
    clientIdIssuedAt: int
    clientSecretExpiresAt: int
    authorizationEndpoint: str
    tokenEndpoint: str
    ResponseMetadata: ResponseMetadata


class StartDeviceAuthorizationResponse(BaseValidatorModel):
    deviceCode: str
    userCode: str
    verificationUri: str
    verificationUriComplete: str
    expiresIn: int
    interval: int
    ResponseMetadata: ResponseMetadata