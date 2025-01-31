# Greengrass Classes

# AssociateRoleToGroupRequestRequestTypeDef

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


# AssociateServiceRoleToAccountRequestRequestTypeDef

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


# ConnectorDefinitionVersionTypeDef

### Connectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ConnectorTypeDef]]


# ConnectorTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CoreDefinitionVersionTypeDef

### Cores
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.CoreTypeDef]]


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


# CreateConnectorDefinitionRequestRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.ConnectorDefinitionVersionTypeDef]

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


# CreateConnectorDefinitionVersionRequestRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Connectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ConnectorTypeDef]]


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


# CreateCoreDefinitionRequestRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.CoreDefinitionVersionTypeDef]

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


# CreateCoreDefinitionVersionRequestRequestTypeDef

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


# CreateDeploymentRequestRequestTypeDef

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


# CreateDeviceDefinitionRequestRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.DeviceDefinitionVersionTypeDef]

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


# CreateDeviceDefinitionVersionRequestRequestTypeDef

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


# CreateFunctionDefinitionRequestRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefinitionVersionTypeDef]

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


# CreateFunctionDefinitionVersionRequestRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefaultConfigTypeDef]

### Functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.FunctionTypeDef]]


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


# CreateGroupCertificateAuthorityRequestRequestTypeDef

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


# CreateGroupRequestRequestTypeDef

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


# CreateGroupVersionRequestRequestTypeDef

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


# CreateLoggerDefinitionRequestRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.LoggerDefinitionVersionTypeDef]

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


# CreateLoggerDefinitionVersionRequestRequestTypeDef

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


# CreateResourceDefinitionRequestRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.ResourceDefinitionVersionTypeDef]

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


# CreateResourceDefinitionVersionRequestRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ResourceTypeDef]]


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


# CreateSoftwareUpdateJobRequestRequestTypeDef

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


# CreateSubscriptionDefinitionRequestRequestTypeDef

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionDefinitionVersionTypeDef]

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


# CreateSubscriptionDefinitionVersionRequestRequestTypeDef

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


# DeleteConnectorDefinitionRequestRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCoreDefinitionRequestRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceDefinitionRequestRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionDefinitionRequestRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoggerDefinitionRequestRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceDefinitionRequestRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionDefinitionRequestRequestTypeDef

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


# DeviceDefinitionVersionTypeDef

### Devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.DeviceTypeDef]]


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


# DisassociateRoleFromGroupRequestRequestTypeDef

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


# FunctionConfigurationEnvironmentTypeDef

### AccessSysfs
- **Type**: typing.Optional[bool]

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionExecutionConfigTypeDef]

### ResourceAccessPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ResourceAccessPolicyTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FunctionConfigurationTypeDef

### EncodingType
- **Type**: typing.Optional[typing.Literal['binary', 'json']]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionConfigurationEnvironmentTypeDef]

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


# FunctionDefaultConfigTypeDef

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefaultExecutionConfigTypeDef]


# FunctionDefaultExecutionConfigTypeDef

### IsolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### RunAs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionRunAsConfigTypeDef]


# FunctionDefinitionVersionTypeDef

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefaultConfigTypeDef]

### Functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.FunctionTypeDef]]


# FunctionExecutionConfigTypeDef

### IsolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### RunAs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionRunAsConfigTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.FunctionConfigurationTypeDef]


# GetAssociatedRoleRequestRequestTypeDef

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


# GetBulkDeploymentStatusRequestRequestTypeDef

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


# GetConnectivityInfoRequestRequestTypeDef

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


# GetConnectorDefinitionRequestRequestTypeDef

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


# GetConnectorDefinitionVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ConnectorDefinitionVersionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCoreDefinitionRequestRequestTypeDef

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


# GetCoreDefinitionVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.CoreDefinitionVersionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentStatusRequestRequestTypeDef

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


# GetDeviceDefinitionRequestRequestTypeDef

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


# GetDeviceDefinitionVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.DeviceDefinitionVersionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionDefinitionRequestRequestTypeDef

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


# GetFunctionDefinitionVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.FunctionDefinitionVersionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupCertificateAuthorityRequestRequestTypeDef

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


# GetGroupCertificateConfigurationRequestRequestTypeDef

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


# GetGroupRequestRequestTypeDef

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


# GetGroupVersionRequestRequestTypeDef

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


# GetLoggerDefinitionRequestRequestTypeDef

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


# GetLoggerDefinitionVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.LoggerDefinitionVersionTypeDef'>
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


# GetResourceDefinitionRequestRequestTypeDef

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


# GetResourceDefinitionVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResourceDefinitionVersionTypeDef'>
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


# GetSubscriptionDefinitionRequestRequestTypeDef

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


# GetSubscriptionDefinitionVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionDefinitionVersionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetThingRuntimeConfigurationRequestRequestTypeDef

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


# ListBulkDeploymentDetailedReportsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBulkDeploymentsRequestListBulkDeploymentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListBulkDeploymentsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListBulkDeploymentsResponseTypeDef

### BulkDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.BulkDeploymentTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConnectorDefinitionVersionsRequestListConnectorDefinitionVersionsPaginateTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListConnectorDefinitionVersionsRequestRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConnectorDefinitionsRequestListConnectorDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListConnectorDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCoreDefinitionVersionsRequestListCoreDefinitionVersionsPaginateTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListCoreDefinitionVersionsRequestRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCoreDefinitionsRequestListCoreDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListCoreDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeploymentsRequestListDeploymentsPaginateTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListDeploymentsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeviceDefinitionVersionsRequestListDeviceDefinitionVersionsPaginateTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListDeviceDefinitionVersionsRequestRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeviceDefinitionsRequestListDeviceDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListDeviceDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionDefinitionVersionsRequestListFunctionDefinitionVersionsPaginateTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListFunctionDefinitionVersionsRequestRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionDefinitionsRequestListFunctionDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListFunctionDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupCertificateAuthoritiesRequestRequestTypeDef

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


# ListGroupVersionsRequestListGroupVersionsPaginateTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListGroupVersionsRequestRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsRequestListGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListGroupsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.GroupInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLoggerDefinitionVersionsRequestListLoggerDefinitionVersionsPaginateTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListLoggerDefinitionVersionsRequestRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLoggerDefinitionsRequestListLoggerDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListLoggerDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceDefinitionVersionsRequestListResourceDefinitionVersionsPaginateTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListResourceDefinitionVersionsRequestRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceDefinitionsRequestListResourceDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListResourceDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscriptionDefinitionVersionsRequestListSubscriptionDefinitionVersionsPaginateTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListSubscriptionDefinitionVersionsRequestRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.VersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscriptionDefinitionsRequestListSubscriptionDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.PaginatorConfigTypeDef]


# ListSubscriptionDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionsResponseTypeDef

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass_classes.DefinitionInformationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# LoggerDefinitionVersionTypeDef

### Loggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.LoggerTypeDef]]


# LoggerTypeDef

### Component
- **Type**: typing.Literal['GreengrassSystem', 'Lambda']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Level
- **Type**: typing.Literal['DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN']
- **Required**: Yes

### Type
- **Type**: typing.Literal['AWSCloudWatch', 'FileSystem']
- **Required**: Yes

### Space
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResetDeploymentsRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass_classes.SecretsManagerSecretResourceDataTypeDef]


# ResourceDefinitionVersionTypeDef

### Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.ResourceTypeDef]]


# ResourceDownloadOwnerSettingTypeDef

### GroupOwner
- **Type**: <class 'str'>
- **Required**: Yes

### GroupPermission
- **Type**: typing.Literal['ro', 'rw']
- **Required**: Yes


# ResourceTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDataContainer
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass_classes.ResourceDataContainerTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# SecretsManagerSecretResourceDataTypeDef

### ARN
- **Type**: typing.Optional[str]

### AdditionalStagingLabelsToDownload
- **Type**: typing.Optional[typing.Sequence[str]]


# StartBulkDeploymentRequestRequestTypeDef

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


# StopBulkDeploymentRequestRequestTypeDef

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# SubscriptionDefinitionVersionTypeDef

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrass_classes.SubscriptionTypeDef]]


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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectivityInfoRequestRequestTypeDef

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


# UpdateConnectorDefinitionRequestRequestTypeDef

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateCoreDefinitionRequestRequestTypeDef

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateDeviceDefinitionRequestRequestTypeDef

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateFunctionDefinitionRequestRequestTypeDef

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateGroupCertificateConfigurationRequestRequestTypeDef

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


# UpdateGroupRequestRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateLoggerDefinitionRequestRequestTypeDef

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateResourceDefinitionRequestRequestTypeDef

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateSubscriptionDefinitionRequestRequestTypeDef

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateThingRuntimeConfigurationRequestRequestTypeDef

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


