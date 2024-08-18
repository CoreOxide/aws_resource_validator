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
from aws_resource_validator.pydantic_models.backup_gateway_constants import *

class AssociateGatewayToServerInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str
    ServerArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BandwidthRateLimitIntervalTypeDef(BaseValidatorModel):
    DaysOfWeek: List[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class DeleteGatewayInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str

class DeleteHypervisorInputRequestTypeDef(BaseValidatorModel):
    HypervisorArn: str

class DisassociateGatewayFromServerInputRequestTypeDef(BaseValidatorModel):
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

class GetBandwidthRateLimitScheduleInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str

class GetGatewayInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str

class GetHypervisorInputRequestTypeDef(BaseValidatorModel):
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

class GetHypervisorPropertyMappingsInputRequestTypeDef(BaseValidatorModel):
    HypervisorArn: str

class VmwareToAwsTagMappingTypeDef(BaseValidatorModel):
    AwsTagKey: str
    AwsTagValue: str
    VmwareCategory: str
    VmwareTagName: str

class GetVirtualMachineInputRequestTypeDef(BaseValidatorModel):
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

class ListGatewaysInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHypervisorsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListVirtualMachinesInputRequestTypeDef(BaseValidatorModel):
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

class PutMaintenanceStartTimeInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None

class StartVirtualMachinesMetadataSyncInputRequestTypeDef(BaseValidatorModel):
    HypervisorArn: str

class TestHypervisorConfigurationInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str
    Host: str
    Password: Optional[str] = None
    Username: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateGatewayInformationInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str
    GatewayDisplayName: Optional[str] = None

class UpdateGatewaySoftwareNowInputRequestTypeDef(BaseValidatorModel):
    GatewayArn: str

class UpdateHypervisorInputRequestTypeDef(BaseValidatorModel):
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
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalTypeDef]
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutBandwidthRateLimitScheduleInputRequestTypeDef(BaseValidatorModel):
    BandwidthRateLimitIntervals: Sequence[BandwidthRateLimitIntervalTypeDef]
    GatewayArn: str

class CreateGatewayInputRequestTypeDef(BaseValidatorModel):
    ActivationKey: str
    GatewayDisplayName: str
    GatewayType: Literal["BACKUP_VM"]
    Tags: Optional[Sequence[TagTypeDef]] = None

class ImportHypervisorConfigurationInputRequestTypeDef(BaseValidatorModel):
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

class TagResourceInputRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHypervisorOutputTypeDef(BaseValidatorModel):
    Hypervisor: HypervisorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHypervisorPropertyMappingsOutputTypeDef(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutHypervisorPropertyMappingsInputRequestTypeDef(BaseValidatorModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: Sequence[VmwareToAwsTagMappingTypeDef]

class ListHypervisorsOutputTypeDef(BaseValidatorModel):
    Hypervisors: List[HypervisorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGatewaysInputListGatewaysPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHypervisorsInputListHypervisorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualMachinesInputListVirtualMachinesPaginateTypeDef(BaseValidatorModel):
    HypervisorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualMachinesOutputTypeDef(BaseValidatorModel):
    NextToken: str
    VirtualMachines: List[VirtualMachineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualMachineDetailsTypeDef(BaseValidatorModel):
    HostName: Optional[str] = None
    HypervisorId: Optional[str] = None
    LastBackupDate: Optional[datetime] = None
    Name: Optional[str] = None
    Path: Optional[str] = None
    ResourceArn: Optional[str] = None
    VmwareTags: Optional[List[VmwareTagTypeDef]] = None

class GetGatewayOutputTypeDef(BaseValidatorModel):
    Gateway: GatewayDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVirtualMachineOutputTypeDef(BaseValidatorModel):
    VirtualMachine: VirtualMachineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

