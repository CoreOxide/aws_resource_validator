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

class CloseTunnelRequestTypeDef(BaseValidatorModel):
    tunnelId: str
    delete: Optional[bool] = None


class ConnectionStateTypeDef(BaseValidatorModel):
    status: Optional[ConnectionStatusType] = None
    lastUpdatedAt: Optional[datetime] = None


class DescribeTunnelRequestTypeDef(BaseValidatorModel):
    tunnelId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DestinationConfigOutputTypeDef(BaseValidatorModel):
    services: List[str]
    thingName: Optional[str] = None


class DestinationConfigTypeDef(BaseValidatorModel):
    services: Sequence[str]
    thingName: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ListTunnelsRequestTypeDef(BaseValidatorModel):
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


class UntagResourceRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class ListTunnelsResponseTypeDef(BaseValidatorModel):
    tunnelSummaries: List[TunnelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TunnelTypeDef(BaseValidatorModel):
    tunnelId: Optional[str] = None
    tunnelArn: Optional[str] = None
    status: Optional[TunnelStatusType] = None
    sourceConnectionState: Optional[ConnectionStateTypeDef] = None
    destinationConnectionState: Optional[ConnectionStateTypeDef] = None
    description: Optional[str] = None
    destinationConfig: Optional[DestinationConfigOutputTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None


class DestinationConfigUnionTypeDef(BaseValidatorModel):
    pass


class OpenTunnelRequestTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    destinationConfig: Optional[DestinationConfigUnionTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None


class RotateTunnelAccessTokenRequestTypeDef(BaseValidatorModel):
    tunnelId: str
    clientMode: ClientModeType
    destinationConfig: Optional[DestinationConfigUnionTypeDef] = None


class DescribeTunnelResponseTypeDef(BaseValidatorModel):
    tunnel: TunnelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


