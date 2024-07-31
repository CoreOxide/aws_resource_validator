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
from aws_resource_validator.pydantic_models.backup_gateway_constants import *

class AssociateGatewayToServerInputRequestTypeDef(BaseModel):
    GatewayArn: str
    ServerArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BandwidthRateLimitIntervalTypeDef(BaseModel):
    DaysOfWeek: List[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DeleteGatewayInputRequestTypeDef(BaseModel):
    GatewayArn: str

class DeleteHypervisorInputRequestTypeDef(BaseModel):
    HypervisorArn: str

class DisassociateGatewayFromServerInputRequestTypeDef(BaseModel):
    GatewayArn: str

class MaintenanceStartTimeTypeDef(BaseModel):
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None

class GatewayTypeDef(BaseModel):
    GatewayArn: Optional[str] = None
    GatewayDisplayName: Optional[str] = None
    GatewayType: Optional[Literal["BACKUP_VM"]] = None
    HypervisorId: Optional[str] = None
    LastSeenTime: Optional[datetime] = None

class GetBandwidthRateLimitScheduleInputRequestTypeDef(BaseModel):
    GatewayArn: str

class GetGatewayInputRequestTypeDef(BaseModel):
    GatewayArn: str

class GetHypervisorInputRequestTypeDef(BaseModel):
    HypervisorArn: str

class HypervisorDetailsTypeDef(BaseModel):
    Host: Optional[str] = None
    HypervisorArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastSuccessfulMetadataSyncTime: Optional[datetime] = None
    LatestMetadataSyncStatus: Optional[SyncMetadataStatusType] = None
    LatestMetadataSyncStatusMessage: Optional[str] = None
    LogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[HypervisorStateType] = None

class GetHypervisorPropertyMappingsInputRequestTypeDef(BaseModel):
    HypervisorArn: str

class VmwareToAwsTagMappingTypeDef(BaseModel):
    AwsTagKey: str
    AwsTagValue: str
    VmwareCategory: str
    VmwareTagName: str

class GetVirtualMachineInputRequestTypeDef(BaseModel):
    ResourceArn: str

class HypervisorTypeDef(BaseModel):
    Host: Optional[str] = None
    HypervisorArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[HypervisorStateType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListGatewaysInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHypervisorsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class ListVirtualMachinesInputRequestTypeDef(BaseModel):
    HypervisorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class VirtualMachineTypeDef(BaseModel):
    HostName: Optional[str] = None
    HypervisorId: Optional[str] = None
    LastBackupDate: Optional[datetime] = None
    Name: Optional[str] = None
    Path: Optional[str] = None
    ResourceArn: Optional[str] = None

class PutMaintenanceStartTimeInputRequestTypeDef(BaseModel):
    GatewayArn: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[int] = None

class StartVirtualMachinesMetadataSyncInputRequestTypeDef(BaseModel):
    HypervisorArn: str

class TestHypervisorConfigurationInputRequestTypeDef(BaseModel):
    GatewayArn: str
    Host: str
    Password: Optional[str] = None
    Username: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateGatewayInformationInputRequestTypeDef(BaseModel):
    GatewayArn: str
    GatewayDisplayName: Optional[str] = None

class UpdateGatewaySoftwareNowInputRequestTypeDef(BaseModel):
    GatewayArn: str

class UpdateHypervisorInputRequestTypeDef(BaseModel):
    HypervisorArn: str
    Host: Optional[str] = None
    LogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    Password: Optional[str] = None
    Username: Optional[str] = None

class VmwareTagTypeDef(BaseModel):
    VmwareCategory: Optional[str] = None
    VmwareTagDescription: Optional[str] = None
    VmwareTagName: Optional[str] = None

class AssociateGatewayToServerOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHypervisorOutputTypeDef(BaseModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateGatewayFromServerOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportHypervisorConfigurationOutputTypeDef(BaseModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutBandwidthRateLimitScheduleOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutHypervisorPropertyMappingsOutputTypeDef(BaseModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutMaintenanceStartTimeOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartVirtualMachinesMetadataSyncOutputTypeDef(BaseModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceOutputTypeDef(BaseModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceOutputTypeDef(BaseModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayInformationOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewaySoftwareNowOutputTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHypervisorOutputTypeDef(BaseModel):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBandwidthRateLimitScheduleOutputTypeDef(BaseModel):
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalTypeDef]
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutBandwidthRateLimitScheduleInputRequestTypeDef(BaseModel):
    BandwidthRateLimitIntervals: Sequence[BandwidthRateLimitIntervalTypeDef]
    GatewayArn: str

class CreateGatewayInputRequestTypeDef(BaseModel):
    ActivationKey: str
    GatewayDisplayName: str
    GatewayType: Literal["BACKUP_VM"]
    Tags: Optional[Sequence[TagTypeDef]] = None

class ImportHypervisorConfigurationInputRequestTypeDef(BaseModel):
    Host: str
    Name: str
    KmsKeyArn: Optional[str] = None
    Password: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Username: Optional[str] = None

class ListTagsForResourceOutputTypeDef(BaseModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class GatewayDetailsTypeDef(BaseModel):
    GatewayArn: Optional[str] = None
    GatewayDisplayName: Optional[str] = None
    GatewayType: Optional[Literal["BACKUP_VM"]] = None
    HypervisorId: Optional[str] = None
    LastSeenTime: Optional[datetime] = None
    MaintenanceStartTime: Optional[MaintenanceStartTimeTypeDef] = None
    NextUpdateAvailabilityTime: Optional[datetime] = None
    VpcEndpoint: Optional[str] = None

class ListGatewaysOutputTypeDef(BaseModel):
    Gateways: List[GatewayTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHypervisorOutputTypeDef(BaseModel):
    Hypervisor: HypervisorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHypervisorPropertyMappingsOutputTypeDef(BaseModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutHypervisorPropertyMappingsInputRequestTypeDef(BaseModel):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: Sequence[VmwareToAwsTagMappingTypeDef]

class ListHypervisorsOutputTypeDef(BaseModel):
    Hypervisors: List[HypervisorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGatewaysInputListGatewaysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHypervisorsInputListHypervisorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualMachinesInputListVirtualMachinesPaginateTypeDef(BaseModel):
    HypervisorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualMachinesOutputTypeDef(BaseModel):
    NextToken: str
    VirtualMachines: List[VirtualMachineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualMachineDetailsTypeDef(BaseModel):
    HostName: Optional[str] = None
    HypervisorId: Optional[str] = None
    LastBackupDate: Optional[datetime] = None
    Name: Optional[str] = None
    Path: Optional[str] = None
    ResourceArn: Optional[str] = None
    VmwareTags: Optional[List[VmwareTagTypeDef]] = None

class GetGatewayOutputTypeDef(BaseModel):
    Gateway: GatewayDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVirtualMachineOutputTypeDef(BaseModel):
    VirtualMachine: VirtualMachineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

