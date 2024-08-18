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
from aws_resource_validator.pydantic_models.iotsecuretunneling_constants import *

class CloseTunnelRequestRequestTypeDef(BaseValidatorModel):
    tunnelId: str
    delete: Optional[bool] = None

class ConnectionStateTypeDef(BaseValidatorModel):
    status: Optional[ConnectionStatusType] = None
    lastUpdatedAt: Optional[datetime] = None

class DescribeTunnelRequestRequestTypeDef(BaseValidatorModel):
    tunnelId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DestinationConfigTypeDef(BaseValidatorModel):
    services: List[str]
    thingName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class ListTunnelsRequestRequestTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TunnelSummaryTypeDef(BaseValidatorModel):
    tunnelId: Optional[str] = None
    tunnelArn: Optional[str] = None
    status: Optional[TunnelStatusType] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None

class TimeoutConfigTypeDef(BaseValidatorModel):
    maxLifetimeTimeoutMinutes: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class OpenTunnelResponseTypeDef(BaseValidatorModel):
    tunnelId: str
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotateTunnelAccessTokenResponseTypeDef(BaseValidatorModel):
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotateTunnelAccessTokenRequestRequestTypeDef(BaseValidatorModel):
    tunnelId: str
    clientMode: ClientModeType
    destinationConfig: Optional[DestinationConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class ListTunnelsResponseTypeDef(BaseValidatorModel):
    tunnelSummaries: List[TunnelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OpenTunnelRequestRequestTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    destinationConfig: Optional[DestinationConfigTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None

class TunnelTypeDef(BaseValidatorModel):
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

class DescribeTunnelResponseTypeDef(BaseValidatorModel):
    tunnel: TunnelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

