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
from aws_resource_validator.pydantic_models.snowball_constants import *

class CancelClusterRequestTypeDef(BaseValidatorModel):
    ClusterId: str


class CancelJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class ClusterListEntryTypeDef(BaseValidatorModel):
    ClusterId: Optional[str] = None
    ClusterState: Optional[ClusterStateType] = None
    CreationDate: Optional[datetime] = None
    Description: Optional[str] = None


class NotificationOutputTypeDef(BaseValidatorModel):
    SnsTopicARN: Optional[str] = None
    JobStatesToNotify: Optional[List[JobStateType]] = None
    NotifyAll: Optional[bool] = None
    DevicePickupSnsTopicARN: Optional[str] = None


class CompatibleImageTypeDef(BaseValidatorModel):
    AmiId: Optional[str] = None
    Name: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class JobListEntryTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobState: Optional[JobStateType] = None
    IsMaster: Optional[bool] = None
    JobType: Optional[JobTypeType] = None
    SnowballType: Optional[SnowballTypeType] = None
    CreationDate: Optional[datetime] = None
    Description: Optional[str] = None


class CreateLongTermPricingRequestTypeDef(BaseValidatorModel):
    LongTermPricingType: LongTermPricingTypeType
    SnowballType: SnowballTypeType
    IsLongTermPricingAutoRenew: Optional[bool] = None


class CreateReturnShippingLabelRequestTypeDef(BaseValidatorModel):
    JobId: str
    ShippingOption: Optional[ShippingOptionType] = None


class DataTransferTypeDef(BaseValidatorModel):
    BytesTransferred: Optional[int] = None
    ObjectsTransferred: Optional[int] = None
    TotalBytes: Optional[int] = None
    TotalObjects: Optional[int] = None


class ServiceVersionTypeDef(BaseValidatorModel):
    Version: Optional[str] = None


class DescribeAddressRequestTypeDef(BaseValidatorModel):
    AddressId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAddressesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeClusterRequestTypeDef(BaseValidatorModel):
    ClusterId: str


class DescribeJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeReturnShippingLabelRequestTypeDef(BaseValidatorModel):
    JobId: str


class EKSOnDeviceServiceConfigurationTypeDef(BaseValidatorModel):
    KubernetesVersion: Optional[str] = None
    EKSAnywhereVersion: Optional[str] = None


class Ec2AmiResourceTypeDef(BaseValidatorModel):
    AmiId: str
    SnowballAmiId: Optional[str] = None


class EventTriggerDefinitionTypeDef(BaseValidatorModel):
    EventResourceARN: Optional[str] = None


class GetJobManifestRequestTypeDef(BaseValidatorModel):
    JobId: str


class GetJobUnlockCodeRequestTypeDef(BaseValidatorModel):
    JobId: str


class GetSoftwareUpdatesRequestTypeDef(BaseValidatorModel):
    JobId: str


class INDTaxDocumentsTypeDef(BaseValidatorModel):
    GSTIN: Optional[str] = None


class JobLogsTypeDef(BaseValidatorModel):
    JobCompletionReportURI: Optional[str] = None
    JobSuccessLogURI: Optional[str] = None
    JobFailureLogURI: Optional[str] = None


class PickupDetailsOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    IdentificationNumber: Optional[str] = None
    IdentificationExpirationDate: Optional[datetime] = None
    IdentificationIssuingOrg: Optional[str] = None
    DevicePickupId: Optional[str] = None


class KeyRangeTypeDef(BaseValidatorModel):
    BeginMarker: Optional[str] = None
    EndMarker: Optional[str] = None


class ListClusterJobsRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClustersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCompatibleImagesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLongTermPricingRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LongTermPricingListEntryTypeDef(BaseValidatorModel):
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


class ListPickupLocationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NFSOnDeviceServiceConfigurationTypeDef(BaseValidatorModel):
    StorageLimit: Optional[int] = None
    StorageUnit: Optional[Literal["TB"]] = None


class NotificationTypeDef(BaseValidatorModel):
    SnsTopicARN: Optional[str] = None
    JobStatesToNotify: Optional[Sequence[JobStateType]] = None
    NotifyAll: Optional[bool] = None
    DevicePickupSnsTopicARN: Optional[str] = None


class S3OnDeviceServiceConfigurationTypeDef(BaseValidatorModel):
    StorageLimit: Optional[float] = None
    StorageUnit: Optional[Literal["TB"]] = None
    ServiceSize: Optional[int] = None
    FaultTolerance: Optional[int] = None


class TGWOnDeviceServiceConfigurationTypeDef(BaseValidatorModel):
    StorageLimit: Optional[int] = None
    StorageUnit: Optional[Literal["TB"]] = None


class ShipmentTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    TrackingNumber: Optional[str] = None


class WirelessConnectionTypeDef(BaseValidatorModel):
    IsWifiEnabled: Optional[bool] = None


class UpdateJobShipmentStateRequestTypeDef(BaseValidatorModel):
    JobId: str
    ShipmentState: ShipmentStateType


class UpdateLongTermPricingRequestTypeDef(BaseValidatorModel):
    LongTermPricingId: str
    ReplacementJob: Optional[str] = None
    IsLongTermPricingAutoRenew: Optional[bool] = None


class AddressTypeDef(BaseValidatorModel):
    pass


class CreateAddressRequestTypeDef(BaseValidatorModel):
    Address: AddressTypeDef


class CreateAddressResultTypeDef(BaseValidatorModel):
    AddressId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobResultTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLongTermPricingResultTypeDef(BaseValidatorModel):
    LongTermPricingId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateReturnShippingLabelResultTypeDef(BaseValidatorModel):
    Status: ShippingLabelStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAddressResultTypeDef(BaseValidatorModel):
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAddressesResultTypeDef(BaseValidatorModel):
    Addresses: List[AddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeReturnShippingLabelResultTypeDef(BaseValidatorModel):
    Status: ShippingLabelStatusType
    ExpirationDate: datetime
    ReturnShippingLabelURI: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobManifestResultTypeDef(BaseValidatorModel):
    ManifestURI: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobUnlockCodeResultTypeDef(BaseValidatorModel):
    UnlockCode: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSnowballUsageResultTypeDef(BaseValidatorModel):
    SnowballLimit: int
    SnowballsInUse: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetSoftwareUpdatesResultTypeDef(BaseValidatorModel):
    UpdatesURI: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListClustersResultTypeDef(BaseValidatorModel):
    ClusterListEntries: List[ClusterListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCompatibleImagesResultTypeDef(BaseValidatorModel):
    CompatibleImages: List[CompatibleImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPickupLocationsResultTypeDef(BaseValidatorModel):
    Addresses: List[AddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateClusterResultTypeDef(BaseValidatorModel):
    ClusterId: str
    JobListEntries: List[JobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListClusterJobsResultTypeDef(BaseValidatorModel):
    JobListEntries: List[JobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListJobsResultTypeDef(BaseValidatorModel):
    JobListEntries: List[JobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeAddressesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClusterJobsRequestPaginateTypeDef(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClustersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCompatibleImagesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLongTermPricingRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class LambdaResourceOutputTypeDef(BaseValidatorModel):
    LambdaArn: Optional[str] = None
    EventTriggers: Optional[List[EventTriggerDefinitionTypeDef]] = None


class LambdaResourceTypeDef(BaseValidatorModel):
    LambdaArn: Optional[str] = None
    EventTriggers: Optional[Sequence[EventTriggerDefinitionTypeDef]] = None


class TaxDocumentsTypeDef(BaseValidatorModel):
    IND: Optional[INDTaxDocumentsTypeDef] = None


class ListLongTermPricingResultTypeDef(BaseValidatorModel):
    LongTermPricingEntries: List[LongTermPricingListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class OnDeviceServiceConfigurationTypeDef(BaseValidatorModel):
    NFSOnDeviceService: Optional[NFSOnDeviceServiceConfigurationTypeDef] = None
    TGWOnDeviceService: Optional[TGWOnDeviceServiceConfigurationTypeDef] = None
    EKSOnDeviceService: Optional[EKSOnDeviceServiceConfigurationTypeDef] = None
    S3OnDeviceService: Optional[S3OnDeviceServiceConfigurationTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class PickupDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    IdentificationNumber: Optional[str] = None
    IdentificationExpirationDate: Optional[TimestampTypeDef] = None
    IdentificationIssuingOrg: Optional[str] = None
    DevicePickupId: Optional[str] = None


class TargetOnDeviceServiceTypeDef(BaseValidatorModel):
    pass


class S3ResourceOutputTypeDef(BaseValidatorModel):
    BucketArn: Optional[str] = None
    KeyRange: Optional[KeyRangeTypeDef] = None
    TargetOnDeviceServices: Optional[List[TargetOnDeviceServiceTypeDef]] = None


class S3ResourceTypeDef(BaseValidatorModel):
    BucketArn: Optional[str] = None
    KeyRange: Optional[KeyRangeTypeDef] = None
    TargetOnDeviceServices: Optional[Sequence[TargetOnDeviceServiceTypeDef]] = None


class ShippingDetailsTypeDef(BaseValidatorModel):
    ShippingOption: Optional[ShippingOptionType] = None
    InboundShipment: Optional[ShipmentTypeDef] = None
    OutboundShipment: Optional[ShipmentTypeDef] = None


class SnowconeDeviceConfigurationTypeDef(BaseValidatorModel):
    WirelessConnection: Optional[WirelessConnectionTypeDef] = None


class JobResourceOutputTypeDef(BaseValidatorModel):
    S3Resources: Optional[List[S3ResourceOutputTypeDef]] = None
    LambdaResources: Optional[List[LambdaResourceOutputTypeDef]] = None
    Ec2AmiResources: Optional[List[Ec2AmiResourceTypeDef]] = None


class JobResourceTypeDef(BaseValidatorModel):
    S3Resources: Optional[Sequence[S3ResourceTypeDef]] = None
    LambdaResources: Optional[Sequence[LambdaResourceTypeDef]] = None
    Ec2AmiResources: Optional[Sequence[Ec2AmiResourceTypeDef]] = None


class DeviceConfigurationTypeDef(BaseValidatorModel):
    SnowconeDeviceConfiguration: Optional[SnowconeDeviceConfigurationTypeDef] = None


class ClusterMetadataTypeDef(BaseValidatorModel):
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


class JobMetadataTypeDef(BaseValidatorModel):
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


class DescribeClusterResultTypeDef(BaseValidatorModel):
    ClusterMetadata: ClusterMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JobResourceUnionTypeDef(BaseValidatorModel):
    pass


class NotificationUnionTypeDef(BaseValidatorModel):
    pass


class CreateClusterRequestTypeDef(BaseValidatorModel):
    JobType: JobTypeType
    AddressId: str
    SnowballType: SnowballTypeType
    ShippingOption: ShippingOptionType
    Resources: Optional[JobResourceUnionTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    Description: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    Notification: Optional[NotificationUnionTypeDef] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocumentsTypeDef] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    InitialClusterSize: Optional[int] = None
    ForceCreateJobs: Optional[bool] = None
    LongTermPricingIds: Optional[Sequence[str]] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None


class PickupDetailsUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobRequestTypeDef(BaseValidatorModel):
    JobType: Optional[JobTypeType] = None
    Resources: Optional[JobResourceUnionTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    Description: Optional[str] = None
    AddressId: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationUnionTypeDef] = None
    ClusterId: Optional[str] = None
    SnowballType: Optional[SnowballTypeType] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocumentsTypeDef] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeDef] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    LongTermPricingId: Optional[str] = None
    ImpactLevel: Optional[ImpactLevelType] = None
    PickupDetails: Optional[PickupDetailsUnionTypeDef] = None


class UpdateClusterRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    RoleARN: Optional[str] = None
    Description: Optional[str] = None
    Resources: Optional[JobResourceUnionTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationUnionTypeDef] = None
    ForwardingAddressId: Optional[str] = None


class UpdateJobRequestTypeDef(BaseValidatorModel):
    JobId: str
    RoleARN: Optional[str] = None
    Notification: Optional[NotificationUnionTypeDef] = None
    Resources: Optional[JobResourceUnionTypeDef] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfigurationTypeDef] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Description: Optional[str] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    ForwardingAddressId: Optional[str] = None
    PickupDetails: Optional[PickupDetailsUnionTypeDef] = None


class DescribeJobResultTypeDef(BaseValidatorModel):
    JobMetadata: JobMetadataTypeDef
    SubJobMetadata: List[JobMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


