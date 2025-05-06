from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.es.es_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptInboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class OptionStatus(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class AdditionalLimit(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


class MasterUserOptions(BaseValidatorModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None


class AssociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str


class AuthorizeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: str


class AuthorizedPrincipal(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None


class ScheduledAutoTuneDetails(BaseValidatorModel):
    Date: Optional[datetime] = None
    ActionType: Optional[ScheduledAutoTuneActionTypeType] = None
    Action: Optional[str] = None
    Severity: Optional[ScheduledAutoTuneSeverityTypeType] = None


class Duration(BaseValidatorModel):
    Value: Optional[int] = None
    Unit: Optional[Literal['HOURS']] = None

Timestamp = Union[datetime, str]


class AutoTuneOptionsOutput(BaseValidatorModel):
    State: Optional[AutoTuneStateType] = None
    ErrorMessage: Optional[str] = None


class AutoTuneStatus(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None


class CancelDomainConfigChangeRequest(BaseValidatorModel):
    DomainName: str
    DryRun: Optional[bool] = None


class CancelledChangeProperty(BaseValidatorModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None


class CancelElasticsearchServiceSoftwareUpdateRequest(BaseValidatorModel):
    DomainName: str


class ServiceSoftwareOptions(BaseValidatorModel):
    CurrentVersion: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    Cancellable: Optional[bool] = None
    UpdateStatus: Optional[DeploymentStatusType] = None
    Description: Optional[str] = None
    AutomatedUpdateDate: Optional[datetime] = None
    OptionalDeployment: Optional[bool] = None


class ChangeProgressDetails(BaseValidatorModel):
    ChangeId: Optional[str] = None
    Message: Optional[str] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    InitiatedBy: Optional[InitiatedByType] = None


class ChangeProgressStage(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None


class CognitoOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None


class ColdStorageOptions(BaseValidatorModel):
    Enabled: bool


class CompatibleVersionsMap(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None


class DomainEndpointOptions(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None
    CustomEndpointEnabled: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    CustomEndpointCertificateArn: Optional[str] = None


class EBSOptions(BaseValidatorModel):
    EBSEnabled: Optional[bool] = None
    VolumeType: Optional[VolumeTypeType] = None
    VolumeSize: Optional[int] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None


class EncryptionAtRestOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class LogPublishingOption(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class NodeToNodeEncryptionOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None


class SnapshotOptions(BaseValidatorModel):
    AutomatedSnapshotStartHour: Optional[int] = None


class VPCOptions(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class DomainInformation(BaseValidatorModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None


class OutboundCrossClusterSearchConnectionStatus(BaseValidatorModel):
    StatusCode: Optional[OutboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None


class PackageSource(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None


class DeleteElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str


class DeleteInboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


class DeleteOutboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


class DeletePackageRequest(BaseValidatorModel):
    PackageID: str


class DeleteVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str


class VpcEndpointSummary(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    Status: Optional[VpcEndpointStatusType] = None


class DescribeDomainAutoTunesRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDomainChangeProgressRequest(BaseValidatorModel):
    DomainName: str
    ChangeId: Optional[str] = None


class DescribeElasticsearchDomainConfigRequest(BaseValidatorModel):
    DomainName: str


class DescribeElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str


class DescribeElasticsearchDomainsRequest(BaseValidatorModel):
    DomainNames: List[str]


class DescribeElasticsearchInstanceTypeLimitsRequest(BaseValidatorModel):
    InstanceType: ESPartitionInstanceTypeType
    ElasticsearchVersion: str
    DomainName: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


class DescribePackagesFilter(BaseValidatorModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeReservedElasticsearchInstanceOfferingsRequest(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReservedElasticsearchInstancesRequest(BaseValidatorModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointsRequest(BaseValidatorModel):
    VpcEndpointIds: List[str]


class VpcEndpointError(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    ErrorCode: Optional[VpcEndpointErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class DissociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str


class DomainInfo(BaseValidatorModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None


class ErrorDetails(BaseValidatorModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None


class DryRunResults(BaseValidatorModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None


class ZoneAwarenessConfig(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class ModifyingProperties(BaseValidatorModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None


class VPCDerivedInfo(BaseValidatorModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class GetCompatibleElasticsearchVersionsRequest(BaseValidatorModel):
    DomainName: Optional[str] = None


class GetPackageVersionHistoryRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PackageVersionHistory(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class GetUpgradeHistoryRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetUpgradeStatusRequest(BaseValidatorModel):
    DomainName: str


class InboundCrossClusterSearchConnectionStatus(BaseValidatorModel):
    StatusCode: Optional[InboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None


class InstanceCountLimits(BaseValidatorModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None


class ListDomainNamesRequest(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None


class ListDomainsForPackageRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListElasticsearchInstanceTypesRequest(BaseValidatorModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListElasticsearchVersionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPackagesForDomainRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsRequest(BaseValidatorModel):
    ARN: str


class ListVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


class ListVpcEndpointsForDomainRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


class ListVpcEndpointsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class PurchaseReservedElasticsearchInstanceOfferingRequest(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class RejectInboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


class RemoveTagsRequest(BaseValidatorModel):
    ARN: str
    TagKeys: List[str]


class RevokeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: str


class SAMLIdp(BaseValidatorModel):
    MetadataContent: str
    EntityId: str


class StartElasticsearchServiceSoftwareUpdateRequest(BaseValidatorModel):
    DomainName: str


class StorageTypeLimit(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


class UpgradeElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None


class UpgradeStepItem(BaseValidatorModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetUpgradeStatusResponse(BaseValidatorModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadata


class ListElasticsearchInstanceTypesResponse(BaseValidatorModel):
    ElasticsearchInstanceTypes: List[ESPartitionInstanceTypeType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListElasticsearchVersionsResponse(BaseValidatorModel):
    ElasticsearchVersions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PurchaseReservedElasticsearchInstanceOfferingResponse(BaseValidatorModel):
    ReservedElasticsearchInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadata


class AccessPoliciesStatus(BaseValidatorModel):
    Options: str
    Status: OptionStatus


class AdvancedOptionsStatus(BaseValidatorModel):
    Options: Dict[str, str]
    Status: OptionStatus


class ElasticsearchVersionStatus(BaseValidatorModel):
    Options: str
    Status: OptionStatus


class AddTagsRequest(BaseValidatorModel):
    ARN: str
    TagList: List[Tag]


class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class AuthorizeVpcEndpointAccessResponse(BaseValidatorModel):
    AuthorizedPrincipal: AuthorizedPrincipal
    ResponseMetadata: ResponseMetadata


class ListVpcEndpointAccessResponse(BaseValidatorModel):
    AuthorizedPrincipalList: List[AuthorizedPrincipal]
    NextToken: str
    ResponseMetadata: ResponseMetadata


class AutoTuneDetails(BaseValidatorModel):
    ScheduledAutoTuneDetails: Optional[ScheduledAutoTuneDetails] = None


class AutoTuneMaintenanceScheduleOutput(BaseValidatorModel):
    StartAt: Optional[datetime] = None
    Duration: Optional[Duration] = None
    CronExpressionForRecurrence: Optional[str] = None


class AutoTuneMaintenanceSchedule(BaseValidatorModel):
    StartAt: Optional[Timestamp] = None
    Duration: Optional[Duration] = None
    CronExpressionForRecurrence: Optional[str] = None


class CancelDomainConfigChangeResponse(BaseValidatorModel):
    DryRun: bool
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangeProperty]
    ResponseMetadata: ResponseMetadata


class CancelElasticsearchServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


class StartElasticsearchServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


class UpgradeElasticsearchDomainResponse(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    ChangeProgressDetails: ChangeProgressDetails
    ResponseMetadata: ResponseMetadata


class ChangeProgressStatusDetails(BaseValidatorModel):
    ChangeId: Optional[str] = None
    StartTime: Optional[datetime] = None
    Status: Optional[OverallChangeStatusType] = None
    PendingProperties: Optional[List[str]] = None
    CompletedProperties: Optional[List[str]] = None
    TotalNumberOfStages: Optional[int] = None
    ChangeProgressStages: Optional[List[ChangeProgressStage]] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    LastUpdatedTime: Optional[datetime] = None
    InitiatedBy: Optional[InitiatedByType] = None


class CognitoOptionsStatus(BaseValidatorModel):
    Options: CognitoOptions
    Status: OptionStatus


class GetCompatibleElasticsearchVersionsResponse(BaseValidatorModel):
    CompatibleElasticsearchVersions: List[CompatibleVersionsMap]
    ResponseMetadata: ResponseMetadata


class DomainEndpointOptionsStatus(BaseValidatorModel):
    Options: DomainEndpointOptions
    Status: OptionStatus


class EBSOptionsStatus(BaseValidatorModel):
    Options: EBSOptions
    Status: OptionStatus


class EncryptionAtRestOptionsStatus(BaseValidatorModel):
    Options: EncryptionAtRestOptions
    Status: OptionStatus


class LogPublishingOptionsStatus(BaseValidatorModel):
    Options: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    Status: Optional[OptionStatus] = None


class NodeToNodeEncryptionOptionsStatus(BaseValidatorModel):
    Options: NodeToNodeEncryptionOptions
    Status: OptionStatus


class SnapshotOptionsStatus(BaseValidatorModel):
    Options: SnapshotOptions
    Status: OptionStatus


class CreateVpcEndpointRequest(BaseValidatorModel):
    DomainArn: str
    VpcOptions: VPCOptions
    ClientToken: Optional[str] = None


class UpdateVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str
    VpcOptions: VPCOptions


class CreateOutboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    SourceDomainInfo: DomainInformation
    DestinationDomainInfo: DomainInformation
    ConnectionAlias: str


class CreateOutboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    SourceDomainInfo: DomainInformation
    DestinationDomainInfo: DomainInformation
    ConnectionAlias: str
    ConnectionStatus: OutboundCrossClusterSearchConnectionStatus
    CrossClusterSearchConnectionId: str
    ResponseMetadata: ResponseMetadata


class OutboundCrossClusterSearchConnection(BaseValidatorModel):
    SourceDomainInfo: Optional[DomainInformation] = None
    DestinationDomainInfo: Optional[DomainInformation] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundCrossClusterSearchConnectionStatus] = None


class CreatePackageRequest(BaseValidatorModel):
    PackageName: str
    PackageType: Literal['TXT-DICTIONARY']
    PackageSource: PackageSource
    PackageDescription: Optional[str] = None


class UpdatePackageRequest(BaseValidatorModel):
    PackageID: str
    PackageSource: PackageSource
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None


class DeleteVpcEndpointResponse(BaseValidatorModel):
    VpcEndpointSummary: VpcEndpointSummary
    ResponseMetadata: ResponseMetadata


class ListVpcEndpointsForDomainResponse(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummary]
    NextToken: str
    ResponseMetadata: ResponseMetadata


class ListVpcEndpointsResponse(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummary]
    NextToken: str
    ResponseMetadata: ResponseMetadata


class DescribeInboundCrossClusterSearchConnectionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeOutboundCrossClusterSearchConnectionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePackagesRequest(BaseValidatorModel):
    Filters: Optional[List[DescribePackagesFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReservedElasticsearchInstanceOfferingsRequestPaginate(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedElasticsearchInstancesRequestPaginate(BaseValidatorModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetUpgradeHistoryRequestPaginate(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListElasticsearchInstanceTypesRequestPaginate(BaseValidatorModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListElasticsearchVersionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainNamesResponse(BaseValidatorModel):
    DomainNames: List[DomainInfo]
    ResponseMetadata: ResponseMetadata


class DomainPackageDetails(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal['TXT-DICTIONARY']] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetails] = None


class PackageDetails(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal['TXT-DICTIONARY']] = None
    PackageDescription: Optional[str] = None
    PackageStatus: Optional[PackageStatusType] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    AvailablePackageVersion: Optional[str] = None
    ErrorDetails: Optional[ErrorDetails] = None


class ElasticsearchClusterConfig(BaseValidatorModel):
    InstanceType: Optional[ESPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfig] = None
    DedicatedMasterType: Optional[ESPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[ESWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptions] = None


class VPCDerivedInfoStatus(BaseValidatorModel):
    Options: VPCDerivedInfo
    Status: OptionStatus


class VpcEndpoint(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    VpcOptions: Optional[VPCDerivedInfo] = None
    Status: Optional[VpcEndpointStatusType] = None
    Endpoint: Optional[str] = None


class GetPackageVersionHistoryResponse(BaseValidatorModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InboundCrossClusterSearchConnection(BaseValidatorModel):
    SourceDomainInfo: Optional[DomainInformation] = None
    DestinationDomainInfo: Optional[DomainInformation] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundCrossClusterSearchConnectionStatus] = None


class InstanceLimits(BaseValidatorModel):
    InstanceCountLimits: Optional[InstanceCountLimits] = None


class ReservedElasticsearchInstanceOffering(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    ElasticsearchInstanceType: Optional[ESPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedElasticsearchInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class ReservedElasticsearchInstance(BaseValidatorModel):
    ReservationName: Optional[str] = None
    ReservedElasticsearchInstanceId: Optional[str] = None
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    ElasticsearchInstanceType: Optional[ESPartitionInstanceTypeType] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    ElasticsearchInstanceCount: Optional[int] = None
    State: Optional[str] = None
    PaymentOption: Optional[ReservedElasticsearchInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class SAMLOptionsInput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdp] = None
    MasterUserName: Optional[str] = None
    MasterBackendRole: Optional[str] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None


class SAMLOptionsOutput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdp] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None


class StorageType(BaseValidatorModel):
    StorageTypeName: Optional[str] = None
    StorageSubTypeName: Optional[str] = None
    StorageTypeLimits: Optional[List[StorageTypeLimit]] = None


class UpgradeHistory(BaseValidatorModel):
    UpgradeName: Optional[str] = None
    StartTimestamp: Optional[datetime] = None
    UpgradeStatus: Optional[UpgradeStatusType] = None
    StepsList: Optional[List[UpgradeStepItem]] = None


class AutoTune(BaseValidatorModel):
    AutoTuneType: Optional[Literal['SCHEDULED_ACTION']] = None
    AutoTuneDetails: Optional[AutoTuneDetails] = None


class AutoTuneOptionsExtra(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutput]] = None

AutoTuneMaintenanceScheduleUnion = Union[AutoTuneMaintenanceSchedule, AutoTuneMaintenanceScheduleOutput]


class AutoTuneOptions(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceSchedule]] = None


class DescribeDomainChangeProgressResponse(BaseValidatorModel):
    ChangeProgressStatus: ChangeProgressStatusDetails
    ResponseMetadata: ResponseMetadata


class DeleteOutboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: OutboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


class DescribeOutboundCrossClusterSearchConnectionsResponse(BaseValidatorModel):
    CrossClusterSearchConnections: List[OutboundCrossClusterSearchConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
    ResponseMetadata: ResponseMetadata


class DissociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
    ResponseMetadata: ResponseMetadata


class ListDomainsForPackageResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPackagesForDomainResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreatePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


class DeletePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


class DescribePackagesResponse(BaseValidatorModel):
    PackageDetailsList: List[PackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdatePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


class ElasticsearchClusterConfigStatus(BaseValidatorModel):
    Options: ElasticsearchClusterConfig
    Status: OptionStatus


class CreateVpcEndpointResponse(BaseValidatorModel):
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


class DescribeVpcEndpointsResponse(BaseValidatorModel):
    VpcEndpoints: List[VpcEndpoint]
    VpcEndpointErrors: List[VpcEndpointError]
    ResponseMetadata: ResponseMetadata


class UpdateVpcEndpointResponse(BaseValidatorModel):
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


class AcceptInboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


class DeleteInboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


class DescribeInboundCrossClusterSearchConnectionsResponse(BaseValidatorModel):
    CrossClusterSearchConnections: List[InboundCrossClusterSearchConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RejectInboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


class DescribeReservedElasticsearchInstanceOfferingsResponse(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferings: List[ReservedElasticsearchInstanceOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeReservedElasticsearchInstancesResponse(BaseValidatorModel):
    ReservedElasticsearchInstances: List[ReservedElasticsearchInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AdvancedSecurityOptionsInput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptions] = None
    SAMLOptions: Optional[SAMLOptionsInput] = None
    AnonymousAuthEnabled: Optional[bool] = None


class AdvancedSecurityOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutput] = None
    AnonymousAuthDisableDate: Optional[datetime] = None
    AnonymousAuthEnabled: Optional[bool] = None


class Limits(BaseValidatorModel):
    StorageTypes: Optional[List[StorageType]] = None
    InstanceLimits: Optional[InstanceLimits] = None
    AdditionalLimits: Optional[List[AdditionalLimit]] = None


class GetUpgradeHistoryResponse(BaseValidatorModel):
    UpgradeHistories: List[UpgradeHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeDomainAutoTunesResponse(BaseValidatorModel):
    AutoTunes: List[AutoTune]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AutoTuneOptionsStatus(BaseValidatorModel):
    Options: Optional[AutoTuneOptionsExtra] = None
    Status: Optional[AutoTuneStatus] = None


class AutoTuneOptionsInput(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleUnion]] = None

AutoTuneOptionsUnion = Union[AutoTuneOptions, AutoTuneOptionsExtra]


class AdvancedSecurityOptionsStatus(BaseValidatorModel):
    Options: AdvancedSecurityOptions
    Status: OptionStatus


class ElasticsearchDomainStatus(BaseValidatorModel):
    DomainId: str
    DomainName: str
    ARN: str
    ElasticsearchClusterConfig: ElasticsearchClusterConfig
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    Processing: Optional[bool] = None
    UpgradeProcessing: Optional[bool] = None
    ElasticsearchVersion: Optional[str] = None
    EBSOptions: Optional[EBSOptions] = None
    AccessPolicies: Optional[str] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCDerivedInfo] = None
    CognitoOptions: Optional[CognitoOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    ServiceSoftwareOptions: Optional[ServiceSoftwareOptions] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptions] = None
    AutoTuneOptions: Optional[AutoTuneOptionsOutput] = None
    ChangeProgressDetails: Optional[ChangeProgressDetails] = None
    DomainProcessingStatus: Optional[DomainProcessingStatusTypeType] = None
    ModifyingProperties: Optional[List[ModifyingProperties]] = None


class DescribeElasticsearchInstanceTypeLimitsResponse(BaseValidatorModel):
    LimitsByRole: Dict[str, Limits]
    ResponseMetadata: ResponseMetadata


class CreateElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfig] = None
    EBSOptions: Optional[EBSOptions] = None
    AccessPolicies: Optional[str] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCOptions] = None
    CognitoOptions: Optional[CognitoOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInput] = None
    AutoTuneOptions: Optional[AutoTuneOptionsInput] = None
    TagList: Optional[List[Tag]] = None


class UpdateElasticsearchDomainConfigRequest(BaseValidatorModel):
    DomainName: str
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfig] = None
    EBSOptions: Optional[EBSOptions] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCOptions] = None
    CognitoOptions: Optional[CognitoOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    AccessPolicies: Optional[str] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInput] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    AutoTuneOptions: Optional[AutoTuneOptionsUnion] = None
    DryRun: Optional[bool] = None


class ElasticsearchDomainConfig(BaseValidatorModel):
    ElasticsearchVersion: Optional[ElasticsearchVersionStatus] = None
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfigStatus] = None
    EBSOptions: Optional[EBSOptionsStatus] = None
    AccessPolicies: Optional[AccessPoliciesStatus] = None
    SnapshotOptions: Optional[SnapshotOptionsStatus] = None
    VPCOptions: Optional[VPCDerivedInfoStatus] = None
    CognitoOptions: Optional[CognitoOptionsStatus] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsStatus] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsStatus] = None
    AdvancedOptions: Optional[AdvancedOptionsStatus] = None
    LogPublishingOptions: Optional[LogPublishingOptionsStatus] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsStatus] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsStatus] = None
    AutoTuneOptions: Optional[AutoTuneOptionsStatus] = None
    ChangeProgressDetails: Optional[ChangeProgressDetails] = None
    ModifyingProperties: Optional[List[ModifyingProperties]] = None


class CreateElasticsearchDomainResponse(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatus
    ResponseMetadata: ResponseMetadata


class DeleteElasticsearchDomainResponse(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatus
    ResponseMetadata: ResponseMetadata


class DescribeElasticsearchDomainResponse(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatus
    ResponseMetadata: ResponseMetadata


class DescribeElasticsearchDomainsResponse(BaseValidatorModel):
    DomainStatusList: List[ElasticsearchDomainStatus]
    ResponseMetadata: ResponseMetadata


class DescribeElasticsearchDomainConfigResponse(BaseValidatorModel):
    DomainConfig: ElasticsearchDomainConfig
    ResponseMetadata: ResponseMetadata


class UpdateElasticsearchDomainConfigResponse(BaseValidatorModel):
    DomainConfig: ElasticsearchDomainConfig
    DryRunResults: DryRunResults
    ResponseMetadata: ResponseMetadata