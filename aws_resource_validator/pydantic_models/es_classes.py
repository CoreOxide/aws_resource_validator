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
from aws_resource_validator.pydantic_models.es_constants import *

class AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseValidatorModel):
    CrossClusterSearchConnectionId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class OptionStatusTypeDef(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class AdditionalLimitTypeDef(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class MasterUserOptionsTypeDef(BaseValidatorModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None

class AssociatePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    DomainName: str

class AuthorizeVpcEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Account: str

class AuthorizedPrincipalTypeDef(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None

class ScheduledAutoTuneDetailsTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    ActionType: Optional[ScheduledAutoTuneActionTypeType] = None
    Action: Optional[str] = None
    Severity: Optional[ScheduledAutoTuneSeverityTypeType] = None

class DurationTypeDef(BaseValidatorModel):
    Value: Optional[int] = None
    Unit: Optional[Literal["HOURS"]] = None

class AutoTuneOptionsOutputTypeDef(BaseValidatorModel):
    State: Optional[AutoTuneStateType] = None
    ErrorMessage: Optional[str] = None

class AutoTuneStatusTypeDef(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None

class CancelDomainConfigChangeRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DryRun: Optional[bool] = None

class CancelledChangePropertyTypeDef(BaseValidatorModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None

class CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class ServiceSoftwareOptionsTypeDef(BaseValidatorModel):
    CurrentVersion: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    Cancellable: Optional[bool] = None
    UpdateStatus: Optional[DeploymentStatusType] = None
    Description: Optional[str] = None
    AutomatedUpdateDate: Optional[datetime] = None
    OptionalDeployment: Optional[bool] = None

class ChangeProgressDetailsTypeDef(BaseValidatorModel):
    ChangeId: Optional[str] = None
    Message: Optional[str] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    InitiatedBy: Optional[InitiatedByType] = None

class ChangeProgressStageTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None

class CognitoOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None

class ColdStorageOptionsTypeDef(BaseValidatorModel):
    Enabled: bool

class CompatibleVersionsMapTypeDef(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None

class DomainEndpointOptionsTypeDef(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None
    CustomEndpointEnabled: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    CustomEndpointCertificateArn: Optional[str] = None

class EBSOptionsTypeDef(BaseValidatorModel):
    EBSEnabled: Optional[bool] = None
    VolumeType: Optional[VolumeTypeType] = None
    VolumeSize: Optional[int] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None

class EncryptionAtRestOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None

class LogPublishingOptionTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None

class NodeToNodeEncryptionOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class SnapshotOptionsTypeDef(BaseValidatorModel):
    AutomatedSnapshotStartHour: Optional[int] = None

class VPCOptionsTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class DomainInformationTypeDef(BaseValidatorModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None

class OutboundCrossClusterSearchConnectionStatusTypeDef(BaseValidatorModel):
    StatusCode: Optional[OutboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None

class PackageSourceTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None

class DeleteElasticsearchDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseValidatorModel):
    CrossClusterSearchConnectionId: str

class DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseValidatorModel):
    CrossClusterSearchConnectionId: str

class DeletePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str

class DeleteVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    VpcEndpointId: str

class VpcEndpointSummaryTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    Status: Optional[VpcEndpointStatusType] = None

class DescribeDomainAutoTunesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDomainChangeProgressRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ChangeId: Optional[str] = None

class DescribeElasticsearchDomainConfigRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DescribeElasticsearchDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DescribeElasticsearchDomainsRequestRequestTypeDef(BaseValidatorModel):
    DomainNames: Sequence[str]

class DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef(BaseValidatorModel):
    InstanceType: ESPartitionInstanceTypeType
    ElasticsearchVersion: str
    DomainName: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DescribePackagesFilterTypeDef(BaseValidatorModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedElasticsearchInstancesRequestRequestTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointsRequestRequestTypeDef(BaseValidatorModel):
    VpcEndpointIds: Sequence[str]

class VpcEndpointErrorTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    ErrorCode: Optional[VpcEndpointErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class DissociatePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    DomainName: str

class DomainInfoTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None

class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None

class DryRunResultsTypeDef(BaseValidatorModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None

class ZoneAwarenessConfigTypeDef(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None

class ModifyingPropertiesTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None

class VPCDerivedInfoTypeDef(BaseValidatorModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class GetCompatibleElasticsearchVersionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None

class GetPackageVersionHistoryRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageVersionHistoryTypeDef(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None

class GetUpgradeHistoryRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetUpgradeStatusRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class InboundCrossClusterSearchConnectionStatusTypeDef(BaseValidatorModel):
    StatusCode: Optional[InboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None

class InstanceCountLimitsTypeDef(BaseValidatorModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None

class ListDomainNamesRequestRequestTypeDef(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None

class ListDomainsForPackageRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListElasticsearchInstanceTypesRequestRequestTypeDef(BaseValidatorModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListElasticsearchVersionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPackagesForDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    ARN: str

class ListVpcEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsForDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None

class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseValidatorModel):
    CrossClusterSearchConnectionId: str

class RemoveTagsRequestRequestTypeDef(BaseValidatorModel):
    ARN: str
    TagKeys: Sequence[str]

class RevokeVpcEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Account: str

class SAMLIdpTypeDef(BaseValidatorModel):
    MetadataContent: str
    EntityId: str

class StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class StorageTypeLimitTypeDef(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class UpgradeElasticsearchDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None

class UpgradeStepItemTypeDef(BaseValidatorModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetUpgradeStatusResponseTypeDef(BaseValidatorModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListElasticsearchInstanceTypesResponseTypeDef(BaseValidatorModel):
    ElasticsearchInstanceTypes: List[ESPartitionInstanceTypeType]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListElasticsearchVersionsResponseTypeDef(BaseValidatorModel):
    ElasticsearchVersions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPoliciesStatusTypeDef(BaseValidatorModel):
    Options: str
    Status: OptionStatusTypeDef

class AdvancedOptionsStatusTypeDef(BaseValidatorModel):
    Options: Dict[str, str]
    Status: OptionStatusTypeDef

class ElasticsearchVersionStatusTypeDef(BaseValidatorModel):
    Options: str
    Status: OptionStatusTypeDef

class AddTagsRequestRequestTypeDef(BaseValidatorModel):
    ARN: str
    TagList: Sequence[TagTypeDef]

class ListTagsResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeVpcEndpointAccessResponseTypeDef(BaseValidatorModel):
    AuthorizedPrincipal: AuthorizedPrincipalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointAccessResponseTypeDef(BaseValidatorModel):
    AuthorizedPrincipalList: List[AuthorizedPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AutoTuneDetailsTypeDef(BaseValidatorModel):
    ScheduledAutoTuneDetails: Optional[ScheduledAutoTuneDetailsTypeDef] = None

class AutoTuneMaintenanceScheduleOutputTypeDef(BaseValidatorModel):
    StartAt: Optional[datetime] = None
    Duration: Optional[DurationTypeDef] = None
    CronExpressionForRecurrence: Optional[str] = None

class AutoTuneMaintenanceScheduleTypeDef(BaseValidatorModel):
    StartAt: Optional[TimestampTypeDef] = None
    Duration: Optional[DurationTypeDef] = None
    CronExpressionForRecurrence: Optional[str] = None

class CancelDomainConfigChangeResponseTypeDef(BaseValidatorModel):
    DryRun: bool
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangePropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelElasticsearchServiceSoftwareUpdateResponseTypeDef(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartElasticsearchServiceSoftwareUpdateResponseTypeDef(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradeElasticsearchDomainResponseTypeDef(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    ChangeProgressDetails: ChangeProgressDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeProgressStatusDetailsTypeDef(BaseValidatorModel):
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

class CognitoOptionsStatusTypeDef(BaseValidatorModel):
    Options: CognitoOptionsTypeDef
    Status: OptionStatusTypeDef

class GetCompatibleElasticsearchVersionsResponseTypeDef(BaseValidatorModel):
    CompatibleElasticsearchVersions: List[CompatibleVersionsMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainEndpointOptionsStatusTypeDef(BaseValidatorModel):
    Options: DomainEndpointOptionsTypeDef
    Status: OptionStatusTypeDef

class EBSOptionsStatusTypeDef(BaseValidatorModel):
    Options: EBSOptionsTypeDef
    Status: OptionStatusTypeDef

class EncryptionAtRestOptionsStatusTypeDef(BaseValidatorModel):
    Options: EncryptionAtRestOptionsTypeDef
    Status: OptionStatusTypeDef

class LogPublishingOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[Dict[LogTypeType, LogPublishingOptionTypeDef]] = None
    Status: Optional[OptionStatusTypeDef] = None

class NodeToNodeEncryptionOptionsStatusTypeDef(BaseValidatorModel):
    Options: NodeToNodeEncryptionOptionsTypeDef
    Status: OptionStatusTypeDef

class SnapshotOptionsStatusTypeDef(BaseValidatorModel):
    Options: SnapshotOptionsTypeDef
    Status: OptionStatusTypeDef

class CreateVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    DomainArn: str
    VpcOptions: VPCOptionsTypeDef
    ClientToken: Optional[str] = None

class UpdateVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    VpcEndpointId: str
    VpcOptions: VPCOptionsTypeDef

class CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef(BaseValidatorModel):
    SourceDomainInfo: DomainInformationTypeDef
    DestinationDomainInfo: DomainInformationTypeDef
    ConnectionAlias: str

class CreateOutboundCrossClusterSearchConnectionResponseTypeDef(BaseValidatorModel):
    SourceDomainInfo: DomainInformationTypeDef
    DestinationDomainInfo: DomainInformationTypeDef
    ConnectionAlias: str
    ConnectionStatus: OutboundCrossClusterSearchConnectionStatusTypeDef
    CrossClusterSearchConnectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class OutboundCrossClusterSearchConnectionTypeDef(BaseValidatorModel):
    SourceDomainInfo: Optional[DomainInformationTypeDef] = None
    DestinationDomainInfo: Optional[DomainInformationTypeDef] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundCrossClusterSearchConnectionStatusTypeDef] = None

class CreatePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageName: str
    PackageType: Literal["TXT-DICTIONARY"]
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None

class UpdatePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None

class DeleteVpcEndpointResponseTypeDef(BaseValidatorModel):
    VpcEndpointSummary: VpcEndpointSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointsForDomainResponseTypeDef(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointsResponseTypeDef(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePackagesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[DescribePackagesFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedElasticsearchInstanceOfferingsRequestDescribeReservedElasticsearchInstanceOfferingsPaginateTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedElasticsearchInstancesRequestDescribeReservedElasticsearchInstancesPaginateTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUpgradeHistoryRequestGetUpgradeHistoryPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListElasticsearchInstanceTypesRequestListElasticsearchInstanceTypesPaginateTypeDef(BaseValidatorModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListElasticsearchVersionsRequestListElasticsearchVersionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainNamesResponseTypeDef(BaseValidatorModel):
    DomainNames: List[DomainInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainPackageDetailsTypeDef(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal["TXT-DICTIONARY"]] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

class PackageDetailsTypeDef(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal["TXT-DICTIONARY"]] = None
    PackageDescription: Optional[str] = None
    PackageStatus: Optional[PackageStatusType] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    AvailablePackageVersion: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

class ElasticsearchClusterConfigTypeDef(BaseValidatorModel):
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

class VPCDerivedInfoStatusTypeDef(BaseValidatorModel):
    Options: VPCDerivedInfoTypeDef
    Status: OptionStatusTypeDef

class VpcEndpointTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    VpcOptions: Optional[VPCDerivedInfoTypeDef] = None
    Status: Optional[VpcEndpointStatusType] = None
    Endpoint: Optional[str] = None

class GetPackageVersionHistoryResponseTypeDef(BaseValidatorModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InboundCrossClusterSearchConnectionTypeDef(BaseValidatorModel):
    SourceDomainInfo: Optional[DomainInformationTypeDef] = None
    DestinationDomainInfo: Optional[DomainInformationTypeDef] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundCrossClusterSearchConnectionStatusTypeDef] = None

class InstanceLimitsTypeDef(BaseValidatorModel):
    InstanceCountLimits: Optional[InstanceCountLimitsTypeDef] = None

class ReservedElasticsearchInstanceOfferingTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    ElasticsearchInstanceType: Optional[ESPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedElasticsearchInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReservedElasticsearchInstanceTypeDef(BaseValidatorModel):
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

class SAMLOptionsInputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdpTypeDef] = None
    MasterUserName: Optional[str] = None
    MasterBackendRole: Optional[str] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None

class SAMLOptionsOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdpTypeDef] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None

class StorageTypeTypeDef(BaseValidatorModel):
    StorageTypeName: Optional[str] = None
    StorageSubTypeName: Optional[str] = None
    StorageTypeLimits: Optional[List[StorageTypeLimitTypeDef]] = None

class UpgradeHistoryTypeDef(BaseValidatorModel):
    UpgradeName: Optional[str] = None
    StartTimestamp: Optional[datetime] = None
    UpgradeStatus: Optional[UpgradeStatusType] = None
    StepsList: Optional[List[UpgradeStepItemTypeDef]] = None

class AutoTuneTypeDef(BaseValidatorModel):
    AutoTuneType: Optional[Literal["SCHEDULED_ACTION"]] = None
    AutoTuneDetails: Optional[AutoTuneDetailsTypeDef] = None

class AutoTuneOptionsExtraOutputTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutputTypeDef]] = None

class AutoTuneOptionsInputTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None

class AutoTuneOptionsTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None

class DescribeDomainChangeProgressResponseTypeDef(BaseValidatorModel):
    ChangeProgressStatus: ChangeProgressStatusDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOutboundCrossClusterSearchConnectionResponseTypeDef(BaseValidatorModel):
    CrossClusterSearchConnection: OutboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef(BaseValidatorModel):
    CrossClusterSearchConnections: List[OutboundCrossClusterSearchConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociatePackageResponseTypeDef(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DissociatePackageResponseTypeDef(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsForPackageResponseTypeDef(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPackagesForDomainResponseTypeDef(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreatePackageResponseTypeDef(BaseValidatorModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageResponseTypeDef(BaseValidatorModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackagesResponseTypeDef(BaseValidatorModel):
    PackageDetailsList: List[PackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdatePackageResponseTypeDef(BaseValidatorModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ElasticsearchClusterConfigStatusTypeDef(BaseValidatorModel):
    Options: ElasticsearchClusterConfigTypeDef
    Status: OptionStatusTypeDef

class CreateVpcEndpointResponseTypeDef(BaseValidatorModel):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointsResponseTypeDef(BaseValidatorModel):
    VpcEndpoints: List[VpcEndpointTypeDef]
    VpcEndpointErrors: List[VpcEndpointErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcEndpointResponseTypeDef(BaseValidatorModel):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptInboundCrossClusterSearchConnectionResponseTypeDef(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInboundCrossClusterSearchConnectionResponseTypeDef(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundCrossClusterSearchConnectionsResponseTypeDef(BaseValidatorModel):
    CrossClusterSearchConnections: List[InboundCrossClusterSearchConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectInboundCrossClusterSearchConnectionResponseTypeDef(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferings: List[       ReservedElasticsearchInstanceOfferingTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedElasticsearchInstancesResponseTypeDef(BaseValidatorModel):
    ReservedElasticsearchInstances: List[ReservedElasticsearchInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AdvancedSecurityOptionsInputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptionsTypeDef] = None
    SAMLOptions: Optional[SAMLOptionsInputTypeDef] = None
    AnonymousAuthEnabled: Optional[bool] = None

class AdvancedSecurityOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutputTypeDef] = None
    AnonymousAuthDisableDate: Optional[datetime] = None
    AnonymousAuthEnabled: Optional[bool] = None

class LimitsTypeDef(BaseValidatorModel):
    StorageTypes: Optional[List[StorageTypeTypeDef]] = None
    InstanceLimits: Optional[InstanceLimitsTypeDef] = None
    AdditionalLimits: Optional[List[AdditionalLimitTypeDef]] = None

class GetUpgradeHistoryResponseTypeDef(BaseValidatorModel):
    UpgradeHistories: List[UpgradeHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeDomainAutoTunesResponseTypeDef(BaseValidatorModel):
    AutoTunes: List[AutoTuneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoTuneOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[AutoTuneOptionsExtraOutputTypeDef] = None
    Status: Optional[AutoTuneStatusTypeDef] = None

class CreateElasticsearchDomainRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateElasticsearchDomainConfigRequestRequestTypeDef(BaseValidatorModel):
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

class AdvancedSecurityOptionsStatusTypeDef(BaseValidatorModel):
    Options: AdvancedSecurityOptionsTypeDef
    Status: OptionStatusTypeDef

class ElasticsearchDomainStatusTypeDef(BaseValidatorModel):
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

class DescribeElasticsearchInstanceTypeLimitsResponseTypeDef(BaseValidatorModel):
    LimitsByRole: Dict[str, LimitsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ElasticsearchDomainConfigTypeDef(BaseValidatorModel):
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

class CreateElasticsearchDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteElasticsearchDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticsearchDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticsearchDomainsResponseTypeDef(BaseValidatorModel):
    DomainStatusList: List[ElasticsearchDomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticsearchDomainConfigResponseTypeDef(BaseValidatorModel):
    DomainConfig: ElasticsearchDomainConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateElasticsearchDomainConfigResponseTypeDef(BaseValidatorModel):
    DomainConfig: ElasticsearchDomainConfigTypeDef
    DryRunResults: DryRunResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

