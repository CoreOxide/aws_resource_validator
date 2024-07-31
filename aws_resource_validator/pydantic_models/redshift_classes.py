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
from aws_resource_validator.pydantic_models.redshift_constants import *

class AcceptReservedNodeExchangeInputMessageRequestTypeDef(BaseModel):
    ReservedNodeId: str
    TargetReservedNodeOfferingId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AttributeValueTargetTypeDef(BaseModel):
    AttributeValue: Optional[str] = None

class AccountWithRestoreAccessTypeDef(BaseModel):
    AccountId: Optional[str] = None
    AccountAlias: Optional[str] = None

class AquaConfigurationTypeDef(BaseModel):
    AquaStatus: Optional[AquaStatusType] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None

class AssociateDataShareConsumerMessageRequestTypeDef(BaseModel):
    DataShareArn: str
    AssociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None
    AllowWrites: Optional[bool] = None

class CertificateAssociationTypeDef(BaseModel):
    CustomDomainName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None

class AuthenticationProfileTypeDef(BaseModel):
    AuthenticationProfileName: Optional[str] = None
    AuthenticationProfileContent: Optional[str] = None

class AuthorizeClusterSecurityGroupIngressMessageRequestTypeDef(BaseModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class AuthorizeDataShareMessageRequestTypeDef(BaseModel):
    DataShareArn: str
    ConsumerIdentifier: str
    AllowWrites: Optional[bool] = None

class AuthorizeEndpointAccessMessageRequestTypeDef(BaseModel):
    Account: str
    ClusterIdentifier: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None

class AuthorizeSnapshotAccessMessageRequestTypeDef(BaseModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None

class AuthorizedTokenIssuerExtraOutputTypeDef(BaseModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None

class AuthorizedTokenIssuerOutputTypeDef(BaseModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None

class AuthorizedTokenIssuerTypeDef(BaseModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[Sequence[str]] = None

class SupportedPlatformTypeDef(BaseModel):
    Name: Optional[str] = None

class DeleteClusterSnapshotMessageTypeDef(BaseModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None

class SnapshotErrorMessageTypeDef(BaseModel):
    SnapshotIdentifier: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None

class BatchModifyClusterSnapshotsMessageRequestTypeDef(BaseModel):
    SnapshotIdentifierList: Sequence[str]
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None

class CancelResizeMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class ClusterAssociatedToScheduleTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleAssociationState: Optional[ScheduleStateType] = None

class RevisionTargetTypeDef(BaseModel):
    DatabaseRevision: Optional[str] = None
    Description: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None

class ClusterIamRoleTypeDef(BaseModel):
    IamRoleArn: Optional[str] = None
    ApplyStatus: Optional[str] = None

class ClusterNodeTypeDef(BaseModel):
    NodeRole: Optional[str] = None
    PrivateIPAddress: Optional[str] = None
    PublicIPAddress: Optional[str] = None

class ParameterTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    ApplyType: Optional[ParameterApplyTypeType] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None

class ClusterParameterStatusTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ClusterSecurityGroupMembershipTypeDef(BaseModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class ClusterSnapshotCopyStatusTypeDef(BaseModel):
    DestinationRegion: Optional[str] = None
    RetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None

class DataTransferProgressTypeDef(BaseModel):
    Status: Optional[str] = None
    CurrentRateInMegaBytesPerSecond: Optional[float] = None
    TotalDataInMegaBytes: Optional[int] = None
    DataTransferredInMegaBytes: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None

class DeferredMaintenanceWindowTypeDef(BaseModel):
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[datetime] = None
    DeferMaintenanceEndTime: Optional[datetime] = None

class ElasticIpStatusTypeDef(BaseModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None

class HsmStatusTypeDef(BaseModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None

class PendingModifiedValuesTypeDef(BaseModel):
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

class ReservedNodeExchangeStatusTypeDef(BaseModel):
    ReservedNodeExchangeRequestId: Optional[str] = None
    Status: Optional[ReservedNodeExchangeStatusTypeType] = None
    RequestTime: Optional[datetime] = None
    SourceReservedNodeId: Optional[str] = None
    SourceReservedNodeType: Optional[str] = None
    SourceReservedNodeCount: Optional[int] = None
    TargetReservedNodeOfferingId: Optional[str] = None
    TargetReservedNodeType: Optional[str] = None
    TargetReservedNodeCount: Optional[int] = None

class ResizeInfoTypeDef(BaseModel):
    ResizeType: Optional[str] = None
    AllowCancelResize: Optional[bool] = None

class RestoreStatusTypeDef(BaseModel):
    Status: Optional[str] = None
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None

class VpcSecurityGroupMembershipTypeDef(BaseModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class ClusterVersionTypeDef(BaseModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None

class CopyClusterSnapshotMessageRequestTypeDef(BaseModel):
    SourceSnapshotIdentifier: str
    TargetSnapshotIdentifier: str
    SourceSnapshotClusterIdentifier: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None

class CreateAuthenticationProfileMessageRequestTypeDef(BaseModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str

class CreateCustomDomainAssociationMessageRequestTypeDef(BaseModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str

class CreateEndpointAccessMessageRequestTypeDef(BaseModel):
    EndpointName: str
    SubnetGroupName: str
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None

class DataShareAssociationTypeDef(BaseModel):
    ConsumerIdentifier: Optional[str] = None
    Status: Optional[DataShareStatusType] = None
    ConsumerRegion: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    StatusChangeDate: Optional[datetime] = None
    ProducerAllowedWrites: Optional[bool] = None
    ConsumerAcceptedWrites: Optional[bool] = None

class DeauthorizeDataShareMessageRequestTypeDef(BaseModel):
    DataShareArn: str
    ConsumerIdentifier: str

class DeleteAuthenticationProfileMessageRequestTypeDef(BaseModel):
    AuthenticationProfileName: str

class DeleteClusterMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    SkipFinalClusterSnapshot: Optional[bool] = None
    FinalClusterSnapshotIdentifier: Optional[str] = None
    FinalClusterSnapshotRetentionPeriod: Optional[int] = None

class DeleteClusterParameterGroupMessageRequestTypeDef(BaseModel):
    ParameterGroupName: str

class DeleteClusterSecurityGroupMessageRequestTypeDef(BaseModel):
    ClusterSecurityGroupName: str

class DeleteClusterSnapshotMessageRequestTypeDef(BaseModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None

class DeleteClusterSubnetGroupMessageRequestTypeDef(BaseModel):
    ClusterSubnetGroupName: str

class DeleteCustomDomainAssociationMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    CustomDomainName: str

class DeleteEndpointAccessMessageRequestTypeDef(BaseModel):
    EndpointName: str

class DeleteEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str

class DeleteHsmClientCertificateMessageRequestTypeDef(BaseModel):
    HsmClientCertificateIdentifier: str

class DeleteHsmConfigurationMessageRequestTypeDef(BaseModel):
    HsmConfigurationIdentifier: str

class DeleteRedshiftIdcApplicationMessageRequestTypeDef(BaseModel):
    RedshiftIdcApplicationArn: str

class DeleteResourcePolicyMessageRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteScheduledActionMessageRequestTypeDef(BaseModel):
    ScheduledActionName: str

class DeleteSnapshotCopyGrantMessageRequestTypeDef(BaseModel):
    SnapshotCopyGrantName: str

class DeleteSnapshotScheduleMessageRequestTypeDef(BaseModel):
    ScheduleIdentifier: str

class DeleteTagsMessageRequestTypeDef(BaseModel):
    ResourceName: str
    TagKeys: Sequence[str]

class DeleteUsageLimitMessageRequestTypeDef(BaseModel):
    UsageLimitId: str

class DescribeAccountAttributesMessageRequestTypeDef(BaseModel):
    AttributeNames: Optional[Sequence[str]] = None

class DescribeAuthenticationProfilesMessageRequestTypeDef(BaseModel):
    AuthenticationProfileName: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClusterDbRevisionsMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClusterParameterGroupsMessageRequestTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeClusterParametersMessageRequestTypeDef(BaseModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClusterSecurityGroupsMessageRequestTypeDef(BaseModel):
    ClusterSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class SnapshotSortingEntityTypeDef(BaseModel):
    Attribute: SnapshotAttributeToSortByType
    SortOrder: Optional[SortByOrderType] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeClusterSubnetGroupsMessageRequestTypeDef(BaseModel):
    ClusterSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeClusterTracksMessageRequestTypeDef(BaseModel):
    MaintenanceTrackName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClusterVersionsMessageRequestTypeDef(BaseModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClustersMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeCustomDomainAssociationsMessageRequestTypeDef(BaseModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDataSharesForConsumerMessageRequestTypeDef(BaseModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDataSharesForProducerMessageRequestTypeDef(BaseModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDataSharesMessageRequestTypeDef(BaseModel):
    DataShareArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDefaultClusterParametersMessageRequestTypeDef(BaseModel):
    ParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEndpointAccessMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEndpointAuthorizationMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventCategoriesMessageRequestTypeDef(BaseModel):
    SourceType: Optional[str] = None

class DescribeEventSubscriptionsMessageRequestTypeDef(BaseModel):
    SubscriptionName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeHsmClientCertificatesMessageRequestTypeDef(BaseModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeHsmConfigurationsMessageRequestTypeDef(BaseModel):
    HsmConfigurationIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeInboundIntegrationsMessageRequestTypeDef(BaseModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeLoggingStatusMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class NodeConfigurationOptionsFilterTypeDef(BaseModel):
    Name: Optional[NodeConfigurationOptionsFilterNameType] = None
    Operator: Optional[OperatorTypeType] = None
    Values: Optional[Sequence[str]] = None

class DescribeOrderableClusterOptionsMessageRequestTypeDef(BaseModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribePartnersInputMessageRequestTypeDef(BaseModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None

class PartnerIntegrationInfoTypeDef(BaseModel):
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None
    Status: Optional[PartnerIntegrationStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class DescribeRedshiftIdcApplicationsMessageRequestTypeDef(BaseModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedNodeExchangeStatusInputMessageRequestTypeDef(BaseModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedNodeOfferingsMessageRequestTypeDef(BaseModel):
    ReservedNodeOfferingId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedNodesMessageRequestTypeDef(BaseModel):
    ReservedNodeId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeResizeMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class ScheduledActionFilterTypeDef(BaseModel):
    Name: ScheduledActionFilterNameType
    Values: Sequence[str]

class DescribeSnapshotCopyGrantsMessageRequestTypeDef(BaseModel):
    SnapshotCopyGrantName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeSnapshotSchedulesMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeTableRestoreStatusMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeTagsMessageRequestTypeDef(BaseModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeUsageLimitsMessageRequestTypeDef(BaseModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DisableLoggingMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class DisableSnapshotCopyMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class DisassociateDataShareConsumerMessageRequestTypeDef(BaseModel):
    DataShareArn: str
    DisassociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None

class EnableLoggingMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    LogDestinationType: Optional[LogDestinationTypeType] = None
    LogExports: Optional[Sequence[str]] = None

class EnableSnapshotCopyMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    DestinationRegion: str
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None

class EndpointAuthorizationTypeDef(BaseModel):
    Grantor: Optional[str] = None
    Grantee: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    AuthorizeTime: Optional[datetime] = None
    ClusterStatus: Optional[str] = None
    Status: Optional[AuthorizationStatusType] = None
    AllowedAllVPCs: Optional[bool] = None
    AllowedVPCs: Optional[List[str]] = None
    EndpointCount: Optional[int] = None

class EventInfoMapTypeDef(BaseModel):
    EventId: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    EventDescription: Optional[str] = None
    Severity: Optional[str] = None

class EventTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Date: Optional[datetime] = None
    EventId: Optional[str] = None

class FailoverPrimaryComputeInputMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class GetClusterCredentialsMessageRequestTypeDef(BaseModel):
    DbUser: str
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    AutoCreate: Optional[bool] = None
    DbGroups: Optional[Sequence[str]] = None
    CustomDomainName: Optional[str] = None

class GetClusterCredentialsWithIAMMessageRequestTypeDef(BaseModel):
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    CustomDomainName: Optional[str] = None

class GetReservedNodeExchangeConfigurationOptionsInputMessageRequestTypeDef(BaseModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class GetReservedNodeExchangeOfferingsInputMessageRequestTypeDef(BaseModel):
    ReservedNodeId: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class GetResourcePolicyMessageRequestTypeDef(BaseModel):
    ResourceArn: str

class ResourcePolicyTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None

class IntegrationErrorTypeDef(BaseModel):
    ErrorCode: str
    ErrorMessage: Optional[str] = None

class LakeFormationQueryTypeDef(BaseModel):
    Authorization: ServiceAuthorizationType

class ListRecommendationsMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class ModifyAquaInputMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None

class ModifyAuthenticationProfileMessageRequestTypeDef(BaseModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str

class ModifyClusterDbRevisionMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    RevisionTarget: str

class ModifyClusterIamRolesMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    AddIamRoles: Optional[Sequence[str]] = None
    RemoveIamRoles: Optional[Sequence[str]] = None
    DefaultIamRoleArn: Optional[str] = None

class ModifyClusterMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    ClusterSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
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

class ModifyClusterSnapshotMessageRequestTypeDef(BaseModel):
    SnapshotIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None

class ModifyClusterSnapshotScheduleMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    ScheduleIdentifier: Optional[str] = None
    DisassociateSchedule: Optional[bool] = None

class ModifyClusterSubnetGroupMessageRequestTypeDef(BaseModel):
    ClusterSubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None

class ModifyCustomDomainAssociationMessageRequestTypeDef(BaseModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str

class ModifyEndpointAccessMessageRequestTypeDef(BaseModel):
    EndpointName: str
    VpcSecurityGroupIds: Optional[Sequence[str]] = None

class ModifyEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIds: Optional[Sequence[str]] = None
    EventCategories: Optional[Sequence[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None

class ModifySnapshotCopyRetentionPeriodMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    RetentionPeriod: int
    Manual: Optional[bool] = None

class ModifySnapshotScheduleMessageRequestTypeDef(BaseModel):
    ScheduleIdentifier: str
    ScheduleDefinitions: Sequence[str]

class ModifyUsageLimitMessageRequestTypeDef(BaseModel):
    UsageLimitId: str
    Amount: Optional[int] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None

class NetworkInterfaceTypeDef(BaseModel):
    NetworkInterfaceId: Optional[str] = None
    SubnetId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Ipv6Address: Optional[str] = None

class NodeConfigurationOptionTypeDef(BaseModel):
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    EstimatedDiskUtilizationPercent: Optional[float] = None
    Mode: Optional[ModeType] = None

class PartnerIntegrationInputMessageRequestTypeDef(BaseModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str

class PauseClusterMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class PauseClusterMessageTypeDef(BaseModel):
    ClusterIdentifier: str

class PurchaseReservedNodeOfferingMessageRequestTypeDef(BaseModel):
    ReservedNodeOfferingId: str
    NodeCount: Optional[int] = None

class PutResourcePolicyMessageRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str

class RebootClusterMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class RecommendedActionTypeDef(BaseModel):
    Text: Optional[str] = None
    Database: Optional[str] = None
    Command: Optional[str] = None
    Type: Optional[RecommendedActionTypeType] = None

class ReferenceLinkTypeDef(BaseModel):
    Text: Optional[str] = None
    Link: Optional[str] = None

class RecurringChargeTypeDef(BaseModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class RejectDataShareMessageRequestTypeDef(BaseModel):
    DataShareArn: str

class ResizeClusterMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None

class ResizeClusterMessageTypeDef(BaseModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None

class RestoreFromClusterSnapshotMessageRequestTypeDef(BaseModel):
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
    ClusterSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    KmsKeyId: Optional[str] = None
    NodeType: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[Sequence[str]] = None
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

class RestoreTableFromClusterSnapshotMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    SnapshotIdentifier: str
    SourceDatabaseName: str
    SourceTableName: str
    NewTableName: str
    SourceSchemaName: Optional[str] = None
    TargetDatabaseName: Optional[str] = None
    TargetSchemaName: Optional[str] = None
    EnableCaseSensitiveIdentifier: Optional[bool] = None

class TableRestoreStatusTypeDef(BaseModel):
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

class ResumeClusterMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class ResumeClusterMessageTypeDef(BaseModel):
    ClusterIdentifier: str

class RevokeClusterSecurityGroupIngressMessageRequestTypeDef(BaseModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class RevokeEndpointAccessMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None
    Force: Optional[bool] = None

class RevokeSnapshotAccessMessageRequestTypeDef(BaseModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None

class RotateEncryptionKeyMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str

class SupportedOperationTypeDef(BaseModel):
    OperationName: Optional[str] = None

class UpdatePartnerStatusInputMessageRequestTypeDef(BaseModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str
    Status: PartnerIntegrationStatusType
    StatusMessage: Optional[str] = None

class ClusterCredentialsTypeDef(BaseModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterExtendedCredentialsTypeDef(BaseModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    NextRefreshTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterParameterGroupNameMessageTypeDef(BaseModel):
    ParameterGroupName: str
    ParameterGroupStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAuthenticationProfileResultTypeDef(BaseModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomDomainAssociationResultTypeDef(BaseModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerStorageMessageTypeDef(BaseModel):
    TotalBackupSizeInMegaBytes: float
    TotalProvisionedStorageInMegaBytes: float
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAuthenticationProfileResultTypeDef(BaseModel):
    AuthenticationProfileName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointAuthorizationResponseTypeDef(BaseModel):
    Grantor: str
    Grantee: str
    ClusterIdentifier: str
    AuthorizeTime: datetime
    ClusterStatus: str
    Status: AuthorizationStatusType
    AllowedAllVPCs: bool
    AllowedVPCs: List[str]
    EndpointCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingStatusTypeDef(BaseModel):
    LoggingEnabled: bool
    BucketName: str
    S3KeyPrefix: str
    LastSuccessfulDeliveryTime: datetime
    LastFailureTime: datetime
    LastFailureMessage: str
    LogDestinationType: LogDestinationTypeType
    LogExports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyAuthenticationProfileResultTypeDef(BaseModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCustomDomainAssociationResultTypeDef(BaseModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class PartnerIntegrationOutputMessageTypeDef(BaseModel):
    DatabaseName: str
    PartnerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResizeProgressMessageTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class AccountAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[AttributeValueTargetTypeDef]] = None

class ModifyAquaOutputMessageTypeDef(BaseModel):
    AquaConfiguration: AquaConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociationTypeDef(BaseModel):
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    CertificateAssociations: Optional[List[CertificateAssociationTypeDef]] = None

class DescribeAuthenticationProfilesResultTypeDef(BaseModel):
    AuthenticationProfiles: List[AuthenticationProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None
    SupportedPlatforms: Optional[List[SupportedPlatformTypeDef]] = None

class BatchDeleteClusterSnapshotsRequestRequestTypeDef(BaseModel):
    Identifiers: Sequence[DeleteClusterSnapshotMessageTypeDef]

class BatchDeleteClusterSnapshotsResultTypeDef(BaseModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchModifyClusterSnapshotsOutputMessageTypeDef(BaseModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterDbRevisionTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    CurrentDatabaseRevision: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None
    RevisionTargets: Optional[List[RevisionTargetTypeDef]] = None

class SecondaryClusterInfoTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNodeTypeDef]] = None

class ClusterParameterGroupDetailsTypeDef(BaseModel):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DefaultClusterParametersTypeDef(BaseModel):
    ParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None

class ModifyClusterParameterGroupMessageRequestTypeDef(BaseModel):
    ParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ResetClusterParameterGroupMessageRequestTypeDef(BaseModel):
    ParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class ClusterParameterGroupStatusTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ClusterParameterStatusList: Optional[List[ClusterParameterStatusTypeDef]] = None

class ClusterParameterGroupTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateClusterMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    NodeType: str
    MasterUsername: str
    DBName: Optional[str] = None
    ClusterType: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    ClusterSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[Sequence[str]] = None
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

class CreateClusterParameterGroupMessageRequestTypeDef(BaseModel):
    ParameterGroupName: str
    ParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterSecurityGroupMessageRequestTypeDef(BaseModel):
    ClusterSecurityGroupName: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterSnapshotMessageRequestTypeDef(BaseModel):
    SnapshotIdentifier: str
    ClusterIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterSubnetGroupMessageRequestTypeDef(BaseModel):
    ClusterSubnetGroupName: str
    Description: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    SourceIds: Optional[Sequence[str]] = None
    EventCategories: Optional[Sequence[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateHsmClientCertificateMessageRequestTypeDef(BaseModel):
    HsmClientCertificateIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateHsmConfigurationMessageRequestTypeDef(BaseModel):
    HsmConfigurationIdentifier: str
    Description: str
    HsmIpAddress: str
    HsmPartitionName: str
    HsmPartitionPassword: str
    HsmServerPublicCertificate: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotCopyGrantMessageRequestTypeDef(BaseModel):
    SnapshotCopyGrantName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotScheduleMessageRequestTypeDef(BaseModel):
    ScheduleDefinitions: Optional[Sequence[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None
    NextInvocations: Optional[int] = None

class CreateTagsMessageRequestTypeDef(BaseModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CreateUsageLimitMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class EC2SecurityGroupTypeDef(BaseModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class EventSubscriptionTypeDef(BaseModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class HsmClientCertificateTypeDef(BaseModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmClientCertificatePublicKey: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class HsmConfigurationTypeDef(BaseModel):
    HsmConfigurationIdentifier: Optional[str] = None
    Description: Optional[str] = None
    HsmIpAddress: Optional[str] = None
    HsmPartitionName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class IPRangeTypeDef(BaseModel):
    Status: Optional[str] = None
    CIDRIP: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class SnapshotCopyGrantTypeDef(BaseModel):
    SnapshotCopyGrantName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class SnapshotScheduleResponseTypeDef(BaseModel):
    ScheduleDefinitions: List[str]
    ScheduleIdentifier: str
    ScheduleDescription: str
    Tags: List[TagTypeDef]
    NextInvocations: List[datetime]
    AssociatedClusterCount: int
    AssociatedClusters: List[ClusterAssociatedToScheduleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotScheduleTypeDef(BaseModel):
    ScheduleDefinitions: Optional[List[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    NextInvocations: Optional[List[datetime]] = None
    AssociatedClusterCount: Optional[int] = None
    AssociatedClusters: Optional[List[ClusterAssociatedToScheduleTypeDef]] = None

class SnapshotTypeDef(BaseModel):
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
    AccountsWithRestoreAccess: Optional[List[AccountWithRestoreAccessTypeDef]] = None
    OwnerAccount: Optional[str] = None
    TotalBackupSizeInMegaBytes: Optional[float] = None
    ActualIncrementalBackupSizeInMegaBytes: Optional[float] = None
    BackupProgressInMegaBytes: Optional[float] = None
    CurrentBackupRateInMegaBytesPerSecond: Optional[float] = None
    EstimatedSecondsToCompletion: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    SourceRegion: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    RestorableNodeTypes: Optional[List[str]] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRemainingDays: Optional[int] = None
    SnapshotRetentionStartTime: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    SnapshotArn: Optional[str] = None

class TaggedResourceTypeDef(BaseModel):
    Tag: Optional[TagTypeDef] = None
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None

class UsageLimitResponseTypeDef(BaseModel):
    UsageLimitId: str
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: UsageLimitPeriodType
    BreachAction: UsageLimitBreachActionType
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsageLimitTypeDef(BaseModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    LimitType: Optional[UsageLimitLimitTypeType] = None
    Amount: Optional[int] = None
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeReservedNodeExchangeStatusOutputMessageTypeDef(BaseModel):
    ReservedNodeExchangeStatusDetails: List[ReservedNodeExchangeStatusTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterVersionsMessageTypeDef(BaseModel):
    Marker: str
    ClusterVersions: List[ClusterVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsMessageRequestTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class ModifyClusterMaintenanceMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: str
    DeferMaintenance: Optional[bool] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[TimestampTypeDef] = None
    DeferMaintenanceEndTime: Optional[TimestampTypeDef] = None
    DeferMaintenanceDuration: Optional[int] = None

class DataShareResponseTypeDef(BaseModel):
    DataShareArn: str
    ProducerArn: str
    AllowPubliclyAccessibleConsumers: bool
    DataShareAssociations: List[DataShareAssociationTypeDef]
    ManagedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataShareTypeDef(BaseModel):
    DataShareArn: Optional[str] = None
    ProducerArn: Optional[str] = None
    AllowPubliclyAccessibleConsumers: Optional[bool] = None
    DataShareAssociations: Optional[List[DataShareAssociationTypeDef]] = None
    ManagedBy: Optional[str] = None

class DescribeClusterDbRevisionsMessageDescribeClusterDbRevisionsPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterParameterGroupsMessageDescribeClusterParameterGroupsPaginateTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterParametersMessageDescribeClusterParametersPaginateTypeDef(BaseModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSecurityGroupsMessageDescribeClusterSecurityGroupsPaginateTypeDef(BaseModel):
    ClusterSecurityGroupName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSubnetGroupsMessageDescribeClusterSubnetGroupsPaginateTypeDef(BaseModel):
    ClusterSubnetGroupName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterTracksMessageDescribeClusterTracksPaginateTypeDef(BaseModel):
    MaintenanceTrackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterVersionsMessageDescribeClusterVersionsPaginateTypeDef(BaseModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClustersMessageDescribeClustersPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCustomDomainAssociationsMessageDescribeCustomDomainAssociationsPaginateTypeDef(BaseModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDataSharesForConsumerMessageDescribeDataSharesForConsumerPaginateTypeDef(BaseModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDataSharesForProducerMessageDescribeDataSharesForProducerPaginateTypeDef(BaseModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDataSharesMessageDescribeDataSharesPaginateTypeDef(BaseModel):
    DataShareArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDefaultClusterParametersMessageDescribeDefaultClusterParametersPaginateTypeDef(BaseModel):
    ParameterGroupFamily: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEndpointAccessMessageDescribeEndpointAccessPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEndpointAuthorizationMessageDescribeEndpointAuthorizationPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef(BaseModel):
    SubscriptionName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHsmClientCertificatesMessageDescribeHsmClientCertificatesPaginateTypeDef(BaseModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHsmConfigurationsMessageDescribeHsmConfigurationsPaginateTypeDef(BaseModel):
    HsmConfigurationIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInboundIntegrationsMessageDescribeInboundIntegrationsPaginateTypeDef(BaseModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrderableClusterOptionsMessageDescribeOrderableClusterOptionsPaginateTypeDef(BaseModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRedshiftIdcApplicationsMessageDescribeRedshiftIdcApplicationsPaginateTypeDef(BaseModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodeExchangeStatusInputMessageDescribeReservedNodeExchangeStatusPaginateTypeDef(BaseModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodeOfferingsMessageDescribeReservedNodeOfferingsPaginateTypeDef(BaseModel):
    ReservedNodeOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodesMessageDescribeReservedNodesPaginateTypeDef(BaseModel):
    ReservedNodeId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotCopyGrantsMessageDescribeSnapshotCopyGrantsPaginateTypeDef(BaseModel):
    SnapshotCopyGrantName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotSchedulesMessageDescribeSnapshotSchedulesPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTableRestoreStatusMessageDescribeTableRestoreStatusPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsMessageDescribeTagsPaginateTypeDef(BaseModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsageLimitsMessageDescribeUsageLimitsPaginateTypeDef(BaseModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReservedNodeExchangeConfigurationOptionsInputMessageGetReservedNodeExchangeConfigurationOptionsPaginateTypeDef(BaseModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReservedNodeExchangeOfferingsInputMessageGetReservedNodeExchangeOfferingsPaginateTypeDef(BaseModel):
    ReservedNodeId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationsMessageListRecommendationsPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSnapshotsMessageDescribeClusterSnapshotsPaginateTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[Sequence[SnapshotSortingEntityTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSnapshotsMessageRequestTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[Sequence[SnapshotSortingEntityTypeDef]] = None

class DescribeClusterSnapshotsMessageSnapshotAvailableWaitTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[Sequence[SnapshotSortingEntityTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClustersMessageClusterAvailableWaitTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClustersMessageClusterDeletedWaitTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClustersMessageClusterRestoredWaitTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNodeConfigurationOptionsMessageDescribeNodeConfigurationOptionsPaginateTypeDef(BaseModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[Sequence[NodeConfigurationOptionsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNodeConfigurationOptionsMessageRequestTypeDef(BaseModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[Sequence[NodeConfigurationOptionsFilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribePartnersOutputMessageTypeDef(BaseModel):
    PartnerIntegrationInfoList: List[PartnerIntegrationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScheduledActionsMessageDescribeScheduledActionsPaginateTypeDef(BaseModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Active: Optional[bool] = None
    Filters: Optional[Sequence[ScheduledActionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledActionsMessageRequestTypeDef(BaseModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Active: Optional[bool] = None
    Filters: Optional[Sequence[ScheduledActionFilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class EndpointAuthorizationListTypeDef(BaseModel):
    EndpointAuthorizationList: List[EndpointAuthorizationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMapTypeDef(BaseModel):
    SourceType: Optional[str] = None
    Events: Optional[List[EventInfoMapTypeDef]] = None

class EventsMessageTypeDef(BaseModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResultTypeDef(BaseModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResultTypeDef(BaseModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InboundIntegrationTypeDef(BaseModel):
    IntegrationArn: Optional[str] = None
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    Status: Optional[ZeroETLIntegrationStatusType] = None
    Errors: Optional[List[IntegrationErrorTypeDef]] = None
    CreateTime: Optional[datetime] = None

class LakeFormationScopeUnionTypeDef(BaseModel):
    LakeFormationQuery: Optional[LakeFormationQueryTypeDef] = None

class VpcEndpointTypeDef(BaseModel):
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    NetworkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None

class NodeConfigurationOptionsMessageTypeDef(BaseModel):
    NodeConfigurationOptionList: List[NodeConfigurationOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationTypeDef(BaseModel):
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
    RecommendedActions: Optional[List[RecommendedActionTypeDef]] = None
    ReferenceLinks: Optional[List[ReferenceLinkTypeDef]] = None

class ReservedNodeOfferingTypeDef(BaseModel):
    ReservedNodeOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None

class ReservedNodeTypeDef(BaseModel):
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
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None

class RestoreTableFromClusterSnapshotResultTypeDef(BaseModel):
    TableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TableRestoreStatusMessageTypeDef(BaseModel):
    TableRestoreStatusDetails: List[TableRestoreStatusTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionTypeTypeDef(BaseModel):
    ResizeCluster: Optional[ResizeClusterMessageTypeDef] = None
    PauseCluster: Optional[PauseClusterMessageTypeDef] = None
    ResumeCluster: Optional[ResumeClusterMessageTypeDef] = None

class UpdateTargetTypeDef(BaseModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    SupportedOperations: Optional[List[SupportedOperationTypeDef]] = None

class AccountAttributeListTypeDef(BaseModel):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomDomainAssociationsMessageTypeDef(BaseModel):
    Marker: str
    Associations: List[AssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableClusterOptionTypeDef(BaseModel):
    ClusterVersion: Optional[str] = None
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None

class SubnetTypeDef(BaseModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None

class ClusterDbRevisionsMessageTypeDef(BaseModel):
    Marker: str
    ClusterDbRevisions: List[ClusterDbRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDefaultClusterParametersResultTypeDef(BaseModel):
    DefaultClusterParameters: DefaultClusterParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterParameterGroupsMessageTypeDef(BaseModel):
    Marker: str
    ParameterGroups: List[ClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterParameterGroupResultTypeDef(BaseModel):
    ClusterParameterGroup: ClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(BaseModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmClientCertificateResultTypeDef(BaseModel):
    HsmClientCertificate: HsmClientCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HsmClientCertificateMessageTypeDef(BaseModel):
    Marker: str
    HsmClientCertificates: List[HsmClientCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmConfigurationResultTypeDef(BaseModel):
    HsmConfiguration: HsmConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HsmConfigurationMessageTypeDef(BaseModel):
    Marker: str
    HsmConfigurations: List[HsmConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSecurityGroupTypeDef(BaseModel):
    ClusterSecurityGroupName: Optional[str] = None
    Description: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroupTypeDef]] = None
    IPRanges: Optional[List[IPRangeTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateSnapshotCopyGrantResultTypeDef(BaseModel):
    SnapshotCopyGrant: SnapshotCopyGrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotCopyGrantMessageTypeDef(BaseModel):
    Marker: str
    SnapshotCopyGrants: List[SnapshotCopyGrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotSchedulesOutputMessageTypeDef(BaseModel):
    SnapshotSchedules: List[SnapshotScheduleTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeSnapshotAccessResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyClusterSnapshotResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSnapshotResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterSnapshotResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterSnapshotResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeSnapshotAccessResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotMessageTypeDef(BaseModel):
    Marker: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaggedResourceListMessageTypeDef(BaseModel):
    TaggedResources: List[TaggedResourceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UsageLimitListTypeDef(BaseModel):
    UsageLimits: List[UsageLimitTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesForConsumerResultTypeDef(BaseModel):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesForProducerResultTypeDef(BaseModel):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesResultTypeDef(BaseModel):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMessageTypeDef(BaseModel):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InboundIntegrationsMessageTypeDef(BaseModel):
    Marker: str
    InboundIntegrations: List[InboundIntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceIntegrationsUnionExtraOutputTypeDef(BaseModel):
    LakeFormation: Optional[List[LakeFormationScopeUnionTypeDef]] = None

class ServiceIntegrationsUnionOutputTypeDef(BaseModel):
    LakeFormation: Optional[List[LakeFormationScopeUnionTypeDef]] = None

class ServiceIntegrationsUnionTypeDef(BaseModel):
    LakeFormation: Optional[Sequence[LakeFormationScopeUnionTypeDef]] = None

class EndpointAccessResponseTypeDef(BaseModel):
    ClusterIdentifier: str
    ResourceOwner: str
    SubnetGroupName: str
    EndpointStatus: str
    EndpointName: str
    EndpointCreateTime: datetime
    Port: int
    Address: str
    VpcSecurityGroups: List[VpcSecurityGroupMembershipTypeDef]
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointAccessTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    SubnetGroupName: Optional[str] = None
    EndpointStatus: Optional[str] = None
    EndpointName: Optional[str] = None
    EndpointCreateTime: Optional[datetime] = None
    Port: Optional[int] = None
    Address: Optional[str] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    VpcEndpoint: Optional[VpcEndpointTypeDef] = None

class EndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    VpcEndpoints: Optional[List[VpcEndpointTypeDef]] = None

class ListRecommendationsResultTypeDef(BaseModel):
    Recommendations: List[RecommendationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReservedNodeExchangeOfferingsOutputMessageTypeDef(BaseModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedNodeOfferingsMessageTypeDef(BaseModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptReservedNodeExchangeOutputMessageTypeDef(BaseModel):
    ExchangedReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedNodeOfferingResultTypeDef(BaseModel):
    ReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedNodeConfigurationOptionTypeDef(BaseModel):
    SourceReservedNode: Optional[ReservedNodeTypeDef] = None
    TargetReservedNodeCount: Optional[int] = None
    TargetReservedNodeOffering: Optional[ReservedNodeOfferingTypeDef] = None

class ReservedNodesMessageTypeDef(BaseModel):
    Marker: str
    ReservedNodes: List[ReservedNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledActionMessageRequestTypeDef(BaseModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionTypeTypeDef
    Schedule: str
    IamRole: str
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Enable: Optional[bool] = None

class ModifyScheduledActionMessageRequestTypeDef(BaseModel):
    ScheduledActionName: str
    TargetAction: Optional[ScheduledActionTypeTypeDef] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Enable: Optional[bool] = None

class ScheduledActionResponseTypeDef(BaseModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionTypeTypeDef
    Schedule: str
    IamRole: str
    ScheduledActionDescription: str
    State: ScheduledActionStateType
    NextInvocations: List[datetime]
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionTypeDef(BaseModel):
    ScheduledActionName: Optional[str] = None
    TargetAction: Optional[ScheduledActionTypeTypeDef] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    State: Optional[ScheduledActionStateType] = None
    NextInvocations: Optional[List[datetime]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class MaintenanceTrackTypeDef(BaseModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    UpdateTargets: Optional[List[UpdateTargetTypeDef]] = None

class OrderableClusterOptionsMessageTypeDef(BaseModel):
    OrderableClusterOptions: List[OrderableClusterOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSubnetGroupTypeDef(BaseModel):
    ClusterSubnetGroupName: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    SupportedClusterIpAddressTypes: Optional[List[str]] = None

class AuthorizeClusterSecurityGroupIngressResultTypeDef(BaseModel):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSecurityGroupMessageTypeDef(BaseModel):
    Marker: str
    ClusterSecurityGroups: List[ClusterSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSecurityGroupResultTypeDef(BaseModel):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeClusterSecurityGroupIngressResultTypeDef(BaseModel):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RedshiftIdcApplicationTypeDef(BaseModel):
    IdcInstanceArn: Optional[str] = None
    RedshiftIdcApplicationName: Optional[str] = None
    RedshiftIdcApplicationArn: Optional[str] = None
    IdentityNamespace: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcManagedApplicationArn: Optional[str] = None
    IdcOnboardStatus: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerOutputTypeDef]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionOutputTypeDef]] = None

class EndpointAccessListTypeDef(BaseModel):
    EndpointAccessList: List[EndpointAccessTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    NodeType: Optional[str] = None
    ClusterStatus: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ModifyStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[EndpointTypeDef] = None
    ClusterCreateTime: Optional[datetime] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ClusterSecurityGroups: Optional[List[ClusterSecurityGroupMembershipTypeDef]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    ClusterParameterGroups: Optional[List[ClusterParameterGroupStatusTypeDef]] = None
    ClusterSubnetGroupName: Optional[str] = None
    VpcId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValuesTypeDef] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    Encrypted: Optional[bool] = None
    RestoreStatus: Optional[RestoreStatusTypeDef] = None
    DataTransferProgress: Optional[DataTransferProgressTypeDef] = None
    HsmStatus: Optional[HsmStatusTypeDef] = None
    ClusterSnapshotCopyStatus: Optional[ClusterSnapshotCopyStatusTypeDef] = None
    ClusterPublicKey: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNodeTypeDef]] = None
    ElasticIpStatus: Optional[ElasticIpStatusTypeDef] = None
    ClusterRevisionNumber: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    IamRoles: Optional[List[ClusterIamRoleTypeDef]] = None
    PendingActions: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    DeferredMaintenanceWindows: Optional[List[DeferredMaintenanceWindowTypeDef]] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[ScheduleStateType] = None
    ExpectedNextSnapshotScheduleTime: Optional[datetime] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[datetime] = None
    ResizeInfo: Optional[ResizeInfoTypeDef] = None
    AvailabilityZoneRelocationStatus: Optional[str] = None
    ClusterNamespaceArn: Optional[str] = None
    TotalStorageCapacityInMegaBytes: Optional[int] = None
    AquaConfiguration: Optional[AquaConfigurationTypeDef] = None
    DefaultIamRoleArn: Optional[str] = None
    ReservedNodeExchangeStatus: Optional[ReservedNodeExchangeStatusTypeDef] = None
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[str] = None
    MultiAZSecondary: Optional[SecondaryClusterInfoTypeDef] = None

class GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef(BaseModel):
    Marker: str
    ReservedNodeConfigurationOptionList: List[ReservedNodeConfigurationOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionsMessageTypeDef(BaseModel):
    Marker: str
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrackListMessageTypeDef(BaseModel):
    MaintenanceTracks: List[MaintenanceTrackTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSubnetGroupMessageTypeDef(BaseModel):
    Marker: str
    ClusterSubnetGroups: List[ClusterSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSubnetGroupResultTypeDef(BaseModel):
    ClusterSubnetGroup: ClusterSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterSubnetGroupResultTypeDef(BaseModel):
    ClusterSubnetGroup: ClusterSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRedshiftIdcApplicationResultTypeDef(BaseModel):
    RedshiftIdcApplication: RedshiftIdcApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRedshiftIdcApplicationsResultTypeDef(BaseModel):
    RedshiftIdcApplications: List[RedshiftIdcApplicationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyRedshiftIdcApplicationResultTypeDef(BaseModel):
    RedshiftIdcApplication: RedshiftIdcApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRedshiftIdcApplicationMessageRequestTypeDef(BaseModel):
    IdcInstanceArn: str
    RedshiftIdcApplicationName: str
    IdcDisplayName: str
    IamRoleArn: str
    IdentityNamespace: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[Sequence[AuthorizedTokenIssuerUnionTypeDef]] = None
    ServiceIntegrations: Optional[Sequence[ServiceIntegrationsUnionUnionTypeDef]] = None

class ModifyRedshiftIdcApplicationMessageRequestTypeDef(BaseModel):
    RedshiftIdcApplicationArn: str
    IdentityNamespace: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[Sequence[AuthorizedTokenIssuerUnionTypeDef]] = None
    ServiceIntegrations: Optional[Sequence[ServiceIntegrationsUnionUnionTypeDef]] = None

class ClustersMessageTypeDef(BaseModel):
    Marker: str
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisableSnapshotCopyResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSnapshotCopyResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverPrimaryComputeResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterDbRevisionResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterIamRolesResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterMaintenanceResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySnapshotCopyRetentionPeriodResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PauseClusterResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootClusterResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResizeClusterResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreFromClusterSnapshotResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeClusterResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RotateEncryptionKeyResultTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

