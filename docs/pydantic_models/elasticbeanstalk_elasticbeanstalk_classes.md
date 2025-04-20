# Elasticbeanstalk Elasticbeanstalk Classes

# AbortEnvironmentUpdateMessage

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# ApplicationDescription

### ApplicationArn
- **Type**: typing.Optional[str]

### ApplicationName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateUpdated
- **Type**: typing.Optional[datetime.datetime]

### Versions
- **Type**: typing.Optional[typing.List[str]]

### ConfigurationTemplates
- **Type**: typing.Optional[typing.List[str]]

### ResourceLifecycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationResourceLifecycleConfig]


# ApplicationDescriptionMessage

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ApplicationDescriptionsMessage

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ApplicationMetrics

### Duration
- **Type**: typing.Optional[int]

### RequestCount
- **Type**: typing.Optional[int]

### StatusCodes
- **Type**: <class 'NoneType'>

### Latency
- **Type**: <class 'NoneType'>


# ApplicationResourceLifecycleConfig

### ServiceRole
- **Type**: typing.Optional[str]

### VersionLifecycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationVersionLifecycleConfig]


# ApplicationResourceLifecycleDescriptionMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceLifecycleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationResourceLifecycleConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ApplicationVersionDescription

### ApplicationVersionArn
- **Type**: typing.Optional[str]

### ApplicationName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### SourceBuildInformation
- **Type**: <class 'NoneType'>

### BuildArn
- **Type**: typing.Optional[str]

### SourceBundle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.S3Location]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateUpdated
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Building', 'Failed', 'Processed', 'Processing', 'Unprocessed']]


# ApplicationVersionDescriptionMessage

### ApplicationVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationVersionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ApplicationVersionDescriptionsMessage

### ApplicationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationVersionDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ApplicationVersionLifecycleConfig

### MaxCountRule
- **Type**: <class 'NoneType'>

### MaxAgeRule
- **Type**: <class 'NoneType'>


# ApplyEnvironmentManagedActionRequest

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]


# ApplyEnvironmentManagedActionResult

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ActionDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ActionType
- **Type**: typing.Literal['InstanceRefresh', 'PlatformUpdate', 'Unknown']
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateEnvironmentOperationsRoleMessage

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsRole
- **Type**: <class 'str'>
- **Required**: Yes


# AutoScalingGroup

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BuildConfiguration

### CodeBuildServiceRole
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactName
- **Type**: typing.Optional[str]

### ComputeType
- **Type**: typing.Optional[typing.Literal['BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL']]

### TimeoutInMinutes
- **Type**: typing.Optional[int]


# Builder

### ARN
- **Type**: typing.Optional[str]


# CPUUtilization

### User
- **Type**: typing.Optional[float]

### Nice
- **Type**: typing.Optional[float]

### System
- **Type**: typing.Optional[float]

### Idle
- **Type**: typing.Optional[float]

### IOWait
- **Type**: typing.Optional[float]

### IRQ
- **Type**: typing.Optional[float]

### SoftIRQ
- **Type**: typing.Optional[float]

### Privileged
- **Type**: typing.Optional[float]


# CheckDNSAvailabilityMessage

### CNAMEPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# CheckDNSAvailabilityResultMessage

### Available
- **Type**: <class 'bool'>
- **Required**: Yes

### FullyQualifiedCNAME
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ComposeEnvironmentsMessage

### ApplicationName
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### VersionLabels
- **Type**: typing.Optional[typing.List[str]]


# ConfigurationOptionDescription

### Namespace
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### ChangeSeverity
- **Type**: typing.Optional[str]

### UserDefined
- **Type**: typing.Optional[bool]

### ValueType
- **Type**: typing.Optional[typing.Literal['List', 'Scalar']]

### ValueOptions
- **Type**: typing.Optional[typing.List[str]]

### MinValue
- **Type**: typing.Optional[int]

### MaxValue
- **Type**: typing.Optional[int]

### MaxLength
- **Type**: typing.Optional[int]

### Regex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.OptionRestrictionRegex]


# ConfigurationOptionSetting

### ResourceName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ConfigurationOptionsDescription

### SolutionStackName
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigurationSettingsDescription

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### ApplicationName
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### DeploymentStatus
- **Type**: typing.Optional[typing.Literal['deployed', 'failed', 'pending']]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateUpdated
- **Type**: typing.Optional[datetime.datetime]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]]


# ConfigurationSettingsDescriptionResponse

### SolutionStackName
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentStatus
- **Type**: typing.Literal['deployed', 'failed', 'pending']
- **Required**: Yes

### DateCreated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DateUpdated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OptionSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigurationSettingsDescriptions

### ConfigurationSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationSettingsDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigurationSettingsValidationMessages

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ValidationMessage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApplicationMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ResourceLifecycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationResourceLifecycleConfig]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Tag]]


# CreateApplicationVersionMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SourceBuildInformation
- **Type**: <class 'NoneType'>

### SourceBundle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.S3Location]

### BuildConfiguration
- **Type**: <class 'NoneType'>

### AutoCreateApplication
- **Type**: typing.Optional[bool]

### Process
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Tag]]


# CreateConfigurationTemplateMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### SourceConfiguration
- **Type**: <class 'NoneType'>

### EnvironmentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Tag]]


# CreateEnvironmentMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentName
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CNAMEPrefix
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentTier]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Tag]]

### VersionLabel
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]]

### OptionsToRemove
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.OptionSpecification]]

### OperationsRole
- **Type**: typing.Optional[str]


# CreatePlatformVersionRequest

### PlatformName
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformDefinitionBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.S3Location'>
- **Required**: Yes

### EnvironmentName
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Tag]]


# CreatePlatformVersionResult

### PlatformSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformSummary'>
- **Required**: Yes

### Builder
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Builder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStorageLocationResultMessage

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# CustomAmi

### VirtualizationType
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]


# DeleteApplicationMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TerminateEnvByForce
- **Type**: typing.Optional[bool]


# DeleteApplicationVersionMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteSourceBundle
- **Type**: typing.Optional[bool]


# DeleteConfigurationTemplateMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentConfigurationMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlatformVersionRequest

### PlatformArn
- **Type**: typing.Optional[str]


# DeletePlatformVersionResult

### PlatformSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# Deployment

### VersionLabel
- **Type**: typing.Optional[str]

### DeploymentId
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### DeploymentTime
- **Type**: typing.Optional[datetime.datetime]


# DescribeAccountAttributesResult

### ResourceQuotas
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResourceQuotas'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationVersionsMessage

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabels
- **Type**: typing.Optional[typing.List[str]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationVersionsMessagePaginate

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabels
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PaginatorConfig]


# DescribeApplicationsMessage

### ApplicationNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeConfigurationOptionsMessage

### ApplicationName
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.OptionSpecification]]


# DescribeConfigurationSettingsMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# DescribeEnvironmentHealthRequest

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### AttributeNames
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'ApplicationMetrics', 'Causes', 'Color', 'HealthStatus', 'InstancesHealth', 'RefreshedAt', 'Status']]]


# DescribeEnvironmentHealthResult

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### HealthStatus
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Green', 'Grey', 'Red', 'Yellow']
- **Required**: Yes

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### Causes
- **Type**: typing.List[str]
- **Required**: Yes

### ApplicationMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationMetrics'>
- **Required**: Yes

### InstancesHealth
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.InstanceHealthSummary'>
- **Required**: Yes

### RefreshedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEnvironmentManagedActionHistoryRequest

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# DescribeEnvironmentManagedActionHistoryRequestPaginate

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PaginatorConfig]


# DescribeEnvironmentManagedActionHistoryResult

### ManagedActionHistoryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ManagedActionHistoryItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEnvironmentManagedActionsRequest

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Pending', 'Running', 'Scheduled', 'Unknown']]


# DescribeEnvironmentManagedActionsResult

### ManagedActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ManagedAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEnvironmentResourcesMessage

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# DescribeEnvironmentsMessage

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.List[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.List[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEnvironmentsMessagePaginate

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.List[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.List[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PaginatorConfig]


# DescribeEnvironmentsMessageWait

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.List[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.List[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEnvironmentsMessageWaitExtra

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.List[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.List[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEnvironmentsMessageWaitExtraExtra

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.List[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.List[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEventsMessage

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'FATAL', 'INFO', 'TRACE', 'WARN']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsMessagePaginate

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'FATAL', 'INFO', 'TRACE', 'WARN']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PaginatorConfig]


# DescribeInstancesHealthRequest

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### AttributeNames
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'ApplicationMetrics', 'AvailabilityZone', 'Causes', 'Color', 'Deployment', 'HealthStatus', 'InstanceType', 'LaunchedAt', 'RefreshedAt', 'System']]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancesHealthResult

### InstanceHealthList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.SingleInstanceHealth]
- **Required**: Yes

### RefreshedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePlatformVersionRequest

### PlatformArn
- **Type**: typing.Optional[str]


# DescribePlatformVersionResult

### PlatformDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateEnvironmentOperationsRoleMessage

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# EnvironmentDescription

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointURL
- **Type**: typing.Optional[str]

### CNAME
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateUpdated
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Aborting', 'Launching', 'LinkingFrom', 'LinkingTo', 'Ready', 'Terminated', 'Terminating', 'Updating']]

### AbortableOperationInProgress
- **Type**: typing.Optional[bool]

### Health
- **Type**: typing.Optional[typing.Literal['Green', 'Grey', 'Red', 'Yellow']]

### HealthStatus
- **Type**: typing.Optional[typing.Literal['Degraded', 'Info', 'NoData', 'Ok', 'Pending', 'Severe', 'Suspended', 'Unknown', 'Warning']]

### Resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentResourcesDescription]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentTier]

### EnvironmentLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentLink]]

### EnvironmentArn
- **Type**: typing.Optional[str]

### OperationsRole
- **Type**: typing.Optional[str]


# EnvironmentDescriptionResponse

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### SolutionStackName
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformArn
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointURL
- **Type**: <class 'str'>
- **Required**: Yes

### CNAME
- **Type**: <class 'str'>
- **Required**: Yes

### DateCreated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DateUpdated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Aborting', 'Launching', 'LinkingFrom', 'LinkingTo', 'Ready', 'Terminated', 'Terminating', 'Updating']
- **Required**: Yes

### AbortableOperationInProgress
- **Type**: <class 'bool'>
- **Required**: Yes

### Health
- **Type**: typing.Literal['Green', 'Grey', 'Red', 'Yellow']
- **Required**: Yes

### HealthStatus
- **Type**: typing.Literal['Degraded', 'Info', 'NoData', 'Ok', 'Pending', 'Severe', 'Suspended', 'Unknown', 'Warning']
- **Required**: Yes

### Resources
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentResourcesDescription'>
- **Required**: Yes

### Tier
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentTier'>
- **Required**: Yes

### EnvironmentLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentLink]
- **Required**: Yes

### EnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsRole
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# EnvironmentDescriptionsMessage

### Environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# EnvironmentInfoDescription

### InfoType
- **Type**: typing.Optional[typing.Literal['bundle', 'tail']]

### Ec2InstanceId
- **Type**: typing.Optional[str]

### SampleTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Message
- **Type**: typing.Optional[str]


# EnvironmentLink

### LinkName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# EnvironmentResourceDescription

### EnvironmentName
- **Type**: typing.Optional[str]

### AutoScalingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.AutoScalingGroup]]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Instance]]

### LaunchConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.LaunchConfiguration]]

### LaunchTemplates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.LaunchTemplate]]

### LoadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.LoadBalancer]]

### Triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Trigger]]

### Queues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Queue]]


# EnvironmentResourceDescriptionsMessage

### EnvironmentResources
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentResourceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# EnvironmentResourcesDescription

### LoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.LoadBalancerDescription]


# EnvironmentTier

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# EventDescription

### EventDate
- **Type**: typing.Optional[datetime.datetime]

### Message
- **Type**: typing.Optional[str]

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'FATAL', 'INFO', 'TRACE', 'WARN']]


# EventDescriptionsMessage

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EventDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Instance

### Id
- **Type**: typing.Optional[str]


# InstanceHealthSummary

### NoData
- **Type**: typing.Optional[int]

### Unknown
- **Type**: typing.Optional[int]

### Pending
- **Type**: typing.Optional[int]

### Ok
- **Type**: typing.Optional[int]

### Info
- **Type**: typing.Optional[int]

### Warning
- **Type**: typing.Optional[int]

### Degraded
- **Type**: typing.Optional[int]

### Severe
- **Type**: typing.Optional[int]


# Latency

### P999
- **Type**: typing.Optional[float]

### P99
- **Type**: typing.Optional[float]

### P95
- **Type**: typing.Optional[float]

### P90
- **Type**: typing.Optional[float]

### P85
- **Type**: typing.Optional[float]

### P75
- **Type**: typing.Optional[float]

### P50
- **Type**: typing.Optional[float]

### P10
- **Type**: typing.Optional[float]


# LaunchConfiguration

### Name
- **Type**: typing.Optional[str]


# LaunchTemplate

### Id
- **Type**: typing.Optional[str]


# ListAvailableSolutionStacksResultMessage

### SolutionStacks
- **Type**: typing.List[str]
- **Required**: Yes

### SolutionStackDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.SolutionStackDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# ListPlatformBranchesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.SearchFilter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformBranchesResult

### PlatformBranchSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformBranchSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformVersionsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformFilter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformVersionsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PaginatorConfig]


# ListPlatformVersionsResult

### PlatformSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# Listener

### Protocol
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# LoadBalancer

### Name
- **Type**: typing.Optional[str]


# LoadBalancerDescription

### LoadBalancerName
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Listeners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Listener]]


# ManagedAction

### ActionId
- **Type**: typing.Optional[str]

### ActionDescription
- **Type**: typing.Optional[str]

### ActionType
- **Type**: typing.Optional[typing.Literal['InstanceRefresh', 'PlatformUpdate', 'Unknown']]

### Status
- **Type**: typing.Optional[typing.Literal['Pending', 'Running', 'Scheduled', 'Unknown']]

### WindowStartTime
- **Type**: typing.Optional[datetime.datetime]


# ManagedActionHistoryItem

### ActionId
- **Type**: typing.Optional[str]

### ActionType
- **Type**: typing.Optional[typing.Literal['InstanceRefresh', 'PlatformUpdate', 'Unknown']]

### ActionDescription
- **Type**: typing.Optional[str]

### FailureType
- **Type**: typing.Optional[typing.Literal['CancellationFailed', 'InternalFailure', 'InvalidEnvironmentState', 'PermissionsError', 'RollbackFailed', 'RollbackSuccessful', 'UpdateCancelled']]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'Unknown']]

### FailureDescription
- **Type**: typing.Optional[str]

### ExecutedTime
- **Type**: typing.Optional[datetime.datetime]

### FinishedTime
- **Type**: typing.Optional[datetime.datetime]


# MaxAgeRule

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxAgeInDays
- **Type**: typing.Optional[int]

### DeleteSourceFromS3
- **Type**: typing.Optional[bool]


# MaxCountRule

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxCount
- **Type**: typing.Optional[int]

### DeleteSourceFromS3
- **Type**: typing.Optional[bool]


# OptionRestrictionRegex

### Pattern
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]


# OptionSpecification

### ResourceName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlatformBranchSummary

### PlatformName
- **Type**: typing.Optional[str]

### BranchName
- **Type**: typing.Optional[str]

### LifecycleState
- **Type**: typing.Optional[str]

### BranchOrder
- **Type**: typing.Optional[int]

### SupportedTierList
- **Type**: typing.Optional[typing.List[str]]


# PlatformDescription

### PlatformArn
- **Type**: typing.Optional[str]

### PlatformOwner
- **Type**: typing.Optional[str]

### PlatformName
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformStatus
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleted', 'Deleting', 'Failed', 'Ready']]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateUpdated
- **Type**: typing.Optional[datetime.datetime]

### PlatformCategory
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Maintainer
- **Type**: typing.Optional[str]

### OperatingSystemName
- **Type**: typing.Optional[str]

### OperatingSystemVersion
- **Type**: typing.Optional[str]

### ProgrammingLanguages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformProgrammingLanguage]]

### Frameworks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.PlatformFramework]]

### CustomAmiList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.CustomAmi]]

### SupportedTierList
- **Type**: typing.Optional[typing.List[str]]

### SupportedAddonList
- **Type**: typing.Optional[typing.List[str]]

### PlatformLifecycleState
- **Type**: typing.Optional[str]

### PlatformBranchName
- **Type**: typing.Optional[str]

### PlatformBranchLifecycleState
- **Type**: typing.Optional[str]


# PlatformFilter

### Type
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# PlatformFramework

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# PlatformProgrammingLanguage

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# PlatformSummary

### PlatformArn
- **Type**: typing.Optional[str]

### PlatformOwner
- **Type**: typing.Optional[str]

### PlatformStatus
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleted', 'Deleting', 'Failed', 'Ready']]

### PlatformCategory
- **Type**: typing.Optional[str]

### OperatingSystemName
- **Type**: typing.Optional[str]

### OperatingSystemVersion
- **Type**: typing.Optional[str]

### SupportedTierList
- **Type**: typing.Optional[typing.List[str]]

### SupportedAddonList
- **Type**: typing.Optional[typing.List[str]]

### PlatformLifecycleState
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### PlatformBranchName
- **Type**: typing.Optional[str]

### PlatformBranchLifecycleState
- **Type**: typing.Optional[str]


# Queue

### Name
- **Type**: typing.Optional[str]

### URL
- **Type**: typing.Optional[str]


# RebuildEnvironmentMessage

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# RequestEnvironmentInfoMessage

### InfoType
- **Type**: typing.Literal['bundle', 'tail']
- **Required**: Yes

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# ResourceQuota

### Maximum
- **Type**: typing.Optional[int]


# ResourceQuotas

### ApplicationQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResourceQuota]

### ApplicationVersionQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResourceQuota]

### EnvironmentQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResourceQuota]

### ConfigurationTemplateQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResourceQuota]

### CustomPlatformQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResourceQuota]


# ResourceTagsDescriptionMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
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


# RestartAppServerMessage

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# RetrieveEnvironmentInfoMessage

### InfoType
- **Type**: typing.Literal['bundle', 'tail']
- **Required**: Yes

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# RetrieveEnvironmentInfoResultMessage

### EnvironmentInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentInfoDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ResponseMetadata'>
- **Required**: Yes


# S3Location

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]


# SearchFilter

### Attribute
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# SingleInstanceHealth

### InstanceId
- **Type**: typing.Optional[str]

### HealthStatus
- **Type**: typing.Optional[str]

### Color
- **Type**: typing.Optional[str]

### Causes
- **Type**: typing.Optional[typing.List[str]]

### LaunchedAt
- **Type**: typing.Optional[datetime.datetime]

### ApplicationMetrics
- **Type**: <class 'NoneType'>

### System
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.SystemStatus]

### Deployment
- **Type**: <class 'NoneType'>

### AvailabilityZone
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]


# SolutionStackDescription

### SolutionStackName
- **Type**: typing.Optional[str]

### PermittedFileTypes
- **Type**: typing.Optional[typing.List[str]]


# SourceBuildInformation

### SourceType
- **Type**: typing.Literal['Git', 'Zip']
- **Required**: Yes

### SourceRepository
- **Type**: typing.Literal['CodeCommit', 'S3']
- **Required**: Yes

### SourceLocation
- **Type**: <class 'str'>
- **Required**: Yes


# SourceConfiguration

### ApplicationName
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]


# StatusCodes

### Status2xx
- **Type**: typing.Optional[int]

### Status3xx
- **Type**: typing.Optional[int]

### Status4xx
- **Type**: typing.Optional[int]

### Status5xx
- **Type**: typing.Optional[int]


# SwapEnvironmentCNAMEsMessage

### SourceEnvironmentId
- **Type**: typing.Optional[str]

### SourceEnvironmentName
- **Type**: typing.Optional[str]

### DestinationEnvironmentId
- **Type**: typing.Optional[str]

### DestinationEnvironmentName
- **Type**: typing.Optional[str]


# SystemStatus

### CPUUtilization
- **Type**: <class 'NoneType'>

### LoadAverage
- **Type**: typing.Optional[typing.List[float]]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TerminateEnvironmentMessage

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### TerminateResources
- **Type**: typing.Optional[bool]

### ForceTerminate
- **Type**: typing.Optional[bool]


# Trigger

### Name
- **Type**: typing.Optional[str]


# UpdateApplicationMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateApplicationResourceLifecycleMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceLifecycleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ApplicationResourceLifecycleConfig'>
- **Required**: Yes


# UpdateApplicationVersionMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationTemplateMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]]

### OptionsToRemove
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.OptionSpecification]]


# UpdateEnvironmentMessage

### ApplicationName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.EnvironmentTier]

### VersionLabel
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]]

### OptionsToRemove
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.OptionSpecification]]


# UpdateTagsForResourceMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.Tag]]

### TagsToRemove
- **Type**: typing.Optional[typing.List[str]]


# ValidateConfigurationSettingsMessage

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### OptionSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_classes.ConfigurationOptionSetting]
- **Required**: Yes

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# ValidationMessage

### Message
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['error', 'warning']]

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


