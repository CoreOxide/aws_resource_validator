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
from aws_resource_validator.pydantic_models.networkmonitor_constants import *

class CreateMonitorProbeInputTypeDef(BaseModel):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: Optional[int] = None
    packetSize: Optional[int] = None
    probeTags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ProbeInputTypeDef(BaseModel):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: Optional[int] = None
    packetSize: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteMonitorInputRequestTypeDef(BaseModel):
    monitorName: str

class DeleteProbeInputRequestTypeDef(BaseModel):
    monitorName: str
    probeId: str

class GetMonitorInputRequestTypeDef(BaseModel):
    monitorName: str

class ProbeTypeDef(BaseModel):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    probeId: Optional[str] = None
    probeArn: Optional[str] = None
    destinationPort: Optional[int] = None
    packetSize: Optional[int] = None
    addressFamily: Optional[AddressFamilyType] = None
    vpcId: Optional[str] = None
    state: Optional[ProbeStateType] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class GetProbeInputRequestTypeDef(BaseModel):
    monitorName: str
    probeId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListMonitorsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    state: Optional[str] = None

class MonitorSummaryTypeDef(BaseModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: Optional[int] = None
    tags: Optional[Dict[str, str]] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateMonitorInputRequestTypeDef(BaseModel):
    monitorName: str
    aggregationPeriod: int

class UpdateProbeInputRequestTypeDef(BaseModel):
    monitorName: str
    probeId: str
    state: Optional[ProbeStateType] = None
    destination: Optional[str] = None
    destinationPort: Optional[int] = None
    protocol: Optional[ProtocolType] = None
    packetSize: Optional[int] = None

class CreateMonitorInputRequestTypeDef(BaseModel):
    monitorName: str
    probes: Optional[Sequence[CreateMonitorProbeInputTypeDef]] = None
    aggregationPeriod: Optional[int] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateMonitorOutputTypeDef(BaseModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProbeOutputTypeDef(BaseModel):
    probeId: str
    probeArn: str
    sourceArn: str
    destination: str
    destinationPort: int
    protocol: ProtocolType
    packetSize: int
    addressFamily: AddressFamilyType
    vpcId: str
    state: ProbeStateType
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetProbeOutputTypeDef(BaseModel):
    probeId: str
    probeArn: str
    sourceArn: str
    destination: str
    destinationPort: int
    protocol: ProtocolType
    packetSize: int
    addressFamily: AddressFamilyType
    vpcId: str
    state: ProbeStateType
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitorOutputTypeDef(BaseModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProbeOutputTypeDef(BaseModel):
    probeId: str
    probeArn: str
    sourceArn: str
    destination: str
    destinationPort: int
    protocol: ProtocolType
    packetSize: int
    addressFamily: AddressFamilyType
    vpcId: str
    state: ProbeStateType
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProbeInputRequestTypeDef(BaseModel):
    monitorName: str
    probe: ProbeInputTypeDef
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetMonitorOutputTypeDef(BaseModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    probes: List[ProbeTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListMonitorsInputListMonitorsPaginateTypeDef(BaseModel):
    state: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorsOutputTypeDef(BaseModel):
    monitors: List[MonitorSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

