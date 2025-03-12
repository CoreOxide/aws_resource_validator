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
from aws_resource_validator.pydantic_models.backup_gateway_constants import *

class AssociateGatewayToServerInputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ServerArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BandwidthRateLimitIntervalOutputTypeDef(BaseValidatorModel):
    DaysOfWeek: List[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None


class BandwidthRateLimitIntervalTypeDef(BaseValidatorModel):
    DaysOfWeek: Sequence[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class DeleteGatewayInputTypeDef(BaseValidatorModel):
    GatewayArn: str


class DeleteHypervisorInputTypeDef(BaseValidatorModel):
    HypervisorArn: str


class DisassociateGatewayFromServerInputTypeDef(BaseValidatorModel):
    GatewayArn: str


class MaintenanceStartTimeTypeDef(BaseValidatorModel):
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None


class GatewayTypeDef(BaseValidatorModel):
    GatewayArn: Optional[str] = None
    GatewayDisplayName: Optional[str] = None
    GatewayType: Optional[Literal["BACKUP_VM"]] = None
    HypervisorId: Optional[str] = None
    LastSeenTime: Optional[datetime] = None


class GetBandwidthRateLimitScheduleInputTypeDef(BaseValidatorModel):
    GatewayArn: str


class GetGatewayInputTypeDef(BaseValidatorModel):
    GatewayArn: str


class GetHypervisorInputTypeDef(BaseValidatorModel):
    HypervisorArn: str


class HypervisorDetailsTypeDef(BaseValidatorModel):
    Host: Optional[str] = None
    HypervisorArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastSuccessfulMetadataSyncTime: Optional[datetime] = None
    LatestMetadataSyncStatus: Optional[SyncMetadataStatusType] = None
    LatestMetadataSyncStatusMessage: Optional[str] = None
    LogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[HypervisorStateType] = None


class GetHypervisorPropertyMappingsInputTypeDef(BaseValidatorModel):
    HypervisorArn: str


class VmwareToAwsTagMappingTypeDef(BaseValidatorModel):
    AwsTagKey: str
    AwsTagValue: str
    VmwareCategory: str
    VmwareTagName: str


class GetVirtualMachineInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class HypervisorTypeDef(BaseValidatorModel):
    Host: Optional[str] = None
    HypervisorArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[HypervisorStateType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListGatewaysInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHypervisorsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListVirtualMachinesInputTypeDef(BaseValidatorModel):
    HypervisorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class VirtualMachineTypeDef(BaseValidatorModel):
    HostName: Optional[str] = None
    HypervisorId: Optional[str] = None
    LastBackupDate: Optional[datetime] = None
    Name: Optional[str] = None
    Path: Optional[str] = None
    ResourceArn: Optional[str] = None


class PutMaintenanceStartTimeInputTypeDef(BaseValidatorModel):
    GatewayArn: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None


class StartVirtualMachinesMetadataSyncInputTypeDef(BaseValidatorModel):
    HypervisorArn: str


class TestHypervisorConfigurationInputTypeDef(BaseValidatorModel):
    GatewayArn: str
    Host: str
    Password: Optional[str] = None
    Username: Optional[str] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateGatewayInformationInputTypeDef(BaseValidatorModel):
    GatewayArn: str
    GatewayDisplayName: Optional[str] = None


class UpdateGatewaySoftwareNowInputTypeDef(BaseValidatorModel):
    GatewayArn: str


class UpdateHypervisorInputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    Host: Optional[str] = None
    LogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    Password: Optional[str] = None
    Username: Optional[str] = None


class VmwareTagTypeDef(BaseValidatorModel):
    VmwareCategory: Optional[str] = None
    VmwareTagDescription: Optional[str] = None
    VmwareTagName: Optional[str] = None


class AssociateGatewayToServerOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGatewayOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteGatewayOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteHypervisorOutputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateGatewayFromServerOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportHypervisorConfigurationOutputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutBandwidthRateLimitScheduleOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutHypervisorPropertyMappingsOutputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutMaintenanceStartTimeOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartVirtualMachinesMetadataSyncOutputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UntagResourceOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGatewayInformationOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGatewaySoftwareNowOutputTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateHypervisorOutputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBandwidthRateLimitScheduleOutputTypeDef(BaseValidatorModel):
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutputTypeDef]
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGatewayInputTypeDef(BaseValidatorModel):
    ActivationKey: str
    GatewayDisplayName: str
    GatewayType: Literal["BACKUP_VM"]
    Tags: Optional[Sequence[TagTypeDef]] = None


class ImportHypervisorConfigurationInputTypeDef(BaseValidatorModel):
    Host: str
    Name: str
    KmsKeyArn: Optional[str] = None
    Password: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Username: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class GatewayDetailsTypeDef(BaseValidatorModel):
    GatewayArn: Optional[str] = None
    GatewayDisplayName: Optional[str] = None
    GatewayType: Optional[Literal["BACKUP_VM"]] = None
    HypervisorId: Optional[str] = None
    LastSeenTime: Optional[datetime] = None
    MaintenanceStartTime: Optional[MaintenanceStartTimeTypeDef] = None
    NextUpdateAvailabilityTime: Optional[datetime] = None
    VpcEndpoint: Optional[str] = None


class ListGatewaysOutputTypeDef(BaseValidatorModel):
    Gateways: List[GatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetHypervisorOutputTypeDef(BaseValidatorModel):
    Hypervisor: HypervisorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetHypervisorPropertyMappingsOutputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutHypervisorPropertyMappingsInputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: Sequence[VmwareToAwsTagMappingTypeDef]


class ListHypervisorsOutputTypeDef(BaseValidatorModel):
    Hypervisors: List[HypervisorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGatewaysInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHypervisorsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualMachinesInputPaginateTypeDef(BaseValidatorModel):
    HypervisorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualMachinesOutputTypeDef(BaseValidatorModel):
    VirtualMachines: List[VirtualMachineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class VirtualMachineDetailsTypeDef(BaseValidatorModel):
    HostName: Optional[str] = None
    HypervisorId: Optional[str] = None
    LastBackupDate: Optional[datetime] = None
    Name: Optional[str] = None
    Path: Optional[str] = None
    ResourceArn: Optional[str] = None
    VmwareTags: Optional[List[VmwareTagTypeDef]] = None


class BandwidthRateLimitIntervalUnionTypeDef(BaseValidatorModel):
    pass


class PutBandwidthRateLimitScheduleInputTypeDef(BaseValidatorModel):
    BandwidthRateLimitIntervals: Sequence[BandwidthRateLimitIntervalUnionTypeDef]
    GatewayArn: str


class GetGatewayOutputTypeDef(BaseValidatorModel):
    Gateway: GatewayDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetVirtualMachineOutputTypeDef(BaseValidatorModel):
    VirtualMachine: VirtualMachineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


