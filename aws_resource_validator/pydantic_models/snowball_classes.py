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
from aws_resource_validator.pydantic_models.snowball_constants import *

class AddressTypeDef(BaseModel):
    AddressId: Optional[str] = None
    Name: Optional[str] = None
    Company: Optional[str] = None
    Street1: Optional[str] = None
    Street2: Optional[str] = None
    Street3: Optional[str] = None
    City: Optional[str] = None
    StateOrProvince: Optional[str] = None
    PrefectureOrDistrict: Optional[str] = None
    Landmark: Optional[str] = None
    Country: Optional[str] = None
    PostalCode: Optional[str] = None
    PhoneNumber: Optional[str] = None
    IsRestricted: Optional[bool] = None
    Type: Optional[AddressTypeType] = None

class CancelClusterRequestRequestTypeDef(BaseModel):
    ClusterId: str

class CancelJobRequestRequestTypeDef(BaseModel):
    JobId: str

class ClusterListEntryTypeDef(BaseModel):
    ClusterId: Optional[str] = None
    ClusterState: Optional[ClusterStateType] = None
    CreationDate: Optional[datetime] = None
    Description: Optional[str] = None

class NotificationOutputTypeDef(BaseModel):
    SnsTopicARN: Optional[str] = None
    JobStatesToNotify: Optional[List[JobStateType]] = None
    NotifyAll: Optional[bool] = None
    DevicePickupSnsTopicARN: Optional[str] = None

class CompatibleImageTypeDef(BaseModel):
    AmiId: Optional[str] = None
    Name: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class NotificationTypeDef(BaseModel):
    SnsTopicARN: Optional[str] = None
    JobStatesToNotify: Optional[Sequence[JobStateType]] = None
    NotifyAll: Optional[bool] = None
    DevicePickupSnsTopicARN: Optional[str] = None

class JobListEntryTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobState: Optional[JobStateType] = None
    IsMaster: Optional[bool] = None
    JobType: Optional[JobTypeType] = None
    SnowballType: Optional[SnowballTypeType] = None
    CreationDate: Optional[datetime] = None
    Description: Optional[str] = None

class CreateLongTermPricingRequestRequestTypeDef(BaseModel):
    LongTermPricingType: LongTermPricingTypeType
    SnowballType: SnowballTypeType
    IsLongTermPricingAutoRenew: Optional[bool] = None

class CreateReturnShippingLabelRequestRequestTypeDef(BaseModel):
    JobId: str
    ShippingOption: Optional[ShippingOptionType] = None

class DataTransferTypeDef(BaseModel):
    BytesTransferred: Optional[int] = None
    ObjectsTransferred: Optional[int] = None
    TotalBytes: Optional[int] = None
    TotalObjects: Optional[int] = None

class ServiceVersionTypeDef(BaseModel):
    Version: Optional[str] = None

class DescribeAddressRequestRequestTypeDef(BaseModel):
    AddressId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAddressesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeClusterRequestRequestTypeDef(BaseModel):
    ClusterId: str

class DescribeJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeReturnShippingLabelRequestRequestTypeDef(BaseModel):
    JobId: str

class EKSOnDeviceServiceConfigurationTypeDef(BaseModel):
    KubernetesVersion: Optional[str] = None
    EKSAnywhereVersion: Optional[str] = None

class Ec2AmiResourceTypeDef(BaseModel):
    AmiId: str
    SnowballAmiId: Optional[str] = None

class EventTriggerDefinitionTypeDef(BaseModel):
    EventResourceARN: Optional[str] = None

class GetJobManifestRequestRequestTypeDef(BaseModel):
    JobId: str

class GetJobUnlockCodeRequestRequestTypeDef(BaseModel):
    JobId: str

class GetSoftwareUpdatesRequestRequestTypeDef(BaseModel):
    JobId: str

class INDTaxDocumentsTypeDef(BaseModel):
    GSTIN: Optional[str] = None

class JobLogsTypeDef(BaseModel):
    JobCompletionReportURI: Optional[str] = None
    JobSuccessLogURI: Optional[str] = None
    JobFailureLogURI: Optional[str] = None

class PickupDetailsOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    IdentificationNumber: Optional[str] = None
    IdentificationExpirationDate: Optional[datetime] = None
    IdentificationIssuingOrg: Optional[str] = None
    DevicePickupId: Optional[str] = None

class KeyRangeTypeDef(BaseModel):
    BeginMarker: Optional[str] = None
    EndMarker: Optional[str] = None

class ListClusterJobsRequestRequestTypeDef(BaseModel):
    ClusterId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClustersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCompatibleImagesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLongTermPricingRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LongTermPricingListEntryTypeDef(BaseModel):
    LongTermPricingId: Optional[str] = None
    LongTermPricingEndDate: Optional[datetime] = None
    LongTermPricingStartDate: Optional[datetime] = None
    LongTermPricingType: Optional[LongTermPricingTypeType] = None
    CurrentActiveJob: Optional[str] = None
    ReplacementJob: Optional[str] = None
    IsLongTermPricingAutoRenew: Optional[bool] = None
    LongTermPricingStatus: Optional[str] = None
    SnowballType: Optional[SnowballTypeType] = None
    JobIds: Optional[List[str]] = None

class ListPickupLocationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NFSOnDeviceServiceConfigurationTypeDef(BaseModel):
    StorageLimit: Optional[int] = None
    StorageUnit: Optional[Literal["TB"]] = None

class S3OnDeviceServiceConfigurationTypeDef(BaseModel):
    StorageLimit: Optional[float] = None
    StorageUnit: Optional[Literal["TB"]] = None
    ServiceSize: Optional[int] = None
    FaultTolerance: Optional[int] = None

class TGWOnDeviceServiceConfigurationTypeDef(BaseModel):
    StorageLimit: Optional[int] = None
    StorageUnit: Optional[Literal["TB"]] = None

class TargetOnDeviceServiceTypeDef(BaseModel):
    ServiceName: Optional[DeviceServiceNameType] = None
    TransferOption: Optional[TransferOptionType] = None

class ShipmentTypeDef(BaseModel):
    Status: Optional[str] = None
    TrackingNumber: Optional[str] = None

class WirelessConnectionTypeDef(BaseModel):
    IsWifiEnabled: Optional[bool] = None

class UpdateJobShipmentStateRequestRequestTypeDef(BaseModel):
    JobId: str
    ShipmentState: ShipmentStateType

class UpdateLongTermPricingRequestRequestTypeDef(BaseModel):
    LongTermPricingId: str
    ReplacementJob: Optional[str] = None
    IsLongTermPricingAutoRenew: Optional[bool] = None

class CreateAddressRequestRequestTypeDef(BaseModel):
    Address: AddressTypeDef

class CreateAddressResultTypeDef(BaseModel):
    AddressId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResultTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLongTermPricingResultTypeDef(BaseModel):
    LongTermPricingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReturnShippingLabelResultTypeDef(BaseModel):
    Status: ShippingLabelStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressResultTypeDef(BaseModel):
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressesResultTypeDef(BaseModel):
    Addresses: List[AddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReturnShippingLabelResultTypeDef(BaseModel):
    Status: ShippingLabelStatusType
    ExpirationDate: datetime
    ReturnShippingLabelURI: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobManifestResultTypeDef(BaseModel):
    ManifestURI: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobUnlockCodeResultTypeDef(BaseModel):
    UnlockCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnowballUsageResultTypeDef(BaseModel):
    SnowballLimit: int
    SnowballsInUse: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetSoftwareUpdatesResultTypeDef(BaseModel):
    UpdatesURI: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersResultTypeDef(BaseModel):
    ClusterListEntries: List[ClusterListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCompatibleImagesResultTypeDef(BaseModel):
    CompatibleImages: List[CompatibleImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPickupLocationsResultTypeDef(BaseModel):
    Addresses: List[AddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateClusterResultTypeDef(BaseModel):
    ClusterId: str
    JobListEntries: List[JobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListClusterJobsResultTypeDef(BaseModel):
    JobListEntries: List[JobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListJobsResultTypeDef(BaseModel):
    JobListEntries: List[JobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DependentServiceTypeDef(BaseModel):
    ServiceName: Optional[ServiceNameType] = None
    ServiceVersion: Optional[ServiceVersionTypeDef] = None

class DescribeAddressesRequestDescribeAddressesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClusterJobsRequestListClusterJobsPaginateTypeDef(BaseModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLongTermPricingRequestListLongTermPricingPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LambdaResourceOutputTypeDef(BaseModel):
    LambdaArn: Optional[str] = None
    EventTriggers: Optional[List[EventTriggerDefinitionTypeDef]] = None

class LambdaResourceTypeDef(BaseModel):
    LambdaArn: Optional[str] = None
    EventTriggers: Optional[Sequence[EventTriggerDefinitionTypeDef]] = None

class TaxDocumentsTypeDef(BaseModel):
    IND: Optional[INDTaxDocumentsTypeDef] = None

class ListLongTermPricingResultTypeDef(BaseModel):
    LongTermPricingEntries: List[LongTermPricingListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OnDeviceServiceConfigurationTypeDef(BaseModel):
    NFSOnDeviceService: Optional[NFSOnDeviceServiceConfigurationTypeDef] = None
    TGWOnDeviceService: Optional[TGWOnDeviceServiceConfigurationTypeDef] = None
    EKSOnDeviceService: Optional[EKSOnDeviceServiceConfigurationTypeDef] = None
    S3OnDeviceService: Optional[S3OnDeviceServiceConfigurationTypeDef] = None

class PickupDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    IdentificationNumber: Optional[str] = None
    IdentificationExpirationDate: Optional[TimestampTypeDef] = None
    IdentificationIssuingOrg: Optional[str] = None
    DevicePickupId: Optional[str] = None

class S3ResourceOutputTypeDef(BaseModel):
    BucketArn: Optional[str] = None
    KeyRange: Optional[KeyRangeTypeDef] = None
    TargetOnDeviceServices: Optional[List[TargetOnDeviceServiceTypeDef]] = None

class S3ResourceTypeDef(BaseModel):
    BucketArn: Optional[str] = None
    KeyRange: Optional[KeyRangeTypeDef] = None
    TargetOnDeviceServices: Optional[Sequence[TargetOnDeviceServiceTypeDef]] = None

class ShippingDetailsTypeDef(BaseModel):
    ShippingOption: Optional[ShippingOptionType] = None
    InboundShipment: Optional[ShipmentTypeDef] = None
    OutboundShipment: Optional[ShipmentTypeDef] = None

class SnowconeDeviceConfigurationTypeDef(BaseModel):
    WirelessConnection: Optional[WirelessConnectionTypeDef] = None

class ListServiceVersionsRequestRequestTypeDef(BaseModel):
    ServiceName: ServiceNameType
    DependentServices: Optional[Sequence[DependentServiceTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServiceVersionsResultTypeDef(BaseModel):
    ServiceVersions: List[ServiceVersionTypeDef]
    ServiceName: ServiceNameType
    DependentServices: List[DependentServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class JobResourceOutputTypeDef(BaseModel):
    S3Resources: Optional[List[S3ResourceOutputTypeDef]] = None
    LambdaResources: Optional[List[LambdaResourceOutputTypeDef]] = None
    Ec2AmiResources: Optional[List[Ec2AmiResourceTypeDef]] = None

class JobResourceTypeDef(BaseModel):
    S3Resources: Optional[Sequence[S3ResourceTypeDef]] = None
    LambdaResources: Optional[Sequence[LambdaResourceTypeDef]] = None
    Ec2AmiResources: Optional[Sequence[Ec2AmiResourceTypeDef]] = None

class DeviceConfigurationTypeDef(BaseModel):
    SnowconeDeviceConfiguration: Optional[SnowconeDeviceConfigurationTypeDef] = None

class ClusterMetadataTypeDef(BaseModel):
    ClusterId: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    ClusterState: Optional[ClusterStateType] = None
    JobType: Optional[JobTypeType] = None
    SnowballType: Optional[SnowballTypeType] = None
    CreationDate: Optional[datetime] = None
    Resources: Optional[JobResourceOutputTypeDef] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationOutputTypeDef] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocumentsTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None

class CreateClusterRequestRequestTypeDef(BaseModel):
    JobType: JobTypeType
    AddressId: str
    SnowballType: SnowballTypeType
    ShippingOption: ShippingOptionType
    Resources: Optional[JobResourceTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    Description: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    Notification: Optional[NotificationTypeDef] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocumentsTypeDef] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    InitialClusterSize: Optional[int] = None
    ForceCreateJobs: Optional[bool] = None
    LongTermPricingIds: Optional[Sequence[str]] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None

class UpdateClusterRequestRequestTypeDef(BaseModel):
    ClusterId: str
    RoleARN: Optional[str] = None
    Description: Optional[str] = None
    Resources: Optional[JobResourceTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationTypeDef] = None
    ForwardingAddressId: Optional[str] = None

class UpdateJobRequestRequestTypeDef(BaseModel):
    JobId: str
    RoleARN: Optional[str] = None
    Notification: Optional[NotificationTypeDef] = None
    Resources: Optional[JobResourceTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Description: Optional[str] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    ForwardingAddressId: Optional[str] = None
    PickupDetails: Optional[PickupDetailsTypeDef] = None

class CreateJobRequestRequestTypeDef(BaseModel):
    JobType: Optional[JobTypeType] = None
    Resources: Optional[JobResourceTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    Description: Optional[str] = None
    AddressId: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationTypeDef] = None
    ClusterId: Optional[str] = None
    SnowballType: Optional[SnowballTypeType] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocumentsTypeDef] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeDef] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    LongTermPricingId: Optional[str] = None
    ImpactLevel: Optional[ImpactLevelType] = None
    PickupDetails: Optional[PickupDetailsTypeDef] = None

class JobMetadataTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobState: Optional[JobStateType] = None
    JobType: Optional[JobTypeType] = None
    SnowballType: Optional[SnowballTypeType] = None
    CreationDate: Optional[datetime] = None
    Resources: Optional[JobResourceOutputTypeDef] = None
    Description: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    AddressId: Optional[str] = None
    ShippingDetails: Optional[ShippingDetailsTypeDef] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    Notification: Optional[NotificationOutputTypeDef] = None
    DataTransferProgress: Optional[DataTransferTypeDef] = None
    JobLogInfo: Optional[JobLogsTypeDef] = None
    ClusterId: Optional[str] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocumentsTypeDef] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeDef] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    LongTermPricingId: Optional[str] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    ImpactLevel: Optional[ImpactLevelType] = None
    PickupDetails: Optional[PickupDetailsOutputTypeDef] = None
    SnowballId: Optional[str] = None

class DescribeClusterResultTypeDef(BaseModel):
    ClusterMetadata: ClusterMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobResultTypeDef(BaseModel):
    JobMetadata: JobMetadataTypeDef
    SubJobMetadata: List[JobMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

