from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.securityhub.securityhub_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptAdministratorInvitationRequest(BaseValidatorModel):
    AdministratorId: str
    InvitationId: str


class AcceptInvitationRequest(BaseValidatorModel):
    MasterId: str
    InvitationId: str


class AccountDetails(BaseValidatorModel):
    AccountId: str
    Email: Optional[str] = None


class ActionLocalIpDetails(BaseValidatorModel):
    IpAddressV4: Optional[str] = None


class ActionLocalPortDetails(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class DnsRequestAction(BaseValidatorModel):
    Domain: Optional[str] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None


class City(BaseValidatorModel):
    CityName: Optional[str] = None


class Country(BaseValidatorModel):
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None


class GeoLocation(BaseValidatorModel):
    Lon: Optional[float] = None
    Lat: Optional[float] = None


class IpOrganizationDetails(BaseValidatorModel):
    Asn: Optional[int] = None
    AsnOrg: Optional[str] = None
    Isp: Optional[str] = None
    Org: Optional[str] = None


class ActionRemotePortDetails(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class ActionTarget(BaseValidatorModel):
    ActionTargetArn: str
    Name: str
    Description: str


class ActorSession(BaseValidatorModel):
    Uid: Optional[str] = None
    MfaStatus: Optional[ActorSessionMfaStatusType] = None
    CreatedTime: Optional[int] = None
    Issuer: Optional[str] = None


class UserAccount(BaseValidatorModel):
    Uid: Optional[str] = None
    Name: Optional[str] = None


class Adjustment(BaseValidatorModel):
    Metric: Optional[str] = None
    Reason: Optional[str] = None


class AdminAccount(BaseValidatorModel):
    AccountId: Optional[str] = None
    Status: Optional[AdminStatusType] = None


class AssociatedStandard(BaseValidatorModel):
    StandardsId: Optional[str] = None


class AssociationFilters(BaseValidatorModel):
    ConfigurationPolicyId: Optional[str] = None
    AssociationType: Optional[AssociationTypeType] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None


class AssociationStateDetails(BaseValidatorModel):
    State: Optional[str] = None
    StatusMessage: Optional[str] = None


class NoteUpdate(BaseValidatorModel):
    Text: str
    UpdatedBy: str


class RelatedFinding(BaseValidatorModel):
    ProductArn: str
    Id: str


class SeverityUpdate(BaseValidatorModel):
    Normalized: Optional[int] = None
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None


class WorkflowUpdate(BaseValidatorModel):
    Status: Optional[WorkflowStatusType] = None


class MapFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparison: Optional[MapFilterComparisonType] = None


class NumberFilter(BaseValidatorModel):
    Gte: Optional[float] = None
    Lte: Optional[float] = None
    Eq: Optional[float] = None
    Gt: Optional[float] = None
    Lt: Optional[float] = None


class StringFilter(BaseValidatorModel):
    Value: Optional[str] = None
    Comparison: Optional[StringFilterComparisonType] = None


class AutomationRulesMetadata(BaseValidatorModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None


class AvailabilityZone(BaseValidatorModel):
    ZoneName: Optional[str] = None
    SubnetId: Optional[str] = None


class AwsAmazonMqBrokerEncryptionOptionsDetails(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    UseAwsOwnedKey: Optional[bool] = None


class AwsAmazonMqBrokerLdapServerMetadataDetailsOutput(BaseValidatorModel):
    Hosts: Optional[List[str]] = None
    RoleBase: Optional[str] = None
    RoleName: Optional[str] = None
    RoleSearchMatching: Optional[str] = None
    RoleSearchSubtree: Optional[bool] = None
    ServiceAccountUsername: Optional[str] = None
    UserBase: Optional[str] = None
    UserRoleName: Optional[str] = None
    UserSearchMatching: Optional[str] = None
    UserSearchSubtree: Optional[bool] = None


class AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails(BaseValidatorModel):
    DayOfWeek: Optional[str] = None
    TimeOfDay: Optional[str] = None
    TimeZone: Optional[str] = None


class AwsAmazonMqBrokerUsersDetails(BaseValidatorModel):
    PendingChange: Optional[str] = None
    Username: Optional[str] = None


class AwsAmazonMqBrokerLdapServerMetadataDetails(BaseValidatorModel):
    Hosts: Optional[List[str]] = None
    RoleBase: Optional[str] = None
    RoleName: Optional[str] = None
    RoleSearchMatching: Optional[str] = None
    RoleSearchSubtree: Optional[bool] = None
    ServiceAccountUsername: Optional[str] = None
    UserBase: Optional[str] = None
    UserRoleName: Optional[str] = None
    UserSearchMatching: Optional[str] = None
    UserSearchSubtree: Optional[bool] = None


class AwsAmazonMqBrokerLogsPendingDetails(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None


class AwsApiCallActionDomainDetails(BaseValidatorModel):
    Domain: Optional[str] = None


class AwsApiGatewayAccessLogSettings(BaseValidatorModel):
    Format: Optional[str] = None
    DestinationArn: Optional[str] = None


class AwsApiGatewayCanarySettingsOutput(BaseValidatorModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Dict[str, str]] = None
    UseStageCache: Optional[bool] = None


class AwsApiGatewayCanarySettings(BaseValidatorModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Dict[str, str]] = None
    UseStageCache: Optional[bool] = None


class AwsApiGatewayEndpointConfigurationOutput(BaseValidatorModel):
    Types: Optional[List[str]] = None


class AwsApiGatewayEndpointConfiguration(BaseValidatorModel):
    Types: Optional[List[str]] = None


class AwsApiGatewayMethodSettings(BaseValidatorModel):
    MetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[str] = None
    DataTraceEnabled: Optional[bool] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None
    CachingEnabled: Optional[bool] = None
    CacheTtlInSeconds: Optional[int] = None
    CacheDataEncrypted: Optional[bool] = None
    RequireAuthorizationForCacheControl: Optional[bool] = None
    UnauthorizedCacheControlHeaderStrategy: Optional[str] = None
    HttpMethod: Optional[str] = None
    ResourcePath: Optional[str] = None


class AwsCorsConfigurationOutput(BaseValidatorModel):
    AllowOrigins: Optional[List[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[List[str]] = None
    AllowHeaders: Optional[List[str]] = None


class AwsApiGatewayV2RouteSettings(BaseValidatorModel):
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[str] = None
    DataTraceEnabled: Optional[bool] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None


class AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails(BaseValidatorModel):
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerUri: Optional[str] = None
    IdentityValidationExpression: Optional[str] = None


class AwsAppSyncGraphQlApiOpenIdConnectConfigDetails(BaseValidatorModel):
    AuthTtL: Optional[int] = None
    ClientId: Optional[str] = None
    IatTtL: Optional[int] = None
    Issuer: Optional[str] = None


class AwsAppSyncGraphQlApiUserPoolConfigDetails(BaseValidatorModel):
    AppIdClientRegex: Optional[str] = None
    AwsRegion: Optional[str] = None
    DefaultAction: Optional[str] = None
    UserPoolId: Optional[str] = None


class AwsAppSyncGraphQlApiLogConfigDetails(BaseValidatorModel):
    CloudWatchLogsRoleArn: Optional[str] = None
    ExcludeVerboseContent: Optional[bool] = None
    FieldLogLevel: Optional[str] = None


class AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails(BaseValidatorModel):
    EncryptionOption: Optional[str] = None
    KmsKey: Optional[str] = None


class AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails(BaseValidatorModel):
    Value: Optional[str] = None


class AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails(BaseValidatorModel):
    OnDemandAllocationStrategy: Optional[str] = None
    OnDemandBaseCapacity: Optional[int] = None
    OnDemandPercentageAboveBaseCapacity: Optional[int] = None
    SpotAllocationStrategy: Optional[str] = None
    SpotInstancePools: Optional[int] = None
    SpotMaxPrice: Optional[str] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None


class AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsAutoScalingLaunchConfigurationMetadataOptions(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None


class AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutput(BaseValidatorModel):
    BackupOptions: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None


class AwsBackupBackupPlanAdvancedBackupSettingsDetails(BaseValidatorModel):
    BackupOptions: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None


class AwsBackupBackupPlanLifecycleDetails(BaseValidatorModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None


class AwsBackupBackupVaultNotificationsDetailsOutput(BaseValidatorModel):
    BackupVaultEvents: Optional[List[str]] = None
    SnsTopicArn: Optional[str] = None


class AwsBackupBackupVaultNotificationsDetails(BaseValidatorModel):
    BackupVaultEvents: Optional[List[str]] = None
    SnsTopicArn: Optional[str] = None


class AwsBackupRecoveryPointCalculatedLifecycleDetails(BaseValidatorModel):
    DeleteAt: Optional[str] = None
    MoveToColdStorageAt: Optional[str] = None


class AwsBackupRecoveryPointCreatedByDetails(BaseValidatorModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    BackupPlanVersion: Optional[str] = None
    BackupRuleId: Optional[str] = None


class AwsBackupRecoveryPointLifecycleDetails(BaseValidatorModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None


class AwsCertificateManagerCertificateExtendedKeyUsage(BaseValidatorModel):
    Name: Optional[str] = None
    OId: Optional[str] = None


class AwsCertificateManagerCertificateKeyUsage(BaseValidatorModel):
    Name: Optional[str] = None


class AwsCertificateManagerCertificateOptions(BaseValidatorModel):
    CertificateTransparencyLoggingPreference: Optional[str] = None


class AwsCertificateManagerCertificateResourceRecord(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None


class AwsCloudFormationStackDriftInformationDetails(BaseValidatorModel):
    StackDriftStatus: Optional[str] = None


class AwsCloudFormationStackOutputsDetails(BaseValidatorModel):
    Description: Optional[str] = None
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None


class AwsCloudFrontDistributionCacheBehavior(BaseValidatorModel):
    ViewerProtocolPolicy: Optional[str] = None


class AwsCloudFrontDistributionDefaultCacheBehavior(BaseValidatorModel):
    ViewerProtocolPolicy: Optional[str] = None


class AwsCloudFrontDistributionLogging(BaseValidatorModel):
    Bucket: Optional[str] = None
    Enabled: Optional[bool] = None
    IncludeCookies: Optional[bool] = None
    Prefix: Optional[str] = None


class AwsCloudFrontDistributionViewerCertificate(BaseValidatorModel):
    AcmCertificateArn: Optional[str] = None
    Certificate: Optional[str] = None
    CertificateSource: Optional[str] = None
    CloudFrontDefaultCertificate: Optional[bool] = None
    IamCertificateId: Optional[str] = None
    MinimumProtocolVersion: Optional[str] = None
    SslSupportMethod: Optional[str] = None


class AwsCloudFrontDistributionOriginSslProtocolsOutput(BaseValidatorModel):
    Items: Optional[List[str]] = None
    Quantity: Optional[int] = None


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutput(BaseValidatorModel):
    Items: Optional[List[int]] = None
    Quantity: Optional[int] = None


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodes(BaseValidatorModel):
    Items: Optional[List[int]] = None
    Quantity: Optional[int] = None


class AwsCloudFrontDistributionOriginS3OriginConfig(BaseValidatorModel):
    OriginAccessIdentity: Optional[str] = None


class AwsCloudFrontDistributionOriginSslProtocols(BaseValidatorModel):
    Items: Optional[List[str]] = None
    Quantity: Optional[int] = None


class AwsCloudTrailTrailDetails(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    CloudWatchLogsRoleArn: Optional[str] = None
    HasCustomEventSelectors: Optional[bool] = None
    HomeRegion: Optional[str] = None
    IncludeGlobalServiceEvents: Optional[bool] = None
    IsMultiRegionTrail: Optional[bool] = None
    IsOrganizationTrail: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    LogFileValidationEnabled: Optional[bool] = None
    Name: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SnsTopicName: Optional[str] = None
    TrailArn: Optional[str] = None


class AwsCloudWatchAlarmDimensionsDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsCodeBuildProjectArtifactsDetails(BaseValidatorModel):
    ArtifactIdentifier: Optional[str] = None
    EncryptionDisabled: Optional[bool] = None
    Location: Optional[str] = None
    Name: Optional[str] = None
    NamespaceType: Optional[str] = None
    OverrideArtifactName: Optional[bool] = None
    Packaging: Optional[str] = None
    Path: Optional[str] = None
    Type: Optional[str] = None


class AwsCodeBuildProjectSource(BaseValidatorModel):
    Type: Optional[str] = None
    Location: Optional[str] = None
    GitCloneDepth: Optional[int] = None
    InsecureSsl: Optional[bool] = None


class AwsCodeBuildProjectVpcConfigOutput(BaseValidatorModel):
    VpcId: Optional[str] = None
    Subnets: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None


class AwsCodeBuildProjectEnvironmentRegistryCredential(BaseValidatorModel):
    Credential: Optional[str] = None
    CredentialProvider: Optional[str] = None


class AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails(BaseValidatorModel):
    GroupName: Optional[str] = None
    Status: Optional[str] = None
    StreamName: Optional[str] = None


class AwsCodeBuildProjectLogsConfigS3LogsDetails(BaseValidatorModel):
    EncryptionDisabled: Optional[bool] = None
    Location: Optional[str] = None
    Status: Optional[str] = None


class AwsCodeBuildProjectVpcConfig(BaseValidatorModel):
    VpcId: Optional[str] = None
    Subnets: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class AwsCorsConfiguration(BaseValidatorModel):
    AllowOrigins: Optional[List[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[List[str]] = None
    AllowHeaders: Optional[List[str]] = None


class AwsDmsEndpointDetails(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    EndpointArn: Optional[str] = None
    EndpointIdentifier: Optional[str] = None
    EndpointType: Optional[str] = None
    EngineName: Optional[str] = None
    ExternalId: Optional[str] = None
    ExtraConnectionAttributes: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    SslMode: Optional[str] = None
    Username: Optional[str] = None


class AwsDmsReplicationInstanceReplicationSubnetGroupDetails(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: Optional[str] = None


class AwsDmsReplicationInstanceVpcSecurityGroupsDetails(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None


class AwsDmsReplicationTaskDetails(BaseValidatorModel):
    CdcStartPosition: Optional[str] = None
    CdcStartTime: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    MigrationType: Optional[str] = None
    Id: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    ReplicationTaskIdentifier: Optional[str] = None
    ReplicationTaskSettings: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TableMappings: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    TaskData: Optional[str] = None


class AwsDynamoDbTableAttributeDefinition(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[str] = None


class AwsDynamoDbTableBillingModeSummary(BaseValidatorModel):
    BillingMode: Optional[str] = None
    LastUpdateToPayPerRequestDateTime: Optional[str] = None


class AwsDynamoDbTableKeySchema(BaseValidatorModel):
    AttributeName: Optional[str] = None
    KeyType: Optional[str] = None


class AwsDynamoDbTableProvisionedThroughput(BaseValidatorModel):
    LastDecreaseDateTime: Optional[str] = None
    LastIncreaseDateTime: Optional[str] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[int] = None
    WriteCapacityUnits: Optional[int] = None


class AwsDynamoDbTableRestoreSummary(BaseValidatorModel):
    SourceBackupArn: Optional[str] = None
    SourceTableArn: Optional[str] = None
    RestoreDateTime: Optional[str] = None
    RestoreInProgress: Optional[bool] = None


class AwsDynamoDbTableSseDescription(BaseValidatorModel):
    InaccessibleEncryptionDateTime: Optional[str] = None
    Status: Optional[str] = None
    SseType: Optional[str] = None
    KmsMasterKeyArn: Optional[str] = None


class AwsDynamoDbTableStreamSpecification(BaseValidatorModel):
    StreamEnabled: Optional[bool] = None
    StreamViewType: Optional[str] = None


class AwsDynamoDbTableProjectionOutput(BaseValidatorModel):
    NonKeyAttributes: Optional[List[str]] = None
    ProjectionType: Optional[str] = None


class AwsDynamoDbTableProjection(BaseValidatorModel):
    NonKeyAttributes: Optional[List[str]] = None
    ProjectionType: Optional[str] = None


class AwsDynamoDbTableProvisionedThroughputOverride(BaseValidatorModel):
    ReadCapacityUnits: Optional[int] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails(BaseValidatorModel):
    DirectoryId: Optional[str] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails(BaseValidatorModel):
    SamlProviderArn: Optional[str] = None
    SelfServiceSamlProviderArn: Optional[str] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails(BaseValidatorModel):
    ClientRootCertificateChain: Optional[str] = None


class AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None


class AwsEc2ClientVpnEndpointConnectionLogOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None


class AwsEc2EipDetails(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    AssociationId: Optional[str] = None
    Domain: Optional[str] = None
    PublicIpv4Pool: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfaceOwnerId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None


class AwsEc2InstanceMetadataOptions(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None
    InstanceMetadataTags: Optional[str] = None


class AwsEc2InstanceMonitoringDetails(BaseValidatorModel):
    State: Optional[str] = None


class AwsEc2InstanceNetworkInterfacesDetails(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    Throughput: Optional[int] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None


class AwsEc2LaunchTemplateDataCpuOptionsDetails(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None


class AwsEc2LaunchTemplateDataCreditSpecificationDetails(BaseValidatorModel):
    CpuCredits: Optional[str] = None


class AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails(BaseValidatorModel):
    Type: Optional[str] = None


class AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails(BaseValidatorModel):
    Count: Optional[int] = None
    Type: Optional[str] = None


class AwsEc2LaunchTemplateDataEnclaveOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsEc2LaunchTemplateDataHibernationOptionsDetails(BaseValidatorModel):
    Configured: Optional[bool] = None


class AwsEc2LaunchTemplateDataIamInstanceProfileDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class AwsEc2LaunchTemplateDataLicenseSetDetails(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


class AwsEc2LaunchTemplateDataMaintenanceOptionsDetails(BaseValidatorModel):
    AutoRecovery: Optional[str] = None


class AwsEc2LaunchTemplateDataMetadataOptionsDetails(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpTokens: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    InstanceMetadataTags: Optional[str] = None


class AwsEc2LaunchTemplateDataMonitoringDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsEc2LaunchTemplateDataPlacementDetails(BaseValidatorModel):
    Affinity: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    SpreadDomain: Optional[str] = None
    Tenancy: Optional[str] = None


class AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails(BaseValidatorModel):
    EnableResourceNameDnsAAAARecord: Optional[bool] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    HostnameType: Optional[str] = None


class AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails(BaseValidatorModel):
    BlockDurationMinutes: Optional[int] = None
    InstanceInterruptionBehavior: Optional[str] = None
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[str] = None
    ValidUntil: Optional[str] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails(BaseValidatorModel):
    Max: Optional[float] = None
    Min: Optional[float] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails(BaseValidatorModel):
    Max: Optional[float] = None
    Min: Optional[float] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails(BaseValidatorModel):
    Ipv6Address: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails(BaseValidatorModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None


class AwsEc2NetworkAclAssociation(BaseValidatorModel):
    NetworkAclAssociationId: Optional[str] = None
    NetworkAclId: Optional[str] = None
    SubnetId: Optional[str] = None


class IcmpTypeCode(BaseValidatorModel):
    Code: Optional[int] = None
    Type: Optional[int] = None


class PortRangeFromTo(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None


class AwsEc2NetworkInterfaceAttachment(BaseValidatorModel):
    AttachTime: Optional[str] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    Status: Optional[str] = None


class AwsEc2NetworkInterfaceIpV6AddressDetail(BaseValidatorModel):
    IpV6Address: Optional[str] = None


class AwsEc2NetworkInterfacePrivateIpAddressDetail(BaseValidatorModel):
    PrivateIpAddress: Optional[str] = None
    PrivateDnsName: Optional[str] = None


class AwsEc2NetworkInterfaceSecurityGroup(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None


class PropagatingVgwSetDetails(BaseValidatorModel):
    GatewayId: Optional[str] = None


class RouteSetDetails(BaseValidatorModel):
    CarrierGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    NatGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    Origin: Optional[str] = None
    State: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None


class AwsEc2SecurityGroupIpRange(BaseValidatorModel):
    CidrIp: Optional[str] = None


class AwsEc2SecurityGroupIpv6Range(BaseValidatorModel):
    CidrIpv6: Optional[str] = None


class AwsEc2SecurityGroupPrefixListId(BaseValidatorModel):
    PrefixListId: Optional[str] = None


class AwsEc2SecurityGroupUserIdGroupPair(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None


class Ipv6CidrBlockAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None


class AwsEc2TransitGatewayDetailsOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteTablePropagation: Optional[str] = None
    AutoAcceptSharedAttachments: Optional[str] = None
    DefaultRouteTableAssociation: Optional[str] = None
    TransitGatewayCidrBlocks: Optional[List[str]] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    VpnEcmpSupport: Optional[str] = None
    DnsSupport: Optional[str] = None
    MulticastSupport: Optional[str] = None
    AmazonSideAsn: Optional[int] = None


class AwsEc2TransitGatewayDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteTablePropagation: Optional[str] = None
    AutoAcceptSharedAttachments: Optional[str] = None
    DefaultRouteTableAssociation: Optional[str] = None
    TransitGatewayCidrBlocks: Optional[List[str]] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    VpnEcmpSupport: Optional[str] = None
    DnsSupport: Optional[str] = None
    MulticastSupport: Optional[str] = None
    AmazonSideAsn: Optional[int] = None


class AwsEc2VolumeAttachment(BaseValidatorModel):
    AttachTime: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    InstanceId: Optional[str] = None
    Status: Optional[str] = None


class CidrBlockAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None


class AwsEc2VpcEndpointServiceServiceTypeDetails(BaseValidatorModel):
    ServiceType: Optional[str] = None


class AwsEc2VpcPeeringConnectionStatusDetails(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class VpcInfoCidrBlockSetDetails(BaseValidatorModel):
    CidrBlock: Optional[str] = None


class VpcInfoIpv6CidrBlockSetDetails(BaseValidatorModel):
    Ipv6CidrBlock: Optional[str] = None


class VpcInfoPeeringOptionsDetails(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None


class AwsEc2VpnConnectionRoutesDetails(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    State: Optional[str] = None


class AwsEc2VpnConnectionVgwTelemetryDetails(BaseValidatorModel):
    AcceptedRouteCount: Optional[int] = None
    CertificateArn: Optional[str] = None
    LastStatusChange: Optional[str] = None
    OutsideIpAddress: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None


class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutput(BaseValidatorModel):
    DpdTimeoutSeconds: Optional[int] = None
    IkeVersions: Optional[List[str]] = None
    OutsideIpAddress: Optional[str] = None
    Phase1DhGroupNumbers: Optional[List[int]] = None
    Phase1EncryptionAlgorithms: Optional[List[str]] = None
    Phase1IntegrityAlgorithms: Optional[List[str]] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2DhGroupNumbers: Optional[List[int]] = None
    Phase2EncryptionAlgorithms: Optional[List[str]] = None
    Phase2IntegrityAlgorithms: Optional[List[str]] = None
    Phase2LifetimeSeconds: Optional[int] = None
    PreSharedKey: Optional[str] = None
    RekeyFuzzPercentage: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    TunnelInsideCidr: Optional[str] = None


class AwsEc2VpnConnectionOptionsTunnelOptionsDetails(BaseValidatorModel):
    DpdTimeoutSeconds: Optional[int] = None
    IkeVersions: Optional[List[str]] = None
    OutsideIpAddress: Optional[str] = None
    Phase1DhGroupNumbers: Optional[List[int]] = None
    Phase1EncryptionAlgorithms: Optional[List[str]] = None
    Phase1IntegrityAlgorithms: Optional[List[str]] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2DhGroupNumbers: Optional[List[int]] = None
    Phase2EncryptionAlgorithms: Optional[List[str]] = None
    Phase2IntegrityAlgorithms: Optional[List[str]] = None
    Phase2LifetimeSeconds: Optional[int] = None
    PreSharedKey: Optional[str] = None
    RekeyFuzzPercentage: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    TunnelInsideCidr: Optional[str] = None


class AwsEcrContainerImageDetailsOutput(BaseValidatorModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[List[str]] = None
    ImagePublishedAt: Optional[str] = None


class AwsEcrContainerImageDetails(BaseValidatorModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[List[str]] = None
    ImagePublishedAt: Optional[str] = None


class AwsEcrRepositoryImageScanningConfigurationDetails(BaseValidatorModel):
    ScanOnPush: Optional[bool] = None


class AwsEcrRepositoryLifecyclePolicyDetails(BaseValidatorModel):
    LifecyclePolicyText: Optional[str] = None
    RegistryId: Optional[str] = None


class AwsEcsClusterClusterSettingsDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails(BaseValidatorModel):
    CloudWatchEncryptionEnabled: Optional[bool] = None
    CloudWatchLogGroupName: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3EncryptionEnabled: Optional[bool] = None
    S3KeyPrefix: Optional[str] = None


class AwsEcsClusterDefaultCapacityProviderStrategyDetails(BaseValidatorModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None


class AwsMountPoint(BaseValidatorModel):
    SourceVolume: Optional[str] = None
    ContainerPath: Optional[str] = None


class AwsEcsServiceCapacityProviderStrategyDetails(BaseValidatorModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None


class AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails(BaseValidatorModel):
    Enable: Optional[bool] = None
    Rollback: Optional[bool] = None


class AwsEcsServiceDeploymentControllerDetails(BaseValidatorModel):
    Type: Optional[str] = None


class AwsEcsServiceLoadBalancersDetails(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    LoadBalancerName: Optional[str] = None
    TargetGroupArn: Optional[str] = None


class AwsEcsServicePlacementConstraintsDetails(BaseValidatorModel):
    Expression: Optional[str] = None
    Type: Optional[str] = None


class AwsEcsServicePlacementStrategiesDetails(BaseValidatorModel):
    Field: Optional[str] = None
    Type: Optional[str] = None


class AwsEcsServiceServiceRegistriesDetails(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    Port: Optional[int] = None
    RegistryArn: Optional[str] = None


class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutput(BaseValidatorModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None


class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails(BaseValidatorModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails(BaseValidatorModel):
    Condition: Optional[str] = None
    ContainerName: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails(BaseValidatorModel):
    Hostname: Optional[str] = None
    IpAddress: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutput(BaseValidatorModel):
    Options: Optional[Dict[str, str]] = None
    Type: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutput(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    ReadOnly: Optional[bool] = None
    SourceVolume: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails(BaseValidatorModel):
    ContainerPort: Optional[int] = None
    HostPort: Optional[int] = None
    Protocol: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails(BaseValidatorModel):
    CredentialsParameter: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails(BaseValidatorModel):
    Name: Optional[str] = None
    ValueFrom: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails(BaseValidatorModel):
    Namespace: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails(BaseValidatorModel):
    HardLimit: Optional[int] = None
    Name: Optional[str] = None
    SoftLimit: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails(BaseValidatorModel):
    ReadOnly: Optional[bool] = None
    SourceContainer: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails(BaseValidatorModel):
    Options: Optional[Dict[str, str]] = None
    Type: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutput(BaseValidatorModel):
    Add: Optional[List[str]] = None
    Drop: Optional[List[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails(BaseValidatorModel):
    Add: Optional[List[str]] = None
    Drop: Optional[List[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutput(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[List[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutput(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[List[str]] = None
    Size: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[List[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[List[str]] = None
    Size: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails(BaseValidatorModel):
    Name: Optional[str] = None
    ValueFrom: Optional[str] = None


class AwsEcsTaskDefinitionInferenceAcceleratorsDetails(BaseValidatorModel):
    DeviceName: Optional[str] = None
    DeviceType: Optional[str] = None


class AwsEcsTaskDefinitionPlacementConstraintsDetails(BaseValidatorModel):
    Expression: Optional[str] = None
    Type: Optional[str] = None


class AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutput(BaseValidatorModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Dict[str, str]] = None
    Labels: Optional[Dict[str, str]] = None
    Scope: Optional[str] = None


class AwsEcsTaskDefinitionVolumesHostDetails(BaseValidatorModel):
    SourcePath: Optional[str] = None


class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails(BaseValidatorModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Dict[str, str]] = None
    Labels: Optional[Dict[str, str]] = None
    Scope: Optional[str] = None


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Iam: Optional[str] = None


class AwsEcsTaskVolumeHostDetails(BaseValidatorModel):
    SourcePath: Optional[str] = None


class AwsEfsAccessPointPosixUserDetailsOutput(BaseValidatorModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[List[str]] = None
    Uid: Optional[str] = None


class AwsEfsAccessPointPosixUserDetails(BaseValidatorModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[List[str]] = None
    Uid: Optional[str] = None


class AwsEfsAccessPointRootDirectoryCreationInfoDetails(BaseValidatorModel):
    OwnerGid: Optional[str] = None
    OwnerUid: Optional[str] = None
    Permissions: Optional[str] = None


class AwsEksClusterResourcesVpcConfigDetailsOutput(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    EndpointPublicAccess: Optional[bool] = None


class AwsEksClusterLoggingClusterLoggingDetailsOutput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Types: Optional[List[str]] = None


class AwsEksClusterLoggingClusterLoggingDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Types: Optional[List[str]] = None


class AwsEksClusterResourcesVpcConfigDetails(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    EndpointPublicAccess: Optional[bool] = None


class AwsElasticBeanstalkEnvironmentEnvironmentLink(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    LinkName: Optional[str] = None


class AwsElasticBeanstalkEnvironmentOptionSetting(BaseValidatorModel):
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None
    ResourceName: Optional[str] = None
    Value: Optional[str] = None


class AwsElasticBeanstalkEnvironmentTier(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Version: Optional[str] = None


class AwsElasticsearchDomainDomainEndpointOptions(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[str] = None


class AwsElasticsearchDomainEncryptionAtRestOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class AwsElasticsearchDomainNodeToNodeEncryptionOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsElasticsearchDomainServiceSoftwareOptions(BaseValidatorModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None


class AwsElasticsearchDomainVPCOptionsOutput(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VPCId: Optional[str] = None


class AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class AwsElasticsearchDomainLogPublishingOptionsLogConfig(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class AwsElasticsearchDomainVPCOptions(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VPCId: Optional[str] = None


class AwsElbAppCookieStickinessPolicy(BaseValidatorModel):
    CookieName: Optional[str] = None
    PolicyName: Optional[str] = None


class AwsElbLbCookieStickinessPolicy(BaseValidatorModel):
    CookieExpirationPeriod: Optional[int] = None
    PolicyName: Optional[str] = None


class AwsElbLoadBalancerAccessLog(BaseValidatorModel):
    EmitInterval: Optional[int] = None
    Enabled: Optional[bool] = None
    S3BucketName: Optional[str] = None
    S3BucketPrefix: Optional[str] = None


class AwsElbLoadBalancerAdditionalAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class AwsElbLoadBalancerConnectionDraining(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Timeout: Optional[int] = None


class AwsElbLoadBalancerConnectionSettings(BaseValidatorModel):
    IdleTimeout: Optional[int] = None


class AwsElbLoadBalancerCrossZoneLoadBalancing(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsElbLoadBalancerBackendServerDescriptionOutput(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None


class AwsElbLoadBalancerBackendServerDescription(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None


class AwsElbLoadBalancerHealthCheck(BaseValidatorModel):
    HealthyThreshold: Optional[int] = None
    Interval: Optional[int] = None
    Target: Optional[str] = None
    Timeout: Optional[int] = None
    UnhealthyThreshold: Optional[int] = None


class AwsElbLoadBalancerInstance(BaseValidatorModel):
    InstanceId: Optional[str] = None


class AwsElbLoadBalancerSourceSecurityGroup(BaseValidatorModel):
    GroupName: Optional[str] = None
    OwnerAlias: Optional[str] = None


class AwsElbLoadBalancerListener(BaseValidatorModel):
    InstancePort: Optional[int] = None
    InstanceProtocol: Optional[str] = None
    LoadBalancerPort: Optional[int] = None
    Protocol: Optional[str] = None
    SslCertificateId: Optional[str] = None


class AwsElbv2LoadBalancerAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class LoadBalancerState(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None


class AwsEventSchemasRegistryDetails(BaseValidatorModel):
    Description: Optional[str] = None
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None


class AwsEventsEndpointEventBusesDetails(BaseValidatorModel):
    EventBusArn: Optional[str] = None


class AwsEventsEndpointReplicationConfigDetails(BaseValidatorModel):
    State: Optional[str] = None


class AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails(BaseValidatorModel):
    HealthCheck: Optional[str] = None


class AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails(BaseValidatorModel):
    Route: Optional[str] = None


class AwsEventsEventbusDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Policy: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesCloudTrailDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesDnsLogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesFlowLogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesS3LogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetails(BaseValidatorModel):
    Reason: Optional[str] = None
    Status: Optional[str] = None


class AwsGuardDutyDetectorFeaturesDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None


class AwsIamAccessKeySessionContextAttributes(BaseValidatorModel):
    MfaAuthenticated: Optional[bool] = None
    CreationDate: Optional[str] = None


class AwsIamAccessKeySessionContextSessionIssuer(BaseValidatorModel):
    Type: Optional[str] = None
    PrincipalId: Optional[str] = None
    Arn: Optional[str] = None
    AccountId: Optional[str] = None
    UserName: Optional[str] = None


class AwsIamAttachedManagedPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None


class AwsIamGroupPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None


class AwsIamInstanceProfileRole(BaseValidatorModel):
    Arn: Optional[str] = None
    AssumeRolePolicyDocument: Optional[str] = None
    CreateDate: Optional[str] = None
    Path: Optional[str] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None


class AwsIamPermissionsBoundary(BaseValidatorModel):
    PermissionsBoundaryArn: Optional[str] = None
    PermissionsBoundaryType: Optional[str] = None


class AwsIamPolicyVersion(BaseValidatorModel):
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    CreateDate: Optional[str] = None


class AwsIamRolePolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None


class AwsIamUserPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None


class AwsKinesisStreamStreamEncryptionDetails(BaseValidatorModel):
    EncryptionType: Optional[str] = None
    KeyId: Optional[str] = None


class AwsKmsKeyDetails(BaseValidatorModel):
    AWSAccountId: Optional[str] = None
    CreationDate: Optional[float] = None
    KeyId: Optional[str] = None
    KeyManager: Optional[str] = None
    KeyState: Optional[str] = None
    Origin: Optional[str] = None
    Description: Optional[str] = None
    KeyRotationStatus: Optional[bool] = None


class AwsLambdaFunctionCode(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ZipFile: Optional[str] = None


class AwsLambdaFunctionDeadLetterConfig(BaseValidatorModel):
    TargetArn: Optional[str] = None


class AwsLambdaFunctionLayer(BaseValidatorModel):
    Arn: Optional[str] = None
    CodeSize: Optional[int] = None


class AwsLambdaFunctionTracingConfig(BaseValidatorModel):
    Mode: Optional[str] = None


class AwsLambdaFunctionVpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None


class AwsLambdaFunctionEnvironmentError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class AwsLambdaFunctionVpcConfig(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None


class AwsLambdaLayerVersionDetailsOutput(BaseValidatorModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[List[str]] = None
    CreatedDate: Optional[str] = None


class AwsLambdaLayerVersionDetails(BaseValidatorModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[List[str]] = None
    CreatedDate: Optional[str] = None


class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutput(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationTlsDetails(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails(BaseValidatorModel):
    DataVolumeKMSKeyId: Optional[str] = None


class AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails(BaseValidatorModel):
    InCluster: Optional[bool] = None
    ClientBroker: Optional[str] = None


class AwsNetworkFirewallFirewallSubnetMappingsDetails(BaseValidatorModel):
    SubnetId: Optional[str] = None


class AwsOpenSearchServiceDomainMasterUserOptionsDetails(BaseValidatorModel):
    MasterUserArn: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None


class AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class AwsOpenSearchServiceDomainDomainEndpointOptionsDetails(BaseValidatorModel):
    CustomEndpointCertificateArn: Optional[str] = None
    CustomEndpointEnabled: Optional[bool] = None
    EnforceHTTPS: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    TLSSecurityPolicy: Optional[str] = None


class AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails(BaseValidatorModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None
    OptionalDeployment: Optional[bool] = None


class AwsOpenSearchServiceDomainVpcOptionsDetailsOutput(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None


class AwsOpenSearchServiceDomainLogPublishingOption(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class AwsOpenSearchServiceDomainVpcOptionsDetails(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None


class AwsRdsDbClusterAssociatedRole(BaseValidatorModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbClusterMember(BaseValidatorModel):
    IsClusterWriter: Optional[bool] = None
    PromotionTier: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    DbClusterParameterGroupStatus: Optional[str] = None


class AwsRdsDbClusterOptionGroupMembership(BaseValidatorModel):
    DbClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbDomainMembership(BaseValidatorModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    Fqdn: Optional[str] = None
    IamRoleName: Optional[str] = None


class AwsRdsDbInstanceVpcSecurityGroup(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutput(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


class AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


class AwsRdsDbInstanceAssociatedRole(BaseValidatorModel):
    RoleArn: Optional[str] = None
    FeatureName: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbInstanceEndpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None


class AwsRdsDbOptionGroupMembership(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbParameterGroup(BaseValidatorModel):
    DbParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None


class AwsRdsDbProcessorFeature(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsRdsDbStatusInfo(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class AwsRdsPendingCloudWatchLogsExportsOutput(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None


class AwsRdsDbSecurityGroupEc2SecurityGroup(BaseValidatorModel):
    Ec2SecurityGroupId: Optional[str] = None
    Ec2SecurityGroupName: Optional[str] = None
    Ec2SecurityGroupOwnerId: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbSecurityGroupIpRange(BaseValidatorModel):
    CidrIp: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbSubnetGroupSubnetAvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class AwsRdsEventSubscriptionDetailsOutput(BaseValidatorModel):
    CustSubscriptionId: Optional[str] = None
    CustomerAwsId: Optional[str] = None
    Enabled: Optional[bool] = None
    EventCategoriesList: Optional[List[str]] = None
    EventSubscriptionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    SourceType: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None


class AwsRdsEventSubscriptionDetails(BaseValidatorModel):
    CustSubscriptionId: Optional[str] = None
    CustomerAwsId: Optional[str] = None
    Enabled: Optional[bool] = None
    EventCategoriesList: Optional[List[str]] = None
    EventSubscriptionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    SourceType: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None


class AwsRdsPendingCloudWatchLogsExports(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None


class AwsRedshiftClusterClusterNode(BaseValidatorModel):
    NodeRole: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PublicIpAddress: Optional[str] = None


class AwsRedshiftClusterClusterParameterStatus(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None


class AwsRedshiftClusterClusterSecurityGroup(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class AwsRedshiftClusterClusterSnapshotCopyStatus(BaseValidatorModel):
    DestinationRegion: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None


class AwsRedshiftClusterDeferredMaintenanceWindow(BaseValidatorModel):
    DeferMaintenanceEndTime: Optional[str] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[str] = None


class AwsRedshiftClusterElasticIpStatus(BaseValidatorModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None


class AwsRedshiftClusterEndpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


class AwsRedshiftClusterHsmStatus(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None


class AwsRedshiftClusterIamRole(BaseValidatorModel):
    ApplyStatus: Optional[str] = None
    IamRoleArn: Optional[str] = None


class AwsRedshiftClusterLoggingStatus(BaseValidatorModel):
    BucketName: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    LastFailureTime: Optional[str] = None
    LastSuccessfulDeliveryTime: Optional[str] = None
    LoggingEnabled: Optional[bool] = None
    S3KeyPrefix: Optional[str] = None


class AwsRedshiftClusterPendingModifiedValues(BaseValidatorModel):
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ClusterIdentifier: Optional[str] = None
    ClusterType: Optional[str] = None
    ClusterVersion: Optional[str] = None
    EncryptionType: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None


class AwsRedshiftClusterResizeInfo(BaseValidatorModel):
    AllowCancelResize: Optional[bool] = None
    ResizeType: Optional[str] = None


class AwsRedshiftClusterRestoreStatus(BaseValidatorModel):
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    Status: Optional[str] = None


class AwsRedshiftClusterVpcSecurityGroup(BaseValidatorModel):
    Status: Optional[str] = None
    VpcSecurityGroupId: Optional[str] = None


class AwsRoute53HostedZoneConfigDetails(BaseValidatorModel):
    Comment: Optional[str] = None


class AwsRoute53HostedZoneVpcDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Region: Optional[str] = None


class CloudWatchLogsLogGroupArnConfigDetails(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    HostedZoneId: Optional[str] = None
    Id: Optional[str] = None


class AwsS3AccessPointVpcConfigurationDetails(BaseValidatorModel):
    VpcId: Optional[str] = None


class AwsS3AccountPublicAccessBlockDetails(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None


class AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails(BaseValidatorModel):
    DaysAfterInitiation: Optional[int] = None


class AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails(BaseValidatorModel):
    Days: Optional[int] = None
    StorageClass: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails(BaseValidatorModel):
    Date: Optional[str] = None
    Days: Optional[int] = None
    StorageClass: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class AwsS3BucketBucketVersioningConfiguration(BaseValidatorModel):
    IsMfaDeleteEnabled: Optional[bool] = None
    Status: Optional[str] = None


class AwsS3BucketLoggingConfiguration(BaseValidatorModel):
    DestinationBucketName: Optional[str] = None
    LogFilePrefix: Optional[str] = None


class AwsS3BucketNotificationConfigurationS3KeyFilterRule(BaseValidatorModel):
    Name: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType] = None
    Value: Optional[str] = None


class AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails(BaseValidatorModel):
    Days: Optional[int] = None
    Mode: Optional[str] = None
    Years: Optional[int] = None


class AwsS3BucketServerSideEncryptionByDefault(BaseValidatorModel):
    SSEAlgorithm: Optional[str] = None
    KMSMasterKeyID: Optional[str] = None


class AwsS3BucketWebsiteConfigurationRedirectTo(BaseValidatorModel):
    Hostname: Optional[str] = None
    Protocol: Optional[str] = None


class AwsS3BucketWebsiteConfigurationRoutingRuleCondition(BaseValidatorModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None


class AwsS3BucketWebsiteConfigurationRoutingRuleRedirect(BaseValidatorModel):
    Hostname: Optional[str] = None
    HttpRedirectCode: Optional[str] = None
    Protocol: Optional[str] = None
    ReplaceKeyPrefixWith: Optional[str] = None
    ReplaceKeyWith: Optional[str] = None


class AwsS3ObjectDetails(BaseValidatorModel):
    LastModified: Optional[str] = None
    ETag: Optional[str] = None
    VersionId: Optional[str] = None
    ContentType: Optional[str] = None
    ServerSideEncryption: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None


class AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails(BaseValidatorModel):
    MinimumInstanceMetadataServiceVersion: Optional[str] = None


class AwsSecretsManagerSecretRotationRules(BaseValidatorModel):
    AutomaticallyAfterDays: Optional[int] = None


class BooleanFilter(BaseValidatorModel):
    Value: Optional[bool] = None


class IpFilter(BaseValidatorModel):
    Cidr: Optional[str] = None


class KeywordFilter(BaseValidatorModel):
    Value: Optional[str] = None


class AwsSecurityFindingIdentifier(BaseValidatorModel):
    Id: str
    ProductArn: str


class GeneratorDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[List[str]] = None


class Malware(BaseValidatorModel):
    Name: str
    Type: Optional[MalwareTypeType] = None
    Path: Optional[str] = None
    State: Optional[MalwareStateType] = None


class Note(BaseValidatorModel):
    Text: str
    UpdatedBy: str
    UpdatedAt: str


class PatchSummary(BaseValidatorModel):
    Id: str
    InstalledCount: Optional[int] = None
    MissingCount: Optional[int] = None
    FailedCount: Optional[int] = None
    InstalledOtherCount: Optional[int] = None
    InstalledRejectedCount: Optional[int] = None
    InstalledPendingReboot: Optional[int] = None
    OperationStartTime: Optional[str] = None
    OperationEndTime: Optional[str] = None
    RebootOption: Optional[str] = None
    Operation: Optional[str] = None


class ProcessDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Path: Optional[str] = None
    Pid: Optional[int] = None
    ParentPid: Optional[int] = None
    LaunchedAt: Optional[str] = None
    TerminatedAt: Optional[str] = None


class Severity(BaseValidatorModel):
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None
    Normalized: Optional[int] = None
    Original: Optional[str] = None


class ThreatIntelIndicator(BaseValidatorModel):
    Type: Optional[ThreatIntelIndicatorTypeType] = None
    Value: Optional[str] = None
    Category: Optional[ThreatIntelIndicatorCategoryType] = None
    LastObservedAt: Optional[str] = None
    Source: Optional[str] = None
    SourceUrl: Optional[str] = None


class Workflow(BaseValidatorModel):
    Status: Optional[WorkflowStatusType] = None


class AwsSnsTopicSubscription(BaseValidatorModel):
    Endpoint: Optional[str] = None
    Protocol: Optional[str] = None


class AwsSqsQueueDetails(BaseValidatorModel):
    KmsDataKeyReusePeriodSeconds: Optional[int] = None
    KmsMasterKeyId: Optional[str] = None
    QueueName: Optional[str] = None
    DeadLetterTargetArn: Optional[str] = None


class AwsSsmComplianceSummary(BaseValidatorModel):
    Status: Optional[str] = None
    CompliantCriticalCount: Optional[int] = None
    CompliantHighCount: Optional[int] = None
    CompliantMediumCount: Optional[int] = None
    ExecutionType: Optional[str] = None
    NonCompliantCriticalCount: Optional[int] = None
    CompliantInformationalCount: Optional[int] = None
    NonCompliantInformationalCount: Optional[int] = None
    CompliantUnspecifiedCount: Optional[int] = None
    NonCompliantLowCount: Optional[int] = None
    NonCompliantHighCount: Optional[int] = None
    CompliantLowCount: Optional[int] = None
    ComplianceType: Optional[str] = None
    PatchBaselineId: Optional[str] = None
    OverallSeverity: Optional[str] = None
    NonCompliantMediumCount: Optional[int] = None
    NonCompliantUnspecifiedCount: Optional[int] = None
    PatchGroup: Optional[str] = None


class AwsStepFunctionStateMachineTracingConfigurationDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails(BaseValidatorModel):
    LogGroupArn: Optional[str] = None


class AwsWafRateBasedRuleMatchPredicate(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None


class AwsWafRegionalRateBasedRuleMatchPredicate(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None


class AwsWafRegionalRulePredicateListDetails(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None


class AwsWafRegionalRuleGroupRulesActionDetails(BaseValidatorModel):
    Type: Optional[str] = None


class AwsWafRegionalWebAclRulesListActionDetails(BaseValidatorModel):
    Type: Optional[str] = None


class AwsWafRegionalWebAclRulesListOverrideActionDetails(BaseValidatorModel):
    Type: Optional[str] = None


class AwsWafRulePredicateListDetails(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None


class AwsWafRuleGroupRulesActionDetails(BaseValidatorModel):
    Type: Optional[str] = None


class WafAction(BaseValidatorModel):
    Type: Optional[str] = None


class WafExcludedRule(BaseValidatorModel):
    RuleId: Optional[str] = None


class WafOverrideAction(BaseValidatorModel):
    Type: Optional[str] = None


class AwsWafv2CustomHttpHeader(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsWafv2VisibilityConfigDetails(BaseValidatorModel):
    CloudWatchMetricsEnabled: Optional[bool] = None
    MetricName: Optional[str] = None
    SampledRequestsEnabled: Optional[bool] = None


class AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails(BaseValidatorModel):
    ImmunityTime: Optional[int] = None


class AwsXrayEncryptionConfigDetails(BaseValidatorModel):
    KeyId: Optional[str] = None
    Status: Optional[str] = None
    Type: Optional[str] = None


class BatchDeleteAutomationRulesRequest(BaseValidatorModel):
    AutomationRulesArns: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedAutomationRule(BaseValidatorModel):
    RuleArn: Optional[str] = None
    ErrorCode: Optional[int] = None
    ErrorMessage: Optional[str] = None


class BatchDisableStandardsRequest(BaseValidatorModel):
    StandardsSubscriptionArns: List[str]


class StandardsSubscriptionRequest(BaseValidatorModel):
    StandardsArn: str
    StandardsInput: Optional[Dict[str, str]] = None


class BatchGetAutomationRulesRequest(BaseValidatorModel):
    AutomationRulesArns: List[str]


class ConfigurationPolicyAssociationSummary(BaseValidatorModel):
    ConfigurationPolicyId: Optional[str] = None
    TargetId: Optional[str] = None
    TargetType: Optional[TargetTypeType] = None
    AssociationType: Optional[AssociationTypeType] = None
    UpdatedAt: Optional[datetime] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None
    AssociationStatusMessage: Optional[str] = None


class BatchGetSecurityControlsRequest(BaseValidatorModel):
    SecurityControlIds: List[str]


class UnprocessedSecurityControl(BaseValidatorModel):
    SecurityControlId: str
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None


class StandardsControlAssociationId(BaseValidatorModel):
    SecurityControlId: str
    StandardsArn: str


class StandardsControlAssociationDetail(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: Optional[List[str]] = None
    UpdatedAt: Optional[datetime] = None
    UpdatedReason: Optional[str] = None
    StandardsControlTitle: Optional[str] = None
    StandardsControlDescription: Optional[str] = None
    StandardsControlArns: Optional[List[str]] = None


class ImportFindingsError(BaseValidatorModel):
    Id: str
    ErrorCode: str
    ErrorMessage: str


class StandardsControlAssociationUpdate(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    AssociationStatus: AssociationStatusType
    UpdatedReason: Optional[str] = None


class BooleanConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[bool] = None


class Cell(BaseValidatorModel):
    Column: Optional[int] = None
    Row: Optional[int] = None
    ColumnName: Optional[str] = None
    CellReference: Optional[str] = None


class ClassificationStatus(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None


class CodeVulnerabilitiesFilePath(BaseValidatorModel):
    EndLine: Optional[int] = None
    FileName: Optional[str] = None
    FilePath: Optional[str] = None
    StartLine: Optional[int] = None


class SecurityControlParameterOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[List[str]] = None


class StatusReason(BaseValidatorModel):
    ReasonCode: str
    Description: Optional[str] = None


class DoubleConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[float] = None
    Min: Optional[float] = None
    Max: Optional[float] = None


class EnumConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[List[str]] = None


class EnumListConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[List[str]] = None
    MaxItems: Optional[int] = None
    AllowedValues: Optional[List[str]] = None


class IntegerConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[int] = None
    Min: Optional[int] = None
    Max: Optional[int] = None


class IntegerListConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[List[int]] = None
    Min: Optional[int] = None
    Max: Optional[int] = None
    MaxItems: Optional[int] = None


class StringConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    Re2Expression: Optional[str] = None
    ExpressionDescription: Optional[str] = None


class StringListConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[List[str]] = None
    Re2Expression: Optional[str] = None
    MaxItems: Optional[int] = None
    ExpressionDescription: Optional[str] = None


class Target(BaseValidatorModel):
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    RootId: Optional[str] = None


class ConfigurationPolicySummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    ServiceEnabled: Optional[bool] = None


class VolumeMount(BaseValidatorModel):
    Name: Optional[str] = None
    MountPath: Optional[str] = None


class CreateActionTargetRequest(BaseValidatorModel):
    Name: str
    Description: str
    Id: str


class CreateFindingAggregatorRequest(BaseValidatorModel):
    RegionLinkingMode: str
    Regions: Optional[List[str]] = None


class Result(BaseValidatorModel):
    AccountId: Optional[str] = None
    ProcessingResult: Optional[str] = None


class DateRange(BaseValidatorModel):
    Value: Optional[int] = None
    Unit: Optional[Literal['DAYS']] = None


class DeclineInvitationsRequest(BaseValidatorModel):
    AccountIds: List[str]


class DeleteActionTargetRequest(BaseValidatorModel):
    ActionTargetArn: str


class DeleteConfigurationPolicyRequest(BaseValidatorModel):
    Identifier: str


class DeleteFindingAggregatorRequest(BaseValidatorModel):
    FindingAggregatorArn: str


class DeleteInsightRequest(BaseValidatorModel):
    InsightArn: str


class DeleteInvitationsRequest(BaseValidatorModel):
    AccountIds: List[str]


class DeleteMembersRequest(BaseValidatorModel):
    AccountIds: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeActionTargetsRequest(BaseValidatorModel):
    ActionTargetArns: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeHubRequest(BaseValidatorModel):
    HubArn: Optional[str] = None


class OrganizationConfiguration(BaseValidatorModel):
    ConfigurationType: Optional[OrganizationConfigurationConfigurationTypeType] = None
    Status: Optional[OrganizationConfigurationStatusType] = None
    StatusMessage: Optional[str] = None


class DescribeProductsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProductArn: Optional[str] = None


class Product(BaseValidatorModel):
    ProductArn: str
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Description: Optional[str] = None
    Categories: Optional[List[str]] = None
    IntegrationTypes: Optional[List[IntegrationTypeType]] = None
    MarketplaceUrl: Optional[str] = None
    ActivationUrl: Optional[str] = None
    ProductSubscriptionResourcePolicy: Optional[str] = None


class DescribeStandardsControlsRequest(BaseValidatorModel):
    StandardsSubscriptionArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StandardsControl(BaseValidatorModel):
    StandardsControlArn: Optional[str] = None
    ControlStatus: Optional[ControlStatusType] = None
    DisabledReason: Optional[str] = None
    ControlStatusUpdatedAt: Optional[datetime] = None
    ControlId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    RemediationUrl: Optional[str] = None
    SeverityRating: Optional[SeverityRatingType] = None
    RelatedRequirements: Optional[List[str]] = None


class DescribeStandardsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DisableImportFindingsForProductRequest(BaseValidatorModel):
    ProductSubscriptionArn: str


class DisableOrganizationAdminAccountRequest(BaseValidatorModel):
    AdminAccountId: str


class DisassociateMembersRequest(BaseValidatorModel):
    AccountIds: List[str]


class EnableImportFindingsForProductRequest(BaseValidatorModel):
    ProductArn: str


class EnableOrganizationAdminAccountRequest(BaseValidatorModel):
    AdminAccountId: str


class EnableSecurityHubRequest(BaseValidatorModel):
    Tags: Optional[Dict[str, str]] = None
    EnableDefaultStandards: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None


class FilePaths(BaseValidatorModel):
    FilePath: Optional[str] = None
    FileName: Optional[str] = None
    ResourceId: Optional[str] = None
    Hash: Optional[str] = None


class FindingAggregator(BaseValidatorModel):
    FindingAggregatorArn: Optional[str] = None


class FindingHistoryUpdateSource(BaseValidatorModel):
    Type: Optional[FindingHistoryUpdateSourceTypeType] = None
    Identity: Optional[str] = None


class FindingHistoryUpdate(BaseValidatorModel):
    UpdatedField: Optional[str] = None
    OldValue: Optional[str] = None
    NewValue: Optional[str] = None


class FindingProviderSeverity(BaseValidatorModel):
    Label: Optional[SeverityLabelType] = None
    Original: Optional[str] = None


class FirewallPolicyStatefulRuleGroupReferencesDetails(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class FirewallPolicyStatelessRuleGroupReferencesDetails(BaseValidatorModel):
    Priority: Optional[int] = None
    ResourceArn: Optional[str] = None


class GeneratorDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[List[str]] = None


class Invitation(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    MemberStatus: Optional[str] = None


class GetConfigurationPolicyRequest(BaseValidatorModel):
    Identifier: str


class GetEnabledStandardsRequest(BaseValidatorModel):
    StandardsSubscriptionArns: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetFindingAggregatorRequest(BaseValidatorModel):
    FindingAggregatorArn: str

Timestamp = Union[datetime, str]


class SortCriterion(BaseValidatorModel):
    Field: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


class GetInsightResultsRequest(BaseValidatorModel):
    InsightArn: str


class GetInsightsRequest(BaseValidatorModel):
    InsightArns: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMembersRequest(BaseValidatorModel):
    AccountIds: List[str]


class Member(BaseValidatorModel):
    AccountId: Optional[str] = None
    Email: Optional[str] = None
    MasterId: Optional[str] = None
    AdministratorId: Optional[str] = None
    MemberStatus: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class GetSecurityControlDefinitionRequest(BaseValidatorModel):
    SecurityControlId: str


class IndicatorOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    Title: Optional[str] = None
    Type: Optional[str] = None


class Indicator(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    Title: Optional[str] = None
    Type: Optional[str] = None


class InsightResultValue(BaseValidatorModel):
    GroupByAttributeValue: str
    Count: int


class InviteMembersRequest(BaseValidatorModel):
    AccountIds: List[str]


class ListAutomationRulesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListConfigurationPoliciesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEnabledProductsForImportRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFindingAggregatorsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInvitationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMembersRequest(BaseValidatorModel):
    OnlyAssociated: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOrganizationAdminAccountsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSecurityControlDefinitionsRequest(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListStandardsControlAssociationsRequest(BaseValidatorModel):
    SecurityControlId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StandardsControlAssociationSummary(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: Optional[List[str]] = None
    UpdatedAt: Optional[datetime] = None
    UpdatedReason: Optional[str] = None
    StandardsControlTitle: Optional[str] = None
    StandardsControlDescription: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class NetworkAutonomousSystem(BaseValidatorModel):
    Name: Optional[str] = None
    Number: Optional[int] = None


class NetworkConnection(BaseValidatorModel):
    Direction: Optional[ConnectionDirectionType] = None


class NetworkGeoLocation(BaseValidatorModel):
    City: Optional[str] = None
    Country: Optional[str] = None
    Lat: Optional[float] = None
    Lon: Optional[float] = None


class PortRange(BaseValidatorModel):
    Begin: Optional[int] = None
    End: Optional[int] = None


class Range(BaseValidatorModel):
    Start: Optional[int] = None
    End: Optional[int] = None
    StartColumn: Optional[int] = None


class Record(BaseValidatorModel):
    JsonPath: Optional[str] = None
    RecordIndex: Optional[int] = None


class ParameterValueOutput(BaseValidatorModel):
    Integer: Optional[int] = None
    IntegerList: Optional[List[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[List[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[List[str]] = None


class ParameterValue(BaseValidatorModel):
    Integer: Optional[int] = None
    IntegerList: Optional[List[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[List[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[List[str]] = None


class Recommendation(BaseValidatorModel):
    Text: Optional[str] = None
    Url: Optional[str] = None


class RuleGroupSourceListDetailsOutput(BaseValidatorModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[List[str]] = None
    Targets: Optional[List[str]] = None


class RuleGroupSourceListDetails(BaseValidatorModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[List[str]] = None
    Targets: Optional[List[str]] = None


class RuleGroupSourceStatefulRulesHeaderDetails(BaseValidatorModel):
    Destination: Optional[str] = None
    DestinationPort: Optional[str] = None
    Direction: Optional[str] = None
    Protocol: Optional[str] = None
    Source: Optional[str] = None
    SourcePort: Optional[str] = None


class RuleGroupSourceStatefulRulesOptionsDetailsOutput(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None


class RuleGroupSourceStatefulRulesOptionsDetails(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None


class RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class RuleGroupSourceStatelessRuleMatchAttributesDestinations(BaseValidatorModel):
    AddressDefinition: Optional[str] = None


class RuleGroupSourceStatelessRuleMatchAttributesSourcePorts(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class RuleGroupSourceStatelessRuleMatchAttributesSources(BaseValidatorModel):
    AddressDefinition: Optional[str] = None


class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutput(BaseValidatorModel):
    Flags: Optional[List[str]] = None
    Masks: Optional[List[str]] = None


class RuleGroupSourceStatelessRuleMatchAttributesTcpFlags(BaseValidatorModel):
    Flags: Optional[List[str]] = None
    Masks: Optional[List[str]] = None


class RuleGroupVariablesIpSetsDetailsOutput(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class RuleGroupVariablesIpSetsDetails(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class RuleGroupVariablesPortSetsDetailsOutput(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class RuleGroupVariablesPortSetsDetails(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class SecurityControlParameter(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[List[str]] = None


class SoftwarePackage(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Epoch: Optional[str] = None
    Release: Optional[str] = None
    Architecture: Optional[str] = None
    PackageManager: Optional[str] = None
    FilePath: Optional[str] = None
    FixedInVersion: Optional[str] = None
    Remediation: Optional[str] = None
    SourceLayerHash: Optional[str] = None
    SourceLayerArn: Optional[str] = None


class StandardsManagedBy(BaseValidatorModel):
    Company: Optional[str] = None
    Product: Optional[str] = None


class StandardsStatusReason(BaseValidatorModel):
    StatusReasonCode: StatusReasonCodeType


class StatelessCustomPublishMetricActionDimension(BaseValidatorModel):
    Value: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateActionTargetRequest(BaseValidatorModel):
    ActionTargetArn: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateFindingAggregatorRequest(BaseValidatorModel):
    FindingAggregatorArn: str
    RegionLinkingMode: str
    Regions: Optional[List[str]] = None


class UpdateSecurityHubConfigurationRequest(BaseValidatorModel):
    AutoEnableControls: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None


class UpdateStandardsControlRequest(BaseValidatorModel):
    StandardsControlArn: str
    ControlStatus: Optional[ControlStatusType] = None
    DisabledReason: Optional[str] = None


class VulnerabilityVendor(BaseValidatorModel):
    Name: str
    Url: Optional[str] = None
    VendorSeverity: Optional[str] = None
    VendorCreatedAt: Optional[str] = None
    VendorUpdatedAt: Optional[str] = None


class CreateMembersRequest(BaseValidatorModel):
    AccountDetails: List[AccountDetails]


class ActionRemoteIpDetails(BaseValidatorModel):
    IpAddressV4: Optional[str] = None
    Organization: Optional[IpOrganizationDetails] = None
    Country: Optional[Country] = None
    City: Optional[City] = None
    GeoLocation: Optional[GeoLocation] = None


class ActorUser(BaseValidatorModel):
    Name: Optional[str] = None
    Uid: Optional[str] = None
    Type: Optional[str] = None
    CredentialUid: Optional[str] = None
    Account: Optional[UserAccount] = None


class CvssOutput(BaseValidatorModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[List[Adjustment]] = None


class Cvss(BaseValidatorModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[List[Adjustment]] = None


class ListConfigurationPolicyAssociationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[AssociationFilters] = None


class AssociationSetDetails(BaseValidatorModel):
    AssociationState: Optional[AssociationStateDetails] = None
    GatewayId: Optional[str] = None
    Main: Optional[bool] = None
    RouteTableAssociationId: Optional[str] = None
    RouteTableId: Optional[str] = None
    SubnetId: Optional[str] = None


class AutomationRulesFindingFieldsUpdateOutput(BaseValidatorModel):
    Note: Optional[NoteUpdate] = None
    Severity: Optional[SeverityUpdate] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[List[str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Workflow: Optional[WorkflowUpdate] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None


class AutomationRulesFindingFieldsUpdate(BaseValidatorModel):
    Note: Optional[NoteUpdate] = None
    Severity: Optional[SeverityUpdate] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[List[str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Workflow: Optional[WorkflowUpdate] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None

AwsAmazonMqBrokerLdapServerMetadataDetailsUnion = Union[AwsAmazonMqBrokerLdapServerMetadataDetails, AwsAmazonMqBrokerLdapServerMetadataDetailsOutput]


class AwsAmazonMqBrokerLogsDetails(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None
    AuditLogGroup: Optional[str] = None
    GeneralLogGroup: Optional[str] = None
    Pending: Optional[AwsAmazonMqBrokerLogsPendingDetails] = None

AwsApiGatewayCanarySettingsUnion = Union[AwsApiGatewayCanarySettings, AwsApiGatewayCanarySettingsOutput]


class AwsApiGatewayRestApiDetailsOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[List[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationOutput] = None

AwsApiGatewayEndpointConfigurationUnion = Union[AwsApiGatewayEndpointConfiguration, AwsApiGatewayEndpointConfigurationOutput]


class AwsApiGatewayStageDetailsOutput(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[List[AwsApiGatewayMethodSettings]] = None
    Variables: Optional[Dict[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsOutput] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None


class AwsApiGatewayV2ApiDetailsOutput(BaseValidatorModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationOutput] = None


class AwsApiGatewayV2StageDetailsOutput(BaseValidatorModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Dict[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None


class AwsApiGatewayV2StageDetails(BaseValidatorModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Dict[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None


class AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails(BaseValidatorModel):
    AuthenticationType: Optional[str] = None
    LambdaAuthorizerConfig: Optional[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetails] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetails] = None


class AwsAthenaWorkGroupConfigurationResultConfigurationDetails(BaseValidatorModel):
    EncryptionConfiguration: Optional[AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutput(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification] = None
    Overrides: Optional[List[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails]] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification] = None
    Overrides: Optional[List[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails]] = None


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails] = None
    NoDevice: Optional[bool] = None
    VirtualName: Optional[str] = None

AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnion = Union[AwsBackupBackupPlanAdvancedBackupSettingsDetails, AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutput]


class AwsBackupBackupPlanRuleCopyActionsDetails(BaseValidatorModel):
    DestinationBackupVaultArn: Optional[str] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetails] = None


class AwsBackupBackupVaultDetailsOutput(BaseValidatorModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsOutput] = None
    AccessPolicy: Optional[str] = None

AwsBackupBackupVaultNotificationsDetailsUnion = Union[AwsBackupBackupVaultNotificationsDetails, AwsBackupBackupVaultNotificationsDetailsOutput]


class AwsBackupRecoveryPointDetails(BaseValidatorModel):
    BackupSizeInBytes: Optional[int] = None
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    CalculatedLifecycle: Optional[AwsBackupRecoveryPointCalculatedLifecycleDetails] = None
    CompletionDate: Optional[str] = None
    CreatedBy: Optional[AwsBackupRecoveryPointCreatedByDetails] = None
    CreationDate: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IsEncrypted: Optional[bool] = None
    LastRestoreTime: Optional[str] = None
    Lifecycle: Optional[AwsBackupRecoveryPointLifecycleDetails] = None
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    SourceBackupVaultArn: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    StorageClass: Optional[str] = None


class AwsCertificateManagerCertificateDomainValidationOptionOutput(BaseValidatorModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecord] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[List[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None


class AwsCertificateManagerCertificateDomainValidationOption(BaseValidatorModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecord] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[List[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None


class AwsCloudFormationStackDetailsOutput(BaseValidatorModel):
    Capabilities: Optional[List[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetails] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    Outputs: Optional[List[AwsCloudFormationStackOutputsDetails]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None


class AwsCloudFormationStackDetails(BaseValidatorModel):
    Capabilities: Optional[List[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetails] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    Outputs: Optional[List[AwsCloudFormationStackOutputsDetails]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None


class AwsCloudFrontDistributionCacheBehaviorsOutput(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionCacheBehavior]] = None


class AwsCloudFrontDistributionCacheBehaviors(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionCacheBehavior]] = None


class AwsCloudFrontDistributionOriginCustomOriginConfigOutput(BaseValidatorModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsOutput] = None


class AwsCloudFrontDistributionOriginGroupFailoverOutput(BaseValidatorModel):
    StatusCodes: Optional[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutput] = None

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnion = Union[AwsCloudFrontDistributionOriginGroupFailoverStatusCodes, AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutput]

AwsCloudFrontDistributionOriginSslProtocolsUnion = Union[AwsCloudFrontDistributionOriginSslProtocols, AwsCloudFrontDistributionOriginSslProtocolsOutput]


class AwsCloudWatchAlarmDetailsOutput(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[List[AwsCloudWatchAlarmDimensionsDetails]] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    EvaluationPeriods: Optional[int] = None
    ExtendedStatistic: Optional[str] = None
    InsufficientDataActions: Optional[List[str]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    OkActions: Optional[List[str]] = None
    Period: Optional[int] = None
    Statistic: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdMetricId: Optional[str] = None
    TreatMissingData: Optional[str] = None
    Unit: Optional[str] = None


class AwsCloudWatchAlarmDetails(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[List[AwsCloudWatchAlarmDimensionsDetails]] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    EvaluationPeriods: Optional[int] = None
    ExtendedStatistic: Optional[str] = None
    InsufficientDataActions: Optional[List[str]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    OkActions: Optional[List[str]] = None
    Period: Optional[int] = None
    Statistic: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdMetricId: Optional[str] = None
    TreatMissingData: Optional[str] = None
    Unit: Optional[str] = None


class AwsCodeBuildProjectEnvironmentOutput(BaseValidatorModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails]] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredential] = None
    Type: Optional[str] = None


class AwsCodeBuildProjectEnvironment(BaseValidatorModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails]] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredential] = None
    Type: Optional[str] = None


class AwsCodeBuildProjectLogsConfigDetails(BaseValidatorModel):
    CloudWatchLogs: Optional[AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails] = None
    S3Logs: Optional[AwsCodeBuildProjectLogsConfigS3LogsDetails] = None

AwsCodeBuildProjectVpcConfigUnion = Union[AwsCodeBuildProjectVpcConfig, AwsCodeBuildProjectVpcConfigOutput]

AwsCorsConfigurationUnion = Union[AwsCorsConfiguration, AwsCorsConfigurationOutput]


class AwsDmsReplicationInstanceDetailsOutput(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    EngineVersion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ReplicationInstanceClass: Optional[str] = None
    ReplicationInstanceIdentifier: Optional[str] = None
    ReplicationSubnetGroup: Optional[AwsDmsReplicationInstanceReplicationSubnetGroupDetails] = None
    VpcSecurityGroups: Optional[List[AwsDmsReplicationInstanceVpcSecurityGroupsDetails]] = None


class AwsDmsReplicationInstanceDetails(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    EngineVersion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ReplicationInstanceClass: Optional[str] = None
    ReplicationInstanceIdentifier: Optional[str] = None
    ReplicationSubnetGroup: Optional[AwsDmsReplicationInstanceReplicationSubnetGroupDetails] = None
    VpcSecurityGroups: Optional[List[AwsDmsReplicationInstanceVpcSecurityGroupsDetails]] = None


class AwsDynamoDbTableGlobalSecondaryIndexOutput(BaseValidatorModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutput] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None


class AwsDynamoDbTableLocalSecondaryIndexOutput(BaseValidatorModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutput] = None

AwsDynamoDbTableProjectionUnion = Union[AwsDynamoDbTableProjection, AwsDynamoDbTableProjectionOutput]


class AwsDynamoDbTableReplicaGlobalSecondaryIndex(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedThroughputOverride: Optional[AwsDynamoDbTableProvisionedThroughputOverride] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsDetails(BaseValidatorModel):
    Type: Optional[str] = None
    ActiveDirectory: Optional[AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails] = None
    MutualAuthentication: Optional[AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails] = None
    FederatedAuthentication: Optional[AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails] = None


class AwsEc2ClientVpnEndpointClientConnectOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None
    Status: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails] = None


class AwsEc2InstanceDetailsOutput(BaseValidatorModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[List[str]] = None
    IpV6Addresses: Optional[List[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[List[AwsEc2InstanceNetworkInterfacesDetails]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptions] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetails] = None


class AwsEc2InstanceDetails(BaseValidatorModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[List[str]] = None
    IpV6Addresses: Optional[List[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[List[AwsEc2InstanceNetworkInterfacesDetails]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptions] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetails] = None


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails(BaseValidatorModel):
    CapacityReservationPreference: Optional[str] = None
    CapacityReservationTarget: Optional[AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails] = None


class AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails(BaseValidatorModel):
    MarketType: Optional[str] = None
    SpotOptions: Optional[AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutput(BaseValidatorModel):
    AcceleratorCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails] = None
    AcceleratorManufacturers: Optional[List[str]] = None
    AcceleratorNames: Optional[List[str]] = None
    AcceleratorTotalMemoryMiB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails] = None
    AcceleratorTypes: Optional[List[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[List[str]] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[List[str]] = None
    MemoryGiBPerVCpu: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails] = None
    MemoryMiB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails] = None
    NetworkInterfaceCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails] = None
    VCpuCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsDetails(BaseValidatorModel):
    AcceleratorCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails] = None
    AcceleratorManufacturers: Optional[List[str]] = None
    AcceleratorNames: Optional[List[str]] = None
    AcceleratorTotalMemoryMiB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails] = None
    AcceleratorTypes: Optional[List[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[List[str]] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[List[str]] = None
    MemoryGiBPerVCpu: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails] = None
    MemoryMiB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails] = None
    NetworkInterfaceCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails] = None
    VCpuCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutput(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails]] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails]] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails]] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails]] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None


class AwsEc2NetworkAclEntry(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Egress: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCode] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeFromTo] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    RuleNumber: Optional[int] = None


class AwsEc2NetworkInterfaceDetailsOutput(BaseValidatorModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachment] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[List[AwsEc2NetworkInterfaceSecurityGroup]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[List[AwsEc2NetworkInterfaceIpV6AddressDetail]] = None
    PrivateIpAddresses: Optional[List[AwsEc2NetworkInterfacePrivateIpAddressDetail]] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None


class AwsEc2NetworkInterfaceDetails(BaseValidatorModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachment] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[List[AwsEc2NetworkInterfaceSecurityGroup]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[List[AwsEc2NetworkInterfaceIpV6AddressDetail]] = None
    PrivateIpAddresses: Optional[List[AwsEc2NetworkInterfacePrivateIpAddressDetail]] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None


class AwsEc2SecurityGroupIpPermissionOutput(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[AwsEc2SecurityGroupUserIdGroupPair]] = None
    IpRanges: Optional[List[AwsEc2SecurityGroupIpRange]] = None
    Ipv6Ranges: Optional[List[AwsEc2SecurityGroupIpv6Range]] = None
    PrefixListIds: Optional[List[AwsEc2SecurityGroupPrefixListId]] = None


class AwsEc2SecurityGroupIpPermission(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[AwsEc2SecurityGroupUserIdGroupPair]] = None
    IpRanges: Optional[List[AwsEc2SecurityGroupIpRange]] = None
    Ipv6Ranges: Optional[List[AwsEc2SecurityGroupIpv6Range]] = None
    PrefixListIds: Optional[List[AwsEc2SecurityGroupPrefixListId]] = None


class AwsEc2SubnetDetailsOutput(BaseValidatorModel):
    AssignIpv6AddressOnCreation: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    AvailableIpAddressCount: Optional[int] = None
    CidrBlock: Optional[str] = None
    DefaultForAz: Optional[bool] = None
    MapPublicIpOnLaunch: Optional[bool] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    SubnetArn: Optional[str] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociation]] = None


class AwsEc2SubnetDetails(BaseValidatorModel):
    AssignIpv6AddressOnCreation: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    AvailableIpAddressCount: Optional[int] = None
    CidrBlock: Optional[str] = None
    DefaultForAz: Optional[bool] = None
    MapPublicIpOnLaunch: Optional[bool] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    SubnetArn: Optional[str] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociation]] = None

AwsEc2TransitGatewayDetailsUnion = Union[AwsEc2TransitGatewayDetails, AwsEc2TransitGatewayDetailsOutput]


class AwsEc2VolumeDetailsOutput(BaseValidatorModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[List[AwsEc2VolumeAttachment]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None


class AwsEc2VolumeDetails(BaseValidatorModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[List[AwsEc2VolumeAttachment]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None


class AwsEc2VpcDetailsOutput(BaseValidatorModel):
    CidrBlockAssociationSet: Optional[List[CidrBlockAssociation]] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociation]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None


class AwsEc2VpcDetails(BaseValidatorModel):
    CidrBlockAssociationSet: Optional[List[CidrBlockAssociation]] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociation]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None


class AwsEc2VpcEndpointServiceDetailsOutput(BaseValidatorModel):
    AcceptanceRequired: Optional[bool] = None
    AvailabilityZones: Optional[List[str]] = None
    BaseEndpointDnsNames: Optional[List[str]] = None
    ManagesVpcEndpoints: Optional[bool] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    PrivateDnsName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceState: Optional[str] = None
    ServiceType: Optional[List[AwsEc2VpcEndpointServiceServiceTypeDetails]] = None


class AwsEc2VpcEndpointServiceDetails(BaseValidatorModel):
    AcceptanceRequired: Optional[bool] = None
    AvailabilityZones: Optional[List[str]] = None
    BaseEndpointDnsNames: Optional[List[str]] = None
    ManagesVpcEndpoints: Optional[bool] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    PrivateDnsName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceState: Optional[str] = None
    ServiceType: Optional[List[AwsEc2VpcEndpointServiceServiceTypeDetails]] = None


class AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[List[VpcInfoCidrBlockSetDetails]] = None
    Ipv6CidrBlockSet: Optional[List[VpcInfoIpv6CidrBlockSetDetails]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetails] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None


class AwsEc2VpcPeeringConnectionVpcInfoDetails(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[List[VpcInfoCidrBlockSetDetails]] = None
    Ipv6CidrBlockSet: Optional[List[VpcInfoIpv6CidrBlockSetDetails]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetails] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None


class AwsEc2VpnConnectionOptionsDetailsOutput(BaseValidatorModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutput]] = None

AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnion = Union[AwsEc2VpnConnectionOptionsTunnelOptionsDetails, AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutput]

AwsEcrContainerImageDetailsUnion = Union[AwsEcrContainerImageDetails, AwsEcrContainerImageDetailsOutput]


class AwsEcrRepositoryDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    ImageScanningConfiguration: Optional[AwsEcrRepositoryImageScanningConfigurationDetails] = None
    ImageTagMutability: Optional[str] = None
    LifecyclePolicy: Optional[AwsEcrRepositoryLifecyclePolicyDetails] = None
    RepositoryName: Optional[str] = None
    RepositoryPolicyText: Optional[str] = None


class AwsEcsClusterConfigurationExecuteCommandConfigurationDetails(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    LogConfiguration: Optional[AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails] = None
    Logging: Optional[str] = None


class AwsEcsContainerDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[List[AwsMountPoint]] = None
    Privileged: Optional[bool] = None


class AwsEcsContainerDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[List[AwsMountPoint]] = None
    Privileged: Optional[bool] = None


class AwsEcsServiceDeploymentConfigurationDetails(BaseValidatorModel):
    DeploymentCircuitBreaker: Optional[AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails] = None
    MaximumPercent: Optional[int] = None
    MinimumHealthyPercent: Optional[int] = None


class AwsEcsServiceNetworkConfigurationDetailsOutput(BaseValidatorModel):
    AwsVpcConfiguration: Optional[AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutput] = None

AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnion = Union[AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails, AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutput]

AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails, AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutput]

AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails, AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutput]

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails, AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutput]


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutput(BaseValidatorModel):
    Capabilities: Optional[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutput] = None
    Devices: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutput]] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutput]] = None

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails, AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutput]

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails, AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutput]


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutput(BaseValidatorModel):
    LogDriver: Optional[str] = None
    Options: Optional[Dict[str, str]] = None
    SecretOptions: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails(BaseValidatorModel):
    LogDriver: Optional[str] = None
    Options: Optional[Dict[str, str]] = None
    SecretOptions: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails]] = None


class AwsEcsTaskDefinitionProxyConfigurationDetailsOutput(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails]] = None
    Type: Optional[str] = None


class AwsEcsTaskDefinitionProxyConfigurationDetails(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails]] = None
    Type: Optional[str] = None

AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnion = Union[AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails, AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutput]


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails(BaseValidatorModel):
    AuthorizationConfig: Optional[AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails] = None
    FilesystemId: Optional[str] = None
    RootDirectory: Optional[str] = None
    TransitEncryption: Optional[str] = None
    TransitEncryptionPort: Optional[int] = None


class AwsEcsTaskVolumeDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Host: Optional[AwsEcsTaskVolumeHostDetails] = None

AwsEfsAccessPointPosixUserDetailsUnion = Union[AwsEfsAccessPointPosixUserDetails, AwsEfsAccessPointPosixUserDetailsOutput]


class AwsEfsAccessPointRootDirectoryDetails(BaseValidatorModel):
    CreationInfo: Optional[AwsEfsAccessPointRootDirectoryCreationInfoDetails] = None
    Path: Optional[str] = None


class AwsEksClusterLoggingDetailsOutput(BaseValidatorModel):
    ClusterLogging: Optional[List[AwsEksClusterLoggingClusterLoggingDetailsOutput]] = None

AwsEksClusterLoggingClusterLoggingDetailsUnion = Union[AwsEksClusterLoggingClusterLoggingDetails, AwsEksClusterLoggingClusterLoggingDetailsOutput]

AwsEksClusterResourcesVpcConfigDetailsUnion = Union[AwsEksClusterResourcesVpcConfigDetails, AwsEksClusterResourcesVpcConfigDetailsOutput]


class AwsElasticBeanstalkEnvironmentDetailsOutput(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[List[AwsElasticBeanstalkEnvironmentEnvironmentLink]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[AwsElasticBeanstalkEnvironmentOptionSetting]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTier] = None
    VersionLabel: Optional[str] = None


class AwsElasticBeanstalkEnvironmentDetails(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[List[AwsElasticBeanstalkEnvironmentEnvironmentLink]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[AwsElasticBeanstalkEnvironmentOptionSetting]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTier] = None
    VersionLabel: Optional[str] = None


class AwsElasticsearchDomainElasticsearchClusterConfigDetails(BaseValidatorModel):
    DedicatedMasterCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[str] = None
    ZoneAwarenessConfig: Optional[AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails] = None
    ZoneAwarenessEnabled: Optional[bool] = None


class AwsElasticsearchDomainLogPublishingOptions(BaseValidatorModel):
    IndexSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfig] = None
    SearchSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfig] = None
    AuditLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfig] = None

AwsElasticsearchDomainVPCOptionsUnion = Union[AwsElasticsearchDomainVPCOptions, AwsElasticsearchDomainVPCOptionsOutput]


class AwsElbLoadBalancerPoliciesOutput(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[List[AwsElbAppCookieStickinessPolicy]] = None
    LbCookieStickinessPolicies: Optional[List[AwsElbLbCookieStickinessPolicy]] = None
    OtherPolicies: Optional[List[str]] = None


class AwsElbLoadBalancerPolicies(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[List[AwsElbAppCookieStickinessPolicy]] = None
    LbCookieStickinessPolicies: Optional[List[AwsElbLbCookieStickinessPolicy]] = None
    OtherPolicies: Optional[List[str]] = None


class AwsElbLoadBalancerAttributesOutput(BaseValidatorModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLog] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDraining] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettings] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancing] = None
    AdditionalAttributes: Optional[List[AwsElbLoadBalancerAdditionalAttribute]] = None


class AwsElbLoadBalancerAttributes(BaseValidatorModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLog] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDraining] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettings] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancing] = None
    AdditionalAttributes: Optional[List[AwsElbLoadBalancerAdditionalAttribute]] = None

AwsElbLoadBalancerBackendServerDescriptionUnion = Union[AwsElbLoadBalancerBackendServerDescription, AwsElbLoadBalancerBackendServerDescriptionOutput]


class AwsElbLoadBalancerListenerDescriptionOutput(BaseValidatorModel):
    Listener: Optional[AwsElbLoadBalancerListener] = None
    PolicyNames: Optional[List[str]] = None


class AwsElbLoadBalancerListenerDescription(BaseValidatorModel):
    Listener: Optional[AwsElbLoadBalancerListener] = None
    PolicyNames: Optional[List[str]] = None


class AwsElbv2LoadBalancerDetailsOutput(BaseValidatorModel):
    AvailabilityZones: Optional[List[AvailabilityZone]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    State: Optional[LoadBalancerState] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[List[AwsElbv2LoadBalancerAttribute]] = None


class AwsElbv2LoadBalancerDetails(BaseValidatorModel):
    AvailabilityZones: Optional[List[AvailabilityZone]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    State: Optional[LoadBalancerState] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[List[AwsElbv2LoadBalancerAttribute]] = None


class AwsEventsEndpointRoutingConfigFailoverConfigDetails(BaseValidatorModel):
    Primary: Optional[AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails] = None
    Secondary: Optional[AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails] = None


class AwsGuardDutyDetectorDataSourcesKubernetesDetails(BaseValidatorModel):
    AuditLogs: Optional[AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails] = None


class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetails(BaseValidatorModel):
    EbsVolumes: Optional[AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetails] = None


class AwsIamAccessKeySessionContext(BaseValidatorModel):
    Attributes: Optional[AwsIamAccessKeySessionContextAttributes] = None
    SessionIssuer: Optional[AwsIamAccessKeySessionContextSessionIssuer] = None


class AwsIamGroupDetailsOutput(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[List[AwsIamGroupPolicy]] = None
    Path: Optional[str] = None


class AwsIamGroupDetails(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[List[AwsIamGroupPolicy]] = None
    Path: Optional[str] = None


class AwsIamInstanceProfileOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[List[AwsIamInstanceProfileRole]] = None


class AwsIamInstanceProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[List[AwsIamInstanceProfileRole]] = None


class AwsIamPolicyDetailsOutput(BaseValidatorModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[List[AwsIamPolicyVersion]] = None
    UpdateDate: Optional[str] = None


class AwsIamPolicyDetails(BaseValidatorModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[List[AwsIamPolicyVersion]] = None
    UpdateDate: Optional[str] = None


class AwsIamUserDetailsOutput(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[List[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[List[AwsIamUserPolicy]] = None


class AwsIamUserDetails(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[List[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[List[AwsIamUserPolicy]] = None


class AwsKinesisStreamDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    StreamEncryption: Optional[AwsKinesisStreamStreamEncryptionDetails] = None
    ShardCount: Optional[int] = None
    RetentionPeriodHours: Optional[int] = None


class AwsLambdaFunctionEnvironmentOutput(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentError] = None


class AwsLambdaFunctionEnvironment(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentError] = None

AwsLambdaFunctionVpcConfigUnion = Union[AwsLambdaFunctionVpcConfig, AwsLambdaFunctionVpcConfigOutput]

AwsLambdaLayerVersionDetailsUnion = Union[AwsLambdaLayerVersionDetails, AwsLambdaLayerVersionDetailsOutput]


class AwsMskClusterClusterInfoClientAuthenticationSaslDetails(BaseValidatorModel):
    Iam: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails] = None
    Scram: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails] = None

AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnion = Union[AwsMskClusterClusterInfoClientAuthenticationTlsDetails, AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutput]


class AwsMskClusterClusterInfoEncryptionInfoDetails(BaseValidatorModel):
    EncryptionInTransit: Optional[AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails] = None
    EncryptionAtRest: Optional[AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails] = None


class AwsNetworkFirewallFirewallDetailsOutput(BaseValidatorModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[List[AwsNetworkFirewallFirewallSubnetMappingsDetails]] = None
    VpcId: Optional[str] = None


class AwsNetworkFirewallFirewallDetails(BaseValidatorModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[List[AwsNetworkFirewallFirewallSubnetMappingsDetails]] = None
    VpcId: Optional[str] = None


class AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[AwsOpenSearchServiceDomainMasterUserOptionsDetails] = None


class AwsOpenSearchServiceDomainClusterConfigDetails(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails] = None
    DedicatedMasterCount: Optional[int] = None
    InstanceType: Optional[str] = None
    WarmType: Optional[str] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None


class AwsOpenSearchServiceDomainLogPublishingOptionsDetails(BaseValidatorModel):
    IndexSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOption] = None
    SearchSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOption] = None
    AuditLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOption] = None

AwsOpenSearchServiceDomainVpcOptionsDetailsUnion = Union[AwsOpenSearchServiceDomainVpcOptionsDetails, AwsOpenSearchServiceDomainVpcOptionsDetailsOutput]


class AwsRdsDbClusterDetailsOutput(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    DatabaseName: Optional[str] = None
    Status: Optional[str] = None
    Endpoint: Optional[str] = None
    ReaderEndpoint: Optional[str] = None
    CustomEndpoints: Optional[List[str]] = None
    MultiAz: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReadReplicaIdentifiers: Optional[List[str]] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroup]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[List[AwsRdsDbClusterAssociatedRole]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembership]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[List[AwsRdsDbClusterOptionGroupMembership]] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[List[AwsRdsDbClusterMember]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None


class AwsRdsDbClusterDetails(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    DatabaseName: Optional[str] = None
    Status: Optional[str] = None
    Endpoint: Optional[str] = None
    ReaderEndpoint: Optional[str] = None
    CustomEndpoints: Optional[List[str]] = None
    MultiAz: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReadReplicaIdentifiers: Optional[List[str]] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroup]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[List[AwsRdsDbClusterAssociatedRole]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembership]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[List[AwsRdsDbClusterOptionGroupMembership]] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[List[AwsRdsDbClusterMember]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None


class AwsRdsDbClusterSnapshotDetailsOutput(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    PercentProgress: Optional[int] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterSnapshotIdentifier: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    DbClusterSnapshotAttributes: Optional[List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutput]] = None

AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnion = Union[AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute, AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutput]


class AwsRdsDbSnapshotDetailsOutput(BaseValidatorModel):
    DbSnapshotIdentifier: Optional[str] = None
    DbInstanceIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    VpcId: Optional[str] = None
    InstanceCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    PercentProgress: Optional[int] = None
    SourceRegion: Optional[str] = None
    SourceDbSnapshotIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    Timezone: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None
    DbiResourceId: Optional[str] = None


class AwsRdsDbSnapshotDetails(BaseValidatorModel):
    DbSnapshotIdentifier: Optional[str] = None
    DbInstanceIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    VpcId: Optional[str] = None
    InstanceCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    PercentProgress: Optional[int] = None
    SourceRegion: Optional[str] = None
    SourceDbSnapshotIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    Timezone: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None
    DbiResourceId: Optional[str] = None


class AwsRdsDbPendingModifiedValuesOutput(BaseValidatorModel):
    DbInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    Port: Optional[int] = None
    BackupRetentionPeriod: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    CaCertificateIdentifier: Optional[str] = None
    DbSubnetGroupName: Optional[str] = None
    PendingCloudWatchLogsExports: Optional[AwsRdsPendingCloudWatchLogsExportsOutput] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None


class AwsRdsDbSecurityGroupDetailsOutput(BaseValidatorModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[List[AwsRdsDbSecurityGroupEc2SecurityGroup]] = None
    IpRanges: Optional[List[AwsRdsDbSecurityGroupIpRange]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None


class AwsRdsDbSecurityGroupDetails(BaseValidatorModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[List[AwsRdsDbSecurityGroupEc2SecurityGroup]] = None
    IpRanges: Optional[List[AwsRdsDbSecurityGroupIpRange]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None


class AwsRdsDbSubnetGroupSubnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AwsRdsDbSubnetGroupSubnetAvailabilityZone] = None
    SubnetStatus: Optional[str] = None

AwsRdsEventSubscriptionDetailsUnion = Union[AwsRdsEventSubscriptionDetails, AwsRdsEventSubscriptionDetailsOutput]

AwsRdsPendingCloudWatchLogsExportsUnion = Union[AwsRdsPendingCloudWatchLogsExports, AwsRdsPendingCloudWatchLogsExportsOutput]


class AwsRedshiftClusterClusterParameterGroupOutput(BaseValidatorModel):
    ClusterParameterStatusList: Optional[List[AwsRedshiftClusterClusterParameterStatus]] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None


class AwsRedshiftClusterClusterParameterGroup(BaseValidatorModel):
    ClusterParameterStatusList: Optional[List[AwsRedshiftClusterClusterParameterStatus]] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None


class AwsRoute53HostedZoneObjectDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[AwsRoute53HostedZoneConfigDetails] = None


class AwsRoute53QueryLoggingConfigDetails(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[CloudWatchLogsLogGroupArnConfigDetails] = None


class AwsS3AccessPointDetails(BaseValidatorModel):
    AccessPointArn: Optional[str] = None
    Alias: Optional[str] = None
    Bucket: Optional[str] = None
    BucketAccountId: Optional[str] = None
    Name: Optional[str] = None
    NetworkOrigin: Optional[str] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    VpcConfiguration: Optional[AwsS3AccessPointVpcConfigurationDetails] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails] = None
    Type: Optional[str] = None


class AwsS3BucketNotificationConfigurationS3KeyFilterOutput(BaseValidatorModel):
    FilterRules: Optional[List[AwsS3BucketNotificationConfigurationS3KeyFilterRule]] = None


class AwsS3BucketNotificationConfigurationS3KeyFilter(BaseValidatorModel):
    FilterRules: Optional[List[AwsS3BucketNotificationConfigurationS3KeyFilterRule]] = None


class AwsS3BucketObjectLockConfigurationRuleDetails(BaseValidatorModel):
    DefaultRetention: Optional[AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails] = None


class AwsS3BucketServerSideEncryptionRule(BaseValidatorModel):
    ApplyServerSideEncryptionByDefault: Optional[AwsS3BucketServerSideEncryptionByDefault] = None


class AwsS3BucketWebsiteConfigurationRoutingRule(BaseValidatorModel):
    Condition: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleCondition] = None
    Redirect: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleRedirect] = None


class AwsSageMakerNotebookInstanceDetailsOutput(BaseValidatorModel):
    AcceleratorTypes: Optional[List[str]] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails] = None
    InstanceType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NotebookInstanceArn: Optional[str] = None
    NotebookInstanceLifecycleConfigName: Optional[str] = None
    NotebookInstanceName: Optional[str] = None
    NotebookInstanceStatus: Optional[str] = None
    PlatformIdentifier: Optional[str] = None
    RoleArn: Optional[str] = None
    RootAccess: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SubnetId: Optional[str] = None
    Url: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None


class AwsSageMakerNotebookInstanceDetails(BaseValidatorModel):
    AcceleratorTypes: Optional[List[str]] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails] = None
    InstanceType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NotebookInstanceArn: Optional[str] = None
    NotebookInstanceLifecycleConfigName: Optional[str] = None
    NotebookInstanceName: Optional[str] = None
    NotebookInstanceStatus: Optional[str] = None
    PlatformIdentifier: Optional[str] = None
    RoleArn: Optional[str] = None
    RootAccess: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SubnetId: Optional[str] = None
    Url: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None


class AwsSecretsManagerSecretDetails(BaseValidatorModel):
    RotationRules: Optional[AwsSecretsManagerSecretRotationRules] = None
    RotationOccurredWithinFrequency: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    RotationEnabled: Optional[bool] = None
    RotationLambdaArn: Optional[str] = None
    Deleted: Optional[bool] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


class BatchUpdateFindingsRequest(BaseValidatorModel):
    FindingIdentifiers: List[AwsSecurityFindingIdentifier]
    Note: Optional[NoteUpdate] = None
    Severity: Optional[SeverityUpdate] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[List[str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Workflow: Optional[WorkflowUpdate] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None


class BatchUpdateFindingsUnprocessedFinding(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifier
    ErrorCode: str
    ErrorMessage: str


class AwsSnsTopicDetailsOutput(BaseValidatorModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[List[AwsSnsTopicSubscription]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None


class AwsSnsTopicDetails(BaseValidatorModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[List[AwsSnsTopicSubscription]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None


class AwsSsmPatch(BaseValidatorModel):
    ComplianceSummary: Optional[AwsSsmComplianceSummary] = None


class AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails(BaseValidatorModel):
    CloudWatchLogsLogGroup: Optional[AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails] = None


class AwsWafRateBasedRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRateBasedRuleMatchPredicate]] = None


class AwsWafRateBasedRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRateBasedRuleMatchPredicate]] = None


class AwsWafRegionalRateBasedRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRegionalRateBasedRuleMatchPredicate]] = None


class AwsWafRegionalRateBasedRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRegionalRateBasedRuleMatchPredicate]] = None


class AwsWafRegionalRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRegionalRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafRegionalRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRegionalRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafRegionalRuleGroupRulesDetails(BaseValidatorModel):
    Action: Optional[AwsWafRegionalRuleGroupRulesActionDetails] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None


class AwsWafRegionalWebAclRulesListDetails(BaseValidatorModel):
    Action: Optional[AwsWafRegionalWebAclRulesListActionDetails] = None
    OverrideAction: Optional[AwsWafRegionalWebAclRulesListOverrideActionDetails] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None


class AwsWafRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafRuleGroupRulesDetails(BaseValidatorModel):
    Action: Optional[AwsWafRuleGroupRulesActionDetails] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None


class AwsWafWebAclRuleOutput(BaseValidatorModel):
    Action: Optional[WafAction] = None
    ExcludedRules: Optional[List[WafExcludedRule]] = None
    OverrideAction: Optional[WafOverrideAction] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None


class AwsWafWebAclRule(BaseValidatorModel):
    Action: Optional[WafAction] = None
    ExcludedRules: Optional[List[WafExcludedRule]] = None
    OverrideAction: Optional[WafOverrideAction] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None


class AwsWafv2CustomRequestHandlingDetailsOutput(BaseValidatorModel):
    InsertHeaders: Optional[List[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2CustomRequestHandlingDetails(BaseValidatorModel):
    InsertHeaders: Optional[List[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2CustomResponseDetailsOutput(BaseValidatorModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[List[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2CustomResponseDetails(BaseValidatorModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[List[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2WebAclCaptchaConfigDetails(BaseValidatorModel):
    ImmunityTimeProperty: Optional[AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails] = None


class CreateActionTargetResponse(BaseValidatorModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadata


class CreateAutomationRuleResponse(BaseValidatorModel):
    RuleArn: str
    ResponseMetadata: ResponseMetadata


class CreateFindingAggregatorResponse(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadata


class CreateInsightResponse(BaseValidatorModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadata


class DeleteActionTargetResponse(BaseValidatorModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadata


class DeleteInsightResponse(BaseValidatorModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadata


class DescribeActionTargetsResponse(BaseValidatorModel):
    ActionTargets: List[ActionTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeHubResponse(BaseValidatorModel):
    HubArn: str
    SubscribedAt: str
    AutoEnableControls: bool
    ControlFindingGenerator: ControlFindingGeneratorType
    ResponseMetadata: ResponseMetadata


class EnableImportFindingsForProductResponse(BaseValidatorModel):
    ProductSubscriptionArn: str
    ResponseMetadata: ResponseMetadata


class GetConfigurationPolicyAssociationResponse(BaseValidatorModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadata


class GetFindingAggregatorResponse(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadata


class GetInvitationsCountResponse(BaseValidatorModel):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadata


class ListAutomationRulesResponse(BaseValidatorModel):
    AutomationRulesMetadata: List[AutomationRulesMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEnabledProductsForImportResponse(BaseValidatorModel):
    ProductSubscriptions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOrganizationAdminAccountsResponse(BaseValidatorModel):
    AdminAccounts: List[AdminAccount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartConfigurationPolicyAssociationResponse(BaseValidatorModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadata


class UpdateFindingAggregatorResponse(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadata


class BatchDeleteAutomationRulesResponse(BaseValidatorModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRule]
    ResponseMetadata: ResponseMetadata


class BatchUpdateAutomationRulesResponse(BaseValidatorModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRule]
    ResponseMetadata: ResponseMetadata


class BatchEnableStandardsRequest(BaseValidatorModel):
    StandardsSubscriptionRequests: List[StandardsSubscriptionRequest]


class ListConfigurationPolicyAssociationsResponse(BaseValidatorModel):
    ConfigurationPolicyAssociationSummaries: List[ConfigurationPolicyAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetStandardsControlAssociationsRequest(BaseValidatorModel):
    StandardsControlAssociationIds: List[StandardsControlAssociationId]


class UnprocessedStandardsControlAssociation(BaseValidatorModel):
    StandardsControlAssociationId: StandardsControlAssociationId
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None


class BatchImportFindingsResponse(BaseValidatorModel):
    FailedCount: int
    SuccessCount: int
    FailedFindings: List[ImportFindingsError]
    ResponseMetadata: ResponseMetadata


class BatchUpdateStandardsControlAssociationsRequest(BaseValidatorModel):
    StandardsControlAssociationUpdates: List[StandardsControlAssociationUpdate]


class UnprocessedStandardsControlAssociationUpdate(BaseValidatorModel):
    StandardsControlAssociationUpdate: StandardsControlAssociationUpdate
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None


class VulnerabilityCodeVulnerabilitiesOutput(BaseValidatorModel):
    Cwes: Optional[List[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePath] = None
    SourceArn: Optional[str] = None


class VulnerabilityCodeVulnerabilities(BaseValidatorModel):
    Cwes: Optional[List[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePath] = None
    SourceArn: Optional[str] = None


class ComplianceOutput(BaseValidatorModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[List[str]] = None
    StatusReasons: Optional[List[StatusReason]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[List[AssociatedStandard]] = None
    SecurityControlParameters: Optional[List[SecurityControlParameterOutput]] = None


class ConfigurationOptions(BaseValidatorModel):
    Integer: Optional[IntegerConfigurationOptions] = None
    IntegerList: Optional[IntegerListConfigurationOptions] = None
    Double: Optional[DoubleConfigurationOptions] = None
    String: Optional[StringConfigurationOptions] = None
    StringList: Optional[StringListConfigurationOptions] = None
    Boolean: Optional[BooleanConfigurationOptions] = None
    Enum: Optional[EnumConfigurationOptions] = None
    EnumList: Optional[EnumListConfigurationOptions] = None


class ConfigurationPolicyAssociation(BaseValidatorModel):
    Target: Optional[Target] = None


class GetConfigurationPolicyAssociationRequest(BaseValidatorModel):
    Target: Target


class StartConfigurationPolicyAssociationRequest(BaseValidatorModel):
    ConfigurationPolicyIdentifier: str
    Target: Target


class StartConfigurationPolicyDisassociationRequest(BaseValidatorModel):
    ConfigurationPolicyIdentifier: str
    Target: Optional[Target] = None


class ListConfigurationPoliciesResponse(BaseValidatorModel):
    ConfigurationPolicySummaries: List[ConfigurationPolicySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ContainerDetailsOutput(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMount]] = None
    Privileged: Optional[bool] = None


class ContainerDetails(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMount]] = None
    Privileged: Optional[bool] = None


class CreateMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DeclineInvitationsResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DeleteInvitationsResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DeleteMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class InviteMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DateFilter(BaseValidatorModel):
    Start: Optional[str] = None
    End: Optional[str] = None
    DateRange: Optional[DateRange] = None


class DescribeActionTargetsRequestPaginate(BaseValidatorModel):
    ActionTargetArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeProductsRequestPaginate(BaseValidatorModel):
    ProductArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStandardsControlsRequestPaginate(BaseValidatorModel):
    StandardsSubscriptionArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStandardsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetEnabledStandardsRequestPaginate(BaseValidatorModel):
    StandardsSubscriptionArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetInsightsRequestPaginate(BaseValidatorModel):
    InsightArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationPolicyAssociationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[AssociationFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnabledProductsForImportRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingAggregatorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvitationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersRequestPaginate(BaseValidatorModel):
    OnlyAssociated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationAdminAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityControlDefinitionsRequestPaginate(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStandardsControlAssociationsRequestPaginate(BaseValidatorModel):
    SecurityControlId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrganizationConfigurationResponse(BaseValidatorModel):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    AutoEnableStandards: AutoEnableStandardsType
    OrganizationConfiguration: OrganizationConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateOrganizationConfigurationRequest(BaseValidatorModel):
    AutoEnable: bool
    AutoEnableStandards: Optional[AutoEnableStandardsType] = None
    OrganizationConfiguration: Optional[OrganizationConfiguration] = None


class DescribeProductsResponse(BaseValidatorModel):
    Products: List[Product]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeStandardsControlsResponse(BaseValidatorModel):
    Controls: List[StandardsControl]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ThreatOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[FilePaths]] = None


class Threat(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[FilePaths]] = None


class ListFindingAggregatorsResponse(BaseValidatorModel):
    FindingAggregators: List[FindingAggregator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FindingHistoryRecord(BaseValidatorModel):
    FindingIdentifier: Optional[AwsSecurityFindingIdentifier] = None
    UpdateTime: Optional[datetime] = None
    FindingCreated: Optional[bool] = None
    UpdateSource: Optional[FindingHistoryUpdateSource] = None
    Updates: Optional[List[FindingHistoryUpdate]] = None
    NextToken: Optional[str] = None


class FindingProviderFieldsOutput(BaseValidatorModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None
    Severity: Optional[FindingProviderSeverity] = None
    Types: Optional[List[str]] = None


class FindingProviderFields(BaseValidatorModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None
    Severity: Optional[FindingProviderSeverity] = None
    Types: Optional[List[str]] = None

GeneratorDetailsUnion = Union[GeneratorDetails, GeneratorDetailsOutput]


class GetAdministratorAccountResponse(BaseValidatorModel):
    Administrator: Invitation
    ResponseMetadata: ResponseMetadata


class GetMasterAccountResponse(BaseValidatorModel):
    Master: Invitation
    ResponseMetadata: ResponseMetadata


class ListInvitationsResponse(BaseValidatorModel):
    Invitations: List[Invitation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetFindingHistoryRequestPaginate(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifier
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetFindingHistoryRequest(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifier
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMembersResponse(BaseValidatorModel):
    Members: List[Member]
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class ListMembersResponse(BaseValidatorModel):
    Members: List[Member]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SignalOutput(BaseValidatorModel):
    Type: Optional[str] = None
    Id: Optional[str] = None
    Title: Optional[str] = None
    ProductArn: Optional[str] = None
    ResourceIds: Optional[List[str]] = None
    SignalIndicators: Optional[List[IndicatorOutput]] = None
    Name: Optional[str] = None
    CreatedAt: Optional[int] = None
    UpdatedAt: Optional[int] = None
    FirstSeenAt: Optional[int] = None
    LastSeenAt: Optional[int] = None
    Severity: Optional[float] = None
    Count: Optional[int] = None
    ActorIds: Optional[List[str]] = None
    EndpointIds: Optional[List[str]] = None

IndicatorUnion = Union[Indicator, IndicatorOutput]


class Signal(BaseValidatorModel):
    Type: Optional[str] = None
    Id: Optional[str] = None
    Title: Optional[str] = None
    ProductArn: Optional[str] = None
    ResourceIds: Optional[List[str]] = None
    SignalIndicators: Optional[List[Indicator]] = None
    Name: Optional[str] = None
    CreatedAt: Optional[int] = None
    UpdatedAt: Optional[int] = None
    FirstSeenAt: Optional[int] = None
    LastSeenAt: Optional[int] = None
    Severity: Optional[float] = None
    Count: Optional[int] = None
    ActorIds: Optional[List[str]] = None
    EndpointIds: Optional[List[str]] = None


class InsightResults(BaseValidatorModel):
    InsightArn: str
    GroupByAttribute: str
    ResultValues: List[InsightResultValue]


class ListStandardsControlAssociationsResponse(BaseValidatorModel):
    StandardsControlAssociationSummaries: List[StandardsControlAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NetworkEndpoint(BaseValidatorModel):
    Id: Optional[str] = None
    Ip: Optional[str] = None
    Domain: Optional[str] = None
    Port: Optional[int] = None
    Location: Optional[NetworkGeoLocation] = None
    AutonomousSystem: Optional[NetworkAutonomousSystem] = None
    Connection: Optional[NetworkConnection] = None


class NetworkPathComponentDetailsOutput(BaseValidatorModel):
    Address: Optional[List[str]] = None
    PortRanges: Optional[List[PortRange]] = None


class NetworkPathComponentDetails(BaseValidatorModel):
    Address: Optional[List[str]] = None
    PortRanges: Optional[List[PortRange]] = None


class Network(BaseValidatorModel):
    Direction: Optional[NetworkDirectionType] = None
    Protocol: Optional[str] = None
    OpenPortRange: Optional[PortRange] = None
    SourceIpV4: Optional[str] = None
    SourceIpV6: Optional[str] = None
    SourcePort: Optional[int] = None
    SourceDomain: Optional[str] = None
    SourceMac: Optional[str] = None
    DestinationIpV4: Optional[str] = None
    DestinationIpV6: Optional[str] = None
    DestinationPort: Optional[int] = None
    DestinationDomain: Optional[str] = None


class Page(BaseValidatorModel):
    PageNumber: Optional[int] = None
    LineRange: Optional[Range] = None
    OffsetRange: Optional[Range] = None


class ParameterConfigurationOutput(BaseValidatorModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueOutput] = None

ParameterValueUnion = Union[ParameterValue, ParameterValueOutput]


class Remediation(BaseValidatorModel):
    Recommendation: Optional[Recommendation] = None

RuleGroupSourceListDetailsUnion = Union[RuleGroupSourceListDetails, RuleGroupSourceListDetailsOutput]


class RuleGroupSourceStatefulRulesDetailsOutput(BaseValidatorModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetails] = None
    RuleOptions: Optional[List[RuleGroupSourceStatefulRulesOptionsDetailsOutput]] = None

RuleGroupSourceStatefulRulesOptionsDetailsUnion = Union[RuleGroupSourceStatefulRulesOptionsDetails, RuleGroupSourceStatefulRulesOptionsDetailsOutput]


class RuleGroupSourceStatelessRuleMatchAttributesOutput(BaseValidatorModel):
    DestinationPorts: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts]] = None
    Destinations: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesDestinations]] = None
    Protocols: Optional[List[int]] = None
    SourcePorts: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSourcePorts]] = None
    Sources: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSources]] = None
    TcpFlags: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutput]] = None

RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnion = Union[RuleGroupSourceStatelessRuleMatchAttributesTcpFlags, RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutput]

RuleGroupVariablesIpSetsDetailsUnion = Union[RuleGroupVariablesIpSetsDetails, RuleGroupVariablesIpSetsDetailsOutput]


class RuleGroupVariablesOutput(BaseValidatorModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsOutput] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsOutput] = None

RuleGroupVariablesPortSetsDetailsUnion = Union[RuleGroupVariablesPortSetsDetails, RuleGroupVariablesPortSetsDetailsOutput]

SecurityControlParameterUnion = Union[SecurityControlParameter, SecurityControlParameterOutput]


class Standard(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EnabledByDefault: Optional[bool] = None
    StandardsManagedBy: Optional[StandardsManagedBy] = None


class StandardsSubscription(BaseValidatorModel):
    StandardsSubscriptionArn: str
    StandardsArn: str
    StandardsInput: Dict[str, str]
    StandardsStatus: StandardsStatusType
    StandardsControlsUpdatable: Optional[StandardsControlsUpdatableType] = None
    StandardsStatusReason: Optional[StandardsStatusReason] = None


class StatelessCustomPublishMetricActionOutput(BaseValidatorModel):
    Dimensions: Optional[List[StatelessCustomPublishMetricActionDimension]] = None


class StatelessCustomPublishMetricAction(BaseValidatorModel):
    Dimensions: Optional[List[StatelessCustomPublishMetricActionDimension]] = None


class AwsApiCallActionOutput(BaseValidatorModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetails] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetails] = None
    AffectedResources: Optional[Dict[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None


class AwsApiCallAction(BaseValidatorModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetails] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetails] = None
    AffectedResources: Optional[Dict[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None


class NetworkConnectionAction(BaseValidatorModel):
    ConnectionDirection: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetails] = None
    RemotePortDetails: Optional[ActionRemotePortDetails] = None
    LocalPortDetails: Optional[ActionLocalPortDetails] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None


class PortProbeDetail(BaseValidatorModel):
    LocalPortDetails: Optional[ActionLocalPortDetails] = None
    LocalIpDetails: Optional[ActionLocalIpDetails] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetails] = None


class Actor(BaseValidatorModel):
    Id: Optional[str] = None
    User: Optional[ActorUser] = None
    Session: Optional[ActorSession] = None

CvssUnion = Union[Cvss, CvssOutput]


class AwsEc2RouteTableDetailsOutput(BaseValidatorModel):
    AssociationSet: Optional[List[AssociationSetDetails]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[List[PropagatingVgwSetDetails]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[List[RouteSetDetails]] = None
    VpcId: Optional[str] = None


class AwsEc2RouteTableDetails(BaseValidatorModel):
    AssociationSet: Optional[List[AssociationSetDetails]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[List[PropagatingVgwSetDetails]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[List[RouteSetDetails]] = None
    VpcId: Optional[str] = None


class AutomationRulesActionOutput(BaseValidatorModel):
    Type: Optional[Literal['FINDING_FIELDS_UPDATE']] = None
    FindingFieldsUpdate: Optional[AutomationRulesFindingFieldsUpdateOutput] = None

AutomationRulesFindingFieldsUpdateUnion = Union[AutomationRulesFindingFieldsUpdate, AutomationRulesFindingFieldsUpdateOutput]


class AwsAmazonMqBrokerDetailsOutput(BaseValidatorModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetails] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsOutput] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetails] = None
    MaintenanceWindowStartTime: Optional[AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    Users: Optional[List[AwsAmazonMqBrokerUsersDetails]] = None


class AwsAmazonMqBrokerDetails(BaseValidatorModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetails] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsUnion] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetails] = None
    MaintenanceWindowStartTime: Optional[AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    Users: Optional[List[AwsAmazonMqBrokerUsersDetails]] = None


class AwsApiGatewayStageDetails(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[List[AwsApiGatewayMethodSettings]] = None
    Variables: Optional[Dict[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsUnion] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None


class AwsApiGatewayRestApiDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[List[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationUnion] = None

AwsApiGatewayV2StageDetailsUnion = Union[AwsApiGatewayV2StageDetails, AwsApiGatewayV2StageDetailsOutput]


class AwsAppSyncGraphQlApiDetailsOutput(BaseValidatorModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetails] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetails] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetails] = None
    AdditionalAuthenticationProviders: Optional[List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails]] = None
    WafWebAclArn: Optional[str] = None


class AwsAppSyncGraphQlApiDetails(BaseValidatorModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetails] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetails] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetails] = None
    AdditionalAuthenticationProviders: Optional[List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails]] = None
    WafWebAclArn: Optional[str] = None


class AwsAthenaWorkGroupConfigurationDetails(BaseValidatorModel):
    ResultConfiguration: Optional[AwsAthenaWorkGroupConfigurationResultConfigurationDetails] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutput(BaseValidatorModel):
    InstancesDistribution: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails] = None
    LaunchTemplate: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutput] = None

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnion = Union[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails, AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutput]


class AwsAutoScalingLaunchConfigurationDetailsOutput(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails]] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptions] = None


class AwsAutoScalingLaunchConfigurationDetails(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails]] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptions] = None


class AwsBackupBackupPlanRuleDetailsOutput(BaseValidatorModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[List[AwsBackupBackupPlanRuleCopyActionsDetails]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetails] = None


class AwsBackupBackupPlanRuleDetails(BaseValidatorModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[List[AwsBackupBackupPlanRuleCopyActionsDetails]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetails] = None


class AwsBackupBackupVaultDetails(BaseValidatorModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsUnion] = None
    AccessPolicy: Optional[str] = None


class AwsCertificateManagerCertificateRenewalSummaryOutput(BaseValidatorModel):
    DomainValidationOptions: Optional[List[AwsCertificateManagerCertificateDomainValidationOptionOutput]] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

AwsCertificateManagerCertificateDomainValidationOptionUnion = Union[AwsCertificateManagerCertificateDomainValidationOption, AwsCertificateManagerCertificateDomainValidationOptionOutput]


class AwsCertificateManagerCertificateRenewalSummary(BaseValidatorModel):
    DomainValidationOptions: Optional[List[AwsCertificateManagerCertificateDomainValidationOption]] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

AwsCloudFormationStackDetailsUnion = Union[AwsCloudFormationStackDetails, AwsCloudFormationStackDetailsOutput]

AwsCloudFrontDistributionCacheBehaviorsUnion = Union[AwsCloudFrontDistributionCacheBehaviors, AwsCloudFrontDistributionCacheBehaviorsOutput]


class AwsCloudFrontDistributionOriginItemOutput(BaseValidatorModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfig] = None
    CustomOriginConfig: Optional[AwsCloudFrontDistributionOriginCustomOriginConfigOutput] = None


class AwsCloudFrontDistributionOriginGroupOutput(BaseValidatorModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverOutput] = None


class AwsCloudFrontDistributionOriginGroupFailover(BaseValidatorModel):
    StatusCodes: Optional[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnion] = None


class AwsCloudFrontDistributionOriginCustomOriginConfig(BaseValidatorModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsUnion] = None

AwsCloudWatchAlarmDetailsUnion = Union[AwsCloudWatchAlarmDetails, AwsCloudWatchAlarmDetailsOutput]

AwsCodeBuildProjectEnvironmentUnion = Union[AwsCodeBuildProjectEnvironment, AwsCodeBuildProjectEnvironmentOutput]


class AwsCodeBuildProjectDetailsOutput(BaseValidatorModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[List[AwsCodeBuildProjectArtifactsDetails]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentOutput] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSource] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetails] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigOutput] = None
    SecondaryArtifacts: Optional[List[AwsCodeBuildProjectArtifactsDetails]] = None


class AwsApiGatewayV2ApiDetails(BaseValidatorModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationUnion] = None

AwsDmsReplicationInstanceDetailsUnion = Union[AwsDmsReplicationInstanceDetails, AwsDmsReplicationInstanceDetailsOutput]


class AwsDynamoDbTableGlobalSecondaryIndex(BaseValidatorModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionUnion] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None


class AwsDynamoDbTableLocalSecondaryIndex(BaseValidatorModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionUnion] = None


class AwsDynamoDbTableReplicaOutput(BaseValidatorModel):
    GlobalSecondaryIndexes: Optional[List[AwsDynamoDbTableReplicaGlobalSecondaryIndex]] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[AwsDynamoDbTableProvisionedThroughputOverride] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None


class AwsDynamoDbTableReplica(BaseValidatorModel):
    GlobalSecondaryIndexes: Optional[List[AwsDynamoDbTableReplicaGlobalSecondaryIndex]] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[AwsDynamoDbTableProvisionedThroughputOverride] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None


class AwsEc2ClientVpnEndpointDetailsOutput(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetails]] = None
    ConnectionLogOptions: Optional[AwsEc2ClientVpnEndpointConnectionLogOptionsDetails] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsDetails] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails] = None


class AwsEc2ClientVpnEndpointDetails(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetails]] = None
    ConnectionLogOptions: Optional[AwsEc2ClientVpnEndpointConnectionLogOptionsDetails] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsDetails] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails] = None

AwsEc2InstanceDetailsUnion = Union[AwsEc2InstanceDetails, AwsEc2InstanceDetailsOutput]

AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnion = Union[AwsEc2LaunchTemplateDataInstanceRequirementsDetails, AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutput]


class AwsEc2LaunchTemplateDataDetailsOutput(BaseValidatorModel):
    BlockDeviceMappingSet: Optional[List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails]] = None
    CapacityReservationSpecification: Optional[AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetails] = None
    CreditSpecification: Optional[AwsEc2LaunchTemplateDataCreditSpecificationDetails] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails]] = None
    ElasticInferenceAcceleratorSet: Optional[List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails]] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetails] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetails] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetails] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails] = None
    InstanceRequirements: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutput] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[List[AwsEc2LaunchTemplateDataLicenseSetDetails]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetails] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetails] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetails] = None
    NetworkInterfaceSet: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutput]] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetails] = None
    PrivateDnsNameOptions: Optional[AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    SecurityGroupSet: Optional[List[str]] = None
    UserData: Optional[str] = None

AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnion = Union[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails, AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutput]


class AwsEc2NetworkAclDetailsOutput(BaseValidatorModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[List[AwsEc2NetworkAclAssociation]] = None
    Entries: Optional[List[AwsEc2NetworkAclEntry]] = None


class AwsEc2NetworkAclDetails(BaseValidatorModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[List[AwsEc2NetworkAclAssociation]] = None
    Entries: Optional[List[AwsEc2NetworkAclEntry]] = None

AwsEc2NetworkInterfaceDetailsUnion = Union[AwsEc2NetworkInterfaceDetails, AwsEc2NetworkInterfaceDetailsOutput]


class AwsEc2SecurityGroupDetailsOutput(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[List[AwsEc2SecurityGroupIpPermissionOutput]] = None
    IpPermissionsEgress: Optional[List[AwsEc2SecurityGroupIpPermissionOutput]] = None

AwsEc2SecurityGroupIpPermissionUnion = Union[AwsEc2SecurityGroupIpPermission, AwsEc2SecurityGroupIpPermissionOutput]

AwsEc2SubnetDetailsUnion = Union[AwsEc2SubnetDetails, AwsEc2SubnetDetailsOutput]

AwsEc2VolumeDetailsUnion = Union[AwsEc2VolumeDetails, AwsEc2VolumeDetailsOutput]

AwsEc2VpcDetailsUnion = Union[AwsEc2VpcDetails, AwsEc2VpcDetailsOutput]

AwsEc2VpcEndpointServiceDetailsUnion = Union[AwsEc2VpcEndpointServiceDetails, AwsEc2VpcEndpointServiceDetailsOutput]


class AwsEc2VpcPeeringConnectionDetailsOutput(BaseValidatorModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetails] = None
    VpcPeeringConnectionId: Optional[str] = None

AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion = Union[AwsEc2VpcPeeringConnectionVpcInfoDetails, AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput]


class AwsEc2VpnConnectionDetailsOutput(BaseValidatorModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[List[AwsEc2VpnConnectionVgwTelemetryDetails]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsOutput] = None
    Routes: Optional[List[AwsEc2VpnConnectionRoutesDetails]] = None
    TransitGatewayId: Optional[str] = None


class AwsEc2VpnConnectionOptionsDetails(BaseValidatorModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnion]] = None


class AwsEcsClusterConfigurationDetails(BaseValidatorModel):
    ExecuteCommandConfiguration: Optional[AwsEcsClusterConfigurationExecuteCommandConfigurationDetails] = None

AwsEcsContainerDetailsUnion = Union[AwsEcsContainerDetails, AwsEcsContainerDetailsOutput]


class AwsEcsServiceDetailsOutput(BaseValidatorModel):
    CapacityProviderStrategy: Optional[List[AwsEcsServiceCapacityProviderStrategyDetails]] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetails] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetails] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[List[AwsEcsServiceLoadBalancersDetails]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[AwsEcsServiceNetworkConfigurationDetailsOutput] = None
    PlacementConstraints: Optional[List[AwsEcsServicePlacementConstraintsDetails]] = None
    PlacementStrategies: Optional[List[AwsEcsServicePlacementStrategiesDetails]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[List[AwsEcsServiceServiceRegistriesDetails]] = None
    TaskDefinition: Optional[str] = None


class AwsEcsServiceNetworkConfigurationDetails(BaseValidatorModel):
    AwsVpcConfiguration: Optional[AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnion] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails(BaseValidatorModel):
    Capabilities: Optional[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnion] = None
    Devices: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnion]] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnion]] = None


class AwsEcsTaskDefinitionContainerDefinitionsDetailsOutput(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails]] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[List[str]] = None
    DnsServers: Optional[List[str]] = None
    DockerLabels: Optional[Dict[str, str]] = None
    DockerSecurityOptions: Optional[List[str]] = None
    EntryPoint: Optional[List[str]] = None
    Environment: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails]] = None
    EnvironmentFiles: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails]] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails]] = None
    FirelensConfiguration: Optional[AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutput] = None
    HealthCheck: Optional[AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutput] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[List[str]] = None
    LinuxParameters: Optional[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutput] = None
    LogConfiguration: Optional[AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutput] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails]] = None
    Name: Optional[str] = None
    PortMappings: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails]] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails] = None
    ResourceRequirements: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails]] = None
    Secrets: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails]] = None
    Ulimits: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails]] = None
    WorkingDirectory: Optional[str] = None

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails, AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutput]

AwsEcsTaskDefinitionProxyConfigurationDetailsUnion = Union[AwsEcsTaskDefinitionProxyConfigurationDetails, AwsEcsTaskDefinitionProxyConfigurationDetailsOutput]


class AwsEcsTaskDefinitionVolumesDetailsOutput(BaseValidatorModel):
    DockerVolumeConfiguration: Optional[AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutput] = None
    EfsVolumeConfiguration: Optional[AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetails] = None
    Name: Optional[str] = None


class AwsEcsTaskDefinitionVolumesDetails(BaseValidatorModel):
    DockerVolumeConfiguration: Optional[AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnion] = None
    EfsVolumeConfiguration: Optional[AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetails] = None
    Name: Optional[str] = None


class AwsEcsTaskDetailsOutput(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskVolumeDetails]] = None
    Containers: Optional[List[AwsEcsContainerDetailsOutput]] = None


class AwsEfsAccessPointDetailsOutput(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsOutput] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetails] = None


class AwsEfsAccessPointDetails(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsUnion] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetails] = None


class AwsEksClusterDetailsOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsOutput] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsOutput] = None


class AwsEksClusterLoggingDetails(BaseValidatorModel):
    ClusterLogging: Optional[List[AwsEksClusterLoggingClusterLoggingDetailsUnion]] = None

AwsElasticBeanstalkEnvironmentDetailsUnion = Union[AwsElasticBeanstalkEnvironmentDetails, AwsElasticBeanstalkEnvironmentDetailsOutput]


class AwsElasticsearchDomainDetailsOutput(BaseValidatorModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptions] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[AwsElasticsearchDomainElasticsearchClusterConfigDetails] = None
    EncryptionAtRestOptions: Optional[AwsElasticsearchDomainEncryptionAtRestOptions] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptions] = None
    NodeToNodeEncryptionOptions: Optional[AwsElasticsearchDomainNodeToNodeEncryptionOptions] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptions] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsOutput] = None


class AwsElasticsearchDomainDetails(BaseValidatorModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptions] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[AwsElasticsearchDomainElasticsearchClusterConfigDetails] = None
    EncryptionAtRestOptions: Optional[AwsElasticsearchDomainEncryptionAtRestOptions] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptions] = None
    NodeToNodeEncryptionOptions: Optional[AwsElasticsearchDomainNodeToNodeEncryptionOptions] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptions] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsUnion] = None

AwsElbLoadBalancerPoliciesUnion = Union[AwsElbLoadBalancerPolicies, AwsElbLoadBalancerPoliciesOutput]

AwsElbLoadBalancerAttributesUnion = Union[AwsElbLoadBalancerAttributes, AwsElbLoadBalancerAttributesOutput]


class AwsElbLoadBalancerDetailsOutput(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    BackendServerDescriptions: Optional[List[AwsElbLoadBalancerBackendServerDescriptionOutput]] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheck] = None
    Instances: Optional[List[AwsElbLoadBalancerInstance]] = None
    ListenerDescriptions: Optional[List[AwsElbLoadBalancerListenerDescriptionOutput]] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesOutput] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesOutput] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroup] = None
    Subnets: Optional[List[str]] = None
    VpcId: Optional[str] = None

AwsElbLoadBalancerListenerDescriptionUnion = Union[AwsElbLoadBalancerListenerDescription, AwsElbLoadBalancerListenerDescriptionOutput]

AwsElbv2LoadBalancerDetailsUnion = Union[AwsElbv2LoadBalancerDetails, AwsElbv2LoadBalancerDetailsOutput]


class AwsEventsEndpointRoutingConfigDetails(BaseValidatorModel):
    FailoverConfig: Optional[AwsEventsEndpointRoutingConfigFailoverConfigDetails] = None


class AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetails] = None
    ServiceRole: Optional[str] = None


class AwsIamAccessKeyDetails(BaseValidatorModel):
    UserName: Optional[str] = None
    Status: Optional[AwsIamAccessKeyStatusType] = None
    CreatedAt: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[str] = None
    PrincipalName: Optional[str] = None
    AccountId: Optional[str] = None
    AccessKeyId: Optional[str] = None
    SessionContext: Optional[AwsIamAccessKeySessionContext] = None

AwsIamGroupDetailsUnion = Union[AwsIamGroupDetails, AwsIamGroupDetailsOutput]


class AwsIamRoleDetailsOutput(BaseValidatorModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[List[AwsIamInstanceProfileOutput]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[List[AwsIamRolePolicy]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None

AwsIamInstanceProfileUnion = Union[AwsIamInstanceProfile, AwsIamInstanceProfileOutput]

AwsIamPolicyDetailsUnion = Union[AwsIamPolicyDetails, AwsIamPolicyDetailsOutput]

AwsIamUserDetailsUnion = Union[AwsIamUserDetails, AwsIamUserDetailsOutput]


class AwsLambdaFunctionDetailsOutput(BaseValidatorModel):
    Code: Optional[AwsLambdaFunctionCode] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfig] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentOutput] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[List[AwsLambdaFunctionLayer]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfig] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigOutput] = None
    Version: Optional[str] = None
    Architectures: Optional[List[str]] = None
    PackageType: Optional[str] = None

AwsLambdaFunctionEnvironmentUnion = Union[AwsLambdaFunctionEnvironment, AwsLambdaFunctionEnvironmentOutput]


class AwsMskClusterClusterInfoClientAuthenticationDetailsOutput(BaseValidatorModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetails] = None
    Unauthenticated: Optional[AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutput] = None


class AwsMskClusterClusterInfoClientAuthenticationDetails(BaseValidatorModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetails] = None
    Unauthenticated: Optional[AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnion] = None

AwsNetworkFirewallFirewallDetailsUnion = Union[AwsNetworkFirewallFirewallDetails, AwsNetworkFirewallFirewallDetailsOutput]


class AwsOpenSearchServiceDomainDetailsOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails] = None
    NodeToNodeEncryptionOptions: Optional[AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails] = None
    ServiceSoftwareOptions: Optional[AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetails] = None
    DomainEndpointOptions: Optional[AwsOpenSearchServiceDomainDomainEndpointOptionsDetails] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsOutput] = None
    LogPublishingOptions: Optional[AwsOpenSearchServiceDomainLogPublishingOptionsDetails] = None
    DomainEndpoints: Optional[Dict[str, str]] = None
    AdvancedSecurityOptions: Optional[AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails] = None


class AwsOpenSearchServiceDomainDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails] = None
    NodeToNodeEncryptionOptions: Optional[AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails] = None
    ServiceSoftwareOptions: Optional[AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetails] = None
    DomainEndpointOptions: Optional[AwsOpenSearchServiceDomainDomainEndpointOptionsDetails] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsUnion] = None
    LogPublishingOptions: Optional[AwsOpenSearchServiceDomainLogPublishingOptionsDetails] = None
    DomainEndpoints: Optional[Dict[str, str]] = None
    AdvancedSecurityOptions: Optional[AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails] = None

AwsRdsDbClusterDetailsUnion = Union[AwsRdsDbClusterDetails, AwsRdsDbClusterDetailsOutput]


class AwsRdsDbClusterSnapshotDetails(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    PercentProgress: Optional[int] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterSnapshotIdentifier: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    DbClusterSnapshotAttributes: Optional[List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnion]] = None

AwsRdsDbSnapshotDetailsUnion = Union[AwsRdsDbSnapshotDetails, AwsRdsDbSnapshotDetailsOutput]

AwsRdsDbSecurityGroupDetailsUnion = Union[AwsRdsDbSecurityGroupDetails, AwsRdsDbSecurityGroupDetailsOutput]


class AwsRdsDbSubnetGroupOutput(BaseValidatorModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[AwsRdsDbSubnetGroupSubnet]] = None
    DbSubnetGroupArn: Optional[str] = None


class AwsRdsDbSubnetGroup(BaseValidatorModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[AwsRdsDbSubnetGroupSubnet]] = None
    DbSubnetGroupArn: Optional[str] = None


class AwsRdsDbPendingModifiedValues(BaseValidatorModel):
    DbInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    Port: Optional[int] = None
    BackupRetentionPeriod: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    CaCertificateIdentifier: Optional[str] = None
    DbSubnetGroupName: Optional[str] = None
    PendingCloudWatchLogsExports: Optional[AwsRdsPendingCloudWatchLogsExportsUnion] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None


class AwsRedshiftClusterDetailsOutput(BaseValidatorModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[List[AwsRedshiftClusterClusterNode]] = None
    ClusterParameterGroups: Optional[List[AwsRedshiftClusterClusterParameterGroupOutput]] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[List[AwsRedshiftClusterClusterSecurityGroup]] = None
    ClusterSnapshotCopyStatus: Optional[AwsRedshiftClusterClusterSnapshotCopyStatus] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[List[AwsRedshiftClusterDeferredMaintenanceWindow]] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatus] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpoint] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatus] = None
    IamRoles: Optional[List[AwsRedshiftClusterIamRole]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[List[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValues] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfo] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatus] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRedshiftClusterVpcSecurityGroup]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatus] = None

AwsRedshiftClusterClusterParameterGroupUnion = Union[AwsRedshiftClusterClusterParameterGroup, AwsRedshiftClusterClusterParameterGroupOutput]


class AwsRoute53HostedZoneDetailsOutput(BaseValidatorModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetails] = None
    Vpcs: Optional[List[AwsRoute53HostedZoneVpcDetails]] = None
    NameServers: Optional[List[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetails] = None


class AwsRoute53HostedZoneDetails(BaseValidatorModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetails] = None
    Vpcs: Optional[List[AwsRoute53HostedZoneVpcDetails]] = None
    NameServers: Optional[List[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetails] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutput(BaseValidatorModel):
    Operands: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails]] = None
    Prefix: Optional[str] = None
    Tag: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails] = None
    Type: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails(BaseValidatorModel):
    Operands: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails]] = None
    Prefix: Optional[str] = None
    Tag: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails] = None
    Type: Optional[str] = None


class AwsS3BucketNotificationConfigurationFilterOutput(BaseValidatorModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterOutput] = None

AwsS3BucketNotificationConfigurationS3KeyFilterUnion = Union[AwsS3BucketNotificationConfigurationS3KeyFilter, AwsS3BucketNotificationConfigurationS3KeyFilterOutput]


class AwsS3BucketObjectLockConfiguration(BaseValidatorModel):
    ObjectLockEnabled: Optional[str] = None
    Rule: Optional[AwsS3BucketObjectLockConfigurationRuleDetails] = None


class AwsS3BucketServerSideEncryptionConfigurationOutput(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketServerSideEncryptionRule]] = None


class AwsS3BucketServerSideEncryptionConfiguration(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketServerSideEncryptionRule]] = None


class AwsS3BucketWebsiteConfigurationOutput(BaseValidatorModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectTo] = None
    RoutingRules: Optional[List[AwsS3BucketWebsiteConfigurationRoutingRule]] = None


class AwsS3BucketWebsiteConfiguration(BaseValidatorModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectTo] = None
    RoutingRules: Optional[List[AwsS3BucketWebsiteConfigurationRoutingRule]] = None

AwsSageMakerNotebookInstanceDetailsUnion = Union[AwsSageMakerNotebookInstanceDetails, AwsSageMakerNotebookInstanceDetailsOutput]


class BatchUpdateFindingsResponse(BaseValidatorModel):
    ProcessedFindings: List[AwsSecurityFindingIdentifier]
    UnprocessedFindings: List[BatchUpdateFindingsUnprocessedFinding]
    ResponseMetadata: ResponseMetadata

AwsSnsTopicDetailsUnion = Union[AwsSnsTopicDetails, AwsSnsTopicDetailsOutput]


class AwsSsmPatchComplianceDetails(BaseValidatorModel):
    Patch: Optional[AwsSsmPatch] = None


class AwsStepFunctionStateMachineLoggingConfigurationDetailsOutput(BaseValidatorModel):
    Destinations: Optional[List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails]] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None


class AwsStepFunctionStateMachineLoggingConfigurationDetails(BaseValidatorModel):
    Destinations: Optional[List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails]] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None

AwsWafRateBasedRuleDetailsUnion = Union[AwsWafRateBasedRuleDetails, AwsWafRateBasedRuleDetailsOutput]

AwsWafRegionalRateBasedRuleDetailsUnion = Union[AwsWafRegionalRateBasedRuleDetails, AwsWafRegionalRateBasedRuleDetailsOutput]

AwsWafRegionalRuleDetailsUnion = Union[AwsWafRegionalRuleDetails, AwsWafRegionalRuleDetailsOutput]


class AwsWafRegionalRuleGroupDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRegionalRuleGroupRulesDetails]] = None


class AwsWafRegionalRuleGroupDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRegionalRuleGroupRulesDetails]] = None


class AwsWafRegionalWebAclDetailsOutput(BaseValidatorModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[List[AwsWafRegionalWebAclRulesListDetails]] = None
    WebAclId: Optional[str] = None


class AwsWafRegionalWebAclDetails(BaseValidatorModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[List[AwsWafRegionalWebAclRulesListDetails]] = None
    WebAclId: Optional[str] = None

AwsWafRuleDetailsUnion = Union[AwsWafRuleDetails, AwsWafRuleDetailsOutput]


class AwsWafRuleGroupDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRuleGroupRulesDetails]] = None


class AwsWafRuleGroupDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRuleGroupRulesDetails]] = None


class AwsWafWebAclDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[List[AwsWafWebAclRuleOutput]] = None
    WebAclId: Optional[str] = None

AwsWafWebAclRuleUnion = Union[AwsWafWebAclRule, AwsWafWebAclRuleOutput]


class AwsWafv2ActionAllowDetailsOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutput] = None


class AwsWafv2RulesActionCaptchaDetailsOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutput] = None


class AwsWafv2RulesActionCountDetailsOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutput] = None

AwsWafv2CustomRequestHandlingDetailsUnion = Union[AwsWafv2CustomRequestHandlingDetails, AwsWafv2CustomRequestHandlingDetailsOutput]


class AwsWafv2ActionBlockDetailsOutput(BaseValidatorModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsOutput] = None

AwsWafv2CustomResponseDetailsUnion = Union[AwsWafv2CustomResponseDetails, AwsWafv2CustomResponseDetailsOutput]


class BatchGetStandardsControlAssociationsResponse(BaseValidatorModel):
    StandardsControlAssociationDetails: List[StandardsControlAssociationDetail]
    UnprocessedAssociations: List[UnprocessedStandardsControlAssociation]
    ResponseMetadata: ResponseMetadata


class BatchUpdateStandardsControlAssociationsResponse(BaseValidatorModel):
    UnprocessedAssociationUpdates: List[UnprocessedStandardsControlAssociationUpdate]
    ResponseMetadata: ResponseMetadata


class VulnerabilityOutput(BaseValidatorModel):
    Id: str
    VulnerablePackages: Optional[List[SoftwarePackage]] = None
    Cvss: Optional[List[CvssOutput]] = None
    RelatedVulnerabilities: Optional[List[str]] = None
    Vendor: Optional[VulnerabilityVendor] = None
    ReferenceUrls: Optional[List[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[List[VulnerabilityCodeVulnerabilitiesOutput]] = None

VulnerabilityCodeVulnerabilitiesUnion = Union[VulnerabilityCodeVulnerabilities, VulnerabilityCodeVulnerabilitiesOutput]


class ParameterDefinition(BaseValidatorModel):
    Description: str
    ConfigurationOptions: ConfigurationOptions


class BatchGetConfigurationPolicyAssociationsRequest(BaseValidatorModel):
    ConfigurationPolicyAssociationIdentifiers: List[ConfigurationPolicyAssociation]


class UnprocessedConfigurationPolicyAssociation(BaseValidatorModel):
    ConfigurationPolicyAssociationIdentifiers: Optional[ConfigurationPolicyAssociation] = None
    ErrorCode: Optional[str] = None
    ErrorReason: Optional[str] = None

ContainerDetailsUnion = Union[ContainerDetails, ContainerDetailsOutput]


class AutomationRulesFindingFiltersOutput(BaseValidatorModel):
    ProductArn: Optional[List[StringFilter]] = None
    AwsAccountId: Optional[List[StringFilter]] = None
    Id: Optional[List[StringFilter]] = None
    GeneratorId: Optional[List[StringFilter]] = None
    Type: Optional[List[StringFilter]] = None
    FirstObservedAt: Optional[List[DateFilter]] = None
    LastObservedAt: Optional[List[DateFilter]] = None
    CreatedAt: Optional[List[DateFilter]] = None
    UpdatedAt: Optional[List[DateFilter]] = None
    Confidence: Optional[List[NumberFilter]] = None
    Criticality: Optional[List[NumberFilter]] = None
    Title: Optional[List[StringFilter]] = None
    Description: Optional[List[StringFilter]] = None
    SourceUrl: Optional[List[StringFilter]] = None
    ProductName: Optional[List[StringFilter]] = None
    CompanyName: Optional[List[StringFilter]] = None
    SeverityLabel: Optional[List[StringFilter]] = None
    ResourceType: Optional[List[StringFilter]] = None
    ResourceId: Optional[List[StringFilter]] = None
    ResourcePartition: Optional[List[StringFilter]] = None
    ResourceRegion: Optional[List[StringFilter]] = None
    ResourceTags: Optional[List[MapFilter]] = None
    ResourceDetailsOther: Optional[List[MapFilter]] = None
    ComplianceStatus: Optional[List[StringFilter]] = None
    ComplianceSecurityControlId: Optional[List[StringFilter]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilter]] = None
    VerificationState: Optional[List[StringFilter]] = None
    WorkflowStatus: Optional[List[StringFilter]] = None
    RecordState: Optional[List[StringFilter]] = None
    RelatedFindingsProductArn: Optional[List[StringFilter]] = None
    RelatedFindingsId: Optional[List[StringFilter]] = None
    NoteText: Optional[List[StringFilter]] = None
    NoteUpdatedAt: Optional[List[DateFilter]] = None
    NoteUpdatedBy: Optional[List[StringFilter]] = None
    UserDefinedFields: Optional[List[MapFilter]] = None
    ResourceApplicationArn: Optional[List[StringFilter]] = None
    ResourceApplicationName: Optional[List[StringFilter]] = None
    AwsAccountName: Optional[List[StringFilter]] = None


class AutomationRulesFindingFilters(BaseValidatorModel):
    ProductArn: Optional[List[StringFilter]] = None
    AwsAccountId: Optional[List[StringFilter]] = None
    Id: Optional[List[StringFilter]] = None
    GeneratorId: Optional[List[StringFilter]] = None
    Type: Optional[List[StringFilter]] = None
    FirstObservedAt: Optional[List[DateFilter]] = None
    LastObservedAt: Optional[List[DateFilter]] = None
    CreatedAt: Optional[List[DateFilter]] = None
    UpdatedAt: Optional[List[DateFilter]] = None
    Confidence: Optional[List[NumberFilter]] = None
    Criticality: Optional[List[NumberFilter]] = None
    Title: Optional[List[StringFilter]] = None
    Description: Optional[List[StringFilter]] = None
    SourceUrl: Optional[List[StringFilter]] = None
    ProductName: Optional[List[StringFilter]] = None
    CompanyName: Optional[List[StringFilter]] = None
    SeverityLabel: Optional[List[StringFilter]] = None
    ResourceType: Optional[List[StringFilter]] = None
    ResourceId: Optional[List[StringFilter]] = None
    ResourcePartition: Optional[List[StringFilter]] = None
    ResourceRegion: Optional[List[StringFilter]] = None
    ResourceTags: Optional[List[MapFilter]] = None
    ResourceDetailsOther: Optional[List[MapFilter]] = None
    ComplianceStatus: Optional[List[StringFilter]] = None
    ComplianceSecurityControlId: Optional[List[StringFilter]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilter]] = None
    VerificationState: Optional[List[StringFilter]] = None
    WorkflowStatus: Optional[List[StringFilter]] = None
    RecordState: Optional[List[StringFilter]] = None
    RelatedFindingsProductArn: Optional[List[StringFilter]] = None
    RelatedFindingsId: Optional[List[StringFilter]] = None
    NoteText: Optional[List[StringFilter]] = None
    NoteUpdatedAt: Optional[List[DateFilter]] = None
    NoteUpdatedBy: Optional[List[StringFilter]] = None
    UserDefinedFields: Optional[List[MapFilter]] = None
    ResourceApplicationArn: Optional[List[StringFilter]] = None
    ResourceApplicationName: Optional[List[StringFilter]] = None
    AwsAccountName: Optional[List[StringFilter]] = None


class AwsSecurityFindingFiltersOutput(BaseValidatorModel):
    ProductArn: Optional[List[StringFilter]] = None
    AwsAccountId: Optional[List[StringFilter]] = None
    Id: Optional[List[StringFilter]] = None
    GeneratorId: Optional[List[StringFilter]] = None
    Region: Optional[List[StringFilter]] = None
    Type: Optional[List[StringFilter]] = None
    FirstObservedAt: Optional[List[DateFilter]] = None
    LastObservedAt: Optional[List[DateFilter]] = None
    CreatedAt: Optional[List[DateFilter]] = None
    UpdatedAt: Optional[List[DateFilter]] = None
    SeverityProduct: Optional[List[NumberFilter]] = None
    SeverityNormalized: Optional[List[NumberFilter]] = None
    SeverityLabel: Optional[List[StringFilter]] = None
    Confidence: Optional[List[NumberFilter]] = None
    Criticality: Optional[List[NumberFilter]] = None
    Title: Optional[List[StringFilter]] = None
    Description: Optional[List[StringFilter]] = None
    RecommendationText: Optional[List[StringFilter]] = None
    SourceUrl: Optional[List[StringFilter]] = None
    ProductFields: Optional[List[MapFilter]] = None
    ProductName: Optional[List[StringFilter]] = None
    CompanyName: Optional[List[StringFilter]] = None
    UserDefinedFields: Optional[List[MapFilter]] = None
    MalwareName: Optional[List[StringFilter]] = None
    MalwareType: Optional[List[StringFilter]] = None
    MalwarePath: Optional[List[StringFilter]] = None
    MalwareState: Optional[List[StringFilter]] = None
    NetworkDirection: Optional[List[StringFilter]] = None
    NetworkProtocol: Optional[List[StringFilter]] = None
    NetworkSourceIpV4: Optional[List[IpFilter]] = None
    NetworkSourceIpV6: Optional[List[IpFilter]] = None
    NetworkSourcePort: Optional[List[NumberFilter]] = None
    NetworkSourceDomain: Optional[List[StringFilter]] = None
    NetworkSourceMac: Optional[List[StringFilter]] = None
    NetworkDestinationIpV4: Optional[List[IpFilter]] = None
    NetworkDestinationIpV6: Optional[List[IpFilter]] = None
    NetworkDestinationPort: Optional[List[NumberFilter]] = None
    NetworkDestinationDomain: Optional[List[StringFilter]] = None
    ProcessName: Optional[List[StringFilter]] = None
    ProcessPath: Optional[List[StringFilter]] = None
    ProcessPid: Optional[List[NumberFilter]] = None
    ProcessParentPid: Optional[List[NumberFilter]] = None
    ProcessLaunchedAt: Optional[List[DateFilter]] = None
    ProcessTerminatedAt: Optional[List[DateFilter]] = None
    ThreatIntelIndicatorType: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorValue: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorCategory: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[List[DateFilter]] = None
    ThreatIntelIndicatorSource: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorSourceUrl: Optional[List[StringFilter]] = None
    ResourceType: Optional[List[StringFilter]] = None
    ResourceId: Optional[List[StringFilter]] = None
    ResourcePartition: Optional[List[StringFilter]] = None
    ResourceRegion: Optional[List[StringFilter]] = None
    ResourceTags: Optional[List[MapFilter]] = None
    ResourceAwsEc2InstanceType: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceImageId: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[List[IpFilter]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[List[IpFilter]] = None
    ResourceAwsEc2InstanceKeyName: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceVpcId: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[List[DateFilter]] = None
    ResourceAwsS3BucketOwnerId: Optional[List[StringFilter]] = None
    ResourceAwsS3BucketOwnerName: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyUserName: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyStatus: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[List[DateFilter]] = None
    ResourceAwsIamUserUserName: Optional[List[StringFilter]] = None
    ResourceContainerName: Optional[List[StringFilter]] = None
    ResourceContainerImageId: Optional[List[StringFilter]] = None
    ResourceContainerImageName: Optional[List[StringFilter]] = None
    ResourceContainerLaunchedAt: Optional[List[DateFilter]] = None
    ResourceDetailsOther: Optional[List[MapFilter]] = None
    ComplianceStatus: Optional[List[StringFilter]] = None
    VerificationState: Optional[List[StringFilter]] = None
    WorkflowState: Optional[List[StringFilter]] = None
    WorkflowStatus: Optional[List[StringFilter]] = None
    RecordState: Optional[List[StringFilter]] = None
    RelatedFindingsProductArn: Optional[List[StringFilter]] = None
    RelatedFindingsId: Optional[List[StringFilter]] = None
    NoteText: Optional[List[StringFilter]] = None
    NoteUpdatedAt: Optional[List[DateFilter]] = None
    NoteUpdatedBy: Optional[List[StringFilter]] = None
    Keyword: Optional[List[KeywordFilter]] = None
    FindingProviderFieldsConfidence: Optional[List[NumberFilter]] = None
    FindingProviderFieldsCriticality: Optional[List[NumberFilter]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[List[StringFilter]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[List[StringFilter]] = None
    FindingProviderFieldsSeverityLabel: Optional[List[StringFilter]] = None
    FindingProviderFieldsSeverityOriginal: Optional[List[StringFilter]] = None
    FindingProviderFieldsTypes: Optional[List[StringFilter]] = None
    Sample: Optional[List[BooleanFilter]] = None
    ComplianceSecurityControlId: Optional[List[StringFilter]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilter]] = None
    VulnerabilitiesExploitAvailable: Optional[List[StringFilter]] = None
    VulnerabilitiesFixAvailable: Optional[List[StringFilter]] = None
    ComplianceSecurityControlParametersName: Optional[List[StringFilter]] = None
    ComplianceSecurityControlParametersValue: Optional[List[StringFilter]] = None
    AwsAccountName: Optional[List[StringFilter]] = None
    ResourceApplicationName: Optional[List[StringFilter]] = None
    ResourceApplicationArn: Optional[List[StringFilter]] = None


class AwsSecurityFindingFilters(BaseValidatorModel):
    ProductArn: Optional[List[StringFilter]] = None
    AwsAccountId: Optional[List[StringFilter]] = None
    Id: Optional[List[StringFilter]] = None
    GeneratorId: Optional[List[StringFilter]] = None
    Region: Optional[List[StringFilter]] = None
    Type: Optional[List[StringFilter]] = None
    FirstObservedAt: Optional[List[DateFilter]] = None
    LastObservedAt: Optional[List[DateFilter]] = None
    CreatedAt: Optional[List[DateFilter]] = None
    UpdatedAt: Optional[List[DateFilter]] = None
    SeverityProduct: Optional[List[NumberFilter]] = None
    SeverityNormalized: Optional[List[NumberFilter]] = None
    SeverityLabel: Optional[List[StringFilter]] = None
    Confidence: Optional[List[NumberFilter]] = None
    Criticality: Optional[List[NumberFilter]] = None
    Title: Optional[List[StringFilter]] = None
    Description: Optional[List[StringFilter]] = None
    RecommendationText: Optional[List[StringFilter]] = None
    SourceUrl: Optional[List[StringFilter]] = None
    ProductFields: Optional[List[MapFilter]] = None
    ProductName: Optional[List[StringFilter]] = None
    CompanyName: Optional[List[StringFilter]] = None
    UserDefinedFields: Optional[List[MapFilter]] = None
    MalwareName: Optional[List[StringFilter]] = None
    MalwareType: Optional[List[StringFilter]] = None
    MalwarePath: Optional[List[StringFilter]] = None
    MalwareState: Optional[List[StringFilter]] = None
    NetworkDirection: Optional[List[StringFilter]] = None
    NetworkProtocol: Optional[List[StringFilter]] = None
    NetworkSourceIpV4: Optional[List[IpFilter]] = None
    NetworkSourceIpV6: Optional[List[IpFilter]] = None
    NetworkSourcePort: Optional[List[NumberFilter]] = None
    NetworkSourceDomain: Optional[List[StringFilter]] = None
    NetworkSourceMac: Optional[List[StringFilter]] = None
    NetworkDestinationIpV4: Optional[List[IpFilter]] = None
    NetworkDestinationIpV6: Optional[List[IpFilter]] = None
    NetworkDestinationPort: Optional[List[NumberFilter]] = None
    NetworkDestinationDomain: Optional[List[StringFilter]] = None
    ProcessName: Optional[List[StringFilter]] = None
    ProcessPath: Optional[List[StringFilter]] = None
    ProcessPid: Optional[List[NumberFilter]] = None
    ProcessParentPid: Optional[List[NumberFilter]] = None
    ProcessLaunchedAt: Optional[List[DateFilter]] = None
    ProcessTerminatedAt: Optional[List[DateFilter]] = None
    ThreatIntelIndicatorType: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorValue: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorCategory: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[List[DateFilter]] = None
    ThreatIntelIndicatorSource: Optional[List[StringFilter]] = None
    ThreatIntelIndicatorSourceUrl: Optional[List[StringFilter]] = None
    ResourceType: Optional[List[StringFilter]] = None
    ResourceId: Optional[List[StringFilter]] = None
    ResourcePartition: Optional[List[StringFilter]] = None
    ResourceRegion: Optional[List[StringFilter]] = None
    ResourceTags: Optional[List[MapFilter]] = None
    ResourceAwsEc2InstanceType: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceImageId: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[List[IpFilter]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[List[IpFilter]] = None
    ResourceAwsEc2InstanceKeyName: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceVpcId: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[List[StringFilter]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[List[DateFilter]] = None
    ResourceAwsS3BucketOwnerId: Optional[List[StringFilter]] = None
    ResourceAwsS3BucketOwnerName: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyUserName: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyStatus: Optional[List[StringFilter]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[List[DateFilter]] = None
    ResourceAwsIamUserUserName: Optional[List[StringFilter]] = None
    ResourceContainerName: Optional[List[StringFilter]] = None
    ResourceContainerImageId: Optional[List[StringFilter]] = None
    ResourceContainerImageName: Optional[List[StringFilter]] = None
    ResourceContainerLaunchedAt: Optional[List[DateFilter]] = None
    ResourceDetailsOther: Optional[List[MapFilter]] = None
    ComplianceStatus: Optional[List[StringFilter]] = None
    VerificationState: Optional[List[StringFilter]] = None
    WorkflowState: Optional[List[StringFilter]] = None
    WorkflowStatus: Optional[List[StringFilter]] = None
    RecordState: Optional[List[StringFilter]] = None
    RelatedFindingsProductArn: Optional[List[StringFilter]] = None
    RelatedFindingsId: Optional[List[StringFilter]] = None
    NoteText: Optional[List[StringFilter]] = None
    NoteUpdatedAt: Optional[List[DateFilter]] = None
    NoteUpdatedBy: Optional[List[StringFilter]] = None
    Keyword: Optional[List[KeywordFilter]] = None
    FindingProviderFieldsConfidence: Optional[List[NumberFilter]] = None
    FindingProviderFieldsCriticality: Optional[List[NumberFilter]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[List[StringFilter]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[List[StringFilter]] = None
    FindingProviderFieldsSeverityLabel: Optional[List[StringFilter]] = None
    FindingProviderFieldsSeverityOriginal: Optional[List[StringFilter]] = None
    FindingProviderFieldsTypes: Optional[List[StringFilter]] = None
    Sample: Optional[List[BooleanFilter]] = None
    ComplianceSecurityControlId: Optional[List[StringFilter]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilter]] = None
    VulnerabilitiesExploitAvailable: Optional[List[StringFilter]] = None
    VulnerabilitiesFixAvailable: Optional[List[StringFilter]] = None
    ComplianceSecurityControlParametersName: Optional[List[StringFilter]] = None
    ComplianceSecurityControlParametersValue: Optional[List[StringFilter]] = None
    AwsAccountName: Optional[List[StringFilter]] = None
    ResourceApplicationName: Optional[List[StringFilter]] = None
    ResourceApplicationArn: Optional[List[StringFilter]] = None

ThreatUnion = Union[Threat, ThreatOutput]


class GetFindingHistoryResponse(BaseValidatorModel):
    Records: List[FindingHistoryRecord]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

FindingProviderFieldsUnion = Union[FindingProviderFields, FindingProviderFieldsOutput]

SignalUnion = Union[Signal, SignalOutput]


class GetInsightResultsResponse(BaseValidatorModel):
    InsightResults: InsightResults
    ResponseMetadata: ResponseMetadata


class NetworkHeaderOutput(BaseValidatorModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsOutput] = None
    Source: Optional[NetworkPathComponentDetailsOutput] = None

NetworkPathComponentDetailsUnion = Union[NetworkPathComponentDetails, NetworkPathComponentDetailsOutput]


class OccurrencesOutput(BaseValidatorModel):
    LineRanges: Optional[List[Range]] = None
    OffsetRanges: Optional[List[Range]] = None
    Pages: Optional[List[Page]] = None
    Records: Optional[List[Record]] = None
    Cells: Optional[List[Cell]] = None


class Occurrences(BaseValidatorModel):
    LineRanges: Optional[List[Range]] = None
    OffsetRanges: Optional[List[Range]] = None
    Pages: Optional[List[Page]] = None
    Records: Optional[List[Record]] = None
    Cells: Optional[List[Cell]] = None


class SecurityControlCustomParameterOutput(BaseValidatorModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutput]] = None


class SecurityControl(BaseValidatorModel):
    SecurityControlId: str
    SecurityControlArn: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    SecurityControlStatus: ControlStatusType
    UpdateStatus: Optional[UpdateStatusType] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutput]] = None
    LastUpdateReason: Optional[str] = None


class ParameterConfiguration(BaseValidatorModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueUnion] = None


class RuleGroupSourceStatefulRulesDetails(BaseValidatorModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetails] = None
    RuleOptions: Optional[List[RuleGroupSourceStatefulRulesOptionsDetailsUnion]] = None


class RuleGroupSourceStatelessRuleDefinitionOutput(BaseValidatorModel):
    Actions: Optional[List[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesOutput] = None


class RuleGroupSourceStatelessRuleMatchAttributes(BaseValidatorModel):
    DestinationPorts: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts]] = None
    Destinations: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesDestinations]] = None
    Protocols: Optional[List[int]] = None
    SourcePorts: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSourcePorts]] = None
    Sources: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSources]] = None
    TcpFlags: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnion]] = None


class RuleGroupVariables(BaseValidatorModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsUnion] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsUnion] = None


class Compliance(BaseValidatorModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[List[str]] = None
    StatusReasons: Optional[List[StatusReason]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[List[AssociatedStandard]] = None
    SecurityControlParameters: Optional[List[SecurityControlParameterUnion]] = None


class DescribeStandardsResponse(BaseValidatorModel):
    Standards: List[Standard]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchDisableStandardsResponse(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscription]
    ResponseMetadata: ResponseMetadata


class BatchEnableStandardsResponse(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscription]
    ResponseMetadata: ResponseMetadata


class GetEnabledStandardsResponse(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StatelessCustomActionDefinitionOutput(BaseValidatorModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionOutput] = None

StatelessCustomPublishMetricActionUnion = Union[StatelessCustomPublishMetricAction, StatelessCustomPublishMetricActionOutput]

AwsApiCallActionUnion = Union[AwsApiCallAction, AwsApiCallActionOutput]


class PortProbeActionOutput(BaseValidatorModel):
    PortProbeDetails: Optional[List[PortProbeDetail]] = None
    Blocked: Optional[bool] = None


class PortProbeAction(BaseValidatorModel):
    PortProbeDetails: Optional[List[PortProbeDetail]] = None
    Blocked: Optional[bool] = None


class SequenceOutput(BaseValidatorModel):
    Uid: Optional[str] = None
    Actors: Optional[List[Actor]] = None
    Endpoints: Optional[List[NetworkEndpoint]] = None
    Signals: Optional[List[SignalOutput]] = None
    SequenceIndicators: Optional[List[IndicatorOutput]] = None

AwsEc2RouteTableDetailsUnion = Union[AwsEc2RouteTableDetails, AwsEc2RouteTableDetailsOutput]


class AutomationRulesAction(BaseValidatorModel):
    Type: Optional[Literal['FINDING_FIELDS_UPDATE']] = None
    FindingFieldsUpdate: Optional[AutomationRulesFindingFieldsUpdateUnion] = None

AwsAmazonMqBrokerDetailsUnion = Union[AwsAmazonMqBrokerDetails, AwsAmazonMqBrokerDetailsOutput]

AwsApiGatewayStageDetailsUnion = Union[AwsApiGatewayStageDetails, AwsApiGatewayStageDetailsOutput]

AwsApiGatewayRestApiDetailsUnion = Union[AwsApiGatewayRestApiDetails, AwsApiGatewayRestApiDetailsOutput]

AwsAppSyncGraphQlApiDetailsUnion = Union[AwsAppSyncGraphQlApiDetails, AwsAppSyncGraphQlApiDetailsOutput]


class AwsAthenaWorkGroupDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[str] = None
    Configuration: Optional[AwsAthenaWorkGroupConfigurationDetails] = None


class AwsAutoScalingAutoScalingGroupDetailsOutput(BaseValidatorModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutput] = None
    AvailabilityZones: Optional[List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails]] = None
    LaunchTemplate: Optional[AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification] = None
    CapacityRebalance: Optional[bool] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails(BaseValidatorModel):
    InstancesDistribution: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails] = None
    LaunchTemplate: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnion] = None

AwsAutoScalingLaunchConfigurationDetailsUnion = Union[AwsAutoScalingLaunchConfigurationDetails, AwsAutoScalingLaunchConfigurationDetailsOutput]


class AwsBackupBackupPlanBackupPlanDetailsOutput(BaseValidatorModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutput]] = None
    BackupPlanRule: Optional[List[AwsBackupBackupPlanRuleDetailsOutput]] = None

AwsBackupBackupPlanRuleDetailsUnion = Union[AwsBackupBackupPlanRuleDetails, AwsBackupBackupPlanRuleDetailsOutput]

AwsBackupBackupVaultDetailsUnion = Union[AwsBackupBackupVaultDetails, AwsBackupBackupVaultDetailsOutput]


class AwsCertificateManagerCertificateDetailsOutput(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[List[AwsCertificateManagerCertificateDomainValidationOptionOutput]] = None
    ExtendedKeyUsages: Optional[List[AwsCertificateManagerCertificateExtendedKeyUsage]] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[List[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[List[AwsCertificateManagerCertificateKeyUsage]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptions] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[AwsCertificateManagerCertificateRenewalSummaryOutput] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    Type: Optional[str] = None

AwsCertificateManagerCertificateRenewalSummaryUnion = Union[AwsCertificateManagerCertificateRenewalSummary, AwsCertificateManagerCertificateRenewalSummaryOutput]


class AwsCloudFrontDistributionOriginsOutput(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginItemOutput]] = None


class AwsCloudFrontDistributionOriginGroupsOutput(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginGroupOutput]] = None

AwsCloudFrontDistributionOriginGroupFailoverUnion = Union[AwsCloudFrontDistributionOriginGroupFailover, AwsCloudFrontDistributionOriginGroupFailoverOutput]

AwsCloudFrontDistributionOriginCustomOriginConfigUnion = Union[AwsCloudFrontDistributionOriginCustomOriginConfig, AwsCloudFrontDistributionOriginCustomOriginConfigOutput]


class AwsCodeBuildProjectDetails(BaseValidatorModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[List[AwsCodeBuildProjectArtifactsDetails]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentUnion] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSource] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetails] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigUnion] = None
    SecondaryArtifacts: Optional[List[AwsCodeBuildProjectArtifactsDetails]] = None

AwsApiGatewayV2ApiDetailsUnion = Union[AwsApiGatewayV2ApiDetails, AwsApiGatewayV2ApiDetailsOutput]

AwsDynamoDbTableGlobalSecondaryIndexUnion = Union[AwsDynamoDbTableGlobalSecondaryIndex, AwsDynamoDbTableGlobalSecondaryIndexOutput]

AwsDynamoDbTableLocalSecondaryIndexUnion = Union[AwsDynamoDbTableLocalSecondaryIndex, AwsDynamoDbTableLocalSecondaryIndexOutput]


class AwsDynamoDbTableDetailsOutput(BaseValidatorModel):
    AttributeDefinitions: Optional[List[AwsDynamoDbTableAttributeDefinition]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummary] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[List[AwsDynamoDbTableGlobalSecondaryIndexOutput]] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[List[AwsDynamoDbTableLocalSecondaryIndexOutput]] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None
    Replicas: Optional[List[AwsDynamoDbTableReplicaOutput]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummary] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescription] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecification] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

AwsDynamoDbTableReplicaUnion = Union[AwsDynamoDbTableReplica, AwsDynamoDbTableReplicaOutput]

AwsEc2ClientVpnEndpointDetailsUnion = Union[AwsEc2ClientVpnEndpointDetails, AwsEc2ClientVpnEndpointDetailsOutput]


class AwsEc2LaunchTemplateDetailsOutput(BaseValidatorModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsOutput] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None


class AwsEc2LaunchTemplateDataDetails(BaseValidatorModel):
    BlockDeviceMappingSet: Optional[List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails]] = None
    CapacityReservationSpecification: Optional[AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetails] = None
    CreditSpecification: Optional[AwsEc2LaunchTemplateDataCreditSpecificationDetails] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails]] = None
    ElasticInferenceAcceleratorSet: Optional[List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails]] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetails] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetails] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetails] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails] = None
    InstanceRequirements: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnion] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[List[AwsEc2LaunchTemplateDataLicenseSetDetails]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetails] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetails] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetails] = None
    NetworkInterfaceSet: Optional[List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnion]] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetails] = None
    PrivateDnsNameOptions: Optional[AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    SecurityGroupSet: Optional[List[str]] = None
    UserData: Optional[str] = None

AwsEc2NetworkAclDetailsUnion = Union[AwsEc2NetworkAclDetails, AwsEc2NetworkAclDetailsOutput]


class AwsEc2SecurityGroupDetails(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[List[AwsEc2SecurityGroupIpPermissionUnion]] = None
    IpPermissionsEgress: Optional[List[AwsEc2SecurityGroupIpPermission]] = None


class AwsEc2VpcPeeringConnectionDetails(BaseValidatorModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetails] = None
    VpcPeeringConnectionId: Optional[str] = None

AwsEc2VpnConnectionOptionsDetailsUnion = Union[AwsEc2VpnConnectionOptionsDetails, AwsEc2VpnConnectionOptionsDetailsOutput]


class AwsEcsClusterDetailsOutput(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[List[str]] = None
    ClusterSettings: Optional[List[AwsEcsClusterClusterSettingsDetails]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetails] = None
    DefaultCapacityProviderStrategy: Optional[List[AwsEcsClusterDefaultCapacityProviderStrategyDetails]] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None


class AwsEcsClusterDetails(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[List[str]] = None
    ClusterSettings: Optional[List[AwsEcsClusterClusterSettingsDetails]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetails] = None
    DefaultCapacityProviderStrategy: Optional[List[AwsEcsClusterDefaultCapacityProviderStrategyDetails]] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None


class AwsEcsTaskDetails(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskVolumeDetails]] = None
    Containers: Optional[List[AwsEcsContainerDetailsUnion]] = None

AwsEcsServiceNetworkConfigurationDetailsUnion = Union[AwsEcsServiceNetworkConfigurationDetails, AwsEcsServiceNetworkConfigurationDetailsOutput]

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails, AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutput]


class AwsEcsTaskDefinitionDetailsOutput(BaseValidatorModel):
    ContainerDefinitions: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsDetailsOutput]] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[List[AwsEcsTaskDefinitionInferenceAcceleratorsDetails]] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[List[AwsEcsTaskDefinitionPlacementConstraintsDetails]] = None
    ProxyConfiguration: Optional[AwsEcsTaskDefinitionProxyConfigurationDetailsOutput] = None
    RequiresCompatibilities: Optional[List[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskDefinitionVolumesDetailsOutput]] = None
    Status: Optional[str] = None

AwsEcsTaskDefinitionVolumesDetailsUnion = Union[AwsEcsTaskDefinitionVolumesDetails, AwsEcsTaskDefinitionVolumesDetailsOutput]

AwsEfsAccessPointDetailsUnion = Union[AwsEfsAccessPointDetails, AwsEfsAccessPointDetailsOutput]

AwsEksClusterLoggingDetailsUnion = Union[AwsEksClusterLoggingDetails, AwsEksClusterLoggingDetailsOutput]

AwsElasticsearchDomainDetailsUnion = Union[AwsElasticsearchDomainDetails, AwsElasticsearchDomainDetailsOutput]


class AwsElbLoadBalancerDetails(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    BackendServerDescriptions: Optional[List[AwsElbLoadBalancerBackendServerDescriptionUnion]] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheck] = None
    Instances: Optional[List[AwsElbLoadBalancerInstance]] = None
    ListenerDescriptions: Optional[List[AwsElbLoadBalancerListenerDescriptionUnion]] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesUnion] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesUnion] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroup] = None
    Subnets: Optional[List[str]] = None
    VpcId: Optional[str] = None


class AwsEventsEndpointDetailsOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[List[AwsEventsEndpointEventBusesDetails]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetails] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetails] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


class AwsEventsEndpointDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[List[AwsEventsEndpointEventBusesDetails]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetails] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetails] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesDetails(BaseValidatorModel):
    CloudTrail: Optional[AwsGuardDutyDetectorDataSourcesCloudTrailDetails] = None
    DnsLogs: Optional[AwsGuardDutyDetectorDataSourcesDnsLogsDetails] = None
    FlowLogs: Optional[AwsGuardDutyDetectorDataSourcesFlowLogsDetails] = None
    Kubernetes: Optional[AwsGuardDutyDetectorDataSourcesKubernetesDetails] = None
    MalwareProtection: Optional[AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails] = None
    S3Logs: Optional[AwsGuardDutyDetectorDataSourcesS3LogsDetails] = None


class AwsIamRoleDetails(BaseValidatorModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[List[AwsIamInstanceProfileUnion]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[List[AwsIamRolePolicy]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None


class AwsLambdaFunctionDetails(BaseValidatorModel):
    Code: Optional[AwsLambdaFunctionCode] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfig] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentUnion] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[List[AwsLambdaFunctionLayer]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfig] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigUnion] = None
    Version: Optional[str] = None
    Architectures: Optional[List[str]] = None
    PackageType: Optional[str] = None


class AwsMskClusterClusterInfoDetailsOutput(BaseValidatorModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetails] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[AwsMskClusterClusterInfoClientAuthenticationDetailsOutput] = None
    EnhancedMonitoring: Optional[str] = None

AwsMskClusterClusterInfoClientAuthenticationDetailsUnion = Union[AwsMskClusterClusterInfoClientAuthenticationDetails, AwsMskClusterClusterInfoClientAuthenticationDetailsOutput]

AwsOpenSearchServiceDomainDetailsUnion = Union[AwsOpenSearchServiceDomainDetails, AwsOpenSearchServiceDomainDetailsOutput]

AwsRdsDbClusterSnapshotDetailsUnion = Union[AwsRdsDbClusterSnapshotDetails, AwsRdsDbClusterSnapshotDetailsOutput]


class AwsRdsDbInstanceDetailsOutput(BaseValidatorModel):
    AssociatedRoles: Optional[List[AwsRdsDbInstanceAssociatedRole]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroup]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[List[str]] = None
    DbParameterGroups: Optional[List[AwsRdsDbParameterGroup]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupOutput] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesOutput] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[AwsRdsDbOptionGroupMembership]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[List[AwsRdsDbStatusInfo]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembership]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    MaxAllocatedStorage: Optional[int] = None

AwsRdsDbSubnetGroupUnion = Union[AwsRdsDbSubnetGroup, AwsRdsDbSubnetGroupOutput]

AwsRdsDbPendingModifiedValuesUnion = Union[AwsRdsDbPendingModifiedValues, AwsRdsDbPendingModifiedValuesOutput]


class AwsRedshiftClusterDetails(BaseValidatorModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[List[AwsRedshiftClusterClusterNode]] = None
    ClusterParameterGroups: Optional[List[AwsRedshiftClusterClusterParameterGroupUnion]] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[List[AwsRedshiftClusterClusterSecurityGroup]] = None
    ClusterSnapshotCopyStatus: Optional[AwsRedshiftClusterClusterSnapshotCopyStatus] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[List[AwsRedshiftClusterDeferredMaintenanceWindow]] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatus] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpoint] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatus] = None
    IamRoles: Optional[List[AwsRedshiftClusterIamRole]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[List[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValues] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfo] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatus] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRedshiftClusterVpcSecurityGroup]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatus] = None

AwsRoute53HostedZoneDetailsUnion = Union[AwsRoute53HostedZoneDetails, AwsRoute53HostedZoneDetailsOutput]


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutput(BaseValidatorModel):
    Predicate: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutput] = None

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnion = Union[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails, AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutput]


class AwsS3BucketNotificationConfigurationDetailOutput(BaseValidatorModel):
    Events: Optional[List[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterOutput] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None


class AwsS3BucketNotificationConfigurationFilter(BaseValidatorModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterUnion] = None

AwsS3BucketServerSideEncryptionConfigurationUnion = Union[AwsS3BucketServerSideEncryptionConfiguration, AwsS3BucketServerSideEncryptionConfigurationOutput]

AwsS3BucketWebsiteConfigurationUnion = Union[AwsS3BucketWebsiteConfiguration, AwsS3BucketWebsiteConfigurationOutput]


class AwsStepFunctionStateMachineDetailsOutput(BaseValidatorModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[AwsStepFunctionStateMachineLoggingConfigurationDetailsOutput] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[AwsStepFunctionStateMachineTracingConfigurationDetails] = None
    Type: Optional[str] = None

AwsStepFunctionStateMachineLoggingConfigurationDetailsUnion = Union[AwsStepFunctionStateMachineLoggingConfigurationDetails, AwsStepFunctionStateMachineLoggingConfigurationDetailsOutput]

AwsWafRegionalRuleGroupDetailsUnion = Union[AwsWafRegionalRuleGroupDetails, AwsWafRegionalRuleGroupDetailsOutput]

AwsWafRegionalWebAclDetailsUnion = Union[AwsWafRegionalWebAclDetails, AwsWafRegionalWebAclDetailsOutput]

AwsWafRuleGroupDetailsUnion = Union[AwsWafRuleGroupDetails, AwsWafRuleGroupDetailsOutput]


class AwsWafWebAclDetails(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[List[AwsWafWebAclRuleUnion]] = None
    WebAclId: Optional[str] = None


class AwsWafv2ActionAllowDetails(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsUnion] = None


class AwsWafv2RulesActionCaptchaDetails(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsUnion] = None


class AwsWafv2RulesActionCountDetails(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsUnion] = None


class AwsWafv2RulesActionDetailsOutput(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutput] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutput] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsOutput] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsOutput] = None


class AwsWafv2WebAclActionDetailsOutput(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutput] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutput] = None


class AwsWafv2ActionBlockDetails(BaseValidatorModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsUnion] = None


class Vulnerability(BaseValidatorModel):
    Id: str
    VulnerablePackages: Optional[List[SoftwarePackage]] = None
    Cvss: Optional[List[CvssUnion]] = None
    RelatedVulnerabilities: Optional[List[str]] = None
    Vendor: Optional[VulnerabilityVendor] = None
    ReferenceUrls: Optional[List[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[List[VulnerabilityCodeVulnerabilitiesUnion]] = None


class SecurityControlDefinition(BaseValidatorModel):
    SecurityControlId: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    CurrentRegionAvailability: RegionAvailabilityStatusType
    CustomizableProperties: Optional[List[Literal['Parameters']]] = None
    ParameterDefinitions: Optional[Dict[str, ParameterDefinition]] = None


class BatchGetConfigurationPolicyAssociationsResponse(BaseValidatorModel):
    ConfigurationPolicyAssociations: List[ConfigurationPolicyAssociationSummary]
    UnprocessedConfigurationPolicyAssociations: List[UnprocessedConfigurationPolicyAssociation]
    ResponseMetadata: ResponseMetadata


class AutomationRulesConfig(BaseValidatorModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersOutput] = None
    Actions: Optional[List[AutomationRulesActionOutput]] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None

AutomationRulesFindingFiltersUnion = Union[AutomationRulesFindingFilters, AutomationRulesFindingFiltersOutput]


class Insight(BaseValidatorModel):
    InsightArn: str
    Name: str
    Filters: AwsSecurityFindingFiltersOutput
    GroupByAttribute: str

AwsSecurityFindingFiltersUnion = Union[AwsSecurityFindingFilters, AwsSecurityFindingFiltersOutput]


class Sequence(BaseValidatorModel):
    Uid: Optional[str] = None
    Actors: Optional[List[Actor]] = None
    Endpoints: Optional[List[NetworkEndpoint]] = None
    Signals: Optional[List[SignalUnion]] = None
    SequenceIndicators: Optional[List[IndicatorUnion]] = None


class NetworkPathComponentOutput(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderOutput] = None
    Ingress: Optional[NetworkHeaderOutput] = None


class NetworkHeader(BaseValidatorModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsUnion] = None
    Source: Optional[NetworkPathComponentDetailsUnion] = None


class CustomDataIdentifiersDetectionsOutput(BaseValidatorModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesOutput] = None


class SensitiveDataDetectionsOutput(BaseValidatorModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesOutput] = None

OccurrencesUnion = Union[Occurrences, OccurrencesOutput]


class SecurityControlsConfigurationOutput(BaseValidatorModel):
    EnabledSecurityControlIdentifiers: Optional[List[str]] = None
    DisabledSecurityControlIdentifiers: Optional[List[str]] = None
    SecurityControlCustomParameters: Optional[List[SecurityControlCustomParameterOutput]] = None


class BatchGetSecurityControlsResponse(BaseValidatorModel):
    SecurityControls: List[SecurityControl]
    UnprocessedIds: List[UnprocessedSecurityControl]
    ResponseMetadata: ResponseMetadata

ParameterConfigurationUnion = Union[ParameterConfiguration, ParameterConfigurationOutput]


class SecurityControlCustomParameter(BaseValidatorModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Dict[str, ParameterConfiguration]] = None

RuleGroupSourceStatefulRulesDetailsUnion = Union[RuleGroupSourceStatefulRulesDetails, RuleGroupSourceStatefulRulesDetailsOutput]


class RuleGroupSourceStatelessRulesDetailsOutput(BaseValidatorModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionOutput] = None

RuleGroupSourceStatelessRuleMatchAttributesUnion = Union[RuleGroupSourceStatelessRuleMatchAttributes, RuleGroupSourceStatelessRuleMatchAttributesOutput]

RuleGroupVariablesUnion = Union[RuleGroupVariables, RuleGroupVariablesOutput]

ComplianceUnion = Union[Compliance, ComplianceOutput]


class FirewallPolicyStatelessCustomActionsDetailsOutput(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutput] = None
    ActionName: Optional[str] = None


class RuleGroupSourceCustomActionsDetailsOutput(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutput] = None
    ActionName: Optional[str] = None


class StatelessCustomActionDefinition(BaseValidatorModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionUnion] = None


class ActionOutput(BaseValidatorModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionAction] = None
    AwsApiCallAction: Optional[AwsApiCallActionOutput] = None
    DnsRequestAction: Optional[DnsRequestAction] = None
    PortProbeAction: Optional[PortProbeActionOutput] = None

PortProbeActionUnion = Union[PortProbeAction, PortProbeActionOutput]


class DetectionOutput(BaseValidatorModel):
    Sequence: Optional[SequenceOutput] = None

AutomationRulesActionUnion = Union[AutomationRulesAction, AutomationRulesActionOutput]

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnion = Union[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails, AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutput]


class AwsBackupBackupPlanDetailsOutput(BaseValidatorModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsOutput] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None


class AwsBackupBackupPlanBackupPlanDetails(BaseValidatorModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnion]] = None
    BackupPlanRule: Optional[List[AwsBackupBackupPlanRuleDetailsUnion]] = None


class AwsCertificateManagerCertificateDetails(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[List[AwsCertificateManagerCertificateDomainValidationOptionUnion]] = None
    ExtendedKeyUsages: Optional[List[AwsCertificateManagerCertificateExtendedKeyUsage]] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[List[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[List[AwsCertificateManagerCertificateKeyUsage]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptions] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[AwsCertificateManagerCertificateRenewalSummaryUnion] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    Type: Optional[str] = None


class AwsCloudFrontDistributionDetailsOutput(BaseValidatorModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsOutput] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehavior] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLogging] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsOutput] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsOutput] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificate] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None


class AwsCloudFrontDistributionOriginGroup(BaseValidatorModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverUnion] = None


class AwsCloudFrontDistributionOriginItem(BaseValidatorModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfig] = None
    CustomOriginConfig: Optional[AwsCloudFrontDistributionOriginCustomOriginConfigUnion] = None

AwsCodeBuildProjectDetailsUnion = Union[AwsCodeBuildProjectDetails, AwsCodeBuildProjectDetailsOutput]


class AwsDynamoDbTableDetails(BaseValidatorModel):
    AttributeDefinitions: Optional[List[AwsDynamoDbTableAttributeDefinition]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummary] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[List[AwsDynamoDbTableGlobalSecondaryIndexUnion]] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[List[AwsDynamoDbTableLocalSecondaryIndexUnion]] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None
    Replicas: Optional[List[AwsDynamoDbTableReplicaUnion]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummary] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescription] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecification] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

AwsEc2LaunchTemplateDataDetailsUnion = Union[AwsEc2LaunchTemplateDataDetails, AwsEc2LaunchTemplateDataDetailsOutput]

AwsEc2SecurityGroupDetailsUnion = Union[AwsEc2SecurityGroupDetails, AwsEc2SecurityGroupDetailsOutput]

AwsEc2VpcPeeringConnectionDetailsUnion = Union[AwsEc2VpcPeeringConnectionDetails, AwsEc2VpcPeeringConnectionDetailsOutput]


class AwsEc2VpnConnectionDetails(BaseValidatorModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[List[AwsEc2VpnConnectionVgwTelemetryDetails]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsUnion] = None
    Routes: Optional[List[AwsEc2VpnConnectionRoutesDetails]] = None
    TransitGatewayId: Optional[str] = None

AwsEcsClusterDetailsUnion = Union[AwsEcsClusterDetails, AwsEcsClusterDetailsOutput]

AwsEcsTaskDetailsUnion = Union[AwsEcsTaskDetails, AwsEcsTaskDetailsOutput]


class AwsEcsServiceDetails(BaseValidatorModel):
    CapacityProviderStrategy: Optional[List[AwsEcsServiceCapacityProviderStrategyDetails]] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetails] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetails] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[List[AwsEcsServiceLoadBalancersDetails]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[AwsEcsServiceNetworkConfigurationDetailsUnion] = None
    PlacementConstraints: Optional[List[AwsEcsServicePlacementConstraintsDetails]] = None
    PlacementStrategies: Optional[List[AwsEcsServicePlacementStrategiesDetails]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[List[AwsEcsServiceServiceRegistriesDetails]] = None
    TaskDefinition: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsDetails(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails]] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[List[str]] = None
    DnsServers: Optional[List[str]] = None
    DockerLabels: Optional[Dict[str, str]] = None
    DockerSecurityOptions: Optional[List[str]] = None
    EntryPoint: Optional[List[str]] = None
    Environment: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails]] = None
    EnvironmentFiles: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails]] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails]] = None
    FirelensConfiguration: Optional[AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnion] = None
    HealthCheck: Optional[AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnion] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[List[str]] = None
    LinuxParameters: Optional[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnion] = None
    LogConfiguration: Optional[AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnion] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails]] = None
    Name: Optional[str] = None
    PortMappings: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails]] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails] = None
    ResourceRequirements: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails]] = None
    Secrets: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails]] = None
    Ulimits: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails]] = None
    WorkingDirectory: Optional[str] = None


class AwsEksClusterDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsUnion] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsUnion] = None

AwsElbLoadBalancerDetailsUnion = Union[AwsElbLoadBalancerDetails, AwsElbLoadBalancerDetailsOutput]

AwsEventsEndpointDetailsUnion = Union[AwsEventsEndpointDetails, AwsEventsEndpointDetailsOutput]


class AwsGuardDutyDetectorDetailsOutput(BaseValidatorModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetails] = None
    Features: Optional[List[AwsGuardDutyDetectorFeaturesDetails]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None


class AwsGuardDutyDetectorDetails(BaseValidatorModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetails] = None
    Features: Optional[List[AwsGuardDutyDetectorFeaturesDetails]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None

AwsIamRoleDetailsUnion = Union[AwsIamRoleDetails, AwsIamRoleDetailsOutput]

AwsLambdaFunctionDetailsUnion = Union[AwsLambdaFunctionDetails, AwsLambdaFunctionDetailsOutput]


class AwsMskClusterDetailsOutput(BaseValidatorModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsOutput] = None


class AwsMskClusterClusterInfoDetails(BaseValidatorModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetails] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[AwsMskClusterClusterInfoClientAuthenticationDetailsUnion] = None
    EnhancedMonitoring: Optional[str] = None


class AwsRdsDbInstanceDetails(BaseValidatorModel):
    AssociatedRoles: Optional[List[AwsRdsDbInstanceAssociatedRole]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroup]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[List[str]] = None
    DbParameterGroups: Optional[List[AwsRdsDbParameterGroup]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupUnion] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesUnion] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[AwsRdsDbOptionGroupMembership]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[List[AwsRdsDbStatusInfo]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembership]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    MaxAllocatedStorage: Optional[int] = None

AwsRedshiftClusterDetailsUnion = Union[AwsRedshiftClusterDetails, AwsRedshiftClusterDetailsOutput]


class AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutput(BaseValidatorModel):
    AbortIncompleteMultipartUpload: Optional[AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutput] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails]] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails]] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails(BaseValidatorModel):
    Predicate: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnion] = None


class AwsS3BucketNotificationConfigurationOutput(BaseValidatorModel):
    Configurations: Optional[List[AwsS3BucketNotificationConfigurationDetailOutput]] = None

AwsS3BucketNotificationConfigurationFilterUnion = Union[AwsS3BucketNotificationConfigurationFilter, AwsS3BucketNotificationConfigurationFilterOutput]


class AwsStepFunctionStateMachineDetails(BaseValidatorModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[AwsStepFunctionStateMachineLoggingConfigurationDetailsUnion] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[AwsStepFunctionStateMachineTracingConfigurationDetails] = None
    Type: Optional[str] = None

AwsWafWebAclDetailsUnion = Union[AwsWafWebAclDetails, AwsWafWebAclDetailsOutput]

AwsWafv2ActionAllowDetailsUnion = Union[AwsWafv2ActionAllowDetails, AwsWafv2ActionAllowDetailsOutput]

AwsWafv2RulesActionCaptchaDetailsUnion = Union[AwsWafv2RulesActionCaptchaDetails, AwsWafv2RulesActionCaptchaDetailsOutput]

AwsWafv2RulesActionCountDetailsUnion = Union[AwsWafv2RulesActionCountDetails, AwsWafv2RulesActionCountDetailsOutput]


class AwsWafv2RulesDetailsOutput(BaseValidatorModel):
    Action: Optional[AwsWafv2RulesActionDetailsOutput] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None

AwsWafv2ActionBlockDetailsUnion = Union[AwsWafv2ActionBlockDetails, AwsWafv2ActionBlockDetailsOutput]

VulnerabilityUnion = Union[Vulnerability, VulnerabilityOutput]


class GetSecurityControlDefinitionResponse(BaseValidatorModel):
    SecurityControlDefinition: SecurityControlDefinition
    ResponseMetadata: ResponseMetadata


class ListSecurityControlDefinitionsResponse(BaseValidatorModel):
    SecurityControlDefinitions: List[SecurityControlDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetAutomationRulesResponse(BaseValidatorModel):
    Rules: List[AutomationRulesConfig]
    UnprocessedAutomationRules: List[UnprocessedAutomationRule]
    ResponseMetadata: ResponseMetadata


class GetInsightsResponse(BaseValidatorModel):
    Insights: List[Insight]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateInsightRequest(BaseValidatorModel):
    Name: str
    Filters: AwsSecurityFindingFiltersUnion
    GroupByAttribute: str


class GetFindingsRequestPaginate(BaseValidatorModel):
    Filters: Optional[AwsSecurityFindingFiltersUnion] = None
    SortCriteria: Optional[List[SortCriterion]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetFindingsRequest(BaseValidatorModel):
    Filters: Optional[AwsSecurityFindingFiltersUnion] = None
    SortCriteria: Optional[List[SortCriterion]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UpdateFindingsRequest(BaseValidatorModel):
    Filters: AwsSecurityFindingFiltersUnion
    Note: Optional[NoteUpdate] = None
    RecordState: Optional[RecordStateType] = None


class UpdateInsightRequest(BaseValidatorModel):
    InsightArn: str
    Name: Optional[str] = None
    Filters: Optional[AwsSecurityFindingFiltersUnion] = None
    GroupByAttribute: Optional[str] = None

SequenceUnion = Union[Sequence, SequenceOutput]

NetworkHeaderUnion = Union[NetworkHeader, NetworkHeaderOutput]


class CustomDataIdentifiersResultOutput(BaseValidatorModel):
    Detections: Optional[List[CustomDataIdentifiersDetectionsOutput]] = None
    TotalCount: Optional[int] = None


class SensitiveDataResultOutput(BaseValidatorModel):
    Category: Optional[str] = None
    Detections: Optional[List[SensitiveDataDetectionsOutput]] = None
    TotalCount: Optional[int] = None


class CustomDataIdentifiersDetections(BaseValidatorModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesUnion] = None


class SensitiveDataDetections(BaseValidatorModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesUnion] = None


class SecurityHubPolicyOutput(BaseValidatorModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[List[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfigurationOutput] = None


class UpdateSecurityControlRequest(BaseValidatorModel):
    SecurityControlId: str
    Parameters: Dict[str, ParameterConfigurationUnion]
    LastUpdateReason: Optional[str] = None


class SecurityControlsConfiguration(BaseValidatorModel):
    EnabledSecurityControlIdentifiers: Optional[List[str]] = None
    DisabledSecurityControlIdentifiers: Optional[List[str]] = None
    SecurityControlCustomParameters: Optional[List[SecurityControlCustomParameter]] = None


class RuleGroupSourceStatelessRuleDefinition(BaseValidatorModel):
    Actions: Optional[List[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesUnion] = None


class FirewallPolicyDetailsOutput(BaseValidatorModel):
    StatefulRuleGroupReferences: Optional[List[FirewallPolicyStatefulRuleGroupReferencesDetails]] = None
    StatelessCustomActions: Optional[List[FirewallPolicyStatelessCustomActionsDetailsOutput]] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessRuleGroupReferences: Optional[List[FirewallPolicyStatelessRuleGroupReferencesDetails]] = None


class RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutput(BaseValidatorModel):
    CustomActions: Optional[List[RuleGroupSourceCustomActionsDetailsOutput]] = None
    StatelessRules: Optional[List[RuleGroupSourceStatelessRulesDetailsOutput]] = None

StatelessCustomActionDefinitionUnion = Union[StatelessCustomActionDefinition, StatelessCustomActionDefinitionOutput]


class Action(BaseValidatorModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionAction] = None
    AwsApiCallAction: Optional[AwsApiCallActionUnion] = None
    DnsRequestAction: Optional[DnsRequestAction] = None
    PortProbeAction: Optional[PortProbeActionUnion] = None


class CreateAutomationRuleRequest(BaseValidatorModel):
    RuleOrder: int
    RuleName: str
    Description: str
    Criteria: AutomationRulesFindingFiltersUnion
    Actions: List[AutomationRulesActionUnion]
    Tags: Optional[Dict[str, str]] = None
    RuleStatus: Optional[RuleStatusType] = None
    IsTerminal: Optional[bool] = None


class UpdateAutomationRulesRequestItem(BaseValidatorModel):
    RuleArn: str
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    Description: Optional[str] = None
    RuleName: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersUnion] = None
    Actions: Optional[List[AutomationRulesActionUnion]] = None


class AwsAutoScalingAutoScalingGroupDetails(BaseValidatorModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnion] = None
    AvailabilityZones: Optional[List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails]] = None
    LaunchTemplate: Optional[AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification] = None
    CapacityRebalance: Optional[bool] = None

AwsBackupBackupPlanBackupPlanDetailsUnion = Union[AwsBackupBackupPlanBackupPlanDetails, AwsBackupBackupPlanBackupPlanDetailsOutput]

AwsCertificateManagerCertificateDetailsUnion = Union[AwsCertificateManagerCertificateDetails, AwsCertificateManagerCertificateDetailsOutput]

AwsCloudFrontDistributionOriginGroupUnion = Union[AwsCloudFrontDistributionOriginGroup, AwsCloudFrontDistributionOriginGroupOutput]

AwsCloudFrontDistributionOriginItemUnion = Union[AwsCloudFrontDistributionOriginItem, AwsCloudFrontDistributionOriginItemOutput]

AwsDynamoDbTableDetailsUnion = Union[AwsDynamoDbTableDetails, AwsDynamoDbTableDetailsOutput]


class AwsEc2LaunchTemplateDetails(BaseValidatorModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsUnion] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None

AwsEc2VpnConnectionDetailsUnion = Union[AwsEc2VpnConnectionDetails, AwsEc2VpnConnectionDetailsOutput]

AwsEcsServiceDetailsUnion = Union[AwsEcsServiceDetails, AwsEcsServiceDetailsOutput]

AwsEcsTaskDefinitionContainerDefinitionsDetailsUnion = Union[AwsEcsTaskDefinitionContainerDefinitionsDetails, AwsEcsTaskDefinitionContainerDefinitionsDetailsOutput]

AwsEksClusterDetailsUnion = Union[AwsEksClusterDetails, AwsEksClusterDetailsOutput]

AwsGuardDutyDetectorDetailsUnion = Union[AwsGuardDutyDetectorDetails, AwsGuardDutyDetectorDetailsOutput]

AwsMskClusterClusterInfoDetailsUnion = Union[AwsMskClusterClusterInfoDetails, AwsMskClusterClusterInfoDetailsOutput]

AwsRdsDbInstanceDetailsUnion = Union[AwsRdsDbInstanceDetails, AwsRdsDbInstanceDetailsOutput]


class AwsS3BucketBucketLifecycleConfigurationDetailsOutput(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutput]] = None

AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnion = Union[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails, AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutput]


class AwsS3BucketNotificationConfigurationDetail(BaseValidatorModel):
    Events: Optional[List[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterUnion] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None

AwsStepFunctionStateMachineDetailsUnion = Union[AwsStepFunctionStateMachineDetails, AwsStepFunctionStateMachineDetailsOutput]


class AwsWafv2RuleGroupDetailsOutput(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutput]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class AwsWafv2WebAclDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetails] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsOutput] = None
    Description: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutput]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class AwsWafv2RulesActionDetails(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsUnion] = None
    Block: Optional[AwsWafv2ActionBlockDetailsUnion] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsUnion] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsUnion] = None


class AwsWafv2WebAclActionDetails(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsUnion] = None
    Block: Optional[AwsWafv2ActionBlockDetailsUnion] = None


class Detection(BaseValidatorModel):
    Sequence: Optional[SequenceUnion] = None


class NetworkPathComponent(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderUnion] = None
    Ingress: Optional[NetworkHeaderUnion] = None


class ClassificationResultOutput(BaseValidatorModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatus] = None
    SensitiveData: Optional[List[SensitiveDataResultOutput]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultOutput] = None

CustomDataIdentifiersDetectionsUnion = Union[CustomDataIdentifiersDetections, CustomDataIdentifiersDetectionsOutput]

SensitiveDataDetectionsUnion = Union[SensitiveDataDetections, SensitiveDataDetectionsOutput]


class PolicyOutput(BaseValidatorModel):
    SecurityHub: Optional[SecurityHubPolicyOutput] = None


class SecurityHubPolicy(BaseValidatorModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[List[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfiguration] = None

RuleGroupSourceStatelessRuleDefinitionUnion = Union[RuleGroupSourceStatelessRuleDefinition, RuleGroupSourceStatelessRuleDefinitionOutput]


class AwsNetworkFirewallFirewallPolicyDetailsOutput(BaseValidatorModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsOutput] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None


class RuleGroupSourceOutput(BaseValidatorModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsOutput] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[List[RuleGroupSourceStatefulRulesDetailsOutput]] = None
    StatelessRulesAndCustomActions: Optional[RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutput] = None


class FirewallPolicyStatelessCustomActionsDetails(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionUnion] = None
    ActionName: Optional[str] = None


class RuleGroupSourceCustomActionsDetails(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionUnion] = None
    ActionName: Optional[str] = None

ActionUnion = Union[Action, ActionOutput]


class BatchUpdateAutomationRulesRequest(BaseValidatorModel):
    UpdateAutomationRulesRequestItems: List[UpdateAutomationRulesRequestItem]

AwsAutoScalingAutoScalingGroupDetailsUnion = Union[AwsAutoScalingAutoScalingGroupDetails, AwsAutoScalingAutoScalingGroupDetailsOutput]


class AwsBackupBackupPlanDetails(BaseValidatorModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsUnion] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None


class AwsCloudFrontDistributionOriginGroups(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginGroupUnion]] = None


class AwsCloudFrontDistributionOrigins(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginItemUnion]] = None

AwsEc2LaunchTemplateDetailsUnion = Union[AwsEc2LaunchTemplateDetails, AwsEc2LaunchTemplateDetailsOutput]


class AwsEcsTaskDefinitionDetails(BaseValidatorModel):
    ContainerDefinitions: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsDetailsUnion]] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[List[AwsEcsTaskDefinitionInferenceAcceleratorsDetails]] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[List[AwsEcsTaskDefinitionPlacementConstraintsDetails]] = None
    ProxyConfiguration: Optional[AwsEcsTaskDefinitionProxyConfigurationDetailsUnion] = None
    RequiresCompatibilities: Optional[List[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskDefinitionVolumesDetailsUnion]] = None
    Status: Optional[str] = None


class AwsMskClusterDetails(BaseValidatorModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsUnion] = None


class AwsS3BucketDetailsOutput(BaseValidatorModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[AwsS3BucketServerSideEncryptionConfigurationOutput] = None
    BucketLifecycleConfiguration: Optional[AwsS3BucketBucketLifecycleConfigurationDetailsOutput] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfiguration] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationOutput] = None
    BucketNotificationConfiguration: Optional[AwsS3BucketNotificationConfigurationOutput] = None
    BucketVersioningConfiguration: Optional[AwsS3BucketBucketVersioningConfiguration] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfiguration] = None
    Name: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesDetails(BaseValidatorModel):
    AbortIncompleteMultipartUpload: Optional[AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnion] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails]] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails]] = None

AwsS3BucketNotificationConfigurationDetailUnion = Union[AwsS3BucketNotificationConfigurationDetail, AwsS3BucketNotificationConfigurationDetailOutput]

AwsWafv2RulesActionDetailsUnion = Union[AwsWafv2RulesActionDetails, AwsWafv2RulesActionDetailsOutput]

AwsWafv2WebAclActionDetailsUnion = Union[AwsWafv2WebAclActionDetails, AwsWafv2WebAclActionDetailsOutput]

DetectionUnion = Union[Detection, DetectionOutput]

NetworkPathComponentUnion = Union[NetworkPathComponent, NetworkPathComponentOutput]


class DataClassificationDetailsOutput(BaseValidatorModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultOutput] = None


class CustomDataIdentifiersResult(BaseValidatorModel):
    Detections: Optional[List[CustomDataIdentifiersDetectionsUnion]] = None
    TotalCount: Optional[int] = None


class SensitiveDataResult(BaseValidatorModel):
    Category: Optional[str] = None
    Detections: Optional[List[SensitiveDataDetectionsUnion]] = None
    TotalCount: Optional[int] = None


class CreateConfigurationPolicyResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutput
    ResponseMetadata: ResponseMetadata


class GetConfigurationPolicyResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutput
    ResponseMetadata: ResponseMetadata


class UpdateConfigurationPolicyResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutput
    ResponseMetadata: ResponseMetadata


class Policy(BaseValidatorModel):
    SecurityHub: Optional[SecurityHubPolicy] = None


class RuleGroupSourceStatelessRulesDetails(BaseValidatorModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionUnion] = None


class RuleGroupDetailsOutput(BaseValidatorModel):
    RuleVariables: Optional[RuleGroupVariablesOutput] = None
    RulesSource: Optional[RuleGroupSourceOutput] = None

FirewallPolicyStatelessCustomActionsDetailsUnion = Union[FirewallPolicyStatelessCustomActionsDetails, FirewallPolicyStatelessCustomActionsDetailsOutput]

RuleGroupSourceCustomActionsDetailsUnion = Union[RuleGroupSourceCustomActionsDetails, RuleGroupSourceCustomActionsDetailsOutput]

AwsBackupBackupPlanDetailsUnion = Union[AwsBackupBackupPlanDetails, AwsBackupBackupPlanDetailsOutput]

AwsCloudFrontDistributionOriginGroupsUnion = Union[AwsCloudFrontDistributionOriginGroups, AwsCloudFrontDistributionOriginGroupsOutput]

AwsCloudFrontDistributionOriginsUnion = Union[AwsCloudFrontDistributionOrigins, AwsCloudFrontDistributionOriginsOutput]

AwsEcsTaskDefinitionDetailsUnion = Union[AwsEcsTaskDefinitionDetails, AwsEcsTaskDefinitionDetailsOutput]

AwsMskClusterDetailsUnion = Union[AwsMskClusterDetails, AwsMskClusterDetailsOutput]

AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnion = Union[AwsS3BucketBucketLifecycleConfigurationRulesDetails, AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutput]


class AwsS3BucketNotificationConfiguration(BaseValidatorModel):
    Configurations: Optional[List[AwsS3BucketNotificationConfigurationDetailUnion]] = None


class AwsWafv2RulesDetails(BaseValidatorModel):
    Action: Optional[AwsWafv2RulesActionDetailsUnion] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None

CustomDataIdentifiersResultUnion = Union[CustomDataIdentifiersResult, CustomDataIdentifiersResultOutput]

SensitiveDataResultUnion = Union[SensitiveDataResult, SensitiveDataResultOutput]

PolicyUnion = Union[Policy, PolicyOutput]

RuleGroupSourceStatelessRulesDetailsUnion = Union[RuleGroupSourceStatelessRulesDetails, RuleGroupSourceStatelessRulesDetailsOutput]


class AwsNetworkFirewallRuleGroupDetailsOutput(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsOutput] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None


class FirewallPolicyDetails(BaseValidatorModel):
    StatefulRuleGroupReferences: Optional[List[FirewallPolicyStatefulRuleGroupReferencesDetails]] = None
    StatelessCustomActions: Optional[List[FirewallPolicyStatelessCustomActionsDetailsUnion]] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessRuleGroupReferences: Optional[List[FirewallPolicyStatelessRuleGroupReferencesDetails]] = None


class AwsCloudFrontDistributionDetails(BaseValidatorModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsUnion] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehavior] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLogging] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsUnion] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsUnion] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificate] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationDetails(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnion]] = None

AwsS3BucketNotificationConfigurationUnion = Union[AwsS3BucketNotificationConfiguration, AwsS3BucketNotificationConfigurationOutput]

AwsWafv2RulesDetailsUnion = Union[AwsWafv2RulesDetails, AwsWafv2RulesDetailsOutput]


class AwsWafv2WebAclDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetails] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsUnion] = None
    Description: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetails]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class ClassificationResult(BaseValidatorModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatus] = None
    SensitiveData: Optional[List[SensitiveDataResultUnion]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultUnion] = None


class CreateConfigurationPolicyRequest(BaseValidatorModel):
    Name: str
    ConfigurationPolicy: PolicyUnion
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateConfigurationPolicyRequest(BaseValidatorModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedReason: Optional[str] = None
    ConfigurationPolicy: Optional[PolicyUnion] = None


class RuleGroupSourceStatelessRulesAndCustomActionsDetails(BaseValidatorModel):
    CustomActions: Optional[List[RuleGroupSourceCustomActionsDetailsUnion]] = None
    StatelessRules: Optional[List[RuleGroupSourceStatelessRulesDetailsUnion]] = None


class ResourceDetailsOutput(BaseValidatorModel):
    AwsAutoScalingAutoScalingGroup: Optional[AwsAutoScalingAutoScalingGroupDetailsOutput] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsOutput] = None
    AwsCloudFrontDistribution: Optional[AwsCloudFrontDistributionDetailsOutput] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsOutput] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsOutput] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsOutput] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsOutput] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsOutput] = None
    AwsEc2Eip: Optional[AwsEc2EipDetails] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsOutput] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsOutput] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsOutput] = None
    AwsElasticBeanstalkEnvironment: Optional[AwsElasticBeanstalkEnvironmentDetailsOutput] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsOutput] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsOutput] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    AwsS3Object: Optional[AwsS3ObjectDetails] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetails] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetails] = None
    AwsIamUser: Optional[AwsIamUserDetailsOutput] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsOutput] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsOutput] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsOutput] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsOutput] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsOutput] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsOutput] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetails] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetails] = None
    AwsCertificateManagerCertificate: Optional[AwsCertificateManagerCertificateDetailsOutput] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsOutput] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsOutput] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsOutput] = None
    AwsIamRole: Optional[AwsIamRoleDetailsOutput] = None
    AwsKmsKey: Optional[AwsKmsKeyDetails] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsOutput] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsOutput] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsOutput] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsOutput] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetails] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsOutput] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsOutput] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsOutput] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsOutput] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsOutput] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsOutput] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsOutput] = None
    Container: Optional[ContainerDetailsOutput] = None
    Other: Optional[Dict[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsOutput] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsOutput] = None
    AwsAutoScalingLaunchConfiguration: Optional[AwsAutoScalingLaunchConfigurationDetailsOutput] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsOutput] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsOutput] = None
    AwsOpenSearchServiceDomain: Optional[AwsOpenSearchServiceDomainDetailsOutput] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsOutput] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetails] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsOutput] = None
    AwsWafRegionalRateBasedRule: Optional[AwsWafRegionalRateBasedRuleDetailsOutput] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetails] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsOutput] = None
    AwsNetworkFirewallFirewallPolicy: Optional[AwsNetworkFirewallFirewallPolicyDetailsOutput] = None
    AwsNetworkFirewallFirewall: Optional[AwsNetworkFirewallFirewallDetailsOutput] = None
    AwsNetworkFirewallRuleGroup: Optional[AwsNetworkFirewallRuleGroupDetailsOutput] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsOutput] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetails] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsOutput] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsOutput] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsOutput] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsOutput] = None
    AwsEc2VpcPeeringConnection: Optional[AwsEc2VpcPeeringConnectionDetailsOutput] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsOutput] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsOutput] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsOutput] = None
    AwsWafRule: Optional[AwsWafRuleDetailsOutput] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsOutput] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsOutput] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsOutput] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsOutput] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetails] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsOutput] = None
    AwsSageMakerNotebookInstance: Optional[AwsSageMakerNotebookInstanceDetailsOutput] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsOutput] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsOutput] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsOutput] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsOutput] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsOutput] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetails] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsOutput] = None
    AwsStepFunctionStateMachine: Optional[AwsStepFunctionStateMachineDetailsOutput] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetails] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetails] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetails] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsOutput] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetails] = None
    AwsDmsReplicationInstance: Optional[AwsDmsReplicationInstanceDetailsOutput] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsOutput] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsOutput] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetails] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsOutput] = None

FirewallPolicyDetailsUnion = Union[FirewallPolicyDetails, FirewallPolicyDetailsOutput]

AwsCloudFrontDistributionDetailsUnion = Union[AwsCloudFrontDistributionDetails, AwsCloudFrontDistributionDetailsOutput]

AwsS3BucketBucketLifecycleConfigurationDetailsUnion = Union[AwsS3BucketBucketLifecycleConfigurationDetails, AwsS3BucketBucketLifecycleConfigurationDetailsOutput]


class AwsWafv2RuleGroupDetails(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsUnion]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None

AwsWafv2WebAclDetailsUnion = Union[AwsWafv2WebAclDetails, AwsWafv2WebAclDetailsOutput]

ClassificationResultUnion = Union[ClassificationResult, ClassificationResultOutput]

RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnion = Union[RuleGroupSourceStatelessRulesAndCustomActionsDetails, RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutput]


class ResourceOutput(BaseValidatorModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsOutput] = None
    Details: Optional[ResourceDetailsOutput] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None


class AwsNetworkFirewallFirewallPolicyDetails(BaseValidatorModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsUnion] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None


class AwsS3BucketDetails(BaseValidatorModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[AwsS3BucketServerSideEncryptionConfigurationUnion] = None
    BucketLifecycleConfiguration: Optional[AwsS3BucketBucketLifecycleConfigurationDetailsUnion] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfiguration] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationUnion] = None
    BucketNotificationConfiguration: Optional[AwsS3BucketNotificationConfigurationUnion] = None
    BucketVersioningConfiguration: Optional[AwsS3BucketBucketVersioningConfiguration] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfiguration] = None
    Name: Optional[str] = None

AwsWafv2RuleGroupDetailsUnion = Union[AwsWafv2RuleGroupDetails, AwsWafv2RuleGroupDetailsOutput]


class DataClassificationDetails(BaseValidatorModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultUnion] = None


class RuleGroupSource(BaseValidatorModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsUnion] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[List[RuleGroupSourceStatefulRulesDetailsUnion]] = None
    StatelessRulesAndCustomActions: Optional[RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnion] = None


class AwsSecurityFindingOutput(BaseValidatorModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceOutput]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[List[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[Severity] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[Remediation] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Dict[str, str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Malware: Optional[List[Malware]] = None
    Network: Optional[Network] = None
    NetworkPath: Optional[List[NetworkPathComponentOutput]] = None
    Process: Optional[ProcessDetails] = None
    Threats: Optional[List[ThreatOutput]] = None
    ThreatIntelIndicators: Optional[List[ThreatIntelIndicator]] = None
    Compliance: Optional[ComplianceOutput] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[Workflow] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None
    Note: Optional[Note] = None
    Vulnerabilities: Optional[List[VulnerabilityOutput]] = None
    PatchSummary: Optional[PatchSummary] = None
    Action: Optional[ActionOutput] = None
    FindingProviderFields: Optional[FindingProviderFieldsOutput] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsOutput] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None
    Detection: Optional[DetectionOutput] = None

AwsNetworkFirewallFirewallPolicyDetailsUnion = Union[AwsNetworkFirewallFirewallPolicyDetails, AwsNetworkFirewallFirewallPolicyDetailsOutput]

AwsS3BucketDetailsUnion = Union[AwsS3BucketDetails, AwsS3BucketDetailsOutput]

DataClassificationDetailsUnion = Union[DataClassificationDetails, DataClassificationDetailsOutput]

RuleGroupSourceUnion = Union[RuleGroupSource, RuleGroupSourceOutput]


class GetFindingsResponse(BaseValidatorModel):
    Findings: List[AwsSecurityFindingOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RuleGroupDetails(BaseValidatorModel):
    RuleVariables: Optional[RuleGroupVariablesUnion] = None
    RulesSource: Optional[RuleGroupSourceUnion] = None

RuleGroupDetailsUnion = Union[RuleGroupDetails, RuleGroupDetailsOutput]


class AwsNetworkFirewallRuleGroupDetails(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsUnion] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None

AwsNetworkFirewallRuleGroupDetailsUnion = Union[AwsNetworkFirewallRuleGroupDetails, AwsNetworkFirewallRuleGroupDetailsOutput]


class ResourceDetails(BaseValidatorModel):
    AwsAutoScalingAutoScalingGroup: Optional[AwsAutoScalingAutoScalingGroupDetailsUnion] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsUnion] = None
    AwsCloudFrontDistribution: Optional[AwsCloudFrontDistributionDetailsUnion] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsUnion] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsUnion] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsUnion] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsUnion] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsUnion] = None
    AwsEc2Eip: Optional[AwsEc2EipDetails] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsUnion] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsUnion] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsUnion] = None
    AwsElasticBeanstalkEnvironment: Optional[AwsElasticBeanstalkEnvironmentDetailsUnion] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsUnion] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsUnion] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    AwsS3Object: Optional[AwsS3ObjectDetails] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetails] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetails] = None
    AwsIamUser: Optional[AwsIamUserDetailsUnion] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsUnion] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsUnion] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsUnion] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsUnion] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsUnion] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsUnion] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetails] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetails] = None
    AwsCertificateManagerCertificate: Optional[AwsCertificateManagerCertificateDetailsUnion] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsUnion] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsUnion] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsUnion] = None
    AwsIamRole: Optional[AwsIamRoleDetailsUnion] = None
    AwsKmsKey: Optional[AwsKmsKeyDetails] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsUnion] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsUnion] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsUnion] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsUnion] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetails] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsUnion] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsUnion] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsUnion] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsUnion] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsUnion] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsUnion] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsUnion] = None
    Container: Optional[ContainerDetailsUnion] = None
    Other: Optional[Dict[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsUnion] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsUnion] = None
    AwsAutoScalingLaunchConfiguration: Optional[AwsAutoScalingLaunchConfigurationDetailsUnion] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsUnion] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsUnion] = None
    AwsOpenSearchServiceDomain: Optional[AwsOpenSearchServiceDomainDetailsUnion] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsUnion] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetails] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsUnion] = None
    AwsWafRegionalRateBasedRule: Optional[AwsWafRegionalRateBasedRuleDetailsUnion] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetails] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsUnion] = None
    AwsNetworkFirewallFirewallPolicy: Optional[AwsNetworkFirewallFirewallPolicyDetailsUnion] = None
    AwsNetworkFirewallFirewall: Optional[AwsNetworkFirewallFirewallDetailsUnion] = None
    AwsNetworkFirewallRuleGroup: Optional[AwsNetworkFirewallRuleGroupDetailsUnion] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsUnion] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetails] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsUnion] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsUnion] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsUnion] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsUnion] = None
    AwsEc2VpcPeeringConnection: Optional[AwsEc2VpcPeeringConnectionDetailsUnion] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsUnion] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsUnion] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsUnion] = None
    AwsWafRule: Optional[AwsWafRuleDetailsUnion] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsUnion] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsUnion] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsUnion] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsUnion] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetails] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsUnion] = None
    AwsSageMakerNotebookInstance: Optional[AwsSageMakerNotebookInstanceDetailsUnion] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsUnion] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsUnion] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsUnion] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsUnion] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsUnion] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetails] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsUnion] = None
    AwsStepFunctionStateMachine: Optional[AwsStepFunctionStateMachineDetailsUnion] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetails] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetails] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetails] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsUnion] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetails] = None
    AwsDmsReplicationInstance: Optional[AwsDmsReplicationInstanceDetailsUnion] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsUnion] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsUnion] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetails] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsUnion] = None

ResourceDetailsUnion = Union[ResourceDetails, ResourceDetailsOutput]


class Resource(BaseValidatorModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsUnion] = None
    Details: Optional[ResourceDetailsUnion] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None

ResourceUnion = Union[Resource, ResourceOutput]


class AwsSecurityFinding(BaseValidatorModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceUnion]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[List[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[Severity] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[Remediation] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Dict[str, str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Malware: Optional[List[Malware]] = None
    Network: Optional[Network] = None
    NetworkPath: Optional[List[NetworkPathComponentUnion]] = None
    Process: Optional[ProcessDetails] = None
    Threats: Optional[List[ThreatUnion]] = None
    ThreatIntelIndicators: Optional[List[ThreatIntelIndicator]] = None
    Compliance: Optional[ComplianceUnion] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[Workflow] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None
    Note: Optional[Note] = None
    Vulnerabilities: Optional[List[VulnerabilityUnion]] = None
    PatchSummary: Optional[PatchSummary] = None
    Action: Optional[ActionUnion] = None
    FindingProviderFields: Optional[FindingProviderFieldsUnion] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsUnion] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None
    Detection: Optional[DetectionUnion] = None

AwsSecurityFindingUnion = Union[AwsSecurityFinding, AwsSecurityFindingOutput]


class BatchImportFindingsRequest(BaseValidatorModel):
    Findings: List[AwsSecurityFindingUnion]