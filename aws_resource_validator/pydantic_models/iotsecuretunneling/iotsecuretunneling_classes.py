from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotsecuretunneling.iotsecuretunneling_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CloseTunnelRequest(BaseValidatorModel):
    tunnelId: str
    delete: Optional[bool] = None


class ConnectionState(BaseValidatorModel):
    status: Optional[ConnectionStatusType] = None
    lastUpdatedAt: Optional[datetime] = None


class DescribeTunnelRequest(BaseValidatorModel):
    tunnelId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DestinationConfigOutput(BaseValidatorModel):
    services: List[str]
    thingName: Optional[str] = None


class DestinationConfig(BaseValidatorModel):
    services: List[str]
    thingName: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class Tag(BaseValidatorModel):
    key: str
    value: str


class ListTunnelsRequest(BaseValidatorModel):
    thingName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TunnelSummary(BaseValidatorModel):
    tunnelId: Optional[str] = None
    tunnelArn: Optional[str] = None
    status: Optional[TunnelStatusType] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None


class TimeoutConfig(BaseValidatorModel):
    maxLifetimeTimeoutMinutes: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class OpenTunnelResponse(BaseValidatorModel):
    tunnelId: str
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadata


class RotateTunnelAccessTokenResponse(BaseValidatorModel):
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadata

DestinationConfigUnion = Union[DestinationConfig, DestinationConfigOutput]


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class ListTunnelsResponse(BaseValidatorModel):
    tunnelSummaries: List[TunnelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Tunnel(BaseValidatorModel):
    tunnelId: Optional[str] = None
    tunnelArn: Optional[str] = None
    status: Optional[TunnelStatusType] = None
    sourceConnectionState: Optional[ConnectionState] = None
    destinationConnectionState: Optional[ConnectionState] = None
    description: Optional[str] = None
    destinationConfig: Optional[DestinationConfigOutput] = None
    timeoutConfig: Optional[TimeoutConfig] = None
    tags: Optional[List[Tag]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None


class OpenTunnelRequest(BaseValidatorModel):
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    destinationConfig: Optional[DestinationConfigUnion] = None
    timeoutConfig: Optional[TimeoutConfig] = None


class RotateTunnelAccessTokenRequest(BaseValidatorModel):
    tunnelId: str
    clientMode: ClientModeType
    destinationConfig: Optional[DestinationConfigUnion] = None


class DescribeTunnelResponse(BaseValidatorModel):
    tunnel: Tunnel
    ResponseMetadata: ResponseMetadata