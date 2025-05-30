from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CreateMonitorProbeInput(BaseValidatorModel):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: Optional[int] = None
    packetSize: Optional[int] = None
    probeTags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ProbeInput(BaseValidatorModel):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: Optional[int] = None
    packetSize: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class DeleteMonitorInput(BaseValidatorModel):
    monitorName: str


class DeleteProbeInput(BaseValidatorModel):
    monitorName: str
    probeId: str


# This class is the input for the 'get_monitor' function.
class GetMonitorInput(BaseValidatorModel):
    monitorName: str


class Probe(BaseValidatorModel):
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


# This class is the input for the 'get_probe' function.
class GetProbeInput(BaseValidatorModel):
    monitorName: str
    probeId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_monitors' function.
class ListMonitorsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    state: Optional[str] = None


class MonitorSummary(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_monitor' function.
class UpdateMonitorInput(BaseValidatorModel):
    monitorName: str
    aggregationPeriod: int


# This class is the input for the 'update_probe' function.
class UpdateProbeInput(BaseValidatorModel):
    monitorName: str
    probeId: str
    state: Optional[ProbeStateType] = None
    destination: Optional[str] = None
    destinationPort: Optional[int] = None
    protocol: Optional[ProtocolType] = None
    packetSize: Optional[int] = None


# This class is the input for the 'create_monitor' function.
class CreateMonitorInput(BaseValidatorModel):
    monitorName: str
    probes: Optional[List[CreateMonitorProbeInput]] = None
    aggregationPeriod: Optional[int] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_monitor' function.
class CreateMonitorOutput(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_probe' function.
class CreateProbeOutput(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_probe' function.
class GetProbeOutput(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_monitor' function.
class UpdateMonitorOutput(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_probe' function.
class UpdateProbeOutput(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_probe' function.
class CreateProbeInput(BaseValidatorModel):
    monitorName: str
    probe: ProbeInput
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_monitor' function.
class GetMonitorOutput(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    probes: List[Probe]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListMonitorsInputPaginate(BaseValidatorModel):
    state: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_monitors' function.
class ListMonitorsOutput(BaseValidatorModel):
    monitors: List[MonitorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None