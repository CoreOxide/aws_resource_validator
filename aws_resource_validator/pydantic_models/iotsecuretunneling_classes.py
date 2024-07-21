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
from aws_resource_validator.pydantic_models.iotsecuretunneling_constants import *

class CloseTunnelRequestRequestTypeDef(BaseModel):
    tunnelId: str
    delete: Optional[bool] = None

class ConnectionStateTypeDef(BaseModel):
    status: Optional[ConnectionStatusType] = None
    lastUpdatedAt: Optional[datetime] = None

class DescribeTunnelRequestRequestTypeDef(BaseModel):
    tunnelId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DestinationConfigTypeDef(BaseModel):
    services: List[str]
    thingName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagTypeDef(BaseModel):
    key: str
    value: str

class ListTunnelsRequestRequestTypeDef(BaseModel):
    thingName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TunnelSummaryTypeDef(BaseModel):
    tunnelId: Optional[str] = None
    tunnelArn: Optional[str] = None
    status: Optional[TunnelStatusType] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None

class TimeoutConfigTypeDef(BaseModel):
    maxLifetimeTimeoutMinutes: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class OpenTunnelResponseTypeDef(BaseModel):
    tunnelId: str
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotateTunnelAccessTokenResponseTypeDef(BaseModel):
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotateTunnelAccessTokenRequestRequestTypeDef(BaseModel):
    tunnelId: str
    clientMode: ClientModeType
    destinationConfig: Optional[DestinationConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class ListTunnelsResponseTypeDef(BaseModel):
    tunnelSummaries: List[TunnelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OpenTunnelRequestRequestTypeDef(BaseModel):
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    destinationConfig: Optional[DestinationConfigTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None

class TunnelTypeDef(BaseModel):
    tunnelId: Optional[str] = None
    tunnelArn: Optional[str] = None
    status: Optional[TunnelStatusType] = None
    sourceConnectionState: Optional[ConnectionStateTypeDef] = None
    destinationConnectionState: Optional[ConnectionStateTypeDef] = None
    description: Optional[str] = None
    destinationConfig: Optional[DestinationConfigTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None

class DescribeTunnelResponseTypeDef(BaseModel):
    tunnel: TunnelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

