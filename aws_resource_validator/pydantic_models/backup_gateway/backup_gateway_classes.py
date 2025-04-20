from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.backup_gateway.backup_gateway_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssociateGatewayToServerInput(BaseValidatorModel):
    GatewayArn: str
    ServerArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BandwidthRateLimitIntervalOutput(BaseValidatorModel):
    DaysOfWeek: List[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None


class BandwidthRateLimitInterval(BaseValidatorModel):
    DaysOfWeek: List[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteGatewayInput(BaseValidatorModel):
    GatewayArn: str


class DeleteHypervisorInput(BaseValidatorModel):
    HypervisorArn: str


class DisassociateGatewayFromServerInput(BaseValidatorModel):
    GatewayArn: str


class MaintenanceStartTime(BaseValidatorModel):
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None


class Gateway(BaseValidatorModel):
    GatewayArn: Optional[str] = None
    GatewayDisplayName: Optional[str] = None
    GatewayType: Optional[Literal['BACKUP_VM']] = None
    HypervisorId: Optional[str] = None
    LastSeenTime: Optional[datetime] = None


class GetBandwidthRateLimitScheduleInput(BaseValidatorModel):
    GatewayArn: str


class GetGatewayInput(BaseValidatorModel):
    GatewayArn: str


class GetHypervisorInput(BaseValidatorModel):
    HypervisorArn: str


class HypervisorDetails(BaseValidatorModel):
    Host: Optional[str] = None
    HypervisorArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastSuccessfulMetadataSyncTime: Optional[datetime] = None
    LatestMetadataSyncStatus: Optional[SyncMetadataStatusType] = None
    LatestMetadataSyncStatusMessage: Optional[str] = None
    LogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[HypervisorStateType] = None


class GetHypervisorPropertyMappingsInput(BaseValidatorModel):
    HypervisorArn: str


class VmwareToAwsTagMapping(BaseValidatorModel):
    AwsTagKey: str
    AwsTagValue: str
    VmwareCategory: str
    VmwareTagName: str


class GetVirtualMachineInput(BaseValidatorModel):
    ResourceArn: str


class Hypervisor(BaseValidatorModel):
    Host: Optional[str] = None
    HypervisorArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[HypervisorStateType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListGatewaysInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHypervisorsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class ListVirtualMachinesInput(BaseValidatorModel):
    HypervisorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class VirtualMachine(BaseValidatorModel):
    HostName: Optional[str] = None
    HypervisorId: Optional[str] = None
    LastBackupDate: Optional[datetime] = None
    Name: Optional[str] = None
    Path: Optional[str] = None
    ResourceArn: Optional[str] = None


class PutMaintenanceStartTimeInput(BaseValidatorModel):
    GatewayArn: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None


class StartVirtualMachinesMetadataSyncInput(BaseValidatorModel):
    HypervisorArn: str


class TestHypervisorConfigurationInput(BaseValidatorModel):
    GatewayArn: str
    Host: str
    Password: Optional[str] = None
    Username: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class UpdateGatewayInformationInput(BaseValidatorModel):
    GatewayArn: str
    GatewayDisplayName: Optional[str] = None


class UpdateGatewaySoftwareNowInput(BaseValidatorModel):
    GatewayArn: str


class UpdateHypervisorInput(BaseValidatorModel):
    HypervisorArn: str
    Host: Optional[str] = None
    LogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    Password: Optional[str] = None
    Username: Optional[str] = None


class VmwareTag(BaseValidatorModel):
    VmwareCategory: Optional[str] = None
    VmwareTagDescription: Optional[str] = None
    VmwareTagName: Optional[str] = None


class AssociateGatewayToServerOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class CreateGatewayOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class DeleteGatewayOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class DeleteHypervisorOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


class DisassociateGatewayFromServerOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class ImportHypervisorConfigurationOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


class PutBandwidthRateLimitScheduleOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class PutHypervisorPropertyMappingsOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


class PutMaintenanceStartTimeOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class StartVirtualMachinesMetadataSyncOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


class TagResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


class UntagResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


class UpdateGatewayInformationOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class UpdateGatewaySoftwareNowOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class UpdateHypervisorOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


class GetBandwidthRateLimitScheduleOutput(BaseValidatorModel):
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutput]
    GatewayArn: str
    ResponseMetadata: ResponseMetadata

BandwidthRateLimitIntervalUnion = Union[BandwidthRateLimitInterval, BandwidthRateLimitIntervalOutput]


class CreateGatewayInput(BaseValidatorModel):
    ActivationKey: str
    GatewayDisplayName: str
    GatewayType: Literal['BACKUP_VM']
    Tags: Optional[List[Tag]] = None


class ImportHypervisorConfigurationInput(BaseValidatorModel):
    Host: str
    Name: str
    KmsKeyArn: Optional[str] = None
    Password: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Username: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceInput(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class GatewayDetails(BaseValidatorModel):
    GatewayArn: Optional[str] = None
    GatewayDisplayName: Optional[str] = None
    GatewayType: Optional[Literal['BACKUP_VM']] = None
    HypervisorId: Optional[str] = None
    LastSeenTime: Optional[datetime] = None
    MaintenanceStartTime: Optional[MaintenanceStartTime] = None
    NextUpdateAvailabilityTime: Optional[datetime] = None
    VpcEndpoint: Optional[str] = None


class ListGatewaysOutput(BaseValidatorModel):
    Gateways: List[Gateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetHypervisorOutput(BaseValidatorModel):
    Hypervisor: HypervisorDetails
    ResponseMetadata: ResponseMetadata


class GetHypervisorPropertyMappingsOutput(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMapping]
    ResponseMetadata: ResponseMetadata


class PutHypervisorPropertyMappingsInput(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMapping]


class ListHypervisorsOutput(BaseValidatorModel):
    Hypervisors: List[Hypervisor]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGatewaysInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHypervisorsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualMachinesInputPaginate(BaseValidatorModel):
    HypervisorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualMachinesOutput(BaseValidatorModel):
    VirtualMachines: List[VirtualMachine]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class VirtualMachineDetails(BaseValidatorModel):
    HostName: Optional[str] = None
    HypervisorId: Optional[str] = None
    LastBackupDate: Optional[datetime] = None
    Name: Optional[str] = None
    Path: Optional[str] = None
    ResourceArn: Optional[str] = None
    VmwareTags: Optional[List[VmwareTag]] = None


class PutBandwidthRateLimitScheduleInput(BaseValidatorModel):
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalUnion]
    GatewayArn: str


class GetGatewayOutput(BaseValidatorModel):
    Gateway: GatewayDetails
    ResponseMetadata: ResponseMetadata


class GetVirtualMachineOutput(BaseValidatorModel):
    VirtualMachine: VirtualMachineDetails
    ResponseMetadata: ResponseMetadata