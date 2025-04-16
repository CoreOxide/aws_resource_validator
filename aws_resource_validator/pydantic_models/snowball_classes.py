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

class CancelClusterRequest(BaseValidatorModel):
    ClusterId: str


class CancelJobRequest(BaseValidatorModel):
    JobId: str


class ClusterListEntry(BaseValidatorModel):
    ClusterId: Optional[str] = None
    ClusterState: Optional[ClusterStateType] = None
    CreationDate: Optional[datetime] = None
    Description: Optional[str] = None


class NotificationOutput(BaseValidatorModel):
    SnsTopicARN: Optional[str] = None
    JobStatesToNotify: Optional[List[JobStateType]] = None
    NotifyAll: Optional[bool] = None
    DevicePickupSnsTopicARN: Optional[str] = None


class CompatibleImage(BaseValidatorModel):
    AmiId: Optional[str] = None
    Name: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class JobListEntry(BaseValidatorModel):
    JobId: Optional[str] = None
    JobState: Optional[JobStateType] = None
    IsMaster: Optional[bool] = None
    JobType: Optional[JobTypeType] = None
    SnowballType: Optional[SnowballTypeType] = None
    CreationDate: Optional[datetime] = None
    Description: Optional[str] = None


class CreateLongTermPricingRequest(BaseValidatorModel):
    LongTermPricingType: LongTermPricingTypeType
    SnowballType: SnowballTypeType
    IsLongTermPricingAutoRenew: Optional[bool] = None


class CreateReturnShippingLabelRequest(BaseValidatorModel):
    JobId: str
    ShippingOption: Optional[ShippingOptionType] = None


class DataTransfer(BaseValidatorModel):
    BytesTransferred: Optional[int] = None
    ObjectsTransferred: Optional[int] = None
    TotalBytes: Optional[int] = None
    TotalObjects: Optional[int] = None


class ServiceVersion(BaseValidatorModel):
    Version: Optional[str] = None


class DescribeAddressRequest(BaseValidatorModel):
    AddressId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAddressesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeClusterRequest(BaseValidatorModel):
    ClusterId: str


class DescribeJobRequest(BaseValidatorModel):
    JobId: str


class DescribeReturnShippingLabelRequest(BaseValidatorModel):
    JobId: str


class EKSOnDeviceServiceConfiguration(BaseValidatorModel):
    KubernetesVersion: Optional[str] = None
    EKSAnywhereVersion: Optional[str] = None


class Ec2AmiResource(BaseValidatorModel):
    AmiId: str
    SnowballAmiId: Optional[str] = None


class EventTriggerDefinition(BaseValidatorModel):
    EventResourceARN: Optional[str] = None


class GetJobManifestRequest(BaseValidatorModel):
    JobId: str


class GetJobUnlockCodeRequest(BaseValidatorModel):
    JobId: str


class GetSoftwareUpdatesRequest(BaseValidatorModel):
    JobId: str


class INDTaxDocuments(BaseValidatorModel):
    GSTIN: Optional[str] = None


class JobLogs(BaseValidatorModel):
    JobCompletionReportURI: Optional[str] = None
    JobSuccessLogURI: Optional[str] = None
    JobFailureLogURI: Optional[str] = None


class PickupDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    IdentificationNumber: Optional[str] = None
    IdentificationExpirationDate: Optional[datetime] = None
    IdentificationIssuingOrg: Optional[str] = None
    DevicePickupId: Optional[str] = None


class KeyRange(BaseValidatorModel):
    BeginMarker: Optional[str] = None
    EndMarker: Optional[str] = None


class ListClusterJobsRequest(BaseValidatorModel):
    ClusterId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClustersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCompatibleImagesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLongTermPricingRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LongTermPricingListEntry(BaseValidatorModel):
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


class ListPickupLocationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NFSOnDeviceServiceConfiguration(BaseValidatorModel):
    StorageLimit: Optional[int] = None
    StorageUnit: Optional[Literal["TB"]] = None


class Notification(BaseValidatorModel):
    SnsTopicARN: Optional[str] = None
    JobStatesToNotify: Optional[Sequence[JobStateType]] = None
    NotifyAll: Optional[bool] = None
    DevicePickupSnsTopicARN: Optional[str] = None


class S3OnDeviceServiceConfiguration(BaseValidatorModel):
    StorageLimit: Optional[float] = None
    StorageUnit: Optional[Literal["TB"]] = None
    ServiceSize: Optional[int] = None
    FaultTolerance: Optional[int] = None


class TGWOnDeviceServiceConfiguration(BaseValidatorModel):
    StorageLimit: Optional[int] = None
    StorageUnit: Optional[Literal["TB"]] = None


class Shipment(BaseValidatorModel):
    Status: Optional[str] = None
    TrackingNumber: Optional[str] = None


class WirelessConnection(BaseValidatorModel):
    IsWifiEnabled: Optional[bool] = None


class UpdateJobShipmentStateRequest(BaseValidatorModel):
    JobId: str
    ShipmentState: ShipmentStateType


class UpdateLongTermPricingRequest(BaseValidatorModel):
    LongTermPricingId: str
    ReplacementJob: Optional[str] = None
    IsLongTermPricingAutoRenew: Optional[bool] = None


class Address(BaseValidatorModel):
    pass


class CreateAddressRequest(BaseValidatorModel):
    Address: Address


class CreateAddressResult(BaseValidatorModel):
    AddressId: str
    ResponseMetadata: ResponseMetadata


class CreateJobResult(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class CreateLongTermPricingResult(BaseValidatorModel):
    LongTermPricingId: str
    ResponseMetadata: ResponseMetadata


class CreateReturnShippingLabelResult(BaseValidatorModel):
    Status: ShippingLabelStatusType
    ResponseMetadata: ResponseMetadata


class DescribeAddressResult(BaseValidatorModel):
    Address: Address
    ResponseMetadata: ResponseMetadata


class DescribeAddressesResult(BaseValidatorModel):
    Addresses: List[Address]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeReturnShippingLabelResult(BaseValidatorModel):
    Status: ShippingLabelStatusType
    ExpirationDate: datetime
    ReturnShippingLabelURI: str
    ResponseMetadata: ResponseMetadata


class GetJobManifestResult(BaseValidatorModel):
    ManifestURI: str
    ResponseMetadata: ResponseMetadata


class GetJobUnlockCodeResult(BaseValidatorModel):
    UnlockCode: str
    ResponseMetadata: ResponseMetadata


class GetSnowballUsageResult(BaseValidatorModel):
    SnowballLimit: int
    SnowballsInUse: int
    ResponseMetadata: ResponseMetadata


class GetSoftwareUpdatesResult(BaseValidatorModel):
    UpdatesURI: str
    ResponseMetadata: ResponseMetadata


class ListClustersResult(BaseValidatorModel):
    ClusterListEntries: List[ClusterListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCompatibleImagesResult(BaseValidatorModel):
    CompatibleImages: List[CompatibleImage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPickupLocationsResult(BaseValidatorModel):
    Addresses: List[Address]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateClusterResult(BaseValidatorModel):
    ClusterId: str
    JobListEntries: List[JobListEntry]
    ResponseMetadata: ResponseMetadata


class ListClusterJobsResult(BaseValidatorModel):
    JobListEntries: List[JobListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListJobsResult(BaseValidatorModel):
    JobListEntries: List[JobListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeAddressesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClusterJobsRequestPaginate(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCompatibleImagesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLongTermPricingRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class LambdaResourceOutput(BaseValidatorModel):
    LambdaArn: Optional[str] = None
    EventTriggers: Optional[List[EventTriggerDefinition]] = None


class LambdaResource(BaseValidatorModel):
    LambdaArn: Optional[str] = None
    EventTriggers: Optional[Sequence[EventTriggerDefinition]] = None


class TaxDocuments(BaseValidatorModel):
    IND: Optional[INDTaxDocuments] = None


class ListLongTermPricingResult(BaseValidatorModel):
    LongTermPricingEntries: List[LongTermPricingListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OnDeviceServiceConfiguration(BaseValidatorModel):
    NFSOnDeviceService: Optional[NFSOnDeviceServiceConfiguration] = None
    TGWOnDeviceService: Optional[TGWOnDeviceServiceConfiguration] = None
    EKSOnDeviceService: Optional[EKSOnDeviceServiceConfiguration] = None
    S3OnDeviceService: Optional[S3OnDeviceServiceConfiguration] = None


class Timestamp(BaseValidatorModel):
    pass


class PickupDetails(BaseValidatorModel):
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    IdentificationNumber: Optional[str] = None
    IdentificationExpirationDate: Optional[Timestamp] = None
    IdentificationIssuingOrg: Optional[str] = None
    DevicePickupId: Optional[str] = None


class TargetOnDeviceService(BaseValidatorModel):
    pass


class S3ResourceOutput(BaseValidatorModel):
    BucketArn: Optional[str] = None
    KeyRange: Optional[KeyRange] = None
    TargetOnDeviceServices: Optional[List[TargetOnDeviceService]] = None


class S3Resource(BaseValidatorModel):
    BucketArn: Optional[str] = None
    KeyRange: Optional[KeyRange] = None
    TargetOnDeviceServices: Optional[Sequence[TargetOnDeviceService]] = None


class ShippingDetails(BaseValidatorModel):
    ShippingOption: Optional[ShippingOptionType] = None
    InboundShipment: Optional[Shipment] = None
    OutboundShipment: Optional[Shipment] = None


class SnowconeDeviceConfiguration(BaseValidatorModel):
    WirelessConnection: Optional[WirelessConnection] = None


class JobResourceOutput(BaseValidatorModel):
    S3Resources: Optional[List[S3ResourceOutput]] = None
    LambdaResources: Optional[List[LambdaResourceOutput]] = None
    Ec2AmiResources: Optional[List[Ec2AmiResource]] = None


class JobResource(BaseValidatorModel):
    S3Resources: Optional[Sequence[S3Resource]] = None
    LambdaResources: Optional[Sequence[LambdaResource]] = None
    Ec2AmiResources: Optional[Sequence[Ec2AmiResource]] = None


class DeviceConfiguration(BaseValidatorModel):
    SnowconeDeviceConfiguration: Optional[SnowconeDeviceConfiguration] = None


class ClusterMetadata(BaseValidatorModel):
    ClusterId: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    ClusterState: Optional[ClusterStateType] = None
    JobType: Optional[JobTypeType] = None
    SnowballType: Optional[SnowballTypeType] = None
    CreationDate: Optional[datetime] = None
    Resources: Optional[JobResourceOutput] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationOutput] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocuments] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None


class JobMetadata(BaseValidatorModel):
    JobId: Optional[str] = None
    JobState: Optional[JobStateType] = None
    JobType: Optional[JobTypeType] = None
    SnowballType: Optional[SnowballTypeType] = None
    CreationDate: Optional[datetime] = None
    Resources: Optional[JobResourceOutput] = None
    Description: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    AddressId: Optional[str] = None
    ShippingDetails: Optional[ShippingDetails] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    Notification: Optional[NotificationOutput] = None
    DataTransferProgress: Optional[DataTransfer] = None
    JobLogInfo: Optional[JobLogs] = None
    ClusterId: Optional[str] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocuments] = None
    DeviceConfiguration: Optional[DeviceConfiguration] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    LongTermPricingId: Optional[str] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    ImpactLevel: Optional[ImpactLevelType] = None
    PickupDetails: Optional[PickupDetailsOutput] = None
    SnowballId: Optional[str] = None


class DescribeClusterResult(BaseValidatorModel):
    ClusterMetadata: ClusterMetadata
    ResponseMetadata: ResponseMetadata


class JobResourceUnion(BaseValidatorModel):
    pass


class NotificationUnion(BaseValidatorModel):
    pass


class CreateClusterRequest(BaseValidatorModel):
    JobType: JobTypeType
    AddressId: str
    SnowballType: SnowballTypeType
    ShippingOption: ShippingOptionType
    Resources: Optional[JobResourceUnion] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    Description: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    Notification: Optional[NotificationUnion] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocuments] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    InitialClusterSize: Optional[int] = None
    ForceCreateJobs: Optional[bool] = None
    LongTermPricingIds: Optional[Sequence[str]] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None


class PickupDetailsUnion(BaseValidatorModel):
    pass


class CreateJobRequest(BaseValidatorModel):
    JobType: Optional[JobTypeType] = None
    Resources: Optional[JobResourceUnion] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    Description: Optional[str] = None
    AddressId: Optional[str] = None
    KmsKeyARN: Optional[str] = None
    RoleARN: Optional[str] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationUnion] = None
    ClusterId: Optional[str] = None
    SnowballType: Optional[SnowballTypeType] = None
    ForwardingAddressId: Optional[str] = None
    TaxDocuments: Optional[TaxDocuments] = None
    DeviceConfiguration: Optional[DeviceConfiguration] = None
    RemoteManagement: Optional[RemoteManagementType] = None
    LongTermPricingId: Optional[str] = None
    ImpactLevel: Optional[ImpactLevelType] = None
    PickupDetails: Optional[PickupDetailsUnion] = None


class UpdateClusterRequest(BaseValidatorModel):
    ClusterId: str
    RoleARN: Optional[str] = None
    Description: Optional[str] = None
    Resources: Optional[JobResourceUnion] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Notification: Optional[NotificationUnion] = None
    ForwardingAddressId: Optional[str] = None


class UpdateJobRequest(BaseValidatorModel):
    JobId: str
    RoleARN: Optional[str] = None
    Notification: Optional[NotificationUnion] = None
    Resources: Optional[JobResourceUnion] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    AddressId: Optional[str] = None
    ShippingOption: Optional[ShippingOptionType] = None
    Description: Optional[str] = None
    SnowballCapacityPreference: Optional[SnowballCapacityType] = None
    ForwardingAddressId: Optional[str] = None
    PickupDetails: Optional[PickupDetailsUnion] = None


class DescribeJobResult(BaseValidatorModel):
    JobMetadata: JobMetadata
    SubJobMetadata: List[JobMetadata]
    ResponseMetadata: ResponseMetadata


