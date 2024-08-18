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
from aws_resource_validator.pydantic_models.opensearch_constants import *

class NaturalLanguageQueryGenerationOptionsInputTypeDef(BaseValidatorModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None

class NaturalLanguageQueryGenerationOptionsOutputTypeDef(BaseValidatorModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None
    CurrentState: Optional[NaturalLanguageQueryGenerationCurrentStateType] = None

class OptionStatusTypeDef(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None

class AWSDomainInformationTypeDef(BaseValidatorModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None

class AcceptInboundConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class AdditionalLimitTypeDef(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class JWTOptionsInputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None

class MasterUserOptionsTypeDef(BaseValidatorModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None

class JWTOptionsOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None

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
    UseOffPeakWindow: Optional[bool] = None

class AutoTuneStatusTypeDef(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None

class AvailabilityZoneInfoTypeDef(BaseValidatorModel):
    AvailabilityZoneName: Optional[str] = None
    ZoneStatus: Optional[ZoneStatusType] = None
    ConfiguredDataNodeCount: Optional[str] = None
    AvailableDataNodeCount: Optional[str] = None
    TotalShards: Optional[str] = None
    TotalUnAssignedShards: Optional[str] = None

class CancelDomainConfigChangeRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DryRun: Optional[bool] = None

class CancelledChangePropertyTypeDef(BaseValidatorModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None

class CancelServiceSoftwareUpdateRequestRequestTypeDef(BaseValidatorModel):
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
    InitiatedBy: Optional[InitiatedByType] = None
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class ChangeProgressStageTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None

class ColdStorageOptionsTypeDef(BaseValidatorModel):
    Enabled: bool

class ZoneAwarenessConfigTypeDef(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None

class CognitoOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None

class CompatibleVersionsMapTypeDef(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None

class CrossClusterSearchConnectionPropertiesTypeDef(BaseValidatorModel):
    SkipUnavailable: Optional[SkipUnavailableStatusType] = None

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

class SoftwareUpdateOptionsTypeDef(BaseValidatorModel):
    AutoSoftwareUpdateEnabled: Optional[bool] = None

class VPCOptionsTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class OutboundConnectionStatusTypeDef(BaseValidatorModel):
    StatusCode: Optional[OutboundConnectionStatusCodeType] = None
    Message: Optional[str] = None

class PackageSourceTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None

class S3GlueDataCatalogTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None

class DeleteDataSourceRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DeleteInboundConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionId: str

class DeleteOutboundConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionId: str

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

class DescribeDomainConfigRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DescribeDomainHealthRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DescribeDomainNodesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DomainNodesStatusTypeDef(BaseValidatorModel):
    NodeId: Optional[str] = None
    NodeType: Optional[NodeTypeType] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    NodeStatus: Optional[NodeStatusType] = None
    StorageType: Optional[str] = None
    StorageVolumeType: Optional[VolumeTypeType] = None
    StorageSize: Optional[str] = None

class DescribeDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DescribeDomainsRequestRequestTypeDef(BaseValidatorModel):
    DomainNames: Sequence[str]

class DescribeDryRunProgressRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DryRunId: Optional[str] = None
    LoadDryRunConfig: Optional[bool] = None

class DryRunResultsTypeDef(BaseValidatorModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DescribeInstanceTypeLimitsRequestRequestTypeDef(BaseValidatorModel):
    InstanceType: OpenSearchPartitionInstanceTypeType
    EngineVersion: str
    DomainName: Optional[str] = None

class DescribePackagesFilterTypeDef(BaseValidatorModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[Sequence[str]] = None

class DescribeReservedInstanceOfferingsRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedInstancesRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstanceId: Optional[str] = None
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

class ModifyingPropertiesTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None

class DomainInfoTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None

class DomainMaintenanceDetailsTypeDef(BaseValidatorModel):
    MaintenanceId: Optional[str] = None
    DomainName: Optional[str] = None
    Action: Optional[MaintenanceTypeType] = None
    NodeId: Optional[str] = None
    Status: Optional[MaintenanceStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None

class VPCDerivedInfoTypeDef(BaseValidatorModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class ValidationFailureTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class GetCompatibleVersionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None

class GetDataSourceRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str

class GetDomainMaintenanceStatusRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaintenanceId: str

class GetPackageVersionHistoryRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetUpgradeHistoryRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetUpgradeStatusRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class InboundConnectionStatusTypeDef(BaseValidatorModel):
    StatusCode: Optional[InboundConnectionStatusCodeType] = None
    Message: Optional[str] = None

class InstanceCountLimitsTypeDef(BaseValidatorModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None

class InstanceTypeDetailsTypeDef(BaseValidatorModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    EncryptionEnabled: Optional[bool] = None
    CognitoEnabled: Optional[bool] = None
    AppLogsEnabled: Optional[bool] = None
    AdvancedSecurityEnabled: Optional[bool] = None
    WarmEnabled: Optional[bool] = None
    InstanceRole: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None

class ListDataSourcesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class ListDomainMaintenancesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Action: Optional[MaintenanceTypeType] = None
    Status: Optional[MaintenanceStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDomainNamesRequestRequestTypeDef(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None

class ListDomainsForPackageRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInstanceTypeDetailsRequestRequestTypeDef(BaseValidatorModel):
    EngineVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RetrieveAZs: Optional[bool] = None
    InstanceType: Optional[str] = None

class ListPackagesForDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListScheduledActionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ScheduledActionTypeDef(BaseValidatorModel):
    Id: str
    Type: ActionTypeType
    Severity: ActionSeverityType
    ScheduledTime: int
    Description: Optional[str] = None
    ScheduledBy: Optional[ScheduledByType] = None
    Status: Optional[ActionStatusType] = None
    Mandatory: Optional[bool] = None
    Cancellable: Optional[bool] = None

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    ARN: str

class ListVersionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVpcEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsForDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None

class ListVpcEndpointsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class WindowStartTimeTypeDef(BaseValidatorModel):
    Hours: int
    Minutes: int

class PluginPropertiesTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    ClassName: Optional[str] = None
    UncompressedSizeInBytes: Optional[int] = None

class PurchaseReservedInstanceOfferingRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None

class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class RejectInboundConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionId: str

class RemoveTagsRequestRequestTypeDef(BaseValidatorModel):
    ARN: str
    TagKeys: Sequence[str]

class RevokeVpcEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Account: str

class SAMLIdpTypeDef(BaseValidatorModel):
    MetadataContent: str
    EntityId: str

class StartDomainMaintenanceRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Action: MaintenanceTypeType
    NodeId: Optional[str] = None

class StartServiceSoftwareUpdateRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ScheduleAt: Optional[ScheduleAtType] = None
    DesiredStartTime: Optional[int] = None

class StorageTypeLimitTypeDef(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None

class UpdateScheduledActionRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ActionID: str
    ActionType: ActionTypeType
    ScheduleAt: ScheduleAtType
    DesiredStartTime: Optional[int] = None

class UpgradeDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None

class UpgradeStepItemTypeDef(BaseValidatorModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None

class AIMLOptionsInputTypeDef(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[       NaturalLanguageQueryGenerationOptionsInputTypeDef     ] = None

class AIMLOptionsOutputTypeDef(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[       NaturalLanguageQueryGenerationOptionsOutputTypeDef     ] = None

class AccessPoliciesStatusTypeDef(BaseValidatorModel):
    Options: str
    Status: OptionStatusTypeDef

class AdvancedOptionsStatusTypeDef(BaseValidatorModel):
    Options: Dict[str, str]
    Status: OptionStatusTypeDef

class IPAddressTypeStatusTypeDef(BaseValidatorModel):
    Options: IPAddressTypeType
    Status: OptionStatusTypeDef

class VersionStatusTypeDef(BaseValidatorModel):
    Options: str
    Status: OptionStatusTypeDef

class DomainInformationContainerTypeDef(BaseValidatorModel):
    AWSDomainInformation: Optional[AWSDomainInformationTypeDef] = None

class AddDataSourceResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainMaintenanceStatusResponseTypeDef(BaseValidatorModel):
    Status: MaintenanceStatusType
    StatusMessage: str
    NodeId: str
    Action: MaintenanceTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetUpgradeStatusResponseTypeDef(BaseValidatorModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseReservedInstanceOfferingResponseTypeDef(BaseValidatorModel):
    ReservedInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDomainMaintenanceResponseTypeDef(BaseValidatorModel):
    MaintenanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class EnvironmentInfoTypeDef(BaseValidatorModel):
    AvailabilityZoneInformation: Optional[List[AvailabilityZoneInfoTypeDef]] = None

class CancelDomainConfigChangeResponseTypeDef(BaseValidatorModel):
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangePropertyTypeDef]
    DryRun: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServiceSoftwareUpdateResponseTypeDef(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartServiceSoftwareUpdateResponseTypeDef(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradeDomainResponseTypeDef(BaseValidatorModel):
    UpgradeId: str
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    AdvancedOptions: Dict[str, str]
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
    LastUpdatedTime: Optional[datetime] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    InitiatedBy: Optional[InitiatedByType] = None

class ClusterConfigTypeDef(BaseValidatorModel):
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

class CognitoOptionsStatusTypeDef(BaseValidatorModel):
    Options: CognitoOptionsTypeDef
    Status: OptionStatusTypeDef

class GetCompatibleVersionsResponseTypeDef(BaseValidatorModel):
    CompatibleVersions: List[CompatibleVersionsMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionPropertiesTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None
    CrossClusterSearch: Optional[CrossClusterSearchConnectionPropertiesTypeDef] = None

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

class SoftwareUpdateOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[SoftwareUpdateOptionsTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None

class CreateVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    DomainArn: str
    VpcOptions: VPCOptionsTypeDef
    ClientToken: Optional[str] = None

class UpdateVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    VpcEndpointId: str
    VpcOptions: VPCOptionsTypeDef

class CreatePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageName: str
    PackageType: PackageTypeType
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None

class UpdatePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageID: str
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None

class DataSourceTypeTypeDef(BaseValidatorModel):
    S3GlueDataCatalog: Optional[S3GlueDataCatalogTypeDef] = None

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

class DescribeDomainNodesResponseTypeDef(BaseValidatorModel):
    DomainNodesStatusList: List[DomainNodesStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundConnectionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeOutboundConnectionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePackagesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[DescribePackagesFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDomainNamesResponseTypeDef(BaseValidatorModel):
    DomainNames: List[DomainInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainMaintenancesResponseTypeDef(BaseValidatorModel):
    DomainMaintenances: List[DomainMaintenanceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DomainPackageDetailsTypeDef(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[PackageTypeType] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

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

class DryRunProgressStatusTypeDef(BaseValidatorModel):
    DryRunId: str
    DryRunStatus: str
    CreationDate: str
    UpdateDate: str
    ValidationFailures: Optional[List[ValidationFailureTypeDef]] = None

class InstanceLimitsTypeDef(BaseValidatorModel):
    InstanceCountLimits: Optional[InstanceCountLimitsTypeDef] = None

class ListInstanceTypeDetailsResponseTypeDef(BaseValidatorModel):
    InstanceTypeDetails: List[InstanceTypeDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListScheduledActionsResponseTypeDef(BaseValidatorModel):
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateScheduledActionResponseTypeDef(BaseValidatorModel):
    ScheduledAction: ScheduledActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OffPeakWindowTypeDef(BaseValidatorModel):
    WindowStartTime: Optional[WindowStartTimeTypeDef] = None

class PackageDetailsTypeDef(BaseValidatorModel):
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

class PackageVersionHistoryTypeDef(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    PluginProperties: Optional[PluginPropertiesTypeDef] = None

class ReservedInstanceOfferingTypeDef(BaseValidatorModel):
    ReservedInstanceOfferingId: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReservedInstanceTypeDef(BaseValidatorModel):
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

class AIMLOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[AIMLOptionsOutputTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None

class InboundConnectionTypeDef(BaseValidatorModel):
    LocalDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    RemoteDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    ConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundConnectionStatusTypeDef] = None
    ConnectionMode: Optional[ConnectionModeType] = None

class AutoTuneTypeDef(BaseValidatorModel):
    AutoTuneType: Optional[Literal["SCHEDULED_ACTION"]] = None
    AutoTuneDetails: Optional[AutoTuneDetailsTypeDef] = None

class AutoTuneOptionsExtraOutputTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutputTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None

class AutoTuneOptionsInputTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None

class AutoTuneOptionsTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None

class DescribeDomainHealthResponseTypeDef(BaseValidatorModel):
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

class DescribeDomainChangeProgressResponseTypeDef(BaseValidatorModel):
    ChangeProgressStatus: ChangeProgressStatusDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterConfigStatusTypeDef(BaseValidatorModel):
    Options: ClusterConfigTypeDef
    Status: OptionStatusTypeDef

class CreateOutboundConnectionRequestRequestTypeDef(BaseValidatorModel):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionPropertiesTypeDef] = None

class CreateOutboundConnectionResponseTypeDef(BaseValidatorModel):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionStatus: OutboundConnectionStatusTypeDef
    ConnectionId: str
    ConnectionMode: ConnectionModeType
    ConnectionProperties: ConnectionPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OutboundConnectionTypeDef(BaseValidatorModel):
    LocalDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    RemoteDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    ConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundConnectionStatusTypeDef] = None
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionPropertiesTypeDef] = None

class AddDataSourceRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: Optional[str] = None

class DataSourceDetailsTypeDef(BaseValidatorModel):
    DataSourceType: Optional[DataSourceTypeTypeDef] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None

class GetDataSourceResponseTypeDef(BaseValidatorModel):
    DataSourceType: DataSourceTypeTypeDef
    Name: str
    Description: str
    Status: DataSourceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None

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

class OffPeakWindowOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    OffPeakWindow: Optional[OffPeakWindowTypeDef] = None

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

class GetPackageVersionHistoryResponseTypeDef(BaseValidatorModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstanceOfferingsResponseTypeDef(BaseValidatorModel):
    ReservedInstanceOfferings: List[ReservedInstanceOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstancesResponseTypeDef(BaseValidatorModel):
    ReservedInstances: List[ReservedInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AdvancedSecurityOptionsInputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptionsTypeDef] = None
    SAMLOptions: Optional[SAMLOptionsInputTypeDef] = None
    JWTOptions: Optional[JWTOptionsInputTypeDef] = None
    AnonymousAuthEnabled: Optional[bool] = None

class AdvancedSecurityOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutputTypeDef] = None
    JWTOptions: Optional[JWTOptionsOutputTypeDef] = None
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

class AcceptInboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundConnectionsResponseTypeDef(BaseValidatorModel):
    Connections: List[InboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectInboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainAutoTunesResponseTypeDef(BaseValidatorModel):
    AutoTunes: List[AutoTuneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoTuneOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[AutoTuneOptionsExtraOutputTypeDef] = None
    Status: Optional[AutoTuneStatusTypeDef] = None

class DeleteOutboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: OutboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOutboundConnectionsResponseTypeDef(BaseValidatorModel):
    Connections: List[OutboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    DataSources: List[DataSourceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OffPeakWindowOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[OffPeakWindowOptionsTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None

class CreateDomainRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDomainConfigRequestRequestTypeDef(BaseValidatorModel):
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

class AdvancedSecurityOptionsStatusTypeDef(BaseValidatorModel):
    Options: AdvancedSecurityOptionsTypeDef
    Status: OptionStatusTypeDef

class DomainStatusTypeDef(BaseValidatorModel):
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

class DescribeInstanceTypeLimitsResponseTypeDef(BaseValidatorModel):
    LimitsByRole: Dict[str, LimitsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainConfigTypeDef(BaseValidatorModel):
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

class CreateDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainsResponseTypeDef(BaseValidatorModel):
    DomainStatusList: List[DomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDryRunProgressResponseTypeDef(BaseValidatorModel):
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    DryRunConfig: DomainStatusTypeDef
    DryRunResults: DryRunResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainConfigResponseTypeDef(BaseValidatorModel):
    DomainConfig: DomainConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainConfigResponseTypeDef(BaseValidatorModel):
    DomainConfig: DomainConfigTypeDef
    DryRunResults: DryRunResultsTypeDef
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

