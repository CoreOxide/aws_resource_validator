# elasticbeanstalk_classes

# AbortEnvironmentUpdateMessageRequestTypeDef

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# ApplicationDescriptionMessageTypeDef

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationResourceLifecycleConfigTypeDef]


# ApplicationDescriptionsMessageTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationMetricsTypeDef

### Duration
- **Type**: typing.Optional[int]

### RequestCount
- **Type**: typing.Optional[int]

### StatusCodes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.StatusCodesTypeDef]

### Latency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.LatencyTypeDef]


# ApplicationResourceLifecycleConfigTypeDef

### ServiceRole
- **Type**: typing.Optional[str]

### VersionLifecycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationVersionLifecycleConfigTypeDef]


# ApplicationResourceLifecycleDescriptionMessageTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceLifecycleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationResourceLifecycleConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationVersionDescriptionMessageTypeDef

### ApplicationVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationVersionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationVersionDescriptionTypeDef

### ApplicationVersionArn
- **Type**: typing.Optional[str]

### ApplicationName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### SourceBuildInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.SourceBuildInformationTypeDef]

### BuildArn
- **Type**: typing.Optional[str]

### SourceBundle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.S3LocationTypeDef]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateUpdated
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Building', 'Failed', 'Processed', 'Processing', 'Unprocessed']]


# ApplicationVersionDescriptionsMessageTypeDef

### ApplicationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationVersionDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ApplicationVersionLifecycleConfigTypeDef

### MaxCountRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.MaxCountRuleTypeDef]

### MaxAgeRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.MaxAgeRuleTypeDef]


# ApplyEnvironmentManagedActionRequestRequestTypeDef

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]


# ApplyEnvironmentManagedActionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateEnvironmentOperationsRoleMessageRequestTypeDef

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsRole
- **Type**: <class 'str'>
- **Required**: Yes


# AutoScalingGroupTypeDef

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BuildConfigurationTypeDef

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


# BuilderTypeDef

### ARN
- **Type**: typing.Optional[str]


# CPUUtilizationTypeDef

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


# CheckDNSAvailabilityMessageRequestTypeDef

### CNAMEPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# CheckDNSAvailabilityResultMessageTypeDef

### Available
- **Type**: <class 'bool'>
- **Required**: Yes

### FullyQualifiedCNAME
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ComposeEnvironmentsMessageRequestTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### VersionLabels
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfigurationOptionDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.OptionRestrictionRegexTypeDef]


# ConfigurationOptionSettingTypeDef

### ResourceName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ConfigurationOptionsDescriptionTypeDef

### SolutionStackName
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigurationSettingsDescriptionResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigurationSettingsDescriptionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]]


# ConfigurationSettingsDescriptionsTypeDef

### ConfigurationSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationSettingsDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigurationSettingsValidationMessagesTypeDef

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ValidationMessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ResourceLifecycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationResourceLifecycleConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TagTypeDef]]


# CreateApplicationVersionMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SourceBuildInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.SourceBuildInformationTypeDef]

### SourceBundle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.S3LocationTypeDef]

### BuildConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.BuildConfigurationTypeDef]

### AutoCreateApplication
- **Type**: typing.Optional[bool]

### Process
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TagTypeDef]]


# CreateConfigurationTemplateMessageRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.SourceConfigurationTypeDef]

### EnvironmentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TagTypeDef]]


# CreateEnvironmentMessageRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentTierTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TagTypeDef]]

### VersionLabel
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]]

### OptionsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.OptionSpecificationTypeDef]]

### OperationsRole
- **Type**: typing.Optional[str]


# CreatePlatformVersionRequestRequestTypeDef

### PlatformName
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PlatformDefinitionBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.S3LocationTypeDef'>
- **Required**: Yes

### EnvironmentName
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TagTypeDef]]


# CreatePlatformVersionResultTypeDef

### PlatformSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformSummaryTypeDef'>
- **Required**: Yes

### Builder
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.BuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStorageLocationResultMessageTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomAmiTypeDef

### VirtualizationType
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]


# DeleteApplicationMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TerminateEnvByForce
- **Type**: typing.Optional[bool]


# DeleteApplicationVersionMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteSourceBundle
- **Type**: typing.Optional[bool]


# DeleteConfigurationTemplateMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentConfigurationMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlatformVersionRequestRequestTypeDef

### PlatformArn
- **Type**: typing.Optional[str]


# DeletePlatformVersionResultTypeDef

### PlatformSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeploymentTypeDef

### VersionLabel
- **Type**: typing.Optional[str]

### DeploymentId
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### DeploymentTime
- **Type**: typing.Optional[datetime.datetime]


# DescribeAccountAttributesResultTypeDef

### ResourceQuotas
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResourceQuotasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationVersionsMessageDescribeApplicationVersionsPaginateTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabels
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PaginatorConfigTypeDef]


# DescribeApplicationVersionsMessageRequestTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabels
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationsMessageRequestTypeDef

### ApplicationNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeConfigurationOptionsMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.OptionSpecificationTypeDef]]


# DescribeConfigurationSettingsMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# DescribeEnvironmentHealthRequestRequestTypeDef

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'ApplicationMetrics', 'Causes', 'Color', 'HealthStatus', 'InstancesHealth', 'RefreshedAt', 'Status']]]


# DescribeEnvironmentHealthResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationMetricsTypeDef'>
- **Required**: Yes

### InstancesHealth
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.InstanceHealthSummaryTypeDef'>
- **Required**: Yes

### RefreshedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEnvironmentManagedActionHistoryRequestDescribeEnvironmentManagedActionHistoryPaginateTypeDef

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PaginatorConfigTypeDef]


# DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# DescribeEnvironmentManagedActionHistoryResultTypeDef

### ManagedActionHistoryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ManagedActionHistoryItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEnvironmentManagedActionsRequestRequestTypeDef

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Pending', 'Running', 'Scheduled', 'Unknown']]


# DescribeEnvironmentManagedActionsResultTypeDef

### ManagedActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ManagedActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEnvironmentResourcesMessageRequestTypeDef

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# DescribeEnvironmentsMessageDescribeEnvironmentsPaginateTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PaginatorConfigTypeDef]


# DescribeEnvironmentsMessageEnvironmentExistsWaitTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.WaiterConfigTypeDef]


# DescribeEnvironmentsMessageEnvironmentTerminatedWaitTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.WaiterConfigTypeDef]


# DescribeEnvironmentsMessageEnvironmentUpdatedWaitTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.WaiterConfigTypeDef]


# DescribeEnvironmentsMessageRequestTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### EnvironmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EnvironmentNames
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeDeleted
- **Type**: typing.Optional[bool]

### IncludedDeletedBackTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsMessageDescribeEventsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PaginatorConfigTypeDef]


# DescribeEventsMessageRequestTypeDef

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


# DescribeInstancesHealthRequestRequestTypeDef

### EnvironmentName
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'ApplicationMetrics', 'AvailabilityZone', 'Causes', 'Color', 'Deployment', 'HealthStatus', 'InstanceType', 'LaunchedAt', 'RefreshedAt', 'System']]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancesHealthResultTypeDef

### InstanceHealthList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.SingleInstanceHealthTypeDef]
- **Required**: Yes

### RefreshedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePlatformVersionRequestRequestTypeDef

### PlatformArn
- **Type**: typing.Optional[str]


# DescribePlatformVersionResultTypeDef

### PlatformDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateEnvironmentOperationsRoleMessageRequestTypeDef

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentDescriptionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentResourcesDescriptionTypeDef'>
- **Required**: Yes

### Tier
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentTierTypeDef'>
- **Required**: Yes

### EnvironmentLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentLinkTypeDef]
- **Required**: Yes

### EnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsRole
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentResourcesDescriptionTypeDef]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentTierTypeDef]

### EnvironmentLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentLinkTypeDef]]

### EnvironmentArn
- **Type**: typing.Optional[str]

### OperationsRole
- **Type**: typing.Optional[str]


# EnvironmentDescriptionsMessageTypeDef

### Environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# EnvironmentInfoDescriptionTypeDef

### InfoType
- **Type**: typing.Optional[typing.Literal['bundle', 'tail']]

### Ec2InstanceId
- **Type**: typing.Optional[str]

### SampleTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Message
- **Type**: typing.Optional[str]


# EnvironmentLinkTypeDef

### LinkName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# EnvironmentResourceDescriptionTypeDef

### EnvironmentName
- **Type**: typing.Optional[str]

### AutoScalingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.AutoScalingGroupTypeDef]]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.InstanceTypeDef]]

### LaunchConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.LaunchConfigurationTypeDef]]

### LaunchTemplates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.LaunchTemplateTypeDef]]

### LoadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.LoadBalancerTypeDef]]

### Triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TriggerTypeDef]]

### Queues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.QueueTypeDef]]


# EnvironmentResourceDescriptionsMessageTypeDef

### EnvironmentResources
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentResourceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentResourcesDescriptionTypeDef

### LoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.LoadBalancerDescriptionTypeDef]


# EnvironmentTierTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# EventDescriptionTypeDef

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


# EventDescriptionsMessageTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EventDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# InstanceHealthSummaryTypeDef

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


# InstanceTypeDef

### Id
- **Type**: typing.Optional[str]


# LatencyTypeDef

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


# LaunchConfigurationTypeDef

### Name
- **Type**: typing.Optional[str]


# LaunchTemplateTypeDef

### Id
- **Type**: typing.Optional[str]


# ListAvailableSolutionStacksResultMessageTypeDef

### SolutionStacks
- **Type**: typing.List[str]
- **Required**: Yes

### SolutionStackDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.SolutionStackDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPlatformBranchesRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.SearchFilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformBranchesResultTypeDef

### PlatformBranchSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformBranchSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformVersionsRequestListPlatformVersionsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PaginatorConfigTypeDef]


# ListPlatformVersionsRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformFilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformVersionsResultTypeDef

### PlatformSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceMessageRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListenerTypeDef

### Protocol
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# LoadBalancerDescriptionTypeDef

### LoadBalancerName
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Listeners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ListenerTypeDef]]


# LoadBalancerTypeDef

### Name
- **Type**: typing.Optional[str]


# ManagedActionHistoryItemTypeDef

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


# ManagedActionTypeDef

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


# MaxAgeRuleTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxAgeInDays
- **Type**: typing.Optional[int]

### DeleteSourceFromS3
- **Type**: typing.Optional[bool]


# MaxCountRuleTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxCount
- **Type**: typing.Optional[int]

### DeleteSourceFromS3
- **Type**: typing.Optional[bool]


# OptionRestrictionRegexTypeDef

### Pattern
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]


# OptionSpecificationTypeDef

### ResourceName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlatformBranchSummaryTypeDef

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


# PlatformDescriptionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformProgrammingLanguageTypeDef]]

### Frameworks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.PlatformFrameworkTypeDef]]

### CustomAmiList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.CustomAmiTypeDef]]

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


# PlatformFilterTypeDef

### Type
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# PlatformFrameworkTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# PlatformProgrammingLanguageTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# PlatformSummaryTypeDef

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


# QueueTypeDef

### Name
- **Type**: typing.Optional[str]

### URL
- **Type**: typing.Optional[str]


# RebuildEnvironmentMessageRequestTypeDef

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# RequestEnvironmentInfoMessageRequestTypeDef

### InfoType
- **Type**: typing.Literal['bundle', 'tail']
- **Required**: Yes

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# ResourceQuotaTypeDef

### Maximum
- **Type**: typing.Optional[int]


# ResourceQuotasTypeDef

### ApplicationQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResourceQuotaTypeDef]

### ApplicationVersionQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResourceQuotaTypeDef]

### EnvironmentQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResourceQuotaTypeDef]

### ConfigurationTemplateQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResourceQuotaTypeDef]

### CustomPlatformQuota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResourceQuotaTypeDef]


# ResourceTagsDescriptionMessageTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RestartAppServerMessageRequestTypeDef

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# RetrieveEnvironmentInfoMessageRequestTypeDef

### InfoType
- **Type**: typing.Literal['bundle', 'tail']
- **Required**: Yes

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# RetrieveEnvironmentInfoResultMessageTypeDef

### EnvironmentInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentInfoDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3LocationTypeDef

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]


# SearchFilterTypeDef

### Attribute
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# SingleInstanceHealthTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationMetricsTypeDef]

### System
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.SystemStatusTypeDef]

### Deployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.DeploymentTypeDef]

### AvailabilityZone
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]


# SolutionStackDescriptionTypeDef

### SolutionStackName
- **Type**: typing.Optional[str]

### PermittedFileTypes
- **Type**: typing.Optional[typing.List[str]]


# SourceBuildInformationTypeDef

### SourceType
- **Type**: typing.Literal['Git', 'Zip']
- **Required**: Yes

### SourceRepository
- **Type**: typing.Literal['CodeCommit', 'S3']
- **Required**: Yes

### SourceLocation
- **Type**: <class 'str'>
- **Required**: Yes


# SourceConfigurationTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]


# StatusCodesTypeDef

### Status2xx
- **Type**: typing.Optional[int]

### Status3xx
- **Type**: typing.Optional[int]

### Status4xx
- **Type**: typing.Optional[int]

### Status5xx
- **Type**: typing.Optional[int]


# SwapEnvironmentCNAMEsMessageRequestTypeDef

### SourceEnvironmentId
- **Type**: typing.Optional[str]

### SourceEnvironmentName
- **Type**: typing.Optional[str]

### DestinationEnvironmentId
- **Type**: typing.Optional[str]

### DestinationEnvironmentName
- **Type**: typing.Optional[str]


# SystemStatusTypeDef

### CPUUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.CPUUtilizationTypeDef]

### LoadAverage
- **Type**: typing.Optional[typing.List[float]]


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TerminateEnvironmentMessageRequestTypeDef

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]

### TerminateResources
- **Type**: typing.Optional[bool]

### ForceTerminate
- **Type**: typing.Optional[bool]


# TriggerTypeDef

### Name
- **Type**: typing.Optional[str]


# UpdateApplicationMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateApplicationResourceLifecycleMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceLifecycleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ApplicationResourceLifecycleConfigTypeDef'>
- **Required**: Yes


# UpdateApplicationVersionMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationTemplateMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]]

### OptionsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.OptionSpecificationTypeDef]]


# UpdateEnvironmentMessageRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.EnvironmentTierTypeDef]

### VersionLabel
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### PlatformArn
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]]

### OptionsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.OptionSpecificationTypeDef]]


# UpdateTagsForResourceMessageRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.TagTypeDef]]

### TagsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# ValidateConfigurationSettingsMessageRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### OptionSettings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticbeanstalk_classes.ConfigurationOptionSettingTypeDef]
- **Required**: Yes

### TemplateName
- **Type**: typing.Optional[str]

### EnvironmentName
- **Type**: typing.Optional[str]


# ValidationMessageTypeDef

### Message
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['error', 'warning']]

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


