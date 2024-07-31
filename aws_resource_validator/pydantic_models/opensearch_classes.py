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
from aws_resource_validator.pydantic_models.opensearch_constants import *

class NaturalLanguageQueryGenerationOptionsInputTypeDef(BaseModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None

class NaturalLanguageQueryGenerationOptionsOutputTypeDef(BaseModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None
    CurrentState: Optional[NaturalLanguageQueryGenerationCurrentStateType] = None

class OptionStatusTypeDef(BaseModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None

class AWSDomainInformationTypeDef(BaseModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None

class AcceptInboundConnectionRequestRequestTypeDef(BaseModel):
    ConnectionId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AdditionalLimitTypeDef(BaseModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class JWTOptionsInputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None

class MasterUserOptionsTypeDef(BaseModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None

class JWTOptionsOutputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None

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
    UseOffPeakWindow: Optional[bool] = None

class AutoTuneStatusTypeDef(BaseModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None

class AvailabilityZoneInfoTypeDef(BaseModel):
    AvailabilityZoneName: Optional[str] = None
    ZoneStatus: Optional[ZoneStatusType] = None
    ConfiguredDataNodeCount: Optional[str] = None
    AvailableDataNodeCount: Optional[str] = None
    TotalShards: Optional[str] = None
    TotalUnAssignedShards: Optional[str] = None

class CancelDomainConfigChangeRequestRequestTypeDef(BaseModel):
    DomainName: str
    DryRun: Optional[bool] = None

class CancelledChangePropertyTypeDef(BaseModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None

class CancelServiceSoftwareUpdateRequestRequestTypeDef(BaseModel):
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
    InitiatedBy: Optional[InitiatedByType] = None
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class ChangeProgressStageTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None

class ColdStorageOptionsTypeDef(BaseModel):
    Enabled: bool

class ZoneAwarenessConfigTypeDef(BaseModel):
    AvailabilityZoneCount: Optional[int] = None

class CognitoOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None

class CompatibleVersionsMapTypeDef(BaseModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None

class CrossClusterSearchConnectionPropertiesTypeDef(BaseModel):
    SkipUnavailable: Optional[SkipUnavailableStatusType] = None

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

class SoftwareUpdateOptionsTypeDef(BaseModel):
    AutoSoftwareUpdateEnabled: Optional[bool] = None

class VPCOptionsTypeDef(BaseModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class OutboundConnectionStatusTypeDef(BaseModel):
    StatusCode: Optional[OutboundConnectionStatusCodeType] = None
    Message: Optional[str] = None

class PackageSourceTypeDef(BaseModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None

class S3GlueDataCatalogTypeDef(BaseModel):
    RoleArn: Optional[str] = None

class DeleteDataSourceRequestRequestTypeDef(BaseModel):
    DomainName: str
    Name: str

class DeleteDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DeleteInboundConnectionRequestRequestTypeDef(BaseModel):
    ConnectionId: str

class DeleteOutboundConnectionRequestRequestTypeDef(BaseModel):
    ConnectionId: str

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

class DescribeDomainConfigRequestRequestTypeDef(BaseModel):
    DomainName: str

class DescribeDomainHealthRequestRequestTypeDef(BaseModel):
    DomainName: str

class DescribeDomainNodesRequestRequestTypeDef(BaseModel):
    DomainName: str

class DomainNodesStatusTypeDef(BaseModel):
    NodeId: Optional[str] = None
    NodeType: Optional[NodeTypeType] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    NodeStatus: Optional[NodeStatusType] = None
    StorageType: Optional[str] = None
    StorageVolumeType: Optional[VolumeTypeType] = None
    StorageSize: Optional[str] = None

class DescribeDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DescribeDomainsRequestRequestTypeDef(BaseModel):
    DomainNames: Sequence[str]

class DescribeDryRunProgressRequestRequestTypeDef(BaseModel):
    DomainName: str
    DryRunId: Optional[str] = None
    LoadDryRunConfig: Optional[bool] = None

class DryRunResultsTypeDef(BaseModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DescribeInstanceTypeLimitsRequestRequestTypeDef(BaseModel):
    InstanceType: OpenSearchPartitionInstanceTypeType
    EngineVersion: str
    DomainName: Optional[str] = None

class DescribePackagesFilterTypeDef(BaseModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[Sequence[str]] = None

class DescribeReservedInstanceOfferingsRequestRequestTypeDef(BaseModel):
    ReservedInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedInstancesRequestRequestTypeDef(BaseModel):
    ReservedInstanceId: Optional[str] = None
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

class ModifyingPropertiesTypeDef(BaseModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None

class DomainInfoTypeDef(BaseModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None

class DomainMaintenanceDetailsTypeDef(BaseModel):
    MaintenanceId: Optional[str] = None
    DomainName: Optional[str] = None
    Action: Optional[MaintenanceTypeType] = None
    NodeId: Optional[str] = None
    Status: Optional[MaintenanceStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ErrorDetailsTypeDef(BaseModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None

class VPCDerivedInfoTypeDef(BaseModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class ValidationFailureTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class GetCompatibleVersionsRequestRequestTypeDef(BaseModel):
    DomainName: Optional[str] = None

class GetDataSourceRequestRequestTypeDef(BaseModel):
    DomainName: str
    Name: str

class GetDomainMaintenanceStatusRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaintenanceId: str

class GetPackageVersionHistoryRequestRequestTypeDef(BaseModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetUpgradeHistoryRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetUpgradeStatusRequestRequestTypeDef(BaseModel):
    DomainName: str

class InboundConnectionStatusTypeDef(BaseModel):
    StatusCode: Optional[InboundConnectionStatusCodeType] = None
    Message: Optional[str] = None

class InstanceCountLimitsTypeDef(BaseModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None

class InstanceTypeDetailsTypeDef(BaseModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    EncryptionEnabled: Optional[bool] = None
    CognitoEnabled: Optional[bool] = None
    AppLogsEnabled: Optional[bool] = None
    AdvancedSecurityEnabled: Optional[bool] = None
    WarmEnabled: Optional[bool] = None
    InstanceRole: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None

class ListDataSourcesRequestRequestTypeDef(BaseModel):
    DomainName: str

class ListDomainMaintenancesRequestRequestTypeDef(BaseModel):
    DomainName: str
    Action: Optional[MaintenanceTypeType] = None
    Status: Optional[MaintenanceStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDomainNamesRequestRequestTypeDef(BaseModel):
    EngineType: Optional[EngineTypeType] = None

class ListDomainsForPackageRequestRequestTypeDef(BaseModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInstanceTypeDetailsRequestRequestTypeDef(BaseModel):
    EngineVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RetrieveAZs: Optional[bool] = None
    InstanceType: Optional[str] = None

class ListPackagesForDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListScheduledActionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ScheduledActionTypeDef(BaseModel):
    Id: str
    Type: ActionTypeType
    Severity: ActionSeverityType
    ScheduledTime: int
    Description: Optional[str] = None
    ScheduledBy: Optional[ScheduledByType] = None
    Status: Optional[ActionStatusType] = None
    Mandatory: Optional[bool] = None
    Cancellable: Optional[bool] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    ARN: str

class ListVersionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVpcEndpointAccessRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsForDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class WindowStartTimeTypeDef(BaseModel):
    Hours: int
    Minutes: int

class PluginPropertiesTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    ClassName: Optional[str] = None
    UncompressedSizeInBytes: Optional[int] = None

class PurchaseReservedInstanceOfferingRequestRequestTypeDef(BaseModel):
    ReservedInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None

class RecurringChargeTypeDef(BaseModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class RejectInboundConnectionRequestRequestTypeDef(BaseModel):
    ConnectionId: str

class RemoveTagsRequestRequestTypeDef(BaseModel):
    ARN: str
    TagKeys: Sequence[str]

class RevokeVpcEndpointAccessRequestRequestTypeDef(BaseModel):
    DomainName: str
    Account: str

class SAMLIdpTypeDef(BaseModel):
    MetadataContent: str
    EntityId: str

class StartDomainMaintenanceRequestRequestTypeDef(BaseModel):
    DomainName: str
    Action: MaintenanceTypeType
    NodeId: Optional[str] = None

class StartServiceSoftwareUpdateRequestRequestTypeDef(BaseModel):
    DomainName: str
    ScheduleAt: Optional[ScheduleAtType] = None
    DesiredStartTime: Optional[int] = None

class StorageTypeLimitTypeDef(BaseModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class UpdateScheduledActionRequestRequestTypeDef(BaseModel):
    DomainName: str
    ActionID: str
    ActionType: ActionTypeType
    ScheduleAt: ScheduleAtType
    DesiredStartTime: Optional[int] = None

class UpgradeDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None

class UpgradeStepItemTypeDef(BaseModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None

class AIMLOptionsInputTypeDef(BaseModel):
    NaturalLanguageQueryGenerationOptions: Optional[       NaturalLanguageQueryGenerationOptionsInputTypeDef     ] = None

class AIMLOptionsOutputTypeDef(BaseModel):
    NaturalLanguageQueryGenerationOptions: Optional[       NaturalLanguageQueryGenerationOptionsOutputTypeDef     ] = None

class AccessPoliciesStatusTypeDef(BaseModel):
    Options: str
    Status: OptionStatusTypeDef

class AdvancedOptionsStatusTypeDef(BaseModel):
    Options: Dict[str, str]
    Status: OptionStatusTypeDef

class IPAddressTypeStatusTypeDef(BaseModel):
    Options: IPAddressTypeType
    Status: OptionStatusTypeDef

class VersionStatusTypeDef(BaseModel):
    Options: str
    Status: OptionStatusTypeDef

class DomainInformationContainerTypeDef(BaseModel):
    AWSDomainInformation: Optional[AWSDomainInformationTypeDef] = None

class AddDataSourceResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainMaintenanceStatusResponseTypeDef(BaseModel):
    Status: MaintenanceStatusType
    StatusMessage: str
    NodeId: str
    Action: MaintenanceTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetUpgradeStatusResponseTypeDef(BaseModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsResponseTypeDef(BaseModel):
    Versions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseReservedInstanceOfferingResponseTypeDef(BaseModel):
    ReservedInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDomainMaintenanceResponseTypeDef(BaseModel):
    MaintenanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class EnvironmentInfoTypeDef(BaseModel):
    AvailabilityZoneInformation: Optional[List[AvailabilityZoneInfoTypeDef]] = None

class CancelDomainConfigChangeResponseTypeDef(BaseModel):
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangePropertyTypeDef]
    DryRun: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServiceSoftwareUpdateResponseTypeDef(BaseModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartServiceSoftwareUpdateResponseTypeDef(BaseModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradeDomainResponseTypeDef(BaseModel):
    UpgradeId: str
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    AdvancedOptions: Dict[str, str]
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
    LastUpdatedTime: Optional[datetime] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    InitiatedBy: Optional[InitiatedByType] = None

class ClusterConfigTypeDef(BaseModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfigTypeDef] = None
    DedicatedMasterType: Optional[OpenSearchPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[OpenSearchWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptionsTypeDef] = None
    MultiAZWithStandbyEnabled: Optional[bool] = None

class CognitoOptionsStatusTypeDef(BaseModel):
    Options: CognitoOptionsTypeDef
    Status: OptionStatusTypeDef

class GetCompatibleVersionsResponseTypeDef(BaseModel):
    CompatibleVersions: List[CompatibleVersionsMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionPropertiesTypeDef(BaseModel):
    Endpoint: Optional[str] = None
    CrossClusterSearch: Optional[CrossClusterSearchConnectionPropertiesTypeDef] = None

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

class SoftwareUpdateOptionsStatusTypeDef(BaseModel):
    Options: Optional[SoftwareUpdateOptionsTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None

class CreateVpcEndpointRequestRequestTypeDef(BaseModel):
    DomainArn: str
    VpcOptions: VPCOptionsTypeDef
    ClientToken: Optional[str] = None

class UpdateVpcEndpointRequestRequestTypeDef(BaseModel):
    VpcEndpointId: str
    VpcOptions: VPCOptionsTypeDef

class CreatePackageRequestRequestTypeDef(BaseModel):
    PackageName: str
    PackageType: PackageTypeType
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None

class UpdatePackageRequestRequestTypeDef(BaseModel):
    PackageID: str
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None

class DataSourceTypeTypeDef(BaseModel):
    S3GlueDataCatalog: Optional[S3GlueDataCatalogTypeDef] = None

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

class DescribeDomainNodesResponseTypeDef(BaseModel):
    DomainNodesStatusList: List[DomainNodesStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundConnectionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeOutboundConnectionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePackagesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[DescribePackagesFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDomainNamesResponseTypeDef(BaseModel):
    DomainNames: List[DomainInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainMaintenancesResponseTypeDef(BaseModel):
    DomainMaintenances: List[DomainMaintenanceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DomainPackageDetailsTypeDef(BaseModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[PackageTypeType] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

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

class DryRunProgressStatusTypeDef(BaseModel):
    DryRunId: str
    DryRunStatus: str
    CreationDate: str
    UpdateDate: str
    ValidationFailures: Optional[List[ValidationFailureTypeDef]] = None

class InstanceLimitsTypeDef(BaseModel):
    InstanceCountLimits: Optional[InstanceCountLimitsTypeDef] = None

class ListInstanceTypeDetailsResponseTypeDef(BaseModel):
    InstanceTypeDetails: List[InstanceTypeDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListScheduledActionsResponseTypeDef(BaseModel):
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateScheduledActionResponseTypeDef(BaseModel):
    ScheduledAction: ScheduledActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OffPeakWindowTypeDef(BaseModel):
    WindowStartTime: Optional[WindowStartTimeTypeDef] = None

class PackageDetailsTypeDef(BaseModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[PackageTypeType] = None
    PackageDescription: Optional[str] = None
    PackageStatus: Optional[PackageStatusType] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    AvailablePackageVersion: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None
    EngineVersion: Optional[str] = None
    AvailablePluginProperties: Optional[PluginPropertiesTypeDef] = None

class PackageVersionHistoryTypeDef(BaseModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    PluginProperties: Optional[PluginPropertiesTypeDef] = None

class ReservedInstanceOfferingTypeDef(BaseModel):
    ReservedInstanceOfferingId: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReservedInstanceTypeDef(BaseModel):
    ReservationName: Optional[str] = None
    ReservedInstanceId: Optional[str] = None
    BillingSubscriptionId: Optional[int] = None
    ReservedInstanceOfferingId: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    InstanceCount: Optional[int] = None
    State: Optional[str] = None
    PaymentOption: Optional[ReservedInstancePaymentOptionType] = None
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

class AIMLOptionsStatusTypeDef(BaseModel):
    Options: Optional[AIMLOptionsOutputTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None

class InboundConnectionTypeDef(BaseModel):
    LocalDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    RemoteDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    ConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundConnectionStatusTypeDef] = None
    ConnectionMode: Optional[ConnectionModeType] = None

class AutoTuneTypeDef(BaseModel):
    AutoTuneType: Optional[Literal["SCHEDULED_ACTION"]] = None
    AutoTuneDetails: Optional[AutoTuneDetailsTypeDef] = None

class AutoTuneOptionsExtraOutputTypeDef(BaseModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutputTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None

class AutoTuneOptionsInputTypeDef(BaseModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None

class AutoTuneOptionsTypeDef(BaseModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None

class DescribeDomainHealthResponseTypeDef(BaseModel):
    DomainState: DomainStateType
    AvailabilityZoneCount: str
    ActiveAvailabilityZoneCount: str
    StandByAvailabilityZoneCount: str
    DataNodeCount: str
    DedicatedMaster: bool
    MasterEligibleNodeCount: str
    WarmNodeCount: str
    MasterNode: MasterNodeStatusType
    ClusterHealth: DomainHealthType
    TotalShards: str
    TotalUnAssignedShards: str
    EnvironmentInformation: List[EnvironmentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainChangeProgressResponseTypeDef(BaseModel):
    ChangeProgressStatus: ChangeProgressStatusDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterConfigStatusTypeDef(BaseModel):
    Options: ClusterConfigTypeDef
    Status: OptionStatusTypeDef

class CreateOutboundConnectionRequestRequestTypeDef(BaseModel):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionPropertiesTypeDef] = None

class CreateOutboundConnectionResponseTypeDef(BaseModel):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionStatus: OutboundConnectionStatusTypeDef
    ConnectionId: str
    ConnectionMode: ConnectionModeType
    ConnectionProperties: ConnectionPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OutboundConnectionTypeDef(BaseModel):
    LocalDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    RemoteDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    ConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundConnectionStatusTypeDef] = None
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionPropertiesTypeDef] = None

class AddDataSourceRequestRequestTypeDef(BaseModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: Optional[str] = None

class DataSourceDetailsTypeDef(BaseModel):
    DataSourceType: Optional[DataSourceTypeTypeDef] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None

class GetDataSourceResponseTypeDef(BaseModel):
    DataSourceType: DataSourceTypeTypeDef
    Name: str
    Description: str
    Status: DataSourceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceRequestRequestTypeDef(BaseModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None

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

class OffPeakWindowOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    OffPeakWindow: Optional[OffPeakWindowTypeDef] = None

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

class GetPackageVersionHistoryResponseTypeDef(BaseModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstanceOfferingsResponseTypeDef(BaseModel):
    ReservedInstanceOfferings: List[ReservedInstanceOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstancesResponseTypeDef(BaseModel):
    ReservedInstances: List[ReservedInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AdvancedSecurityOptionsInputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptionsTypeDef] = None
    SAMLOptions: Optional[SAMLOptionsInputTypeDef] = None
    JWTOptions: Optional[JWTOptionsInputTypeDef] = None
    AnonymousAuthEnabled: Optional[bool] = None

class AdvancedSecurityOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutputTypeDef] = None
    JWTOptions: Optional[JWTOptionsOutputTypeDef] = None
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

class AcceptInboundConnectionResponseTypeDef(BaseModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInboundConnectionResponseTypeDef(BaseModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundConnectionsResponseTypeDef(BaseModel):
    Connections: List[InboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectInboundConnectionResponseTypeDef(BaseModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainAutoTunesResponseTypeDef(BaseModel):
    AutoTunes: List[AutoTuneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoTuneOptionsStatusTypeDef(BaseModel):
    Options: Optional[AutoTuneOptionsExtraOutputTypeDef] = None
    Status: Optional[AutoTuneStatusTypeDef] = None

class DeleteOutboundConnectionResponseTypeDef(BaseModel):
    Connection: OutboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOutboundConnectionsResponseTypeDef(BaseModel):
    Connections: List[OutboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDataSourcesResponseTypeDef(BaseModel):
    DataSources: List[DataSourceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OffPeakWindowOptionsStatusTypeDef(BaseModel):
    Options: Optional[OffPeakWindowOptionsTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None

class CreateDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    EngineVersion: Optional[str] = None
    ClusterConfig: Optional[ClusterConfigTypeDef] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCOptionsTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOptionTypeDef]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInputTypeDef] = None
    TagList: Optional[Sequence[TagTypeDef]] = None
    AutoTuneOptions: Optional[AutoTuneOptionsInputTypeDef] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsTypeDef] = None
    AIMLOptions: Optional[AIMLOptionsInputTypeDef] = None

class UpdateDomainConfigRequestRequestTypeDef(BaseModel):
    DomainName: str
    ClusterConfig: Optional[ClusterConfigTypeDef] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCOptionsTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOptionTypeDef]] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInputTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsTypeDef] = None
    DryRun: Optional[bool] = None
    DryRunMode: Optional[DryRunModeType] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsTypeDef] = None
    AIMLOptions: Optional[AIMLOptionsInputTypeDef] = None

class AdvancedSecurityOptionsStatusTypeDef(BaseModel):
    Options: AdvancedSecurityOptionsTypeDef
    Status: OptionStatusTypeDef

class DomainStatusTypeDef(BaseModel):
    DomainId: str
    DomainName: str
    ARN: str
    ClusterConfig: ClusterConfigTypeDef
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    Endpoint: Optional[str] = None
    EndpointV2: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    DomainEndpointV2HostedZoneId: Optional[str] = None
    Processing: Optional[bool] = None
    UpgradeProcessing: Optional[bool] = None
    EngineVersion: Optional[str] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
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
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsTypeDef] = None
    DomainProcessingStatus: Optional[DomainProcessingStatusTypeType] = None
    ModifyingProperties: Optional[List[ModifyingPropertiesTypeDef]] = None
    AIMLOptions: Optional[AIMLOptionsOutputTypeDef] = None

class DescribeInstanceTypeLimitsResponseTypeDef(BaseModel):
    LimitsByRole: Dict[str, LimitsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainConfigTypeDef(BaseModel):
    EngineVersion: Optional[VersionStatusTypeDef] = None
    ClusterConfig: Optional[ClusterConfigStatusTypeDef] = None
    EBSOptions: Optional[EBSOptionsStatusTypeDef] = None
    AccessPolicies: Optional[AccessPoliciesStatusTypeDef] = None
    IPAddressType: Optional[IPAddressTypeStatusTypeDef] = None
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
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsStatusTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsStatusTypeDef] = None
    ModifyingProperties: Optional[List[ModifyingPropertiesTypeDef]] = None
    AIMLOptions: Optional[AIMLOptionsStatusTypeDef] = None

class CreateDomainResponseTypeDef(BaseModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(BaseModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResponseTypeDef(BaseModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainsResponseTypeDef(BaseModel):
    DomainStatusList: List[DomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDryRunProgressResponseTypeDef(BaseModel):
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    DryRunConfig: DomainStatusTypeDef
    DryRunResults: DryRunResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainConfigResponseTypeDef(BaseModel):
    DomainConfig: DomainConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainConfigResponseTypeDef(BaseModel):
    DomainConfig: DomainConfigTypeDef
    DryRunResults: DryRunResultsTypeDef
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

