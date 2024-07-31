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
from aws_resource_validator.pydantic_models.securityhub_constants import *

class AcceptAdministratorInvitationRequestRequestTypeDef(BaseModel):
    AdministratorId: str
    InvitationId: str

class AcceptInvitationRequestRequestTypeDef(BaseModel):
    MasterId: str
    InvitationId: str

class AccountDetailsTypeDef(BaseModel):
    AccountId: str
    Email: Optional[str] = None

class DnsRequestActionTypeDef(BaseModel):
    Domain: Optional[str] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None

class ActionLocalIpDetailsTypeDef(BaseModel):
    IpAddressV4: Optional[str] = None

class ActionLocalPortDetailsTypeDef(BaseModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None

class CityTypeDef(BaseModel):
    CityName: Optional[str] = None

class CountryTypeDef(BaseModel):
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None

class GeoLocationTypeDef(BaseModel):
    Lon: Optional[float] = None
    Lat: Optional[float] = None

class IpOrganizationDetailsTypeDef(BaseModel):
    Asn: Optional[int] = None
    AsnOrg: Optional[str] = None
    Isp: Optional[str] = None
    Org: Optional[str] = None

class ActionRemotePortDetailsTypeDef(BaseModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None

class ActionTargetTypeDef(BaseModel):
    ActionTargetArn: str
    Name: str
    Description: str

class AdjustmentTypeDef(BaseModel):
    Metric: Optional[str] = None
    Reason: Optional[str] = None

class AdminAccountTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Status: Optional[AdminStatusType] = None

class AssociatedStandardTypeDef(BaseModel):
    StandardsId: Optional[str] = None

class AssociationFiltersTypeDef(BaseModel):
    ConfigurationPolicyId: Optional[str] = None
    AssociationType: Optional[AssociationTypeType] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None

class AssociationStateDetailsTypeDef(BaseModel):
    State: Optional[str] = None
    StatusMessage: Optional[str] = None

class NoteUpdateTypeDef(BaseModel):
    Text: str
    UpdatedBy: str

class RelatedFindingTypeDef(BaseModel):
    ProductArn: str
    Id: str

class SeverityUpdateTypeDef(BaseModel):
    Normalized: Optional[int] = None
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None

class WorkflowUpdateTypeDef(BaseModel):
    Status: Optional[WorkflowStatusType] = None

class MapFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparison: Optional[MapFilterComparisonType] = None

class NumberFilterTypeDef(BaseModel):
    Gte: Optional[float] = None
    Lte: Optional[float] = None
    Gt: Optional[float] = None
    Lt: Optional[float] = None
    Eq: Optional[float] = None

class StringFilterTypeDef(BaseModel):
    Value: Optional[str] = None
    Comparison: Optional[StringFilterComparisonType] = None

class AutomationRulesMetadataTypeDef(BaseModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None

class AvailabilityZoneTypeDef(BaseModel):
    ZoneName: Optional[str] = None
    SubnetId: Optional[str] = None

class AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None
    UseAwsOwnedKey: Optional[bool] = None

class AwsAmazonMqBrokerLdapServerMetadataDetailsExtraOutputTypeDef(BaseModel):
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

class AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef(BaseModel):
    DayOfWeek: Optional[str] = None
    TimeOfDay: Optional[str] = None
    TimeZone: Optional[str] = None

class AwsAmazonMqBrokerUsersDetailsTypeDef(BaseModel):
    PendingChange: Optional[str] = None
    Username: Optional[str] = None

class AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef(BaseModel):
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

class AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef(BaseModel):
    Hosts: Optional[Sequence[str]] = None
    RoleBase: Optional[str] = None
    RoleName: Optional[str] = None
    RoleSearchMatching: Optional[str] = None
    RoleSearchSubtree: Optional[bool] = None
    ServiceAccountUsername: Optional[str] = None
    UserBase: Optional[str] = None
    UserRoleName: Optional[str] = None
    UserSearchMatching: Optional[str] = None
    UserSearchSubtree: Optional[bool] = None

class AwsAmazonMqBrokerLogsPendingDetailsTypeDef(BaseModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None

class AwsApiCallActionDomainDetailsTypeDef(BaseModel):
    Domain: Optional[str] = None

class AwsApiGatewayAccessLogSettingsTypeDef(BaseModel):
    Format: Optional[str] = None
    DestinationArn: Optional[str] = None

class AwsApiGatewayCanarySettingsExtraOutputTypeDef(BaseModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Dict[str, str]] = None
    UseStageCache: Optional[bool] = None

class AwsApiGatewayCanarySettingsOutputTypeDef(BaseModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Dict[str, str]] = None
    UseStageCache: Optional[bool] = None

class AwsApiGatewayCanarySettingsTypeDef(BaseModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Mapping[str, str]] = None
    UseStageCache: Optional[bool] = None

class AwsApiGatewayEndpointConfigurationExtraOutputTypeDef(BaseModel):
    Types: Optional[List[str]] = None

class AwsApiGatewayEndpointConfigurationOutputTypeDef(BaseModel):
    Types: Optional[List[str]] = None

class AwsApiGatewayEndpointConfigurationTypeDef(BaseModel):
    Types: Optional[Sequence[str]] = None

class AwsApiGatewayMethodSettingsTypeDef(BaseModel):
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

class AwsCorsConfigurationExtraOutputTypeDef(BaseModel):
    AllowOrigins: Optional[List[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[List[str]] = None
    AllowHeaders: Optional[List[str]] = None

class AwsCorsConfigurationOutputTypeDef(BaseModel):
    AllowOrigins: Optional[List[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[List[str]] = None
    AllowHeaders: Optional[List[str]] = None

class AwsCorsConfigurationTypeDef(BaseModel):
    AllowOrigins: Optional[Sequence[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowHeaders: Optional[Sequence[str]] = None

class AwsApiGatewayV2RouteSettingsTypeDef(BaseModel):
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[str] = None
    DataTraceEnabled: Optional[bool] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None

class AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef(BaseModel):
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerUri: Optional[str] = None
    IdentityValidationExpression: Optional[str] = None

class AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef(BaseModel):
    AuthTtL: Optional[int] = None
    ClientId: Optional[str] = None
    IatTtL: Optional[int] = None
    Issuer: Optional[str] = None

class AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef(BaseModel):
    AppIdClientRegex: Optional[str] = None
    AwsRegion: Optional[str] = None
    DefaultAction: Optional[str] = None
    UserPoolId: Optional[str] = None

class AwsAppSyncGraphQlApiLogConfigDetailsTypeDef(BaseModel):
    CloudWatchLogsRoleArn: Optional[str] = None
    ExcludeVerboseContent: Optional[bool] = None
    FieldLogLevel: Optional[str] = None

class AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef(BaseModel):
    EncryptionOption: Optional[str] = None
    KmsKey: Optional[str] = None

class AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef(BaseModel):
    Value: Optional[str] = None

class AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef(BaseModel):
    OnDemandAllocationStrategy: Optional[str] = None
    OnDemandBaseCapacity: Optional[int] = None
    OnDemandPercentageAboveBaseCapacity: Optional[int] = None
    SpotAllocationStrategy: Optional[str] = None
    SpotInstancePools: Optional[int] = None
    SpotMaxPrice: Optional[str] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef(BaseModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None

class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef(BaseModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None

class AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef(BaseModel):
    HttpEndpoint: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsExtraOutputTypeDef(BaseModel):
    BackupOptions: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef(BaseModel):
    BackupOptions: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef(BaseModel):
    BackupOptions: Optional[Mapping[str, str]] = None
    ResourceType: Optional[str] = None

class AwsBackupBackupPlanLifecycleDetailsTypeDef(BaseModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None

class AwsBackupBackupVaultNotificationsDetailsExtraOutputTypeDef(BaseModel):
    BackupVaultEvents: Optional[List[str]] = None
    SnsTopicArn: Optional[str] = None

class AwsBackupBackupVaultNotificationsDetailsOutputTypeDef(BaseModel):
    BackupVaultEvents: Optional[List[str]] = None
    SnsTopicArn: Optional[str] = None

class AwsBackupBackupVaultNotificationsDetailsTypeDef(BaseModel):
    BackupVaultEvents: Optional[Sequence[str]] = None
    SnsTopicArn: Optional[str] = None

class AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef(BaseModel):
    DeleteAt: Optional[str] = None
    MoveToColdStorageAt: Optional[str] = None

class AwsBackupRecoveryPointCreatedByDetailsTypeDef(BaseModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    BackupPlanVersion: Optional[str] = None
    BackupRuleId: Optional[str] = None

class AwsBackupRecoveryPointLifecycleDetailsTypeDef(BaseModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None

class AwsCertificateManagerCertificateExtendedKeyUsageTypeDef(BaseModel):
    Name: Optional[str] = None
    OId: Optional[str] = None

class AwsCertificateManagerCertificateKeyUsageTypeDef(BaseModel):
    Name: Optional[str] = None

class AwsCertificateManagerCertificateOptionsTypeDef(BaseModel):
    CertificateTransparencyLoggingPreference: Optional[str] = None

class AwsCertificateManagerCertificateResourceRecordTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsCloudFormationStackDriftInformationDetailsTypeDef(BaseModel):
    StackDriftStatus: Optional[str] = None

class AwsCloudFormationStackOutputsDetailsTypeDef(BaseModel):
    Description: Optional[str] = None
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None

class AwsCloudFrontDistributionCacheBehaviorTypeDef(BaseModel):
    ViewerProtocolPolicy: Optional[str] = None

class AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef(BaseModel):
    ViewerProtocolPolicy: Optional[str] = None

class AwsCloudFrontDistributionLoggingTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Enabled: Optional[bool] = None
    IncludeCookies: Optional[bool] = None
    Prefix: Optional[str] = None

class AwsCloudFrontDistributionViewerCertificateTypeDef(BaseModel):
    AcmCertificateArn: Optional[str] = None
    Certificate: Optional[str] = None
    CertificateSource: Optional[str] = None
    CloudFrontDefaultCertificate: Optional[bool] = None
    IamCertificateId: Optional[str] = None
    MinimumProtocolVersion: Optional[str] = None
    SslSupportMethod: Optional[str] = None

class AwsCloudFrontDistributionOriginSslProtocolsExtraOutputTypeDef(BaseModel):
    Items: Optional[List[str]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef(BaseModel):
    Items: Optional[List[str]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginSslProtocolsTypeDef(BaseModel):
    Items: Optional[Sequence[str]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesExtraOutputTypeDef(BaseModel):
    Items: Optional[List[int]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef(BaseModel):
    Items: Optional[List[int]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef(BaseModel):
    Items: Optional[Sequence[int]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginS3OriginConfigTypeDef(BaseModel):
    OriginAccessIdentity: Optional[str] = None

class AwsCloudTrailTrailDetailsTypeDef(BaseModel):
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

class AwsCloudWatchAlarmDimensionsDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsCodeBuildProjectArtifactsDetailsTypeDef(BaseModel):
    ArtifactIdentifier: Optional[str] = None
    EncryptionDisabled: Optional[bool] = None
    Location: Optional[str] = None
    Name: Optional[str] = None
    NamespaceType: Optional[str] = None
    OverrideArtifactName: Optional[bool] = None
    Packaging: Optional[str] = None
    Path: Optional[str] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectSourceTypeDef(BaseModel):
    Type: Optional[str] = None
    Location: Optional[str] = None
    GitCloneDepth: Optional[int] = None
    InsecureSsl: Optional[bool] = None

class AwsCodeBuildProjectVpcConfigExtraOutputTypeDef(BaseModel):
    VpcId: Optional[str] = None
    Subnets: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class AwsCodeBuildProjectVpcConfigOutputTypeDef(BaseModel):
    VpcId: Optional[str] = None
    Subnets: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class AwsCodeBuildProjectVpcConfigTypeDef(BaseModel):
    VpcId: Optional[str] = None
    Subnets: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef(BaseModel):
    Credential: Optional[str] = None
    CredentialProvider: Optional[str] = None

class AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef(BaseModel):
    GroupName: Optional[str] = None
    Status: Optional[str] = None
    StreamName: Optional[str] = None

class AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef(BaseModel):
    EncryptionDisabled: Optional[bool] = None
    Location: Optional[str] = None
    Status: Optional[str] = None

class AwsDmsEndpointDetailsTypeDef(BaseModel):
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

class AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef(BaseModel):
    ReplicationSubnetGroupIdentifier: Optional[str] = None

class AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef(BaseModel):
    VpcSecurityGroupId: Optional[str] = None

class AwsDmsReplicationTaskDetailsTypeDef(BaseModel):
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

class AwsDynamoDbTableAttributeDefinitionTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[str] = None

class AwsDynamoDbTableBillingModeSummaryTypeDef(BaseModel):
    BillingMode: Optional[str] = None
    LastUpdateToPayPerRequestDateTime: Optional[str] = None

class AwsDynamoDbTableKeySchemaTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    KeyType: Optional[str] = None

class AwsDynamoDbTableProvisionedThroughputTypeDef(BaseModel):
    LastDecreaseDateTime: Optional[str] = None
    LastIncreaseDateTime: Optional[str] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[int] = None
    WriteCapacityUnits: Optional[int] = None

class AwsDynamoDbTableRestoreSummaryTypeDef(BaseModel):
    SourceBackupArn: Optional[str] = None
    SourceTableArn: Optional[str] = None
    RestoreDateTime: Optional[str] = None
    RestoreInProgress: Optional[bool] = None

class AwsDynamoDbTableSseDescriptionTypeDef(BaseModel):
    InaccessibleEncryptionDateTime: Optional[str] = None
    Status: Optional[str] = None
    SseType: Optional[str] = None
    KmsMasterKeyArn: Optional[str] = None

class AwsDynamoDbTableStreamSpecificationTypeDef(BaseModel):
    StreamEnabled: Optional[bool] = None
    StreamViewType: Optional[str] = None

class AwsDynamoDbTableProjectionExtraOutputTypeDef(BaseModel):
    NonKeyAttributes: Optional[List[str]] = None
    ProjectionType: Optional[str] = None

class AwsDynamoDbTableProjectionOutputTypeDef(BaseModel):
    NonKeyAttributes: Optional[List[str]] = None
    ProjectionType: Optional[str] = None

class AwsDynamoDbTableProjectionTypeDef(BaseModel):
    NonKeyAttributes: Optional[Sequence[str]] = None
    ProjectionType: Optional[str] = None

class AwsDynamoDbTableProvisionedThroughputOverrideTypeDef(BaseModel):
    ReadCapacityUnits: Optional[int] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef(BaseModel):
    DirectoryId: Optional[str] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef(BaseModel):
    SamlProviderArn: Optional[str] = None
    SelfServiceSamlProviderArn: Optional[str] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef(BaseModel):
    ClientRootCertificateChain: Optional[str] = None

class AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None

class AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None

class AwsEc2EipDetailsTypeDef(BaseModel):
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

class AwsEc2InstanceMetadataOptionsTypeDef(BaseModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None
    InstanceMetadataTags: Optional[str] = None

class AwsEc2InstanceMonitoringDetailsTypeDef(BaseModel):
    State: Optional[str] = None

class AwsEc2InstanceNetworkInterfacesDetailsTypeDef(BaseModel):
    NetworkInterfaceId: Optional[str] = None

class AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef(BaseModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    Throughput: Optional[int] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None

class AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef(BaseModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef(BaseModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None

class AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef(BaseModel):
    CpuCredits: Optional[str] = None

class AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef(BaseModel):
    Type: Optional[str] = None

class AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef(BaseModel):
    Count: Optional[int] = None
    Type: Optional[str] = None

class AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef(BaseModel):
    Configured: Optional[bool] = None

class AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef(BaseModel):
    LicenseConfigurationArn: Optional[str] = None

class AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef(BaseModel):
    AutoRecovery: Optional[str] = None

class AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef(BaseModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpTokens: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    InstanceMetadataTags: Optional[str] = None

class AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsEc2LaunchTemplateDataPlacementDetailsTypeDef(BaseModel):
    Affinity: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    SpreadDomain: Optional[str] = None
    Tenancy: Optional[str] = None

class AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef(BaseModel):
    EnableResourceNameDnsAAAARecord: Optional[bool] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    HostnameType: Optional[str] = None

class AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef(BaseModel):
    BlockDurationMinutes: Optional[int] = None
    InstanceInterruptionBehavior: Optional[str] = None
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[str] = None
    ValidUntil: Optional[str] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef(BaseModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef(BaseModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef(BaseModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef(BaseModel):
    Max: Optional[float] = None
    Min: Optional[float] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef(BaseModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef(BaseModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef(BaseModel):
    Max: Optional[float] = None
    Min: Optional[float] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef(BaseModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef(BaseModel):
    Ipv4Prefix: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef(BaseModel):
    Ipv6Address: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef(BaseModel):
    Ipv6Prefix: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef(BaseModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None

class AwsEc2NetworkAclAssociationTypeDef(BaseModel):
    NetworkAclAssociationId: Optional[str] = None
    NetworkAclId: Optional[str] = None
    SubnetId: Optional[str] = None

class IcmpTypeCodeTypeDef(BaseModel):
    Code: Optional[int] = None
    Type: Optional[int] = None

class PortRangeFromToTypeDef(BaseModel):
    From: Optional[int] = None
    To: Optional[int] = None

class AwsEc2NetworkInterfaceAttachmentTypeDef(BaseModel):
    AttachTime: Optional[str] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    Status: Optional[str] = None

class AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef(BaseModel):
    IpV6Address: Optional[str] = None

class AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef(BaseModel):
    PrivateIpAddress: Optional[str] = None
    PrivateDnsName: Optional[str] = None

class AwsEc2NetworkInterfaceSecurityGroupTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class PropagatingVgwSetDetailsTypeDef(BaseModel):
    GatewayId: Optional[str] = None

class RouteSetDetailsTypeDef(BaseModel):
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

class AwsEc2SecurityGroupIpRangeTypeDef(BaseModel):
    CidrIp: Optional[str] = None

class AwsEc2SecurityGroupIpv6RangeTypeDef(BaseModel):
    CidrIpv6: Optional[str] = None

class AwsEc2SecurityGroupPrefixListIdTypeDef(BaseModel):
    PrefixListId: Optional[str] = None

class AwsEc2SecurityGroupUserIdGroupPairTypeDef(BaseModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None

class Ipv6CidrBlockAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None

class AwsEc2TransitGatewayDetailsExtraOutputTypeDef(BaseModel):
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

class AwsEc2TransitGatewayDetailsOutputTypeDef(BaseModel):
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

class AwsEc2TransitGatewayDetailsTypeDef(BaseModel):
    Id: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteTablePropagation: Optional[str] = None
    AutoAcceptSharedAttachments: Optional[str] = None
    DefaultRouteTableAssociation: Optional[str] = None
    TransitGatewayCidrBlocks: Optional[Sequence[str]] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    VpnEcmpSupport: Optional[str] = None
    DnsSupport: Optional[str] = None
    MulticastSupport: Optional[str] = None
    AmazonSideAsn: Optional[int] = None

class AwsEc2VolumeAttachmentTypeDef(BaseModel):
    AttachTime: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    InstanceId: Optional[str] = None
    Status: Optional[str] = None

class CidrBlockAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None

class AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef(BaseModel):
    ServiceType: Optional[str] = None

class AwsEc2VpcPeeringConnectionStatusDetailsTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class VpcInfoCidrBlockSetDetailsTypeDef(BaseModel):
    CidrBlock: Optional[str] = None

class VpcInfoIpv6CidrBlockSetDetailsTypeDef(BaseModel):
    Ipv6CidrBlock: Optional[str] = None

class VpcInfoPeeringOptionsDetailsTypeDef(BaseModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class AwsEc2VpnConnectionRoutesDetailsTypeDef(BaseModel):
    DestinationCidrBlock: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef(BaseModel):
    AcceptedRouteCount: Optional[int] = None
    CertificateArn: Optional[str] = None
    LastStatusChange: Optional[str] = None
    OutsideIpAddress: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsExtraOutputTypeDef(BaseModel):
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

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef(BaseModel):
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

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef(BaseModel):
    DpdTimeoutSeconds: Optional[int] = None
    IkeVersions: Optional[Sequence[str]] = None
    OutsideIpAddress: Optional[str] = None
    Phase1DhGroupNumbers: Optional[Sequence[int]] = None
    Phase1EncryptionAlgorithms: Optional[Sequence[str]] = None
    Phase1IntegrityAlgorithms: Optional[Sequence[str]] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2DhGroupNumbers: Optional[Sequence[int]] = None
    Phase2EncryptionAlgorithms: Optional[Sequence[str]] = None
    Phase2IntegrityAlgorithms: Optional[Sequence[str]] = None
    Phase2LifetimeSeconds: Optional[int] = None
    PreSharedKey: Optional[str] = None
    RekeyFuzzPercentage: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    TunnelInsideCidr: Optional[str] = None

class AwsEcrContainerImageDetailsExtraOutputTypeDef(BaseModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[List[str]] = None
    ImagePublishedAt: Optional[str] = None

class AwsEcrContainerImageDetailsOutputTypeDef(BaseModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[List[str]] = None
    ImagePublishedAt: Optional[str] = None

class AwsEcrContainerImageDetailsTypeDef(BaseModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[Sequence[str]] = None
    ImagePublishedAt: Optional[str] = None

class AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef(BaseModel):
    ScanOnPush: Optional[bool] = None

class AwsEcrRepositoryLifecyclePolicyDetailsTypeDef(BaseModel):
    LifecyclePolicyText: Optional[str] = None
    RegistryId: Optional[str] = None

class AwsEcsClusterClusterSettingsDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef(BaseModel):
    CloudWatchEncryptionEnabled: Optional[bool] = None
    CloudWatchLogGroupName: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3EncryptionEnabled: Optional[bool] = None
    S3KeyPrefix: Optional[str] = None

class AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef(BaseModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None

class AwsMountPointTypeDef(BaseModel):
    SourceVolume: Optional[str] = None
    ContainerPath: Optional[str] = None

class AwsEcsServiceCapacityProviderStrategyDetailsTypeDef(BaseModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None

class AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef(BaseModel):
    Enable: Optional[bool] = None
    Rollback: Optional[bool] = None

class AwsEcsServiceDeploymentControllerDetailsTypeDef(BaseModel):
    Type: Optional[str] = None

class AwsEcsServiceLoadBalancersDetailsTypeDef(BaseModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    LoadBalancerName: Optional[str] = None
    TargetGroupArn: Optional[str] = None

class AwsEcsServicePlacementConstraintsDetailsTypeDef(BaseModel):
    Expression: Optional[str] = None
    Type: Optional[str] = None

class AwsEcsServicePlacementStrategiesDetailsTypeDef(BaseModel):
    Field: Optional[str] = None
    Type: Optional[str] = None

class AwsEcsServiceServiceRegistriesDetailsTypeDef(BaseModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    Port: Optional[int] = None
    RegistryArn: Optional[str] = None

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsExtraOutputTypeDef(BaseModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef(BaseModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef(BaseModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef(BaseModel):
    Condition: Optional[str] = None
    ContainerName: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef(BaseModel):
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef(BaseModel):
    Hostname: Optional[str] = None
    IpAddress: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsExtraOutputTypeDef(BaseModel):
    Options: Optional[Dict[str, str]] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsExtraOutputTypeDef(BaseModel):
    Command: Optional[List[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef(BaseModel):
    ContainerPath: Optional[str] = None
    ReadOnly: Optional[bool] = None
    SourceVolume: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef(BaseModel):
    ContainerPort: Optional[int] = None
    HostPort: Optional[int] = None
    Protocol: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef(BaseModel):
    CredentialsParameter: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef(BaseModel):
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    ValueFrom: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef(BaseModel):
    Namespace: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef(BaseModel):
    HardLimit: Optional[int] = None
    Name: Optional[str] = None
    SoftLimit: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef(BaseModel):
    ReadOnly: Optional[bool] = None
    SourceContainer: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef(BaseModel):
    Options: Optional[Dict[str, str]] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef(BaseModel):
    Command: Optional[List[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef(BaseModel):
    Options: Optional[Mapping[str, str]] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef(BaseModel):
    Command: Optional[Sequence[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsExtraOutputTypeDef(BaseModel):
    Add: Optional[List[str]] = None
    Drop: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef(BaseModel):
    Add: Optional[List[str]] = None
    Drop: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef(BaseModel):
    Add: Optional[Sequence[str]] = None
    Drop: Optional[Sequence[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsExtraOutputTypeDef(BaseModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsExtraOutputTypeDef(BaseModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[List[str]] = None
    Size: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef(BaseModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef(BaseModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[List[str]] = None
    Size: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef(BaseModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef(BaseModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[Sequence[str]] = None
    Size: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    ValueFrom: Optional[str] = None

class AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    DeviceType: Optional[str] = None

class AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef(BaseModel):
    Expression: Optional[str] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsExtraOutputTypeDef(BaseModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Dict[str, str]] = None
    Labels: Optional[Dict[str, str]] = None
    Scope: Optional[str] = None

class AwsEcsTaskDefinitionVolumesHostDetailsTypeDef(BaseModel):
    SourcePath: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef(BaseModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Dict[str, str]] = None
    Labels: Optional[Dict[str, str]] = None
    Scope: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef(BaseModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Mapping[str, str]] = None
    Labels: Optional[Mapping[str, str]] = None
    Scope: Optional[str] = None

class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef(BaseModel):
    AccessPointId: Optional[str] = None
    Iam: Optional[str] = None

class AwsEcsTaskVolumeHostDetailsTypeDef(BaseModel):
    SourcePath: Optional[str] = None

class AwsEfsAccessPointPosixUserDetailsExtraOutputTypeDef(BaseModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[List[str]] = None
    Uid: Optional[str] = None

class AwsEfsAccessPointPosixUserDetailsOutputTypeDef(BaseModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[List[str]] = None
    Uid: Optional[str] = None

class AwsEfsAccessPointPosixUserDetailsTypeDef(BaseModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[Sequence[str]] = None
    Uid: Optional[str] = None

class AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef(BaseModel):
    OwnerGid: Optional[str] = None
    OwnerUid: Optional[str] = None
    Permissions: Optional[str] = None

class AwsEksClusterResourcesVpcConfigDetailsExtraOutputTypeDef(BaseModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    EndpointPublicAccess: Optional[bool] = None

class AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef(BaseModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    EndpointPublicAccess: Optional[bool] = None

class AwsEksClusterResourcesVpcConfigDetailsTypeDef(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    EndpointPublicAccess: Optional[bool] = None

class AwsEksClusterLoggingClusterLoggingDetailsExtraOutputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Types: Optional[List[str]] = None

class AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Types: Optional[List[str]] = None

class AwsEksClusterLoggingClusterLoggingDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Types: Optional[Sequence[str]] = None

class AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef(BaseModel):
    EnvironmentName: Optional[str] = None
    LinkName: Optional[str] = None

class AwsElasticBeanstalkEnvironmentOptionSettingTypeDef(BaseModel):
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None
    ResourceName: Optional[str] = None
    Value: Optional[str] = None

class AwsElasticBeanstalkEnvironmentTierTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Version: Optional[str] = None

class AwsElasticsearchDomainDomainEndpointOptionsTypeDef(BaseModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[str] = None

class AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None

class AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsElasticsearchDomainServiceSoftwareOptionsTypeDef(BaseModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None

class AwsElasticsearchDomainVPCOptionsExtraOutputTypeDef(BaseModel):
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VPCId: Optional[str] = None

class AwsElasticsearchDomainVPCOptionsOutputTypeDef(BaseModel):
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VPCId: Optional[str] = None

class AwsElasticsearchDomainVPCOptionsTypeDef(BaseModel):
    AvailabilityZones: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VPCId: Optional[str] = None

class AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef(BaseModel):
    AvailabilityZoneCount: Optional[int] = None

class AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None

class AwsElbAppCookieStickinessPolicyTypeDef(BaseModel):
    CookieName: Optional[str] = None
    PolicyName: Optional[str] = None

class AwsElbLbCookieStickinessPolicyTypeDef(BaseModel):
    CookieExpirationPeriod: Optional[int] = None
    PolicyName: Optional[str] = None

class AwsElbLoadBalancerAccessLogTypeDef(BaseModel):
    EmitInterval: Optional[int] = None
    Enabled: Optional[bool] = None
    S3BucketName: Optional[str] = None
    S3BucketPrefix: Optional[str] = None

class AwsElbLoadBalancerAdditionalAttributeTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AwsElbLoadBalancerConnectionDrainingTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Timeout: Optional[int] = None

class AwsElbLoadBalancerConnectionSettingsTypeDef(BaseModel):
    IdleTimeout: Optional[int] = None

class AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsElbLoadBalancerBackendServerDescriptionExtraOutputTypeDef(BaseModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef(BaseModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerBackendServerDescriptionTypeDef(BaseModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[Sequence[str]] = None

class AwsElbLoadBalancerHealthCheckTypeDef(BaseModel):
    HealthyThreshold: Optional[int] = None
    Interval: Optional[int] = None
    Target: Optional[str] = None
    Timeout: Optional[int] = None
    UnhealthyThreshold: Optional[int] = None

class AwsElbLoadBalancerInstanceTypeDef(BaseModel):
    InstanceId: Optional[str] = None

class AwsElbLoadBalancerSourceSecurityGroupTypeDef(BaseModel):
    GroupName: Optional[str] = None
    OwnerAlias: Optional[str] = None

class AwsElbLoadBalancerListenerTypeDef(BaseModel):
    InstancePort: Optional[int] = None
    InstanceProtocol: Optional[str] = None
    LoadBalancerPort: Optional[int] = None
    Protocol: Optional[str] = None
    SslCertificateId: Optional[str] = None

class AwsElbv2LoadBalancerAttributeTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class LoadBalancerStateTypeDef(BaseModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None

class AwsEventSchemasRegistryDetailsTypeDef(BaseModel):
    Description: Optional[str] = None
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None

class AwsEventsEndpointEventBusesDetailsTypeDef(BaseModel):
    EventBusArn: Optional[str] = None

class AwsEventsEndpointReplicationConfigDetailsTypeDef(BaseModel):
    State: Optional[str] = None

class AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef(BaseModel):
    HealthCheck: Optional[str] = None

class AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef(BaseModel):
    Route: Optional[str] = None

class AwsEventsEventbusDetailsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Policy: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef(BaseModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef(BaseModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef(BaseModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef(BaseModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef(BaseModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef(BaseModel):
    Reason: Optional[str] = None
    Status: Optional[str] = None

class AwsGuardDutyDetectorFeaturesDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None

class AwsIamAccessKeySessionContextAttributesTypeDef(BaseModel):
    MfaAuthenticated: Optional[bool] = None
    CreationDate: Optional[str] = None

class AwsIamAccessKeySessionContextSessionIssuerTypeDef(BaseModel):
    Type: Optional[str] = None
    PrincipalId: Optional[str] = None
    Arn: Optional[str] = None
    AccountId: Optional[str] = None
    UserName: Optional[str] = None

class AwsIamAttachedManagedPolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None

class AwsIamGroupPolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None

class AwsIamInstanceProfileRoleTypeDef(BaseModel):
    Arn: Optional[str] = None
    AssumeRolePolicyDocument: Optional[str] = None
    CreateDate: Optional[str] = None
    Path: Optional[str] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None

class AwsIamPermissionsBoundaryTypeDef(BaseModel):
    PermissionsBoundaryArn: Optional[str] = None
    PermissionsBoundaryType: Optional[str] = None

class AwsIamPolicyVersionTypeDef(BaseModel):
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    CreateDate: Optional[str] = None

class AwsIamRolePolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None

class AwsIamUserPolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None

class AwsKinesisStreamStreamEncryptionDetailsTypeDef(BaseModel):
    EncryptionType: Optional[str] = None
    KeyId: Optional[str] = None

class AwsKmsKeyDetailsTypeDef(BaseModel):
    AWSAccountId: Optional[str] = None
    CreationDate: Optional[float] = None
    KeyId: Optional[str] = None
    KeyManager: Optional[str] = None
    KeyState: Optional[str] = None
    Origin: Optional[str] = None
    Description: Optional[str] = None
    KeyRotationStatus: Optional[bool] = None

class AwsLambdaFunctionCodeTypeDef(BaseModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ZipFile: Optional[str] = None

class AwsLambdaFunctionDeadLetterConfigTypeDef(BaseModel):
    TargetArn: Optional[str] = None

class AwsLambdaFunctionLayerTypeDef(BaseModel):
    Arn: Optional[str] = None
    CodeSize: Optional[int] = None

class AwsLambdaFunctionTracingConfigTypeDef(BaseModel):
    Mode: Optional[str] = None

class AwsLambdaFunctionVpcConfigExtraOutputTypeDef(BaseModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsLambdaFunctionVpcConfigOutputTypeDef(BaseModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsLambdaFunctionVpcConfigTypeDef(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None

class AwsLambdaFunctionEnvironmentErrorTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class AwsLambdaLayerVersionDetailsExtraOutputTypeDef(BaseModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[List[str]] = None
    CreatedDate: Optional[str] = None

class AwsLambdaLayerVersionDetailsOutputTypeDef(BaseModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[List[str]] = None
    CreatedDate: Optional[str] = None

class AwsLambdaLayerVersionDetailsTypeDef(BaseModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[Sequence[str]] = None
    CreatedDate: Optional[str] = None

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsExtraOutputTypeDef(BaseModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef(BaseModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef(BaseModel):
    CertificateAuthorityArnList: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef(BaseModel):
    DataVolumeKMSKeyId: Optional[str] = None

class AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef(BaseModel):
    InCluster: Optional[bool] = None
    ClientBroker: Optional[str] = None

class AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef(BaseModel):
    SubnetId: Optional[str] = None

class AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef(BaseModel):
    MasterUserArn: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None

class AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef(BaseModel):
    AvailabilityZoneCount: Optional[int] = None

class AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef(BaseModel):
    CustomEndpointCertificateArn: Optional[str] = None
    CustomEndpointEnabled: Optional[bool] = None
    EnforceHTTPS: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    TLSSecurityPolicy: Optional[str] = None

class AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None

class AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef(BaseModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None
    OptionalDeployment: Optional[bool] = None

class AwsOpenSearchServiceDomainVpcOptionsDetailsExtraOutputTypeDef(BaseModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None

class AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef(BaseModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None

class AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None

class AwsOpenSearchServiceDomainLogPublishingOptionTypeDef(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None

class AwsRdsDbClusterAssociatedRoleTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbClusterMemberTypeDef(BaseModel):
    IsClusterWriter: Optional[bool] = None
    PromotionTier: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    DbClusterParameterGroupStatus: Optional[str] = None

class AwsRdsDbClusterOptionGroupMembershipTypeDef(BaseModel):
    DbClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbDomainMembershipTypeDef(BaseModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    Fqdn: Optional[str] = None
    IamRoleName: Optional[str] = None

class AwsRdsDbInstanceVpcSecurityGroupTypeDef(BaseModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeExtraOutputTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[Sequence[str]] = None

class AwsRdsDbInstanceAssociatedRoleTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    FeatureName: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbInstanceEndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None

class AwsRdsDbOptionGroupMembershipTypeDef(BaseModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbParameterGroupTypeDef(BaseModel):
    DbParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None

class AwsRdsDbProcessorFeatureTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsRdsDbStatusInfoTypeDef(BaseModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class AwsRdsPendingCloudWatchLogsExportsExtraOutputTypeDef(BaseModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

class AwsRdsPendingCloudWatchLogsExportsOutputTypeDef(BaseModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

class AwsRdsPendingCloudWatchLogsExportsTypeDef(BaseModel):
    LogTypesToEnable: Optional[Sequence[str]] = None
    LogTypesToDisable: Optional[Sequence[str]] = None

class AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef(BaseModel):
    Ec2SecurityGroupId: Optional[str] = None
    Ec2SecurityGroupName: Optional[str] = None
    Ec2SecurityGroupOwnerId: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbSecurityGroupIpRangeTypeDef(BaseModel):
    CidrIp: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None

class AwsRdsEventSubscriptionDetailsExtraOutputTypeDef(BaseModel):
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

class AwsRdsEventSubscriptionDetailsOutputTypeDef(BaseModel):
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

class AwsRdsEventSubscriptionDetailsTypeDef(BaseModel):
    CustSubscriptionId: Optional[str] = None
    CustomerAwsId: Optional[str] = None
    Enabled: Optional[bool] = None
    EventCategoriesList: Optional[Sequence[str]] = None
    EventSubscriptionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SourceIdsList: Optional[Sequence[str]] = None
    SourceType: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None

class AwsRedshiftClusterClusterNodeTypeDef(BaseModel):
    NodeRole: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PublicIpAddress: Optional[str] = None

class AwsRedshiftClusterClusterParameterStatusTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None

class AwsRedshiftClusterClusterSecurityGroupTypeDef(BaseModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef(BaseModel):
    DestinationRegion: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None

class AwsRedshiftClusterDeferredMaintenanceWindowTypeDef(BaseModel):
    DeferMaintenanceEndTime: Optional[str] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[str] = None

class AwsRedshiftClusterElasticIpStatusTypeDef(BaseModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None

class AwsRedshiftClusterEndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None

class AwsRedshiftClusterHsmStatusTypeDef(BaseModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None

class AwsRedshiftClusterIamRoleTypeDef(BaseModel):
    ApplyStatus: Optional[str] = None
    IamRoleArn: Optional[str] = None

class AwsRedshiftClusterLoggingStatusTypeDef(BaseModel):
    BucketName: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    LastFailureTime: Optional[str] = None
    LastSuccessfulDeliveryTime: Optional[str] = None
    LoggingEnabled: Optional[bool] = None
    S3KeyPrefix: Optional[str] = None

class AwsRedshiftClusterPendingModifiedValuesTypeDef(BaseModel):
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

class AwsRedshiftClusterResizeInfoTypeDef(BaseModel):
    AllowCancelResize: Optional[bool] = None
    ResizeType: Optional[str] = None

class AwsRedshiftClusterRestoreStatusTypeDef(BaseModel):
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    Status: Optional[str] = None

class AwsRedshiftClusterVpcSecurityGroupTypeDef(BaseModel):
    Status: Optional[str] = None
    VpcSecurityGroupId: Optional[str] = None

class AwsRoute53HostedZoneConfigDetailsTypeDef(BaseModel):
    Comment: Optional[str] = None

class AwsRoute53HostedZoneVpcDetailsTypeDef(BaseModel):
    Id: Optional[str] = None
    Region: Optional[str] = None

class CloudWatchLogsLogGroupArnConfigDetailsTypeDef(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    HostedZoneId: Optional[str] = None
    Id: Optional[str] = None

class AwsS3AccessPointVpcConfigurationDetailsTypeDef(BaseModel):
    VpcId: Optional[str] = None

class AwsS3AccountPublicAccessBlockDetailsTypeDef(BaseModel):
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None

class AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef(BaseModel):
    Days: Optional[int] = None
    StorageClass: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef(BaseModel):
    Date: Optional[str] = None
    Days: Optional[int] = None
    StorageClass: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AwsS3BucketBucketVersioningConfigurationTypeDef(BaseModel):
    IsMfaDeleteEnabled: Optional[bool] = None
    Status: Optional[str] = None

class AwsS3BucketLoggingConfigurationTypeDef(BaseModel):
    DestinationBucketName: Optional[str] = None
    LogFilePrefix: Optional[str] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef(BaseModel):
    Name: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType] = None
    Value: Optional[str] = None

class AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef(BaseModel):
    Days: Optional[int] = None
    Mode: Optional[str] = None
    Years: Optional[int] = None

class AwsS3BucketServerSideEncryptionByDefaultTypeDef(BaseModel):
    SSEAlgorithm: Optional[str] = None
    KMSMasterKeyID: Optional[str] = None

class AwsS3BucketWebsiteConfigurationRedirectToTypeDef(BaseModel):
    Hostname: Optional[str] = None
    Protocol: Optional[str] = None

class AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef(BaseModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None

class AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef(BaseModel):
    Hostname: Optional[str] = None
    HttpRedirectCode: Optional[str] = None
    Protocol: Optional[str] = None
    ReplaceKeyPrefixWith: Optional[str] = None
    ReplaceKeyWith: Optional[str] = None

class AwsS3ObjectDetailsTypeDef(BaseModel):
    LastModified: Optional[str] = None
    ETag: Optional[str] = None
    VersionId: Optional[str] = None
    ContentType: Optional[str] = None
    ServerSideEncryption: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None

class AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef(BaseModel):
    MinimumInstanceMetadataServiceVersion: Optional[str] = None

class AwsSecretsManagerSecretRotationRulesTypeDef(BaseModel):
    AutomaticallyAfterDays: Optional[int] = None

class GeneratorDetailsExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[List[str]] = None

class MalwareTypeDef(BaseModel):
    Name: str
    Type: Optional[MalwareTypeType] = None
    Path: Optional[str] = None
    State: Optional[MalwareStateType] = None

class NoteTypeDef(BaseModel):
    Text: str
    UpdatedBy: str
    UpdatedAt: str

class PatchSummaryTypeDef(BaseModel):
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

class ProcessDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Path: Optional[str] = None
    Pid: Optional[int] = None
    ParentPid: Optional[int] = None
    LaunchedAt: Optional[str] = None
    TerminatedAt: Optional[str] = None

class SeverityTypeDef(BaseModel):
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None
    Normalized: Optional[int] = None
    Original: Optional[str] = None

class ThreatIntelIndicatorTypeDef(BaseModel):
    Type: Optional[ThreatIntelIndicatorTypeType] = None
    Value: Optional[str] = None
    Category: Optional[ThreatIntelIndicatorCategoryType] = None
    LastObservedAt: Optional[str] = None
    Source: Optional[str] = None
    SourceUrl: Optional[str] = None

class WorkflowTypeDef(BaseModel):
    Status: Optional[WorkflowStatusType] = None

class BooleanFilterTypeDef(BaseModel):
    Value: Optional[bool] = None

class IpFilterTypeDef(BaseModel):
    Cidr: Optional[str] = None

class KeywordFilterTypeDef(BaseModel):
    Value: Optional[str] = None

class AwsSecurityFindingIdentifierTypeDef(BaseModel):
    Id: str
    ProductArn: str

class GeneratorDetailsOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[List[str]] = None

class GeneratorDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[Sequence[str]] = None

class AwsSnsTopicSubscriptionTypeDef(BaseModel):
    Endpoint: Optional[str] = None
    Protocol: Optional[str] = None

class AwsSqsQueueDetailsTypeDef(BaseModel):
    KmsDataKeyReusePeriodSeconds: Optional[int] = None
    KmsMasterKeyId: Optional[str] = None
    QueueName: Optional[str] = None
    DeadLetterTargetArn: Optional[str] = None

class AwsSsmComplianceSummaryTypeDef(BaseModel):
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

class AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef(BaseModel):
    LogGroupArn: Optional[str] = None

class AwsWafRateBasedRuleMatchPredicateTypeDef(BaseModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRegionalRateBasedRuleMatchPredicateTypeDef(BaseModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRegionalRulePredicateListDetailsTypeDef(BaseModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRegionalRuleGroupRulesActionDetailsTypeDef(BaseModel):
    Type: Optional[str] = None

class AwsWafRegionalWebAclRulesListActionDetailsTypeDef(BaseModel):
    Type: Optional[str] = None

class AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef(BaseModel):
    Type: Optional[str] = None

class AwsWafRulePredicateListDetailsTypeDef(BaseModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRuleGroupRulesActionDetailsTypeDef(BaseModel):
    Type: Optional[str] = None

class WafActionTypeDef(BaseModel):
    Type: Optional[str] = None

class WafExcludedRuleTypeDef(BaseModel):
    RuleId: Optional[str] = None

class WafOverrideActionTypeDef(BaseModel):
    Type: Optional[str] = None

class AwsWafv2CustomHttpHeaderTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsWafv2VisibilityConfigDetailsTypeDef(BaseModel):
    CloudWatchMetricsEnabled: Optional[bool] = None
    MetricName: Optional[str] = None
    SampledRequestsEnabled: Optional[bool] = None

class AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef(BaseModel):
    ImmunityTime: Optional[int] = None

class AwsXrayEncryptionConfigDetailsTypeDef(BaseModel):
    KeyId: Optional[str] = None
    Status: Optional[str] = None
    Type: Optional[str] = None

class BatchDeleteAutomationRulesRequestRequestTypeDef(BaseModel):
    AutomationRulesArns: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnprocessedAutomationRuleTypeDef(BaseModel):
    RuleArn: Optional[str] = None
    ErrorCode: Optional[int] = None
    ErrorMessage: Optional[str] = None

class BatchDisableStandardsRequestRequestTypeDef(BaseModel):
    StandardsSubscriptionArns: Sequence[str]

class StandardsSubscriptionRequestTypeDef(BaseModel):
    StandardsArn: str
    StandardsInput: Optional[Mapping[str, str]] = None

class BatchGetAutomationRulesRequestRequestTypeDef(BaseModel):
    AutomationRulesArns: Sequence[str]

class ConfigurationPolicyAssociationSummaryTypeDef(BaseModel):
    ConfigurationPolicyId: Optional[str] = None
    TargetId: Optional[str] = None
    TargetType: Optional[TargetTypeType] = None
    AssociationType: Optional[AssociationTypeType] = None
    UpdatedAt: Optional[datetime] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None
    AssociationStatusMessage: Optional[str] = None

class BatchGetSecurityControlsRequestRequestTypeDef(BaseModel):
    SecurityControlIds: Sequence[str]

class UnprocessedSecurityControlTypeDef(BaseModel):
    SecurityControlId: str
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None

class StandardsControlAssociationIdTypeDef(BaseModel):
    SecurityControlId: str
    StandardsArn: str

class StandardsControlAssociationDetailTypeDef(BaseModel):
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

class ImportFindingsErrorTypeDef(BaseModel):
    Id: str
    ErrorCode: str
    ErrorMessage: str

class StandardsControlAssociationUpdateTypeDef(BaseModel):
    StandardsArn: str
    SecurityControlId: str
    AssociationStatus: AssociationStatusType
    UpdatedReason: Optional[str] = None

class BooleanConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[bool] = None

class CellTypeDef(BaseModel):
    Column: Optional[int] = None
    Row: Optional[int] = None
    ColumnName: Optional[str] = None
    CellReference: Optional[str] = None

class ClassificationStatusTypeDef(BaseModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None

class CodeVulnerabilitiesFilePathTypeDef(BaseModel):
    EndLine: Optional[int] = None
    FileName: Optional[str] = None
    FilePath: Optional[str] = None
    StartLine: Optional[int] = None

class SecurityControlParameterExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[List[str]] = None

class StatusReasonTypeDef(BaseModel):
    ReasonCode: str
    Description: Optional[str] = None

class SecurityControlParameterOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[List[str]] = None

class SecurityControlParameterTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[Sequence[str]] = None

class DoubleConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[float] = None
    Min: Optional[float] = None
    Max: Optional[float] = None

class EnumConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[List[str]] = None

class EnumListConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[List[str]] = None
    MaxItems: Optional[int] = None
    AllowedValues: Optional[List[str]] = None

class IntegerConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[int] = None
    Min: Optional[int] = None
    Max: Optional[int] = None

class IntegerListConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[List[int]] = None
    Min: Optional[int] = None
    Max: Optional[int] = None
    MaxItems: Optional[int] = None

class StringConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    Re2Expression: Optional[str] = None
    ExpressionDescription: Optional[str] = None

class StringListConfigurationOptionsTypeDef(BaseModel):
    DefaultValue: Optional[List[str]] = None
    Re2Expression: Optional[str] = None
    MaxItems: Optional[int] = None
    ExpressionDescription: Optional[str] = None

class TargetTypeDef(BaseModel):
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    RootId: Optional[str] = None

class ConfigurationPolicySummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    ServiceEnabled: Optional[bool] = None

class VolumeMountTypeDef(BaseModel):
    Name: Optional[str] = None
    MountPath: Optional[str] = None

class CreateActionTargetRequestRequestTypeDef(BaseModel):
    Name: str
    Description: str
    Id: str

class CreateFindingAggregatorRequestRequestTypeDef(BaseModel):
    RegionLinkingMode: str
    Regions: Optional[Sequence[str]] = None

class ResultTypeDef(BaseModel):
    AccountId: Optional[str] = None
    ProcessingResult: Optional[str] = None

class DateRangeTypeDef(BaseModel):
    Value: Optional[int] = None
    Unit: Optional[Literal["DAYS"]] = None

class DeclineInvitationsRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class DeleteActionTargetRequestRequestTypeDef(BaseModel):
    ActionTargetArn: str

class DeleteConfigurationPolicyRequestRequestTypeDef(BaseModel):
    Identifier: str

class DeleteFindingAggregatorRequestRequestTypeDef(BaseModel):
    FindingAggregatorArn: str

class DeleteInsightRequestRequestTypeDef(BaseModel):
    InsightArn: str

class DeleteInvitationsRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class DeleteMembersRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeActionTargetsRequestRequestTypeDef(BaseModel):
    ActionTargetArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeHubRequestRequestTypeDef(BaseModel):
    HubArn: Optional[str] = None

class OrganizationConfigurationTypeDef(BaseModel):
    ConfigurationType: Optional[OrganizationConfigurationConfigurationTypeType] = None
    Status: Optional[OrganizationConfigurationStatusType] = None
    StatusMessage: Optional[str] = None

class DescribeProductsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProductArn: Optional[str] = None

class ProductTypeDef(BaseModel):
    ProductArn: str
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Description: Optional[str] = None
    Categories: Optional[List[str]] = None
    IntegrationTypes: Optional[List[IntegrationTypeType]] = None
    MarketplaceUrl: Optional[str] = None
    ActivationUrl: Optional[str] = None
    ProductSubscriptionResourcePolicy: Optional[str] = None

class DescribeStandardsControlsRequestRequestTypeDef(BaseModel):
    StandardsSubscriptionArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StandardsControlTypeDef(BaseModel):
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

class DescribeStandardsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DisableImportFindingsForProductRequestRequestTypeDef(BaseModel):
    ProductSubscriptionArn: str

class DisableOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    AdminAccountId: str

class DisassociateMembersRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class EnableImportFindingsForProductRequestRequestTypeDef(BaseModel):
    ProductArn: str

class EnableOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    AdminAccountId: str

class EnableSecurityHubRequestRequestTypeDef(BaseModel):
    Tags: Optional[Mapping[str, str]] = None
    EnableDefaultStandards: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None

class FilePathsTypeDef(BaseModel):
    FilePath: Optional[str] = None
    FileName: Optional[str] = None
    ResourceId: Optional[str] = None
    Hash: Optional[str] = None

class FindingAggregatorTypeDef(BaseModel):
    FindingAggregatorArn: Optional[str] = None

class FindingHistoryUpdateSourceTypeDef(BaseModel):
    Type: Optional[FindingHistoryUpdateSourceTypeType] = None
    Identity: Optional[str] = None

class FindingHistoryUpdateTypeDef(BaseModel):
    UpdatedField: Optional[str] = None
    OldValue: Optional[str] = None
    NewValue: Optional[str] = None

class FindingProviderSeverityTypeDef(BaseModel):
    Label: Optional[SeverityLabelType] = None
    Original: Optional[str] = None

class FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef(BaseModel):
    ResourceArn: Optional[str] = None

class FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef(BaseModel):
    Priority: Optional[int] = None
    ResourceArn: Optional[str] = None

class InvitationTypeDef(BaseModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    MemberStatus: Optional[str] = None

class GetConfigurationPolicyRequestRequestTypeDef(BaseModel):
    Identifier: str

class GetEnabledStandardsRequestRequestTypeDef(BaseModel):
    StandardsSubscriptionArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetFindingAggregatorRequestRequestTypeDef(BaseModel):
    FindingAggregatorArn: str

class SortCriterionTypeDef(BaseModel):
    Field: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None

class GetInsightResultsRequestRequestTypeDef(BaseModel):
    InsightArn: str

class GetInsightsRequestRequestTypeDef(BaseModel):
    InsightArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetMembersRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class MemberTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Email: Optional[str] = None
    MasterId: Optional[str] = None
    AdministratorId: Optional[str] = None
    MemberStatus: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class GetSecurityControlDefinitionRequestRequestTypeDef(BaseModel):
    SecurityControlId: str

class InsightResultValueTypeDef(BaseModel):
    GroupByAttributeValue: str
    Count: int

class InviteMembersRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class ListAutomationRulesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListConfigurationPoliciesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEnabledProductsForImportRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFindingAggregatorsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInvitationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMembersRequestRequestTypeDef(BaseModel):
    OnlyAssociated: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOrganizationAdminAccountsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSecurityControlDefinitionsRequestRequestTypeDef(BaseModel):
    StandardsArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListStandardsControlAssociationsRequestRequestTypeDef(BaseModel):
    SecurityControlId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StandardsControlAssociationSummaryTypeDef(BaseModel):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: Optional[List[str]] = None
    UpdatedAt: Optional[datetime] = None
    UpdatedReason: Optional[str] = None
    StandardsControlTitle: Optional[str] = None
    StandardsControlDescription: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PortRangeTypeDef(BaseModel):
    Begin: Optional[int] = None
    End: Optional[int] = None

class RangeTypeDef(BaseModel):
    Start: Optional[int] = None
    End: Optional[int] = None
    StartColumn: Optional[int] = None

class RecordTypeDef(BaseModel):
    JsonPath: Optional[str] = None
    RecordIndex: Optional[int] = None

class ParameterValueOutputTypeDef(BaseModel):
    Integer: Optional[int] = None
    IntegerList: Optional[List[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[List[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[List[str]] = None

class ParameterValueTypeDef(BaseModel):
    Integer: Optional[int] = None
    IntegerList: Optional[Sequence[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[Sequence[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[Sequence[str]] = None

class RecommendationTypeDef(BaseModel):
    Text: Optional[str] = None
    Url: Optional[str] = None

class RuleGroupSourceListDetailsExtraOutputTypeDef(BaseModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[List[str]] = None
    Targets: Optional[List[str]] = None

class RuleGroupSourceListDetailsOutputTypeDef(BaseModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[List[str]] = None
    Targets: Optional[List[str]] = None

class RuleGroupSourceListDetailsTypeDef(BaseModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[str]] = None

class RuleGroupSourceStatefulRulesHeaderDetailsTypeDef(BaseModel):
    Destination: Optional[str] = None
    DestinationPort: Optional[str] = None
    Direction: Optional[str] = None
    Protocol: Optional[str] = None
    Source: Optional[str] = None
    SourcePort: Optional[str] = None

class RuleGroupSourceStatefulRulesOptionsDetailsExtraOutputTypeDef(BaseModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None

class RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef(BaseModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None

class RuleGroupSourceStatefulRulesOptionsDetailsTypeDef(BaseModel):
    Keyword: Optional[str] = None
    Settings: Optional[Sequence[str]] = None

class RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef(BaseModel):
    AddressDefinition: Optional[str] = None

class RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef(BaseModel):
    AddressDefinition: Optional[str] = None

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsExtraOutputTypeDef(BaseModel):
    Flags: Optional[List[str]] = None
    Masks: Optional[List[str]] = None

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef(BaseModel):
    Flags: Optional[List[str]] = None
    Masks: Optional[List[str]] = None

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef(BaseModel):
    Flags: Optional[Sequence[str]] = None
    Masks: Optional[Sequence[str]] = None

class RuleGroupVariablesIpSetsDetailsExtraOutputTypeDef(BaseModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesPortSetsDetailsExtraOutputTypeDef(BaseModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesIpSetsDetailsOutputTypeDef(BaseModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesIpSetsDetailsTypeDef(BaseModel):
    Definition: Optional[Sequence[str]] = None

class RuleGroupVariablesPortSetsDetailsOutputTypeDef(BaseModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesPortSetsDetailsTypeDef(BaseModel):
    Definition: Optional[Sequence[str]] = None

class SoftwarePackageTypeDef(BaseModel):
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

class StandardsManagedByTypeDef(BaseModel):
    Company: Optional[str] = None
    Product: Optional[str] = None

class StandardsStatusReasonTypeDef(BaseModel):
    StatusReasonCode: StatusReasonCodeType

class StatelessCustomPublishMetricActionDimensionTypeDef(BaseModel):
    Value: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateActionTargetRequestRequestTypeDef(BaseModel):
    ActionTargetArn: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateFindingAggregatorRequestRequestTypeDef(BaseModel):
    FindingAggregatorArn: str
    RegionLinkingMode: str
    Regions: Optional[Sequence[str]] = None

class UpdateSecurityHubConfigurationRequestRequestTypeDef(BaseModel):
    AutoEnableControls: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None

class UpdateStandardsControlRequestRequestTypeDef(BaseModel):
    StandardsControlArn: str
    ControlStatus: Optional[ControlStatusType] = None
    DisabledReason: Optional[str] = None

class VulnerabilityVendorTypeDef(BaseModel):
    Name: str
    Url: Optional[str] = None
    VendorSeverity: Optional[str] = None
    VendorCreatedAt: Optional[str] = None
    VendorUpdatedAt: Optional[str] = None

class CreateMembersRequestRequestTypeDef(BaseModel):
    AccountDetails: Sequence[AccountDetailsTypeDef]

class ActionRemoteIpDetailsTypeDef(BaseModel):
    IpAddressV4: Optional[str] = None
    Organization: Optional[IpOrganizationDetailsTypeDef] = None
    Country: Optional[CountryTypeDef] = None
    City: Optional[CityTypeDef] = None
    GeoLocation: Optional[GeoLocationTypeDef] = None

class CvssExtraOutputTypeDef(BaseModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[List[AdjustmentTypeDef]] = None

class CvssOutputTypeDef(BaseModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[List[AdjustmentTypeDef]] = None

class CvssTypeDef(BaseModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[Sequence[AdjustmentTypeDef]] = None

class ListConfigurationPolicyAssociationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[AssociationFiltersTypeDef] = None

class AssociationSetDetailsTypeDef(BaseModel):
    AssociationState: Optional[AssociationStateDetailsTypeDef] = None
    GatewayId: Optional[str] = None
    Main: Optional[bool] = None
    RouteTableAssociationId: Optional[str] = None
    RouteTableId: Optional[str] = None
    SubnetId: Optional[str] = None

class AutomationRulesFindingFieldsUpdateOutputTypeDef(BaseModel):
    Note: Optional[NoteUpdateTypeDef] = None
    Severity: Optional[SeverityUpdateTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[List[str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Workflow: Optional[WorkflowUpdateTypeDef] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None

class AutomationRulesFindingFieldsUpdateTypeDef(BaseModel):
    Note: Optional[NoteUpdateTypeDef] = None
    Severity: Optional[SeverityUpdateTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[Sequence[str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Workflow: Optional[WorkflowUpdateTypeDef] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None

class AwsAmazonMqBrokerLogsDetailsTypeDef(BaseModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None
    AuditLogGroup: Optional[str] = None
    GeneralLogGroup: Optional[str] = None
    Pending: Optional[AwsAmazonMqBrokerLogsPendingDetailsTypeDef] = None

class AwsApiGatewayRestApiDetailsExtraOutputTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[List[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationExtraOutputTypeDef] = None

class AwsApiGatewayRestApiDetailsOutputTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[List[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationOutputTypeDef] = None

class AwsApiGatewayRestApiDetailsTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[Sequence[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationTypeDef] = None

class AwsApiGatewayStageDetailsExtraOutputTypeDef(BaseModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[List[AwsApiGatewayMethodSettingsTypeDef]] = None
    Variables: Optional[Dict[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsExtraOutputTypeDef] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None

class AwsApiGatewayStageDetailsOutputTypeDef(BaseModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[List[AwsApiGatewayMethodSettingsTypeDef]] = None
    Variables: Optional[Dict[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsOutputTypeDef] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None

class AwsApiGatewayStageDetailsTypeDef(BaseModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[Sequence[AwsApiGatewayMethodSettingsTypeDef]] = None
    Variables: Optional[Mapping[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsTypeDef] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None

class AwsApiGatewayV2ApiDetailsExtraOutputTypeDef(BaseModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationExtraOutputTypeDef] = None

class AwsApiGatewayV2ApiDetailsOutputTypeDef(BaseModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationOutputTypeDef] = None

class AwsApiGatewayV2ApiDetailsTypeDef(BaseModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationTypeDef] = None

class AwsApiGatewayV2StageDetailsExtraOutputTypeDef(BaseModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Dict[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None

class AwsApiGatewayV2StageDetailsOutputTypeDef(BaseModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Dict[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None

class AwsApiGatewayV2StageDetailsTypeDef(BaseModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Mapping[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None

class AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef(BaseModel):
    AuthenticationType: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None

class AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef(BaseModel):
    EncryptionConfiguration: Optional[       AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsExtraOutputTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    Overrides: Optional[       List[         AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef       ]     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    Overrides: Optional[       List[         AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef       ]     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    Overrides: Optional[       Sequence[         AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef       ]     ] = None

class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef] = None
    NoDevice: Optional[bool] = None
    VirtualName: Optional[str] = None

class AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef(BaseModel):
    DestinationBackupVaultArn: Optional[str] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsBackupBackupVaultDetailsExtraOutputTypeDef(BaseModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsExtraOutputTypeDef] = None
    AccessPolicy: Optional[str] = None

class AwsBackupBackupVaultDetailsOutputTypeDef(BaseModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsOutputTypeDef] = None
    AccessPolicy: Optional[str] = None

class AwsBackupBackupVaultDetailsTypeDef(BaseModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsTypeDef] = None
    AccessPolicy: Optional[str] = None

class AwsBackupRecoveryPointDetailsTypeDef(BaseModel):
    BackupSizeInBytes: Optional[int] = None
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    CalculatedLifecycle: Optional[AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef] = None
    CompletionDate: Optional[str] = None
    CreatedBy: Optional[AwsBackupRecoveryPointCreatedByDetailsTypeDef] = None
    CreationDate: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IsEncrypted: Optional[bool] = None
    LastRestoreTime: Optional[str] = None
    Lifecycle: Optional[AwsBackupRecoveryPointLifecycleDetailsTypeDef] = None
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    SourceBackupVaultArn: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    StorageClass: Optional[str] = None

class AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef(BaseModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecordTypeDef] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[List[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None

class AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef(BaseModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecordTypeDef] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[List[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None

class AwsCertificateManagerCertificateDomainValidationOptionTypeDef(BaseModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecordTypeDef] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[Sequence[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None

class AwsCloudFormationStackDetailsExtraOutputTypeDef(BaseModel):
    Capabilities: Optional[List[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetailsTypeDef] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    Outputs: Optional[List[AwsCloudFormationStackOutputsDetailsTypeDef]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None

class AwsCloudFormationStackDetailsOutputTypeDef(BaseModel):
    Capabilities: Optional[List[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetailsTypeDef] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    Outputs: Optional[List[AwsCloudFormationStackOutputsDetailsTypeDef]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None

class AwsCloudFormationStackDetailsTypeDef(BaseModel):
    Capabilities: Optional[Sequence[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetailsTypeDef] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[Sequence[str]] = None
    Outputs: Optional[Sequence[AwsCloudFormationStackOutputsDetailsTypeDef]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None

class AwsCloudFrontDistributionCacheBehaviorsExtraOutputTypeDef(BaseModel):
    Items: Optional[List[AwsCloudFrontDistributionCacheBehaviorTypeDef]] = None

class AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef(BaseModel):
    Items: Optional[List[AwsCloudFrontDistributionCacheBehaviorTypeDef]] = None

class AwsCloudFrontDistributionCacheBehaviorsTypeDef(BaseModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionCacheBehaviorTypeDef]] = None

class AwsCloudFrontDistributionOriginCustomOriginConfigExtraOutputTypeDef(BaseModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[       AwsCloudFrontDistributionOriginSslProtocolsExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef(BaseModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef] = None

class AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef(BaseModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsTypeDef] = None

class AwsCloudFrontDistributionOriginGroupFailoverExtraOutputTypeDef(BaseModel):
    StatusCodes: Optional[       AwsCloudFrontDistributionOriginGroupFailoverStatusCodesExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef(BaseModel):
    StatusCodes: Optional[       AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginGroupFailoverTypeDef(BaseModel):
    StatusCodes: Optional[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef] = None

class AwsCloudWatchAlarmDetailsExtraOutputTypeDef(BaseModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[List[AwsCloudWatchAlarmDimensionsDetailsTypeDef]] = None
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

class AwsCloudWatchAlarmDetailsOutputTypeDef(BaseModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[List[AwsCloudWatchAlarmDimensionsDetailsTypeDef]] = None
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

class AwsCloudWatchAlarmDetailsTypeDef(BaseModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[Sequence[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[Sequence[AwsCloudWatchAlarmDimensionsDetailsTypeDef]] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    EvaluationPeriods: Optional[int] = None
    ExtendedStatistic: Optional[str] = None
    InsufficientDataActions: Optional[Sequence[str]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    OkActions: Optional[Sequence[str]] = None
    Period: Optional[int] = None
    Statistic: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdMetricId: Optional[str] = None
    TreatMissingData: Optional[str] = None
    Unit: Optional[str] = None

class AwsCodeBuildProjectEnvironmentExtraOutputTypeDef(BaseModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[       List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]     ] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectEnvironmentOutputTypeDef(BaseModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[       List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]     ] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectEnvironmentTypeDef(BaseModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[       Sequence[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]     ] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectLogsConfigDetailsTypeDef(BaseModel):
    CloudWatchLogs: Optional[AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef] = None
    S3Logs: Optional[AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef] = None

class AwsDmsReplicationInstanceDetailsExtraOutputTypeDef(BaseModel):
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
    ReplicationSubnetGroup: Optional[       AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef     ] = None
    VpcSecurityGroups: Optional[       List[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]     ] = None

class AwsDmsReplicationInstanceDetailsOutputTypeDef(BaseModel):
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
    ReplicationSubnetGroup: Optional[       AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef     ] = None
    VpcSecurityGroups: Optional[       List[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]     ] = None

class AwsDmsReplicationInstanceDetailsTypeDef(BaseModel):
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
    ReplicationSubnetGroup: Optional[       AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef     ] = None
    VpcSecurityGroups: Optional[       Sequence[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]     ] = None

class AwsDynamoDbTableGlobalSecondaryIndexExtraOutputTypeDef(BaseModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionExtraOutputTypeDef] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None

class AwsDynamoDbTableLocalSecondaryIndexExtraOutputTypeDef(BaseModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionExtraOutputTypeDef] = None

class AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef(BaseModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutputTypeDef] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None

class AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef(BaseModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutputTypeDef] = None

class AwsDynamoDbTableGlobalSecondaryIndexTypeDef(BaseModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionTypeDef] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None

class AwsDynamoDbTableLocalSecondaryIndexTypeDef(BaseModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionTypeDef] = None

class AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef(BaseModel):
    IndexName: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef(BaseModel):
    Type: Optional[str] = None
    ActiveDirectory: Optional[       AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef     ] = None
    MutualAuthentication: Optional[       AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef     ] = None
    FederatedAuthentication: Optional[       AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef     ] = None

class AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None
    Status: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef] = None

class AwsEc2InstanceDetailsExtraOutputTypeDef(BaseModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[List[str]] = None
    IpV6Addresses: Optional[List[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[List[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptionsTypeDef] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetailsTypeDef] = None

class AwsEc2InstanceDetailsOutputTypeDef(BaseModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[List[str]] = None
    IpV6Addresses: Optional[List[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[List[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptionsTypeDef] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetailsTypeDef] = None

class AwsEc2InstanceDetailsTypeDef(BaseModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[Sequence[str]] = None
    IpV6Addresses: Optional[Sequence[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[Sequence[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptionsTypeDef] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetailsTypeDef] = None

class AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None

class AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef(BaseModel):
    CapacityReservationPreference: Optional[str] = None
    CapacityReservationTarget: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef(BaseModel):
    MarketType: Optional[str] = None
    SpotOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsExtraOutputTypeDef(BaseModel):
    AcceleratorCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef     ] = None
    AcceleratorManufacturers: Optional[List[str]] = None
    AcceleratorNames: Optional[List[str]] = None
    AcceleratorTotalMemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef     ] = None
    AcceleratorTypes: Optional[List[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef     ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[List[str]] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[List[str]] = None
    MemoryGiBPerVCpu: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef     ] = None
    MemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef     ] = None
    NetworkInterfaceCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef     ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef     ] = None
    VCpuCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef(BaseModel):
    AcceleratorCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef     ] = None
    AcceleratorManufacturers: Optional[List[str]] = None
    AcceleratorNames: Optional[List[str]] = None
    AcceleratorTotalMemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef     ] = None
    AcceleratorTypes: Optional[List[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef     ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[List[str]] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[List[str]] = None
    MemoryGiBPerVCpu: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef     ] = None
    MemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef     ] = None
    NetworkInterfaceCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef     ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef     ] = None
    VCpuCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef(BaseModel):
    AcceleratorCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef     ] = None
    AcceleratorManufacturers: Optional[Sequence[str]] = None
    AcceleratorNames: Optional[Sequence[str]] = None
    AcceleratorTotalMemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef     ] = None
    AcceleratorTypes: Optional[Sequence[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef     ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[Sequence[str]] = None
    ExcludedInstanceTypes: Optional[Sequence[str]] = None
    InstanceGenerations: Optional[Sequence[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[Sequence[str]] = None
    MemoryGiBPerVCpu: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef     ] = None
    MemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef     ] = None
    NetworkInterfaceCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef     ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef     ] = None
    VCpuCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsExtraOutputTypeDef(BaseModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]     ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]     ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]     ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]     ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef(BaseModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]     ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]     ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]     ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]     ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef(BaseModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[Sequence[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]     ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]     ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]     ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]     ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None

class AwsEc2NetworkAclEntryTypeDef(BaseModel):
    CidrBlock: Optional[str] = None
    Egress: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeFromToTypeDef] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    RuleNumber: Optional[int] = None

class AwsEc2NetworkInterfaceDetailsExtraOutputTypeDef(BaseModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachmentTypeDef] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[List[AwsEc2NetworkInterfaceSecurityGroupTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[List[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]] = None
    PrivateIpAddresses: Optional[       List[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]     ] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class AwsEc2NetworkInterfaceDetailsOutputTypeDef(BaseModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachmentTypeDef] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[List[AwsEc2NetworkInterfaceSecurityGroupTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[List[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]] = None
    PrivateIpAddresses: Optional[       List[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]     ] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class AwsEc2NetworkInterfaceDetailsTypeDef(BaseModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachmentTypeDef] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[Sequence[AwsEc2NetworkInterfaceSecurityGroupTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[Sequence[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]] = None
    PrivateIpAddresses: Optional[       Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]     ] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef(BaseModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[AwsEc2SecurityGroupUserIdGroupPairTypeDef]] = None
    IpRanges: Optional[List[AwsEc2SecurityGroupIpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[AwsEc2SecurityGroupIpv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[AwsEc2SecurityGroupPrefixListIdTypeDef]] = None

class AwsEc2SecurityGroupIpPermissionOutputTypeDef(BaseModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[AwsEc2SecurityGroupUserIdGroupPairTypeDef]] = None
    IpRanges: Optional[List[AwsEc2SecurityGroupIpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[AwsEc2SecurityGroupIpv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[AwsEc2SecurityGroupPrefixListIdTypeDef]] = None

class AwsEc2SecurityGroupIpPermissionTypeDef(BaseModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[Sequence[AwsEc2SecurityGroupUserIdGroupPairTypeDef]] = None
    IpRanges: Optional[Sequence[AwsEc2SecurityGroupIpRangeTypeDef]] = None
    Ipv6Ranges: Optional[Sequence[AwsEc2SecurityGroupIpv6RangeTypeDef]] = None
    PrefixListIds: Optional[Sequence[AwsEc2SecurityGroupPrefixListIdTypeDef]] = None

class AwsEc2SubnetDetailsExtraOutputTypeDef(BaseModel):
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
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None

class AwsEc2SubnetDetailsOutputTypeDef(BaseModel):
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
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None

class AwsEc2SubnetDetailsTypeDef(BaseModel):
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
    Ipv6CidrBlockAssociationSet: Optional[Sequence[Ipv6CidrBlockAssociationTypeDef]] = None

class AwsEc2VolumeDetailsExtraOutputTypeDef(BaseModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[List[AwsEc2VolumeAttachmentTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None

class AwsEc2VolumeDetailsOutputTypeDef(BaseModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[List[AwsEc2VolumeAttachmentTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None

class AwsEc2VolumeDetailsTypeDef(BaseModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[Sequence[AwsEc2VolumeAttachmentTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None

class AwsEc2VpcDetailsExtraOutputTypeDef(BaseModel):
    CidrBlockAssociationSet: Optional[List[CidrBlockAssociationTypeDef]] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpcDetailsOutputTypeDef(BaseModel):
    CidrBlockAssociationSet: Optional[List[CidrBlockAssociationTypeDef]] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpcDetailsTypeDef(BaseModel):
    CidrBlockAssociationSet: Optional[Sequence[CidrBlockAssociationTypeDef]] = None
    Ipv6CidrBlockAssociationSet: Optional[Sequence[Ipv6CidrBlockAssociationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpcEndpointServiceDetailsExtraOutputTypeDef(BaseModel):
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
    ServiceType: Optional[List[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]] = None

class AwsEc2VpcEndpointServiceDetailsOutputTypeDef(BaseModel):
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
    ServiceType: Optional[List[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]] = None

class AwsEc2VpcEndpointServiceDetailsTypeDef(BaseModel):
    AcceptanceRequired: Optional[bool] = None
    AvailabilityZones: Optional[Sequence[str]] = None
    BaseEndpointDnsNames: Optional[Sequence[str]] = None
    ManagesVpcEndpoints: Optional[bool] = None
    GatewayLoadBalancerArns: Optional[Sequence[str]] = None
    NetworkLoadBalancerArns: Optional[Sequence[str]] = None
    PrivateDnsName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceState: Optional[str] = None
    ServiceType: Optional[Sequence[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]] = None

class AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef(BaseModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[List[VpcInfoCidrBlockSetDetailsTypeDef]] = None
    Ipv6CidrBlockSet: Optional[List[VpcInfoIpv6CidrBlockSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetailsTypeDef] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None

class AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef(BaseModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[List[VpcInfoCidrBlockSetDetailsTypeDef]] = None
    Ipv6CidrBlockSet: Optional[List[VpcInfoIpv6CidrBlockSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetailsTypeDef] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None

class AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef(BaseModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[Sequence[VpcInfoCidrBlockSetDetailsTypeDef]] = None
    Ipv6CidrBlockSet: Optional[Sequence[VpcInfoIpv6CidrBlockSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetailsTypeDef] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None

class AwsEc2VpnConnectionOptionsDetailsExtraOutputTypeDef(BaseModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[       List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsExtraOutputTypeDef]     ] = None

class AwsEc2VpnConnectionOptionsDetailsOutputTypeDef(BaseModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[       List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef]     ] = None

class AwsEc2VpnConnectionOptionsDetailsTypeDef(BaseModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[       Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef]     ] = None

class AwsEcrRepositoryDetailsTypeDef(BaseModel):
    Arn: Optional[str] = None
    ImageScanningConfiguration: Optional[       AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef     ] = None
    ImageTagMutability: Optional[str] = None
    LifecyclePolicy: Optional[AwsEcrRepositoryLifecyclePolicyDetailsTypeDef] = None
    RepositoryName: Optional[str] = None
    RepositoryPolicyText: Optional[str] = None

class AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None
    LogConfiguration: Optional[       AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef     ] = None
    Logging: Optional[str] = None

class AwsEcsContainerDetailsExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[List[AwsMountPointTypeDef]] = None
    Privileged: Optional[bool] = None

class AwsEcsContainerDetailsOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[List[AwsMountPointTypeDef]] = None
    Privileged: Optional[bool] = None

class AwsEcsContainerDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[Sequence[AwsMountPointTypeDef]] = None
    Privileged: Optional[bool] = None

class AwsEcsServiceDeploymentConfigurationDetailsTypeDef(BaseModel):
    DeploymentCircuitBreaker: Optional[       AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef     ] = None
    MaximumPercent: Optional[int] = None
    MinimumHealthyPercent: Optional[int] = None

class AwsEcsServiceNetworkConfigurationDetailsExtraOutputTypeDef(BaseModel):
    AwsVpcConfiguration: Optional[       AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsExtraOutputTypeDef     ] = None

class AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef(BaseModel):
    AwsVpcConfiguration: Optional[       AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef     ] = None

class AwsEcsServiceNetworkConfigurationDetailsTypeDef(BaseModel):
    AwsVpcConfiguration: Optional[       AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsExtraOutputTypeDef(BaseModel):
    Capabilities: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsExtraOutputTypeDef     ] = None
    Devices: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsExtraOutputTypeDef       ]     ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsExtraOutputTypeDef       ]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef(BaseModel):
    Capabilities: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef     ] = None
    Devices: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef]     ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef(BaseModel):
    Capabilities: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef     ] = None
    Devices: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef]     ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsExtraOutputTypeDef(BaseModel):
    LogDriver: Optional[str] = None
    Options: Optional[Dict[str, str]] = None
    SecretOptions: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef       ]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef(BaseModel):
    LogDriver: Optional[str] = None
    Options: Optional[Dict[str, str]] = None
    SecretOptions: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef       ]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef(BaseModel):
    LogDriver: Optional[str] = None
    Options: Optional[Mapping[str, str]] = None
    SecretOptions: Optional[       Sequence[         AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef       ]     ] = None

class AwsEcsTaskDefinitionProxyConfigurationDetailsExtraOutputTypeDef(BaseModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[       List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]     ] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef(BaseModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[       List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]     ] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef(BaseModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[       Sequence[         AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef       ]     ] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef(BaseModel):
    AuthorizationConfig: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef     ] = None
    FilesystemId: Optional[str] = None
    RootDirectory: Optional[str] = None
    TransitEncryption: Optional[str] = None
    TransitEncryptionPort: Optional[int] = None

class AwsEcsTaskVolumeDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Host: Optional[AwsEcsTaskVolumeHostDetailsTypeDef] = None

class AwsEfsAccessPointRootDirectoryDetailsTypeDef(BaseModel):
    CreationInfo: Optional[AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef] = None
    Path: Optional[str] = None

class AwsEksClusterLoggingDetailsExtraOutputTypeDef(BaseModel):
    ClusterLogging: Optional[       List[AwsEksClusterLoggingClusterLoggingDetailsExtraOutputTypeDef]     ] = None

class AwsEksClusterLoggingDetailsOutputTypeDef(BaseModel):
    ClusterLogging: Optional[List[AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef]] = None

class AwsEksClusterLoggingDetailsTypeDef(BaseModel):
    ClusterLogging: Optional[Sequence[AwsEksClusterLoggingClusterLoggingDetailsTypeDef]] = None

class AwsElasticBeanstalkEnvironmentDetailsExtraOutputTypeDef(BaseModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[List[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTierTypeDef] = None
    VersionLabel: Optional[str] = None

class AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef(BaseModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[List[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTierTypeDef] = None
    VersionLabel: Optional[str] = None

class AwsElasticBeanstalkEnvironmentDetailsTypeDef(BaseModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[       Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]     ] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[Sequence[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTierTypeDef] = None
    VersionLabel: Optional[str] = None

class AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef(BaseModel):
    DedicatedMasterCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[str] = None
    ZoneAwarenessConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef     ] = None
    ZoneAwarenessEnabled: Optional[bool] = None

class AwsElasticsearchDomainLogPublishingOptionsTypeDef(BaseModel):
    IndexSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef] = None
    SearchSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef] = None
    AuditLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef] = None

class AwsElbLoadBalancerPoliciesExtraOutputTypeDef(BaseModel):
    AppCookieStickinessPolicies: Optional[List[AwsElbAppCookieStickinessPolicyTypeDef]] = None
    LbCookieStickinessPolicies: Optional[List[AwsElbLbCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[List[str]] = None

class AwsElbLoadBalancerPoliciesOutputTypeDef(BaseModel):
    AppCookieStickinessPolicies: Optional[List[AwsElbAppCookieStickinessPolicyTypeDef]] = None
    LbCookieStickinessPolicies: Optional[List[AwsElbLbCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[List[str]] = None

class AwsElbLoadBalancerPoliciesTypeDef(BaseModel):
    AppCookieStickinessPolicies: Optional[       Sequence[AwsElbAppCookieStickinessPolicyTypeDef]     ] = None
    LbCookieStickinessPolicies: Optional[Sequence[AwsElbLbCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[Sequence[str]] = None

class AwsElbLoadBalancerAttributesExtraOutputTypeDef(BaseModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLogTypeDef] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettingsTypeDef] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef] = None
    AdditionalAttributes: Optional[List[AwsElbLoadBalancerAdditionalAttributeTypeDef]] = None

class AwsElbLoadBalancerAttributesOutputTypeDef(BaseModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLogTypeDef] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettingsTypeDef] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef] = None
    AdditionalAttributes: Optional[List[AwsElbLoadBalancerAdditionalAttributeTypeDef]] = None

class AwsElbLoadBalancerAttributesTypeDef(BaseModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLogTypeDef] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettingsTypeDef] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef] = None
    AdditionalAttributes: Optional[Sequence[AwsElbLoadBalancerAdditionalAttributeTypeDef]] = None

class AwsElbLoadBalancerListenerDescriptionExtraOutputTypeDef(BaseModel):
    Listener: Optional[AwsElbLoadBalancerListenerTypeDef] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerListenerDescriptionOutputTypeDef(BaseModel):
    Listener: Optional[AwsElbLoadBalancerListenerTypeDef] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerListenerDescriptionTypeDef(BaseModel):
    Listener: Optional[AwsElbLoadBalancerListenerTypeDef] = None
    PolicyNames: Optional[Sequence[str]] = None

class AwsElbv2LoadBalancerDetailsExtraOutputTypeDef(BaseModel):
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    State: Optional[LoadBalancerStateTypeDef] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[List[AwsElbv2LoadBalancerAttributeTypeDef]] = None

class AwsElbv2LoadBalancerDetailsOutputTypeDef(BaseModel):
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    State: Optional[LoadBalancerStateTypeDef] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[List[AwsElbv2LoadBalancerAttributeTypeDef]] = None

class AwsElbv2LoadBalancerDetailsTypeDef(BaseModel):
    AvailabilityZones: Optional[Sequence[AvailabilityZoneTypeDef]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    State: Optional[LoadBalancerStateTypeDef] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[Sequence[AwsElbv2LoadBalancerAttributeTypeDef]] = None

class AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef(BaseModel):
    Primary: Optional[AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef] = None
    Secondary: Optional[       AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef     ] = None

class AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef(BaseModel):
    AuditLogs: Optional[AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef] = None

class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef(BaseModel):
    EbsVolumes: Optional[       AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef     ] = None

class AwsIamAccessKeySessionContextTypeDef(BaseModel):
    Attributes: Optional[AwsIamAccessKeySessionContextAttributesTypeDef] = None
    SessionIssuer: Optional[AwsIamAccessKeySessionContextSessionIssuerTypeDef] = None

class AwsIamGroupDetailsExtraOutputTypeDef(BaseModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[List[AwsIamGroupPolicyTypeDef]] = None
    Path: Optional[str] = None

class AwsIamGroupDetailsOutputTypeDef(BaseModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[List[AwsIamGroupPolicyTypeDef]] = None
    Path: Optional[str] = None

class AwsIamGroupDetailsTypeDef(BaseModel):
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[Sequence[AwsIamGroupPolicyTypeDef]] = None
    Path: Optional[str] = None

class AwsIamInstanceProfileExtraOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[List[AwsIamInstanceProfileRoleTypeDef]] = None

class AwsIamInstanceProfileOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[List[AwsIamInstanceProfileRoleTypeDef]] = None

class AwsIamInstanceProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[Sequence[AwsIamInstanceProfileRoleTypeDef]] = None

class AwsIamPolicyDetailsExtraOutputTypeDef(BaseModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[List[AwsIamPolicyVersionTypeDef]] = None
    UpdateDate: Optional[str] = None

class AwsIamPolicyDetailsOutputTypeDef(BaseModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[List[AwsIamPolicyVersionTypeDef]] = None
    UpdateDate: Optional[str] = None

class AwsIamPolicyDetailsTypeDef(BaseModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[Sequence[AwsIamPolicyVersionTypeDef]] = None
    UpdateDate: Optional[str] = None

class AwsIamUserDetailsExtraOutputTypeDef(BaseModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[List[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[List[AwsIamUserPolicyTypeDef]] = None

class AwsIamUserDetailsOutputTypeDef(BaseModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[List[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[List[AwsIamUserPolicyTypeDef]] = None

class AwsIamUserDetailsTypeDef(BaseModel):
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[Sequence[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[Sequence[AwsIamUserPolicyTypeDef]] = None

class AwsKinesisStreamDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    StreamEncryption: Optional[AwsKinesisStreamStreamEncryptionDetailsTypeDef] = None
    ShardCount: Optional[int] = None
    RetentionPeriodHours: Optional[int] = None

class AwsLambdaFunctionEnvironmentExtraOutputTypeDef(BaseModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentErrorTypeDef] = None

class AwsLambdaFunctionEnvironmentOutputTypeDef(BaseModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentErrorTypeDef] = None

class AwsLambdaFunctionEnvironmentTypeDef(BaseModel):
    Variables: Optional[Mapping[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentErrorTypeDef] = None

class AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef(BaseModel):
    Iam: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef] = None
    Scram: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef] = None

class AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef(BaseModel):
    EncryptionInTransit: Optional[       AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef     ] = None
    EncryptionAtRest: Optional[       AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef     ] = None

class AwsNetworkFirewallFirewallDetailsExtraOutputTypeDef(BaseModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[List[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsNetworkFirewallFirewallDetailsOutputTypeDef(BaseModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[List[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsNetworkFirewallFirewallDetailsTypeDef(BaseModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[       Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]     ] = None
    VpcId: Optional[str] = None

class AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef] = None

class AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef(BaseModel):
    InstanceCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[       AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef     ] = None
    DedicatedMasterCount: Optional[int] = None
    InstanceType: Optional[str] = None
    WarmType: Optional[str] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None

class AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef(BaseModel):
    IndexSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef] = None
    SearchSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef] = None
    AuditLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef] = None

class AwsRdsDbClusterDetailsExtraOutputTypeDef(BaseModel):
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
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[List[AwsRdsDbClusterAssociatedRoleTypeDef]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[       List[AwsRdsDbClusterOptionGroupMembershipTypeDef]     ] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[List[AwsRdsDbClusterMemberTypeDef]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None

class AwsRdsDbClusterDetailsOutputTypeDef(BaseModel):
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
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[List[AwsRdsDbClusterAssociatedRoleTypeDef]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[       List[AwsRdsDbClusterOptionGroupMembershipTypeDef]     ] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[List[AwsRdsDbClusterMemberTypeDef]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None

class AwsRdsDbClusterDetailsTypeDef(BaseModel):
    AllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[Sequence[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    DatabaseName: Optional[str] = None
    Status: Optional[str] = None
    Endpoint: Optional[str] = None
    ReaderEndpoint: Optional[str] = None
    CustomEndpoints: Optional[Sequence[str]] = None
    MultiAz: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReadReplicaIdentifiers: Optional[Sequence[str]] = None
    VpcSecurityGroups: Optional[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[Sequence[AwsRdsDbClusterAssociatedRoleTypeDef]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[Sequence[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[Sequence[AwsRdsDbDomainMembershipTypeDef]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[       Sequence[AwsRdsDbClusterOptionGroupMembershipTypeDef]     ] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[Sequence[AwsRdsDbClusterMemberTypeDef]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None

class AwsRdsDbClusterSnapshotDetailsExtraOutputTypeDef(BaseModel):
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
    DbClusterSnapshotAttributes: Optional[       List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeExtraOutputTypeDef]     ] = None

class AwsRdsDbClusterSnapshotDetailsOutputTypeDef(BaseModel):
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
    DbClusterSnapshotAttributes: Optional[       List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef]     ] = None

class AwsRdsDbClusterSnapshotDetailsTypeDef(BaseModel):
    AvailabilityZones: Optional[Sequence[str]] = None
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
    DbClusterSnapshotAttributes: Optional[       Sequence[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef]     ] = None

class AwsRdsDbSnapshotDetailsExtraOutputTypeDef(BaseModel):
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
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    DbiResourceId: Optional[str] = None

class AwsRdsDbSnapshotDetailsOutputTypeDef(BaseModel):
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
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    DbiResourceId: Optional[str] = None

class AwsRdsDbSnapshotDetailsTypeDef(BaseModel):
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
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeatureTypeDef]] = None
    DbiResourceId: Optional[str] = None

class AwsRdsDbPendingModifiedValuesExtraOutputTypeDef(BaseModel):
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
    PendingCloudWatchLogsExports: Optional[       AwsRdsPendingCloudWatchLogsExportsExtraOutputTypeDef     ] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None

class AwsRdsDbPendingModifiedValuesOutputTypeDef(BaseModel):
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
    PendingCloudWatchLogsExports: Optional[       AwsRdsPendingCloudWatchLogsExportsOutputTypeDef     ] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None

class AwsRdsDbPendingModifiedValuesTypeDef(BaseModel):
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
    PendingCloudWatchLogsExports: Optional[AwsRdsPendingCloudWatchLogsExportsTypeDef] = None
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeatureTypeDef]] = None

class AwsRdsDbSecurityGroupDetailsExtraOutputTypeDef(BaseModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[List[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]] = None
    IpRanges: Optional[List[AwsRdsDbSecurityGroupIpRangeTypeDef]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None

class AwsRdsDbSecurityGroupDetailsOutputTypeDef(BaseModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[List[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]] = None
    IpRanges: Optional[List[AwsRdsDbSecurityGroupIpRangeTypeDef]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None

class AwsRdsDbSecurityGroupDetailsTypeDef(BaseModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[Sequence[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]] = None
    IpRanges: Optional[Sequence[AwsRdsDbSecurityGroupIpRangeTypeDef]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None

class AwsRdsDbSubnetGroupSubnetTypeDef(BaseModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None

class AwsRedshiftClusterClusterParameterGroupExtraOutputTypeDef(BaseModel):
    ClusterParameterStatusList: Optional[       List[AwsRedshiftClusterClusterParameterStatusTypeDef]     ] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None

class AwsRedshiftClusterClusterParameterGroupOutputTypeDef(BaseModel):
    ClusterParameterStatusList: Optional[       List[AwsRedshiftClusterClusterParameterStatusTypeDef]     ] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None

class AwsRedshiftClusterClusterParameterGroupTypeDef(BaseModel):
    ClusterParameterStatusList: Optional[       Sequence[AwsRedshiftClusterClusterParameterStatusTypeDef]     ] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None

class AwsRoute53HostedZoneObjectDetailsTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[AwsRoute53HostedZoneConfigDetailsTypeDef] = None

class AwsRoute53QueryLoggingConfigDetailsTypeDef(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[CloudWatchLogsLogGroupArnConfigDetailsTypeDef] = None

class AwsS3AccessPointDetailsTypeDef(BaseModel):
    AccessPointArn: Optional[str] = None
    Alias: Optional[str] = None
    Bucket: Optional[str] = None
    BucketAccountId: Optional[str] = None
    Name: Optional[str] = None
    NetworkOrigin: Optional[str] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    VpcConfiguration: Optional[AwsS3AccessPointVpcConfigurationDetailsTypeDef] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterExtraOutputTypeDef(BaseModel):
    FilterRules: Optional[       List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef(BaseModel):
    FilterRules: Optional[       List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef(BaseModel):
    FilterRules: Optional[       Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]     ] = None

class AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef(BaseModel):
    DefaultRetention: Optional[       AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef     ] = None

class AwsS3BucketServerSideEncryptionRuleTypeDef(BaseModel):
    ApplyServerSideEncryptionByDefault: Optional[       AwsS3BucketServerSideEncryptionByDefaultTypeDef     ] = None

class AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef(BaseModel):
    Condition: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef] = None
    Redirect: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef] = None

class AwsSageMakerNotebookInstanceDetailsExtraOutputTypeDef(BaseModel):
    AcceleratorTypes: Optional[List[str]] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[       AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef     ] = None
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

class AwsSageMakerNotebookInstanceDetailsOutputTypeDef(BaseModel):
    AcceleratorTypes: Optional[List[str]] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[       AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef     ] = None
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

class AwsSageMakerNotebookInstanceDetailsTypeDef(BaseModel):
    AcceleratorTypes: Optional[Sequence[str]] = None
    AdditionalCodeRepositories: Optional[Sequence[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[       AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef     ] = None
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
    SecurityGroups: Optional[Sequence[str]] = None
    SubnetId: Optional[str] = None
    Url: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None

class AwsSecretsManagerSecretDetailsTypeDef(BaseModel):
    RotationRules: Optional[AwsSecretsManagerSecretRotationRulesTypeDef] = None
    RotationOccurredWithinFrequency: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    RotationEnabled: Optional[bool] = None
    RotationLambdaArn: Optional[str] = None
    Deleted: Optional[bool] = None
    Name: Optional[str] = None
    Description: Optional[str] = None

class BatchUpdateFindingsRequestRequestTypeDef(BaseModel):
    FindingIdentifiers: Sequence[AwsSecurityFindingIdentifierTypeDef]
    Note: Optional[NoteUpdateTypeDef] = None
    Severity: Optional[SeverityUpdateTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[Sequence[str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Workflow: Optional[WorkflowUpdateTypeDef] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None

class BatchUpdateFindingsUnprocessedFindingTypeDef(BaseModel):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    ErrorCode: str
    ErrorMessage: str

class AwsSnsTopicDetailsExtraOutputTypeDef(BaseModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[List[AwsSnsTopicSubscriptionTypeDef]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None

class AwsSnsTopicDetailsOutputTypeDef(BaseModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[List[AwsSnsTopicSubscriptionTypeDef]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None

class AwsSnsTopicDetailsTypeDef(BaseModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[Sequence[AwsSnsTopicSubscriptionTypeDef]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None

class AwsSsmPatchTypeDef(BaseModel):
    ComplianceSummary: Optional[AwsSsmComplianceSummaryTypeDef] = None

class AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef(BaseModel):
    CloudWatchLogsLogGroup: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef     ] = None

class AwsWafRateBasedRuleDetailsExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRateBasedRuleDetailsOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRateBasedRuleDetailsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[Sequence[AwsWafRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRateBasedRuleDetailsExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRateBasedRuleDetailsOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRateBasedRuleDetailsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[Sequence[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRuleDetailsExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRegionalRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRegionalRuleDetailsOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRegionalRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRegionalRuleDetailsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[Sequence[AwsWafRegionalRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRegionalRuleGroupRulesDetailsTypeDef(BaseModel):
    Action: Optional[AwsWafRegionalRuleGroupRulesActionDetailsTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafRegionalWebAclRulesListDetailsTypeDef(BaseModel):
    Action: Optional[AwsWafRegionalWebAclRulesListActionDetailsTypeDef] = None
    OverrideAction: Optional[AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafRuleDetailsExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRuleDetailsOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRuleDetailsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[Sequence[AwsWafRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRuleGroupRulesDetailsTypeDef(BaseModel):
    Action: Optional[AwsWafRuleGroupRulesActionDetailsTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafWebAclRuleExtraOutputTypeDef(BaseModel):
    Action: Optional[WafActionTypeDef] = None
    ExcludedRules: Optional[List[WafExcludedRuleTypeDef]] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafWebAclRuleOutputTypeDef(BaseModel):
    Action: Optional[WafActionTypeDef] = None
    ExcludedRules: Optional[List[WafExcludedRuleTypeDef]] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafWebAclRuleTypeDef(BaseModel):
    Action: Optional[WafActionTypeDef] = None
    ExcludedRules: Optional[Sequence[WafExcludedRuleTypeDef]] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef(BaseModel):
    InsertHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomRequestHandlingDetailsOutputTypeDef(BaseModel):
    InsertHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomRequestHandlingDetailsTypeDef(BaseModel):
    InsertHeaders: Optional[Sequence[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomResponseDetailsExtraOutputTypeDef(BaseModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomResponseDetailsOutputTypeDef(BaseModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomResponseDetailsTypeDef(BaseModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[Sequence[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2WebAclCaptchaConfigDetailsTypeDef(BaseModel):
    ImmunityTimeProperty: Optional[       AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef     ] = None

class CreateActionTargetResponseTypeDef(BaseModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutomationRuleResponseTypeDef(BaseModel):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingAggregatorResponseTypeDef(BaseModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInsightResponseTypeDef(BaseModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteActionTargetResponseTypeDef(BaseModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInsightResponseTypeDef(BaseModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActionTargetsResponseTypeDef(BaseModel):
    ActionTargets: List[ActionTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHubResponseTypeDef(BaseModel):
    HubArn: str
    SubscribedAt: str
    AutoEnableControls: bool
    ControlFindingGenerator: ControlFindingGeneratorType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImportFindingsForProductResponseTypeDef(BaseModel):
    ProductSubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationPolicyAssociationResponseTypeDef(BaseModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingAggregatorResponseTypeDef(BaseModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvitationsCountResponseTypeDef(BaseModel):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomationRulesResponseTypeDef(BaseModel):
    AutomationRulesMetadata: List[AutomationRulesMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEnabledProductsForImportResponseTypeDef(BaseModel):
    ProductSubscriptions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOrganizationAdminAccountsResponseTypeDef(BaseModel):
    AdminAccounts: List[AdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartConfigurationPolicyAssociationResponseTypeDef(BaseModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFindingAggregatorResponseTypeDef(BaseModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteAutomationRulesResponseTypeDef(BaseModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateAutomationRulesResponseTypeDef(BaseModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableStandardsRequestRequestTypeDef(BaseModel):
    StandardsSubscriptionRequests: Sequence[StandardsSubscriptionRequestTypeDef]

class ListConfigurationPolicyAssociationsResponseTypeDef(BaseModel):
    ConfigurationPolicyAssociationSummaries: List[       ConfigurationPolicyAssociationSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetStandardsControlAssociationsRequestRequestTypeDef(BaseModel):
    StandardsControlAssociationIds: Sequence[StandardsControlAssociationIdTypeDef]

class UnprocessedStandardsControlAssociationTypeDef(BaseModel):
    StandardsControlAssociationId: StandardsControlAssociationIdTypeDef
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None

class BatchImportFindingsResponseTypeDef(BaseModel):
    FailedCount: int
    SuccessCount: int
    FailedFindings: List[ImportFindingsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateStandardsControlAssociationsRequestRequestTypeDef(BaseModel):
    StandardsControlAssociationUpdates: Sequence[StandardsControlAssociationUpdateTypeDef]

class UnprocessedStandardsControlAssociationUpdateTypeDef(BaseModel):
    StandardsControlAssociationUpdate: StandardsControlAssociationUpdateTypeDef
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None

class VulnerabilityCodeVulnerabilitiesExtraOutputTypeDef(BaseModel):
    Cwes: Optional[List[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePathTypeDef] = None
    SourceArn: Optional[str] = None

class VulnerabilityCodeVulnerabilitiesOutputTypeDef(BaseModel):
    Cwes: Optional[List[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePathTypeDef] = None
    SourceArn: Optional[str] = None

class VulnerabilityCodeVulnerabilitiesTypeDef(BaseModel):
    Cwes: Optional[Sequence[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePathTypeDef] = None
    SourceArn: Optional[str] = None

class ComplianceExtraOutputTypeDef(BaseModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[List[str]] = None
    StatusReasons: Optional[List[StatusReasonTypeDef]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[List[AssociatedStandardTypeDef]] = None
    SecurityControlParameters: Optional[List[SecurityControlParameterExtraOutputTypeDef]] = None

class ComplianceOutputTypeDef(BaseModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[List[str]] = None
    StatusReasons: Optional[List[StatusReasonTypeDef]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[List[AssociatedStandardTypeDef]] = None
    SecurityControlParameters: Optional[List[SecurityControlParameterOutputTypeDef]] = None

class ComplianceTypeDef(BaseModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[Sequence[str]] = None
    StatusReasons: Optional[Sequence[StatusReasonTypeDef]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[Sequence[AssociatedStandardTypeDef]] = None
    SecurityControlParameters: Optional[Sequence[SecurityControlParameterTypeDef]] = None

class ConfigurationOptionsTypeDef(BaseModel):
    Integer: Optional[IntegerConfigurationOptionsTypeDef] = None
    IntegerList: Optional[IntegerListConfigurationOptionsTypeDef] = None
    Double: Optional[DoubleConfigurationOptionsTypeDef] = None
    String: Optional[StringConfigurationOptionsTypeDef] = None
    StringList: Optional[StringListConfigurationOptionsTypeDef] = None
    Boolean: Optional[BooleanConfigurationOptionsTypeDef] = None
    Enum: Optional[EnumConfigurationOptionsTypeDef] = None
    EnumList: Optional[EnumListConfigurationOptionsTypeDef] = None

class ConfigurationPolicyAssociationTypeDef(BaseModel):
    Target: Optional[TargetTypeDef] = None

class GetConfigurationPolicyAssociationRequestRequestTypeDef(BaseModel):
    Target: TargetTypeDef

class StartConfigurationPolicyAssociationRequestRequestTypeDef(BaseModel):
    ConfigurationPolicyIdentifier: str
    Target: TargetTypeDef

class StartConfigurationPolicyDisassociationRequestRequestTypeDef(BaseModel):
    ConfigurationPolicyIdentifier: str
    Target: Optional[TargetTypeDef] = None

class ListConfigurationPoliciesResponseTypeDef(BaseModel):
    ConfigurationPolicySummaries: List[ConfigurationPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContainerDetailsExtraOutputTypeDef(BaseModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMountTypeDef]] = None
    Privileged: Optional[bool] = None

class ContainerDetailsOutputTypeDef(BaseModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMountTypeDef]] = None
    Privileged: Optional[bool] = None

class ContainerDetailsTypeDef(BaseModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[Sequence[VolumeMountTypeDef]] = None
    Privileged: Optional[bool] = None

class CreateMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineInvitationsResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvitationsResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InviteMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DateFilterTypeDef(BaseModel):
    Start: Optional[str] = None
    End: Optional[str] = None
    DateRange: Optional[DateRangeTypeDef] = None

class DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef(BaseModel):
    ActionTargetArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeProductsRequestDescribeProductsPaginateTypeDef(BaseModel):
    ProductArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef(BaseModel):
    StandardsSubscriptionArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStandardsRequestDescribeStandardsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef(BaseModel):
    StandardsSubscriptionArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInsightsRequestGetInsightsPaginateTypeDef(BaseModel):
    InsightArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef(BaseModel):
    Filters: Optional[AssociationFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInvitationsRequestListInvitationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersRequestListMembersPaginateTypeDef(BaseModel):
    OnlyAssociated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef(BaseModel):
    StandardsArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef(BaseModel):
    SecurityControlId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConfigurationResponseTypeDef(BaseModel):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    AutoEnableStandards: AutoEnableStandardsType
    OrganizationConfiguration: OrganizationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    AutoEnable: bool
    AutoEnableStandards: Optional[AutoEnableStandardsType] = None
    OrganizationConfiguration: Optional[OrganizationConfigurationTypeDef] = None

class DescribeProductsResponseTypeDef(BaseModel):
    Products: List[ProductTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStandardsControlsResponseTypeDef(BaseModel):
    Controls: List[StandardsControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ThreatExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[FilePathsTypeDef]] = None

class ThreatOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[FilePathsTypeDef]] = None

class ThreatTypeDef(BaseModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[Sequence[FilePathsTypeDef]] = None

class ListFindingAggregatorsResponseTypeDef(BaseModel):
    FindingAggregators: List[FindingAggregatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FindingHistoryRecordTypeDef(BaseModel):
    FindingIdentifier: Optional[AwsSecurityFindingIdentifierTypeDef] = None
    UpdateTime: Optional[datetime] = None
    FindingCreated: Optional[bool] = None
    UpdateSource: Optional[FindingHistoryUpdateSourceTypeDef] = None
    Updates: Optional[List[FindingHistoryUpdateTypeDef]] = None
    NextToken: Optional[str] = None

class FindingProviderFieldsExtraOutputTypeDef(BaseModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Severity: Optional[FindingProviderSeverityTypeDef] = None
    Types: Optional[List[str]] = None

class FindingProviderFieldsOutputTypeDef(BaseModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Severity: Optional[FindingProviderSeverityTypeDef] = None
    Types: Optional[List[str]] = None

class FindingProviderFieldsTypeDef(BaseModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None
    Severity: Optional[FindingProviderSeverityTypeDef] = None
    Types: Optional[Sequence[str]] = None

class GetAdministratorAccountResponseTypeDef(BaseModel):
    Administrator: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMasterAccountResponseTypeDef(BaseModel):
    Master: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(BaseModel):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef(BaseModel):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetFindingHistoryRequestRequestTypeDef(BaseModel):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetMembersResponseTypeDef(BaseModel):
    Members: List[MemberTypeDef]
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseModel):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InsightResultsTypeDef(BaseModel):
    InsightArn: str
    GroupByAttribute: str
    ResultValues: List[InsightResultValueTypeDef]

class ListStandardsControlAssociationsResponseTypeDef(BaseModel):
    StandardsControlAssociationSummaries: List[StandardsControlAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NetworkPathComponentDetailsExtraOutputTypeDef(BaseModel):
    Address: Optional[List[str]] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None

class NetworkPathComponentDetailsOutputTypeDef(BaseModel):
    Address: Optional[List[str]] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None

class NetworkPathComponentDetailsTypeDef(BaseModel):
    Address: Optional[Sequence[str]] = None
    PortRanges: Optional[Sequence[PortRangeTypeDef]] = None

class NetworkTypeDef(BaseModel):
    Direction: Optional[NetworkDirectionType] = None
    Protocol: Optional[str] = None
    OpenPortRange: Optional[PortRangeTypeDef] = None
    SourceIpV4: Optional[str] = None
    SourceIpV6: Optional[str] = None
    SourcePort: Optional[int] = None
    SourceDomain: Optional[str] = None
    SourceMac: Optional[str] = None
    DestinationIpV4: Optional[str] = None
    DestinationIpV6: Optional[str] = None
    DestinationPort: Optional[int] = None
    DestinationDomain: Optional[str] = None

class PageTypeDef(BaseModel):
    PageNumber: Optional[int] = None
    LineRange: Optional[RangeTypeDef] = None
    OffsetRange: Optional[RangeTypeDef] = None

class ParameterConfigurationOutputTypeDef(BaseModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueOutputTypeDef] = None

class ParameterConfigurationTypeDef(BaseModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueTypeDef] = None

class RemediationTypeDef(BaseModel):
    Recommendation: Optional[RecommendationTypeDef] = None

class RuleGroupSourceStatefulRulesDetailsExtraOutputTypeDef(BaseModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef] = None
    RuleOptions: Optional[       List[RuleGroupSourceStatefulRulesOptionsDetailsExtraOutputTypeDef]     ] = None

class RuleGroupSourceStatefulRulesDetailsOutputTypeDef(BaseModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef] = None
    RuleOptions: Optional[List[RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef]] = None

class RuleGroupSourceStatefulRulesDetailsTypeDef(BaseModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef] = None
    RuleOptions: Optional[Sequence[RuleGroupSourceStatefulRulesOptionsDetailsTypeDef]] = None

class RuleGroupSourceStatelessRuleMatchAttributesExtraOutputTypeDef(BaseModel):
    DestinationPorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]     ] = None
    Destinations: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]     ] = None
    Protocols: Optional[List[int]] = None
    SourcePorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]     ] = None
    Sources: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]] = None
    TcpFlags: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsExtraOutputTypeDef]     ] = None

class RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef(BaseModel):
    DestinationPorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]     ] = None
    Destinations: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]     ] = None
    Protocols: Optional[List[int]] = None
    SourcePorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]     ] = None
    Sources: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]] = None
    TcpFlags: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef]     ] = None

class RuleGroupSourceStatelessRuleMatchAttributesTypeDef(BaseModel):
    DestinationPorts: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]     ] = None
    Destinations: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]     ] = None
    Protocols: Optional[Sequence[int]] = None
    SourcePorts: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]     ] = None
    Sources: Optional[Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]] = None
    TcpFlags: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef]     ] = None

class RuleGroupVariablesExtraOutputTypeDef(BaseModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsExtraOutputTypeDef] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsExtraOutputTypeDef] = None

class RuleGroupVariablesOutputTypeDef(BaseModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsOutputTypeDef] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsOutputTypeDef] = None

class RuleGroupVariablesTypeDef(BaseModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsTypeDef] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsTypeDef] = None

class StandardTypeDef(BaseModel):
    StandardsArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EnabledByDefault: Optional[bool] = None
    StandardsManagedBy: Optional[StandardsManagedByTypeDef] = None

class StandardsSubscriptionTypeDef(BaseModel):
    StandardsSubscriptionArn: str
    StandardsArn: str
    StandardsInput: Dict[str, str]
    StandardsStatus: StandardsStatusType
    StandardsStatusReason: Optional[StandardsStatusReasonTypeDef] = None

class StatelessCustomPublishMetricActionExtraOutputTypeDef(BaseModel):
    Dimensions: Optional[List[StatelessCustomPublishMetricActionDimensionTypeDef]] = None

class StatelessCustomPublishMetricActionOutputTypeDef(BaseModel):
    Dimensions: Optional[List[StatelessCustomPublishMetricActionDimensionTypeDef]] = None

class StatelessCustomPublishMetricActionTypeDef(BaseModel):
    Dimensions: Optional[Sequence[StatelessCustomPublishMetricActionDimensionTypeDef]] = None

class AwsApiCallActionExtraOutputTypeDef(BaseModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetailsTypeDef] = None
    AffectedResources: Optional[Dict[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None

class AwsApiCallActionOutputTypeDef(BaseModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetailsTypeDef] = None
    AffectedResources: Optional[Dict[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None

class AwsApiCallActionTypeDef(BaseModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetailsTypeDef] = None
    AffectedResources: Optional[Mapping[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None

class NetworkConnectionActionTypeDef(BaseModel):
    ConnectionDirection: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    RemotePortDetails: Optional[ActionRemotePortDetailsTypeDef] = None
    LocalPortDetails: Optional[ActionLocalPortDetailsTypeDef] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None

class PortProbeDetailTypeDef(BaseModel):
    LocalPortDetails: Optional[ActionLocalPortDetailsTypeDef] = None
    LocalIpDetails: Optional[ActionLocalIpDetailsTypeDef] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None

class AwsEc2RouteTableDetailsExtraOutputTypeDef(BaseModel):
    AssociationSet: Optional[List[AssociationSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[List[PropagatingVgwSetDetailsTypeDef]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[List[RouteSetDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsEc2RouteTableDetailsOutputTypeDef(BaseModel):
    AssociationSet: Optional[List[AssociationSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[List[PropagatingVgwSetDetailsTypeDef]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[List[RouteSetDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsEc2RouteTableDetailsTypeDef(BaseModel):
    AssociationSet: Optional[Sequence[AssociationSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[Sequence[PropagatingVgwSetDetailsTypeDef]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[Sequence[RouteSetDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AutomationRulesActionOutputTypeDef(BaseModel):
    Type: Optional[Literal["FINDING_FIELDS_UPDATE"]] = None
    FindingFieldsUpdate: Optional[AutomationRulesFindingFieldsUpdateOutputTypeDef] = None

class AutomationRulesActionTypeDef(BaseModel):
    Type: Optional[Literal["FINDING_FIELDS_UPDATE"]] = None
    FindingFieldsUpdate: Optional[AutomationRulesFindingFieldsUpdateTypeDef] = None

class AwsAmazonMqBrokerDetailsExtraOutputTypeDef(BaseModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[       AwsAmazonMqBrokerLdapServerMetadataDetailsExtraOutputTypeDef     ] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetailsTypeDef] = None
    MaintenanceWindowStartTime: Optional[       AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef     ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    Users: Optional[List[AwsAmazonMqBrokerUsersDetailsTypeDef]] = None

class AwsAmazonMqBrokerDetailsOutputTypeDef(BaseModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetailsTypeDef] = None
    MaintenanceWindowStartTime: Optional[       AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef     ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    Users: Optional[List[AwsAmazonMqBrokerUsersDetailsTypeDef]] = None

class AwsAmazonMqBrokerDetailsTypeDef(BaseModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetailsTypeDef] = None
    MaintenanceWindowStartTime: Optional[       AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef     ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[Sequence[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    Users: Optional[Sequence[AwsAmazonMqBrokerUsersDetailsTypeDef]] = None

class AwsAppSyncGraphQlApiDetailsExtraOutputTypeDef(BaseModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef] = None
    AdditionalAuthenticationProviders: Optional[       List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]     ] = None
    WafWebAclArn: Optional[str] = None

class AwsAppSyncGraphQlApiDetailsOutputTypeDef(BaseModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef] = None
    AdditionalAuthenticationProviders: Optional[       List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]     ] = None
    WafWebAclArn: Optional[str] = None

class AwsAppSyncGraphQlApiDetailsTypeDef(BaseModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef] = None
    AdditionalAuthenticationProviders: Optional[       Sequence[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]     ] = None
    WafWebAclArn: Optional[str] = None

class AwsAthenaWorkGroupConfigurationDetailsTypeDef(BaseModel):
    ResultConfiguration: Optional[       AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsExtraOutputTypeDef(BaseModel):
    InstancesDistribution: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsExtraOutputTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef(BaseModel):
    InstancesDistribution: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef(BaseModel):
    InstancesDistribution: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef     ] = None

class AwsAutoScalingLaunchConfigurationDetailsExtraOutputTypeDef(BaseModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[       List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]     ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[       AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef] = None

class AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef(BaseModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[       List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]     ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[       AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef] = None

class AwsAutoScalingLaunchConfigurationDetailsTypeDef(BaseModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[       Sequence[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]     ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[Sequence[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[       AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef] = None

class AwsBackupBackupPlanRuleDetailsExtraOutputTypeDef(BaseModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[List[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsBackupBackupPlanRuleDetailsOutputTypeDef(BaseModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[List[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsBackupBackupPlanRuleDetailsTypeDef(BaseModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[Sequence[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsCertificateManagerCertificateRenewalSummaryExtraOutputTypeDef(BaseModel):
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef]     ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

class AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef(BaseModel):
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]     ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

class AwsCertificateManagerCertificateRenewalSummaryTypeDef(BaseModel):
    DomainValidationOptions: Optional[       Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]     ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

class AwsCloudFrontDistributionOriginItemExtraOutputTypeDef(BaseModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[       AwsCloudFrontDistributionOriginCustomOriginConfigExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginItemOutputTypeDef(BaseModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[       AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginItemTypeDef(BaseModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef] = None

class AwsCloudFrontDistributionOriginGroupExtraOutputTypeDef(BaseModel):
    FailoverCriteria: Optional[       AwsCloudFrontDistributionOriginGroupFailoverExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginGroupOutputTypeDef(BaseModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef] = None

class AwsCloudFrontDistributionOriginGroupTypeDef(BaseModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverTypeDef] = None

class AwsCodeBuildProjectDetailsExtraOutputTypeDef(BaseModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentExtraOutputTypeDef] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSourceTypeDef] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetailsTypeDef] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigExtraOutputTypeDef] = None
    SecondaryArtifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None

class AwsCodeBuildProjectDetailsOutputTypeDef(BaseModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentOutputTypeDef] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSourceTypeDef] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetailsTypeDef] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigOutputTypeDef] = None
    SecondaryArtifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None

class AwsCodeBuildProjectDetailsTypeDef(BaseModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentTypeDef] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSourceTypeDef] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetailsTypeDef] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigTypeDef] = None
    SecondaryArtifacts: Optional[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None

class AwsDynamoDbTableReplicaExtraOutputTypeDef(BaseModel):
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]     ] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None

class AwsDynamoDbTableReplicaOutputTypeDef(BaseModel):
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]     ] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None

class AwsDynamoDbTableReplicaTypeDef(BaseModel):
    GlobalSecondaryIndexes: Optional[       Sequence[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]     ] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None

class AwsEc2ClientVpnEndpointDetailsExtraOutputTypeDef(BaseModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[       List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]     ] = None
    ConnectionLogOptions: Optional[       AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef     ] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[       AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef     ] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[       AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef     ] = None

class AwsEc2ClientVpnEndpointDetailsOutputTypeDef(BaseModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[       List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]     ] = None
    ConnectionLogOptions: Optional[       AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef     ] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[       AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef     ] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[       AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef     ] = None

class AwsEc2ClientVpnEndpointDetailsTypeDef(BaseModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[Sequence[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[       Sequence[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]     ] = None
    ConnectionLogOptions: Optional[       AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef     ] = None
    SecurityGroupIdSet: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[       AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef     ] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[       AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataDetailsExtraOutputTypeDef(BaseModel):
    BlockDeviceMappingSet: Optional[       List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]     ] = None
    CapacityReservationSpecification: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef     ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef] = None
    CreditSpecification: Optional[       AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef     ] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[       List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]     ] = None
    ElasticInferenceAcceleratorSet: Optional[       List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]     ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef     ] = None
    InstanceRequirements: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsDetailsExtraOutputTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[List[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef] = None
    NetworkInterfaceSet: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsExtraOutputTypeDef]     ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef] = None
    PrivateDnsNameOptions: Optional[       AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef     ] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    SecurityGroupSet: Optional[List[str]] = None
    UserData: Optional[str] = None

class AwsEc2LaunchTemplateDataDetailsOutputTypeDef(BaseModel):
    BlockDeviceMappingSet: Optional[       List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]     ] = None
    CapacityReservationSpecification: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef     ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef] = None
    CreditSpecification: Optional[       AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef     ] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[       List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]     ] = None
    ElasticInferenceAcceleratorSet: Optional[       List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]     ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef     ] = None
    InstanceRequirements: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[List[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef] = None
    NetworkInterfaceSet: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef]     ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef] = None
    PrivateDnsNameOptions: Optional[       AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef     ] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    SecurityGroupSet: Optional[List[str]] = None
    UserData: Optional[str] = None

class AwsEc2LaunchTemplateDataDetailsTypeDef(BaseModel):
    BlockDeviceMappingSet: Optional[       Sequence[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]     ] = None
    CapacityReservationSpecification: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef     ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef] = None
    CreditSpecification: Optional[       AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef     ] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[       Sequence[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]     ] = None
    ElasticInferenceAcceleratorSet: Optional[       Sequence[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]     ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef     ] = None
    InstanceRequirements: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[Sequence[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef] = None
    NetworkInterfaceSet: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef]     ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef] = None
    PrivateDnsNameOptions: Optional[       AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef     ] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[Sequence[str]] = None
    SecurityGroupSet: Optional[Sequence[str]] = None
    UserData: Optional[str] = None

class AwsEc2NetworkAclDetailsExtraOutputTypeDef(BaseModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[List[AwsEc2NetworkAclAssociationTypeDef]] = None
    Entries: Optional[List[AwsEc2NetworkAclEntryTypeDef]] = None

class AwsEc2NetworkAclDetailsOutputTypeDef(BaseModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[List[AwsEc2NetworkAclAssociationTypeDef]] = None
    Entries: Optional[List[AwsEc2NetworkAclEntryTypeDef]] = None

class AwsEc2NetworkAclDetailsTypeDef(BaseModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[Sequence[AwsEc2NetworkAclAssociationTypeDef]] = None
    Entries: Optional[Sequence[AwsEc2NetworkAclEntryTypeDef]] = None

class AwsEc2SecurityGroupDetailsExtraOutputTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[List[AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef]] = None
    IpPermissionsEgress: Optional[List[AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef]] = None

class AwsEc2SecurityGroupDetailsOutputTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]] = None
    IpPermissionsEgress: Optional[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]] = None

class AwsEc2SecurityGroupDetailsTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]] = None
    IpPermissionsEgress: Optional[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]] = None

class AwsEc2VpcPeeringConnectionDetailsExtraOutputTypeDef(BaseModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef] = None
    VpcPeeringConnectionId: Optional[str] = None

class AwsEc2VpcPeeringConnectionDetailsOutputTypeDef(BaseModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef] = None
    VpcPeeringConnectionId: Optional[str] = None

class AwsEc2VpcPeeringConnectionDetailsTypeDef(BaseModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef] = None
    VpcPeeringConnectionId: Optional[str] = None

class AwsEc2VpnConnectionDetailsExtraOutputTypeDef(BaseModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[List[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsExtraOutputTypeDef] = None
    Routes: Optional[List[AwsEc2VpnConnectionRoutesDetailsTypeDef]] = None
    TransitGatewayId: Optional[str] = None

class AwsEc2VpnConnectionDetailsOutputTypeDef(BaseModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[List[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsOutputTypeDef] = None
    Routes: Optional[List[AwsEc2VpnConnectionRoutesDetailsTypeDef]] = None
    TransitGatewayId: Optional[str] = None

class AwsEc2VpnConnectionDetailsTypeDef(BaseModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[Sequence[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsTypeDef] = None
    Routes: Optional[Sequence[AwsEc2VpnConnectionRoutesDetailsTypeDef]] = None
    TransitGatewayId: Optional[str] = None

class AwsEcsClusterConfigurationDetailsTypeDef(BaseModel):
    ExecuteCommandConfiguration: Optional[       AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef     ] = None

class AwsEcsServiceDetailsExtraOutputTypeDef(BaseModel):
    CapacityProviderStrategy: Optional[       List[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]     ] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetailsTypeDef] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetailsTypeDef] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[List[AwsEcsServiceLoadBalancersDetailsTypeDef]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[       AwsEcsServiceNetworkConfigurationDetailsExtraOutputTypeDef     ] = None
    PlacementConstraints: Optional[List[AwsEcsServicePlacementConstraintsDetailsTypeDef]] = None
    PlacementStrategies: Optional[List[AwsEcsServicePlacementStrategiesDetailsTypeDef]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[List[AwsEcsServiceServiceRegistriesDetailsTypeDef]] = None
    TaskDefinition: Optional[str] = None

class AwsEcsServiceDetailsOutputTypeDef(BaseModel):
    CapacityProviderStrategy: Optional[       List[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]     ] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetailsTypeDef] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetailsTypeDef] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[List[AwsEcsServiceLoadBalancersDetailsTypeDef]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef] = None
    PlacementConstraints: Optional[List[AwsEcsServicePlacementConstraintsDetailsTypeDef]] = None
    PlacementStrategies: Optional[List[AwsEcsServicePlacementStrategiesDetailsTypeDef]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[List[AwsEcsServiceServiceRegistriesDetailsTypeDef]] = None
    TaskDefinition: Optional[str] = None

class AwsEcsServiceDetailsTypeDef(BaseModel):
    CapacityProviderStrategy: Optional[       Sequence[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]     ] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetailsTypeDef] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetailsTypeDef] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[Sequence[AwsEcsServiceLoadBalancersDetailsTypeDef]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[AwsEcsServiceNetworkConfigurationDetailsTypeDef] = None
    PlacementConstraints: Optional[       Sequence[AwsEcsServicePlacementConstraintsDetailsTypeDef]     ] = None
    PlacementStrategies: Optional[       Sequence[AwsEcsServicePlacementStrategiesDetailsTypeDef]     ] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[Sequence[AwsEcsServiceServiceRegistriesDetailsTypeDef]] = None
    TaskDefinition: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsDetailsExtraOutputTypeDef(BaseModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]     ] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[List[str]] = None
    DnsServers: Optional[List[str]] = None
    DockerLabels: Optional[Dict[str, str]] = None
    DockerSecurityOptions: Optional[List[str]] = None
    EntryPoint: Optional[List[str]] = None
    Environment: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]     ] = None
    EnvironmentFiles: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]     ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]     ] = None
    FirelensConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsExtraOutputTypeDef     ] = None
    HealthCheck: Optional[       AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsExtraOutputTypeDef     ] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[List[str]] = None
    LinuxParameters: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsExtraOutputTypeDef     ] = None
    LogConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsExtraOutputTypeDef     ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]     ] = None
    Name: Optional[str] = None
    PortMappings: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]     ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[       AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef     ] = None
    ResourceRequirements: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]     ] = None
    Secrets: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]     ] = None
    Ulimits: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]     ] = None
    WorkingDirectory: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef(BaseModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]     ] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[List[str]] = None
    DnsServers: Optional[List[str]] = None
    DockerLabels: Optional[Dict[str, str]] = None
    DockerSecurityOptions: Optional[List[str]] = None
    EntryPoint: Optional[List[str]] = None
    Environment: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]     ] = None
    EnvironmentFiles: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]     ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]     ] = None
    FirelensConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef     ] = None
    HealthCheck: Optional[       AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef     ] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[List[str]] = None
    LinuxParameters: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef     ] = None
    LogConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef     ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]     ] = None
    Name: Optional[str] = None
    PortMappings: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]     ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[       AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef     ] = None
    ResourceRequirements: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]     ] = None
    Secrets: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]     ] = None
    Ulimits: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]     ] = None
    WorkingDirectory: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef(BaseModel):
    Command: Optional[Sequence[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]     ] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[Sequence[str]] = None
    DnsServers: Optional[Sequence[str]] = None
    DockerLabels: Optional[Mapping[str, str]] = None
    DockerSecurityOptions: Optional[Sequence[str]] = None
    EntryPoint: Optional[Sequence[str]] = None
    Environment: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]     ] = None
    EnvironmentFiles: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]     ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]     ] = None
    FirelensConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef     ] = None
    HealthCheck: Optional[       AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef     ] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[Sequence[str]] = None
    LinuxParameters: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef     ] = None
    LogConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef     ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]     ] = None
    Name: Optional[str] = None
    PortMappings: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]     ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[       AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef     ] = None
    ResourceRequirements: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]     ] = None
    Secrets: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]     ] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]     ] = None
    Ulimits: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]     ] = None
    User: Optional[str] = None
    VolumesFrom: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]     ] = None
    WorkingDirectory: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDetailsExtraOutputTypeDef(BaseModel):
    DockerVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsExtraOutputTypeDef     ] = None
    EfsVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef     ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef] = None
    Name: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef(BaseModel):
    DockerVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef     ] = None
    EfsVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef     ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef] = None
    Name: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDetailsTypeDef(BaseModel):
    DockerVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef     ] = None
    EfsVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef     ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef] = None
    Name: Optional[str] = None

class AwsEcsTaskDetailsExtraOutputTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskVolumeDetailsTypeDef]] = None
    Containers: Optional[List[AwsEcsContainerDetailsExtraOutputTypeDef]] = None

class AwsEcsTaskDetailsOutputTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskVolumeDetailsTypeDef]] = None
    Containers: Optional[List[AwsEcsContainerDetailsOutputTypeDef]] = None

class AwsEcsTaskDetailsTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[Sequence[AwsEcsTaskVolumeDetailsTypeDef]] = None
    Containers: Optional[Sequence[AwsEcsContainerDetailsTypeDef]] = None

class AwsEfsAccessPointDetailsExtraOutputTypeDef(BaseModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsExtraOutputTypeDef] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetailsTypeDef] = None

class AwsEfsAccessPointDetailsOutputTypeDef(BaseModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsOutputTypeDef] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetailsTypeDef] = None

class AwsEfsAccessPointDetailsTypeDef(BaseModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsTypeDef] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetailsTypeDef] = None

class AwsEksClusterDetailsExtraOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsExtraOutputTypeDef] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsExtraOutputTypeDef] = None

class AwsEksClusterDetailsOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsOutputTypeDef] = None

class AwsEksClusterDetailsTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsTypeDef] = None

class AwsElasticsearchDomainDetailsExtraOutputTypeDef(BaseModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptionsTypeDef] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef     ] = None
    EncryptionAtRestOptions: Optional[       AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef     ] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[       AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsExtraOutputTypeDef] = None

class AwsElasticsearchDomainDetailsOutputTypeDef(BaseModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptionsTypeDef] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef     ] = None
    EncryptionAtRestOptions: Optional[       AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef     ] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[       AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsOutputTypeDef] = None

class AwsElasticsearchDomainDetailsTypeDef(BaseModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptionsTypeDef] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Mapping[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef     ] = None
    EncryptionAtRestOptions: Optional[       AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef     ] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[       AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsTypeDef] = None

class AwsElbLoadBalancerDetailsExtraOutputTypeDef(BaseModel):
    AvailabilityZones: Optional[List[str]] = None
    BackendServerDescriptions: Optional[       List[AwsElbLoadBalancerBackendServerDescriptionExtraOutputTypeDef]     ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheckTypeDef] = None
    Instances: Optional[List[AwsElbLoadBalancerInstanceTypeDef]] = None
    ListenerDescriptions: Optional[       List[AwsElbLoadBalancerListenerDescriptionExtraOutputTypeDef]     ] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesExtraOutputTypeDef] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesExtraOutputTypeDef] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroupTypeDef] = None
    Subnets: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsElbLoadBalancerDetailsOutputTypeDef(BaseModel):
    AvailabilityZones: Optional[List[str]] = None
    BackendServerDescriptions: Optional[       List[AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef]     ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheckTypeDef] = None
    Instances: Optional[List[AwsElbLoadBalancerInstanceTypeDef]] = None
    ListenerDescriptions: Optional[       List[AwsElbLoadBalancerListenerDescriptionOutputTypeDef]     ] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesOutputTypeDef] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesOutputTypeDef] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroupTypeDef] = None
    Subnets: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsElbLoadBalancerDetailsTypeDef(BaseModel):
    AvailabilityZones: Optional[Sequence[str]] = None
    BackendServerDescriptions: Optional[       Sequence[AwsElbLoadBalancerBackendServerDescriptionTypeDef]     ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheckTypeDef] = None
    Instances: Optional[Sequence[AwsElbLoadBalancerInstanceTypeDef]] = None
    ListenerDescriptions: Optional[Sequence[AwsElbLoadBalancerListenerDescriptionTypeDef]] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesTypeDef] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesTypeDef] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroupTypeDef] = None
    Subnets: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None

class AwsEventsEndpointRoutingConfigDetailsTypeDef(BaseModel):
    FailoverConfig: Optional[AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef] = None

class AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef(BaseModel):
    ScanEc2InstanceWithFindings: Optional[       AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef     ] = None
    ServiceRole: Optional[str] = None

class AwsIamAccessKeyDetailsTypeDef(BaseModel):
    UserName: Optional[str] = None
    Status: Optional[AwsIamAccessKeyStatusType] = None
    CreatedAt: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[str] = None
    PrincipalName: Optional[str] = None
    AccountId: Optional[str] = None
    AccessKeyId: Optional[str] = None
    SessionContext: Optional[AwsIamAccessKeySessionContextTypeDef] = None

class AwsIamRoleDetailsExtraOutputTypeDef(BaseModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[List[AwsIamInstanceProfileExtraOutputTypeDef]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[List[AwsIamRolePolicyTypeDef]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None

class AwsIamRoleDetailsOutputTypeDef(BaseModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[List[AwsIamInstanceProfileOutputTypeDef]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[List[AwsIamRolePolicyTypeDef]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None

class AwsIamRoleDetailsTypeDef(BaseModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[Sequence[AwsIamInstanceProfileTypeDef]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[Sequence[AwsIamRolePolicyTypeDef]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None

class AwsLambdaFunctionDetailsExtraOutputTypeDef(BaseModel):
    Code: Optional[AwsLambdaFunctionCodeTypeDef] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfigTypeDef] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentExtraOutputTypeDef] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[List[AwsLambdaFunctionLayerTypeDef]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfigTypeDef] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigExtraOutputTypeDef] = None
    Version: Optional[str] = None
    Architectures: Optional[List[str]] = None
    PackageType: Optional[str] = None

class AwsLambdaFunctionDetailsOutputTypeDef(BaseModel):
    Code: Optional[AwsLambdaFunctionCodeTypeDef] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfigTypeDef] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentOutputTypeDef] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[List[AwsLambdaFunctionLayerTypeDef]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfigTypeDef] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigOutputTypeDef] = None
    Version: Optional[str] = None
    Architectures: Optional[List[str]] = None
    PackageType: Optional[str] = None

class AwsLambdaFunctionDetailsTypeDef(BaseModel):
    Code: Optional[AwsLambdaFunctionCodeTypeDef] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfigTypeDef] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentTypeDef] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[Sequence[AwsLambdaFunctionLayerTypeDef]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfigTypeDef] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigTypeDef] = None
    Version: Optional[str] = None
    Architectures: Optional[Sequence[str]] = None
    PackageType: Optional[str] = None

class AwsMskClusterClusterInfoClientAuthenticationDetailsExtraOutputTypeDef(BaseModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef] = None
    Unauthenticated: Optional[       AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef     ] = None
    Tls: Optional[       AwsMskClusterClusterInfoClientAuthenticationTlsDetailsExtraOutputTypeDef     ] = None

class AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef(BaseModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef] = None
    Unauthenticated: Optional[       AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef     ] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef] = None

class AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef(BaseModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef] = None
    Unauthenticated: Optional[       AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef     ] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef] = None

class AwsOpenSearchServiceDomainDetailsExtraOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[       AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef     ] = None
    NodeToNodeEncryptionOptions: Optional[       AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[       AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef     ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef] = None
    DomainEndpointOptions: Optional[       AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef     ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsExtraOutputTypeDef] = None
    LogPublishingOptions: Optional[       AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef     ] = None
    DomainEndpoints: Optional[Dict[str, str]] = None
    AdvancedSecurityOptions: Optional[       AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef     ] = None

class AwsOpenSearchServiceDomainDetailsOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[       AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef     ] = None
    NodeToNodeEncryptionOptions: Optional[       AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[       AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef     ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef] = None
    DomainEndpointOptions: Optional[       AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef     ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef] = None
    LogPublishingOptions: Optional[       AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef     ] = None
    DomainEndpoints: Optional[Dict[str, str]] = None
    AdvancedSecurityOptions: Optional[       AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef     ] = None

class AwsOpenSearchServiceDomainDetailsTypeDef(BaseModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[       AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef     ] = None
    NodeToNodeEncryptionOptions: Optional[       AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[       AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef     ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef] = None
    DomainEndpointOptions: Optional[       AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef     ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef] = None
    LogPublishingOptions: Optional[       AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef     ] = None
    DomainEndpoints: Optional[Mapping[str, str]] = None
    AdvancedSecurityOptions: Optional[       AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef     ] = None

class AwsRdsDbSubnetGroupExtraOutputTypeDef(BaseModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[AwsRdsDbSubnetGroupSubnetTypeDef]] = None
    DbSubnetGroupArn: Optional[str] = None

class AwsRdsDbSubnetGroupOutputTypeDef(BaseModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[AwsRdsDbSubnetGroupSubnetTypeDef]] = None
    DbSubnetGroupArn: Optional[str] = None

class AwsRdsDbSubnetGroupTypeDef(BaseModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[Sequence[AwsRdsDbSubnetGroupSubnetTypeDef]] = None
    DbSubnetGroupArn: Optional[str] = None

class AwsRedshiftClusterDetailsExtraOutputTypeDef(BaseModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[List[AwsRedshiftClusterClusterNodeTypeDef]] = None
    ClusterParameterGroups: Optional[       List[AwsRedshiftClusterClusterParameterGroupExtraOutputTypeDef]     ] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[List[AwsRedshiftClusterClusterSecurityGroupTypeDef]] = None
    ClusterSnapshotCopyStatus: Optional[       AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef     ] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[       List[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]     ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatusTypeDef] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpointTypeDef] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatusTypeDef] = None
    IamRoles: Optional[List[AwsRedshiftClusterIamRoleTypeDef]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[List[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValuesTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfoTypeDef] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatusTypeDef] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRedshiftClusterVpcSecurityGroupTypeDef]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatusTypeDef] = None

class AwsRedshiftClusterDetailsOutputTypeDef(BaseModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[List[AwsRedshiftClusterClusterNodeTypeDef]] = None
    ClusterParameterGroups: Optional[       List[AwsRedshiftClusterClusterParameterGroupOutputTypeDef]     ] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[List[AwsRedshiftClusterClusterSecurityGroupTypeDef]] = None
    ClusterSnapshotCopyStatus: Optional[       AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef     ] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[       List[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]     ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatusTypeDef] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpointTypeDef] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatusTypeDef] = None
    IamRoles: Optional[List[AwsRedshiftClusterIamRoleTypeDef]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[List[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValuesTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfoTypeDef] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatusTypeDef] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRedshiftClusterVpcSecurityGroupTypeDef]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatusTypeDef] = None

class AwsRedshiftClusterDetailsTypeDef(BaseModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[Sequence[AwsRedshiftClusterClusterNodeTypeDef]] = None
    ClusterParameterGroups: Optional[       Sequence[AwsRedshiftClusterClusterParameterGroupTypeDef]     ] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[       Sequence[AwsRedshiftClusterClusterSecurityGroupTypeDef]     ] = None
    ClusterSnapshotCopyStatus: Optional[       AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef     ] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[       Sequence[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]     ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatusTypeDef] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpointTypeDef] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatusTypeDef] = None
    IamRoles: Optional[Sequence[AwsRedshiftClusterIamRoleTypeDef]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[Sequence[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValuesTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfoTypeDef] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatusTypeDef] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[AwsRedshiftClusterVpcSecurityGroupTypeDef]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatusTypeDef] = None

class AwsRoute53HostedZoneDetailsExtraOutputTypeDef(BaseModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetailsTypeDef] = None
    Vpcs: Optional[List[AwsRoute53HostedZoneVpcDetailsTypeDef]] = None
    NameServers: Optional[List[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetailsTypeDef] = None

class AwsRoute53HostedZoneDetailsOutputTypeDef(BaseModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetailsTypeDef] = None
    Vpcs: Optional[List[AwsRoute53HostedZoneVpcDetailsTypeDef]] = None
    NameServers: Optional[List[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetailsTypeDef] = None

class AwsRoute53HostedZoneDetailsTypeDef(BaseModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetailsTypeDef] = None
    Vpcs: Optional[Sequence[AwsRoute53HostedZoneVpcDetailsTypeDef]] = None
    NameServers: Optional[Sequence[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetailsTypeDef] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsExtraOutputTypeDef(BaseModel):
    Operands: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]     ] = None
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef(BaseModel):
    Operands: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]     ] = None
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef(BaseModel):
    Operands: Optional[       Sequence[         AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationFilterExtraOutputTypeDef(BaseModel):
    S3KeyFilter: Optional[       AwsS3BucketNotificationConfigurationS3KeyFilterExtraOutputTypeDef     ] = None

class AwsS3BucketNotificationConfigurationFilterOutputTypeDef(BaseModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef] = None

class AwsS3BucketNotificationConfigurationFilterTypeDef(BaseModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef] = None

class AwsS3BucketObjectLockConfigurationTypeDef(BaseModel):
    ObjectLockEnabled: Optional[str] = None
    Rule: Optional[AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef] = None

class AwsS3BucketServerSideEncryptionConfigurationExtraOutputTypeDef(BaseModel):
    Rules: Optional[List[AwsS3BucketServerSideEncryptionRuleTypeDef]] = None

class AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef(BaseModel):
    Rules: Optional[List[AwsS3BucketServerSideEncryptionRuleTypeDef]] = None

class AwsS3BucketServerSideEncryptionConfigurationTypeDef(BaseModel):
    Rules: Optional[Sequence[AwsS3BucketServerSideEncryptionRuleTypeDef]] = None

class AwsS3BucketWebsiteConfigurationExtraOutputTypeDef(BaseModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectToTypeDef] = None
    RoutingRules: Optional[List[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]] = None

class AwsS3BucketWebsiteConfigurationOutputTypeDef(BaseModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectToTypeDef] = None
    RoutingRules: Optional[List[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]] = None

class AwsS3BucketWebsiteConfigurationTypeDef(BaseModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectToTypeDef] = None
    RoutingRules: Optional[Sequence[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]] = None

class BatchUpdateFindingsResponseTypeDef(BaseModel):
    ProcessedFindings: List[AwsSecurityFindingIdentifierTypeDef]
    UnprocessedFindings: List[BatchUpdateFindingsUnprocessedFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AwsSsmPatchComplianceDetailsTypeDef(BaseModel):
    Patch: Optional[AwsSsmPatchTypeDef] = None

class AwsStepFunctionStateMachineLoggingConfigurationDetailsExtraOutputTypeDef(BaseModel):
    Destinations: Optional[       List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]     ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None

class AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef(BaseModel):
    Destinations: Optional[       List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]     ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None

class AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef(BaseModel):
    Destinations: Optional[       Sequence[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]     ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None

class AwsWafRegionalRuleGroupDetailsExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRegionalRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRegionalRuleGroupDetailsOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRegionalRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRegionalRuleGroupDetailsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[Sequence[AwsWafRegionalRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRegionalWebAclDetailsExtraOutputTypeDef(BaseModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[List[AwsWafRegionalWebAclRulesListDetailsTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafRegionalWebAclDetailsOutputTypeDef(BaseModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[List[AwsWafRegionalWebAclRulesListDetailsTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafRegionalWebAclDetailsTypeDef(BaseModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[Sequence[AwsWafRegionalWebAclRulesListDetailsTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafRuleGroupDetailsExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRuleGroupDetailsOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRuleGroupDetailsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[Sequence[AwsWafRuleGroupRulesDetailsTypeDef]] = None

class AwsWafWebAclDetailsExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[List[AwsWafWebAclRuleExtraOutputTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafWebAclDetailsOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[List[AwsWafWebAclRuleOutputTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafWebAclDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[Sequence[AwsWafWebAclRuleTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafv2ActionAllowDetailsExtraOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[       AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef     ] = None

class AwsWafv2RulesActionCaptchaDetailsExtraOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[       AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef     ] = None

class AwsWafv2RulesActionCountDetailsExtraOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[       AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef     ] = None

class AwsWafv2ActionAllowDetailsOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef] = None

class AwsWafv2RulesActionCaptchaDetailsOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef] = None

class AwsWafv2RulesActionCountDetailsOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef] = None

class AwsWafv2ActionAllowDetailsTypeDef(BaseModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsTypeDef] = None

class AwsWafv2RulesActionCaptchaDetailsTypeDef(BaseModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsTypeDef] = None

class AwsWafv2RulesActionCountDetailsTypeDef(BaseModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsTypeDef] = None

class AwsWafv2ActionBlockDetailsExtraOutputTypeDef(BaseModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsExtraOutputTypeDef] = None

class AwsWafv2ActionBlockDetailsOutputTypeDef(BaseModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsOutputTypeDef] = None

class AwsWafv2ActionBlockDetailsTypeDef(BaseModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsTypeDef] = None

class BatchGetStandardsControlAssociationsResponseTypeDef(BaseModel):
    StandardsControlAssociationDetails: List[StandardsControlAssociationDetailTypeDef]
    UnprocessedAssociations: List[UnprocessedStandardsControlAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateStandardsControlAssociationsResponseTypeDef(BaseModel):
    UnprocessedAssociationUpdates: List[UnprocessedStandardsControlAssociationUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VulnerabilityExtraOutputTypeDef(BaseModel):
    Id: str
    VulnerablePackages: Optional[List[SoftwarePackageTypeDef]] = None
    Cvss: Optional[List[CvssExtraOutputTypeDef]] = None
    RelatedVulnerabilities: Optional[List[str]] = None
    Vendor: Optional[VulnerabilityVendorTypeDef] = None
    ReferenceUrls: Optional[List[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[       List[VulnerabilityCodeVulnerabilitiesExtraOutputTypeDef]     ] = None

class VulnerabilityOutputTypeDef(BaseModel):
    Id: str
    VulnerablePackages: Optional[List[SoftwarePackageTypeDef]] = None
    Cvss: Optional[List[CvssOutputTypeDef]] = None
    RelatedVulnerabilities: Optional[List[str]] = None
    Vendor: Optional[VulnerabilityVendorTypeDef] = None
    ReferenceUrls: Optional[List[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[List[VulnerabilityCodeVulnerabilitiesOutputTypeDef]] = None

class VulnerabilityTypeDef(BaseModel):
    Id: str
    VulnerablePackages: Optional[Sequence[SoftwarePackageTypeDef]] = None
    Cvss: Optional[Sequence[CvssTypeDef]] = None
    RelatedVulnerabilities: Optional[Sequence[str]] = None
    Vendor: Optional[VulnerabilityVendorTypeDef] = None
    ReferenceUrls: Optional[Sequence[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[Sequence[VulnerabilityCodeVulnerabilitiesTypeDef]] = None

class ParameterDefinitionTypeDef(BaseModel):
    Description: str
    ConfigurationOptions: ConfigurationOptionsTypeDef

class BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef(BaseModel):
    ConfigurationPolicyAssociationIdentifiers: Sequence[       ConfigurationPolicyAssociationTypeDef     ]

class UnprocessedConfigurationPolicyAssociationTypeDef(BaseModel):
    ConfigurationPolicyAssociationIdentifiers: Optional[       ConfigurationPolicyAssociationTypeDef     ] = None
    ErrorCode: Optional[str] = None
    ErrorReason: Optional[str] = None

class AutomationRulesFindingFiltersOutputTypeDef(BaseModel):
    ProductArn: Optional[List[StringFilterTypeDef]] = None
    AwsAccountId: Optional[List[StringFilterTypeDef]] = None
    Id: Optional[List[StringFilterTypeDef]] = None
    GeneratorId: Optional[List[StringFilterTypeDef]] = None
    Type: Optional[List[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[List[DateFilterTypeDef]] = None
    LastObservedAt: Optional[List[DateFilterTypeDef]] = None
    CreatedAt: Optional[List[DateFilterTypeDef]] = None
    UpdatedAt: Optional[List[DateFilterTypeDef]] = None
    Confidence: Optional[List[NumberFilterTypeDef]] = None
    Criticality: Optional[List[NumberFilterTypeDef]] = None
    Title: Optional[List[StringFilterTypeDef]] = None
    Description: Optional[List[StringFilterTypeDef]] = None
    SourceUrl: Optional[List[StringFilterTypeDef]] = None
    ProductName: Optional[List[StringFilterTypeDef]] = None
    CompanyName: Optional[List[StringFilterTypeDef]] = None
    SeverityLabel: Optional[List[StringFilterTypeDef]] = None
    ResourceType: Optional[List[StringFilterTypeDef]] = None
    ResourceId: Optional[List[StringFilterTypeDef]] = None
    ResourcePartition: Optional[List[StringFilterTypeDef]] = None
    ResourceRegion: Optional[List[StringFilterTypeDef]] = None
    ResourceTags: Optional[List[MapFilterTypeDef]] = None
    ResourceDetailsOther: Optional[List[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[List[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilterTypeDef]] = None
    VerificationState: Optional[List[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[List[StringFilterTypeDef]] = None
    RecordState: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    NoteText: Optional[List[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[List[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[List[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[List[MapFilterTypeDef]] = None
    ResourceApplicationArn: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[List[StringFilterTypeDef]] = None
    AwsAccountName: Optional[List[StringFilterTypeDef]] = None

class AutomationRulesFindingFiltersTypeDef(BaseModel):
    ProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountId: Optional[Sequence[StringFilterTypeDef]] = None
    Id: Optional[Sequence[StringFilterTypeDef]] = None
    GeneratorId: Optional[Sequence[StringFilterTypeDef]] = None
    Type: Optional[Sequence[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    LastObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    CreatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    UpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    Confidence: Optional[Sequence[NumberFilterTypeDef]] = None
    Criticality: Optional[Sequence[NumberFilterTypeDef]] = None
    Title: Optional[Sequence[StringFilterTypeDef]] = None
    Description: Optional[Sequence[StringFilterTypeDef]] = None
    SourceUrl: Optional[Sequence[StringFilterTypeDef]] = None
    ProductName: Optional[Sequence[StringFilterTypeDef]] = None
    CompanyName: Optional[Sequence[StringFilterTypeDef]] = None
    SeverityLabel: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceType: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourcePartition: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceRegion: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceTags: Optional[Sequence[MapFilterTypeDef]] = None
    ResourceDetailsOther: Optional[Sequence[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[Sequence[StringFilterTypeDef]] = None
    VerificationState: Optional[Sequence[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[Sequence[StringFilterTypeDef]] = None
    RecordState: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[Sequence[StringFilterTypeDef]] = None
    NoteText: Optional[Sequence[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[Sequence[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[Sequence[MapFilterTypeDef]] = None
    ResourceApplicationArn: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountName: Optional[Sequence[StringFilterTypeDef]] = None

class AwsSecurityFindingFiltersExtraOutputTypeDef(BaseModel):
    ProductArn: Optional[List[StringFilterTypeDef]] = None
    AwsAccountId: Optional[List[StringFilterTypeDef]] = None
    Id: Optional[List[StringFilterTypeDef]] = None
    GeneratorId: Optional[List[StringFilterTypeDef]] = None
    Region: Optional[List[StringFilterTypeDef]] = None
    Type: Optional[List[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[List[DateFilterTypeDef]] = None
    LastObservedAt: Optional[List[DateFilterTypeDef]] = None
    CreatedAt: Optional[List[DateFilterTypeDef]] = None
    UpdatedAt: Optional[List[DateFilterTypeDef]] = None
    SeverityProduct: Optional[List[NumberFilterTypeDef]] = None
    SeverityNormalized: Optional[List[NumberFilterTypeDef]] = None
    SeverityLabel: Optional[List[StringFilterTypeDef]] = None
    Confidence: Optional[List[NumberFilterTypeDef]] = None
    Criticality: Optional[List[NumberFilterTypeDef]] = None
    Title: Optional[List[StringFilterTypeDef]] = None
    Description: Optional[List[StringFilterTypeDef]] = None
    RecommendationText: Optional[List[StringFilterTypeDef]] = None
    SourceUrl: Optional[List[StringFilterTypeDef]] = None
    ProductFields: Optional[List[MapFilterTypeDef]] = None
    ProductName: Optional[List[StringFilterTypeDef]] = None
    CompanyName: Optional[List[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[List[MapFilterTypeDef]] = None
    MalwareName: Optional[List[StringFilterTypeDef]] = None
    MalwareType: Optional[List[StringFilterTypeDef]] = None
    MalwarePath: Optional[List[StringFilterTypeDef]] = None
    MalwareState: Optional[List[StringFilterTypeDef]] = None
    NetworkDirection: Optional[List[StringFilterTypeDef]] = None
    NetworkProtocol: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkSourceIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkSourcePort: Optional[List[NumberFilterTypeDef]] = None
    NetworkSourceDomain: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceMac: Optional[List[StringFilterTypeDef]] = None
    NetworkDestinationIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationPort: Optional[List[NumberFilterTypeDef]] = None
    NetworkDestinationDomain: Optional[List[StringFilterTypeDef]] = None
    ProcessName: Optional[List[StringFilterTypeDef]] = None
    ProcessPath: Optional[List[StringFilterTypeDef]] = None
    ProcessPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessParentPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ProcessTerminatedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorType: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorValue: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorCategory: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorSource: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorSourceUrl: Optional[List[StringFilterTypeDef]] = None
    ResourceType: Optional[List[StringFilterTypeDef]] = None
    ResourceId: Optional[List[StringFilterTypeDef]] = None
    ResourcePartition: Optional[List[StringFilterTypeDef]] = None
    ResourceRegion: Optional[List[StringFilterTypeDef]] = None
    ResourceTags: Optional[List[MapFilterTypeDef]] = None
    ResourceAwsEc2InstanceType: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceKeyName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceVpcId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyStatus: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsIamUserUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceDetailsOther: Optional[List[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[List[StringFilterTypeDef]] = None
    VerificationState: Optional[List[StringFilterTypeDef]] = None
    WorkflowState: Optional[List[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[List[StringFilterTypeDef]] = None
    RecordState: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    NoteText: Optional[List[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[List[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[List[StringFilterTypeDef]] = None
    Keyword: Optional[List[KeywordFilterTypeDef]] = None
    FindingProviderFieldsConfidence: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsCriticality: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityLabel: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityOriginal: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsTypes: Optional[List[StringFilterTypeDef]] = None
    Sample: Optional[List[BooleanFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[List[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesExploitAvailable: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesFixAvailable: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersName: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersValue: Optional[List[StringFilterTypeDef]] = None
    AwsAccountName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationArn: Optional[List[StringFilterTypeDef]] = None

class AwsSecurityFindingFiltersOutputTypeDef(BaseModel):
    ProductArn: Optional[List[StringFilterTypeDef]] = None
    AwsAccountId: Optional[List[StringFilterTypeDef]] = None
    Id: Optional[List[StringFilterTypeDef]] = None
    GeneratorId: Optional[List[StringFilterTypeDef]] = None
    Region: Optional[List[StringFilterTypeDef]] = None
    Type: Optional[List[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[List[DateFilterTypeDef]] = None
    LastObservedAt: Optional[List[DateFilterTypeDef]] = None
    CreatedAt: Optional[List[DateFilterTypeDef]] = None
    UpdatedAt: Optional[List[DateFilterTypeDef]] = None
    SeverityProduct: Optional[List[NumberFilterTypeDef]] = None
    SeverityNormalized: Optional[List[NumberFilterTypeDef]] = None
    SeverityLabel: Optional[List[StringFilterTypeDef]] = None
    Confidence: Optional[List[NumberFilterTypeDef]] = None
    Criticality: Optional[List[NumberFilterTypeDef]] = None
    Title: Optional[List[StringFilterTypeDef]] = None
    Description: Optional[List[StringFilterTypeDef]] = None
    RecommendationText: Optional[List[StringFilterTypeDef]] = None
    SourceUrl: Optional[List[StringFilterTypeDef]] = None
    ProductFields: Optional[List[MapFilterTypeDef]] = None
    ProductName: Optional[List[StringFilterTypeDef]] = None
    CompanyName: Optional[List[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[List[MapFilterTypeDef]] = None
    MalwareName: Optional[List[StringFilterTypeDef]] = None
    MalwareType: Optional[List[StringFilterTypeDef]] = None
    MalwarePath: Optional[List[StringFilterTypeDef]] = None
    MalwareState: Optional[List[StringFilterTypeDef]] = None
    NetworkDirection: Optional[List[StringFilterTypeDef]] = None
    NetworkProtocol: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkSourceIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkSourcePort: Optional[List[NumberFilterTypeDef]] = None
    NetworkSourceDomain: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceMac: Optional[List[StringFilterTypeDef]] = None
    NetworkDestinationIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationPort: Optional[List[NumberFilterTypeDef]] = None
    NetworkDestinationDomain: Optional[List[StringFilterTypeDef]] = None
    ProcessName: Optional[List[StringFilterTypeDef]] = None
    ProcessPath: Optional[List[StringFilterTypeDef]] = None
    ProcessPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessParentPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ProcessTerminatedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorType: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorValue: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorCategory: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorSource: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorSourceUrl: Optional[List[StringFilterTypeDef]] = None
    ResourceType: Optional[List[StringFilterTypeDef]] = None
    ResourceId: Optional[List[StringFilterTypeDef]] = None
    ResourcePartition: Optional[List[StringFilterTypeDef]] = None
    ResourceRegion: Optional[List[StringFilterTypeDef]] = None
    ResourceTags: Optional[List[MapFilterTypeDef]] = None
    ResourceAwsEc2InstanceType: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceKeyName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceVpcId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyStatus: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsIamUserUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceDetailsOther: Optional[List[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[List[StringFilterTypeDef]] = None
    VerificationState: Optional[List[StringFilterTypeDef]] = None
    WorkflowState: Optional[List[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[List[StringFilterTypeDef]] = None
    RecordState: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    NoteText: Optional[List[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[List[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[List[StringFilterTypeDef]] = None
    Keyword: Optional[List[KeywordFilterTypeDef]] = None
    FindingProviderFieldsConfidence: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsCriticality: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityLabel: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityOriginal: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsTypes: Optional[List[StringFilterTypeDef]] = None
    Sample: Optional[List[BooleanFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[List[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesExploitAvailable: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesFixAvailable: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersName: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersValue: Optional[List[StringFilterTypeDef]] = None
    AwsAccountName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationArn: Optional[List[StringFilterTypeDef]] = None

class AwsSecurityFindingFiltersTypeDef(BaseModel):
    ProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountId: Optional[Sequence[StringFilterTypeDef]] = None
    Id: Optional[Sequence[StringFilterTypeDef]] = None
    GeneratorId: Optional[Sequence[StringFilterTypeDef]] = None
    Region: Optional[Sequence[StringFilterTypeDef]] = None
    Type: Optional[Sequence[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    LastObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    CreatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    UpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    SeverityProduct: Optional[Sequence[NumberFilterTypeDef]] = None
    SeverityNormalized: Optional[Sequence[NumberFilterTypeDef]] = None
    SeverityLabel: Optional[Sequence[StringFilterTypeDef]] = None
    Confidence: Optional[Sequence[NumberFilterTypeDef]] = None
    Criticality: Optional[Sequence[NumberFilterTypeDef]] = None
    Title: Optional[Sequence[StringFilterTypeDef]] = None
    Description: Optional[Sequence[StringFilterTypeDef]] = None
    RecommendationText: Optional[Sequence[StringFilterTypeDef]] = None
    SourceUrl: Optional[Sequence[StringFilterTypeDef]] = None
    ProductFields: Optional[Sequence[MapFilterTypeDef]] = None
    ProductName: Optional[Sequence[StringFilterTypeDef]] = None
    CompanyName: Optional[Sequence[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[Sequence[MapFilterTypeDef]] = None
    MalwareName: Optional[Sequence[StringFilterTypeDef]] = None
    MalwareType: Optional[Sequence[StringFilterTypeDef]] = None
    MalwarePath: Optional[Sequence[StringFilterTypeDef]] = None
    MalwareState: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkDirection: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkProtocol: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkSourceIpV4: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkSourceIpV6: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkSourcePort: Optional[Sequence[NumberFilterTypeDef]] = None
    NetworkSourceDomain: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkSourceMac: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkDestinationIpV4: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkDestinationIpV6: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkDestinationPort: Optional[Sequence[NumberFilterTypeDef]] = None
    NetworkDestinationDomain: Optional[Sequence[StringFilterTypeDef]] = None
    ProcessName: Optional[Sequence[StringFilterTypeDef]] = None
    ProcessPath: Optional[Sequence[StringFilterTypeDef]] = None
    ProcessPid: Optional[Sequence[NumberFilterTypeDef]] = None
    ProcessParentPid: Optional[Sequence[NumberFilterTypeDef]] = None
    ProcessLaunchedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ProcessTerminatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ThreatIntelIndicatorType: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorValue: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorCategory: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ThreatIntelIndicatorSource: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorSourceUrl: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceType: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourcePartition: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceRegion: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceTags: Optional[Sequence[MapFilterTypeDef]] = None
    ResourceAwsEc2InstanceType: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceImageId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[Sequence[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[Sequence[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceKeyName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceVpcId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyUserName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyStatus: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ResourceAwsIamUserUserName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerImageId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerImageName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerLaunchedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ResourceDetailsOther: Optional[Sequence[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[Sequence[StringFilterTypeDef]] = None
    VerificationState: Optional[Sequence[StringFilterTypeDef]] = None
    WorkflowState: Optional[Sequence[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[Sequence[StringFilterTypeDef]] = None
    RecordState: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[Sequence[StringFilterTypeDef]] = None
    NoteText: Optional[Sequence[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[Sequence[StringFilterTypeDef]] = None
    Keyword: Optional[Sequence[KeywordFilterTypeDef]] = None
    FindingProviderFieldsConfidence: Optional[Sequence[NumberFilterTypeDef]] = None
    FindingProviderFieldsCriticality: Optional[Sequence[NumberFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[Sequence[StringFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[       Sequence[StringFilterTypeDef]     ] = None
    FindingProviderFieldsSeverityLabel: Optional[Sequence[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityOriginal: Optional[Sequence[StringFilterTypeDef]] = None
    FindingProviderFieldsTypes: Optional[Sequence[StringFilterTypeDef]] = None
    Sample: Optional[Sequence[BooleanFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[Sequence[StringFilterTypeDef]] = None
    VulnerabilitiesExploitAvailable: Optional[Sequence[StringFilterTypeDef]] = None
    VulnerabilitiesFixAvailable: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersName: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersValue: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceApplicationArn: Optional[Sequence[StringFilterTypeDef]] = None

class GetFindingHistoryResponseTypeDef(BaseModel):
    Records: List[FindingHistoryRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetInsightResultsResponseTypeDef(BaseModel):
    InsightResults: InsightResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkHeaderExtraOutputTypeDef(BaseModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsExtraOutputTypeDef] = None
    Source: Optional[NetworkPathComponentDetailsExtraOutputTypeDef] = None

class NetworkHeaderOutputTypeDef(BaseModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsOutputTypeDef] = None
    Source: Optional[NetworkPathComponentDetailsOutputTypeDef] = None

class NetworkHeaderTypeDef(BaseModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsTypeDef] = None
    Source: Optional[NetworkPathComponentDetailsTypeDef] = None

class OccurrencesExtraOutputTypeDef(BaseModel):
    LineRanges: Optional[List[RangeTypeDef]] = None
    OffsetRanges: Optional[List[RangeTypeDef]] = None
    Pages: Optional[List[PageTypeDef]] = None
    Records: Optional[List[RecordTypeDef]] = None
    Cells: Optional[List[CellTypeDef]] = None

class OccurrencesOutputTypeDef(BaseModel):
    LineRanges: Optional[List[RangeTypeDef]] = None
    OffsetRanges: Optional[List[RangeTypeDef]] = None
    Pages: Optional[List[PageTypeDef]] = None
    Records: Optional[List[RecordTypeDef]] = None
    Cells: Optional[List[CellTypeDef]] = None

class OccurrencesTypeDef(BaseModel):
    LineRanges: Optional[Sequence[RangeTypeDef]] = None
    OffsetRanges: Optional[Sequence[RangeTypeDef]] = None
    Pages: Optional[Sequence[PageTypeDef]] = None
    Records: Optional[Sequence[RecordTypeDef]] = None
    Cells: Optional[Sequence[CellTypeDef]] = None

class SecurityControlCustomParameterOutputTypeDef(BaseModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutputTypeDef]] = None

class SecurityControlTypeDef(BaseModel):
    SecurityControlId: str
    SecurityControlArn: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    SecurityControlStatus: ControlStatusType
    UpdateStatus: Optional[UpdateStatusType] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutputTypeDef]] = None
    LastUpdateReason: Optional[str] = None

class SecurityControlCustomParameterTypeDef(BaseModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Mapping[str, ParameterConfigurationTypeDef]] = None

class RuleGroupSourceStatelessRuleDefinitionExtraOutputTypeDef(BaseModel):
    Actions: Optional[List[str]] = None
    MatchAttributes: Optional[       RuleGroupSourceStatelessRuleMatchAttributesExtraOutputTypeDef     ] = None

class RuleGroupSourceStatelessRuleDefinitionOutputTypeDef(BaseModel):
    Actions: Optional[List[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef] = None

class RuleGroupSourceStatelessRuleDefinitionTypeDef(BaseModel):
    Actions: Optional[Sequence[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesTypeDef] = None

class DescribeStandardsResponseTypeDef(BaseModel):
    Standards: List[StandardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchDisableStandardsResponseTypeDef(BaseModel):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableStandardsResponseTypeDef(BaseModel):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnabledStandardsResponseTypeDef(BaseModel):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StatelessCustomActionDefinitionExtraOutputTypeDef(BaseModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionExtraOutputTypeDef] = None

class StatelessCustomActionDefinitionOutputTypeDef(BaseModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionOutputTypeDef] = None

class StatelessCustomActionDefinitionTypeDef(BaseModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionTypeDef] = None

class PortProbeActionExtraOutputTypeDef(BaseModel):
    PortProbeDetails: Optional[List[PortProbeDetailTypeDef]] = None
    Blocked: Optional[bool] = None

class PortProbeActionOutputTypeDef(BaseModel):
    PortProbeDetails: Optional[List[PortProbeDetailTypeDef]] = None
    Blocked: Optional[bool] = None

class PortProbeActionTypeDef(BaseModel):
    PortProbeDetails: Optional[Sequence[PortProbeDetailTypeDef]] = None
    Blocked: Optional[bool] = None

class AwsAthenaWorkGroupDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[str] = None
    Configuration: Optional[AwsAthenaWorkGroupConfigurationDetailsTypeDef] = None

class AwsAutoScalingAutoScalingGroupDetailsExtraOutputTypeDef(BaseModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsExtraOutputTypeDef     ] = None
    AvailabilityZones: Optional[       List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    CapacityRebalance: Optional[bool] = None

class AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef(BaseModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef     ] = None
    AvailabilityZones: Optional[       List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    CapacityRebalance: Optional[bool] = None

class AwsAutoScalingAutoScalingGroupDetailsTypeDef(BaseModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[Sequence[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef     ] = None
    AvailabilityZones: Optional[       Sequence[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    CapacityRebalance: Optional[bool] = None

class AwsBackupBackupPlanBackupPlanDetailsExtraOutputTypeDef(BaseModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[       List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsExtraOutputTypeDef]     ] = None
    BackupPlanRule: Optional[List[AwsBackupBackupPlanRuleDetailsExtraOutputTypeDef]] = None

class AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef(BaseModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[       List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef]     ] = None
    BackupPlanRule: Optional[List[AwsBackupBackupPlanRuleDetailsOutputTypeDef]] = None

class AwsBackupBackupPlanBackupPlanDetailsTypeDef(BaseModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[       Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef]     ] = None
    BackupPlanRule: Optional[Sequence[AwsBackupBackupPlanRuleDetailsTypeDef]] = None

class AwsCertificateManagerCertificateDetailsExtraOutputTypeDef(BaseModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef]     ] = None
    ExtendedKeyUsages: Optional[       List[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]     ] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[List[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[List[AwsCertificateManagerCertificateKeyUsageTypeDef]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptionsTypeDef] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[       AwsCertificateManagerCertificateRenewalSummaryExtraOutputTypeDef     ] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    Type: Optional[str] = None

class AwsCertificateManagerCertificateDetailsOutputTypeDef(BaseModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]     ] = None
    ExtendedKeyUsages: Optional[       List[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]     ] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[List[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[List[AwsCertificateManagerCertificateKeyUsageTypeDef]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptionsTypeDef] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    Type: Optional[str] = None

class AwsCertificateManagerCertificateDetailsTypeDef(BaseModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[       Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]     ] = None
    ExtendedKeyUsages: Optional[       Sequence[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]     ] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[Sequence[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[Sequence[AwsCertificateManagerCertificateKeyUsageTypeDef]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptionsTypeDef] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[AwsCertificateManagerCertificateRenewalSummaryTypeDef] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[Sequence[str]] = None
    Type: Optional[str] = None

class AwsCloudFrontDistributionOriginsExtraOutputTypeDef(BaseModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginItemExtraOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginsOutputTypeDef(BaseModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginItemOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginsTypeDef(BaseModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionOriginItemTypeDef]] = None

class AwsCloudFrontDistributionOriginGroupsExtraOutputTypeDef(BaseModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginGroupExtraOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginGroupsOutputTypeDef(BaseModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginGroupOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginGroupsTypeDef(BaseModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionOriginGroupTypeDef]] = None

class AwsDynamoDbTableDetailsExtraOutputTypeDef(BaseModel):
    AttributeDefinitions: Optional[List[AwsDynamoDbTableAttributeDefinitionTypeDef]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummaryTypeDef] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableGlobalSecondaryIndexExtraOutputTypeDef]     ] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[       List[AwsDynamoDbTableLocalSecondaryIndexExtraOutputTypeDef]     ] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None
    Replicas: Optional[List[AwsDynamoDbTableReplicaExtraOutputTypeDef]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummaryTypeDef] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescriptionTypeDef] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecificationTypeDef] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

class AwsDynamoDbTableDetailsOutputTypeDef(BaseModel):
    AttributeDefinitions: Optional[List[AwsDynamoDbTableAttributeDefinitionTypeDef]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummaryTypeDef] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef]     ] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[       List[AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef]     ] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None
    Replicas: Optional[List[AwsDynamoDbTableReplicaOutputTypeDef]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummaryTypeDef] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescriptionTypeDef] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecificationTypeDef] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

class AwsDynamoDbTableDetailsTypeDef(BaseModel):
    AttributeDefinitions: Optional[Sequence[AwsDynamoDbTableAttributeDefinitionTypeDef]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummaryTypeDef] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       Sequence[AwsDynamoDbTableGlobalSecondaryIndexTypeDef]     ] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchemaTypeDef]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[Sequence[AwsDynamoDbTableLocalSecondaryIndexTypeDef]] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None
    Replicas: Optional[Sequence[AwsDynamoDbTableReplicaTypeDef]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummaryTypeDef] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescriptionTypeDef] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecificationTypeDef] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

class AwsEc2LaunchTemplateDetailsExtraOutputTypeDef(BaseModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsExtraOutputTypeDef] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None

class AwsEc2LaunchTemplateDetailsOutputTypeDef(BaseModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsOutputTypeDef] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None

class AwsEc2LaunchTemplateDetailsTypeDef(BaseModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsTypeDef] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None

class AwsEcsClusterDetailsExtraOutputTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[List[str]] = None
    ClusterSettings: Optional[List[AwsEcsClusterClusterSettingsDetailsTypeDef]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetailsTypeDef] = None
    DefaultCapacityProviderStrategy: Optional[       List[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]     ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None

class AwsEcsClusterDetailsOutputTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[List[str]] = None
    ClusterSettings: Optional[List[AwsEcsClusterClusterSettingsDetailsTypeDef]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetailsTypeDef] = None
    DefaultCapacityProviderStrategy: Optional[       List[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]     ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None

class AwsEcsClusterDetailsTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[Sequence[str]] = None
    ClusterSettings: Optional[Sequence[AwsEcsClusterClusterSettingsDetailsTypeDef]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetailsTypeDef] = None
    DefaultCapacityProviderStrategy: Optional[       Sequence[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]     ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None

class AwsEcsTaskDefinitionDetailsExtraOutputTypeDef(BaseModel):
    ContainerDefinitions: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDetailsExtraOutputTypeDef]     ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[       List[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]     ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[       List[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]     ] = None
    ProxyConfiguration: Optional[       AwsEcsTaskDefinitionProxyConfigurationDetailsExtraOutputTypeDef     ] = None
    RequiresCompatibilities: Optional[List[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskDefinitionVolumesDetailsExtraOutputTypeDef]] = None
    Status: Optional[str] = None

class AwsEcsTaskDefinitionDetailsOutputTypeDef(BaseModel):
    ContainerDefinitions: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef]     ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[       List[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]     ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[       List[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]     ] = None
    ProxyConfiguration: Optional[       AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef     ] = None
    RequiresCompatibilities: Optional[List[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef]] = None
    Status: Optional[str] = None

class AwsEcsTaskDefinitionDetailsTypeDef(BaseModel):
    ContainerDefinitions: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef]     ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[       Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]     ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[       Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]     ] = None
    ProxyConfiguration: Optional[AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef] = None
    RequiresCompatibilities: Optional[Sequence[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[Sequence[AwsEcsTaskDefinitionVolumesDetailsTypeDef]] = None
    Status: Optional[str] = None

class AwsEventsEndpointDetailsExtraOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[List[AwsEventsEndpointEventBusesDetailsTypeDef]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetailsTypeDef] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None

class AwsEventsEndpointDetailsOutputTypeDef(BaseModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[List[AwsEventsEndpointEventBusesDetailsTypeDef]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetailsTypeDef] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None

class AwsEventsEndpointDetailsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[Sequence[AwsEventsEndpointEventBusesDetailsTypeDef]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetailsTypeDef] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesDetailsTypeDef(BaseModel):
    CloudTrail: Optional[AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef] = None
    DnsLogs: Optional[AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef] = None
    FlowLogs: Optional[AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef] = None
    Kubernetes: Optional[AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef] = None
    MalwareProtection: Optional[       AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef     ] = None
    S3Logs: Optional[AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef] = None

class AwsMskClusterClusterInfoDetailsExtraOutputTypeDef(BaseModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[       AwsMskClusterClusterInfoClientAuthenticationDetailsExtraOutputTypeDef     ] = None
    EnhancedMonitoring: Optional[str] = None

class AwsMskClusterClusterInfoDetailsOutputTypeDef(BaseModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[       AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef     ] = None
    EnhancedMonitoring: Optional[str] = None

class AwsMskClusterClusterInfoDetailsTypeDef(BaseModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[       AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef     ] = None
    EnhancedMonitoring: Optional[str] = None

class AwsRdsDbInstanceDetailsExtraOutputTypeDef(BaseModel):
    AssociatedRoles: Optional[List[AwsRdsDbInstanceAssociatedRoleTypeDef]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[List[str]] = None
    DbParameterGroups: Optional[List[AwsRdsDbParameterGroupTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupExtraOutputTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesExtraOutputTypeDef] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[AwsRdsDbOptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[List[AwsRdsDbStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    MaxAllocatedStorage: Optional[int] = None

class AwsRdsDbInstanceDetailsOutputTypeDef(BaseModel):
    AssociatedRoles: Optional[List[AwsRdsDbInstanceAssociatedRoleTypeDef]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[List[str]] = None
    DbParameterGroups: Optional[List[AwsRdsDbParameterGroupTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupOutputTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesOutputTypeDef] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[AwsRdsDbOptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[List[AwsRdsDbStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    MaxAllocatedStorage: Optional[int] = None

class AwsRdsDbInstanceDetailsTypeDef(BaseModel):
    AssociatedRoles: Optional[Sequence[AwsRdsDbInstanceAssociatedRoleTypeDef]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[Sequence[str]] = None
    DbParameterGroups: Optional[Sequence[AwsRdsDbParameterGroupTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesTypeDef] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[Sequence[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[Sequence[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[Sequence[AwsRdsDbOptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[Sequence[AwsRdsDbStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[Sequence[AwsRdsDbDomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeatureTypeDef]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    MaxAllocatedStorage: Optional[int] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsExtraOutputTypeDef(BaseModel):
    Predicate: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsExtraOutputTypeDef     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef(BaseModel):
    Predicate: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef(BaseModel):
    Predicate: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef     ] = None

class AwsS3BucketNotificationConfigurationDetailExtraOutputTypeDef(BaseModel):
    Events: Optional[List[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterExtraOutputTypeDef] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationDetailOutputTypeDef(BaseModel):
    Events: Optional[List[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterOutputTypeDef] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationDetailTypeDef(BaseModel):
    Events: Optional[Sequence[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterTypeDef] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None

class AwsStepFunctionStateMachineDetailsExtraOutputTypeDef(BaseModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDetailsExtraOutputTypeDef     ] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[       AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsStepFunctionStateMachineDetailsOutputTypeDef(BaseModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef     ] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[       AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsStepFunctionStateMachineDetailsTypeDef(BaseModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef     ] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[       AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsWafv2RulesActionDetailsExtraOutputTypeDef(BaseModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsExtraOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsExtraOutputTypeDef] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsExtraOutputTypeDef] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsExtraOutputTypeDef] = None

class AwsWafv2WebAclActionDetailsExtraOutputTypeDef(BaseModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsExtraOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsExtraOutputTypeDef] = None

class AwsWafv2RulesActionDetailsOutputTypeDef(BaseModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutputTypeDef] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsOutputTypeDef] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsOutputTypeDef] = None

class AwsWafv2WebAclActionDetailsOutputTypeDef(BaseModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutputTypeDef] = None

class AwsWafv2RulesActionDetailsTypeDef(BaseModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsTypeDef] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsTypeDef] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsTypeDef] = None

class AwsWafv2WebAclActionDetailsTypeDef(BaseModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsTypeDef] = None

class SecurityControlDefinitionTypeDef(BaseModel):
    SecurityControlId: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    CurrentRegionAvailability: RegionAvailabilityStatusType
    CustomizableProperties: Optional[List[Literal["Parameters"]]] = None
    ParameterDefinitions: Optional[Dict[str, ParameterDefinitionTypeDef]] = None

class BatchGetConfigurationPolicyAssociationsResponseTypeDef(BaseModel):
    ConfigurationPolicyAssociations: List[ConfigurationPolicyAssociationSummaryTypeDef]
    UnprocessedConfigurationPolicyAssociations: List[       UnprocessedConfigurationPolicyAssociationTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class AutomationRulesConfigTypeDef(BaseModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersOutputTypeDef] = None
    Actions: Optional[List[AutomationRulesActionOutputTypeDef]] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None

class UpdateAutomationRulesRequestItemTypeDef(BaseModel):
    RuleArn: str
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    Description: Optional[str] = None
    RuleName: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersTypeDef] = None
    Actions: Optional[Sequence[AutomationRulesActionTypeDef]] = None

class InsightTypeDef(BaseModel):
    InsightArn: str
    Name: str
    Filters: AwsSecurityFindingFiltersOutputTypeDef
    GroupByAttribute: str

class CreateInsightRequestRequestTypeDef(BaseModel):
    Name: str
    Filters: AwsSecurityFindingFiltersTypeDef
    GroupByAttribute: str

class GetFindingsRequestGetFindingsPaginateTypeDef(BaseModel):
    Filters: Optional[AwsSecurityFindingFiltersTypeDef] = None
    SortCriteria: Optional[Sequence[SortCriterionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetFindingsRequestRequestTypeDef(BaseModel):
    Filters: Optional[AwsSecurityFindingFiltersTypeDef] = None
    SortCriteria: Optional[Sequence[SortCriterionTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UpdateFindingsRequestRequestTypeDef(BaseModel):
    Filters: AwsSecurityFindingFiltersTypeDef
    Note: Optional[NoteUpdateTypeDef] = None
    RecordState: Optional[RecordStateType] = None

class UpdateInsightRequestRequestTypeDef(BaseModel):
    InsightArn: str
    Name: Optional[str] = None
    Filters: Optional[AwsSecurityFindingFiltersTypeDef] = None
    GroupByAttribute: Optional[str] = None

class NetworkPathComponentExtraOutputTypeDef(BaseModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderExtraOutputTypeDef] = None
    Ingress: Optional[NetworkHeaderExtraOutputTypeDef] = None

class NetworkPathComponentOutputTypeDef(BaseModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderOutputTypeDef] = None
    Ingress: Optional[NetworkHeaderOutputTypeDef] = None

class NetworkPathComponentTypeDef(BaseModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderTypeDef] = None
    Ingress: Optional[NetworkHeaderTypeDef] = None

class CustomDataIdentifiersDetectionsExtraOutputTypeDef(BaseModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesExtraOutputTypeDef] = None

class SensitiveDataDetectionsExtraOutputTypeDef(BaseModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesExtraOutputTypeDef] = None

class CustomDataIdentifiersDetectionsOutputTypeDef(BaseModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesOutputTypeDef] = None

class SensitiveDataDetectionsOutputTypeDef(BaseModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesOutputTypeDef] = None

class CustomDataIdentifiersDetectionsTypeDef(BaseModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesTypeDef] = None

class SensitiveDataDetectionsTypeDef(BaseModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesTypeDef] = None

class SecurityControlsConfigurationOutputTypeDef(BaseModel):
    EnabledSecurityControlIdentifiers: Optional[List[str]] = None
    DisabledSecurityControlIdentifiers: Optional[List[str]] = None
    SecurityControlCustomParameters: Optional[       List[SecurityControlCustomParameterOutputTypeDef]     ] = None

class BatchGetSecurityControlsResponseTypeDef(BaseModel):
    SecurityControls: List[SecurityControlTypeDef]
    UnprocessedIds: List[UnprocessedSecurityControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityControlRequestRequestTypeDef(BaseModel):
    SecurityControlId: str
    Parameters: Mapping[str, ParameterConfigurationUnionTypeDef]
    LastUpdateReason: Optional[str] = None

class SecurityControlsConfigurationTypeDef(BaseModel):
    EnabledSecurityControlIdentifiers: Optional[Sequence[str]] = None
    DisabledSecurityControlIdentifiers: Optional[Sequence[str]] = None
    SecurityControlCustomParameters: Optional[       Sequence[SecurityControlCustomParameterTypeDef]     ] = None

class RuleGroupSourceStatelessRulesDetailsExtraOutputTypeDef(BaseModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionExtraOutputTypeDef] = None

class RuleGroupSourceStatelessRulesDetailsOutputTypeDef(BaseModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionOutputTypeDef] = None

class RuleGroupSourceStatelessRulesDetailsTypeDef(BaseModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionTypeDef] = None

class FirewallPolicyStatelessCustomActionsDetailsExtraOutputTypeDef(BaseModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionExtraOutputTypeDef] = None
    ActionName: Optional[str] = None

class RuleGroupSourceCustomActionsDetailsExtraOutputTypeDef(BaseModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionExtraOutputTypeDef] = None
    ActionName: Optional[str] = None

class FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef(BaseModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutputTypeDef] = None
    ActionName: Optional[str] = None

class RuleGroupSourceCustomActionsDetailsOutputTypeDef(BaseModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutputTypeDef] = None
    ActionName: Optional[str] = None

class FirewallPolicyStatelessCustomActionsDetailsTypeDef(BaseModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionTypeDef] = None
    ActionName: Optional[str] = None

class RuleGroupSourceCustomActionsDetailsTypeDef(BaseModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionTypeDef] = None
    ActionName: Optional[str] = None

class ActionExtraOutputTypeDef(BaseModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    AwsApiCallAction: Optional[AwsApiCallActionExtraOutputTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionExtraOutputTypeDef] = None

class ActionOutputTypeDef(BaseModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    AwsApiCallAction: Optional[AwsApiCallActionOutputTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionOutputTypeDef] = None

class ActionTypeDef(BaseModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    AwsApiCallAction: Optional[AwsApiCallActionTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionTypeDef] = None

class CreateAutomationRuleRequestRequestTypeDef(BaseModel):
    RuleOrder: int
    RuleName: str
    Description: str
    Criteria: AutomationRulesFindingFiltersTypeDef
    Actions: Sequence[AutomationRulesActionUnionTypeDef]
    Tags: Optional[Mapping[str, str]] = None
    RuleStatus: Optional[RuleStatusType] = None
    IsTerminal: Optional[bool] = None

class AwsBackupBackupPlanDetailsExtraOutputTypeDef(BaseModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsExtraOutputTypeDef] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None

class AwsBackupBackupPlanDetailsOutputTypeDef(BaseModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None

class AwsBackupBackupPlanDetailsTypeDef(BaseModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsTypeDef] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None

class AwsCloudFrontDistributionDetailsExtraOutputTypeDef(BaseModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsExtraOutputTypeDef] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLoggingTypeDef] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsExtraOutputTypeDef] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsExtraOutputTypeDef] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificateTypeDef] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None

class AwsCloudFrontDistributionDetailsOutputTypeDef(BaseModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLoggingTypeDef] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsOutputTypeDef] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsOutputTypeDef] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificateTypeDef] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None

class AwsCloudFrontDistributionDetailsTypeDef(BaseModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsTypeDef] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLoggingTypeDef] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsTypeDef] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsTypeDef] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificateTypeDef] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None

class AwsGuardDutyDetectorDetailsExtraOutputTypeDef(BaseModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetailsTypeDef] = None
    Features: Optional[List[AwsGuardDutyDetectorFeaturesDetailsTypeDef]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None

class AwsGuardDutyDetectorDetailsOutputTypeDef(BaseModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetailsTypeDef] = None
    Features: Optional[List[AwsGuardDutyDetectorFeaturesDetailsTypeDef]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None

class AwsGuardDutyDetectorDetailsTypeDef(BaseModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetailsTypeDef] = None
    Features: Optional[Sequence[AwsGuardDutyDetectorFeaturesDetailsTypeDef]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None

class AwsMskClusterDetailsExtraOutputTypeDef(BaseModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsExtraOutputTypeDef] = None

class AwsMskClusterDetailsOutputTypeDef(BaseModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsOutputTypeDef] = None

class AwsMskClusterDetailsTypeDef(BaseModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsTypeDef] = None

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsExtraOutputTypeDef(BaseModel):
    AbortIncompleteMultipartUpload: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef     ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsExtraOutputTypeDef     ] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[       List[         AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef(BaseModel):
    AbortIncompleteMultipartUpload: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef     ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef     ] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[       List[         AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef(BaseModel):
    AbortIncompleteMultipartUpload: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef     ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[       Sequence[         AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[       Sequence[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationExtraOutputTypeDef(BaseModel):
    Configurations: Optional[       List[AwsS3BucketNotificationConfigurationDetailExtraOutputTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationOutputTypeDef(BaseModel):
    Configurations: Optional[       List[AwsS3BucketNotificationConfigurationDetailOutputTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationTypeDef(BaseModel):
    Configurations: Optional[Sequence[AwsS3BucketNotificationConfigurationDetailTypeDef]] = None

class AwsWafv2RulesDetailsExtraOutputTypeDef(BaseModel):
    Action: Optional[AwsWafv2RulesActionDetailsExtraOutputTypeDef] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RulesDetailsOutputTypeDef(BaseModel):
    Action: Optional[AwsWafv2RulesActionDetailsOutputTypeDef] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RulesDetailsTypeDef(BaseModel):
    Action: Optional[AwsWafv2RulesActionDetailsTypeDef] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class GetSecurityControlDefinitionResponseTypeDef(BaseModel):
    SecurityControlDefinition: SecurityControlDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityControlDefinitionsResponseTypeDef(BaseModel):
    SecurityControlDefinitions: List[SecurityControlDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetAutomationRulesResponseTypeDef(BaseModel):
    Rules: List[AutomationRulesConfigTypeDef]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateAutomationRulesRequestRequestTypeDef(BaseModel):
    UpdateAutomationRulesRequestItems: Sequence[UpdateAutomationRulesRequestItemTypeDef]

class GetInsightsResponseTypeDef(BaseModel):
    Insights: List[InsightTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CustomDataIdentifiersResultExtraOutputTypeDef(BaseModel):
    Detections: Optional[List[CustomDataIdentifiersDetectionsExtraOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class SensitiveDataResultExtraOutputTypeDef(BaseModel):
    Category: Optional[str] = None
    Detections: Optional[List[SensitiveDataDetectionsExtraOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class CustomDataIdentifiersResultOutputTypeDef(BaseModel):
    Detections: Optional[List[CustomDataIdentifiersDetectionsOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class SensitiveDataResultOutputTypeDef(BaseModel):
    Category: Optional[str] = None
    Detections: Optional[List[SensitiveDataDetectionsOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class CustomDataIdentifiersResultTypeDef(BaseModel):
    Detections: Optional[Sequence[CustomDataIdentifiersDetectionsTypeDef]] = None
    TotalCount: Optional[int] = None

class SensitiveDataResultTypeDef(BaseModel):
    Category: Optional[str] = None
    Detections: Optional[Sequence[SensitiveDataDetectionsTypeDef]] = None
    TotalCount: Optional[int] = None

class SecurityHubPolicyOutputTypeDef(BaseModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[List[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfigurationOutputTypeDef] = None

class SecurityHubPolicyTypeDef(BaseModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[Sequence[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfigurationTypeDef] = None

class FirewallPolicyDetailsExtraOutputTypeDef(BaseModel):
    StatefulRuleGroupReferences: Optional[       List[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]     ] = None
    StatelessCustomActions: Optional[       List[FirewallPolicyStatelessCustomActionsDetailsExtraOutputTypeDef]     ] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessRuleGroupReferences: Optional[       List[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]     ] = None

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsExtraOutputTypeDef(BaseModel):
    CustomActions: Optional[List[RuleGroupSourceCustomActionsDetailsExtraOutputTypeDef]] = None
    StatelessRules: Optional[List[RuleGroupSourceStatelessRulesDetailsExtraOutputTypeDef]] = None

class FirewallPolicyDetailsOutputTypeDef(BaseModel):
    StatefulRuleGroupReferences: Optional[       List[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]     ] = None
    StatelessCustomActions: Optional[       List[FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef]     ] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessRuleGroupReferences: Optional[       List[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]     ] = None

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef(BaseModel):
    CustomActions: Optional[List[RuleGroupSourceCustomActionsDetailsOutputTypeDef]] = None
    StatelessRules: Optional[List[RuleGroupSourceStatelessRulesDetailsOutputTypeDef]] = None

class FirewallPolicyDetailsTypeDef(BaseModel):
    StatefulRuleGroupReferences: Optional[       Sequence[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]     ] = None
    StatelessCustomActions: Optional[       Sequence[FirewallPolicyStatelessCustomActionsDetailsTypeDef]     ] = None
    StatelessDefaultActions: Optional[Sequence[str]] = None
    StatelessFragmentDefaultActions: Optional[Sequence[str]] = None
    StatelessRuleGroupReferences: Optional[       Sequence[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]     ] = None

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef(BaseModel):
    CustomActions: Optional[Sequence[RuleGroupSourceCustomActionsDetailsTypeDef]] = None
    StatelessRules: Optional[Sequence[RuleGroupSourceStatelessRulesDetailsTypeDef]] = None

class AwsS3BucketBucketLifecycleConfigurationDetailsExtraOutputTypeDef(BaseModel):
    Rules: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsExtraOutputTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef(BaseModel):
    Rules: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef(BaseModel):
    Rules: Optional[Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef]] = None

class AwsWafv2RuleGroupDetailsExtraOutputTypeDef(BaseModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsExtraOutputTypeDef]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2WebAclDetailsExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetailsTypeDef] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsExtraOutputTypeDef] = None
    Description: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsExtraOutputTypeDef]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RuleGroupDetailsOutputTypeDef(BaseModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutputTypeDef]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2WebAclDetailsOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetailsTypeDef] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsOutputTypeDef] = None
    Description: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutputTypeDef]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RuleGroupDetailsTypeDef(BaseModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[Sequence[AwsWafv2RulesDetailsTypeDef]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2WebAclDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetailsTypeDef] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsTypeDef] = None
    Description: Optional[str] = None
    Rules: Optional[Sequence[AwsWafv2RulesDetailsTypeDef]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class ClassificationResultExtraOutputTypeDef(BaseModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatusTypeDef] = None
    SensitiveData: Optional[List[SensitiveDataResultExtraOutputTypeDef]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultExtraOutputTypeDef] = None

class ClassificationResultOutputTypeDef(BaseModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatusTypeDef] = None
    SensitiveData: Optional[List[SensitiveDataResultOutputTypeDef]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultOutputTypeDef] = None

class ClassificationResultTypeDef(BaseModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatusTypeDef] = None
    SensitiveData: Optional[Sequence[SensitiveDataResultTypeDef]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultTypeDef] = None

class PolicyOutputTypeDef(BaseModel):
    SecurityHub: Optional[SecurityHubPolicyOutputTypeDef] = None

class PolicyTypeDef(BaseModel):
    SecurityHub: Optional[SecurityHubPolicyTypeDef] = None

class AwsNetworkFirewallFirewallPolicyDetailsExtraOutputTypeDef(BaseModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsExtraOutputTypeDef] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None

class RuleGroupSourceExtraOutputTypeDef(BaseModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsExtraOutputTypeDef] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[List[RuleGroupSourceStatefulRulesDetailsExtraOutputTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[       RuleGroupSourceStatelessRulesAndCustomActionsDetailsExtraOutputTypeDef     ] = None

class AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef(BaseModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsOutputTypeDef] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None

class RuleGroupSourceOutputTypeDef(BaseModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsOutputTypeDef] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[List[RuleGroupSourceStatefulRulesDetailsOutputTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[       RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef     ] = None

class AwsNetworkFirewallFirewallPolicyDetailsTypeDef(BaseModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsTypeDef] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None

class RuleGroupSourceTypeDef(BaseModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsTypeDef] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[Sequence[RuleGroupSourceStatefulRulesDetailsTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[       RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef     ] = None

class AwsS3BucketDetailsExtraOutputTypeDef(BaseModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[       AwsS3BucketServerSideEncryptionConfigurationExtraOutputTypeDef     ] = None
    BucketLifecycleConfiguration: Optional[       AwsS3BucketBucketLifecycleConfigurationDetailsExtraOutputTypeDef     ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfigurationTypeDef] = None
    BucketWebsiteConfiguration: Optional[       AwsS3BucketWebsiteConfigurationExtraOutputTypeDef     ] = None
    BucketNotificationConfiguration: Optional[       AwsS3BucketNotificationConfigurationExtraOutputTypeDef     ] = None
    BucketVersioningConfiguration: Optional[       AwsS3BucketBucketVersioningConfigurationTypeDef     ] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfigurationTypeDef] = None
    Name: Optional[str] = None

class AwsS3BucketDetailsOutputTypeDef(BaseModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[       AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef     ] = None
    BucketLifecycleConfiguration: Optional[       AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef     ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfigurationTypeDef] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationOutputTypeDef] = None
    BucketNotificationConfiguration: Optional[       AwsS3BucketNotificationConfigurationOutputTypeDef     ] = None
    BucketVersioningConfiguration: Optional[       AwsS3BucketBucketVersioningConfigurationTypeDef     ] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfigurationTypeDef] = None
    Name: Optional[str] = None

class AwsS3BucketDetailsTypeDef(BaseModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[       AwsS3BucketServerSideEncryptionConfigurationTypeDef     ] = None
    BucketLifecycleConfiguration: Optional[       AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef     ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfigurationTypeDef] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationTypeDef] = None
    BucketNotificationConfiguration: Optional[AwsS3BucketNotificationConfigurationTypeDef] = None
    BucketVersioningConfiguration: Optional[       AwsS3BucketBucketVersioningConfigurationTypeDef     ] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfigurationTypeDef] = None
    Name: Optional[str] = None

class DataClassificationDetailsExtraOutputTypeDef(BaseModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultExtraOutputTypeDef] = None

class DataClassificationDetailsOutputTypeDef(BaseModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultOutputTypeDef] = None

class DataClassificationDetailsTypeDef(BaseModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultTypeDef] = None

class CreateConfigurationPolicyResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationPolicyResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfigurationPolicyResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationPolicyRequestRequestTypeDef(BaseModel):
    Name: str
    ConfigurationPolicy: PolicyTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateConfigurationPolicyRequestRequestTypeDef(BaseModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedReason: Optional[str] = None
    ConfigurationPolicy: Optional[PolicyTypeDef] = None

class RuleGroupDetailsExtraOutputTypeDef(BaseModel):
    RuleVariables: Optional[RuleGroupVariablesExtraOutputTypeDef] = None
    RulesSource: Optional[RuleGroupSourceExtraOutputTypeDef] = None

class RuleGroupDetailsOutputTypeDef(BaseModel):
    RuleVariables: Optional[RuleGroupVariablesOutputTypeDef] = None
    RulesSource: Optional[RuleGroupSourceOutputTypeDef] = None

class RuleGroupDetailsTypeDef(BaseModel):
    RuleVariables: Optional[RuleGroupVariablesTypeDef] = None
    RulesSource: Optional[RuleGroupSourceTypeDef] = None

class AwsNetworkFirewallRuleGroupDetailsExtraOutputTypeDef(BaseModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsExtraOutputTypeDef] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None

class AwsNetworkFirewallRuleGroupDetailsOutputTypeDef(BaseModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsOutputTypeDef] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None

class AwsNetworkFirewallRuleGroupDetailsTypeDef(BaseModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsTypeDef] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None

class ResourceDetailsExtraOutputTypeDef(BaseModel):
    AwsAutoScalingAutoScalingGroup: Optional[       AwsAutoScalingAutoScalingGroupDetailsExtraOutputTypeDef     ] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsExtraOutputTypeDef] = None
    AwsCloudFrontDistribution: Optional[       AwsCloudFrontDistributionDetailsExtraOutputTypeDef     ] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsExtraOutputTypeDef] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsExtraOutputTypeDef] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsExtraOutputTypeDef] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsExtraOutputTypeDef] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsExtraOutputTypeDef] = None
    AwsEc2Eip: Optional[AwsEc2EipDetailsTypeDef] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsExtraOutputTypeDef] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsExtraOutputTypeDef] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsExtraOutputTypeDef] = None
    AwsElasticBeanstalkEnvironment: Optional[       AwsElasticBeanstalkEnvironmentDetailsExtraOutputTypeDef     ] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsExtraOutputTypeDef] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsExtraOutputTypeDef] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AwsS3Object: Optional[AwsS3ObjectDetailsTypeDef] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetailsTypeDef] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetailsTypeDef] = None
    AwsIamUser: Optional[AwsIamUserDetailsExtraOutputTypeDef] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsExtraOutputTypeDef] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsExtraOutputTypeDef] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsExtraOutputTypeDef] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsExtraOutputTypeDef] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsExtraOutputTypeDef] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsExtraOutputTypeDef] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetailsTypeDef] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetailsTypeDef] = None
    AwsCertificateManagerCertificate: Optional[       AwsCertificateManagerCertificateDetailsExtraOutputTypeDef     ] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsExtraOutputTypeDef] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsExtraOutputTypeDef] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsExtraOutputTypeDef] = None
    AwsIamRole: Optional[AwsIamRoleDetailsExtraOutputTypeDef] = None
    AwsKmsKey: Optional[AwsKmsKeyDetailsTypeDef] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsExtraOutputTypeDef] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsExtraOutputTypeDef] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsExtraOutputTypeDef] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsExtraOutputTypeDef] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetailsTypeDef] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsExtraOutputTypeDef] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsExtraOutputTypeDef] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsExtraOutputTypeDef] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsExtraOutputTypeDef] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsExtraOutputTypeDef] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsExtraOutputTypeDef] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsExtraOutputTypeDef] = None
    Container: Optional[ContainerDetailsExtraOutputTypeDef] = None
    Other: Optional[Dict[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsExtraOutputTypeDef] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsExtraOutputTypeDef] = None
    AwsAutoScalingLaunchConfiguration: Optional[       AwsAutoScalingLaunchConfigurationDetailsExtraOutputTypeDef     ] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsExtraOutputTypeDef] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsExtraOutputTypeDef] = None
    AwsOpenSearchServiceDomain: Optional[       AwsOpenSearchServiceDomainDetailsExtraOutputTypeDef     ] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsExtraOutputTypeDef] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetailsTypeDef] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsExtraOutputTypeDef] = None
    AwsWafRegionalRateBasedRule: Optional[       AwsWafRegionalRateBasedRuleDetailsExtraOutputTypeDef     ] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetailsTypeDef] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsExtraOutputTypeDef] = None
    AwsNetworkFirewallFirewallPolicy: Optional[       AwsNetworkFirewallFirewallPolicyDetailsExtraOutputTypeDef     ] = None
    AwsNetworkFirewallFirewall: Optional[       AwsNetworkFirewallFirewallDetailsExtraOutputTypeDef     ] = None
    AwsNetworkFirewallRuleGroup: Optional[       AwsNetworkFirewallRuleGroupDetailsExtraOutputTypeDef     ] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsExtraOutputTypeDef] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetailsTypeDef] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsExtraOutputTypeDef] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsExtraOutputTypeDef] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsExtraOutputTypeDef] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsExtraOutputTypeDef] = None
    AwsEc2VpcPeeringConnection: Optional[       AwsEc2VpcPeeringConnectionDetailsExtraOutputTypeDef     ] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsExtraOutputTypeDef] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsExtraOutputTypeDef] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsExtraOutputTypeDef] = None
    AwsWafRule: Optional[AwsWafRuleDetailsExtraOutputTypeDef] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsExtraOutputTypeDef] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsExtraOutputTypeDef] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsExtraOutputTypeDef] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsExtraOutputTypeDef] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetailsTypeDef] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsExtraOutputTypeDef] = None
    AwsSageMakerNotebookInstance: Optional[       AwsSageMakerNotebookInstanceDetailsExtraOutputTypeDef     ] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsExtraOutputTypeDef] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsExtraOutputTypeDef] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsExtraOutputTypeDef] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsExtraOutputTypeDef] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsExtraOutputTypeDef] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetailsTypeDef] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsExtraOutputTypeDef] = None
    AwsStepFunctionStateMachine: Optional[       AwsStepFunctionStateMachineDetailsExtraOutputTypeDef     ] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetailsTypeDef] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetailsTypeDef] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetailsTypeDef] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsExtraOutputTypeDef] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetailsTypeDef] = None
    AwsDmsReplicationInstance: Optional[       AwsDmsReplicationInstanceDetailsExtraOutputTypeDef     ] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsExtraOutputTypeDef] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsExtraOutputTypeDef] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetailsTypeDef] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsExtraOutputTypeDef] = None

class ResourceDetailsOutputTypeDef(BaseModel):
    AwsAutoScalingAutoScalingGroup: Optional[       AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef     ] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsOutputTypeDef] = None
    AwsCloudFrontDistribution: Optional[AwsCloudFrontDistributionDetailsOutputTypeDef] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsOutputTypeDef] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsOutputTypeDef] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsOutputTypeDef] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsOutputTypeDef] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsOutputTypeDef] = None
    AwsEc2Eip: Optional[AwsEc2EipDetailsTypeDef] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsOutputTypeDef] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsOutputTypeDef] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsOutputTypeDef] = None
    AwsElasticBeanstalkEnvironment: Optional[       AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef     ] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsOutputTypeDef] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsOutputTypeDef] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AwsS3Object: Optional[AwsS3ObjectDetailsTypeDef] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetailsTypeDef] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetailsTypeDef] = None
    AwsIamUser: Optional[AwsIamUserDetailsOutputTypeDef] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsOutputTypeDef] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsOutputTypeDef] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsOutputTypeDef] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsOutputTypeDef] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsOutputTypeDef] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsOutputTypeDef] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetailsTypeDef] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetailsTypeDef] = None
    AwsCertificateManagerCertificate: Optional[       AwsCertificateManagerCertificateDetailsOutputTypeDef     ] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsOutputTypeDef] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsOutputTypeDef] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsOutputTypeDef] = None
    AwsIamRole: Optional[AwsIamRoleDetailsOutputTypeDef] = None
    AwsKmsKey: Optional[AwsKmsKeyDetailsTypeDef] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsOutputTypeDef] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsOutputTypeDef] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsOutputTypeDef] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsOutputTypeDef] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetailsTypeDef] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsOutputTypeDef] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsOutputTypeDef] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsOutputTypeDef] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsOutputTypeDef] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsOutputTypeDef] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsOutputTypeDef] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsOutputTypeDef] = None
    Container: Optional[ContainerDetailsOutputTypeDef] = None
    Other: Optional[Dict[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsOutputTypeDef] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsOutputTypeDef] = None
    AwsAutoScalingLaunchConfiguration: Optional[       AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef     ] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsOutputTypeDef] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsOutputTypeDef] = None
    AwsOpenSearchServiceDomain: Optional[AwsOpenSearchServiceDomainDetailsOutputTypeDef] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsOutputTypeDef] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetailsTypeDef] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsOutputTypeDef] = None
    AwsWafRegionalRateBasedRule: Optional[AwsWafRegionalRateBasedRuleDetailsOutputTypeDef] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetailsTypeDef] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsOutputTypeDef] = None
    AwsNetworkFirewallFirewallPolicy: Optional[       AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef     ] = None
    AwsNetworkFirewallFirewall: Optional[AwsNetworkFirewallFirewallDetailsOutputTypeDef] = None
    AwsNetworkFirewallRuleGroup: Optional[AwsNetworkFirewallRuleGroupDetailsOutputTypeDef] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsOutputTypeDef] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetailsTypeDef] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsOutputTypeDef] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsOutputTypeDef] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsOutputTypeDef] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsOutputTypeDef] = None
    AwsEc2VpcPeeringConnection: Optional[AwsEc2VpcPeeringConnectionDetailsOutputTypeDef] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsOutputTypeDef] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsOutputTypeDef] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsOutputTypeDef] = None
    AwsWafRule: Optional[AwsWafRuleDetailsOutputTypeDef] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsOutputTypeDef] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsOutputTypeDef] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsOutputTypeDef] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsOutputTypeDef] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetailsTypeDef] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsOutputTypeDef] = None
    AwsSageMakerNotebookInstance: Optional[       AwsSageMakerNotebookInstanceDetailsOutputTypeDef     ] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsOutputTypeDef] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsOutputTypeDef] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsOutputTypeDef] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsOutputTypeDef] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsOutputTypeDef] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetailsTypeDef] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsOutputTypeDef] = None
    AwsStepFunctionStateMachine: Optional[AwsStepFunctionStateMachineDetailsOutputTypeDef] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetailsTypeDef] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetailsTypeDef] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetailsTypeDef] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsOutputTypeDef] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetailsTypeDef] = None
    AwsDmsReplicationInstance: Optional[AwsDmsReplicationInstanceDetailsOutputTypeDef] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsOutputTypeDef] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsOutputTypeDef] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetailsTypeDef] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsOutputTypeDef] = None

class ResourceDetailsTypeDef(BaseModel):
    AwsAutoScalingAutoScalingGroup: Optional[AwsAutoScalingAutoScalingGroupDetailsTypeDef] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsTypeDef] = None
    AwsCloudFrontDistribution: Optional[AwsCloudFrontDistributionDetailsTypeDef] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsTypeDef] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsTypeDef] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsTypeDef] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsTypeDef] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsTypeDef] = None
    AwsEc2Eip: Optional[AwsEc2EipDetailsTypeDef] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsTypeDef] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsTypeDef] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsTypeDef] = None
    AwsElasticBeanstalkEnvironment: Optional[AwsElasticBeanstalkEnvironmentDetailsTypeDef] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsTypeDef] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsTypeDef] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AwsS3Object: Optional[AwsS3ObjectDetailsTypeDef] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetailsTypeDef] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetailsTypeDef] = None
    AwsIamUser: Optional[AwsIamUserDetailsTypeDef] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsTypeDef] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsTypeDef] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsTypeDef] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsTypeDef] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsTypeDef] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsTypeDef] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetailsTypeDef] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetailsTypeDef] = None
    AwsCertificateManagerCertificate: Optional[       AwsCertificateManagerCertificateDetailsTypeDef     ] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsTypeDef] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsTypeDef] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsTypeDef] = None
    AwsIamRole: Optional[AwsIamRoleDetailsTypeDef] = None
    AwsKmsKey: Optional[AwsKmsKeyDetailsTypeDef] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsTypeDef] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsTypeDef] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsTypeDef] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsTypeDef] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetailsTypeDef] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsTypeDef] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsTypeDef] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsTypeDef] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsTypeDef] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsTypeDef] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsTypeDef] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsTypeDef] = None
    Container: Optional[ContainerDetailsTypeDef] = None
    Other: Optional[Mapping[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsTypeDef] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsTypeDef] = None
    AwsAutoScalingLaunchConfiguration: Optional[       AwsAutoScalingLaunchConfigurationDetailsTypeDef     ] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsTypeDef] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsTypeDef] = None
    AwsOpenSearchServiceDomain: Optional[AwsOpenSearchServiceDomainDetailsTypeDef] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsTypeDef] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetailsTypeDef] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsTypeDef] = None
    AwsWafRegionalRateBasedRule: Optional[AwsWafRegionalRateBasedRuleDetailsTypeDef] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetailsTypeDef] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsTypeDef] = None
    AwsNetworkFirewallFirewallPolicy: Optional[       AwsNetworkFirewallFirewallPolicyDetailsTypeDef     ] = None
    AwsNetworkFirewallFirewall: Optional[AwsNetworkFirewallFirewallDetailsTypeDef] = None
    AwsNetworkFirewallRuleGroup: Optional[AwsNetworkFirewallRuleGroupDetailsTypeDef] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsTypeDef] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetailsTypeDef] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsTypeDef] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsTypeDef] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsTypeDef] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsTypeDef] = None
    AwsEc2VpcPeeringConnection: Optional[AwsEc2VpcPeeringConnectionDetailsTypeDef] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsTypeDef] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsTypeDef] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsTypeDef] = None
    AwsWafRule: Optional[AwsWafRuleDetailsTypeDef] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsTypeDef] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsTypeDef] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsTypeDef] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsTypeDef] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetailsTypeDef] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsTypeDef] = None
    AwsSageMakerNotebookInstance: Optional[AwsSageMakerNotebookInstanceDetailsTypeDef] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsTypeDef] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsTypeDef] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsTypeDef] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsTypeDef] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsTypeDef] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetailsTypeDef] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsTypeDef] = None
    AwsStepFunctionStateMachine: Optional[AwsStepFunctionStateMachineDetailsTypeDef] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetailsTypeDef] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetailsTypeDef] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetailsTypeDef] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsTypeDef] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetailsTypeDef] = None
    AwsDmsReplicationInstance: Optional[AwsDmsReplicationInstanceDetailsTypeDef] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsTypeDef] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsTypeDef] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetailsTypeDef] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsTypeDef] = None

class ResourceExtraOutputTypeDef(BaseModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsExtraOutputTypeDef] = None
    Details: Optional[ResourceDetailsExtraOutputTypeDef] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None

class ResourceOutputTypeDef(BaseModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsOutputTypeDef] = None
    Details: Optional[ResourceDetailsOutputTypeDef] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None

class ResourceTypeDef(BaseModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsTypeDef] = None
    Details: Optional[ResourceDetailsTypeDef] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None

class AwsSecurityFindingExtraOutputTypeDef(BaseModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceExtraOutputTypeDef]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[List[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[SeverityTypeDef] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[RemediationTypeDef] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Dict[str, str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Malware: Optional[List[MalwareTypeDef]] = None
    Network: Optional[NetworkTypeDef] = None
    NetworkPath: Optional[List[NetworkPathComponentExtraOutputTypeDef]] = None
    Process: Optional[ProcessDetailsTypeDef] = None
    Threats: Optional[List[ThreatExtraOutputTypeDef]] = None
    ThreatIntelIndicators: Optional[List[ThreatIntelIndicatorTypeDef]] = None
    Compliance: Optional[ComplianceExtraOutputTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[WorkflowTypeDef] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Note: Optional[NoteTypeDef] = None
    Vulnerabilities: Optional[List[VulnerabilityExtraOutputTypeDef]] = None
    PatchSummary: Optional[PatchSummaryTypeDef] = None
    Action: Optional[ActionExtraOutputTypeDef] = None
    FindingProviderFields: Optional[FindingProviderFieldsExtraOutputTypeDef] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsExtraOutputTypeDef] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None

class AwsSecurityFindingOutputTypeDef(BaseModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceOutputTypeDef]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[List[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[SeverityTypeDef] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[RemediationTypeDef] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Dict[str, str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Malware: Optional[List[MalwareTypeDef]] = None
    Network: Optional[NetworkTypeDef] = None
    NetworkPath: Optional[List[NetworkPathComponentOutputTypeDef]] = None
    Process: Optional[ProcessDetailsTypeDef] = None
    Threats: Optional[List[ThreatOutputTypeDef]] = None
    ThreatIntelIndicators: Optional[List[ThreatIntelIndicatorTypeDef]] = None
    Compliance: Optional[ComplianceOutputTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[WorkflowTypeDef] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Note: Optional[NoteTypeDef] = None
    Vulnerabilities: Optional[List[VulnerabilityOutputTypeDef]] = None
    PatchSummary: Optional[PatchSummaryTypeDef] = None
    Action: Optional[ActionOutputTypeDef] = None
    FindingProviderFields: Optional[FindingProviderFieldsOutputTypeDef] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsOutputTypeDef] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None

class AwsSecurityFindingTypeDef(BaseModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: Sequence[ResourceTypeDef]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[Sequence[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[SeverityTypeDef] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[RemediationTypeDef] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Mapping[str, str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Malware: Optional[Sequence[MalwareTypeDef]] = None
    Network: Optional[NetworkTypeDef] = None
    NetworkPath: Optional[Sequence[NetworkPathComponentTypeDef]] = None
    Process: Optional[ProcessDetailsTypeDef] = None
    Threats: Optional[Sequence[ThreatTypeDef]] = None
    ThreatIntelIndicators: Optional[Sequence[ThreatIntelIndicatorTypeDef]] = None
    Compliance: Optional[ComplianceTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[WorkflowTypeDef] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None
    Note: Optional[NoteTypeDef] = None
    Vulnerabilities: Optional[Sequence[VulnerabilityTypeDef]] = None
    PatchSummary: Optional[PatchSummaryTypeDef] = None
    Action: Optional[ActionTypeDef] = None
    FindingProviderFields: Optional[FindingProviderFieldsTypeDef] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsTypeDef] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None

class GetFindingsResponseTypeDef(BaseModel):
    Findings: List[AwsSecurityFindingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchImportFindingsRequestRequestTypeDef(BaseModel):
    Findings: Sequence[AwsSecurityFindingUnionTypeDef]

