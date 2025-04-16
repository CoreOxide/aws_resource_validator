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
from aws_resource_validator.pydantic_models.iotsecuretunneling_constants import *

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
    services: Sequence[str]
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
    tagKeys: Sequence[str]


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


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


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


class DestinationConfigUnion(BaseValidatorModel):
    pass


class OpenTunnelRequest(BaseValidatorModel):
    description: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    destinationConfig: Optional[DestinationConfigUnion] = None
    timeoutConfig: Optional[TimeoutConfig] = None


class RotateTunnelAccessTokenRequest(BaseValidatorModel):
    tunnelId: str
    clientMode: ClientModeType
    destinationConfig: Optional[DestinationConfigUnion] = None


class DescribeTunnelResponse(BaseValidatorModel):
    tunnel: Tunnel
    ResponseMetadata: ResponseMetadata


