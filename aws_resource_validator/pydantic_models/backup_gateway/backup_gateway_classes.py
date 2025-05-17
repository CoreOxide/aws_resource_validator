from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.backup_gateway.backup_gateway_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'associate_gateway_to_server' function.
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


# This class is the input for the 'delete_gateway' function.
class DeleteGatewayInput(BaseValidatorModel):
    GatewayArn: str


# This class is the input for the 'delete_hypervisor' function.
class DeleteHypervisorInput(BaseValidatorModel):
    HypervisorArn: str


# This class is the input for the 'disassociate_gateway_from_server' function.
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


# This class is the input for the 'get_bandwidth_rate_limit_schedule' function.
class GetBandwidthRateLimitScheduleInput(BaseValidatorModel):
    GatewayArn: str


# This class is the input for the 'get_gateway' function.
class GetGatewayInput(BaseValidatorModel):
    GatewayArn: str


# This class is the input for the 'get_hypervisor' function.
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


# This class is the input for the 'get_hypervisor_property_mappings' function.
class GetHypervisorPropertyMappingsInput(BaseValidatorModel):
    HypervisorArn: str


class VmwareToAwsTagMapping(BaseValidatorModel):
    AwsTagKey: str
    AwsTagValue: str
    VmwareCategory: str
    VmwareTagName: str


# This class is the input for the 'get_virtual_machine' function.
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


# This class is the input for the 'list_gateways' function.
class ListGatewaysInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_hypervisors' function.
class ListHypervisorsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'list_virtual_machines' function.
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


# This class is the input for the 'put_maintenance_start_time' function.
class PutMaintenanceStartTimeInput(BaseValidatorModel):
    GatewayArn: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None


# This class is the input for the 'start_virtual_machines_metadata_sync' function.
class StartVirtualMachinesMetadataSyncInput(BaseValidatorModel):
    HypervisorArn: str


class TestHypervisorConfigurationInput(BaseValidatorModel):
    GatewayArn: str
    Host: str
    Password: Optional[str] = None
    Username: Optional[str] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_gateway_information' function.
class UpdateGatewayInformationInput(BaseValidatorModel):
    GatewayArn: str
    GatewayDisplayName: Optional[str] = None


# This class is the input for the 'update_gateway_software_now' function.
class UpdateGatewaySoftwareNowInput(BaseValidatorModel):
    GatewayArn: str


# This class is the input for the 'update_hypervisor' function.
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


# This class is the output for the 'associate_gateway_to_server' function.
class AssociateGatewayToServerOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_gateway' function.
class CreateGatewayOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_gateway' function.
class DeleteGatewayOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_hypervisor' function.
class DeleteHypervisorOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_gateway_from_server' function.
class DisassociateGatewayFromServerOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_hypervisor_configuration' function.
class ImportHypervisorConfigurationOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_bandwidth_rate_limit_schedule' function.
class PutBandwidthRateLimitScheduleOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_hypervisor_property_mappings' function.
class PutHypervisorPropertyMappingsOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_maintenance_start_time' function.
class PutMaintenanceStartTimeOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_virtual_machines_metadata_sync' function.
class StartVirtualMachinesMetadataSyncOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'tag_resource' function.
class TagResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class UntagResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_gateway_information' function.
class UpdateGatewayInformationOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_gateway_software_now' function.
class UpdateGatewaySoftwareNowOutput(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_hypervisor' function.
class UpdateHypervisorOutput(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bandwidth_rate_limit_schedule' function.
class GetBandwidthRateLimitScheduleOutput(BaseValidatorModel):
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutput]
    GatewayArn: str
    ResponseMetadata: ResponseMetadata

BandwidthRateLimitIntervalUnion = Union[BandwidthRateLimitInterval, BandwidthRateLimitIntervalOutput]


# This class is the input for the 'create_gateway' function.
class CreateGatewayInput(BaseValidatorModel):
    ActivationKey: str
    GatewayDisplayName: str
    GatewayType: Literal['BACKUP_VM']
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'import_hypervisor_configuration' function.
class ImportHypervisorConfigurationInput(BaseValidatorModel):
    Host: str
    Name: str
    KmsKeyArn: Optional[str] = None
    Password: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Username: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'tag_resource' function.
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


# This class is the output for the 'list_gateways' function.
class ListGatewaysOutput(BaseValidatorModel):
    Gateways: List[Gateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_hypervisor' function.
class GetHypervisorOutput(BaseValidatorModel):
    Hypervisor: HypervisorDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_hypervisor_property_mappings' function.
class GetHypervisorPropertyMappingsOutput(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMapping]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_hypervisor_property_mappings' function.
class PutHypervisorPropertyMappingsInput(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMapping]


# This class is the output for the 'list_hypervisors' function.
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


# This class is the output for the 'list_virtual_machines' function.
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


# This class is the input for the 'put_bandwidth_rate_limit_schedule' function.
class PutBandwidthRateLimitScheduleInput(BaseValidatorModel):
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalUnion]
    GatewayArn: str


# This class is the output for the 'get_gateway' function.
class GetGatewayOutput(BaseValidatorModel):
    Gateway: GatewayDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_virtual_machine' function.
class GetVirtualMachineOutput(BaseValidatorModel):
    VirtualMachine: VirtualMachineDetails
    ResponseMetadata: ResponseMetadata