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
from aws_resource_validator.pydantic_models.es_constants import *

class AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseModel):
    CrossClusterSearchConnectionId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class OptionStatusTypeDef(BaseModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AdditionalLimitTypeDef(BaseModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class MasterUserOptionsTypeDef(BaseModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None

class AssociatePackageRequestRequestTypeDef(BaseModel):
    PackageID: str
    DomainName: str

class AuthorizeVpcEndpointAccessRequestRequestTypeDef(BaseModel):
    DomainName: str
    Account: str

class AuthorizedPrincipalTypeDef(BaseModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None

class ScheduledAutoTuneDetailsTypeDef(BaseModel):
    Date: Optional[datetime] = None
    ActionType: Optional[ScheduledAutoTuneActionTypeType] = None
    Action: Optional[str] = None
    Severity: Optional[ScheduledAutoTuneSeverityTypeType] = None

class DurationTypeDef(BaseModel):
    Value: Optional[int] = None
    Unit: Optional[Literal["HOURS"]] = None

class AutoTuneOptionsOutputTypeDef(BaseModel):
    State: Optional[AutoTuneStateType] = None
    ErrorMessage: Optional[str] = None

class AutoTuneStatusTypeDef(BaseModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None

class CancelDomainConfigChangeRequestRequestTypeDef(BaseModel):
    DomainName: str
    DryRun: Optional[bool] = None

class CancelledChangePropertyTypeDef(BaseModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None

class CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef(BaseModel):
    DomainName: str

class ServiceSoftwareOptionsTypeDef(BaseModel):
    CurrentVersion: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    Cancellable: Optional[bool] = None
    UpdateStatus: Optional[DeploymentStatusType] = None
    Description: Optional[str] = None
    AutomatedUpdateDate: Optional[datetime] = None
    OptionalDeployment: Optional[bool] = None

class ChangeProgressDetailsTypeDef(BaseModel):
    ChangeId: Optional[str] = None
    Message: Optional[str] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    InitiatedBy: Optional[InitiatedByType] = None

class ChangeProgressStageTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None

class CognitoOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None

class ColdStorageOptionsTypeDef(BaseModel):
    Enabled: bool

class CompatibleVersionsMapTypeDef(BaseModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None

class DomainEndpointOptionsTypeDef(BaseModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None
    CustomEndpointEnabled: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    CustomEndpointCertificateArn: Optional[str] = None

class EBSOptionsTypeDef(BaseModel):
    EBSEnabled: Optional[bool] = None
    VolumeType: Optional[VolumeTypeType] = None
    VolumeSize: Optional[int] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None

class EncryptionAtRestOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None

class LogPublishingOptionTypeDef(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None

class NodeToNodeEncryptionOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class SnapshotOptionsTypeDef(BaseModel):
    AutomatedSnapshotStartHour: Optional[int] = None

class VPCOptionsTypeDef(BaseModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class DomainInformationTypeDef(BaseModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None

class OutboundCrossClusterSearchConnectionStatusTypeDef(BaseModel):
    StatusCode: Optional[OutboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None

class PackageSourceTypeDef(BaseModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None

class DeleteElasticsearchDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseModel):
    CrossClusterSearchConnectionId: str

class DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseModel):
    CrossClusterSearchConnectionId: str

class DeletePackageRequestRequestTypeDef(BaseModel):
    PackageID: str

class DeleteVpcEndpointRequestRequestTypeDef(BaseModel):
    VpcEndpointId: str

class VpcEndpointSummaryTypeDef(BaseModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    Status: Optional[VpcEndpointStatusType] = None

class DescribeDomainAutoTunesRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDomainChangeProgressRequestRequestTypeDef(BaseModel):
    DomainName: str
    ChangeId: Optional[str] = None

class DescribeElasticsearchDomainConfigRequestRequestTypeDef(BaseModel):
    DomainName: str

class DescribeElasticsearchDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DescribeElasticsearchDomainsRequestRequestTypeDef(BaseModel):
    DomainNames: Sequence[str]

class DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef(BaseModel):
    InstanceType: ESPartitionInstanceTypeType
    ElasticsearchVersion: str
    DomainName: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DescribePackagesFilterTypeDef(BaseModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef(BaseModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedElasticsearchInstancesRequestRequestTypeDef(BaseModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointsRequestRequestTypeDef(BaseModel):
    VpcEndpointIds: Sequence[str]

class VpcEndpointErrorTypeDef(BaseModel):
    VpcEndpointId: Optional[str] = None
    ErrorCode: Optional[VpcEndpointErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class DissociatePackageRequestRequestTypeDef(BaseModel):
    PackageID: str
    DomainName: str

class DomainInfoTypeDef(BaseModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None

class ErrorDetailsTypeDef(BaseModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None

class DryRunResultsTypeDef(BaseModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None

class ZoneAwarenessConfigTypeDef(BaseModel):
    AvailabilityZoneCount: Optional[int] = None

class ModifyingPropertiesTypeDef(BaseModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None

class VPCDerivedInfoTypeDef(BaseModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class GetCompatibleElasticsearchVersionsRequestRequestTypeDef(BaseModel):
    DomainName: Optional[str] = None

class GetPackageVersionHistoryRequestRequestTypeDef(BaseModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageVersionHistoryTypeDef(BaseModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None

class GetUpgradeHistoryRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetUpgradeStatusRequestRequestTypeDef(BaseModel):
    DomainName: str

class InboundCrossClusterSearchConnectionStatusTypeDef(BaseModel):
    StatusCode: Optional[InboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None

class InstanceCountLimitsTypeDef(BaseModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None

class ListDomainNamesRequestRequestTypeDef(BaseModel):
    EngineType: Optional[EngineTypeType] = None

class ListDomainsForPackageRequestRequestTypeDef(BaseModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListElasticsearchInstanceTypesRequestRequestTypeDef(BaseModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListElasticsearchVersionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPackagesForDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    ARN: str

class ListVpcEndpointAccessRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsForDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef(BaseModel):
    ReservedElasticsearchInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None

class RecurringChargeTypeDef(BaseModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseModel):
    CrossClusterSearchConnectionId: str

class RemoveTagsRequestRequestTypeDef(BaseModel):
    ARN: str
    TagKeys: Sequence[str]

class RevokeVpcEndpointAccessRequestRequestTypeDef(BaseModel):
    DomainName: str
    Account: str

class SAMLIdpTypeDef(BaseModel):
    MetadataContent: str
    EntityId: str

class StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef(BaseModel):
    DomainName: str

class StorageTypeLimitTypeDef(BaseModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class UpgradeElasticsearchDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None

class UpgradeStepItemTypeDef(BaseModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetUpgradeStatusResponseTypeDef(BaseModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListElasticsearchInstanceTypesResponseTypeDef(BaseModel):
    ElasticsearchInstanceTypes: List[ESPartitionInstanceTypeType]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListElasticsearchVersionsResponseTypeDef(BaseModel):
    ElasticsearchVersions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef(BaseModel):
    ReservedElasticsearchInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPoliciesStatusTypeDef(BaseModel):
    Options: str
    Status: OptionStatusTypeDef

class AdvancedOptionsStatusTypeDef(BaseModel):
    Options: Dict[str, str]
    Status: OptionStatusTypeDef

class ElasticsearchVersionStatusTypeDef(BaseModel):
    Options: str
    Status: OptionStatusTypeDef

class AddTagsRequestRequestTypeDef(BaseModel):
    ARN: str
    TagList: Sequence[TagTypeDef]

class ListTagsResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeVpcEndpointAccessResponseTypeDef(BaseModel):
    AuthorizedPrincipal: AuthorizedPrincipalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointAccessResponseTypeDef(BaseModel):
    AuthorizedPrincipalList: List[AuthorizedPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AutoTuneDetailsTypeDef(BaseModel):
    ScheduledAutoTuneDetails: Optional[ScheduledAutoTuneDetailsTypeDef] = None

class AutoTuneMaintenanceScheduleOutputTypeDef(BaseModel):
    StartAt: Optional[datetime] = None
    Duration: Optional[DurationTypeDef] = None
    CronExpressionForRecurrence: Optional[str] = None

class AutoTuneMaintenanceScheduleTypeDef(BaseModel):
    StartAt: Optional[TimestampTypeDef] = None
    Duration: Optional[DurationTypeDef] = None
    CronExpressionForRecurrence: Optional[str] = None

class CancelDomainConfigChangeResponseTypeDef(BaseModel):
    DryRun: bool
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangePropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelElasticsearchServiceSoftwareUpdateResponseTypeDef(BaseModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartElasticsearchServiceSoftwareUpdateResponseTypeDef(BaseModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradeElasticsearchDomainResponseTypeDef(BaseModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    ChangeProgressDetails: ChangeProgressDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeProgressStatusDetailsTypeDef(BaseModel):
    ChangeId: Optional[str] = None
    StartTime: Optional[datetime] = None
    Status: Optional[OverallChangeStatusType] = None
    PendingProperties: Optional[List[str]] = None
    CompletedProperties: Optional[List[str]] = None
    TotalNumberOfStages: Optional[int] = None
    ChangeProgressStages: Optional[List[ChangeProgressStageTypeDef]] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    LastUpdatedTime: Optional[datetime] = None
    InitiatedBy: Optional[InitiatedByType] = None

class CognitoOptionsStatusTypeDef(BaseModel):
    Options: CognitoOptionsTypeDef
    Status: OptionStatusTypeDef

class GetCompatibleElasticsearchVersionsResponseTypeDef(BaseModel):
    CompatibleElasticsearchVersions: List[CompatibleVersionsMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainEndpointOptionsStatusTypeDef(BaseModel):
    Options: DomainEndpointOptionsTypeDef
    Status: OptionStatusTypeDef

class EBSOptionsStatusTypeDef(BaseModel):
    Options: EBSOptionsTypeDef
    Status: OptionStatusTypeDef

class EncryptionAtRestOptionsStatusTypeDef(BaseModel):
    Options: EncryptionAtRestOptionsTypeDef
    Status: OptionStatusTypeDef

class LogPublishingOptionsStatusTypeDef(BaseModel):
    Options: Optional[Dict[LogTypeType, LogPublishingOptionTypeDef]] = None
    Status: Optional[OptionStatusTypeDef] = None

class NodeToNodeEncryptionOptionsStatusTypeDef(BaseModel):
    Options: NodeToNodeEncryptionOptionsTypeDef
    Status: OptionStatusTypeDef

class SnapshotOptionsStatusTypeDef(BaseModel):
    Options: SnapshotOptionsTypeDef
    Status: OptionStatusTypeDef

class CreateVpcEndpointRequestRequestTypeDef(BaseModel):
    DomainArn: str
    VpcOptions: VPCOptionsTypeDef
    ClientToken: Optional[str] = None

class UpdateVpcEndpointRequestRequestTypeDef(BaseModel):
    VpcEndpointId: str
    VpcOptions: VPCOptionsTypeDef

class CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseModel):
    SourceDomainInfo: DomainInformationTypeDef
    DestinationDomainInfo: DomainInformationTypeDef
    ConnectionAlias: str

class CreateOutboundCrossClusterSearchConnectionResponseTypeDef(BaseModel):
    SourceDomainInfo: DomainInformationTypeDef
    DestinationDomainInfo: DomainInformationTypeDef
    ConnectionAlias: str
    ConnectionStatus: OutboundCrossClusterSearchConnectionStatusTypeDef
    CrossClusterSearchConnectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class OutboundCrossClusterSearchConnectionTypeDef(BaseModel):
    SourceDomainInfo: Optional[DomainInformationTypeDef] = None
    DestinationDomainInfo: Optional[DomainInformationTypeDef] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundCrossClusterSearchConnectionStatusTypeDef] = None

class CreatePackageRequestRequestTypeDef(BaseModel):
    PackageName: str
    PackageType: Literal["TXT-DICTIONARY"]
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None

class UpdatePackageRequestRequestTypeDef(BaseModel):
    PackageID: str
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None

class DeleteVpcEndpointResponseTypeDef(BaseModel):
    VpcEndpointSummary: VpcEndpointSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointsForDomainResponseTypeDef(BaseModel):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointsResponseTypeDef(BaseModel):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePackagesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[DescribePackagesFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedElasticsearchInstanceOfferingsRequestDescribeReservedElasticsearchInstanceOfferingsPaginateTypeDef(BaseModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedElasticsearchInstancesRequestDescribeReservedElasticsearchInstancesPaginateTypeDef(BaseModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUpgradeHistoryRequestGetUpgradeHistoryPaginateTypeDef(BaseModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListElasticsearchInstanceTypesRequestListElasticsearchInstanceTypesPaginateTypeDef(BaseModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListElasticsearchVersionsRequestListElasticsearchVersionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainNamesResponseTypeDef(BaseModel):
    DomainNames: List[DomainInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainPackageDetailsTypeDef(BaseModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal["TXT-DICTIONARY"]] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

class PackageDetailsTypeDef(BaseModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal["TXT-DICTIONARY"]] = None
    PackageDescription: Optional[str] = None
    PackageStatus: Optional[PackageStatusType] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    AvailablePackageVersion: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

class ElasticsearchClusterConfigTypeDef(BaseModel):
    InstanceType: Optional[ESPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfigTypeDef] = None
    DedicatedMasterType: Optional[ESPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[ESWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptionsTypeDef] = None

class VPCDerivedInfoStatusTypeDef(BaseModel):
    Options: VPCDerivedInfoTypeDef
    Status: OptionStatusTypeDef

class VpcEndpointTypeDef(BaseModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    VpcOptions: Optional[VPCDerivedInfoTypeDef] = None
    Status: Optional[VpcEndpointStatusType] = None
    Endpoint: Optional[str] = None

class GetPackageVersionHistoryResponseTypeDef(BaseModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InboundCrossClusterSearchConnectionTypeDef(BaseModel):
    SourceDomainInfo: Optional[DomainInformationTypeDef] = None
    DestinationDomainInfo: Optional[DomainInformationTypeDef] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundCrossClusterSearchConnectionStatusTypeDef] = None

class InstanceLimitsTypeDef(BaseModel):
    InstanceCountLimits: Optional[InstanceCountLimitsTypeDef] = None

class ReservedElasticsearchInstanceOfferingTypeDef(BaseModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    ElasticsearchInstanceType: Optional[ESPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedElasticsearchInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReservedElasticsearchInstanceTypeDef(BaseModel):
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
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class SAMLOptionsInputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdpTypeDef] = None
    MasterUserName: Optional[str] = None
    MasterBackendRole: Optional[str] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None

class SAMLOptionsOutputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdpTypeDef] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None

class StorageTypeTypeDef(BaseModel):
    StorageTypeName: Optional[str] = None
    StorageSubTypeName: Optional[str] = None
    StorageTypeLimits: Optional[List[StorageTypeLimitTypeDef]] = None

class UpgradeHistoryTypeDef(BaseModel):
    UpgradeName: Optional[str] = None
    StartTimestamp: Optional[datetime] = None
    UpgradeStatus: Optional[UpgradeStatusType] = None
    StepsList: Optional[List[UpgradeStepItemTypeDef]] = None

class AutoTuneTypeDef(BaseModel):
    AutoTuneType: Optional[Literal["SCHEDULED_ACTION"]] = None
    AutoTuneDetails: Optional[AutoTuneDetailsTypeDef] = None

class AutoTuneOptionsExtraOutputTypeDef(BaseModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutputTypeDef]] = None

class AutoTuneOptionsInputTypeDef(BaseModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None

class AutoTuneOptionsTypeDef(BaseModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None

class DescribeDomainChangeProgressResponseTypeDef(BaseModel):
    ChangeProgressStatus: ChangeProgressStatusDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOutboundCrossClusterSearchConnectionResponseTypeDef(BaseModel):
    CrossClusterSearchConnection: OutboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef(BaseModel):
    CrossClusterSearchConnections: List[OutboundCrossClusterSearchConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociatePackageResponseTypeDef(BaseModel):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DissociatePackageResponseTypeDef(BaseModel):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsForPackageResponseTypeDef(BaseModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPackagesForDomainResponseTypeDef(BaseModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreatePackageResponseTypeDef(BaseModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageResponseTypeDef(BaseModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackagesResponseTypeDef(BaseModel):
    PackageDetailsList: List[PackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdatePackageResponseTypeDef(BaseModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ElasticsearchClusterConfigStatusTypeDef(BaseModel):
    Options: ElasticsearchClusterConfigTypeDef
    Status: OptionStatusTypeDef

class CreateVpcEndpointResponseTypeDef(BaseModel):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointsResponseTypeDef(BaseModel):
    VpcEndpoints: List[VpcEndpointTypeDef]
    VpcEndpointErrors: List[VpcEndpointErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcEndpointResponseTypeDef(BaseModel):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptInboundCrossClusterSearchConnectionResponseTypeDef(BaseModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInboundCrossClusterSearchConnectionResponseTypeDef(BaseModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundCrossClusterSearchConnectionsResponseTypeDef(BaseModel):
    CrossClusterSearchConnections: List[InboundCrossClusterSearchConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectInboundCrossClusterSearchConnectionResponseTypeDef(BaseModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef(BaseModel):
    ReservedElasticsearchInstanceOfferings: List[       ReservedElasticsearchInstanceOfferingTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedElasticsearchInstancesResponseTypeDef(BaseModel):
    ReservedElasticsearchInstances: List[ReservedElasticsearchInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AdvancedSecurityOptionsInputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptionsTypeDef] = None
    SAMLOptions: Optional[SAMLOptionsInputTypeDef] = None
    AnonymousAuthEnabled: Optional[bool] = None

class AdvancedSecurityOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutputTypeDef] = None
    AnonymousAuthDisableDate: Optional[datetime] = None
    AnonymousAuthEnabled: Optional[bool] = None

class LimitsTypeDef(BaseModel):
    StorageTypes: Optional[List[StorageTypeTypeDef]] = None
    InstanceLimits: Optional[InstanceLimitsTypeDef] = None
    AdditionalLimits: Optional[List[AdditionalLimitTypeDef]] = None

class GetUpgradeHistoryResponseTypeDef(BaseModel):
    UpgradeHistories: List[UpgradeHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeDomainAutoTunesResponseTypeDef(BaseModel):
    AutoTunes: List[AutoTuneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoTuneOptionsStatusTypeDef(BaseModel):
    Options: Optional[AutoTuneOptionsExtraOutputTypeDef] = None
    Status: Optional[AutoTuneStatusTypeDef] = None

class CreateElasticsearchDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfigTypeDef] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    AccessPolicies: Optional[str] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCOptionsTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOptionTypeDef]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInputTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsInputTypeDef] = None
    TagList: Optional[Sequence[TagTypeDef]] = None

class UpdateElasticsearchDomainConfigRequestRequestTypeDef(BaseModel):
    DomainName: str
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfigTypeDef] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCOptionsTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None
    AccessPolicies: Optional[str] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOptionTypeDef]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInputTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsTypeDef] = None
    DryRun: Optional[bool] = None

class AdvancedSecurityOptionsStatusTypeDef(BaseModel):
    Options: AdvancedSecurityOptionsTypeDef
    Status: OptionStatusTypeDef

class ElasticsearchDomainStatusTypeDef(BaseModel):
    DomainId: str
    DomainName: str
    ARN: str
    ElasticsearchClusterConfig: ElasticsearchClusterConfigTypeDef
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    Processing: Optional[bool] = None
    UpgradeProcessing: Optional[bool] = None
    ElasticsearchVersion: Optional[str] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    AccessPolicies: Optional[str] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCDerivedInfoTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOptionTypeDef]] = None
    ServiceSoftwareOptions: Optional[ServiceSoftwareOptionsTypeDef] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsOutputTypeDef] = None
    ChangeProgressDetails: Optional[ChangeProgressDetailsTypeDef] = None
    DomainProcessingStatus: Optional[DomainProcessingStatusTypeType] = None
    ModifyingProperties: Optional[List[ModifyingPropertiesTypeDef]] = None

class DescribeElasticsearchInstanceTypeLimitsResponseTypeDef(BaseModel):
    LimitsByRole: Dict[str, LimitsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ElasticsearchDomainConfigTypeDef(BaseModel):
    ElasticsearchVersion: Optional[ElasticsearchVersionStatusTypeDef] = None
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfigStatusTypeDef] = None
    EBSOptions: Optional[EBSOptionsStatusTypeDef] = None
    AccessPolicies: Optional[AccessPoliciesStatusTypeDef] = None
    SnapshotOptions: Optional[SnapshotOptionsStatusTypeDef] = None
    VPCOptions: Optional[VPCDerivedInfoStatusTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsStatusTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsStatusTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsStatusTypeDef] = None
    AdvancedOptions: Optional[AdvancedOptionsStatusTypeDef] = None
    LogPublishingOptions: Optional[LogPublishingOptionsStatusTypeDef] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsStatusTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsStatusTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsStatusTypeDef] = None
    ChangeProgressDetails: Optional[ChangeProgressDetailsTypeDef] = None
    ModifyingProperties: Optional[List[ModifyingPropertiesTypeDef]] = None

class CreateElasticsearchDomainResponseTypeDef(BaseModel):
    DomainStatus: ElasticsearchDomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteElasticsearchDomainResponseTypeDef(BaseModel):
    DomainStatus: ElasticsearchDomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticsearchDomainResponseTypeDef(BaseModel):
    DomainStatus: ElasticsearchDomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticsearchDomainsResponseTypeDef(BaseModel):
    DomainStatusList: List[ElasticsearchDomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticsearchDomainConfigResponseTypeDef(BaseModel):
    DomainConfig: ElasticsearchDomainConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateElasticsearchDomainConfigResponseTypeDef(BaseModel):
    DomainConfig: ElasticsearchDomainConfigTypeDef
    DryRunResults: DryRunResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

