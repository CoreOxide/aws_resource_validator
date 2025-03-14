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
from aws_resource_validator.pydantic_models.networkmonitor_constants import *

class CreateMonitorProbeInputTypeDef(BaseValidatorModel):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: Optional[int] = None
    packetSize: Optional[int] = None
    probeTags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ProbeInputTypeDef(BaseValidatorModel):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: Optional[int] = None
    packetSize: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str


class DeleteProbeInputTypeDef(BaseValidatorModel):
    monitorName: str
    probeId: str


class GetMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str


class ProbeTypeDef(BaseValidatorModel):
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


class GetProbeInputTypeDef(BaseValidatorModel):
    monitorName: str
    probeId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListMonitorsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    state: Optional[str] = None


class MonitorSummaryTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str
    aggregationPeriod: int


class UpdateProbeInputTypeDef(BaseValidatorModel):
    monitorName: str
    probeId: str
    state: Optional[ProbeStateType] = None
    destination: Optional[str] = None
    destinationPort: Optional[int] = None
    protocol: Optional[ProtocolType] = None
    packetSize: Optional[int] = None


class CreateMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str
    probes: Optional[Sequence[CreateMonitorProbeInputTypeDef]] = None
    aggregationPeriod: Optional[int] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateMonitorOutputTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProbeOutputTypeDef(BaseValidatorModel):
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


class GetProbeOutputTypeDef(BaseValidatorModel):
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


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMonitorOutputTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProbeOutputTypeDef(BaseValidatorModel):
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


class CreateProbeInputTypeDef(BaseValidatorModel):
    monitorName: str
    probe: ProbeInputTypeDef
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetMonitorOutputTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    probes: List[ProbeTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListMonitorsInputPaginateTypeDef(BaseValidatorModel):
    state: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitorsOutputTypeDef(BaseValidatorModel):
    monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


