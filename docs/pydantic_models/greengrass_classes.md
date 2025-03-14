# Greengrass Classes

# AssociateRoleToGroupRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateRoleToGroupResponseTypeDef

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateServiceRoleToAccountRequestTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateServiceRoleToAccountResponseTypeDef

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BulkDeploymentMetricsTypeDef

### InvalidInputRecords
- **Type**: typing.Optional[int]

### RecordsProcessed
- **Type**: typing.Optional[int]

### RetryAttempts
- **Type**: typing.Optional[int]


# BulkDeploymentResultTypeDef

### CreatedAt
- **Type**: typing.Optional[str]

### DeploymentArn
- **Type**: typing.Optional[str]

### DeploymentId
- **Type**: typing.Optional[str]

### DeploymentStatus
- **Type**: typing.Optional[str]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['ForceResetDeployment', 'NewDeployment', 'Redeployment', 'ResetDeployment']]

### ErrorDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.ErrorDetailTypeDef]]

### ErrorMessage
- **Type**: typing.Optional[str]

### GroupArn
- **Type**: typing.Optional[str]


# BulkDeploymentTypeDef

### BulkDeploymentArn
- **Type**: typing.Optional[str]

### BulkDeploymentId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]


# ConnectivityInfoTypeDef

### HostAddress
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### PortNumber
- **Type**: typing.Optional[int]


# ConnectorDefinitionVersionOutputTypeDef

### Connectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.ConnectorOutputTypeDef]]


# ConnectorDefinitionVersionTypeDef

### Connectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ConnectorTypeDef]]


# ConnectorDefinitionVersionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectorOutputTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConnectorTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ConnectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreDefinitionVersionOutputTypeDef

### Cores
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.CoreTypeDef]]


# CoreDefinitionVersionTypeDef

### Cores
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.CoreTypeDef]]


# CoreDefinitionVersionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes

### SyncShadow
- **Type**: typing.Optional[bool]


# CreateConnectorDefinitionRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.ConnectorDefinitionVersionUnionTypeDef]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConnectorDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectorDefinitionVersionRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Connectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ConnectorUnionTypeDef]]


# CreateConnectorDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCoreDefinitionRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.CoreDefinitionVersionUnionTypeDef]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCoreDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCoreDefinitionVersionRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Cores
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.CoreTypeDef]]


# CreateCoreDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentRequestTypeDef

### DeploymentType
- **Type**: typing.Literal['ForceResetDeployment', 'NewDeployment', 'Redeployment', 'ResetDeployment']
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### DeploymentId
- **Type**: typing.Optional[str]

### GroupVersionId
- **Type**: typing.Optional[str]


# CreateDeploymentResponseTypeDef

### DeploymentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeviceDefinitionRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.DeviceDefinitionVersionUnionTypeDef]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeviceDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeviceDefinitionVersionRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.DeviceTypeDef]]


# CreateDeviceDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFunctionDefinitionRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefinitionVersionUnionTypeDef]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFunctionDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFunctionDefinitionVersionRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefaultConfigTypeDef]

### Functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.FunctionUnionTypeDef]]


# CreateFunctionDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupCertificateAuthorityRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]


# CreateGroupCertificateAuthorityResponseTypeDef

### GroupCertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.GroupVersionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupVersionRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### ConnectorDefinitionVersionArn
- **Type**: typing.Optional[str]

### CoreDefinitionVersionArn
- **Type**: typing.Optional[str]

### DeviceDefinitionVersionArn
- **Type**: typing.Optional[str]

### FunctionDefinitionVersionArn
- **Type**: typing.Optional[str]

### LoggerDefinitionVersionArn
- **Type**: typing.Optional[str]

### ResourceDefinitionVersionArn
- **Type**: typing.Optional[str]

### SubscriptionDefinitionVersionArn
- **Type**: typing.Optional[str]


# CreateGroupVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoggerDefinitionRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.LoggerDefinitionVersionUnionTypeDef]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLoggerDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoggerDefinitionVersionRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Loggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.LoggerTypeDef]]


# CreateLoggerDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceDefinitionRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.ResourceDefinitionVersionUnionTypeDef]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateResourceDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceDefinitionVersionRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ResourceUnionTypeDef]]


# CreateResourceDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSoftwareUpdateJobRequestTypeDef

### S3UrlSignerRole
- **Type**: <class 'str'>
- **Required**: Yes

### SoftwareToUpdate
- **Type**: typing.Literal['core', 'ota_agent']
- **Required**: Yes

### UpdateTargets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UpdateTargetsArchitecture
- **Type**: typing.Literal['aarch64', 'armv6l', 'armv7l', 'x86_64']
- **Required**: Yes

### UpdateTargetsOperatingSystem
- **Type**: typing.Literal['amazon_linux', 'openwrt', 'raspbian', 'ubuntu']
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### UpdateAgentLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'FATAL', 'INFO', 'NONE', 'TRACE', 'VERBOSE', 'WARN']]


# CreateSoftwareUpdateJobResponseTypeDef

### IotJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### IotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformSoftwareVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriptionDefinitionRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionDefinitionVersionUnionTypeDef]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSubscriptionDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriptionDefinitionVersionRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionTypeDef]]


# CreateSubscriptionDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefinitionInformationTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LastUpdatedTimestamp
- **Type**: typing.Optional[str]

### LatestVersion
- **Type**: typing.Optional[str]

### LatestVersionArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeleteConnectorDefinitionRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCoreDefinitionRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceDefinitionRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionDefinitionRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoggerDefinitionRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceDefinitionRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionDefinitionRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentTypeDef

### CreatedAt
- **Type**: typing.Optional[str]

### DeploymentArn
- **Type**: typing.Optional[str]

### DeploymentId
- **Type**: typing.Optional[str]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['ForceResetDeployment', 'NewDeployment', 'Redeployment', 'ResetDeployment']]

### GroupArn
- **Type**: typing.Optional[str]


# DeviceDefinitionVersionOutputTypeDef

### Devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DeviceTypeDef]]


# DeviceDefinitionVersionTypeDef

### Devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.DeviceTypeDef]]


# DeviceDefinitionVersionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes

### SyncShadow
- **Type**: typing.Optional[bool]


# DisassociateRoleFromGroupRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateRoleFromGroupResponseTypeDef

### DisassociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateServiceRoleFromAccountResponseTypeDef

### DisassociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ErrorDetailTypeDef

### DetailedErrorCode
- **Type**: typing.Optional[str]

### DetailedErrorMessage
- **Type**: typing.Optional[str]


# FunctionConfigurationEnvironmentOutputTypeDef

### AccessSysfs
- **Type**: typing.Optional[bool]

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionExecutionConfigTypeDef]

### ResourceAccessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.ResourceAccessPolicyTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]


# FunctionConfigurationEnvironmentTypeDef

### AccessSysfs
- **Type**: typing.Optional[bool]

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionExecutionConfigTypeDef]

### ResourceAccessPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ResourceAccessPolicyTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FunctionConfigurationEnvironmentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionConfigurationOutputTypeDef

### EncodingType
- **Type**: typing.Optional[typing.Literal['binary', 'json']]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionConfigurationEnvironmentOutputTypeDef]

### ExecArgs
- **Type**: typing.Optional[str]

### Executable
- **Type**: typing.Optional[str]

### MemorySize
- **Type**: typing.Optional[int]

### Pinned
- **Type**: typing.Optional[bool]

### Timeout
- **Type**: typing.Optional[int]

### FunctionRuntimeOverride
- **Type**: typing.Optional[str]


# FunctionConfigurationTypeDef

### EncodingType
- **Type**: typing.Optional[typing.Literal['binary', 'json']]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionConfigurationEnvironmentUnionTypeDef]

### ExecArgs
- **Type**: typing.Optional[str]

### Executable
- **Type**: typing.Optional[str]

### MemorySize
- **Type**: typing.Optional[int]

### Pinned
- **Type**: typing.Optional[bool]

### Timeout
- **Type**: typing.Optional[int]

### FunctionRuntimeOverride
- **Type**: typing.Optional[str]


# FunctionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionDefaultConfigTypeDef

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefaultExecutionConfigTypeDef]


# FunctionDefaultExecutionConfigTypeDef

### IsolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### RunAs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionRunAsConfigTypeDef]


# FunctionDefinitionVersionOutputTypeDef

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefaultConfigTypeDef]

### Functions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.FunctionOutputTypeDef]]


# FunctionDefinitionVersionTypeDef

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefaultConfigTypeDef]

### Functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.FunctionTypeDef]]


# FunctionDefinitionVersionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionExecutionConfigTypeDef

### IsolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### RunAs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionRunAsConfigTypeDef]


# FunctionOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: typing.Optional[str]

### FunctionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionConfigurationOutputTypeDef]


# FunctionRunAsConfigTypeDef

### Gid
- **Type**: typing.Optional[int]

### Uid
- **Type**: typing.Optional[int]


# FunctionTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: typing.Optional[str]

### FunctionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionConfigurationUnionTypeDef]


# FunctionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAssociatedRoleRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssociatedRoleResponseTypeDef

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBulkDeploymentStatusRequestTypeDef

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBulkDeploymentStatusResponseTypeDef

### BulkDeploymentMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.BulkDeploymentMetricsTypeDef'>
- **Required**: Yes

### BulkDeploymentStatus
- **Type**: typing.Literal['Completed', 'Failed', 'Initializing', 'Running', 'Stopped', 'Stopping']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.ErrorDetailTypeDef]
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectivityInfoRequestTypeDef

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectivityInfoResponseTypeDef

### ConnectivityInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.ConnectivityInfoTypeDef]
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectorDefinitionRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectorDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectorDefinitionVersionRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetConnectorDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ConnectorDefinitionVersionOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreDefinitionRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCoreDefinitionVersionRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.CoreDefinitionVersionOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDeploymentStatusRequestTypeDef

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentStatusResponseTypeDef

### DeploymentStatus
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentType
- **Type**: typing.Literal['ForceResetDeployment', 'NewDeployment', 'Redeployment', 'ResetDeployment']
- **Required**: Yes

### ErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.ErrorDetailTypeDef]
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceDefinitionRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceDefinitionVersionRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDeviceDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.DeviceDefinitionVersionOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFunctionDefinitionRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionDefinitionVersionRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFunctionDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefinitionVersionOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetGroupCertificateAuthorityRequestTypeDef

### CertificateAuthorityId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupCertificateAuthorityResponseTypeDef

### GroupCertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### GroupCertificateAuthorityId
- **Type**: <class 'str'>
- **Required**: Yes

### PemEncodedCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupCertificateConfigurationRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupCertificateConfigurationResponseTypeDef

### CertificateAuthorityExpiryInMilliseconds
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateExpiryInMilliseconds
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupVersionRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.GroupVersionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoggerDefinitionRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggerDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoggerDefinitionVersionRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### LoggerDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLoggerDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.LoggerDefinitionVersionOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceDefinitionRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceDefinitionVersionRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResourceDefinitionVersionOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceRoleForAccountResponseTypeDef

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionDefinitionRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionDefinitionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionDefinitionVersionRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSubscriptionDefinitionVersionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionDefinitionVersionOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetThingRuntimeConfigurationRequestTypeDef

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetThingRuntimeConfigurationResponseTypeDef

### RuntimeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.RuntimeConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupCertificateAuthorityPropertiesTypeDef

### GroupCertificateAuthorityArn
- **Type**: typing.Optional[str]

### GroupCertificateAuthorityId
- **Type**: typing.Optional[str]


# GroupInformationTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LastUpdatedTimestamp
- **Type**: typing.Optional[str]

### LatestVersion
- **Type**: typing.Optional[str]

### LatestVersionArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# GroupOwnerSettingTypeDef

### AutoAddGroupOwner
- **Type**: typing.Optional[bool]

### GroupOwner
- **Type**: typing.Optional[str]


# GroupVersionTypeDef

### ConnectorDefinitionVersionArn
- **Type**: typing.Optional[str]

### CoreDefinitionVersionArn
- **Type**: typing.Optional[str]

### DeviceDefinitionVersionArn
- **Type**: typing.Optional[str]

### FunctionDefinitionVersionArn
- **Type**: typing.Optional[str]

### LoggerDefinitionVersionArn
- **Type**: typing.Optional[str]

### ResourceDefinitionVersionArn
- **Type**: typing.Optional[str]

### SubscriptionDefinitionVersionArn
- **Type**: typing.Optional[str]


# ListBulkDeploymentDetailedReportsRequestPaginateTypeDef

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListBulkDeploymentDetailedReportsRequestTypeDef

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListBulkDeploymentDetailedReportsResponseTypeDef

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.BulkDeploymentResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBulkDeploymentsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListBulkDeploymentsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListBulkDeploymentsResponseTypeDef

### BulkDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.BulkDeploymentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionVersionsRequestPaginateTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListConnectorDefinitionVersionsRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListConnectorDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionVersionsRequestPaginateTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListCoreDefinitionVersionsRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListCoreDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestPaginateTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListDeploymentsRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentsResponseTypeDef

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DeploymentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionVersionsRequestPaginateTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListDeviceDefinitionVersionsRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListDeviceDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionVersionsRequestPaginateTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListFunctionDefinitionVersionsRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListFunctionDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupCertificateAuthoritiesRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# ListGroupCertificateAuthoritiesResponseTypeDef

### GroupCertificateAuthorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.GroupCertificateAuthorityPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupVersionsRequestPaginateTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListGroupVersionsRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.GroupInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionVersionsRequestPaginateTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListLoggerDefinitionVersionsRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListLoggerDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionVersionsRequestPaginateTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListResourceDefinitionVersionsRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListResourceDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionVersionsRequestPaginateTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListSubscriptionDefinitionVersionsRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListSubscriptionDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LocalDeviceResourceDataTypeDef

### GroupOwnerSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.GroupOwnerSettingTypeDef]

### SourcePath
- **Type**: typing.Optional[str]


# LocalVolumeResourceDataTypeDef

### DestinationPath
- **Type**: typing.Optional[str]

### GroupOwnerSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.GroupOwnerSettingTypeDef]

### SourcePath
- **Type**: typing.Optional[str]


# LoggerDefinitionVersionOutputTypeDef

### Loggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.LoggerTypeDef]]


# LoggerDefinitionVersionTypeDef

### Loggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.LoggerTypeDef]]


# LoggerDefinitionVersionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoggerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResetDeploymentsRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Force
- **Type**: typing.Optional[bool]


# ResetDeploymentsResponseTypeDef

### DeploymentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceAccessPolicyTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Permission
- **Type**: typing.Optional[typing.Literal['ro', 'rw']]


# ResourceDataContainerOutputTypeDef

### LocalDeviceResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.LocalDeviceResourceDataTypeDef]

### LocalVolumeResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.LocalVolumeResourceDataTypeDef]

### S3MachineLearningModelResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.S3MachineLearningModelResourceDataTypeDef]

### SageMakerMachineLearningModelResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.SageMakerMachineLearningModelResourceDataTypeDef]

### SecretsManagerSecretResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.SecretsManagerSecretResourceDataOutputTypeDef]


# ResourceDataContainerTypeDef

### LocalDeviceResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.LocalDeviceResourceDataTypeDef]

### LocalVolumeResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.LocalVolumeResourceDataTypeDef]

### S3MachineLearningModelResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.S3MachineLearningModelResourceDataTypeDef]

### SageMakerMachineLearningModelResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.SageMakerMachineLearningModelResourceDataTypeDef]

### SecretsManagerSecretResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.SecretsManagerSecretResourceDataUnionTypeDef]


# ResourceDataContainerUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceDefinitionVersionOutputTypeDef

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.ResourceOutputTypeDef]]


# ResourceDefinitionVersionTypeDef

### Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ResourceTypeDef]]


# ResourceDefinitionVersionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceDownloadOwnerSettingTypeDef

### GroupOwner
- **Type**: <class 'str'>
- **Required**: Yes

### GroupPermission
- **Type**: typing.Literal['ro', 'rw']
- **Required**: Yes


# ResourceOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDataContainer
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResourceDataContainerOutputTypeDef'>
- **Required**: Yes


# ResourceTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDataContainer
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResourceDataContainerUnionTypeDef'>
- **Required**: Yes


# ResourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadataTypeDef

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


# RuntimeConfigurationTypeDef

### TelemetryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.TelemetryConfigurationTypeDef]


# S3MachineLearningModelResourceDataTypeDef

### DestinationPath
- **Type**: typing.Optional[str]

### OwnerSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.ResourceDownloadOwnerSettingTypeDef]

### S3Uri
- **Type**: typing.Optional[str]


# SageMakerMachineLearningModelResourceDataTypeDef

### DestinationPath
- **Type**: typing.Optional[str]

### OwnerSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.ResourceDownloadOwnerSettingTypeDef]

### SageMakerJobArn
- **Type**: typing.Optional[str]


# SecretsManagerSecretResourceDataOutputTypeDef

### ARN
- **Type**: typing.Optional[str]

### AdditionalStagingLabelsToDownload
- **Type**: typing.Optional[typing.List[str]]


# SecretsManagerSecretResourceDataTypeDef

### ARN
- **Type**: typing.Optional[str]

### AdditionalStagingLabelsToDownload
- **Type**: typing.Optional[typing.Sequence[str]]


# SecretsManagerSecretResourceDataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartBulkDeploymentRequestTypeDef

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputFileUri
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartBulkDeploymentResponseTypeDef

### BulkDeploymentArn
- **Type**: <class 'str'>
- **Required**: Yes

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopBulkDeploymentRequestTypeDef

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# SubscriptionDefinitionVersionOutputTypeDef

### Subscriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionTypeDef]]


# SubscriptionDefinitionVersionTypeDef

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionTypeDef]]


# SubscriptionDefinitionVersionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubscriptionTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TelemetryConfigurationTypeDef

### Telemetry
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes

### ConfigurationSyncStatus
- **Type**: typing.Optional[typing.Literal['InSync', 'OutOfSync']]


# TelemetryConfigurationUpdateTypeDef

### Telemetry
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectivityInfoRequestTypeDef

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectivityInfo
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ConnectivityInfoTypeDef]]


# UpdateConnectivityInfoResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConnectorDefinitionRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateCoreDefinitionRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateDeviceDefinitionRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateFunctionDefinitionRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateGroupCertificateConfigurationRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateExpiryInMilliseconds
- **Type**: typing.Optional[str]


# UpdateGroupCertificateConfigurationResponseTypeDef

### CertificateAuthorityExpiryInMilliseconds
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateExpiryInMilliseconds
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGroupRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateLoggerDefinitionRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateResourceDefinitionRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateSubscriptionDefinitionRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateThingRuntimeConfigurationRequestTypeDef

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes

### TelemetryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.TelemetryConfigurationUpdateTypeDef]


# VersionInformationTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


