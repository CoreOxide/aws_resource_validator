# Greengrass Classes

# AssociateRoleToGroupRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateRoleToGroupResponse

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateServiceRoleToAccountRequest

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateServiceRoleToAccountResponse

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BulkDeployment

### BulkDeploymentArn
- **Type**: typing.Optional[str]

### BulkDeploymentId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]


# BulkDeploymentMetrics

### InvalidInputRecords
- **Type**: typing.Optional[int]

### RecordsProcessed
- **Type**: typing.Optional[int]

### RetryAttempts
- **Type**: typing.Optional[int]


# BulkDeploymentResult

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ErrorDetail]]

### ErrorMessage
- **Type**: typing.Optional[str]

### GroupArn
- **Type**: typing.Optional[str]


# ConnectivityInfo

### HostAddress
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### PortNumber
- **Type**: typing.Optional[int]


# Connector

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConnectorDefinitionVersion

### Connectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Connector]]


# ConnectorDefinitionVersionOutput

### Connectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ConnectorOutput]]


# ConnectorOutput

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# Core

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


# CoreDefinitionVersion

### Cores
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Core]]


# CoreDefinitionVersionOutput

### Cores
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Core]]


# CreateConnectorDefinitionRequest

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ConnectorDefinitionVersion, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ConnectorDefinitionVersionOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConnectorDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectorDefinitionVersionRequest

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Connectors
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Connector, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ConnectorOutput]]]


# CreateConnectorDefinitionVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCoreDefinitionRequest

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.CoreDefinitionVersion, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.CoreDefinitionVersionOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCoreDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCoreDefinitionVersionRequest

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Cores
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Core]]


# CreateCoreDefinitionVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentRequest

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


# CreateDeploymentResponse

### DeploymentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeviceDefinitionRequest

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DeviceDefinitionVersion, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DeviceDefinitionVersionOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDeviceDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeviceDefinitionVersionRequest

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Device]]


# CreateDeviceDefinitionVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFunctionDefinitionRequest

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionDefinitionVersion, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionDefinitionVersionOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateFunctionDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFunctionDefinitionVersionRequest

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionDefaultConfig]

### Functions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Function, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionOutput]]]


# CreateFunctionDefinitionVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupCertificateAuthorityRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]


# CreateGroupCertificateAuthorityResponse

### GroupCertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.GroupVersion]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupVersionRequest

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


# CreateGroupVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoggerDefinitionRequest

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.LoggerDefinitionVersion, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.LoggerDefinitionVersionOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLoggerDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoggerDefinitionVersionRequest

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Loggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Logger]]


# CreateLoggerDefinitionVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceDefinitionRequest

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDefinitionVersion, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDefinitionVersionOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateResourceDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceDefinitionVersionRequest

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Resource, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceOutput]]]


# CreateResourceDefinitionVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSoftwareUpdateJobRequest

### S3UrlSignerRole
- **Type**: <class 'str'>
- **Required**: Yes

### SoftwareToUpdate
- **Type**: typing.Literal['core', 'ota_agent']
- **Required**: Yes

### UpdateTargets
- **Type**: typing.List[str]
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


# CreateSoftwareUpdateJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriptionDefinitionRequest

### AmznClientToken
- **Type**: typing.Optional[str]

### InitialVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.SubscriptionDefinitionVersion, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.SubscriptionDefinitionVersionOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSubscriptionDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriptionDefinitionVersionRequest

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Subscriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Subscription]]


# CreateSubscriptionDefinitionVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# DefinitionInformation

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


# DeleteConnectorDefinitionRequest

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCoreDefinitionRequest

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceDefinitionRequest

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionDefinitionRequest

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoggerDefinitionRequest

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceDefinitionRequest

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionDefinitionRequest

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# Deployment

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


# Device

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


# DeviceDefinitionVersion

### Devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Device]]


# DeviceDefinitionVersionOutput

### Devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Device]]


# DisassociateRoleFromGroupRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateRoleFromGroupResponse

### DisassociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateServiceRoleFromAccountResponse

### DisassociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorDetail

### DetailedErrorCode
- **Type**: typing.Optional[str]

### DetailedErrorMessage
- **Type**: typing.Optional[str]


# Function

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: typing.Optional[str]

### FunctionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionConfiguration, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionConfigurationOutput, NoneType]


# FunctionConfiguration

### EncodingType
- **Type**: typing.Optional[typing.Literal['binary', 'json']]

### Environment
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionConfigurationEnvironment, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionConfigurationEnvironmentOutput, NoneType]

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


# FunctionConfigurationEnvironment

### AccessSysfs
- **Type**: typing.Optional[bool]

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionExecutionConfig]

### ResourceAccessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceAccessPolicy]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]


# FunctionConfigurationEnvironmentOutput

### AccessSysfs
- **Type**: typing.Optional[bool]

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionExecutionConfig]

### ResourceAccessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceAccessPolicy]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]


# FunctionConfigurationOutput

### EncodingType
- **Type**: typing.Optional[typing.Literal['binary', 'json']]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionConfigurationEnvironmentOutput]

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


# FunctionDefaultConfig

### Execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionDefaultExecutionConfig]


# FunctionDefaultExecutionConfig

### IsolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### RunAs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionRunAsConfig]


# FunctionDefinitionVersion

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionDefaultConfig]

### Functions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Function]]


# FunctionDefinitionVersionOutput

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionDefaultConfig]

### Functions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionOutput]]


# FunctionExecutionConfig

### IsolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### RunAs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionRunAsConfig]


# FunctionOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: typing.Optional[str]

### FunctionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionConfigurationOutput]


# FunctionRunAsConfig

### Gid
- **Type**: typing.Optional[int]

### Uid
- **Type**: typing.Optional[int]


# GetAssociatedRoleRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssociatedRoleResponse

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetBulkDeploymentStatusRequest

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBulkDeploymentStatusResponse

### BulkDeploymentMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.BulkDeploymentMetrics'>
- **Required**: Yes

### BulkDeploymentStatus
- **Type**: typing.Literal['Completed', 'Failed', 'Initializing', 'Running', 'Stopped', 'Stopping']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ErrorDetail]
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectivityInfoRequest

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectivityInfoResponse

### ConnectivityInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ConnectivityInfo]
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectorDefinitionRequest

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectorDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectorDefinitionVersionRequest

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetConnectorDefinitionVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ConnectorDefinitionVersionOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreDefinitionRequest

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetCoreDefinitionVersionRequest

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreDefinitionVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.CoreDefinitionVersionOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDeploymentStatusRequest

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentStatusResponse

### DeploymentStatus
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentType
- **Type**: typing.Literal['ForceResetDeployment', 'NewDeployment', 'Redeployment', 'ResetDeployment']
- **Required**: Yes

### ErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ErrorDetail]
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceDefinitionRequest

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceDefinitionVersionRequest

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDeviceDefinitionVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DeviceDefinitionVersionOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFunctionDefinitionRequest

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetFunctionDefinitionVersionRequest

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFunctionDefinitionVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.FunctionDefinitionVersionOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetGroupCertificateAuthorityRequest

### CertificateAuthorityId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupCertificateAuthorityResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupCertificateConfigurationRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupCertificateConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupVersionRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.GroupVersion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoggerDefinitionRequest

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggerDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoggerDefinitionVersionRequest

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### LoggerDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLoggerDefinitionVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.LoggerDefinitionVersionOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceDefinitionRequest

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceDefinitionVersionRequest

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceDefinitionVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDefinitionVersionOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceRoleForAccountResponse

### AssociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionDefinitionRequest

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionDefinitionVersionRequest

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionDefinitionVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSubscriptionDefinitionVersionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.SubscriptionDefinitionVersionOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetThingRuntimeConfigurationRequest

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetThingRuntimeConfigurationResponse

### RuntimeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.RuntimeConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# GroupCertificateAuthorityProperties

### GroupCertificateAuthorityArn
- **Type**: typing.Optional[str]

### GroupCertificateAuthorityId
- **Type**: typing.Optional[str]


# GroupInformation

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


# GroupOwnerSetting

### AutoAddGroupOwner
- **Type**: typing.Optional[bool]

### GroupOwner
- **Type**: typing.Optional[str]


# GroupVersion

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


# ListBulkDeploymentDetailedReportsRequest

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListBulkDeploymentDetailedReportsRequestPaginate

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListBulkDeploymentDetailedReportsResponse

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.BulkDeploymentResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBulkDeploymentsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListBulkDeploymentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListBulkDeploymentsResponse

### BulkDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.BulkDeployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionVersionsRequest

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionVersionsRequestPaginate

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListConnectorDefinitionVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListConnectorDefinitionsResponse

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionVersionsRequest

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionVersionsRequestPaginate

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListCoreDefinitionVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListCoreDefinitionsResponse

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestPaginate

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListDeploymentsResponse

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Deployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionVersionsRequest

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionVersionsRequestPaginate

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListDeviceDefinitionVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListDeviceDefinitionsResponse

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionVersionsRequest

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionVersionsRequestPaginate

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListFunctionDefinitionVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListFunctionDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListFunctionDefinitionsResponse

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupCertificateAuthoritiesRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# ListGroupCertificateAuthoritiesResponse

### GroupCertificateAuthorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.GroupCertificateAuthorityProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# ListGroupVersionsRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupVersionsRequestPaginate

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListGroupVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.GroupInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionVersionsRequest

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionVersionsRequestPaginate

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListLoggerDefinitionVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListLoggerDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListLoggerDefinitionsResponse

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionVersionsRequest

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionVersionsRequestPaginate

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListResourceDefinitionVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListResourceDefinitionsResponse

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionVersionsRequest

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionVersionsRequestPaginate

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListSubscriptionDefinitionVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.VersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.PaginatorConfig]


# ListSubscriptionDefinitionsResponse

### Definitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.DefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# LocalDeviceResourceData

### GroupOwnerSetting
- **Type**: <class 'NoneType'>

### SourcePath
- **Type**: typing.Optional[str]


# LocalVolumeResourceData

### DestinationPath
- **Type**: typing.Optional[str]

### GroupOwnerSetting
- **Type**: <class 'NoneType'>

### SourcePath
- **Type**: typing.Optional[str]


# Logger

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


# LoggerDefinitionVersion

### Loggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Logger]]


# LoggerDefinitionVersionOutput

### Loggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Logger]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResetDeploymentsRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### Force
- **Type**: typing.Optional[bool]


# ResetDeploymentsResponse

### DeploymentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# Resource

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDataContainer
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDataContainer, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDataContainerOutput]
- **Required**: Yes


# ResourceAccessPolicy

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Permission
- **Type**: typing.Optional[typing.Literal['ro', 'rw']]


# ResourceDataContainer

### LocalDeviceResourceData
- **Type**: <class 'NoneType'>

### LocalVolumeResourceData
- **Type**: <class 'NoneType'>

### S3MachineLearningModelResourceData
- **Type**: <class 'NoneType'>

### SageMakerMachineLearningModelResourceData
- **Type**: <class 'NoneType'>

### SecretsManagerSecretResourceData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.SecretsManagerSecretResourceData, aws_resource_validator.pydantic_models.greengrass.greengrass_classes.SecretsManagerSecretResourceDataOutput, NoneType]


# ResourceDataContainerOutput

### LocalDeviceResourceData
- **Type**: <class 'NoneType'>

### LocalVolumeResourceData
- **Type**: <class 'NoneType'>

### S3MachineLearningModelResourceData
- **Type**: <class 'NoneType'>

### SageMakerMachineLearningModelResourceData
- **Type**: <class 'NoneType'>

### SecretsManagerSecretResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.SecretsManagerSecretResourceDataOutput]


# ResourceDefinitionVersion

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Resource]]


# ResourceDefinitionVersionOutput

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceOutput]]


# ResourceDownloadOwnerSetting

### GroupOwner
- **Type**: <class 'str'>
- **Required**: Yes

### GroupPermission
- **Type**: typing.Literal['ro', 'rw']
- **Required**: Yes


# ResourceOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDataContainer
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDataContainerOutput'>
- **Required**: Yes


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


# RuntimeConfiguration

### TelemetryConfiguration
- **Type**: <class 'NoneType'>


# S3MachineLearningModelResourceData

### DestinationPath
- **Type**: typing.Optional[str]

### OwnerSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDownloadOwnerSetting]

### S3Uri
- **Type**: typing.Optional[str]


# SageMakerMachineLearningModelResourceData

### DestinationPath
- **Type**: typing.Optional[str]

### OwnerSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResourceDownloadOwnerSetting]

### SageMakerJobArn
- **Type**: typing.Optional[str]


# SecretsManagerSecretResourceData

### ARN
- **Type**: typing.Optional[str]

### AdditionalStagingLabelsToDownload
- **Type**: typing.Optional[typing.List[str]]


# SecretsManagerSecretResourceDataOutput

### ARN
- **Type**: typing.Optional[str]

### AdditionalStagingLabelsToDownload
- **Type**: typing.Optional[typing.List[str]]


# StartBulkDeploymentRequest

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputFileUri
- **Type**: <class 'str'>
- **Required**: Yes

### AmznClientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartBulkDeploymentResponse

### BulkDeploymentArn
- **Type**: <class 'str'>
- **Required**: Yes

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# StopBulkDeploymentRequest

### BulkDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# Subscription

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


# SubscriptionDefinitionVersion

### Subscriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Subscription]]


# SubscriptionDefinitionVersionOutput

### Subscriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.Subscription]]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TelemetryConfiguration

### Telemetry
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes

### ConfigurationSyncStatus
- **Type**: typing.Optional[typing.Literal['InSync', 'OutOfSync']]


# TelemetryConfigurationUpdate

### Telemetry
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateConnectivityInfoRequest

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectivityInfo
- **Type**: typing.Optional[typing.List[NoneType]]


# UpdateConnectivityInfoResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConnectorDefinitionRequest

### ConnectorDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateCoreDefinitionRequest

### CoreDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateDeviceDefinitionRequest

### DeviceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateFunctionDefinitionRequest

### FunctionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateGroupCertificateConfigurationRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateExpiryInMilliseconds
- **Type**: typing.Optional[str]


# UpdateGroupCertificateConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrass.greengrass_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGroupRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateLoggerDefinitionRequest

### LoggerDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateResourceDefinitionRequest

### ResourceDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateSubscriptionDefinitionRequest

### SubscriptionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateThingRuntimeConfigurationRequest

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes

### TelemetryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrass.greengrass_classes.TelemetryConfigurationUpdate]


# VersionInformation

### Arn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


