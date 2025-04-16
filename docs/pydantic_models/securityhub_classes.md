# Securityhub Classes

# AcceptAdministratorInvitationRequest

### AdministratorId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInvitationRequest

### MasterId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AccountDetails

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: typing.Optional[str]


# Action

### ActionType
- **Type**: typing.Optional[str]

### NetworkConnectionAction
- **Type**: <class 'NoneType'>

### AwsApiCallAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionUnion]

### DnsRequestAction
- **Type**: <class 'NoneType'>

### PortProbeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeActionUnion]


# ActionLocalIpDetails

### IpAddressV4
- **Type**: typing.Optional[str]


# ActionLocalPortDetails

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# ActionOutput

### ActionType
- **Type**: typing.Optional[str]

### NetworkConnectionAction
- **Type**: <class 'NoneType'>

### AwsApiCallAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionOutput]

### DnsRequestAction
- **Type**: <class 'NoneType'>

### PortProbeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeActionOutput]


# ActionRemoteIpDetails

### IpAddressV4
- **Type**: typing.Optional[str]

### Organization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.IpOrganizationDetails]

### Country
- **Type**: <class 'NoneType'>

### City
- **Type**: <class 'NoneType'>

### GeoLocation
- **Type**: <class 'NoneType'>


# ActionRemotePortDetails

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# ActionTarget

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# ActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Actor

### Id
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActorUser]

### Session
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActorSession]


# ActorSession

### Uid
- **Type**: typing.Optional[str]

### MfaStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CreatedTime
- **Type**: typing.Optional[int]

### Issuer
- **Type**: typing.Optional[str]


# ActorUser

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Adjustment

### Metric
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# AdminAccount

### AccountId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLE_IN_PROGRESS', 'ENABLED']]


# AssociatedStandard

### StandardsId
- **Type**: typing.Optional[str]


# AssociationFilters

### ConfigurationPolicyId
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['APPLIED', 'INHERITED']]

### AssociationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]


# AssociationSetDetails

### AssociationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AssociationStateDetails]

### GatewayId
- **Type**: typing.Optional[str]

### Main
- **Type**: typing.Optional[bool]

### RouteTableAssociationId
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]


# AssociationStateDetails

### State
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# AutomationRulesActionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutomationRulesActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutomationRulesConfig

### RuleArn
- **Type**: typing.Optional[str]

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RuleOrder
- **Type**: typing.Optional[int]

### RuleName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsTerminal
- **Type**: typing.Optional[bool]

### Criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFiltersOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesActionOutput]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]


# AutomationRulesFindingFieldsUpdate

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdate]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityUpdate]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowUpdate]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFinding]]


# AutomationRulesFindingFieldsUpdateOutput

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdate]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityUpdate]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Types
- **Type**: typing.Optional[typing.List[str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowUpdate]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFinding]]


# AutomationRulesFindingFiltersOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutomationRulesFindingFiltersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutomationRulesMetadata

### RuleArn
- **Type**: typing.Optional[str]

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RuleOrder
- **Type**: typing.Optional[int]

### RuleName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsTerminal
- **Type**: typing.Optional[bool]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]


# AvailabilityZone

### ZoneName
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]


# AwsAmazonMqBrokerDetails

### AuthenticationStrategy
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### BrokerArn
- **Type**: typing.Optional[str]

### BrokerName
- **Type**: typing.Optional[str]

### DeploymentMode
- **Type**: typing.Optional[str]

### EncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerEncryptionOptionsDetails]

### EngineType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLdapServerMetadataDetailsUnion]

### Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLogsDetails]

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### StorageType
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Users
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerUsersDetails]]


# AwsAmazonMqBrokerDetailsOutput

### AuthenticationStrategy
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### BrokerArn
- **Type**: typing.Optional[str]

### BrokerName
- **Type**: typing.Optional[str]

### DeploymentMode
- **Type**: typing.Optional[str]

### EncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerEncryptionOptionsDetails]

### EngineType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLdapServerMetadataDetailsOutput]

### Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLogsDetails]

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### StorageType
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Users
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerUsersDetails]]


# AwsAmazonMqBrokerEncryptionOptionsDetails

### KmsKeyId
- **Type**: typing.Optional[str]

### UseAwsOwnedKey
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerLdapServerMetadataDetails

### Hosts
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleBase
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RoleSearchMatching
- **Type**: typing.Optional[str]

### RoleSearchSubtree
- **Type**: typing.Optional[bool]

### ServiceAccountUsername
- **Type**: typing.Optional[str]

### UserBase
- **Type**: typing.Optional[str]

### UserRoleName
- **Type**: typing.Optional[str]

### UserSearchMatching
- **Type**: typing.Optional[str]

### UserSearchSubtree
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerLdapServerMetadataDetailsOutput

### Hosts
- **Type**: typing.Optional[typing.List[str]]

### RoleBase
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RoleSearchMatching
- **Type**: typing.Optional[str]

### RoleSearchSubtree
- **Type**: typing.Optional[bool]

### ServiceAccountUsername
- **Type**: typing.Optional[str]

### UserBase
- **Type**: typing.Optional[str]

### UserRoleName
- **Type**: typing.Optional[str]

### UserSearchMatching
- **Type**: typing.Optional[str]

### UserSearchSubtree
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerLdapServerMetadataDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAmazonMqBrokerLogsDetails

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]

### AuditLogGroup
- **Type**: typing.Optional[str]

### GeneralLogGroup
- **Type**: typing.Optional[str]

### Pending
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLogsPendingDetails]


# AwsAmazonMqBrokerLogsPendingDetails

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails

### DayOfWeek
- **Type**: typing.Optional[str]

### TimeOfDay
- **Type**: typing.Optional[str]

### TimeZone
- **Type**: typing.Optional[str]


# AwsAmazonMqBrokerUsersDetails

### PendingChange
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# AwsApiCallActionDomainDetails

### Domain
- **Type**: typing.Optional[str]


# AwsApiCallActionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsApiCallActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsApiGatewayAccessLogSettings

### Format
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]


# AwsApiGatewayCanarySettings

### PercentTraffic
- **Type**: typing.Optional[float]

### DeploymentId
- **Type**: typing.Optional[str]

### StageVariableOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UseStageCache
- **Type**: typing.Optional[bool]


# AwsApiGatewayCanarySettingsOutput

### PercentTraffic
- **Type**: typing.Optional[float]

### DeploymentId
- **Type**: typing.Optional[str]

### StageVariableOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### UseStageCache
- **Type**: typing.Optional[bool]


# AwsApiGatewayCanarySettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsApiGatewayEndpointConfiguration

### Types
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsApiGatewayEndpointConfigurationOutput

### Types
- **Type**: typing.Optional[typing.List[str]]


# AwsApiGatewayEndpointConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsApiGatewayMethodSettings

### MetricsEnabled
- **Type**: typing.Optional[bool]

### LoggingLevel
- **Type**: typing.Optional[str]

### DataTraceEnabled
- **Type**: typing.Optional[bool]

### ThrottlingBurstLimit
- **Type**: typing.Optional[int]

### ThrottlingRateLimit
- **Type**: typing.Optional[float]

### CachingEnabled
- **Type**: typing.Optional[bool]

### CacheTtlInSeconds
- **Type**: typing.Optional[int]

### CacheDataEncrypted
- **Type**: typing.Optional[bool]

### RequireAuthorizationForCacheControl
- **Type**: typing.Optional[bool]

### UnauthorizedCacheControlHeaderStrategy
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[str]

### ResourcePath
- **Type**: typing.Optional[str]


# AwsApiGatewayRestApiDetails

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### BinaryMediaTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### MinimumCompressionSize
- **Type**: typing.Optional[int]

### ApiKeySource
- **Type**: typing.Optional[str]

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayEndpointConfigurationUnion]


# AwsApiGatewayRestApiDetailsOutput

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### BinaryMediaTypes
- **Type**: typing.Optional[typing.List[str]]

### MinimumCompressionSize
- **Type**: typing.Optional[int]

### ApiKeySource
- **Type**: typing.Optional[str]

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayEndpointConfigurationOutput]


# AwsApiGatewayStageDetails

### DeploymentId
- **Type**: typing.Optional[str]

### ClientCertificateId
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CacheClusterEnabled
- **Type**: typing.Optional[bool]

### CacheClusterSize
- **Type**: typing.Optional[str]

### CacheClusterStatus
- **Type**: typing.Optional[str]

### MethodSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayMethodSettings]]

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DocumentationVersion
- **Type**: typing.Optional[str]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettings]

### CanarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayCanarySettingsUnion]

### TracingEnabled
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### WebAclArn
- **Type**: typing.Optional[str]


# AwsApiGatewayStageDetailsOutput

### DeploymentId
- **Type**: typing.Optional[str]

### ClientCertificateId
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CacheClusterEnabled
- **Type**: typing.Optional[bool]

### CacheClusterSize
- **Type**: typing.Optional[str]

### CacheClusterStatus
- **Type**: typing.Optional[str]

### MethodSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayMethodSettings]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### DocumentationVersion
- **Type**: typing.Optional[str]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettings]

### CanarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayCanarySettingsOutput]

### TracingEnabled
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### WebAclArn
- **Type**: typing.Optional[str]


# AwsApiGatewayV2ApiDetails

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiId
- **Type**: typing.Optional[str]

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ProtocolType
- **Type**: typing.Optional[str]

### RouteSelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCorsConfigurationUnion]


# AwsApiGatewayV2ApiDetailsOutput

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiId
- **Type**: typing.Optional[str]

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ProtocolType
- **Type**: typing.Optional[str]

### RouteSelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCorsConfigurationOutput]


# AwsApiGatewayV2RouteSettings

### DetailedMetricsEnabled
- **Type**: typing.Optional[bool]

### LoggingLevel
- **Type**: typing.Optional[str]

### DataTraceEnabled
- **Type**: typing.Optional[bool]

### ThrottlingBurstLimit
- **Type**: typing.Optional[int]

### ThrottlingRateLimit
- **Type**: typing.Optional[float]


# AwsApiGatewayV2StageDetails

### ClientCertificateId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettings]

### DeploymentId
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettings]

### StageName
- **Type**: typing.Optional[str]

### StageVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettings]

### AutoDeploy
- **Type**: typing.Optional[bool]

### LastDeploymentStatusMessage
- **Type**: typing.Optional[str]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]


# AwsApiGatewayV2StageDetailsOutput

### ClientCertificateId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettings]

### DeploymentId
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettings]

### StageName
- **Type**: typing.Optional[str]

### StageVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettings]

### AutoDeploy
- **Type**: typing.Optional[bool]

### LastDeploymentStatusMessage
- **Type**: typing.Optional[str]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]


# AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails

### AuthenticationType
- **Type**: typing.Optional[str]

### LambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails]

### OpenIdConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiOpenIdConnectConfigDetails]

### UserPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiUserPoolConfigDetails]


# AwsAppSyncGraphQlApiDetails

### ApiId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OpenIdConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiOpenIdConnectConfigDetails]

### Name
- **Type**: typing.Optional[str]

### LambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails]

### XrayEnabled
- **Type**: typing.Optional[bool]

### Arn
- **Type**: typing.Optional[str]

### UserPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiUserPoolConfigDetails]

### AuthenticationType
- **Type**: typing.Optional[str]

### LogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLogConfigDetails]

### AdditionalAuthenticationProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails]]

### WafWebAclArn
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiDetailsOutput

### ApiId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OpenIdConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiOpenIdConnectConfigDetails]

### Name
- **Type**: typing.Optional[str]

### LambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails]

### XrayEnabled
- **Type**: typing.Optional[bool]

### Arn
- **Type**: typing.Optional[str]

### UserPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiUserPoolConfigDetails]

### AuthenticationType
- **Type**: typing.Optional[str]

### LogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLogConfigDetails]

### AdditionalAuthenticationProviders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails]]

### WafWebAclArn
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails

### AuthorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### AuthorizerUri
- **Type**: typing.Optional[str]

### IdentityValidationExpression
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiLogConfigDetails

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### ExcludeVerboseContent
- **Type**: typing.Optional[bool]

### FieldLogLevel
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiOpenIdConnectConfigDetails

### AuthTtL
- **Type**: typing.Optional[int]

### ClientId
- **Type**: typing.Optional[str]

### IatTtL
- **Type**: typing.Optional[int]

### Issuer
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiUserPoolConfigDetails

### AppIdClientRegex
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### DefaultAction
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]


# AwsAthenaWorkGroupConfigurationDetails

### ResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupConfigurationResultConfigurationDetails]


# AwsAthenaWorkGroupConfigurationResultConfigurationDetails

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails]


# AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAthenaWorkGroupDetails

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupConfigurationDetails]


# AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails

### Value
- **Type**: typing.Optional[str]


# AwsAutoScalingAutoScalingGroupDetails

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LoadBalancerNames
- **Type**: typing.Optional[typing.Sequence[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[str]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnion]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails]]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification]

### CapacityRebalance
- **Type**: typing.Optional[bool]


# AwsAutoScalingAutoScalingGroupDetailsOutput

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[str]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutput]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails]]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification]

### CapacityRebalance
- **Type**: typing.Optional[bool]


# AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification

### LaunchTemplateId
- **Type**: typing.Optional[str]

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnion]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutput

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutput]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails]]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails

### DeviceName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails]

### NoDevice
- **Type**: typing.Optional[bool]

### VirtualName
- **Type**: typing.Optional[str]


# AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Encrypted
- **Type**: typing.Optional[bool]

### Iops
- **Type**: typing.Optional[int]

### SnapshotId
- **Type**: typing.Optional[str]

### VolumeSize
- **Type**: typing.Optional[int]

### VolumeType
- **Type**: typing.Optional[str]


# AwsAutoScalingLaunchConfigurationDetails

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails]]

### ClassicLinkVpcId
- **Type**: typing.Optional[str]

### ClassicLinkVpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### CreatedTime
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### InstanceMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### PlacementTenancy
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### SpotPrice
- **Type**: typing.Optional[str]

### UserData
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationMetadataOptions]


# AwsAutoScalingLaunchConfigurationDetailsOutput

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails]]

### ClassicLinkVpcId
- **Type**: typing.Optional[str]

### ClassicLinkVpcSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### InstanceMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### PlacementTenancy
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SpotPrice
- **Type**: typing.Optional[str]

### UserData
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationMetadataOptions]


# AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsAutoScalingLaunchConfigurationMetadataOptions

### HttpEndpoint
- **Type**: typing.Optional[str]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### HttpTokens
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanAdvancedBackupSettingsDetails

### BackupOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResourceType
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutput

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceType
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsBackupBackupPlanBackupPlanDetails

### BackupPlanName
- **Type**: typing.Optional[str]

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnion]]

### BackupPlanRule
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleDetailsUnion]]


# AwsBackupBackupPlanBackupPlanDetailsOutput

### BackupPlanName
- **Type**: typing.Optional[str]

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutput]]

### BackupPlanRule
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleDetailsOutput]]


# AwsBackupBackupPlanBackupPlanDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsBackupBackupPlanDetails

### BackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanBackupPlanDetailsUnion]

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanDetailsOutput

### BackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanBackupPlanDetailsOutput]

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanLifecycleDetails

### DeleteAfterDays
- **Type**: typing.Optional[int]

### MoveToColdStorageAfterDays
- **Type**: typing.Optional[int]


# AwsBackupBackupPlanRuleCopyActionsDetails

### DestinationBackupVaultArn
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanLifecycleDetails]


# AwsBackupBackupPlanRuleDetails

### TargetBackupVault
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### ScheduleExpression
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### RuleId
- **Type**: typing.Optional[str]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### CompletionWindowMinutes
- **Type**: typing.Optional[int]

### CopyActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleCopyActionsDetails]]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanLifecycleDetails]


# AwsBackupBackupPlanRuleDetailsOutput

### TargetBackupVault
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### ScheduleExpression
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### RuleId
- **Type**: typing.Optional[str]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### CompletionWindowMinutes
- **Type**: typing.Optional[int]

### CopyActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleCopyActionsDetails]]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanLifecycleDetails]


# AwsBackupBackupPlanRuleDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsBackupBackupVaultDetails

### BackupVaultArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultNotificationsDetailsUnion]

### AccessPolicy
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultDetailsOutput

### BackupVaultArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultNotificationsDetailsOutput]

### AccessPolicy
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultNotificationsDetails

### BackupVaultEvents
- **Type**: typing.Optional[typing.Sequence[str]]

### SnsTopicArn
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultNotificationsDetailsOutput

### BackupVaultEvents
- **Type**: typing.Optional[typing.List[str]]

### SnsTopicArn
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultNotificationsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsBackupRecoveryPointCalculatedLifecycleDetails

### DeleteAt
- **Type**: typing.Optional[str]

### MoveToColdStorageAt
- **Type**: typing.Optional[str]


# AwsBackupRecoveryPointCreatedByDetails

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### BackupPlanVersion
- **Type**: typing.Optional[str]

### BackupRuleId
- **Type**: typing.Optional[str]


# AwsBackupRecoveryPointDetails

### BackupSizeInBytes
- **Type**: typing.Optional[int]

### BackupVaultArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### CalculatedLifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointCalculatedLifecycleDetails]

### CompletionDate
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointCreatedByDetails]

### CreationDate
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]

### IsEncrypted
- **Type**: typing.Optional[bool]

### LastRestoreTime
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointLifecycleDetails]

### RecoveryPointArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### SourceBackupVaultArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[str]


# AwsBackupRecoveryPointLifecycleDetails

### DeleteAfterDays
- **Type**: typing.Optional[int]

### MoveToColdStorageAfterDays
- **Type**: typing.Optional[int]


# AwsCertificateManagerCertificateDomainValidationOption

### DomainName
- **Type**: typing.Optional[str]

### ResourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateResourceRecord]

### ValidationDomain
- **Type**: typing.Optional[str]

### ValidationEmails
- **Type**: typing.Optional[typing.Sequence[str]]

### ValidationMethod
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateDomainValidationOptionOutput

### DomainName
- **Type**: typing.Optional[str]

### ResourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateResourceRecord]

### ValidationDomain
- **Type**: typing.Optional[str]

### ValidationEmails
- **Type**: typing.Optional[typing.List[str]]

### ValidationMethod
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateExtendedKeyUsage

### Name
- **Type**: typing.Optional[str]

### OId
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateKeyUsage

### Name
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateOptions

### CertificateTransparencyLoggingPreference
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateRenewalSummary

### DomainValidationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOption]]

### RenewalStatus
- **Type**: typing.Optional[str]

### RenewalStatusReason
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateRenewalSummaryOutput

### DomainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOptionOutput]]

### RenewalStatus
- **Type**: typing.Optional[str]

### RenewalStatusReason
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateResourceRecord

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFormationStackDetails

### Capabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### CreationTime
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisableRollback
- **Type**: typing.Optional[bool]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDriftInformationDetails]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### LastUpdatedTime
- **Type**: typing.Optional[str]

### NotificationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackOutputsDetails]]

### RoleArn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### StackName
- **Type**: typing.Optional[str]

### StackStatus
- **Type**: typing.Optional[str]

### StackStatusReason
- **Type**: typing.Optional[str]

### TimeoutInMinutes
- **Type**: typing.Optional[int]


# AwsCloudFormationStackDetailsOutput

### Capabilities
- **Type**: typing.Optional[typing.List[str]]

### CreationTime
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisableRollback
- **Type**: typing.Optional[bool]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDriftInformationDetails]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### LastUpdatedTime
- **Type**: typing.Optional[str]

### NotificationArns
- **Type**: typing.Optional[typing.List[str]]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackOutputsDetails]]

### RoleArn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### StackName
- **Type**: typing.Optional[str]

### StackStatus
- **Type**: typing.Optional[str]

### StackStatusReason
- **Type**: typing.Optional[str]

### TimeoutInMinutes
- **Type**: typing.Optional[int]


# AwsCloudFormationStackDriftInformationDetails

### StackDriftStatus
- **Type**: typing.Optional[str]


# AwsCloudFormationStackOutputsDetails

### Description
- **Type**: typing.Optional[str]

### OutputKey
- **Type**: typing.Optional[str]

### OutputValue
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionCacheBehavior

### ViewerProtocolPolicy
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionCacheBehaviors

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehavior]]


# AwsCloudFrontDistributionCacheBehaviorsOutput

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehavior]]


# AwsCloudFrontDistributionCacheBehaviorsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionDefaultCacheBehavior

### ViewerProtocolPolicy
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionDetails

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorsUnion]

### DefaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDefaultCacheBehavior]

### DefaultRootObject
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionLogging]

### Origins
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginsUnion]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupsUnion]

### ViewerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionViewerCertificate]

### Status
- **Type**: typing.Optional[str]

### WebAclId
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionDetailsOutput

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorsOutput]

### DefaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDefaultCacheBehavior]

### DefaultRootObject
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionLogging]

### Origins
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginsOutput]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupsOutput]

### ViewerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionViewerCertificate]

### Status
- **Type**: typing.Optional[str]

### WebAclId
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionLogging

### Bucket
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### IncludeCookies
- **Type**: typing.Optional[bool]

### Prefix
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionOriginCustomOriginConfig

### HttpPort
- **Type**: typing.Optional[int]

### HttpsPort
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]

### OriginProtocolPolicy
- **Type**: typing.Optional[str]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginSslProtocolsUnion]


# AwsCloudFrontDistributionOriginCustomOriginConfigOutput

### HttpPort
- **Type**: typing.Optional[int]

### HttpsPort
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]

### OriginProtocolPolicy
- **Type**: typing.Optional[str]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginSslProtocolsOutput]


# AwsCloudFrontDistributionOriginCustomOriginConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionOriginGroup

### FailoverCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverUnion]


# AwsCloudFrontDistributionOriginGroupFailover

### StatusCodes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnion]


# AwsCloudFrontDistributionOriginGroupFailoverOutput

### StatusCodes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutput]


# AwsCloudFrontDistributionOriginGroupFailoverStatusCodes

### Items
- **Type**: typing.Optional[typing.Sequence[int]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutput

### Items
- **Type**: typing.Optional[typing.List[int]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionOriginGroupFailoverUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionOriginGroupOutput

### FailoverCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverOutput]


# AwsCloudFrontDistributionOriginGroupUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionOriginGroups

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupUnion]]


# AwsCloudFrontDistributionOriginGroupsOutput

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupOutput]]


# AwsCloudFrontDistributionOriginGroupsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionOriginItem

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OriginPath
- **Type**: typing.Optional[str]

### S3OriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginS3OriginConfig]

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginCustomOriginConfigUnion]


# AwsCloudFrontDistributionOriginItemOutput

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OriginPath
- **Type**: typing.Optional[str]

### S3OriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginS3OriginConfig]

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginCustomOriginConfigOutput]


# AwsCloudFrontDistributionOriginItemUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionOriginS3OriginConfig

### OriginAccessIdentity
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionOriginSslProtocols

### Items
- **Type**: typing.Optional[typing.Sequence[str]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginSslProtocolsOutput

### Items
- **Type**: typing.Optional[typing.List[str]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginSslProtocolsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionOrigins

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginItemUnion]]


# AwsCloudFrontDistributionOriginsOutput

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginItemOutput]]


# AwsCloudFrontDistributionOriginsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCloudFrontDistributionViewerCertificate

### AcmCertificateArn
- **Type**: typing.Optional[str]

### Certificate
- **Type**: typing.Optional[str]

### CertificateSource
- **Type**: typing.Optional[str]

### CloudFrontDefaultCertificate
- **Type**: typing.Optional[bool]

### IamCertificateId
- **Type**: typing.Optional[str]

### MinimumProtocolVersion
- **Type**: typing.Optional[str]

### SslSupportMethod
- **Type**: typing.Optional[str]


# AwsCloudTrailTrailDetails

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### HasCustomEventSelectors
- **Type**: typing.Optional[bool]

### HomeRegion
- **Type**: typing.Optional[str]

### IncludeGlobalServiceEvents
- **Type**: typing.Optional[bool]

### IsMultiRegionTrail
- **Type**: typing.Optional[bool]

### IsOrganizationTrail
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### LogFileValidationEnabled
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]

### S3KeyPrefix
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SnsTopicName
- **Type**: typing.Optional[str]

### TrailArn
- **Type**: typing.Optional[str]


# AwsCloudWatchAlarmDetails

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[str]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmName
- **Type**: typing.Optional[str]

### ComparisonOperator
- **Type**: typing.Optional[str]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDimensionsDetails]]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.Sequence[str]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OkActions
- **Type**: typing.Optional[typing.Sequence[str]]

### Period
- **Type**: typing.Optional[int]

### Statistic
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[float]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### TreatMissingData
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# AwsCloudWatchAlarmDetailsOutput

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[str]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmName
- **Type**: typing.Optional[str]

### ComparisonOperator
- **Type**: typing.Optional[str]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDimensionsDetails]]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OkActions
- **Type**: typing.Optional[typing.List[str]]

### Period
- **Type**: typing.Optional[int]

### Statistic
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[float]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### TreatMissingData
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# AwsCloudWatchAlarmDimensionsDetails

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectArtifactsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCodeBuildProjectDetails

### EncryptionKey
- **Type**: typing.Optional[str]

### Artifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetails]]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentUnion]

### Name
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectSource]

### ServiceRole
- **Type**: typing.Optional[str]

### LogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigDetails]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectVpcConfigUnion]

### SecondaryArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetails]]


# AwsCodeBuildProjectDetailsOutput

### EncryptionKey
- **Type**: typing.Optional[str]

### Artifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetails]]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentOutput]

### Name
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectSource]

### ServiceRole
- **Type**: typing.Optional[str]

### LogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigDetails]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectVpcConfigOutput]

### SecondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetails]]


# AwsCodeBuildProjectEnvironmentOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCodeBuildProjectEnvironmentRegistryCredential

### Credential
- **Type**: typing.Optional[str]

### CredentialProvider
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectEnvironmentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails

### GroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectLogsConfigDetails

### CloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails]

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigS3LogsDetails]


# AwsCodeBuildProjectLogsConfigS3LogsDetails

### EncryptionDisabled
- **Type**: typing.Optional[bool]

### Location
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCodeBuildProjectVpcConfig

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsCodeBuildProjectVpcConfigOutput

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# AwsCodeBuildProjectVpcConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCorsConfiguration

### AllowOrigins
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowCredentials
- **Type**: typing.Optional[bool]

### ExposeHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxAge
- **Type**: typing.Optional[int]

### AllowMethods
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowHeaders
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsCorsConfigurationOutput

### AllowOrigins
- **Type**: typing.Optional[typing.List[str]]

### AllowCredentials
- **Type**: typing.Optional[bool]

### ExposeHeaders
- **Type**: typing.Optional[typing.List[str]]

### MaxAge
- **Type**: typing.Optional[int]

### AllowMethods
- **Type**: typing.Optional[typing.List[str]]

### AllowHeaders
- **Type**: typing.Optional[typing.List[str]]


# AwsCorsConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsDmsEndpointDetails

### CertificateArn
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### EndpointArn
- **Type**: typing.Optional[str]

### EndpointIdentifier
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[str]

### EngineName
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]

### ExtraConnectionAttributes
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# AwsDmsReplicationInstanceDetails

### AllocatedStorage
- **Type**: typing.Optional[int]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]

### ReplicationSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceReplicationSubnetGroupDetails]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceVpcSecurityGroupsDetails]]


# AwsDmsReplicationInstanceDetailsOutput

### AllocatedStorage
- **Type**: typing.Optional[int]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]

### ReplicationSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceReplicationSubnetGroupDetails]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceVpcSecurityGroupsDetails]]


# AwsDmsReplicationInstanceReplicationSubnetGroupDetails

### ReplicationSubnetGroupIdentifier
- **Type**: typing.Optional[str]


# AwsDmsReplicationInstanceVpcSecurityGroupsDetails

### VpcSecurityGroupId
- **Type**: typing.Optional[str]


# AwsDmsReplicationTaskDetails

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStartTime
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### MigrationType
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### ReplicationTaskIdentifier
- **Type**: typing.Optional[str]

### ReplicationTaskSettings
- **Type**: typing.Optional[str]

### SourceEndpointArn
- **Type**: typing.Optional[str]

### TableMappings
- **Type**: typing.Optional[str]

### TargetEndpointArn
- **Type**: typing.Optional[str]

### TaskData
- **Type**: typing.Optional[str]


# AwsDynamoDbTableAttributeDefinition

### AttributeName
- **Type**: typing.Optional[str]

### AttributeType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableBillingModeSummary

### BillingMode
- **Type**: typing.Optional[str]

### LastUpdateToPayPerRequestDateTime
- **Type**: typing.Optional[str]


# AwsDynamoDbTableDetails

### AttributeDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableAttributeDefinition]]

### BillingModeSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableBillingModeSummary]

### CreationDateTime
- **Type**: typing.Optional[str]

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableGlobalSecondaryIndexUnion]]

### GlobalTableVersion
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchema]]

### LatestStreamArn
- **Type**: typing.Optional[str]

### LatestStreamLabel
- **Type**: typing.Optional[str]

### LocalSecondaryIndexes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableLocalSecondaryIndexUnion]]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughput]

### Replicas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaUnion]]

### RestoreSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableRestoreSummary]

### SseDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableSseDescription]

### StreamSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableStreamSpecification]

### TableId
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### TableSizeBytes
- **Type**: typing.Optional[int]

### TableStatus
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# AwsDynamoDbTableDetailsOutput

### AttributeDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableAttributeDefinition]]

### BillingModeSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableBillingModeSummary]

### CreationDateTime
- **Type**: typing.Optional[str]

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableGlobalSecondaryIndexOutput]]

### GlobalTableVersion
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchema]]

### LatestStreamArn
- **Type**: typing.Optional[str]

### LatestStreamLabel
- **Type**: typing.Optional[str]

### LocalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableLocalSecondaryIndexOutput]]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughput]

### Replicas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaOutput]]

### RestoreSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableRestoreSummary]

### SseDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableSseDescription]

### StreamSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableStreamSpecification]

### TableId
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### TableSizeBytes
- **Type**: typing.Optional[int]

### TableStatus
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# AwsDynamoDbTableGlobalSecondaryIndex

### Backfilling
- **Type**: typing.Optional[bool]

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### IndexSizeBytes
- **Type**: typing.Optional[int]

### IndexStatus
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchema]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionUnion]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughput]


# AwsDynamoDbTableGlobalSecondaryIndexOutput

### Backfilling
- **Type**: typing.Optional[bool]

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### IndexSizeBytes
- **Type**: typing.Optional[int]

### IndexStatus
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchema]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionOutput]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughput]


# AwsDynamoDbTableGlobalSecondaryIndexUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsDynamoDbTableKeySchema

### AttributeName
- **Type**: typing.Optional[str]

### KeyType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableLocalSecondaryIndex

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### KeySchema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchema]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionUnion]


# AwsDynamoDbTableLocalSecondaryIndexOutput

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchema]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionOutput]


# AwsDynamoDbTableLocalSecondaryIndexUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsDynamoDbTableProjection

### NonKeyAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### ProjectionType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableProjectionOutput

### NonKeyAttributes
- **Type**: typing.Optional[typing.List[str]]

### ProjectionType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableProjectionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsDynamoDbTableProvisionedThroughput

### LastDecreaseDateTime
- **Type**: typing.Optional[str]

### LastIncreaseDateTime
- **Type**: typing.Optional[str]

### NumberOfDecreasesToday
- **Type**: typing.Optional[int]

### ReadCapacityUnits
- **Type**: typing.Optional[int]

### WriteCapacityUnits
- **Type**: typing.Optional[int]


# AwsDynamoDbTableProvisionedThroughputOverride

### ReadCapacityUnits
- **Type**: typing.Optional[int]


# AwsDynamoDbTableReplicaGlobalSecondaryIndex

### IndexName
- **Type**: typing.Optional[str]

### ProvisionedThroughputOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputOverride]


# AwsDynamoDbTableReplicaOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsDynamoDbTableReplicaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsDynamoDbTableRestoreSummary

### SourceBackupArn
- **Type**: typing.Optional[str]

### SourceTableArn
- **Type**: typing.Optional[str]

### RestoreDateTime
- **Type**: typing.Optional[str]

### RestoreInProgress
- **Type**: typing.Optional[bool]


# AwsDynamoDbTableSseDescription

### InaccessibleEncryptionDateTime
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SseType
- **Type**: typing.Optional[str]

### KmsMasterKeyArn
- **Type**: typing.Optional[str]


# AwsDynamoDbTableStreamSpecification

### StreamEnabled
- **Type**: typing.Optional[bool]

### StreamViewType
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails

### DirectoryId
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointAuthenticationOptionsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails

### SamlProviderArn
- **Type**: typing.Optional[str]

### SelfServiceSamlProviderArn
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails

### ClientRootCertificateChain
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointClientConnectOptionsDetails

### Enabled
- **Type**: typing.Optional[bool]

### LambdaFunctionArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails]


# AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails

### Enabled
- **Type**: typing.Optional[bool]

### BannerText
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointConnectionLogOptionsDetails

### Enabled
- **Type**: typing.Optional[bool]

### CloudwatchLogGroup
- **Type**: typing.Optional[str]

### CloudwatchLogStream
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointDetails

### ClientVpnEndpointId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientCidrBlock
- **Type**: typing.Optional[str]

### DnsServer
- **Type**: typing.Optional[typing.Sequence[str]]

### SplitTunnel
- **Type**: typing.Optional[bool]

### TransportProtocol
- **Type**: typing.Optional[str]

### VpnPort
- **Type**: typing.Optional[int]

### ServerCertificateArn
- **Type**: typing.Optional[str]

### AuthenticationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsDetails]]

### ConnectionLogOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointConnectionLogOptionsDetails]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcId
- **Type**: typing.Optional[str]

### SelfServicePortalUrl
- **Type**: typing.Optional[str]

### ClientConnectOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientConnectOptionsDetails]

### SessionTimeoutHours
- **Type**: typing.Optional[int]

### ClientLoginBannerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails]


# AwsEc2ClientVpnEndpointDetailsOutput

### ClientVpnEndpointId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientCidrBlock
- **Type**: typing.Optional[str]

### DnsServer
- **Type**: typing.Optional[typing.List[str]]

### SplitTunnel
- **Type**: typing.Optional[bool]

### TransportProtocol
- **Type**: typing.Optional[str]

### VpnPort
- **Type**: typing.Optional[int]

### ServerCertificateArn
- **Type**: typing.Optional[str]

### AuthenticationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsDetails]]

### ConnectionLogOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointConnectionLogOptionsDetails]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]

### SelfServicePortalUrl
- **Type**: typing.Optional[str]

### ClientConnectOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientConnectOptionsDetails]

### SessionTimeoutHours
- **Type**: typing.Optional[int]

### ClientLoginBannerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails]


# AwsEc2EipDetails

### InstanceId
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]

### AllocationId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### PublicIpv4Pool
- **Type**: typing.Optional[str]

### NetworkBorderGroup
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NetworkInterfaceOwnerId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]


# AwsEc2InstanceMetadataOptions

### HttpEndpoint
- **Type**: typing.Optional[str]

### HttpProtocolIpv6
- **Type**: typing.Optional[str]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### HttpTokens
- **Type**: typing.Optional[str]

### InstanceMetadataTags
- **Type**: typing.Optional[str]


# AwsEc2InstanceMonitoringDetails

### State
- **Type**: typing.Optional[str]


# AwsEc2InstanceNetworkInterfacesDetails

### NetworkInterfaceId
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails

### DeviceName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails]

### NoDevice
- **Type**: typing.Optional[str]

### VirtualName
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Encrypted
- **Type**: typing.Optional[bool]

### Iops
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### SnapshotId
- **Type**: typing.Optional[str]

### Throughput
- **Type**: typing.Optional[int]

### VolumeSize
- **Type**: typing.Optional[int]

### VolumeType
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails

### CapacityReservationPreference
- **Type**: typing.Optional[str]

### CapacityReservationTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails]


# AwsEc2LaunchTemplateDataCpuOptionsDetails

### CoreCount
- **Type**: typing.Optional[int]

### ThreadsPerCore
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataCreditSpecificationDetails

### CpuCredits
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataDetails

### BlockDeviceMappingSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails]]

### CapacityReservationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails]

### CpuOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCpuOptionsDetails]

### CreditSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCreditSpecificationDetails]

### DisableApiStop
- **Type**: typing.Optional[bool]

### DisableApiTermination
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ElasticGpuSpecificationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails]]

### ElasticInferenceAcceleratorSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails]]

### EnclaveOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataEnclaveOptionsDetails]

### HibernationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataHibernationOptionsDetails]

### IamInstanceProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataIamInstanceProfileDetails]

### ImageId
- **Type**: typing.Optional[str]

### InstanceInitiatedShutdownBehavior
- **Type**: typing.Optional[str]

### InstanceMarketOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnion]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LicenseSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataLicenseSetDetails]]

### MaintenanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMaintenanceOptionsDetails]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMetadataOptionsDetails]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMonitoringDetails]

### NetworkInterfaceSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnion]]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPlacementDetails]

### PrivateDnsNameOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails]

### RamDiskId
- **Type**: typing.Optional[str]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupSet
- **Type**: typing.Optional[typing.Sequence[str]]

### UserData
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataDetailsOutput

### BlockDeviceMappingSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails]]

### CapacityReservationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails]

### CpuOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCpuOptionsDetails]

### CreditSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCreditSpecificationDetails]

### DisableApiStop
- **Type**: typing.Optional[bool]

### DisableApiTermination
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ElasticGpuSpecificationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails]]

### ElasticInferenceAcceleratorSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails]]

### EnclaveOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataEnclaveOptionsDetails]

### HibernationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataHibernationOptionsDetails]

### IamInstanceProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataIamInstanceProfileDetails]

### ImageId
- **Type**: typing.Optional[str]

### InstanceInitiatedShutdownBehavior
- **Type**: typing.Optional[str]

### InstanceMarketOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutput]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LicenseSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataLicenseSetDetails]]

### MaintenanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMaintenanceOptionsDetails]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMetadataOptionsDetails]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMonitoringDetails]

### NetworkInterfaceSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutput]]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPlacementDetails]

### PrivateDnsNameOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails]

### RamDiskId
- **Type**: typing.Optional[str]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupSet
- **Type**: typing.Optional[typing.List[str]]

### UserData
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2LaunchTemplateDataEnclaveOptionsDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsEc2LaunchTemplateDataHibernationOptionsDetails

### Configured
- **Type**: typing.Optional[bool]


# AwsEc2LaunchTemplateDataIamInstanceProfileDetails

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails

### MarketType
- **Type**: typing.Optional[str]

### SpotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails]


# AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails

### BlockDurationMinutes
- **Type**: typing.Optional[int]

### InstanceInterruptionBehavior
- **Type**: typing.Optional[str]

### MaxPrice
- **Type**: typing.Optional[str]

### SpotInstanceType
- **Type**: typing.Optional[str]

### ValidUntil
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsDetails

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.Sequence[str]]

### AcceleratorNames
- **Type**: typing.Optional[typing.Sequence[str]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails]

### AcceleratorTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### BareMetal
- **Type**: typing.Optional[str]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails]

### BurstablePerformance
- **Type**: typing.Optional[str]

### CpuManufacturers
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.Sequence[str]]

### LocalStorage
- **Type**: typing.Optional[str]

### LocalStorageTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails]

### MemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails]

### VCpuCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails]


# AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutput

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.List[str]]

### AcceleratorNames
- **Type**: typing.Optional[typing.List[str]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[str]]

### BareMetal
- **Type**: typing.Optional[str]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails]

### BurstablePerformance
- **Type**: typing.Optional[str]

### CpuManufacturers
- **Type**: typing.Optional[typing.List[str]]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.List[str]]

### LocalStorage
- **Type**: typing.Optional[str]

### LocalStorageTypes
- **Type**: typing.Optional[typing.List[str]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails]

### MemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails]

### VCpuCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails]


# AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails

### Max
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]


# AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails

### Max
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]


# AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataLicenseSetDetails

### LicenseConfigurationArn
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataMaintenanceOptionsDetails

### AutoRecovery
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataMetadataOptionsDetails

### HttpEndpoint
- **Type**: typing.Optional[str]

### HttpProtocolIpv6
- **Type**: typing.Optional[str]

### HttpTokens
- **Type**: typing.Optional[str]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### InstanceMetadataTags
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataMonitoringDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails

### AssociateCarrierIpAddress
- **Type**: typing.Optional[bool]

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DeviceIndex
- **Type**: typing.Optional[int]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### InterfaceType
- **Type**: typing.Optional[str]

### Ipv4PrefixCount
- **Type**: typing.Optional[int]

### Ipv4Prefixes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails]]

### Ipv6AddressCount
- **Type**: typing.Optional[int]

### Ipv6Addresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails]]

### Ipv6PrefixCount
- **Type**: typing.Optional[int]

### Ipv6Prefixes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails]]

### NetworkCardIndex
- **Type**: typing.Optional[int]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails]]

### SecondaryPrivateIpAddressCount
- **Type**: typing.Optional[int]

### SubnetId
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutput

### AssociateCarrierIpAddress
- **Type**: typing.Optional[bool]

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DeviceIndex
- **Type**: typing.Optional[int]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### InterfaceType
- **Type**: typing.Optional[str]

### Ipv4PrefixCount
- **Type**: typing.Optional[int]

### Ipv4Prefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails]]

### Ipv6AddressCount
- **Type**: typing.Optional[int]

### Ipv6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails]]

### Ipv6PrefixCount
- **Type**: typing.Optional[int]

### Ipv6Prefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails]]

### NetworkCardIndex
- **Type**: typing.Optional[int]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails]]

### SecondaryPrivateIpAddressCount
- **Type**: typing.Optional[int]

### SubnetId
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails

### Ipv4Prefix
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails

### Ipv6Address
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails

### Ipv6Prefix
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails

### Primary
- **Type**: typing.Optional[bool]

### PrivateIpAddress
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataPlacementDetails

### Affinity
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### HostId
- **Type**: typing.Optional[str]

### HostResourceGroupArn
- **Type**: typing.Optional[str]

### PartitionNumber
- **Type**: typing.Optional[int]

### SpreadDomain
- **Type**: typing.Optional[str]

### Tenancy
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails

### EnableResourceNameDnsAAAARecord
- **Type**: typing.Optional[bool]

### EnableResourceNameDnsARecord
- **Type**: typing.Optional[bool]

### HostnameType
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDetails

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LaunchTemplateData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataDetailsUnion]

### DefaultVersionNumber
- **Type**: typing.Optional[int]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDetailsOutput

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LaunchTemplateData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataDetailsOutput]

### DefaultVersionNumber
- **Type**: typing.Optional[int]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# AwsEc2NetworkAclAssociation

### NetworkAclAssociationId
- **Type**: typing.Optional[str]

### NetworkAclId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]


# AwsEc2NetworkAclDetails

### IsDefault
- **Type**: typing.Optional[bool]

### NetworkAclId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Associations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclAssociation]]

### Entries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclEntry]]


# AwsEc2NetworkAclDetailsOutput

### IsDefault
- **Type**: typing.Optional[bool]

### NetworkAclId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclAssociation]]

### Entries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclEntry]]


# AwsEc2NetworkAclEntry

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2NetworkInterfaceAttachment

### AttachTime
- **Type**: typing.Optional[str]

### AttachmentId
- **Type**: typing.Optional[str]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### DeviceIndex
- **Type**: typing.Optional[int]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceOwnerId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceDetails

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceAttachment]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceSecurityGroup]]

### SourceDestCheck
- **Type**: typing.Optional[bool]

### IpV6Addresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceIpV6AddressDetail]]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfacePrivateIpAddressDetail]]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceDetailsOutput

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceAttachment]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceSecurityGroup]]

### SourceDestCheck
- **Type**: typing.Optional[bool]

### IpV6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceIpV6AddressDetail]]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfacePrivateIpAddressDetail]]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceIpV6AddressDetail

### IpV6Address
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfacePrivateIpAddressDetail

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateDnsName
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceSecurityGroup

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]


# AwsEc2RouteTableDetails

### AssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AssociationSetDetails]]

### OwnerId
- **Type**: typing.Optional[str]

### PropagatingVgwSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.PropagatingVgwSetDetails]]

### RouteTableId
- **Type**: typing.Optional[str]

### RouteSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RouteSetDetails]]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2RouteTableDetailsOutput

### AssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AssociationSetDetails]]

### OwnerId
- **Type**: typing.Optional[str]

### PropagatingVgwSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PropagatingVgwSetDetails]]

### RouteTableId
- **Type**: typing.Optional[str]

### RouteSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RouteSetDetails]]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupDetails

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### IpPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionUnion]]

### IpPermissionsEgress
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermission]]


# AwsEc2SecurityGroupDetailsOutput

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### IpPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionOutput]]

### IpPermissionsEgress
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionOutput]]


# AwsEc2SecurityGroupIpPermission

### IpProtocol
- **Type**: typing.Optional[str]

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]

### UserIdGroupPairs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupUserIdGroupPair]]

### IpRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpRange]]

### Ipv6Ranges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpv6Range]]

### PrefixListIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupPrefixListId]]


# AwsEc2SecurityGroupIpPermissionOutput

### IpProtocol
- **Type**: typing.Optional[str]

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]

### UserIdGroupPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupUserIdGroupPair]]

### IpRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpRange]]

### Ipv6Ranges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpv6Range]]

### PrefixListIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupPrefixListId]]


# AwsEc2SecurityGroupIpPermissionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2SecurityGroupIpRange

### CidrIp
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupIpv6Range

### CidrIpv6
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupPrefixListId

### PrefixListId
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupUserIdGroupPair

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### PeeringStatus
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# AwsEc2SubnetDetails

### AssignIpv6AddressOnCreation
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### AvailableIpAddressCount
- **Type**: typing.Optional[int]

### CidrBlock
- **Type**: typing.Optional[str]

### DefaultForAz
- **Type**: typing.Optional[bool]

### MapPublicIpOnLaunch
- **Type**: typing.Optional[bool]

### OwnerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociation]]


# AwsEc2SubnetDetailsOutput

### AssignIpv6AddressOnCreation
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### AvailableIpAddressCount
- **Type**: typing.Optional[int]

### CidrBlock
- **Type**: typing.Optional[str]

### DefaultForAz
- **Type**: typing.Optional[bool]

### MapPublicIpOnLaunch
- **Type**: typing.Optional[bool]

### OwnerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociation]]


# AwsEc2TransitGatewayDetails

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteTablePropagation
- **Type**: typing.Optional[str]

### AutoAcceptSharedAttachments
- **Type**: typing.Optional[str]

### DefaultRouteTableAssociation
- **Type**: typing.Optional[str]

### TransitGatewayCidrBlocks
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationDefaultRouteTableId
- **Type**: typing.Optional[str]

### PropagationDefaultRouteTableId
- **Type**: typing.Optional[str]

### VpnEcmpSupport
- **Type**: typing.Optional[str]

### DnsSupport
- **Type**: typing.Optional[str]

### MulticastSupport
- **Type**: typing.Optional[str]

### AmazonSideAsn
- **Type**: typing.Optional[int]


# AwsEc2TransitGatewayDetailsOutput

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteTablePropagation
- **Type**: typing.Optional[str]

### AutoAcceptSharedAttachments
- **Type**: typing.Optional[str]

### DefaultRouteTableAssociation
- **Type**: typing.Optional[str]

### TransitGatewayCidrBlocks
- **Type**: typing.Optional[typing.List[str]]

### AssociationDefaultRouteTableId
- **Type**: typing.Optional[str]

### PropagationDefaultRouteTableId
- **Type**: typing.Optional[str]

### VpnEcmpSupport
- **Type**: typing.Optional[str]

### DnsSupport
- **Type**: typing.Optional[str]

### MulticastSupport
- **Type**: typing.Optional[str]

### AmazonSideAsn
- **Type**: typing.Optional[int]


# AwsEc2VolumeAttachment

### AttachTime
- **Type**: typing.Optional[str]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### InstanceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsEc2VolumeDetails

### CreateTime
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Size
- **Type**: typing.Optional[int]

### SnapshotId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeAttachment]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeScanStatus
- **Type**: typing.Optional[str]


# AwsEc2VolumeDetailsOutput

### CreateTime
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Size
- **Type**: typing.Optional[int]

### SnapshotId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeAttachment]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeScanStatus
- **Type**: typing.Optional[str]


# AwsEc2VpcDetails

### CidrBlockAssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.CidrBlockAssociation]]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociation]]

### DhcpOptionsId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# AwsEc2VpcDetailsOutput

### CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CidrBlockAssociation]]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociation]]

### DhcpOptionsId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# AwsEc2VpcEndpointServiceServiceTypeDetails

### ServiceType
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionDetails

### AccepterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion]

### ExpirationTime
- **Type**: typing.Optional[str]

### RequesterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionStatusDetails]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionDetailsOutput

### AccepterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput]

### ExpirationTime
- **Type**: typing.Optional[str]

### RequesterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionStatusDetails]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionStatusDetails

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionVpcInfoDetails

### CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoCidrBlockSetDetails]]

### Ipv6CidrBlockSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoIpv6CidrBlockSetDetails]]

### OwnerId
- **Type**: typing.Optional[str]

### PeeringOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoPeeringOptionsDetails]

### Region
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput

### CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoCidrBlockSetDetails]]

### Ipv6CidrBlockSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoIpv6CidrBlockSetDetails]]

### OwnerId
- **Type**: typing.Optional[str]

### PeeringOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoPeeringOptionsDetails]

### Region
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2VpnConnectionOptionsDetails

### StaticRoutesOnly
- **Type**: typing.Optional[bool]

### TunnelOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnion]]


# AwsEc2VpnConnectionOptionsDetailsOutput

### StaticRoutesOnly
- **Type**: typing.Optional[bool]

### TunnelOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutput]]


# AwsEc2VpnConnectionOptionsTunnelOptionsDetails

### DpdTimeoutSeconds
- **Type**: typing.Optional[int]

### IkeVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### OutsideIpAddress
- **Type**: typing.Optional[str]

### Phase1DhGroupNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Phase1EncryptionAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase1IntegrityAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase1LifetimeSeconds
- **Type**: typing.Optional[int]

### Phase2DhGroupNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Phase2EncryptionAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase2IntegrityAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase2LifetimeSeconds
- **Type**: typing.Optional[int]

### PreSharedKey
- **Type**: typing.Optional[str]

### RekeyFuzzPercentage
- **Type**: typing.Optional[int]

### RekeyMarginTimeSeconds
- **Type**: typing.Optional[int]

### ReplayWindowSize
- **Type**: typing.Optional[int]

### TunnelInsideCidr
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutput

### DpdTimeoutSeconds
- **Type**: typing.Optional[int]

### IkeVersions
- **Type**: typing.Optional[typing.List[str]]

### OutsideIpAddress
- **Type**: typing.Optional[str]

### Phase1DhGroupNumbers
- **Type**: typing.Optional[typing.List[int]]

### Phase1EncryptionAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase1IntegrityAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase1LifetimeSeconds
- **Type**: typing.Optional[int]

### Phase2DhGroupNumbers
- **Type**: typing.Optional[typing.List[int]]

### Phase2EncryptionAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase2IntegrityAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase2LifetimeSeconds
- **Type**: typing.Optional[int]

### PreSharedKey
- **Type**: typing.Optional[str]

### RekeyFuzzPercentage
- **Type**: typing.Optional[int]

### RekeyMarginTimeSeconds
- **Type**: typing.Optional[int]

### ReplayWindowSize
- **Type**: typing.Optional[int]

### TunnelInsideCidr
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2VpnConnectionRoutesDetails

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionVgwTelemetryDetails

### AcceptedRouteCount
- **Type**: typing.Optional[int]

### CertificateArn
- **Type**: typing.Optional[str]

### LastStatusChange
- **Type**: typing.Optional[str]

### OutsideIpAddress
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# AwsEcrContainerImageDetails

### RegistryId
- **Type**: typing.Optional[str]

### RepositoryName
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ImageTags
- **Type**: typing.Optional[typing.Sequence[str]]

### ImagePublishedAt
- **Type**: typing.Optional[str]


# AwsEcrContainerImageDetailsOutput

### RegistryId
- **Type**: typing.Optional[str]

### RepositoryName
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ImageTags
- **Type**: typing.Optional[typing.List[str]]

### ImagePublishedAt
- **Type**: typing.Optional[str]


# AwsEcrRepositoryDetails

### Arn
- **Type**: typing.Optional[str]

### ImageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrRepositoryImageScanningConfigurationDetails]

### ImageTagMutability
- **Type**: typing.Optional[str]

### LifecyclePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrRepositoryLifecyclePolicyDetails]

### RepositoryName
- **Type**: typing.Optional[str]

### RepositoryPolicyText
- **Type**: typing.Optional[str]


# AwsEcrRepositoryImageScanningConfigurationDetails

### ScanOnPush
- **Type**: typing.Optional[bool]


# AwsEcrRepositoryLifecyclePolicyDetails

### LifecyclePolicyText
- **Type**: typing.Optional[str]

### RegistryId
- **Type**: typing.Optional[str]


# AwsEcsClusterClusterSettingsDetails

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsClusterConfigurationDetails

### ExecuteCommandConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationExecuteCommandConfigurationDetails]


# AwsEcsClusterConfigurationExecuteCommandConfigurationDetails

### KmsKeyId
- **Type**: typing.Optional[str]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails]

### Logging
- **Type**: typing.Optional[str]


# AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsClusterDefaultCapacityProviderStrategyDetails

### Base
- **Type**: typing.Optional[int]

### CapacityProvider
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]


# AwsEcsClusterDetails

### ClusterArn
- **Type**: typing.Optional[str]

### ActiveServicesCount
- **Type**: typing.Optional[int]

### CapacityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### ClusterSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterClusterSettingsDetails]]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationDetails]

### DefaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDefaultCapacityProviderStrategyDetails]]

### ClusterName
- **Type**: typing.Optional[str]

### RegisteredContainerInstancesCount
- **Type**: typing.Optional[int]

### RunningTasksCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]


# AwsEcsClusterDetailsOutput

### ClusterArn
- **Type**: typing.Optional[str]

### ActiveServicesCount
- **Type**: typing.Optional[int]

### CapacityProviders
- **Type**: typing.Optional[typing.List[str]]

### ClusterSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterClusterSettingsDetails]]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationDetails]

### DefaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDefaultCapacityProviderStrategyDetails]]

### ClusterName
- **Type**: typing.Optional[str]

### RegisteredContainerInstancesCount
- **Type**: typing.Optional[int]

### RunningTasksCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]


# AwsEcsContainerDetails

### Name
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### MountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsMountPoint]]

### Privileged
- **Type**: typing.Optional[bool]


# AwsEcsContainerDetailsOutput

### Name
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsMountPoint]]

### Privileged
- **Type**: typing.Optional[bool]


# AwsEcsContainerDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsServiceCapacityProviderStrategyDetails

### Base
- **Type**: typing.Optional[int]

### CapacityProvider
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]


# AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails

### Enable
- **Type**: typing.Optional[bool]

### Rollback
- **Type**: typing.Optional[bool]


# AwsEcsServiceDeploymentConfigurationDetails

### DeploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails]

### MaximumPercent
- **Type**: typing.Optional[int]

### MinimumHealthyPercent
- **Type**: typing.Optional[int]


# AwsEcsServiceLoadBalancersDetails

### ContainerName
- **Type**: typing.Optional[str]

### ContainerPort
- **Type**: typing.Optional[int]

### LoadBalancerName
- **Type**: typing.Optional[str]

### TargetGroupArn
- **Type**: typing.Optional[str]


# AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails

### AssignPublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutput

### AssignPublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Subnets
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsServiceNetworkConfigurationDetails

### AwsVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnion]


# AwsEcsServiceNetworkConfigurationDetailsOutput

### AwsVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutput]


# AwsEcsServiceServiceRegistriesDetails

### ContainerName
- **Type**: typing.Optional[str]

### ContainerPort
- **Type**: typing.Optional[int]

### Port
- **Type**: typing.Optional[int]

### RegistryArn
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails

### Condition
- **Type**: typing.Optional[str]

### ContainerName
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDetails

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### Cpu
- **Type**: typing.Optional[int]

### DependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails]]

### DisableNetworking
- **Type**: typing.Optional[bool]

### DnsSearchDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### DnsServers
- **Type**: typing.Optional[typing.Sequence[str]]

### DockerLabels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DockerSecurityOptions
- **Type**: typing.Optional[typing.Sequence[str]]

### EntryPoint
- **Type**: typing.Optional[typing.Sequence[str]]

### Environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails]]

### Essential
- **Type**: typing.Optional[bool]

### ExtraHosts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails]]

### FirelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnion]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnion]

### Hostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### Interactive
- **Type**: typing.Optional[bool]

### Links
- **Type**: typing.Optional[typing.Sequence[str]]

### LinuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnion]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnion]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### MountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails]]

### Name
- **Type**: typing.Optional[str]

### PortMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails]]

### Privileged
- **Type**: typing.Optional[bool]

### PseudoTerminal
- **Type**: typing.Optional[bool]

### ReadonlyRootFilesystem
- **Type**: typing.Optional[bool]

### RepositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails]

### ResourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails]]

### Secrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails]]

### StartTimeout
- **Type**: typing.Optional[int]

### StopTimeout
- **Type**: typing.Optional[int]

### SystemControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails]]

### Ulimits
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails]]

### User
- **Type**: typing.Optional[str]

### VolumesFrom
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDetailsOutput

### Command
- **Type**: typing.Optional[typing.List[str]]

### Cpu
- **Type**: typing.Optional[int]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails]]

### DisableNetworking
- **Type**: typing.Optional[bool]

### DnsSearchDomains
- **Type**: typing.Optional[typing.List[str]]

### DnsServers
- **Type**: typing.Optional[typing.List[str]]

### DockerLabels
- **Type**: typing.Optional[typing.Dict[str, str]]

### DockerSecurityOptions
- **Type**: typing.Optional[typing.List[str]]

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails]]

### Essential
- **Type**: typing.Optional[bool]

### ExtraHosts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails]]

### FirelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutput]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutput]

### Hostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### Interactive
- **Type**: typing.Optional[bool]

### Links
- **Type**: typing.Optional[typing.List[str]]

### LinuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutput]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutput]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails]]

### Name
- **Type**: typing.Optional[str]

### PortMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails]]

### Privileged
- **Type**: typing.Optional[bool]

### PseudoTerminal
- **Type**: typing.Optional[bool]

### ReadonlyRootFilesystem
- **Type**: typing.Optional[bool]

### RepositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails]]

### Secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails]]

### StartTimeout
- **Type**: typing.Optional[int]

### StopTimeout
- **Type**: typing.Optional[int]

### SystemControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails]]

### Ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails]]

### User
- **Type**: typing.Optional[str]

### VolumesFrom
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails

### Hostname
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### Interval
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutput

### Command
- **Type**: typing.Optional[typing.List[str]]

### Interval
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails

### Add
- **Type**: typing.Optional[typing.Sequence[str]]

### Drop
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnion]

### Devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnion]]

### InitProcessEnabled
- **Type**: typing.Optional[bool]

### MaxSwap
- **Type**: typing.Optional[int]

### SharedMemorySize
- **Type**: typing.Optional[int]

### Swappiness
- **Type**: typing.Optional[int]

### Tmpfs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnion]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutput

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutput]

### Devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutput]]

### InitProcessEnabled
- **Type**: typing.Optional[bool]

### MaxSwap
- **Type**: typing.Optional[int]

### SharedMemorySize
- **Type**: typing.Optional[int]

### Swappiness
- **Type**: typing.Optional[int]

### Tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutput]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails

### ContainerPath
- **Type**: typing.Optional[str]

### HostPath
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutput

### ContainerPath
- **Type**: typing.Optional[str]

### HostPath
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails

### ContainerPath
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[typing.Sequence[str]]

### Size
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutput

### ContainerPath
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[typing.List[str]]

### Size
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails

### LogDriver
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SecretOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails]]


# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutput

### LogDriver
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.Dict[str, str]]

### SecretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails]]


# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails

### CredentialsParameter
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails

### Name
- **Type**: typing.Optional[str]

### ValueFrom
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails

### Namespace
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails

### HardLimit
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### SoftLimit
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionDetails

### ContainerDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDetailsUnion]]

### Cpu
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Family
- **Type**: typing.Optional[str]

### InferenceAccelerators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionInferenceAcceleratorsDetails]]

### IpcMode
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### NetworkMode
- **Type**: typing.Optional[str]

### PidMode
- **Type**: typing.Optional[str]

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionPlacementConstraintsDetails]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationDetailsUnion]

### RequiresCompatibilities
- **Type**: typing.Optional[typing.Sequence[str]]

### TaskRoleArn
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDetailsUnion]]

### Status
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionDetailsOutput

### ContainerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDetailsOutput]]

### Cpu
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Family
- **Type**: typing.Optional[str]

### InferenceAccelerators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionInferenceAcceleratorsDetails]]

### IpcMode
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### NetworkMode
- **Type**: typing.Optional[str]

### PidMode
- **Type**: typing.Optional[str]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionPlacementConstraintsDetails]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationDetailsOutput]

### RequiresCompatibilities
- **Type**: typing.Optional[typing.List[str]]

### TaskRoleArn
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDetailsOutput]]

### Status
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionInferenceAcceleratorsDetails

### DeviceName
- **Type**: typing.Optional[str]

### DeviceType
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionPlacementConstraintsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionProxyConfigurationDetailsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionProxyConfigurationDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDetails

### DockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnion]

### EfsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails]

### Host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesHostDetails]

### Name
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDetailsOutput

### DockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutput]

### EfsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails]

### Host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesHostDetails]

### Name
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails

### Autoprovision
- **Type**: typing.Optional[bool]

### Driver
- **Type**: typing.Optional[str]

### DriverOpts
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Labels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Scope
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutput

### Autoprovision
- **Type**: typing.Optional[bool]

### Driver
- **Type**: typing.Optional[str]

### DriverOpts
- **Type**: typing.Optional[typing.Dict[str, str]]

### Labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### Scope
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails

### AccessPointId
- **Type**: typing.Optional[str]

### Iam
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails

### AuthorizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails]

### FilesystemId
- **Type**: typing.Optional[str]

### RootDirectory
- **Type**: typing.Optional[str]

### TransitEncryption
- **Type**: typing.Optional[str]

### TransitEncryptionPort
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionVolumesHostDetails

### SourcePath
- **Type**: typing.Optional[str]


# AwsEcsTaskDetails

### ClusterArn
- **Type**: typing.Optional[str]

### TaskDefinitionArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### StartedAt
- **Type**: typing.Optional[str]

### StartedBy
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskVolumeDetails]]

### Containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsUnion]]


# AwsEcsTaskDetailsOutput

### ClusterArn
- **Type**: typing.Optional[str]

### TaskDefinitionArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### StartedAt
- **Type**: typing.Optional[str]

### StartedBy
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskVolumeDetails]]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsOutput]]


# AwsEcsTaskVolumeDetails

### Name
- **Type**: typing.Optional[str]

### Host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskVolumeHostDetails]


# AwsEcsTaskVolumeHostDetails

### SourcePath
- **Type**: typing.Optional[str]


# AwsEfsAccessPointDetails

### AccessPointId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointPosixUserDetailsUnion]

### RootDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointRootDirectoryDetails]


# AwsEfsAccessPointDetailsOutput

### AccessPointId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointPosixUserDetailsOutput]

### RootDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointRootDirectoryDetails]


# AwsEfsAccessPointPosixUserDetails

### Gid
- **Type**: typing.Optional[str]

### SecondaryGids
- **Type**: typing.Optional[typing.Sequence[str]]

### Uid
- **Type**: typing.Optional[str]


# AwsEfsAccessPointPosixUserDetailsOutput

### Gid
- **Type**: typing.Optional[str]

### SecondaryGids
- **Type**: typing.Optional[typing.List[str]]

### Uid
- **Type**: typing.Optional[str]


# AwsEfsAccessPointPosixUserDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEfsAccessPointRootDirectoryCreationInfoDetails

### OwnerGid
- **Type**: typing.Optional[str]

### OwnerUid
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[str]


# AwsEfsAccessPointRootDirectoryDetails

### CreationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointRootDirectoryCreationInfoDetails]

### Path
- **Type**: typing.Optional[str]


# AwsEksClusterDetails

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityData
- **Type**: typing.Optional[str]

### ClusterStatus
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ResourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterResourcesVpcConfigDetailsUnion]

### RoleArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingDetailsUnion]


# AwsEksClusterDetailsOutput

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityData
- **Type**: typing.Optional[str]

### ClusterStatus
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ResourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterResourcesVpcConfigDetailsOutput]

### RoleArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingDetailsOutput]


# AwsEksClusterLoggingClusterLoggingDetails

### Enabled
- **Type**: typing.Optional[bool]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEksClusterLoggingClusterLoggingDetailsOutput

### Enabled
- **Type**: typing.Optional[bool]

### Types
- **Type**: typing.Optional[typing.List[str]]


# AwsEksClusterLoggingClusterLoggingDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEksClusterLoggingDetails

### ClusterLogging
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingClusterLoggingDetailsUnion]]


# AwsEksClusterLoggingDetailsOutput

### ClusterLogging
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingClusterLoggingDetailsOutput]]


# AwsEksClusterLoggingDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEksClusterResourcesVpcConfigDetails

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EndpointPublicAccess
- **Type**: typing.Optional[bool]


# AwsEksClusterResourcesVpcConfigDetailsOutput

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### EndpointPublicAccess
- **Type**: typing.Optional[bool]


# AwsEksClusterResourcesVpcConfigDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElasticBeanstalkEnvironmentDetails

### ApplicationName
- **Type**: typing.Optional[str]

### Cname
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[str]

### DateUpdated
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EnvironmentArn
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentLinks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentEnvironmentLink]]

### EnvironmentName
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentOptionSetting]]

### PlatformArn
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentTier]

### VersionLabel
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentDetailsOutput

### ApplicationName
- **Type**: typing.Optional[str]

### Cname
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[str]

### DateUpdated
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EnvironmentArn
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentEnvironmentLink]]

### EnvironmentName
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentOptionSetting]]

### PlatformArn
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentTier]

### VersionLabel
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentEnvironmentLink

### EnvironmentName
- **Type**: typing.Optional[str]

### LinkName
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentOptionSetting

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentTier

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElasticsearchDomainDetails

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDomainEndpointOptions]

### DomainId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainElasticsearchClusterConfigDetails]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainEncryptionAtRestOptions]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptions]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainNodeToNodeEncryptionOptions]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainServiceSoftwareOptions]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainVPCOptionsUnion]


# AwsElasticsearchDomainDetailsOutput

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDomainEndpointOptions]

### DomainId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainElasticsearchClusterConfigDetails]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainEncryptionAtRestOptions]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptions]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainNodeToNodeEncryptionOptions]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainServiceSoftwareOptions]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainVPCOptionsOutput]


# AwsElasticsearchDomainDomainEndpointOptions

### EnforceHTTPS
- **Type**: typing.Optional[bool]

### TLSSecurityPolicy
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainElasticsearchClusterConfigDetails

### DedicatedMasterCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### DedicatedMasterType
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[str]

### ZoneAwarenessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]


# AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


# AwsElasticsearchDomainEncryptionAtRestOptions

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainLogPublishingOptions

### IndexSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsLogConfig]

### SearchSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsLogConfig]

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsLogConfig]


# AwsElasticsearchDomainLogPublishingOptionsLogConfig

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# AwsElasticsearchDomainNodeToNodeEncryptionOptions

### Enabled
- **Type**: typing.Optional[bool]


# AwsElasticsearchDomainServiceSoftwareOptions

### AutomatedUpdateDate
- **Type**: typing.Optional[str]

### Cancellable
- **Type**: typing.Optional[bool]

### CurrentVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NewVersion
- **Type**: typing.Optional[str]

### UpdateAvailable
- **Type**: typing.Optional[bool]

### UpdateStatus
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainVPCOptions

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### VPCId
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainVPCOptionsOutput

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VPCId
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainVPCOptionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElbAppCookieStickinessPolicy

### CookieName
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]


# AwsElbLbCookieStickinessPolicy

### CookieExpirationPeriod
- **Type**: typing.Optional[int]

### PolicyName
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerAccessLog

### EmitInterval
- **Type**: typing.Optional[int]

### Enabled
- **Type**: typing.Optional[bool]

### S3BucketName
- **Type**: typing.Optional[str]

### S3BucketPrefix
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerAdditionalAttribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerAttributes

### AccessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAccessLog]

### ConnectionDraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionDraining]

### ConnectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionSettings]

### CrossZoneLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerCrossZoneLoadBalancing]

### AdditionalAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAdditionalAttribute]]


# AwsElbLoadBalancerAttributesOutput

### AccessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAccessLog]

### ConnectionDraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionDraining]

### ConnectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionSettings]

### CrossZoneLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerCrossZoneLoadBalancing]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAdditionalAttribute]]


# AwsElbLoadBalancerAttributesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElbLoadBalancerBackendServerDescription

### InstancePort
- **Type**: typing.Optional[int]

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsElbLoadBalancerBackendServerDescriptionOutput

### InstancePort
- **Type**: typing.Optional[int]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerBackendServerDescriptionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElbLoadBalancerConnectionDraining

### Enabled
- **Type**: typing.Optional[bool]

### Timeout
- **Type**: typing.Optional[int]


# AwsElbLoadBalancerConnectionSettings

### IdleTimeout
- **Type**: typing.Optional[int]


# AwsElbLoadBalancerCrossZoneLoadBalancing

### Enabled
- **Type**: typing.Optional[bool]


# AwsElbLoadBalancerDetails

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### BackendServerDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerBackendServerDescriptionUnion]]

### CanonicalHostedZoneName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneNameID
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerHealthCheck]

### Instances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerInstance]]

### ListenerDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerDescriptionUnion]]

### LoadBalancerAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAttributesUnion]

### LoadBalancerName
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerPoliciesUnion]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerSourceSecurityGroup]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerDetailsOutput

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackendServerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerBackendServerDescriptionOutput]]

### CanonicalHostedZoneName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneNameID
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerHealthCheck]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerInstance]]

### ListenerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerDescriptionOutput]]

### LoadBalancerAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAttributesOutput]

### LoadBalancerName
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerPoliciesOutput]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SourceSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerSourceSecurityGroup]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerHealthCheck

### HealthyThreshold
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### Target
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### UnhealthyThreshold
- **Type**: typing.Optional[int]


# AwsElbLoadBalancerInstance

### InstanceId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerListener

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElbLoadBalancerListenerDescription

### Listener
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListener]

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsElbLoadBalancerListenerDescriptionOutput

### Listener
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListener]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerListenerDescriptionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElbLoadBalancerPolicies

### AppCookieStickinessPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbAppCookieStickinessPolicy]]

### LbCookieStickinessPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLbCookieStickinessPolicy]]

### OtherPolicies
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsElbLoadBalancerPoliciesOutput

### AppCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbAppCookieStickinessPolicy]]

### LbCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLbCookieStickinessPolicy]]

### OtherPolicies
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerPoliciesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsElbLoadBalancerSourceSecurityGroup

### GroupName
- **Type**: typing.Optional[str]

### OwnerAlias
- **Type**: typing.Optional[str]


# AwsElbv2LoadBalancerAttribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEventSchemasRegistryDetails

### Description
- **Type**: typing.Optional[str]

### RegistryArn
- **Type**: typing.Optional[str]

### RegistryName
- **Type**: typing.Optional[str]


# AwsEventsEndpointDetails

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EventBuses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointEventBusesDetails]]

### Name
- **Type**: typing.Optional[str]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointReplicationConfigDetails]

### RoleArn
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigDetails]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# AwsEventsEndpointDetailsOutput

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EventBuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointEventBusesDetails]]

### Name
- **Type**: typing.Optional[str]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointReplicationConfigDetails]

### RoleArn
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigDetails]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# AwsEventsEndpointEventBusesDetails

### EventBusArn
- **Type**: typing.Optional[str]


# AwsEventsEndpointReplicationConfigDetails

### State
- **Type**: typing.Optional[str]


# AwsEventsEndpointRoutingConfigDetails

### FailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigFailoverConfigDetails]


# AwsEventsEndpointRoutingConfigFailoverConfigDetails

### Primary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails]

### Secondary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails]


# AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails

### HealthCheck
- **Type**: typing.Optional[str]


# AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails

### Route
- **Type**: typing.Optional[str]


# AwsEventsEventbusDetails

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesCloudTrailDetails

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesDetails

### CloudTrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesCloudTrailDetails]

### DnsLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesDnsLogsDetails]

### FlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesFlowLogsDetails]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesKubernetesDetails]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails]

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesS3LogsDetails]


# AwsGuardDutyDetectorDataSourcesDnsLogsDetails

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesFlowLogsDetails

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesKubernetesDetails

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails]


# AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetails]

### ServiceRole
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsGuardDutyDetectorDataSourcesS3LogsDetails

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDetails

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesDetails]

### Features
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorFeaturesDetails]]

### FindingPublishingFrequency
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDetailsOutput

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesDetails]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorFeaturesDetails]]

### FindingPublishingFrequency
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorFeaturesDetails

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsIamAccessKeyDetails

### UserName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### CreatedAt
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[str]

### PrincipalName
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AccessKeyId
- **Type**: typing.Optional[str]

### SessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeySessionContext]


# AwsIamAccessKeySessionContext

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeySessionContextAttributes]

### SessionIssuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeySessionContextSessionIssuer]


# AwsIamAccessKeySessionContextAttributes

### MfaAuthenticated
- **Type**: typing.Optional[bool]

### CreationDate
- **Type**: typing.Optional[str]


# AwsIamAccessKeySessionContextSessionIssuer

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsIamAttachedManagedPolicy

### PolicyName
- **Type**: typing.Optional[str]

### PolicyArn
- **Type**: typing.Optional[str]


# AwsIamGroupDetails

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicy]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### GroupPolicyList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupPolicy]]

### Path
- **Type**: typing.Optional[str]


# AwsIamGroupDetailsOutput

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicy]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### GroupPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupPolicy]]

### Path
- **Type**: typing.Optional[str]


# AwsIamGroupPolicy

### PolicyName
- **Type**: typing.Optional[str]


# AwsIamInstanceProfile

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileId
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Roles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileRole]]


# AwsIamInstanceProfileOutput

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileId
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileRole]]


# AwsIamInstanceProfileRole

### Arn
- **Type**: typing.Optional[str]

### AssumeRolePolicyDocument
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### RoleId
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]


# AwsIamInstanceProfileUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsIamPermissionsBoundary

### PermissionsBoundaryArn
- **Type**: typing.Optional[str]

### PermissionsBoundaryType
- **Type**: typing.Optional[str]


# AwsIamPolicyDetails

### AttachmentCount
- **Type**: typing.Optional[int]

### CreateDate
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsAttachable
- **Type**: typing.Optional[bool]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundaryUsageCount
- **Type**: typing.Optional[int]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### PolicyVersionList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyVersion]]

### UpdateDate
- **Type**: typing.Optional[str]


# AwsIamPolicyDetailsOutput

### AttachmentCount
- **Type**: typing.Optional[int]

### CreateDate
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsAttachable
- **Type**: typing.Optional[bool]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundaryUsageCount
- **Type**: typing.Optional[int]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### PolicyVersionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyVersion]]

### UpdateDate
- **Type**: typing.Optional[str]


# AwsIamPolicyVersion

### VersionId
- **Type**: typing.Optional[str]

### IsDefaultVersion
- **Type**: typing.Optional[bool]

### CreateDate
- **Type**: typing.Optional[str]


# AwsIamRoleDetails

### AssumeRolePolicyDocument
- **Type**: typing.Optional[str]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicy]]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileUnion]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundary]

### RoleId
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RolePolicyList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRolePolicy]]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### Path
- **Type**: typing.Optional[str]


# AwsIamRoleDetailsOutput

### AssumeRolePolicyDocument
- **Type**: typing.Optional[str]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicy]]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileOutput]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundary]

### RoleId
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RolePolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRolePolicy]]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### Path
- **Type**: typing.Optional[str]


# AwsIamRolePolicy

### PolicyName
- **Type**: typing.Optional[str]


# AwsIamUserDetails

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicy]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupList
- **Type**: typing.Optional[typing.Sequence[str]]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundary]

### UserId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserPolicyList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserPolicy]]


# AwsIamUserDetailsOutput

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicy]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupList
- **Type**: typing.Optional[typing.List[str]]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundary]

### UserId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserPolicy]]


# AwsIamUserPolicy

### PolicyName
- **Type**: typing.Optional[str]


# AwsKinesisStreamDetails

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### StreamEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKinesisStreamStreamEncryptionDetails]

### ShardCount
- **Type**: typing.Optional[int]

### RetentionPeriodHours
- **Type**: typing.Optional[int]


# AwsKinesisStreamStreamEncryptionDetails

### EncryptionType
- **Type**: typing.Optional[str]

### KeyId
- **Type**: typing.Optional[str]


# AwsKmsKeyDetails

### AWSAccountId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[float]

### KeyId
- **Type**: typing.Optional[str]

### KeyManager
- **Type**: typing.Optional[str]

### KeyState
- **Type**: typing.Optional[str]

### Origin
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KeyRotationStatus
- **Type**: typing.Optional[bool]


# AwsLambdaFunctionCode

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### ZipFile
- **Type**: typing.Optional[str]


# AwsLambdaFunctionDeadLetterConfig

### TargetArn
- **Type**: typing.Optional[str]


# AwsLambdaFunctionDetails

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionCode]

### CodeSha256
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDeadLetterConfig]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentUnion]

### FunctionName
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionLayer]]

### MasterArn
- **Type**: typing.Optional[str]

### MemorySize
- **Type**: typing.Optional[int]

### RevisionId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionTracingConfig]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionVpcConfigUnion]

### Version
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.Sequence[str]]

### PackageType
- **Type**: typing.Optional[str]


# AwsLambdaFunctionDetailsOutput

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionCode]

### CodeSha256
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDeadLetterConfig]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentOutput]

### FunctionName
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionLayer]]

### MasterArn
- **Type**: typing.Optional[str]

### MemorySize
- **Type**: typing.Optional[int]

### RevisionId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionTracingConfig]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionVpcConfigOutput]

### Version
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.List[str]]

### PackageType
- **Type**: typing.Optional[str]


# AwsLambdaFunctionEnvironment

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentError]


# AwsLambdaFunctionEnvironmentError

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsLambdaFunctionEnvironmentOutput

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentError]


# AwsLambdaFunctionEnvironmentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsLambdaFunctionLayer

### Arn
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]


# AwsLambdaFunctionTracingConfig

### Mode
- **Type**: typing.Optional[str]


# AwsLambdaFunctionVpcConfig

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsLambdaFunctionVpcConfigOutput

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsLambdaFunctionVpcConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsLambdaLayerVersionDetails

### Version
- **Type**: typing.Optional[int]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.Sequence[str]]

### CreatedDate
- **Type**: typing.Optional[str]


# AwsLambdaLayerVersionDetailsOutput

### Version
- **Type**: typing.Optional[int]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.List[str]]

### CreatedDate
- **Type**: typing.Optional[str]


# AwsMountPoint

### SourceVolume
- **Type**: typing.Optional[str]

### ContainerPath
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoClientAuthenticationDetails

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslDetails]

### Unauthenticated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnion]


# AwsMskClusterClusterInfoClientAuthenticationDetailsOutput

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslDetails]

### Unauthenticated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutput]


# AwsMskClusterClusterInfoClientAuthenticationDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsMskClusterClusterInfoClientAuthenticationSaslDetails

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails]

### Scram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails]


# AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationTlsDetails

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutput

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoDetails

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoDetails]

### CurrentVersion
- **Type**: typing.Optional[str]

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### ClusterName
- **Type**: typing.Optional[str]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationDetailsUnion]

### EnhancedMonitoring
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoDetailsOutput

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoDetails]

### CurrentVersion
- **Type**: typing.Optional[str]

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### ClusterName
- **Type**: typing.Optional[str]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationDetailsOutput]

### EnhancedMonitoring
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsMskClusterClusterInfoEncryptionInfoDetails

### EncryptionInTransit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails]

### EncryptionAtRest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails]


# AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails

### DataVolumeKMSKeyId
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails

### InCluster
- **Type**: typing.Optional[bool]

### ClientBroker
- **Type**: typing.Optional[str]


# AwsMskClusterDetails

### ClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoDetailsUnion]


# AwsMskClusterDetailsOutput

### ClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoDetailsOutput]


# AwsNetworkFirewallFirewallDetails

### DeleteProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallId
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallSubnetMappingsDetails]]

### VpcId
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallDetailsOutput

### DeleteProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallId
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### SubnetMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallSubnetMappingsDetails]]

### VpcId
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallPolicyDetails

### FirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyDetailsUnion]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyId
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallPolicyDetailsOutput

### FirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyDetailsOutput]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyId
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallSubnetMappingsDetails

### SubnetId
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### MasterUserOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainMasterUserOptionsDetails]


# AwsOpenSearchServiceDomainClusterConfigDetails

### InstanceCount
- **Type**: typing.Optional[int]

### WarmEnabled
- **Type**: typing.Optional[bool]

### WarmCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails]

### DedicatedMasterCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[str]

### WarmType
- **Type**: typing.Optional[str]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### DedicatedMasterType
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


# AwsOpenSearchServiceDomainDetails

### Arn
- **Type**: typing.Optional[str]

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### DomainEndpoint
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainClusterConfigDetails]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDomainEndpointOptionsDetails]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainVpcOptionsDetailsUnion]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionsDetails]

### DomainEndpoints
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails]


# AwsOpenSearchServiceDomainDetailsOutput

### Arn
- **Type**: typing.Optional[str]

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### DomainEndpoint
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainClusterConfigDetails]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDomainEndpointOptionsDetails]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainVpcOptionsDetailsOutput]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionsDetails]

### DomainEndpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails]


# AwsOpenSearchServiceDomainDomainEndpointOptionsDetails

### CustomEndpointCertificateArn
- **Type**: typing.Optional[str]

### CustomEndpointEnabled
- **Type**: typing.Optional[bool]

### EnforceHTTPS
- **Type**: typing.Optional[bool]

### CustomEndpoint
- **Type**: typing.Optional[str]

### TLSSecurityPolicy
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainLogPublishingOption

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# AwsOpenSearchServiceDomainLogPublishingOptionsDetails

### IndexSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOption]

### SearchSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOption]

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOption]


# AwsOpenSearchServiceDomainMasterUserOptionsDetails

### MasterUserArn
- **Type**: typing.Optional[str]

### MasterUserName
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails

### AutomatedUpdateDate
- **Type**: typing.Optional[str]

### Cancellable
- **Type**: typing.Optional[bool]

### CurrentVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NewVersion
- **Type**: typing.Optional[str]

### UpdateAvailable
- **Type**: typing.Optional[bool]

### UpdateStatus
- **Type**: typing.Optional[str]

### OptionalDeployment
- **Type**: typing.Optional[bool]


# AwsOpenSearchServiceDomainVpcOptionsDetails

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsOpenSearchServiceDomainVpcOptionsDetailsOutput

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]


# AwsOpenSearchServiceDomainVpcOptionsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsRdsDbClusterAssociatedRole

### RoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbClusterDetails

### AllocatedStorage
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### ReaderEndpoint
- **Type**: typing.Optional[str]

### CustomEndpoints
- **Type**: typing.Optional[typing.Sequence[str]]

### MultiAz
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroup]]

### HostedZoneId
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### AssociatedRoles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterAssociatedRole]]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### EngineMode
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### HttpEndpointEnabled
- **Type**: typing.Optional[bool]

### ActivityStreamStatus
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### DomainMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembership]]

### DbClusterParameterGroup
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[str]

### DbClusterOptionGroupMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterOptionGroupMembership]]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterMembers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterMember]]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]


# AwsRdsDbClusterDetailsOutput

### AllocatedStorage
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### ReaderEndpoint
- **Type**: typing.Optional[str]

### CustomEndpoints
- **Type**: typing.Optional[typing.List[str]]

### MultiAz
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroup]]

### HostedZoneId
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterAssociatedRole]]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### EngineMode
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### HttpEndpointEnabled
- **Type**: typing.Optional[bool]

### ActivityStreamStatus
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembership]]

### DbClusterParameterGroup
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[str]

### DbClusterOptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterOptionGroupMembership]]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterMember]]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]


# AwsRdsDbClusterMember

### IsClusterWriter
- **Type**: typing.Optional[bool]

### PromotionTier
- **Type**: typing.Optional[int]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### DbClusterParameterGroupStatus
- **Type**: typing.Optional[str]


# AwsRdsDbClusterOptionGroupMembership

### DbClusterOptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutput

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsRdsDbClusterSnapshotDetails

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### DbClusterSnapshotAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnion]]


# AwsRdsDbClusterSnapshotDetailsOutput

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### DbClusterSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutput]]


# AwsRdsDbDomainMembership

### Domain
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Fqdn
- **Type**: typing.Optional[str]

### IamRoleName
- **Type**: typing.Optional[str]


# AwsRdsDbInstanceAssociatedRole

### RoleArn
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbInstanceDetails

### AssociatedRoles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceAssociatedRole]]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### DbInstancePort
- **Type**: typing.Optional[int]

### DbiResourceId
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpoint]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroup]]

### MultiAz
- **Type**: typing.Optional[bool]

### EnhancedMonitoringResourceArn
- **Type**: typing.Optional[str]

### DbInstanceStatus
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DbSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### DbParameterGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbParameterGroup]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupUnion]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbPendingModifiedValuesUnion]

### LatestRestorableTime
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### ReadReplicaSourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaDBInstanceIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### ReadReplicaDBClusterIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbOptionGroupMembership]]

### CharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### StatusInfos
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbStatusInfo]]

### StorageType
- **Type**: typing.Optional[str]

### DomainMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembership]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### Timezone
- **Type**: typing.Optional[str]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKmsKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeature]]

### ListenerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpoint]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]


# AwsRdsDbInstanceDetailsOutput

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceAssociatedRole]]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### DbInstancePort
- **Type**: typing.Optional[int]

### DbiResourceId
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpoint]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroup]]

### MultiAz
- **Type**: typing.Optional[bool]

### EnhancedMonitoringResourceArn
- **Type**: typing.Optional[str]

### DbInstanceStatus
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DbSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### DbParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbParameterGroup]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupOutput]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbPendingModifiedValuesOutput]

### LatestRestorableTime
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### ReadReplicaSourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaDBInstanceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ReadReplicaDBClusterIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbOptionGroupMembership]]

### CharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbStatusInfo]]

### StorageType
- **Type**: typing.Optional[str]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembership]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### Timezone
- **Type**: typing.Optional[str]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKmsKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeature]]

### ListenerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpoint]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]


# AwsRdsDbInstanceEndpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### HostedZoneId
- **Type**: typing.Optional[str]


# AwsRdsDbInstanceVpcSecurityGroup

### VpcSecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbOptionGroupMembership

### OptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbParameterGroup

### DbParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]


# AwsRdsDbPendingModifiedValues

### DbInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### CaCertificateIdentifier
- **Type**: typing.Optional[str]

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### PendingCloudWatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsPendingCloudWatchLogsExportsUnion]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeature]]


# AwsRdsDbPendingModifiedValuesOutput

### DbInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### CaCertificateIdentifier
- **Type**: typing.Optional[str]

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### PendingCloudWatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsPendingCloudWatchLogsExportsOutput]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeature]]


# AwsRdsDbPendingModifiedValuesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsRdsDbProcessorFeature

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupDetails

### DbSecurityGroupArn
- **Type**: typing.Optional[str]

### DbSecurityGroupDescription
- **Type**: typing.Optional[str]

### DbSecurityGroupName
- **Type**: typing.Optional[str]

### Ec2SecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupEc2SecurityGroup]]

### IpRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupIpRange]]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupDetailsOutput

### DbSecurityGroupArn
- **Type**: typing.Optional[str]

### DbSecurityGroupDescription
- **Type**: typing.Optional[str]

### DbSecurityGroupName
- **Type**: typing.Optional[str]

### Ec2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupEc2SecurityGroup]]

### IpRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupIpRange]]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupEc2SecurityGroup

### Ec2SecurityGroupId
- **Type**: typing.Optional[str]

### Ec2SecurityGroupName
- **Type**: typing.Optional[str]

### Ec2SecurityGroupOwnerId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupIpRange

### CidrIp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbSnapshotDetails

### DbSnapshotIdentifier
- **Type**: typing.Optional[str]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceDbSnapshotIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeature]]

### DbiResourceId
- **Type**: typing.Optional[str]


# AwsRdsDbSnapshotDetailsOutput

### DbSnapshotIdentifier
- **Type**: typing.Optional[str]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceDbSnapshotIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeature]]

### DbiResourceId
- **Type**: typing.Optional[str]


# AwsRdsDbStatusInfo

### StatusType
- **Type**: typing.Optional[str]

### Normal
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroup

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### DbSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupSubnet]]

### DbSubnetGroupArn
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupOutput

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### DbSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupSubnet]]

### DbSubnetGroupArn
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupSubnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupSubnetAvailabilityZone]

### SubnetStatus
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupSubnetAvailabilityZone

### Name
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsRdsEventSubscriptionDetails

### CustSubscriptionId
- **Type**: typing.Optional[str]

### CustomerAwsId
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### EventCategoriesList
- **Type**: typing.Optional[typing.Sequence[str]]

### EventSubscriptionArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceIdsList
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionCreationTime
- **Type**: typing.Optional[str]


# AwsRdsEventSubscriptionDetailsOutput

### CustSubscriptionId
- **Type**: typing.Optional[str]

### CustomerAwsId
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### EventCategoriesList
- **Type**: typing.Optional[typing.List[str]]

### EventSubscriptionArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceIdsList
- **Type**: typing.Optional[typing.List[str]]

### SourceType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionCreationTime
- **Type**: typing.Optional[str]


# AwsRdsPendingCloudWatchLogsExports

### LogTypesToEnable
- **Type**: typing.Optional[typing.Sequence[str]]

### LogTypesToDisable
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsRdsPendingCloudWatchLogsExportsOutput

### LogTypesToEnable
- **Type**: typing.Optional[typing.List[str]]

### LogTypesToDisable
- **Type**: typing.Optional[typing.List[str]]


# AwsRdsPendingCloudWatchLogsExportsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsRedshiftClusterClusterNode

### NodeRole
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PublicIpAddress
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterParameterGroup

### ClusterParameterStatusList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterStatus]]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterParameterGroupOutput

### ClusterParameterStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterStatus]]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterParameterGroupUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsRedshiftClusterClusterParameterStatus

### ParameterName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterApplyErrorDescription
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterSecurityGroup

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterSnapshotCopyStatus

### DestinationRegion
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### RetentionPeriod
- **Type**: typing.Optional[int]

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]


# AwsRedshiftClusterDeferredMaintenanceWindow

### DeferMaintenanceEndTime
- **Type**: typing.Optional[str]

### DeferMaintenanceIdentifier
- **Type**: typing.Optional[str]

### DeferMaintenanceStartTime
- **Type**: typing.Optional[str]


# AwsRedshiftClusterDetails

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterAvailabilityStatus
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterNode]]

### ClusterParameterGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterGroupUnion]]

### ClusterPublicKey
- **Type**: typing.Optional[str]

### ClusterRevisionNumber
- **Type**: typing.Optional[str]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSecurityGroup]]

### ClusterSnapshotCopyStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSnapshotCopyStatus]

### ClusterStatus
- **Type**: typing.Optional[str]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeferredMaintenanceWindows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDeferredMaintenanceWindow]]

### ElasticIpStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterElasticIpStatus]

### ElasticResizeNumberOfNodeOptions
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterEndpoint]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### ExpectedNextSnapshotScheduleTime
- **Type**: typing.Optional[str]

### ExpectedNextSnapshotScheduleTimeStatus
- **Type**: typing.Optional[str]

### HsmStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterHsmStatus]

### IamRoles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterIamRole]]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### NextMaintenanceWindowStartTime
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PendingActions
- **Type**: typing.Optional[typing.Sequence[str]]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterPendingModifiedValues]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ResizeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterResizeInfo]

### RestoreStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterRestoreStatus]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### SnapshotScheduleState
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterVpcSecurityGroup]]

### LoggingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterLoggingStatus]


# AwsRedshiftClusterDetailsOutput

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterAvailabilityStatus
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterNode]]

### ClusterParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterGroupOutput]]

### ClusterPublicKey
- **Type**: typing.Optional[str]

### ClusterRevisionNumber
- **Type**: typing.Optional[str]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSecurityGroup]]

### ClusterSnapshotCopyStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSnapshotCopyStatus]

### ClusterStatus
- **Type**: typing.Optional[str]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeferredMaintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDeferredMaintenanceWindow]]

### ElasticIpStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterElasticIpStatus]

### ElasticResizeNumberOfNodeOptions
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterEndpoint]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### ExpectedNextSnapshotScheduleTime
- **Type**: typing.Optional[str]

### ExpectedNextSnapshotScheduleTimeStatus
- **Type**: typing.Optional[str]

### HsmStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterHsmStatus]

### IamRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterIamRole]]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### NextMaintenanceWindowStartTime
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PendingActions
- **Type**: typing.Optional[typing.List[str]]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterPendingModifiedValues]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ResizeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterResizeInfo]

### RestoreStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterRestoreStatus]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### SnapshotScheduleState
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterVpcSecurityGroup]]

### LoggingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterLoggingStatus]


# AwsRedshiftClusterElasticIpStatus

### ElasticIp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterEndpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# AwsRedshiftClusterHsmStatus

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterIamRole

### ApplyStatus
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# AwsRedshiftClusterLoggingStatus

### BucketName
- **Type**: typing.Optional[str]

### LastFailureMessage
- **Type**: typing.Optional[str]

### LastFailureTime
- **Type**: typing.Optional[str]

### LastSuccessfulDeliveryTime
- **Type**: typing.Optional[str]

### LoggingEnabled
- **Type**: typing.Optional[bool]

### S3KeyPrefix
- **Type**: typing.Optional[str]


# AwsRedshiftClusterPendingModifiedValues

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### EncryptionType
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]


# AwsRedshiftClusterResizeInfo

### AllowCancelResize
- **Type**: typing.Optional[bool]

### ResizeType
- **Type**: typing.Optional[str]


# AwsRedshiftClusterRestoreStatus

### CurrentRestoreRateInMegaBytesPerSecond
- **Type**: typing.Optional[float]

### ElapsedTimeInSeconds
- **Type**: typing.Optional[int]

### EstimatedTimeToCompletionInSeconds
- **Type**: typing.Optional[int]

### ProgressInMegaBytes
- **Type**: typing.Optional[int]

### SnapshotSizeInMegaBytes
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterVpcSecurityGroup

### Status
- **Type**: typing.Optional[str]

### VpcSecurityGroupId
- **Type**: typing.Optional[str]


# AwsRoute53HostedZoneConfigDetails

### Comment
- **Type**: typing.Optional[str]


# AwsRoute53HostedZoneDetails

### HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneObjectDetails]

### Vpcs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneVpcDetails]]

### NameServers
- **Type**: typing.Optional[typing.Sequence[str]]

### QueryLoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53QueryLoggingConfigDetails]


# AwsRoute53HostedZoneDetailsOutput

### HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneObjectDetails]

### Vpcs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneVpcDetails]]

### NameServers
- **Type**: typing.Optional[typing.List[str]]

### QueryLoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53QueryLoggingConfigDetails]


# AwsRoute53HostedZoneObjectDetails

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneConfigDetails]


# AwsRoute53HostedZoneVpcDetails

### Id
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# AwsRoute53QueryLoggingConfigDetails

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CloudWatchLogsLogGroupArnConfigDetails]


# AwsS3AccessPointDetails

### AccessPointArn
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### Bucket
- **Type**: typing.Optional[str]

### BucketAccountId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NetworkOrigin
- **Type**: typing.Optional[str]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetails]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccessPointVpcConfigurationDetails]


# AwsS3AccessPointVpcConfigurationDetails

### VpcId
- **Type**: typing.Optional[str]


# AwsS3AccountPublicAccessBlockDetails

### BlockPublicAcls
- **Type**: typing.Optional[bool]

### BlockPublicPolicy
- **Type**: typing.Optional[bool]

### IgnorePublicAcls
- **Type**: typing.Optional[bool]

### RestrictPublicBuckets
- **Type**: typing.Optional[bool]


# AwsS3BucketBucketLifecycleConfigurationDetails

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnion]]


# AwsS3BucketBucketLifecycleConfigurationDetailsOutput

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutput]]


# AwsS3BucketBucketLifecycleConfigurationDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketBucketLifecycleConfigurationRulesDetails

### AbortIncompleteMultipartUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails]

### ExpirationDate
- **Type**: typing.Optional[str]

### ExpirationInDays
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnion]

### ID
- **Type**: typing.Optional[str]

### NoncurrentVersionExpirationInDays
- **Type**: typing.Optional[int]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails]]

### Prefix
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Transitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails]]


# AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutput

### AbortIncompleteMultipartUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails]

### ExpirationDate
- **Type**: typing.Optional[str]

### ExpirationInDays
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutput]

### ID
- **Type**: typing.Optional[str]

### NoncurrentVersionExpirationInDays
- **Type**: typing.Optional[int]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails]]

### Prefix
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails]]


# AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails

### Predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnion]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutput

### Predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutput]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails

### Date
- **Type**: typing.Optional[str]

### Days
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[str]


# AwsS3BucketBucketVersioningConfiguration

### IsMfaDeleteEnabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]


# AwsS3BucketDetails

### OwnerId
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionConfigurationUnion]

### BucketLifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationDetailsUnion]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetails]

### AccessControlList
- **Type**: typing.Optional[str]

### BucketLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketLoggingConfiguration]

### BucketWebsiteConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationUnion]

### BucketNotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationUnion]

### BucketVersioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketVersioningConfiguration]

### ObjectLockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfiguration]

### Name
- **Type**: typing.Optional[str]


# AwsS3BucketDetailsOutput

### OwnerId
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionConfigurationOutput]

### BucketLifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationDetailsOutput]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetails]

### AccessControlList
- **Type**: typing.Optional[str]

### BucketLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketLoggingConfiguration]

### BucketWebsiteConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationOutput]

### BucketNotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationOutput]

### BucketVersioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketVersioningConfiguration]

### ObjectLockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfiguration]

### Name
- **Type**: typing.Optional[str]


# AwsS3BucketLoggingConfiguration

### DestinationBucketName
- **Type**: typing.Optional[str]

### LogFilePrefix
- **Type**: typing.Optional[str]


# AwsS3BucketNotificationConfiguration

### Configurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationDetailUnion]]


# AwsS3BucketNotificationConfigurationDetailOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketNotificationConfigurationDetailUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketNotificationConfigurationFilter

### S3KeyFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterUnion]


# AwsS3BucketNotificationConfigurationFilterOutput

### S3KeyFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterOutput]


# AwsS3BucketNotificationConfigurationOutput

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationDetailOutput]]


# AwsS3BucketNotificationConfigurationS3KeyFilter

### FilterRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterRule]]


# AwsS3BucketNotificationConfigurationS3KeyFilterOutput

### FilterRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterRule]]


# AwsS3BucketNotificationConfigurationS3KeyFilterRule

### Name
- **Type**: typing.Optional[typing.Literal['Prefix', 'Suffix']]

### Value
- **Type**: typing.Optional[str]


# AwsS3BucketNotificationConfigurationS3KeyFilterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketNotificationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketObjectLockConfiguration

### ObjectLockEnabled
- **Type**: typing.Optional[str]

### Rule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfigurationRuleDetails]


# AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails

### Days
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[str]

### Years
- **Type**: typing.Optional[int]


# AwsS3BucketObjectLockConfigurationRuleDetails

### DefaultRetention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails]


# AwsS3BucketServerSideEncryptionByDefault

### SSEAlgorithm
- **Type**: typing.Optional[str]

### KMSMasterKeyID
- **Type**: typing.Optional[str]


# AwsS3BucketServerSideEncryptionConfiguration

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionRule]]


# AwsS3BucketServerSideEncryptionConfigurationOutput

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionRule]]


# AwsS3BucketServerSideEncryptionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketServerSideEncryptionRule

### ApplyServerSideEncryptionByDefault
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionByDefault]


# AwsS3BucketWebsiteConfiguration

### ErrorDocument
- **Type**: typing.Optional[str]

### IndexDocumentSuffix
- **Type**: typing.Optional[str]

### RedirectAllRequestsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRedirectTo]

### RoutingRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRule]]


# AwsS3BucketWebsiteConfigurationOutput

### ErrorDocument
- **Type**: typing.Optional[str]

### IndexDocumentSuffix
- **Type**: typing.Optional[str]

### RedirectAllRequestsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRedirectTo]

### RoutingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRule]]


# AwsS3BucketWebsiteConfigurationRedirectTo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketWebsiteConfigurationRoutingRule

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRuleCondition]

### Redirect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRuleRedirect]


# AwsS3BucketWebsiteConfigurationRoutingRuleCondition

### HttpErrorCodeReturnedEquals
- **Type**: typing.Optional[str]

### KeyPrefixEquals
- **Type**: typing.Optional[str]


# AwsS3BucketWebsiteConfigurationRoutingRuleRedirect

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3BucketWebsiteConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsS3ObjectDetails

### LastModified
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### ServerSideEncryption
- **Type**: typing.Optional[str]

### SSEKMSKeyId
- **Type**: typing.Optional[str]


# AwsSageMakerNotebookInstanceDetails

### AcceleratorTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### DirectInternetAccess
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### InstanceMetadataServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails]

### InstanceType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NotebookInstanceArn
- **Type**: typing.Optional[str]

### NotebookInstanceLifecycleConfigName
- **Type**: typing.Optional[str]

### NotebookInstanceName
- **Type**: typing.Optional[str]

### NotebookInstanceStatus
- **Type**: typing.Optional[str]

### PlatformIdentifier
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### RootAccess
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### VolumeSizeInGB
- **Type**: typing.Optional[int]


# AwsSageMakerNotebookInstanceDetailsOutput

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[str]]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.List[str]]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### DirectInternetAccess
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### InstanceMetadataServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails]

### InstanceType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NotebookInstanceArn
- **Type**: typing.Optional[str]

### NotebookInstanceLifecycleConfigName
- **Type**: typing.Optional[str]

### NotebookInstanceName
- **Type**: typing.Optional[str]

### NotebookInstanceStatus
- **Type**: typing.Optional[str]

### PlatformIdentifier
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### RootAccess
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SubnetId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### VolumeSizeInGB
- **Type**: typing.Optional[int]


# AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails

### MinimumInstanceMetadataServiceVersion
- **Type**: typing.Optional[str]


# AwsSecretsManagerSecretDetails

### RotationRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecretsManagerSecretRotationRules]

### RotationOccurredWithinFrequency
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### RotationEnabled
- **Type**: typing.Optional[bool]

### RotationLambdaArn
- **Type**: typing.Optional[str]

### Deleted
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AwsSecretsManagerSecretRotationRules

### AutomaticallyAfterDays
- **Type**: typing.Optional[int]


# AwsSecurityFinding

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratorId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ResourceUnion]
- **Required**: Yes

### ProductName
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]

### FirstObservedAt
- **Type**: typing.Optional[str]

### LastObservedAt
- **Type**: typing.Optional[str]

### Severity
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Remediation
- **Type**: <class 'NoneType'>

### SourceUrl
- **Type**: typing.Optional[str]

### ProductFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Malware
- **Type**: typing.Optional[typing.Sequence[NoneType]]

### Network
- **Type**: <class 'NoneType'>

### NetworkPath
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentUnion]]

### Process
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ProcessDetails]

### Threats
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ThreatUnion]]

### ThreatIntelIndicators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ThreatIntelIndicator]]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ComplianceUnion]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### WorkflowState
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'DEFERRED', 'IN_PROGRESS', 'NEW', 'RESOLVED']]

### Workflow
- **Type**: <class 'NoneType'>

### RecordState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFinding]]

### Note
- **Type**: <class 'NoneType'>

### Vulnerabilities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityUnion]]

### PatchSummary
- **Type**: <class 'NoneType'>

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionUnion]

### FindingProviderFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderFieldsUnion]

### Sample
- **Type**: typing.Optional[bool]

### GeneratorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.GeneratorDetailsUnion]

### ProcessedAt
- **Type**: typing.Optional[str]

### AwsAccountName
- **Type**: typing.Optional[str]

### Detection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DetectionUnion]


# AwsSecurityFindingFiltersOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsSecurityFindingFiltersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsSecurityFindingIdentifier

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes


# AwsSecurityFindingOutput

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratorId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResourceOutput]
- **Required**: Yes

### ProductName
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Types
- **Type**: typing.Optional[typing.List[str]]

### FirstObservedAt
- **Type**: typing.Optional[str]

### LastObservedAt
- **Type**: typing.Optional[str]

### Severity
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Remediation
- **Type**: <class 'NoneType'>

### SourceUrl
- **Type**: typing.Optional[str]

### ProductFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### Malware
- **Type**: typing.Optional[typing.List[NoneType]]

### Network
- **Type**: <class 'NoneType'>

### NetworkPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentOutput]]

### Process
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ProcessDetails]

### Threats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ThreatOutput]]

### ThreatIntelIndicators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ThreatIntelIndicator]]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ComplianceOutput]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### WorkflowState
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'DEFERRED', 'IN_PROGRESS', 'NEW', 'RESOLVED']]

### Workflow
- **Type**: <class 'NoneType'>

### RecordState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFinding]]

### Note
- **Type**: <class 'NoneType'>

### Vulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityOutput]]

### PatchSummary
- **Type**: <class 'NoneType'>

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionOutput]

### FindingProviderFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderFieldsOutput]

### Sample
- **Type**: typing.Optional[bool]

### GeneratorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.GeneratorDetailsOutput]

### ProcessedAt
- **Type**: typing.Optional[str]

### AwsAccountName
- **Type**: typing.Optional[str]

### Detection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DetectionOutput]


# AwsSecurityFindingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsSnsTopicDetails

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### Subscription
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicSubscription]]

### TopicName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### SqsSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### SqsFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### ApplicationSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpFailureFeedbackRoleArn
- **Type**: typing.Optional[str]


# AwsSnsTopicDetailsOutput

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### Subscription
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicSubscription]]

### TopicName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### SqsSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### SqsFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### ApplicationSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpFailureFeedbackRoleArn
- **Type**: typing.Optional[str]


# AwsSnsTopicSubscription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsSqsQueueDetails

### KmsDataKeyReusePeriodSeconds
- **Type**: typing.Optional[int]

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### QueueName
- **Type**: typing.Optional[str]

### DeadLetterTargetArn
- **Type**: typing.Optional[str]


# AwsSsmComplianceSummary

### Status
- **Type**: typing.Optional[str]

### CompliantCriticalCount
- **Type**: typing.Optional[int]

### CompliantHighCount
- **Type**: typing.Optional[int]

### CompliantMediumCount
- **Type**: typing.Optional[int]

### ExecutionType
- **Type**: typing.Optional[str]

### NonCompliantCriticalCount
- **Type**: typing.Optional[int]

### CompliantInformationalCount
- **Type**: typing.Optional[int]

### NonCompliantInformationalCount
- **Type**: typing.Optional[int]

### CompliantUnspecifiedCount
- **Type**: typing.Optional[int]

### NonCompliantLowCount
- **Type**: typing.Optional[int]

### NonCompliantHighCount
- **Type**: typing.Optional[int]

### CompliantLowCount
- **Type**: typing.Optional[int]

### ComplianceType
- **Type**: typing.Optional[str]

### PatchBaselineId
- **Type**: typing.Optional[str]

### OverallSeverity
- **Type**: typing.Optional[str]

### NonCompliantMediumCount
- **Type**: typing.Optional[int]

### NonCompliantUnspecifiedCount
- **Type**: typing.Optional[int]

### PatchGroup
- **Type**: typing.Optional[str]


# AwsSsmPatch

### ComplianceSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSsmComplianceSummary]


# AwsSsmPatchComplianceDetails

### Patch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSsmPatch]


# AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails

### CloudWatchLogsLogGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails]


# AwsStepFunctionStateMachineLoggingConfigurationDetails

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails]]

### IncludeExecutionData
- **Type**: typing.Optional[bool]

### Level
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineLoggingConfigurationDetailsOutput

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails]]

### IncludeExecutionData
- **Type**: typing.Optional[bool]

### Level
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineTracingConfigurationDetails

### Enabled
- **Type**: typing.Optional[bool]


# AwsWafRateBasedRuleDetails

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleMatchPredicate]]


# AwsWafRateBasedRuleDetailsOutput

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleMatchPredicate]]


# AwsWafRateBasedRuleMatchPredicate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafRegionalRateBasedRuleDetails

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleMatchPredicate]]


# AwsWafRegionalRateBasedRuleDetailsOutput

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleMatchPredicate]]


# AwsWafRegionalRateBasedRuleMatchPredicate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafRegionalRuleDetails

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRulePredicateListDetails]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRegionalRuleDetailsOutput

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRulePredicateListDetails]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRegionalRuleGroupDetails

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupRulesDetails]]


# AwsWafRegionalRuleGroupDetailsOutput

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupRulesDetails]]


# AwsWafRegionalRuleGroupRulesDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafRegionalRulePredicateListDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafRegionalWebAclDetails

### DefaultAction
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RulesList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclRulesListDetails]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclDetailsOutput

### DefaultAction
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RulesList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclRulesListDetails]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclRulesListDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafRuleDetails

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRulePredicateListDetails]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRuleDetailsOutput

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRulePredicateListDetails]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRuleGroupDetails

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupRulesDetails]]


# AwsWafRuleGroupDetailsOutput

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupRulesDetails]]


# AwsWafRuleGroupRulesDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafRulePredicateListDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafWebAclDetails

### Name
- **Type**: typing.Optional[str]

### DefaultAction
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclRuleUnion]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafWebAclDetailsOutput

### Name
- **Type**: typing.Optional[str]

### DefaultAction
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclRuleOutput]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafWebAclRuleOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafWebAclRuleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2ActionAllowDetails

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsUnion]


# AwsWafv2ActionAllowDetailsOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsOutput]


# AwsWafv2ActionAllowDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2ActionBlockDetails

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomResponseDetailsUnion]


# AwsWafv2ActionBlockDetailsOutput

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomResponseDetailsOutput]


# AwsWafv2ActionBlockDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2CustomHttpHeader

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsWafv2CustomRequestHandlingDetails

### InsertHeaders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeader]]


# AwsWafv2CustomRequestHandlingDetailsOutput

### InsertHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeader]]


# AwsWafv2CustomRequestHandlingDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2CustomResponseDetails

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[int]

### ResponseHeaders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeader]]


# AwsWafv2CustomResponseDetailsOutput

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[int]

### ResponseHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeader]]


# AwsWafv2CustomResponseDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2RuleGroupDetails

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsUnion]]

### Scope
- **Type**: typing.Optional[str]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetails]


# AwsWafv2RuleGroupDetailsOutput

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsOutput]]

### Scope
- **Type**: typing.Optional[str]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetails]


# AwsWafv2RulesActionCaptchaDetails

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsUnion]


# AwsWafv2RulesActionCaptchaDetailsOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsOutput]


# AwsWafv2RulesActionCaptchaDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2RulesActionCountDetails

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsUnion]


# AwsWafv2RulesActionCountDetailsOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsOutput]


# AwsWafv2RulesActionCountDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2RulesActionDetails

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsUnion]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsUnion]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCaptchaDetailsUnion]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCountDetailsUnion]


# AwsWafv2RulesActionDetailsOutput

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsOutput]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsOutput]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCaptchaDetailsOutput]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCountDetailsOutput]


# AwsWafv2RulesActionDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2RulesDetails

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionDetailsUnion]

### Name
- **Type**: typing.Optional[str]

### OverrideAction
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetails]


# AwsWafv2RulesDetailsOutput

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionDetailsOutput]

### Name
- **Type**: typing.Optional[str]

### OverrideAction
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetails]


# AwsWafv2RulesDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2VisibilityConfigDetails

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### MetricName
- **Type**: typing.Optional[str]

### SampledRequestsEnabled
- **Type**: typing.Optional[bool]


# AwsWafv2WebAclActionDetails

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsUnion]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsUnion]


# AwsWafv2WebAclActionDetailsOutput

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsOutput]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsOutput]


# AwsWafv2WebAclActionDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsWafv2WebAclCaptchaConfigDetails

### ImmunityTimeProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails]


# AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails

### ImmunityTime
- **Type**: typing.Optional[int]


# AwsWafv2WebAclDetails

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ManagedbyFirewallManager
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### Capacity
- **Type**: typing.Optional[int]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclCaptchaConfigDetails]

### DefaultAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclActionDetailsUnion]

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetails]]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetails]


# AwsWafv2WebAclDetailsOutput

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ManagedbyFirewallManager
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### Capacity
- **Type**: typing.Optional[int]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclCaptchaConfigDetails]

### DefaultAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclActionDetailsOutput]

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsOutput]]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetails]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteAutomationRulesRequest

### AutomationRulesArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteAutomationRulesResponse

### ProcessedAutomationRules
- **Type**: typing.List[str]
- **Required**: Yes

### UnprocessedAutomationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedAutomationRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisableStandardsRequest

### StandardsSubscriptionArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisableStandardsResponse

### StandardsSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchEnableStandardsRequest

### StandardsSubscriptionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscriptionRequest]
- **Required**: Yes


# BatchEnableStandardsResponse

### StandardsSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetAutomationRulesRequest

### AutomationRulesArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetAutomationRulesResponse

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesConfig]
- **Required**: Yes

### UnprocessedAutomationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedAutomationRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetConfigurationPolicyAssociationsRequest

### ConfigurationPolicyAssociationIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociation]
- **Required**: Yes


# BatchGetConfigurationPolicyAssociationsResponse

### ConfigurationPolicyAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociationSummary]
- **Required**: Yes

### UnprocessedConfigurationPolicyAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedConfigurationPolicyAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetSecurityControlsRequest

### SecurityControlIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetSecurityControlsResponse

### SecurityControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControl]
- **Required**: Yes

### UnprocessedIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedSecurityControl]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetStandardsControlAssociationsRequest

### StandardsControlAssociationIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationId]
- **Required**: Yes


# BatchGetStandardsControlAssociationsResponse

### StandardsControlAssociationDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationDetail]
- **Required**: Yes

### UnprocessedAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedStandardsControlAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchImportFindingsRequest

### Findings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingUnion]
- **Required**: Yes


# BatchImportFindingsResponse

### FailedCount
- **Type**: <class 'int'>
- **Required**: Yes

### SuccessCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ImportFindingsError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateAutomationRulesRequest

### UpdateAutomationRulesRequestItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.UpdateAutomationRulesRequestItem]
- **Required**: Yes


# BatchUpdateAutomationRulesResponse

### ProcessedAutomationRules
- **Type**: typing.List[str]
- **Required**: Yes

### UnprocessedAutomationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedAutomationRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateFindingsRequest

### FindingIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifier]
- **Required**: Yes

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdate]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityUpdate]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowUpdate]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFinding]]


# BatchUpdateFindingsResponse

### ProcessedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifier]
- **Required**: Yes

### UnprocessedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.BatchUpdateFindingsUnprocessedFinding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateFindingsUnprocessedFinding

### FindingIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifier'>
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# BatchUpdateStandardsControlAssociationsRequest

### StandardsControlAssociationUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationUpdate]
- **Required**: Yes


# BatchUpdateStandardsControlAssociationsResponse

### UnprocessedAssociationUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedStandardsControlAssociationUpdate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# BooleanConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[bool]


# BooleanFilter

### Value
- **Type**: typing.Optional[bool]


# Cell

### Column
- **Type**: typing.Optional[int]

### Row
- **Type**: typing.Optional[int]

### ColumnName
- **Type**: typing.Optional[str]

### CellReference
- **Type**: typing.Optional[str]


# CidrBlockAssociation

### AssociationId
- **Type**: typing.Optional[str]

### CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockState
- **Type**: typing.Optional[str]


# City

### CityName
- **Type**: typing.Optional[str]


# ClassificationResult

### MimeType
- **Type**: typing.Optional[str]

### SizeClassified
- **Type**: typing.Optional[int]

### AdditionalOccurrences
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationStatus]

### SensitiveData
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataResultUnion]]

### CustomDataIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersResultUnion]


# ClassificationResultOutput

### MimeType
- **Type**: typing.Optional[str]

### SizeClassified
- **Type**: typing.Optional[int]

### AdditionalOccurrences
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationStatus]

### SensitiveData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataResultOutput]]

### CustomDataIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersResultOutput]


# ClassificationResultUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClassificationStatus

### Code
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# CloudWatchLogsLogGroupArnConfigDetails

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### HostedZoneId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# CodeVulnerabilitiesFilePath

### EndLine
- **Type**: typing.Optional[int]

### FileName
- **Type**: typing.Optional[str]

### FilePath
- **Type**: typing.Optional[str]

### StartLine
- **Type**: typing.Optional[int]


# Compliance

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_AVAILABLE', 'PASSED', 'WARNING']]

### RelatedRequirements
- **Type**: typing.Optional[typing.Sequence[str]]

### StatusReasons
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StatusReason]]

### SecurityControlId
- **Type**: typing.Optional[str]

### AssociatedStandards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AssociatedStandard]]

### SecurityControlParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlParameterUnion]]


# ComplianceOutput

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_AVAILABLE', 'PASSED', 'WARNING']]

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]

### StatusReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StatusReason]]

### SecurityControlId
- **Type**: typing.Optional[str]

### AssociatedStandards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AssociatedStandard]]

### SecurityControlParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlParameterOutput]]


# ComplianceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationOptions

### Integer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.IntegerConfigurationOptions]

### IntegerList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.IntegerListConfigurationOptions]

### Double
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DoubleConfigurationOptions]

### String
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StringConfigurationOptions]

### StringList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StringListConfigurationOptions]

### Boolean
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.BooleanConfigurationOptions]

### Enum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.EnumConfigurationOptions]

### EnumList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.EnumListConfigurationOptions]


# ConfigurationPolicyAssociation

### Target
- **Type**: <class 'NoneType'>


# ConfigurationPolicyAssociationSummary

### ConfigurationPolicyId
- **Type**: typing.Optional[str]

### TargetId
- **Type**: typing.Optional[str]

### TargetType
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']]

### AssociationType
- **Type**: typing.Optional[typing.Literal['APPLIED', 'INHERITED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AssociationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]

### AssociationStatusMessage
- **Type**: typing.Optional[str]


# ConfigurationPolicySummary

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ServiceEnabled
- **Type**: typing.Optional[bool]


# ContainerDetails

### ContainerRuntime
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### ImageName
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### VolumeMounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VolumeMount]]

### Privileged
- **Type**: typing.Optional[bool]


# ContainerDetailsOutput

### ContainerRuntime
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### ImageName
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### VolumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VolumeMount]]

### Privileged
- **Type**: typing.Optional[bool]


# Country

### CountryCode
- **Type**: typing.Optional[str]

### CountryName
- **Type**: typing.Optional[str]


# CreateActionTargetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CreateActionTargetResponse

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAutomationRuleRequest

### RuleOrder
- **Type**: <class 'int'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFiltersUnion'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesActionUnion]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IsTerminal
- **Type**: typing.Optional[bool]


# CreateAutomationRuleResponse

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfigurationPolicyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyUnion'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfigurationPolicyResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFindingAggregatorRequest

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateFindingAggregatorResponse

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FindingAggregationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInsightRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersUnion'>
- **Required**: Yes

### GroupByAttribute
- **Type**: <class 'str'>
- **Required**: Yes


# CreateInsightResponse

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMembersRequest

### AccountDetails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AccountDetails]
- **Required**: Yes


# CreateMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Result]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDataIdentifiersDetections

### Count
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesUnion]


# CustomDataIdentifiersDetectionsOutput

### Count
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesOutput]


# CustomDataIdentifiersDetectionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomDataIdentifiersResult

### Detections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersDetectionsUnion]]

### TotalCount
- **Type**: typing.Optional[int]


# CustomDataIdentifiersResultOutput

### Detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersDetectionsOutput]]

### TotalCount
- **Type**: typing.Optional[int]


# CustomDataIdentifiersResultUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Cvss

### Version
- **Type**: typing.Optional[str]

### BaseScore
- **Type**: typing.Optional[float]

### BaseVector
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Adjustments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Adjustment]]


# CvssOutput

### Version
- **Type**: typing.Optional[str]

### BaseScore
- **Type**: typing.Optional[float]

### BaseVector
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Adjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Adjustment]]


# CvssUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataClassificationDetails

### DetailedResultsLocation
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationResultUnion]


# DataClassificationDetailsOutput

### DetailedResultsLocation
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationResultOutput]


# DateFilter

### Start
- **Type**: typing.Optional[str]

### End
- **Type**: typing.Optional[str]

### DateRange
- **Type**: <class 'NoneType'>


# DateRange

### Value
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['DAYS']]


# DeclineInvitationsRequest

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeclineInvitationsResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Result]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteActionTargetRequest

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteActionTargetResponse

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConfigurationPolicyRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFindingAggregatorRequest

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInsightRequest

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInsightResponse

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInvitationsRequest

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteInvitationsResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Result]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMembersRequest

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Result]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeActionTargetsRequest

### ActionTargetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeActionTargetsRequestPaginate

### ActionTargetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# DescribeActionTargetsResponse

### ActionTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ActionTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeHubRequest

### HubArn
- **Type**: typing.Optional[str]


# DescribeHubResponse

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscribedAt
- **Type**: <class 'str'>
- **Required**: Yes

### AutoEnableControls
- **Type**: <class 'bool'>
- **Required**: Yes

### ControlFindingGenerator
- **Type**: typing.Literal['SECURITY_CONTROL', 'STANDARD_CONTROL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponse

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### MemberAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoEnableStandards
- **Type**: typing.Literal['DEFAULT', 'NONE']
- **Required**: Yes

### OrganizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.OrganizationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProductsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ProductArn
- **Type**: typing.Optional[str]


# DescribeProductsRequestPaginate

### ProductArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# DescribeProductsResponse

### Products
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Product]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStandardsControlsRequest

### StandardsSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeStandardsControlsRequestPaginate

### StandardsSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# DescribeStandardsControlsResponse

### Controls
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControl]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStandardsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeStandardsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# DescribeStandardsResponse

### Standards
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Standard]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DetectionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DetectionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisableImportFindingsForProductRequest

### ProductSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisableOrganizationAdminAccountRequest

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMembersRequest

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DnsRequestAction

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DoubleConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# EnableImportFindingsForProductRequest

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableImportFindingsForProductResponse

### ProductSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# EnableOrganizationAdminAccountRequest

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableSecurityHubRequest

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EnableDefaultStandards
- **Type**: typing.Optional[bool]

### ControlFindingGenerator
- **Type**: typing.Optional[typing.Literal['SECURITY_CONTROL', 'STANDARD_CONTROL']]


# EnumConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]


# EnumListConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[typing.List[str]]

### MaxItems
- **Type**: typing.Optional[int]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]


# FilePaths

### FilePath
- **Type**: typing.Optional[str]

### FileName
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]


# FindingAggregator

### FindingAggregatorArn
- **Type**: typing.Optional[str]


# FindingHistoryRecord

### FindingIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifier]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### FindingCreated
- **Type**: typing.Optional[bool]

### UpdateSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingHistoryUpdateSource]

### Updates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FindingHistoryUpdate]]

### NextToken
- **Type**: typing.Optional[str]


# FindingHistoryUpdate

### UpdatedField
- **Type**: typing.Optional[str]

### OldValue
- **Type**: typing.Optional[str]

### NewValue
- **Type**: typing.Optional[str]


# FindingHistoryUpdateSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingProviderFields

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFinding]]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderSeverity]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]


# FindingProviderFieldsOutput

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFinding]]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderSeverity]

### Types
- **Type**: typing.Optional[typing.List[str]]


# FindingProviderFieldsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingProviderSeverity

### Label
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']]

### Original
- **Type**: typing.Optional[str]


# FirewallPolicyDetails

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatefulRuleGroupReferencesDetails]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessCustomActionsDetailsUnion]]

### StatelessDefaultActions
- **Type**: typing.Optional[typing.Sequence[str]]

### StatelessFragmentDefaultActions
- **Type**: typing.Optional[typing.Sequence[str]]

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessRuleGroupReferencesDetails]]


# FirewallPolicyDetailsOutput

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatefulRuleGroupReferencesDetails]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessCustomActionsDetailsOutput]]

### StatelessDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessFragmentDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessRuleGroupReferencesDetails]]


# FirewallPolicyDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FirewallPolicyStatefulRuleGroupReferencesDetails

### ResourceArn
- **Type**: typing.Optional[str]


# FirewallPolicyStatelessCustomActionsDetails

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionUnion]

### ActionName
- **Type**: typing.Optional[str]


# FirewallPolicyStatelessCustomActionsDetailsOutput

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionOutput]

### ActionName
- **Type**: typing.Optional[str]


# FirewallPolicyStatelessCustomActionsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FirewallPolicyStatelessRuleGroupReferencesDetails

### Priority
- **Type**: typing.Optional[int]

### ResourceArn
- **Type**: typing.Optional[str]


# GeneratorDetails

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]


# GeneratorDetailsOutput

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.List[str]]


# GeneratorDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GeoLocation

### Lon
- **Type**: typing.Optional[float]

### Lat
- **Type**: typing.Optional[float]


# GetAdministratorAccountResponse

### Administrator
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.Invitation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigurationPolicyAssociationRequest

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.Target'>
- **Required**: Yes


# GetConfigurationPolicyAssociationResponse

### ConfigurationPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']
- **Required**: Yes

### AssociationType
- **Type**: typing.Literal['APPLIED', 'INHERITED']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCESS']
- **Required**: Yes

### AssociationStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigurationPolicyRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationPolicyResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnabledStandardsRequest

### StandardsSubscriptionArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetEnabledStandardsRequestPaginate

### StandardsSubscriptionArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# GetEnabledStandardsResponse

### StandardsSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFindingAggregatorRequest

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetFindingAggregatorResponse

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FindingAggregationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingHistoryRequest

### FindingIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifier'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.Timestamp]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetFindingHistoryRequestPaginate

### FindingIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifier'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.Timestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# GetFindingHistoryResponse

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FindingHistoryRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFindingsRequest

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersUnion]

### SortCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SortCriterion]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetFindingsRequestPaginate

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersUnion]

### SortCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SortCriterion]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# GetFindingsResponse

### Findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightResultsRequest

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInsightResultsResponse

### InsightResults
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.InsightResults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetInsightsRequest

### InsightArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetInsightsRequestPaginate

### InsightArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# GetInsightsResponse

### Insights
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Insight]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInvitationsCountResponse

### InvitationsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetMasterAccountResponse

### Master
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.Invitation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetMembersRequest

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetMembersResponse

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Member]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Result]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecurityControlDefinitionRequest

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSecurityControlDefinitionResponse

### SecurityControlDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# ImportFindingsError

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# IndicatorOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IndicatorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Insight

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersOutput'>
- **Required**: Yes

### GroupByAttribute
- **Type**: <class 'str'>
- **Required**: Yes


# InsightResultValue

### GroupByAttributeValue
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# InsightResults

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### GroupByAttribute
- **Type**: <class 'str'>
- **Required**: Yes

### ResultValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.InsightResultValue]
- **Required**: Yes


# IntegerConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# IntegerListConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[typing.List[int]]

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]

### MaxItems
- **Type**: typing.Optional[int]


# Invitation

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[datetime.datetime]

### MemberStatus
- **Type**: typing.Optional[str]


# InviteMembersRequest

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# InviteMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Result]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# IpFilter

### Cidr
- **Type**: typing.Optional[str]


# IpOrganizationDetails

### Asn
- **Type**: typing.Optional[int]

### AsnOrg
- **Type**: typing.Optional[str]

### Isp
- **Type**: typing.Optional[str]

### Org
- **Type**: typing.Optional[str]


# Ipv6CidrBlockAssociation

### AssociationId
- **Type**: typing.Optional[str]

### Ipv6CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockState
- **Type**: typing.Optional[str]


# KeywordFilter

### Value
- **Type**: typing.Optional[str]


# ListAutomationRulesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAutomationRulesResponse

### AutomationRulesMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationPoliciesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListConfigurationPoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListConfigurationPoliciesResponse

### ConfigurationPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationPolicyAssociationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AssociationFilters]


# ListConfigurationPolicyAssociationsRequestPaginate

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AssociationFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListConfigurationPolicyAssociationsResponse

### ConfigurationPolicyAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEnabledProductsForImportRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEnabledProductsForImportRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListEnabledProductsForImportResponse

### ProductSubscriptions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFindingAggregatorsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFindingAggregatorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListFindingAggregatorsResponse

### FindingAggregators
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FindingAggregator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListInvitationsResponse

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Invitation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersRequest

### OnlyAssociated
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMembersRequestPaginate

### OnlyAssociated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListMembersResponse

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Member]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListOrganizationAdminAccountsResponse

### AdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AdminAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityControlDefinitionsRequest

### StandardsArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityControlDefinitionsRequestPaginate

### StandardsArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListSecurityControlDefinitionsResponse

### SecurityControlDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStandardsControlAssociationsRequest

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStandardsControlAssociationsRequestPaginate

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfig]


# ListStandardsControlAssociationsResponse

### StandardsControlAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# LoadBalancerState

### Code
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# Malware

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MapFilter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Comparison
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS']]


# Member

### AccountId
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### MasterId
- **Type**: typing.Optional[str]

### AdministratorId
- **Type**: typing.Optional[str]

### MemberStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# Network

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkAutonomousSystem

### Name
- **Type**: typing.Optional[str]

### Number
- **Type**: typing.Optional[int]


# NetworkConnection

### Direction
- **Type**: typing.Optional[typing.Literal['INBOUND', 'OUTBOUND']]


# NetworkConnectionAction

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkEndpoint

### Id
- **Type**: typing.Optional[str]

### Ip
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkGeoLocation]

### AutonomousSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkAutonomousSystem]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkConnection]


# NetworkGeoLocation

### City
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### Lat
- **Type**: typing.Optional[float]

### Lon
- **Type**: typing.Optional[float]


# NetworkHeaderOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkHeaderUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkPathComponent

### ComponentId
- **Type**: typing.Optional[str]

### ComponentType
- **Type**: typing.Optional[str]

### Egress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderUnion]

### Ingress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderUnion]


# NetworkPathComponentDetails

### Address
- **Type**: typing.Optional[typing.Sequence[str]]

### PortRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.PortRange]]


# NetworkPathComponentDetailsOutput

### Address
- **Type**: typing.Optional[typing.List[str]]

### PortRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PortRange]]


# NetworkPathComponentOutput

### ComponentId
- **Type**: typing.Optional[str]

### ComponentType
- **Type**: typing.Optional[str]

### Egress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderOutput]

### Ingress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderOutput]


# NetworkPathComponentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Note

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NoteUpdate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NumberFilter

### Gte
- **Type**: typing.Optional[float]

### Lte
- **Type**: typing.Optional[float]

### Eq
- **Type**: typing.Optional[float]

### Gt
- **Type**: typing.Optional[float]

### Lt
- **Type**: typing.Optional[float]


# Occurrences

### LineRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Range]]

### OffsetRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Range]]

### Pages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Page]]

### Records
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Record]]

### Cells
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Cell]]


# OccurrencesOutput

### LineRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Range]]

### OffsetRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Range]]

### Pages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Page]]

### Records
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Record]]

### Cells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Cell]]


# OccurrencesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationConfiguration

### ConfigurationType
- **Type**: typing.Optional[typing.Literal['CENTRAL', 'LOCAL']]

### Status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'FAILED', 'PENDING']]

### StatusMessage
- **Type**: typing.Optional[str]


# Page

### PageNumber
- **Type**: typing.Optional[int]

### LineRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.Range]

### OffsetRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.Range]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterConfiguration

### ValueType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ParameterValueUnion]


# ParameterConfigurationOutput

### ValueType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ParameterValueOutput]


# ParameterConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterDefinition

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationOptions'>
- **Required**: Yes


# ParameterValue

### Integer
- **Type**: typing.Optional[int]

### IntegerList
- **Type**: typing.Optional[typing.Sequence[int]]

### Double
- **Type**: typing.Optional[float]

### String
- **Type**: typing.Optional[str]

### StringList
- **Type**: typing.Optional[typing.Sequence[str]]

### Boolean
- **Type**: typing.Optional[bool]

### Enum
- **Type**: typing.Optional[str]

### EnumList
- **Type**: typing.Optional[typing.Sequence[str]]


# ParameterValueOutput

### Integer
- **Type**: typing.Optional[int]

### IntegerList
- **Type**: typing.Optional[typing.List[int]]

### Double
- **Type**: typing.Optional[float]

### String
- **Type**: typing.Optional[str]

### StringList
- **Type**: typing.Optional[typing.List[str]]

### Boolean
- **Type**: typing.Optional[bool]

### Enum
- **Type**: typing.Optional[str]

### EnumList
- **Type**: typing.Optional[typing.List[str]]


# ParameterValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PatchSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstalledCount
- **Type**: typing.Optional[int]

### MissingCount
- **Type**: typing.Optional[int]

### FailedCount
- **Type**: typing.Optional[int]

### InstalledOtherCount
- **Type**: typing.Optional[int]

### InstalledRejectedCount
- **Type**: typing.Optional[int]

### InstalledPendingReboot
- **Type**: typing.Optional[int]

### OperationStartTime
- **Type**: typing.Optional[str]

### OperationEndTime
- **Type**: typing.Optional[str]

### RebootOption
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]


# Policy

### SecurityHub
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SecurityHubPolicy]


# PolicyOutput

### SecurityHub
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SecurityHubPolicyOutput]


# PolicyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PortProbeAction

### PortProbeDetails
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeDetail]]

### Blocked
- **Type**: typing.Optional[bool]


# PortProbeActionOutput

### PortProbeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeDetail]]

### Blocked
- **Type**: typing.Optional[bool]


# PortProbeActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PortProbeDetail

### LocalPortDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionLocalPortDetails]

### LocalIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionLocalIpDetails]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionRemoteIpDetails]


# PortRange

### Begin
- **Type**: typing.Optional[int]

### End
- **Type**: typing.Optional[int]


# PortRangeFromTo

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]


# ProcessDetails

### Name
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Pid
- **Type**: typing.Optional[int]

### ParentPid
- **Type**: typing.Optional[int]

### LaunchedAt
- **Type**: typing.Optional[str]

### TerminatedAt
- **Type**: typing.Optional[str]


# Product

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProductName
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Categories
- **Type**: typing.Optional[typing.List[str]]

### IntegrationTypes
- **Type**: typing.Optional[typing.List[typing.Literal['RECEIVE_FINDINGS_FROM_SECURITY_HUB', 'SEND_FINDINGS_TO_SECURITY_HUB', 'UPDATE_FINDINGS_IN_SECURITY_HUB']]]

### MarketplaceUrl
- **Type**: typing.Optional[str]

### ActivationUrl
- **Type**: typing.Optional[str]

### ProductSubscriptionResourcePolicy
- **Type**: typing.Optional[str]


# PropagatingVgwSetDetails

### GatewayId
- **Type**: typing.Optional[str]


# Range

### Start
- **Type**: typing.Optional[int]

### End
- **Type**: typing.Optional[int]

### StartColumn
- **Type**: typing.Optional[int]


# Recommendation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Record

### JsonPath
- **Type**: typing.Optional[str]

### RecordIndex
- **Type**: typing.Optional[int]


# RelatedFinding

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# Remediation

### Recommendation
- **Type**: <class 'NoneType'>


# ResourceOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# Result

### AccountId
- **Type**: typing.Optional[str]

### ProcessingResult
- **Type**: typing.Optional[str]


# RouteSetDetails

### CarrierGatewayId
- **Type**: typing.Optional[str]

### CoreNetworkArn
- **Type**: typing.Optional[str]

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### DestinationIpv6CidrBlock
- **Type**: typing.Optional[str]

### DestinationPrefixListId
- **Type**: typing.Optional[str]

### EgressOnlyInternetGatewayId
- **Type**: typing.Optional[str]

### GatewayId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceOwnerId
- **Type**: typing.Optional[str]

### LocalGatewayId
- **Type**: typing.Optional[str]

### NatGatewayId
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### Origin
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### TransitGatewayId
- **Type**: typing.Optional[str]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# RuleGroupDetails

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesUnion]

### RulesSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceUnion]


# RuleGroupDetailsOutput

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesOutput]

### RulesSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceOutput]


# RuleGroupSource

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceListDetailsUnion]

### RulesString
- **Type**: typing.Optional[str]

### StatefulRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesDetailsUnion]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnion]


# RuleGroupSourceCustomActionsDetails

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionUnion]

### ActionName
- **Type**: typing.Optional[str]


# RuleGroupSourceCustomActionsDetailsOutput

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionOutput]

### ActionName
- **Type**: typing.Optional[str]


# RuleGroupSourceCustomActionsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceListDetails

### GeneratedRulesType
- **Type**: typing.Optional[str]

### TargetTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Targets
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupSourceListDetailsOutput

### GeneratedRulesType
- **Type**: typing.Optional[str]

### TargetTypes
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceListDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceOutput

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceListDetailsOutput]

### RulesString
- **Type**: typing.Optional[str]

### StatefulRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesDetailsOutput]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutput]


# RuleGroupSourceStatefulRulesDetails

### Action
- **Type**: typing.Optional[str]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesHeaderDetails]

### RuleOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesOptionsDetailsUnion]]


# RuleGroupSourceStatefulRulesDetailsOutput

### Action
- **Type**: typing.Optional[str]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesHeaderDetails]

### RuleOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesOptionsDetailsOutput]]


# RuleGroupSourceStatefulRulesDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceStatefulRulesHeaderDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceStatefulRulesOptionsDetails

### Keyword
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupSourceStatefulRulesOptionsDetailsOutput

### Keyword
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceStatefulRulesOptionsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceStatelessRuleDefinition

### Actions
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesUnion]


# RuleGroupSourceStatelessRuleDefinitionOutput

### Actions
- **Type**: typing.Optional[typing.List[str]]

### MatchAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesOutput]


# RuleGroupSourceStatelessRuleDefinitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceStatelessRuleMatchAttributes

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinations]]

### Protocols
- **Type**: typing.Optional[typing.Sequence[int]]

### SourcePorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcePorts]]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSources]]

### TcpFlags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnion]]


# RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]


# RuleGroupSourceStatelessRuleMatchAttributesDestinations

### AddressDefinition
- **Type**: typing.Optional[str]


# RuleGroupSourceStatelessRuleMatchAttributesOutput

### DestinationPorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinations]]

### Protocols
- **Type**: typing.Optional[typing.List[int]]

### SourcePorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcePorts]]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSources]]

### TcpFlags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutput]]


# RuleGroupSourceStatelessRuleMatchAttributesSourcePorts

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]


# RuleGroupSourceStatelessRuleMatchAttributesSources

### AddressDefinition
- **Type**: typing.Optional[str]


# RuleGroupSourceStatelessRuleMatchAttributesTcpFlags

### Flags
- **Type**: typing.Optional[typing.Sequence[str]]

### Masks
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutput

### Flags
- **Type**: typing.Optional[typing.List[str]]

### Masks
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceStatelessRuleMatchAttributesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceStatelessRulesAndCustomActionsDetails

### CustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceCustomActionsDetailsUnion]]

### StatelessRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesDetailsUnion]]


# RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutput

### CustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceCustomActionsDetailsOutput]]

### StatelessRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesDetailsOutput]]


# RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceStatelessRulesDetails

### Priority
- **Type**: typing.Optional[int]

### RuleDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleDefinitionUnion]


# RuleGroupSourceStatelessRulesDetailsOutput

### Priority
- **Type**: typing.Optional[int]

### RuleDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleDefinitionOutput]


# RuleGroupSourceStatelessRulesDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSourceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupVariables

### IpSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesIpSetsDetailsUnion]

### PortSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesPortSetsDetailsUnion]


# RuleGroupVariablesIpSetsDetails

### Definition
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupVariablesIpSetsDetailsOutput

### Definition
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupVariablesIpSetsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupVariablesOutput

### IpSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesIpSetsDetailsOutput]

### PortSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesPortSetsDetailsOutput]


# RuleGroupVariablesPortSetsDetails

### Definition
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupVariablesPortSetsDetailsOutput

### Definition
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupVariablesPortSetsDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupVariablesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityControl

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RemediationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SeverityRating
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes

### SecurityControlStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['READY', 'UPDATING']]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationOutput]]

### LastUpdateReason
- **Type**: typing.Optional[str]


# SecurityControlCustomParameter

### SecurityControlId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfiguration]]


# SecurityControlCustomParameterOutput

### SecurityControlId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationOutput]]


# SecurityControlDefinition

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RemediationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SeverityRating
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes

### CurrentRegionAvailability
- **Type**: typing.Literal['AVAILABLE', 'UNAVAILABLE']
- **Required**: Yes

### CustomizableProperties
- **Type**: typing.Optional[typing.List[typing.Literal['Parameters']]]

### ParameterDefinitions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterDefinition]]


# SecurityControlParameter

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[typing.Sequence[str]]


# SecurityControlParameterOutput

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[typing.List[str]]


# SecurityControlParameterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityControlsConfiguration

### EnabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### DisabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityControlCustomParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlCustomParameter]]


# SecurityControlsConfigurationOutput

### EnabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DisabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### SecurityControlCustomParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlCustomParameterOutput]]


# SecurityHubPolicy

### ServiceEnabled
- **Type**: typing.Optional[bool]

### EnabledStandardIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityControlsConfiguration
- **Type**: <class 'NoneType'>


# SecurityHubPolicyOutput

### ServiceEnabled
- **Type**: typing.Optional[bool]

### EnabledStandardIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### SecurityControlsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlsConfigurationOutput]


# SensitiveDataDetectionsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SensitiveDataDetectionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SensitiveDataResult

### Category
- **Type**: typing.Optional[str]

### Detections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataDetectionsUnion]]

### TotalCount
- **Type**: typing.Optional[int]


# SensitiveDataResultOutput

### Category
- **Type**: typing.Optional[str]

### Detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataDetectionsOutput]]

### TotalCount
- **Type**: typing.Optional[int]


# SensitiveDataResultUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SequenceOutput

### Uid
- **Type**: typing.Optional[str]

### Actors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Actor]]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NetworkEndpoint]]

### Signals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SignalOutput]]

### SequenceIndicators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IndicatorOutput]]


# SequenceType

### Uid
- **Type**: typing.Optional[str]

### Actors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Actor]]

### Endpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NetworkEndpoint]]

### Signals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SignalUnion]]

### SequenceIndicators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.IndicatorUnion]]


# Severity

### Product
- **Type**: typing.Optional[float]

### Label
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']]

### Normalized
- **Type**: typing.Optional[int]

### Original
- **Type**: typing.Optional[str]


# SeverityUpdate

### Normalized
- **Type**: typing.Optional[int]

### Product
- **Type**: typing.Optional[float]

### Label
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']]


# SignalOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SoftwarePackage

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Epoch
- **Type**: typing.Optional[str]

### Release
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### PackageManager
- **Type**: typing.Optional[str]

### FilePath
- **Type**: typing.Optional[str]

### FixedInVersion
- **Type**: typing.Optional[str]

### Remediation
- **Type**: typing.Optional[str]

### SourceLayerHash
- **Type**: typing.Optional[str]

### SourceLayerArn
- **Type**: typing.Optional[str]


# SortCriterion

### Field
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'desc']]


# Standard

### StandardsArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EnabledByDefault
- **Type**: typing.Optional[bool]

### StandardsManagedBy
- **Type**: <class 'NoneType'>


# StandardsControl

### StandardsControlArn
- **Type**: typing.Optional[str]

### ControlStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DisabledReason
- **Type**: typing.Optional[str]

### ControlStatusUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ControlId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RemediationUrl
- **Type**: typing.Optional[str]

### SeverityRating
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM']]

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]


# StandardsControlAssociationDetail

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedReason
- **Type**: typing.Optional[str]

### StandardsControlTitle
- **Type**: typing.Optional[str]

### StandardsControlDescription
- **Type**: typing.Optional[str]

### StandardsControlArns
- **Type**: typing.Optional[typing.List[str]]


# StandardsControlAssociationId

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes


# StandardsControlAssociationSummary

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedReason
- **Type**: typing.Optional[str]

### StandardsControlTitle
- **Type**: typing.Optional[str]

### StandardsControlDescription
- **Type**: typing.Optional[str]


# StandardsControlAssociationUpdate

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### UpdatedReason
- **Type**: typing.Optional[str]


# StandardsManagedBy

### Company
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# StandardsStatusReason

### StatusReasonCode
- **Type**: typing.Literal['INTERNAL_ERROR', 'MAXIMUM_NUMBER_OF_CONFIG_RULES_EXCEEDED', 'NO_AVAILABLE_CONFIGURATION_RECORDER']
- **Required**: Yes


# StandardsSubscription

### StandardsSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsInput
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### StandardsStatus
- **Type**: typing.Literal['DELETING', 'FAILED', 'INCOMPLETE', 'PENDING', 'READY']
- **Required**: Yes

### StandardsControlsUpdatable
- **Type**: typing.Optional[typing.Literal['NOT_READY_FOR_UPDATES', 'READY_FOR_UPDATES']]

### StandardsStatusReason
- **Type**: <class 'NoneType'>


# StandardsSubscriptionRequest

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsInput
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartConfigurationPolicyAssociationRequest

### ConfigurationPolicyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.Target'>
- **Required**: Yes


# StartConfigurationPolicyAssociationResponse

### ConfigurationPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']
- **Required**: Yes

### AssociationType
- **Type**: typing.Literal['APPLIED', 'INHERITED']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCESS']
- **Required**: Yes

### AssociationStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# StartConfigurationPolicyDisassociationRequest

### ConfigurationPolicyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'NoneType'>


# StatelessCustomActionDefinition

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionUnion]


# StatelessCustomActionDefinitionOutput

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionOutput]


# StatelessCustomActionDefinitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatelessCustomPublishMetricAction

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionDimension]]


# StatelessCustomPublishMetricActionDimension

### Value
- **Type**: typing.Optional[str]


# StatelessCustomPublishMetricActionOutput

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionDimension]]


# StatelessCustomPublishMetricActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatusReason

### ReasonCode
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# StringConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[str]

### Re2Expression
- **Type**: typing.Optional[str]

### ExpressionDescription
- **Type**: typing.Optional[str]


# StringFilter

### Value
- **Type**: typing.Optional[str]

### Comparison
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS', 'PREFIX', 'PREFIX_NOT_EQUALS']]


# StringListConfigurationOptions

### DefaultValue
- **Type**: typing.Optional[typing.List[str]]

### Re2Expression
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### ExpressionDescription
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Target

### AccountId
- **Type**: typing.Optional[str]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### RootId
- **Type**: typing.Optional[str]


# Threat

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### FilePaths
- **Type**: typing.Optional[typing.Sequence[NoneType]]


# ThreatIntelIndicator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThreatOutput

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### FilePaths
- **Type**: typing.Optional[typing.List[NoneType]]


# ThreatUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnprocessedAutomationRule

### RuleArn
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[int]

### ErrorMessage
- **Type**: typing.Optional[str]


# UnprocessedConfigurationPolicyAssociation

### ConfigurationPolicyAssociationIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociation]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorReason
- **Type**: typing.Optional[str]


# UnprocessedSecurityControl

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'INVALID_INPUT', 'LIMIT_EXCEEDED', 'NOT_FOUND']
- **Required**: Yes

### ErrorReason
- **Type**: typing.Optional[str]


# UnprocessedStandardsControlAssociation

### StandardsControlAssociationId
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationId'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'INVALID_INPUT', 'LIMIT_EXCEEDED', 'NOT_FOUND']
- **Required**: Yes

### ErrorReason
- **Type**: typing.Optional[str]


# UnprocessedStandardsControlAssociationUpdate

### StandardsControlAssociationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationUpdate'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'INVALID_INPUT', 'LIMIT_EXCEEDED', 'NOT_FOUND']
- **Required**: Yes

### ErrorReason
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateActionTargetRequest

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateAutomationRulesRequestItem

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RuleOrder
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### IsTerminal
- **Type**: typing.Optional[bool]

### Criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFiltersUnion]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesActionUnion]]


# UpdateConfigurationPolicyRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UpdatedReason
- **Type**: typing.Optional[str]

### ConfigurationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PolicyUnion]


# UpdateConfigurationPolicyResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFindingAggregatorRequest

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateFindingAggregatorResponse

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FindingAggregationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFindingsRequest

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersUnion'>
- **Required**: Yes

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdate]

### RecordState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# UpdateInsightRequest

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersUnion]

### GroupByAttribute
- **Type**: typing.Optional[str]


# UpdateOrganizationConfigurationRequest

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoEnableStandards
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NONE']]

### OrganizationConfiguration
- **Type**: <class 'NoneType'>


# UpdateSecurityControlRequest

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationUnion]
- **Required**: Yes

### LastUpdateReason
- **Type**: typing.Optional[str]


# UpdateSecurityHubConfigurationRequest

### AutoEnableControls
- **Type**: typing.Optional[bool]

### ControlFindingGenerator
- **Type**: typing.Optional[typing.Literal['SECURITY_CONTROL', 'STANDARD_CONTROL']]


# UpdateStandardsControlRequest

### StandardsControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### ControlStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DisabledReason
- **Type**: typing.Optional[str]


# UserAccount

### Uid
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# VolumeMount

### Name
- **Type**: typing.Optional[str]

### MountPath
- **Type**: typing.Optional[str]


# VpcInfoCidrBlockSetDetails

### CidrBlock
- **Type**: typing.Optional[str]


# VpcInfoIpv6CidrBlockSetDetails

### Ipv6CidrBlock
- **Type**: typing.Optional[str]


# VpcInfoPeeringOptionsDetails

### AllowDnsResolutionFromRemoteVpc
- **Type**: typing.Optional[bool]

### AllowEgressFromLocalClassicLinkToRemoteVpc
- **Type**: typing.Optional[bool]

### AllowEgressFromLocalVpcToRemoteClassicLink
- **Type**: typing.Optional[bool]


# Vulnerability

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### VulnerablePackages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SoftwarePackage]]

### Cvss
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.CvssUnion]]

### RelatedVulnerabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### Vendor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityVendor]

### ReferenceUrls
- **Type**: typing.Optional[typing.Sequence[str]]

### FixAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'PARTIAL', 'YES']]

### EpssScore
- **Type**: typing.Optional[float]

### ExploitAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### LastKnownExploitAt
- **Type**: typing.Optional[str]

### CodeVulnerabilities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityCodeVulnerabilitiesUnion]]


# VulnerabilityCodeVulnerabilities

### Cwes
- **Type**: typing.Optional[typing.Sequence[str]]

### FilePath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CodeVulnerabilitiesFilePath]

### SourceArn
- **Type**: typing.Optional[str]


# VulnerabilityCodeVulnerabilitiesOutput

### Cwes
- **Type**: typing.Optional[typing.List[str]]

### FilePath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CodeVulnerabilitiesFilePath]

### SourceArn
- **Type**: typing.Optional[str]


# VulnerabilityCodeVulnerabilitiesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VulnerabilityOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### VulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SoftwarePackage]]

### Cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CvssOutput]]

### RelatedVulnerabilities
- **Type**: typing.Optional[typing.List[str]]

### Vendor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityVendor]

### ReferenceUrls
- **Type**: typing.Optional[typing.List[str]]

### FixAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'PARTIAL', 'YES']]

### EpssScore
- **Type**: typing.Optional[float]

### ExploitAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### LastKnownExploitAt
- **Type**: typing.Optional[str]

### CodeVulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityCodeVulnerabilitiesOutput]]


# VulnerabilityUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VulnerabilityVendor

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: typing.Optional[str]

### VendorSeverity
- **Type**: typing.Optional[str]

### VendorCreatedAt
- **Type**: typing.Optional[str]

### VendorUpdatedAt
- **Type**: typing.Optional[str]


# WafExcludedRule

### RuleId
- **Type**: typing.Optional[str]


# Workflow

### Status
- **Type**: typing.Optional[typing.Literal['NEW', 'NOTIFIED', 'RESOLVED', 'SUPPRESSED']]


# WorkflowUpdate

### Status
- **Type**: typing.Optional[typing.Literal['NEW', 'NOTIFIED', 'RESOLVED', 'SUPPRESSED']]


