from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.redshift.redshift_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptReservedNodeExchangeInputMessage(BaseValidatorModel):
    ReservedNodeId: str
    TargetReservedNodeOfferingId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AttributeValueTarget(BaseValidatorModel):
    AttributeValue: Optional[str] = None


class AccountWithRestoreAccess(BaseValidatorModel):
    AccountId: Optional[str] = None
    AccountAlias: Optional[str] = None


class AquaConfiguration(BaseValidatorModel):
    AquaStatus: Optional[AquaStatusType] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None


class AssociateDataShareConsumerMessage(BaseValidatorModel):
    DataShareArn: str
    AssociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None
    AllowWrites: Optional[bool] = None


class CertificateAssociation(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None


class AuthenticationProfile(BaseValidatorModel):
    AuthenticationProfileName: Optional[str] = None
    AuthenticationProfileContent: Optional[str] = None


class AuthorizeClusterSecurityGroupIngressMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


class AuthorizeDataShareMessage(BaseValidatorModel):
    DataShareArn: str
    ConsumerIdentifier: str
    AllowWrites: Optional[bool] = None


class AuthorizeEndpointAccessMessage(BaseValidatorModel):
    Account: str
    ClusterIdentifier: Optional[str] = None
    VpcIds: Optional[List[str]] = None


class AuthorizeSnapshotAccessMessage(BaseValidatorModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None


class AuthorizedTokenIssuerOutput(BaseValidatorModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None


class AuthorizedTokenIssuer(BaseValidatorModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None


class SupportedPlatform(BaseValidatorModel):
    Name: Optional[str] = None


class DeleteClusterSnapshotMessage(BaseValidatorModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None


class SnapshotErrorMessage(BaseValidatorModel):
    SnapshotIdentifier: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None


class BatchModifyClusterSnapshotsMessage(BaseValidatorModel):
    SnapshotIdentifierList: List[str]
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None


class CancelResizeMessage(BaseValidatorModel):
    ClusterIdentifier: str


class ClusterAssociatedToSchedule(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleAssociationState: Optional[ScheduleStateType] = None


class RevisionTarget(BaseValidatorModel):
    DatabaseRevision: Optional[str] = None
    Description: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None


class ClusterIamRole(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    ApplyStatus: Optional[str] = None


class ClusterNode(BaseValidatorModel):
    NodeRole: Optional[str] = None
    PrivateIPAddress: Optional[str] = None
    PublicIPAddress: Optional[str] = None


class Parameter(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    ApplyType: Optional[ParameterApplyTypeType] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None


class ClusterParameterStatus(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ClusterSecurityGroupMembership(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class ClusterSnapshotCopyStatus(BaseValidatorModel):
    DestinationRegion: Optional[str] = None
    RetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None


class DataTransferProgress(BaseValidatorModel):
    Status: Optional[str] = None
    CurrentRateInMegaBytesPerSecond: Optional[float] = None
    TotalDataInMegaBytes: Optional[int] = None
    DataTransferredInMegaBytes: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None


class DeferredMaintenanceWindow(BaseValidatorModel):
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[datetime] = None
    DeferMaintenanceEndTime: Optional[datetime] = None


class ElasticIpStatus(BaseValidatorModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None


class HsmStatus(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None


class PendingModifiedValues(BaseValidatorModel):
    MasterUserPassword: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    ClusterType: Optional[str] = None
    ClusterVersion: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ClusterIdentifier: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    EncryptionType: Optional[str] = None


class ReservedNodeExchangeStatus(BaseValidatorModel):
    ReservedNodeExchangeRequestId: Optional[str] = None
    Status: Optional[ReservedNodeExchangeStatusTypeType] = None
    RequestTime: Optional[datetime] = None
    SourceReservedNodeId: Optional[str] = None
    SourceReservedNodeType: Optional[str] = None
    SourceReservedNodeCount: Optional[int] = None
    TargetReservedNodeOfferingId: Optional[str] = None
    TargetReservedNodeType: Optional[str] = None
    TargetReservedNodeCount: Optional[int] = None


class ResizeInfo(BaseValidatorModel):
    ResizeType: Optional[str] = None
    AllowCancelResize: Optional[bool] = None


class RestoreStatus(BaseValidatorModel):
    Status: Optional[str] = None
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None


class VpcSecurityGroupMembership(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class ClusterVersion(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None


class CopyClusterSnapshotMessage(BaseValidatorModel):
    SourceSnapshotIdentifier: str
    TargetSnapshotIdentifier: str
    SourceSnapshotClusterIdentifier: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None


class CreateAuthenticationProfileMessage(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str


class CreateCustomDomainAssociationMessage(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str


class CreateEndpointAccessMessage(BaseValidatorModel):
    EndpointName: str
    SubnetGroupName: str
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None

Timestamp = Union[datetime, str]


class DataShareAssociation(BaseValidatorModel):
    ConsumerIdentifier: Optional[str] = None
    Status: Optional[DataShareStatusType] = None
    ConsumerRegion: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    StatusChangeDate: Optional[datetime] = None
    ProducerAllowedWrites: Optional[bool] = None
    ConsumerAcceptedWrites: Optional[bool] = None


class DeauthorizeDataShareMessage(BaseValidatorModel):
    DataShareArn: str
    ConsumerIdentifier: str


class DeleteAuthenticationProfileMessage(BaseValidatorModel):
    AuthenticationProfileName: str


class DeleteClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    SkipFinalClusterSnapshot: Optional[bool] = None
    FinalClusterSnapshotIdentifier: Optional[str] = None
    FinalClusterSnapshotRetentionPeriod: Optional[int] = None


class DeleteClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str


class DeleteClusterSecurityGroupMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str


class DeleteClusterSnapshotMessageRequest(BaseValidatorModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None


class DeleteClusterSubnetGroupMessage(BaseValidatorModel):
    ClusterSubnetGroupName: str


class DeleteCustomDomainAssociationMessage(BaseValidatorModel):
    ClusterIdentifier: str
    CustomDomainName: str


class DeleteEndpointAccessMessage(BaseValidatorModel):
    EndpointName: str


class DeleteEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str


class DeleteHsmClientCertificateMessage(BaseValidatorModel):
    HsmClientCertificateIdentifier: str


class DeleteHsmConfigurationMessage(BaseValidatorModel):
    HsmConfigurationIdentifier: str


class DeleteIntegrationMessage(BaseValidatorModel):
    IntegrationArn: str


class DeleteRedshiftIdcApplicationMessage(BaseValidatorModel):
    RedshiftIdcApplicationArn: str


class DeleteResourcePolicyMessage(BaseValidatorModel):
    ResourceArn: str


class DeleteScheduledActionMessage(BaseValidatorModel):
    ScheduledActionName: str


class DeleteSnapshotCopyGrantMessage(BaseValidatorModel):
    SnapshotCopyGrantName: str


class DeleteSnapshotScheduleMessage(BaseValidatorModel):
    ScheduleIdentifier: str


class DeleteTagsMessage(BaseValidatorModel):
    ResourceName: str
    TagKeys: List[str]


class DeleteUsageLimitMessage(BaseValidatorModel):
    UsageLimitId: str


class DescribeAccountAttributesMessage(BaseValidatorModel):
    AttributeNames: Optional[List[str]] = None


class DescribeAuthenticationProfilesMessage(BaseValidatorModel):
    AuthenticationProfileName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeClusterDbRevisionsMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeClusterParameterGroupsMessage(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeClusterParametersMessage(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeClusterSecurityGroupsMessage(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class SnapshotSortingEntity(BaseValidatorModel):
    Attribute: SnapshotAttributeToSortByType
    SortOrder: Optional[SortByOrderType] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeClusterSubnetGroupsMessage(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeClusterTracksMessage(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeClusterVersionsMessage(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeClustersMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeCustomDomainAssociationsMessage(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDataSharesForConsumerMessage(BaseValidatorModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDataSharesForProducerMessage(BaseValidatorModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDataSharesMessage(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDefaultClusterParametersMessage(BaseValidatorModel):
    ParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEndpointAccessMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEndpointAuthorizationMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEventCategoriesMessage(BaseValidatorModel):
    SourceType: Optional[str] = None


class DescribeEventSubscriptionsMessage(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeHsmClientCertificatesMessage(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeHsmConfigurationsMessage(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeInboundIntegrationsMessage(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeIntegrationsFilter(BaseValidatorModel):
    Name: DescribeIntegrationsFilterNameType
    Values: List[str]


class DescribeLoggingStatusMessage(BaseValidatorModel):
    ClusterIdentifier: str


class NodeConfigurationOptionsFilter(BaseValidatorModel):
    Name: Optional[NodeConfigurationOptionsFilterNameType] = None
    Operator: Optional[OperatorTypeType] = None
    Values: Optional[List[str]] = None


class DescribeOrderableClusterOptionsMessage(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribePartnersInputMessage(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None


class PartnerIntegrationInfo(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None
    Status: Optional[PartnerIntegrationStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class DescribeRedshiftIdcApplicationsMessage(BaseValidatorModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReservedNodeExchangeStatusInputMessage(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReservedNodeOfferingsMessage(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReservedNodesMessage(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeResizeMessage(BaseValidatorModel):
    ClusterIdentifier: str


class ScheduledActionFilter(BaseValidatorModel):
    Name: ScheduledActionFilterNameType
    Values: List[str]


class DescribeSnapshotCopyGrantsMessage(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeSnapshotSchedulesMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeTableRestoreStatusMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeTagsMessage(BaseValidatorModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DescribeUsageLimitsMessage(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class DisableLoggingMessage(BaseValidatorModel):
    ClusterIdentifier: str


class DisableSnapshotCopyMessage(BaseValidatorModel):
    ClusterIdentifier: str


class DisassociateDataShareConsumerMessage(BaseValidatorModel):
    DataShareArn: str
    DisassociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None


class EnableLoggingMessage(BaseValidatorModel):
    ClusterIdentifier: str
    BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    LogDestinationType: Optional[LogDestinationTypeType] = None
    LogExports: Optional[List[str]] = None


class EnableSnapshotCopyMessage(BaseValidatorModel):
    ClusterIdentifier: str
    DestinationRegion: str
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None


class EndpointAuthorization(BaseValidatorModel):
    Grantor: Optional[str] = None
    Grantee: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    AuthorizeTime: Optional[datetime] = None
    ClusterStatus: Optional[str] = None
    Status: Optional[AuthorizationStatusType] = None
    AllowedAllVPCs: Optional[bool] = None
    AllowedVPCs: Optional[List[str]] = None
    EndpointCount: Optional[int] = None


class EventInfoMap(BaseValidatorModel):
    EventId: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    EventDescription: Optional[str] = None
    Severity: Optional[str] = None


class Event(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Date: Optional[datetime] = None
    EventId: Optional[str] = None


class FailoverPrimaryComputeInputMessage(BaseValidatorModel):
    ClusterIdentifier: str


class GetClusterCredentialsMessage(BaseValidatorModel):
    DbUser: str
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    AutoCreate: Optional[bool] = None
    DbGroups: Optional[List[str]] = None
    CustomDomainName: Optional[str] = None


class GetClusterCredentialsWithIAMMessage(BaseValidatorModel):
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    CustomDomainName: Optional[str] = None


class GetReservedNodeExchangeConfigurationOptionsInputMessage(BaseValidatorModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class GetReservedNodeExchangeOfferingsInputMessage(BaseValidatorModel):
    ReservedNodeId: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class GetResourcePolicyMessage(BaseValidatorModel):
    ResourceArn: str


class ResourcePolicy(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None


class IntegrationError(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: Optional[str] = None


class LakeFormationQuery(BaseValidatorModel):
    Authorization: ServiceAuthorizationType


class ListRecommendationsMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class ModifyAquaInputMessage(BaseValidatorModel):
    ClusterIdentifier: str
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None


class ModifyAuthenticationProfileMessage(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str


class ModifyClusterDbRevisionMessage(BaseValidatorModel):
    ClusterIdentifier: str
    RevisionTarget: str


class ModifyClusterIamRolesMessage(BaseValidatorModel):
    ClusterIdentifier: str
    AddIamRoles: Optional[List[str]] = None
    RemoveIamRoles: Optional[List[str]] = None
    DefaultIamRoleArn: Optional[str] = None


class ModifyClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    ClusterSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    MasterUserPassword: Optional[str] = None
    ClusterParameterGroupName: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    NewClusterIdentifier: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ElasticIp: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    AvailabilityZoneRelocation: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    Port: Optional[int] = None
    ManageMasterPassword: Optional[bool] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[bool] = None


class ModifyClusterSnapshotMessage(BaseValidatorModel):
    SnapshotIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None


class ModifyClusterSnapshotScheduleMessage(BaseValidatorModel):
    ClusterIdentifier: str
    ScheduleIdentifier: Optional[str] = None
    DisassociateSchedule: Optional[bool] = None


class ModifyClusterSubnetGroupMessage(BaseValidatorModel):
    ClusterSubnetGroupName: str
    SubnetIds: List[str]
    Description: Optional[str] = None


class ModifyCustomDomainAssociationMessage(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str


class ModifyEndpointAccessMessage(BaseValidatorModel):
    EndpointName: str
    VpcSecurityGroupIds: Optional[List[str]] = None


class ModifyEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIds: Optional[List[str]] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None


class ModifyIntegrationMessage(BaseValidatorModel):
    IntegrationArn: str
    Description: Optional[str] = None
    IntegrationName: Optional[str] = None


class ModifySnapshotCopyRetentionPeriodMessage(BaseValidatorModel):
    ClusterIdentifier: str
    RetentionPeriod: int
    Manual: Optional[bool] = None


class ModifySnapshotScheduleMessage(BaseValidatorModel):
    ScheduleIdentifier: str
    ScheduleDefinitions: List[str]


class ModifyUsageLimitMessage(BaseValidatorModel):
    UsageLimitId: str
    Amount: Optional[int] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None


class ProvisionedIdentifier(BaseValidatorModel):
    ClusterIdentifier: str


class ServerlessIdentifier(BaseValidatorModel):
    NamespaceIdentifier: str
    WorkgroupIdentifier: str


class NetworkInterface(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    SubnetId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Ipv6Address: Optional[str] = None


class NodeConfigurationOption(BaseValidatorModel):
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    EstimatedDiskUtilizationPercent: Optional[float] = None
    Mode: Optional[ModeType] = None


class PartnerIntegrationInputMessageRequest(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str


class PartnerIntegrationInputMessage(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str


class PauseClusterMessageRequest(BaseValidatorModel):
    ClusterIdentifier: str


class PauseClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str


class PurchaseReservedNodeOfferingMessage(BaseValidatorModel):
    ReservedNodeOfferingId: str
    NodeCount: Optional[int] = None


class PutResourcePolicyMessage(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class ReadWriteAccess(BaseValidatorModel):
    Authorization: ServiceAuthorizationType


class RebootClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str


class RecommendedAction(BaseValidatorModel):
    Text: Optional[str] = None
    Database: Optional[str] = None
    Command: Optional[str] = None
    Type: Optional[RecommendedActionTypeType] = None


class ReferenceLink(BaseValidatorModel):
    Text: Optional[str] = None
    Link: Optional[str] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class RejectDataShareMessage(BaseValidatorModel):
    DataShareArn: str


class ResizeClusterMessageRequest(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None


class ResizeClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None


class RestoreFromClusterSnapshotMessage(BaseValidatorModel):
    ClusterIdentifier: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    ClusterSubnetGroupName: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    OwnerAccount: Optional[str] = None
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    ElasticIp: Optional[str] = None
    ClusterParameterGroupName: Optional[str] = None
    ClusterSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    KmsKeyId: Optional[str] = None
    NodeType: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    AvailabilityZoneRelocation: Optional[bool] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None
    DefaultIamRoleArn: Optional[str] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None
    Encrypted: Optional[bool] = None
    ManageMasterPassword: Optional[bool] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[bool] = None


class RestoreTableFromClusterSnapshotMessage(BaseValidatorModel):
    ClusterIdentifier: str
    SnapshotIdentifier: str
    SourceDatabaseName: str
    SourceTableName: str
    NewTableName: str
    SourceSchemaName: Optional[str] = None
    TargetDatabaseName: Optional[str] = None
    TargetSchemaName: Optional[str] = None
    EnableCaseSensitiveIdentifier: Optional[bool] = None


class TableRestoreStatus(BaseValidatorModel):
    TableRestoreRequestId: Optional[str] = None
    Status: Optional[TableRestoreStatusTypeType] = None
    Message: Optional[str] = None
    RequestTime: Optional[datetime] = None
    ProgressInMegaBytes: Optional[int] = None
    TotalDataInMegaBytes: Optional[int] = None
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SourceDatabaseName: Optional[str] = None
    SourceSchemaName: Optional[str] = None
    SourceTableName: Optional[str] = None
    TargetDatabaseName: Optional[str] = None
    TargetSchemaName: Optional[str] = None
    NewTableName: Optional[str] = None


class ResumeClusterMessageRequest(BaseValidatorModel):
    ClusterIdentifier: str


class ResumeClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str


class RevokeClusterSecurityGroupIngressMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


class RevokeEndpointAccessMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    VpcIds: Optional[List[str]] = None
    Force: Optional[bool] = None


class RevokeSnapshotAccessMessage(BaseValidatorModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None


class RotateEncryptionKeyMessage(BaseValidatorModel):
    ClusterIdentifier: str


class SupportedOperation(BaseValidatorModel):
    OperationName: Optional[str] = None


class UpdatePartnerStatusInputMessage(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str
    Status: PartnerIntegrationStatusType
    StatusMessage: Optional[str] = None


class ClusterCredentials(BaseValidatorModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadata


class ClusterExtendedCredentials(BaseValidatorModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    NextRefreshTime: datetime
    ResponseMetadata: ResponseMetadata


class ClusterParameterGroupNameMessage(BaseValidatorModel):
    ParameterGroupName: str
    ParameterGroupStatus: str
    ResponseMetadata: ResponseMetadata


class CreateAuthenticationProfileResult(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadata


class CreateCustomDomainAssociationResult(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadata


class CustomerStorageMessage(BaseValidatorModel):
    TotalBackupSizeInMegaBytes: float
    TotalProvisionedStorageInMegaBytes: float
    ResponseMetadata: ResponseMetadata


class DeleteAuthenticationProfileResult(BaseValidatorModel):
    AuthenticationProfileName: str
    ResponseMetadata: ResponseMetadata


class DeregisterNamespaceOutputMessage(BaseValidatorModel):
    Status: NamespaceRegistrationStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EndpointAuthorizationResponse(BaseValidatorModel):
    Grantor: str
    Grantee: str
    ClusterIdentifier: str
    AuthorizeTime: datetime
    ClusterStatus: str
    Status: AuthorizationStatusType
    AllowedAllVPCs: bool
    AllowedVPCs: List[str]
    EndpointCount: int
    ResponseMetadata: ResponseMetadata


class LoggingStatus(BaseValidatorModel):
    LoggingEnabled: bool
    BucketName: str
    S3KeyPrefix: str
    LastSuccessfulDeliveryTime: datetime
    LastFailureTime: datetime
    LastFailureMessage: str
    LogDestinationType: LogDestinationTypeType
    LogExports: List[str]
    ResponseMetadata: ResponseMetadata


class ModifyAuthenticationProfileResult(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadata


class ModifyCustomDomainAssociationResult(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadata


class PartnerIntegrationOutputMessage(BaseValidatorModel):
    DatabaseName: str
    PartnerName: str
    ResponseMetadata: ResponseMetadata


class RegisterNamespaceOutputMessage(BaseValidatorModel):
    Status: NamespaceRegistrationStatusType
    ResponseMetadata: ResponseMetadata


class ResizeProgressMessage(BaseValidatorModel):
    TargetNodeType: str
    TargetNumberOfNodes: int
    TargetClusterType: str
    Status: str
    ImportTablesCompleted: List[str]
    ImportTablesInProgress: List[str]
    ImportTablesNotStarted: List[str]
    AvgResizeRateInMegaBytesPerSecond: float
    TotalResizeDataInMegaBytes: int
    ProgressInMegaBytes: int
    ElapsedTimeInSeconds: int
    EstimatedTimeToCompletionInSeconds: int
    ResizeType: str
    Message: str
    TargetEncryptionType: str
    DataTransferProgressPercent: float
    ResponseMetadata: ResponseMetadata


class AccountAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[AttributeValueTarget]] = None


class ModifyAquaOutputMessage(BaseValidatorModel):
    AquaConfiguration: AquaConfiguration
    ResponseMetadata: ResponseMetadata


class Association(BaseValidatorModel):
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    CertificateAssociations: Optional[List[CertificateAssociation]] = None


class DescribeAuthenticationProfilesResult(BaseValidatorModel):
    AuthenticationProfiles: List[AuthenticationProfile]
    ResponseMetadata: ResponseMetadata

AuthorizedTokenIssuerUnion = Union[AuthorizedTokenIssuer, AuthorizedTokenIssuerOutput]


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None
    SupportedPlatforms: Optional[List[SupportedPlatform]] = None


class BatchDeleteClusterSnapshotsRequest(BaseValidatorModel):
    Identifiers: List[DeleteClusterSnapshotMessage]


class BatchDeleteClusterSnapshotsResult(BaseValidatorModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessage]
    ResponseMetadata: ResponseMetadata


class BatchModifyClusterSnapshotsOutputMessage(BaseValidatorModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessage]
    ResponseMetadata: ResponseMetadata


class ClusterDbRevision(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    CurrentDatabaseRevision: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None
    RevisionTargets: Optional[List[RevisionTarget]] = None


class SecondaryClusterInfo(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNode]] = None


class ClusterParameterGroupDetails(BaseValidatorModel):
    Parameters: List[Parameter]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DefaultClusterParameters(BaseValidatorModel):
    ParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None


class ModifyClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str
    Parameters: List[Parameter]


class ResetClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[List[Parameter]] = None


class ClusterParameterGroupStatus(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ClusterParameterStatusList: Optional[List[ClusterParameterStatus]] = None


class ClusterParameterGroup(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    NodeType: str
    MasterUsername: str
    DBName: Optional[str] = None
    ClusterType: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    ClusterSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    ClusterSubnetGroupName: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ClusterParameterGroupName: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Port: Optional[int] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    Encrypted: Optional[bool] = None
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    ElasticIp: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    AvailabilityZoneRelocation: Optional[bool] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None
    DefaultIamRoleArn: Optional[str] = None
    LoadSampleData: Optional[str] = None
    ManageMasterPassword: Optional[bool] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    RedshiftIdcApplicationArn: Optional[str] = None


class CreateClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str
    ParameterGroupFamily: str
    Description: str
    Tags: Optional[List[Tag]] = None


class CreateClusterSecurityGroupMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str
    Description: str
    Tags: Optional[List[Tag]] = None


class CreateClusterSnapshotMessage(BaseValidatorModel):
    SnapshotIdentifier: str
    ClusterIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Tags: Optional[List[Tag]] = None


class CreateClusterSubnetGroupMessage(BaseValidatorModel):
    ClusterSubnetGroupName: str
    Description: str
    SubnetIds: List[str]
    Tags: Optional[List[Tag]] = None


class CreateEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    SourceIds: Optional[List[str]] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class CreateHsmClientCertificateMessage(BaseValidatorModel):
    HsmClientCertificateIdentifier: str
    Tags: Optional[List[Tag]] = None


class CreateHsmConfigurationMessage(BaseValidatorModel):
    HsmConfigurationIdentifier: str
    Description: str
    HsmIpAddress: str
    HsmPartitionName: str
    HsmPartitionPassword: str
    HsmServerPublicCertificate: str
    Tags: Optional[List[Tag]] = None


class CreateIntegrationMessage(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    KMSKeyId: Optional[str] = None
    TagList: Optional[List[Tag]] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Description: Optional[str] = None


class CreateSnapshotCopyGrantMessage(BaseValidatorModel):
    SnapshotCopyGrantName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateSnapshotScheduleMessage(BaseValidatorModel):
    ScheduleDefinitions: Optional[List[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DryRun: Optional[bool] = None
    NextInvocations: Optional[int] = None


class CreateTagsMessage(BaseValidatorModel):
    ResourceName: str
    Tags: List[Tag]


class CreateUsageLimitMessage(BaseValidatorModel):
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[List[Tag]] = None


class EC2SecurityGroup(BaseValidatorModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class EventSubscription(BaseValidatorModel):
    CustomerAwsId: Optional[str] = None
    CustSubscriptionId: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[datetime] = None
    SourceType: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    EventCategoriesList: Optional[List[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class HsmClientCertificate(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmClientCertificatePublicKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class HsmConfiguration(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    Description: Optional[str] = None
    HsmIpAddress: Optional[str] = None
    HsmPartitionName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class IPRange(BaseValidatorModel):
    Status: Optional[str] = None
    CIDRIP: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class SnapshotCopyGrant(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class SnapshotScheduleResponse(BaseValidatorModel):
    ScheduleDefinitions: List[str]
    ScheduleIdentifier: str
    ScheduleDescription: str
    Tags: List[Tag]
    NextInvocations: List[datetime]
    AssociatedClusterCount: int
    AssociatedClusters: List[ClusterAssociatedToSchedule]
    ResponseMetadata: ResponseMetadata


class SnapshotSchedule(BaseValidatorModel):
    ScheduleDefinitions: Optional[List[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    NextInvocations: Optional[List[datetime]] = None
    AssociatedClusterCount: Optional[int] = None
    AssociatedClusters: Optional[List[ClusterAssociatedToSchedule]] = None


class Snapshot(BaseValidatorModel):
    SnapshotIdentifier: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[datetime] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    ClusterVersion: Optional[str] = None
    EngineFullVersion: Optional[str] = None
    SnapshotType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    DBName: Optional[str] = None
    VpcId: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    EncryptedWithHSM: Optional[bool] = None
    AccountsWithRestoreAccess: Optional[List[AccountWithRestoreAccess]] = None
    OwnerAccount: Optional[str] = None
    TotalBackupSizeInMegaBytes: Optional[float] = None
    ActualIncrementalBackupSizeInMegaBytes: Optional[float] = None
    BackupProgressInMegaBytes: Optional[float] = None
    CurrentBackupRateInMegaBytesPerSecond: Optional[float] = None
    EstimatedSecondsToCompletion: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    SourceRegion: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    RestorableNodeTypes: Optional[List[str]] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRemainingDays: Optional[int] = None
    SnapshotRetentionStartTime: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    SnapshotArn: Optional[str] = None


class TaggedResource(BaseValidatorModel):
    Tag: Optional[Tag] = None
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None


class UsageLimitResponse(BaseValidatorModel):
    UsageLimitId: str
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: UsageLimitPeriodType
    BreachAction: UsageLimitBreachActionType
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UsageLimit(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    LimitType: Optional[UsageLimitLimitTypeType] = None
    Amount: Optional[int] = None
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[List[Tag]] = None


class DescribeReservedNodeExchangeStatusOutputMessage(BaseValidatorModel):
    ReservedNodeExchangeStatusDetails: List[ReservedNodeExchangeStatus]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ClusterVersionsMessage(BaseValidatorModel):
    Marker: str
    ClusterVersions: List[ClusterVersion]
    ResponseMetadata: ResponseMetadata


class DescribeEventsMessage(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class ModifyClusterMaintenanceMessage(BaseValidatorModel):
    ClusterIdentifier: str
    DeferMaintenance: Optional[bool] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[Timestamp] = None
    DeferMaintenanceEndTime: Optional[Timestamp] = None
    DeferMaintenanceDuration: Optional[int] = None


class DataShareResponse(BaseValidatorModel):
    DataShareArn: str
    ProducerArn: str
    AllowPubliclyAccessibleConsumers: bool
    DataShareAssociations: List[DataShareAssociation]
    ManagedBy: str
    DataShareType: Literal['INTERNAL']
    ResponseMetadata: ResponseMetadata


class DataShare(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    ProducerArn: Optional[str] = None
    AllowPubliclyAccessibleConsumers: Optional[bool] = None
    DataShareAssociations: Optional[List[DataShareAssociation]] = None
    ManagedBy: Optional[str] = None
    DataShareType: Optional[Literal['INTERNAL']] = None


class DescribeClusterDbRevisionsMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterParameterGroupsMessagePaginate(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterParametersMessagePaginate(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterSecurityGroupsMessagePaginate(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterSubnetGroupsMessagePaginate(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterTracksMessagePaginate(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterVersionsMessagePaginate(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClustersMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCustomDomainAssociationsMessagePaginate(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataSharesForConsumerMessagePaginate(BaseValidatorModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataSharesForProducerMessagePaginate(BaseValidatorModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataSharesMessagePaginate(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDefaultClusterParametersMessagePaginate(BaseValidatorModel):
    ParameterGroupFamily: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEndpointAccessMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEndpointAuthorizationMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventSubscriptionsMessagePaginate(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeHsmClientCertificatesMessagePaginate(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeHsmConfigurationsMessagePaginate(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInboundIntegrationsMessagePaginate(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrderableClusterOptionsMessagePaginate(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRedshiftIdcApplicationsMessagePaginate(BaseValidatorModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodeExchangeStatusInputMessagePaginate(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodeOfferingsMessagePaginate(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodesMessagePaginate(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotCopyGrantsMessagePaginate(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotSchedulesMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTableRestoreStatusMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTagsMessagePaginate(BaseValidatorModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUsageLimitsMessagePaginate(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReservedNodeExchangeConfigurationOptionsInputMessagePaginate(BaseValidatorModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReservedNodeExchangeOfferingsInputMessagePaginate(BaseValidatorModel):
    ReservedNodeId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecommendationsMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterSnapshotsMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[List[SnapshotSortingEntity]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterSnapshotsMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[List[SnapshotSortingEntity]] = None


class DescribeClusterSnapshotsMessageWait(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[List[SnapshotSortingEntity]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClustersMessageWaitExtraExtra(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClustersMessageWaitExtra(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClustersMessageWait(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeIntegrationsMessagePaginate(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    Filters: Optional[List[DescribeIntegrationsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeIntegrationsMessage(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[List[DescribeIntegrationsFilter]] = None


class DescribeNodeConfigurationOptionsMessagePaginate(BaseValidatorModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[List[NodeConfigurationOptionsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeNodeConfigurationOptionsMessage(BaseValidatorModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[List[NodeConfigurationOptionsFilter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribePartnersOutputMessage(BaseValidatorModel):
    PartnerIntegrationInfoList: List[PartnerIntegrationInfo]
    ResponseMetadata: ResponseMetadata


class DescribeScheduledActionsMessagePaginate(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Active: Optional[bool] = None
    Filters: Optional[List[ScheduledActionFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeScheduledActionsMessage(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Active: Optional[bool] = None
    Filters: Optional[List[ScheduledActionFilter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class EndpointAuthorizationList(BaseValidatorModel):
    EndpointAuthorizationList: List[EndpointAuthorization]
    Marker: str
    ResponseMetadata: ResponseMetadata


class EventCategoriesMap(BaseValidatorModel):
    SourceType: Optional[str] = None
    Events: Optional[List[EventInfoMap]] = None


class EventsMessage(BaseValidatorModel):
    Marker: str
    Events: List[Event]
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResult(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResult(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class InboundIntegration(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    Status: Optional[ZeroETLIntegrationStatusType] = None
    Errors: Optional[List[IntegrationError]] = None
    CreateTime: Optional[datetime] = None


class IntegrationResponse(BaseValidatorModel):
    IntegrationArn: str
    IntegrationName: str
    SourceArn: str
    TargetArn: str
    Status: ZeroETLIntegrationStatusType
    Errors: List[IntegrationError]
    CreateTime: datetime
    Description: str
    KMSKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class Integration(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    IntegrationName: Optional[str] = None
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    Status: Optional[ZeroETLIntegrationStatusType] = None
    Errors: Optional[List[IntegrationError]] = None
    CreateTime: Optional[datetime] = None
    Description: Optional[str] = None
    KMSKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None


class LakeFormationScopeUnion(BaseValidatorModel):
    LakeFormationQuery: Optional[LakeFormationQuery] = None


class NamespaceIdentifierUnion(BaseValidatorModel):
    ServerlessIdentifier: Optional[ServerlessIdentifier] = None
    ProvisionedIdentifier: Optional[ProvisionedIdentifier] = None


class VpcEndpoint(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    NetworkInterfaces: Optional[List[NetworkInterface]] = None


class NodeConfigurationOptionsMessage(BaseValidatorModel):
    NodeConfigurationOptionList: List[NodeConfigurationOption]
    Marker: str
    ResponseMetadata: ResponseMetadata


class S3AccessGrantsScopeUnion(BaseValidatorModel):
    ReadWriteAccess: Optional[ReadWriteAccess] = None


class Recommendation(BaseValidatorModel):
    Id: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    RecommendationType: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    Observation: Optional[str] = None
    ImpactRanking: Optional[ImpactRankingTypeType] = None
    RecommendationText: Optional[str] = None
    RecommendedActions: Optional[List[RecommendedAction]] = None
    ReferenceLinks: Optional[List[ReferenceLink]] = None


class ReservedNodeOffering(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None


class ReservedNode(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    NodeCount: Optional[int] = None
    State: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None


class RestoreTableFromClusterSnapshotResult(BaseValidatorModel):
    TableRestoreStatus: TableRestoreStatus
    ResponseMetadata: ResponseMetadata


class TableRestoreStatusMessage(BaseValidatorModel):
    TableRestoreStatusDetails: List[TableRestoreStatus]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ScheduledActionType(BaseValidatorModel):
    ResizeCluster: Optional[ResizeClusterMessage] = None
    PauseCluster: Optional[PauseClusterMessage] = None
    ResumeCluster: Optional[ResumeClusterMessage] = None


class UpdateTarget(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    SupportedOperations: Optional[List[SupportedOperation]] = None


class AccountAttributeList(BaseValidatorModel):
    AccountAttributes: List[AccountAttribute]
    ResponseMetadata: ResponseMetadata


class CustomDomainAssociationsMessage(BaseValidatorModel):
    Marker: str
    Associations: List[Association]
    ResponseMetadata: ResponseMetadata


class OrderableClusterOption(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZone]] = None


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetStatus: Optional[str] = None


class ClusterDbRevisionsMessage(BaseValidatorModel):
    Marker: str
    ClusterDbRevisions: List[ClusterDbRevision]
    ResponseMetadata: ResponseMetadata


class DescribeDefaultClusterParametersResult(BaseValidatorModel):
    DefaultClusterParameters: DefaultClusterParameters
    ResponseMetadata: ResponseMetadata


class ClusterParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    ParameterGroups: List[ClusterParameterGroup]
    ResponseMetadata: ResponseMetadata


class CreateClusterParameterGroupResult(BaseValidatorModel):
    ClusterParameterGroup: ClusterParameterGroup
    ResponseMetadata: ResponseMetadata


class CreateEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class EventSubscriptionsMessage(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscription]
    ResponseMetadata: ResponseMetadata


class ModifyEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class CreateHsmClientCertificateResult(BaseValidatorModel):
    HsmClientCertificate: HsmClientCertificate
    ResponseMetadata: ResponseMetadata


class HsmClientCertificateMessage(BaseValidatorModel):
    Marker: str
    HsmClientCertificates: List[HsmClientCertificate]
    ResponseMetadata: ResponseMetadata


class CreateHsmConfigurationResult(BaseValidatorModel):
    HsmConfiguration: HsmConfiguration
    ResponseMetadata: ResponseMetadata


class HsmConfigurationMessage(BaseValidatorModel):
    Marker: str
    HsmConfigurations: List[HsmConfiguration]
    ResponseMetadata: ResponseMetadata


class ClusterSecurityGroup(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Description: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroup]] = None
    IPRanges: Optional[List[IPRange]] = None
    Tags: Optional[List[Tag]] = None


class CreateSnapshotCopyGrantResult(BaseValidatorModel):
    SnapshotCopyGrant: SnapshotCopyGrant
    ResponseMetadata: ResponseMetadata


class SnapshotCopyGrantMessage(BaseValidatorModel):
    Marker: str
    SnapshotCopyGrants: List[SnapshotCopyGrant]
    ResponseMetadata: ResponseMetadata


class DescribeSnapshotSchedulesOutputMessage(BaseValidatorModel):
    SnapshotSchedules: List[SnapshotSchedule]
    Marker: str
    ResponseMetadata: ResponseMetadata


class AuthorizeSnapshotAccessResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class CopyClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class CreateClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class DeleteClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class ModifyClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class RevokeSnapshotAccessResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class SnapshotMessage(BaseValidatorModel):
    Marker: str
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata


class TaggedResourceListMessage(BaseValidatorModel):
    TaggedResources: List[TaggedResource]
    Marker: str
    ResponseMetadata: ResponseMetadata


class UsageLimitList(BaseValidatorModel):
    UsageLimits: List[UsageLimit]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeDataSharesForConsumerResult(BaseValidatorModel):
    DataShares: List[DataShare]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeDataSharesForProducerResult(BaseValidatorModel):
    DataShares: List[DataShare]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeDataSharesResult(BaseValidatorModel):
    DataShares: List[DataShare]
    Marker: str
    ResponseMetadata: ResponseMetadata


class EventCategoriesMessage(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMap]
    ResponseMetadata: ResponseMetadata


class InboundIntegrationsMessage(BaseValidatorModel):
    Marker: str
    InboundIntegrations: List[InboundIntegration]
    ResponseMetadata: ResponseMetadata


class IntegrationsMessage(BaseValidatorModel):
    Marker: str
    Integrations: List[Integration]
    ResponseMetadata: ResponseMetadata


class DeregisterNamespaceInputMessage(BaseValidatorModel):
    NamespaceIdentifier: NamespaceIdentifierUnion
    ConsumerIdentifiers: List[str]


class RegisterNamespaceInputMessage(BaseValidatorModel):
    NamespaceIdentifier: NamespaceIdentifierUnion
    ConsumerIdentifiers: List[str]


class EndpointAccessResponse(BaseValidatorModel):
    ClusterIdentifier: str
    ResourceOwner: str
    SubnetGroupName: str
    EndpointStatus: str
    EndpointName: str
    EndpointCreateTime: datetime
    Port: int
    Address: str
    VpcSecurityGroups: List[VpcSecurityGroupMembership]
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


class EndpointAccess(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    SubnetGroupName: Optional[str] = None
    EndpointStatus: Optional[str] = None
    EndpointName: Optional[str] = None
    EndpointCreateTime: Optional[datetime] = None
    Port: Optional[int] = None
    Address: Optional[str] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    VpcEndpoint: Optional[VpcEndpoint] = None


class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    VpcEndpoints: Optional[List[VpcEndpoint]] = None


class ServiceIntegrationsUnionOutput(BaseValidatorModel):
    LakeFormation: Optional[List[LakeFormationScopeUnion]] = None
    S3AccessGrants: Optional[List[S3AccessGrantsScopeUnion]] = None


class ServiceIntegrationsUnion(BaseValidatorModel):
    LakeFormation: Optional[List[LakeFormationScopeUnion]] = None
    S3AccessGrants: Optional[List[S3AccessGrantsScopeUnion]] = None


class ListRecommendationsResult(BaseValidatorModel):
    Recommendations: List[Recommendation]
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetReservedNodeExchangeOfferingsOutputMessage(BaseValidatorModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOffering]
    ResponseMetadata: ResponseMetadata


class ReservedNodeOfferingsMessage(BaseValidatorModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOffering]
    ResponseMetadata: ResponseMetadata


class AcceptReservedNodeExchangeOutputMessage(BaseValidatorModel):
    ExchangedReservedNode: ReservedNode
    ResponseMetadata: ResponseMetadata


class PurchaseReservedNodeOfferingResult(BaseValidatorModel):
    ReservedNode: ReservedNode
    ResponseMetadata: ResponseMetadata


class ReservedNodeConfigurationOption(BaseValidatorModel):
    SourceReservedNode: Optional[ReservedNode] = None
    TargetReservedNodeCount: Optional[int] = None
    TargetReservedNodeOffering: Optional[ReservedNodeOffering] = None


class ReservedNodesMessage(BaseValidatorModel):
    Marker: str
    ReservedNodes: List[ReservedNode]
    ResponseMetadata: ResponseMetadata


class CreateScheduledActionMessage(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionType
    Schedule: str
    IamRole: str
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Enable: Optional[bool] = None


class ModifyScheduledActionMessage(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: Optional[ScheduledActionType] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Enable: Optional[bool] = None


class ScheduledActionResponse(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionType
    Schedule: str
    IamRole: str
    ScheduledActionDescription: str
    State: ScheduledActionStateType
    NextInvocations: List[datetime]
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadata


class ScheduledAction(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetAction: Optional[ScheduledActionType] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    State: Optional[ScheduledActionStateType] = None
    NextInvocations: Optional[List[datetime]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class MaintenanceTrack(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    UpdateTargets: Optional[List[UpdateTarget]] = None


class OrderableClusterOptionsMessage(BaseValidatorModel):
    OrderableClusterOptions: List[OrderableClusterOption]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ClusterSubnetGroup(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None
    Tags: Optional[List[Tag]] = None
    SupportedClusterIpAddressTypes: Optional[List[str]] = None


class AuthorizeClusterSecurityGroupIngressResult(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroup
    ResponseMetadata: ResponseMetadata


class ClusterSecurityGroupMessage(BaseValidatorModel):
    Marker: str
    ClusterSecurityGroups: List[ClusterSecurityGroup]
    ResponseMetadata: ResponseMetadata


class CreateClusterSecurityGroupResult(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroup
    ResponseMetadata: ResponseMetadata


class RevokeClusterSecurityGroupIngressResult(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroup
    ResponseMetadata: ResponseMetadata


class EndpointAccessList(BaseValidatorModel):
    EndpointAccessList: List[EndpointAccess]
    Marker: str
    ResponseMetadata: ResponseMetadata


class Cluster(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NodeType: Optional[str] = None
    ClusterStatus: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ModifyStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[Endpoint] = None
    ClusterCreateTime: Optional[datetime] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ClusterSecurityGroups: Optional[List[ClusterSecurityGroupMembership]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    ClusterParameterGroups: Optional[List[ClusterParameterGroupStatus]] = None
    ClusterSubnetGroupName: Optional[str] = None
    VpcId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValues] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    Encrypted: Optional[bool] = None
    RestoreStatus: Optional[RestoreStatus] = None
    DataTransferProgress: Optional[DataTransferProgress] = None
    HsmStatus: Optional[HsmStatus] = None
    ClusterSnapshotCopyStatus: Optional[ClusterSnapshotCopyStatus] = None
    ClusterPublicKey: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNode]] = None
    ElasticIpStatus: Optional[ElasticIpStatus] = None
    ClusterRevisionNumber: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    IamRoles: Optional[List[ClusterIamRole]] = None
    PendingActions: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    DeferredMaintenanceWindows: Optional[List[DeferredMaintenanceWindow]] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[ScheduleStateType] = None
    ExpectedNextSnapshotScheduleTime: Optional[datetime] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[datetime] = None
    ResizeInfo: Optional[ResizeInfo] = None
    AvailabilityZoneRelocationStatus: Optional[str] = None
    ClusterNamespaceArn: Optional[str] = None
    TotalStorageCapacityInMegaBytes: Optional[int] = None
    AquaConfiguration: Optional[AquaConfiguration] = None
    DefaultIamRoleArn: Optional[str] = None
    ReservedNodeExchangeStatus: Optional[ReservedNodeExchangeStatus] = None
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[str] = None
    MultiAZSecondary: Optional[SecondaryClusterInfo] = None


class RedshiftIdcApplication(BaseValidatorModel):
    IdcInstanceArn: Optional[str] = None
    RedshiftIdcApplicationName: Optional[str] = None
    RedshiftIdcApplicationArn: Optional[str] = None
    IdentityNamespace: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcManagedApplicationArn: Optional[str] = None
    IdcOnboardStatus: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerOutput]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionOutput]] = None

ServiceIntegrationsUnionUnion = Union[ServiceIntegrationsUnion, ServiceIntegrationsUnionOutput]


class GetReservedNodeExchangeConfigurationOptionsOutputMessage(BaseValidatorModel):
    Marker: str
    ReservedNodeConfigurationOptionList: List[ReservedNodeConfigurationOption]
    ResponseMetadata: ResponseMetadata


class ScheduledActionsMessage(BaseValidatorModel):
    Marker: str
    ScheduledActions: List[ScheduledAction]
    ResponseMetadata: ResponseMetadata


class TrackListMessage(BaseValidatorModel):
    MaintenanceTracks: List[MaintenanceTrack]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ClusterSubnetGroupMessage(BaseValidatorModel):
    Marker: str
    ClusterSubnetGroups: List[ClusterSubnetGroup]
    ResponseMetadata: ResponseMetadata


class CreateClusterSubnetGroupResult(BaseValidatorModel):
    ClusterSubnetGroup: ClusterSubnetGroup
    ResponseMetadata: ResponseMetadata


class ModifyClusterSubnetGroupResult(BaseValidatorModel):
    ClusterSubnetGroup: ClusterSubnetGroup
    ResponseMetadata: ResponseMetadata


class ClustersMessage(BaseValidatorModel):
    Marker: str
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata


class CreateClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DeleteClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DisableSnapshotCopyResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class EnableSnapshotCopyResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class FailoverPrimaryComputeResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ModifyClusterDbRevisionResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ModifyClusterIamRolesResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ModifyClusterMaintenanceResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ModifyClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ModifySnapshotCopyRetentionPeriodResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class PauseClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class RebootClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ResizeClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class RestoreFromClusterSnapshotResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ResumeClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class RotateEncryptionKeyResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class CreateRedshiftIdcApplicationResult(BaseValidatorModel):
    RedshiftIdcApplication: RedshiftIdcApplication
    ResponseMetadata: ResponseMetadata


class DescribeRedshiftIdcApplicationsResult(BaseValidatorModel):
    RedshiftIdcApplications: List[RedshiftIdcApplication]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ModifyRedshiftIdcApplicationResult(BaseValidatorModel):
    RedshiftIdcApplication: RedshiftIdcApplication
    ResponseMetadata: ResponseMetadata


class CreateRedshiftIdcApplicationMessage(BaseValidatorModel):
    IdcInstanceArn: str
    RedshiftIdcApplicationName: str
    IdcDisplayName: str
    IamRoleArn: str
    IdentityNamespace: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerUnion]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionUnion]] = None


class ModifyRedshiftIdcApplicationMessage(BaseValidatorModel):
    RedshiftIdcApplicationArn: str
    IdentityNamespace: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerUnion]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionUnion]] = None