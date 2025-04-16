# Kinesisanalyticsv2 Classes

# AddApplicationCloudWatchLoggingOptionRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLoggingOption
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOption'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ConditionalToken
- **Type**: typing.Optional[str]


# AddApplicationCloudWatchLoggingOptionResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionDescription]
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# AddApplicationInputProcessingConfigurationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### InputProcessingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfiguration'>
- **Required**: Yes


# AddApplicationInputProcessingConfigurationResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### InputProcessingConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfigurationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# AddApplicationInputRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Input'>
- **Required**: Yes


# AddApplicationInputResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# AddApplicationOutputRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Output'>
- **Required**: Yes


# AddApplicationOutputResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### OutputDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# AddApplicationReferenceDataSourceRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSource'>
- **Required**: Yes


# AddApplicationReferenceDataSourceResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceDataSourceDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# AddApplicationVpcConfigurationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfiguration'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ConditionalToken
- **Type**: typing.Optional[str]


# AddApplicationVpcConfigurationResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### VpcConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationDescription'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# ApplicationCodeConfiguration

### CodeContentType
- **Type**: typing.Literal['PLAINTEXT', 'ZIPFILE']
- **Required**: Yes

### CodeContent
- **Type**: <class 'NoneType'>


# ApplicationCodeConfigurationDescription

### CodeContentType
- **Type**: typing.Literal['PLAINTEXT', 'ZIPFILE']
- **Required**: Yes

### CodeContentDescription
- **Type**: <class 'NoneType'>


# ApplicationCodeConfigurationUpdate

### CodeContentTypeUpdate
- **Type**: typing.Optional[typing.Literal['PLAINTEXT', 'ZIPFILE']]

### CodeContentUpdate
- **Type**: <class 'NoneType'>


# ApplicationConfiguration

### SqlApplicationConfiguration
- **Type**: <class 'NoneType'>

### FlinkApplicationConfiguration
- **Type**: <class 'NoneType'>

### EnvironmentProperties
- **Type**: <class 'NoneType'>

### ApplicationCodeConfiguration
- **Type**: <class 'NoneType'>

### ApplicationSnapshotConfiguration
- **Type**: <class 'NoneType'>

### ApplicationSystemRollbackConfiguration
- **Type**: <class 'NoneType'>

### VpcConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfiguration]]

### ZeppelinApplicationConfiguration
- **Type**: <class 'NoneType'>


# ApplicationConfigurationDescription

### SqlApplicationConfigurationDescription
- **Type**: <class 'NoneType'>

### ApplicationCodeConfigurationDescription
- **Type**: <class 'NoneType'>

### RunConfigurationDescription
- **Type**: <class 'NoneType'>

### FlinkApplicationConfigurationDescription
- **Type**: <class 'NoneType'>

### EnvironmentPropertyDescriptions
- **Type**: <class 'NoneType'>

### ApplicationSnapshotConfigurationDescription
- **Type**: <class 'NoneType'>

### ApplicationSystemRollbackConfigurationDescription
- **Type**: <class 'NoneType'>

### VpcConfigurationDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationDescription]]

### ZeppelinApplicationConfigurationDescription
- **Type**: <class 'NoneType'>


# ApplicationConfigurationUpdate

### SqlApplicationConfigurationUpdate
- **Type**: <class 'NoneType'>

### ApplicationCodeConfigurationUpdate
- **Type**: <class 'NoneType'>

### FlinkApplicationConfigurationUpdate
- **Type**: <class 'NoneType'>

### EnvironmentPropertyUpdates
- **Type**: <class 'NoneType'>

### ApplicationSnapshotConfigurationUpdate
- **Type**: <class 'NoneType'>

### ApplicationSystemRollbackConfigurationUpdate
- **Type**: <class 'NoneType'>

### VpcConfigurationUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationUpdate]]

### ZeppelinApplicationConfigurationUpdate
- **Type**: <class 'NoneType'>


# ApplicationDetail

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeEnvironment
- **Type**: typing.Literal['FLINK-1_11', 'FLINK-1_13', 'FLINK-1_15', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-1_6', 'FLINK-1_8', 'SQL-1_0', 'ZEPPELIN-FLINK-1_0', 'ZEPPELIN-FLINK-2_0', 'ZEPPELIN-FLINK-3_0']
- **Required**: Yes

### ApplicationStatus
- **Type**: typing.Literal['AUTOSCALING', 'DELETING', 'FORCE_STOPPING', 'MAINTENANCE', 'READY', 'ROLLED_BACK', 'ROLLING_BACK', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationDescription
- **Type**: typing.Optional[str]

### ServiceExecutionRole
- **Type**: typing.Optional[str]

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ApplicationConfigurationDescription
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionDescription]]

### ApplicationMaintenanceConfigurationDescription
- **Type**: <class 'NoneType'>

### ApplicationVersionUpdatedFrom
- **Type**: typing.Optional[int]

### ApplicationVersionRolledBackFrom
- **Type**: typing.Optional[int]

### ApplicationVersionCreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ConditionalToken
- **Type**: typing.Optional[str]

### ApplicationVersionRolledBackTo
- **Type**: typing.Optional[int]

### ApplicationMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'STREAMING']]


# ApplicationMaintenanceConfigurationDescription

### ApplicationMaintenanceWindowStartTime
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationMaintenanceWindowEndTime
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationMaintenanceConfigurationUpdate

### ApplicationMaintenanceWindowStartTimeUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationOperationInfo

### Operation
- **Type**: typing.Optional[str]

### OperationId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### OperationStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']]


# ApplicationOperationInfoDetails

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OperationStatus
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']
- **Required**: Yes

### ApplicationVersionChangeDetails
- **Type**: <class 'NoneType'>

### OperationFailureDetails
- **Type**: <class 'NoneType'>


# ApplicationRestoreConfiguration

### ApplicationRestoreType
- **Type**: typing.Literal['RESTORE_FROM_CUSTOM_SNAPSHOT', 'RESTORE_FROM_LATEST_SNAPSHOT', 'SKIP_RESTORE_FROM_SNAPSHOT']
- **Required**: Yes

### SnapshotName
- **Type**: typing.Optional[str]


# ApplicationSnapshotConfiguration

### SnapshotsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSnapshotConfigurationDescription

### SnapshotsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSnapshotConfigurationUpdate

### SnapshotsEnabledUpdate
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSummary

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationStatus
- **Type**: typing.Literal['AUTOSCALING', 'DELETING', 'FORCE_STOPPING', 'MAINTENANCE', 'READY', 'ROLLED_BACK', 'ROLLING_BACK', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### RuntimeEnvironment
- **Type**: typing.Literal['FLINK-1_11', 'FLINK-1_13', 'FLINK-1_15', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-1_6', 'FLINK-1_8', 'SQL-1_0', 'ZEPPELIN-FLINK-1_0', 'ZEPPELIN-FLINK-2_0', 'ZEPPELIN-FLINK-3_0']
- **Required**: Yes

### ApplicationMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'STREAMING']]


# ApplicationSystemRollbackConfiguration

### RollbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSystemRollbackConfigurationDescription

### RollbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSystemRollbackConfigurationUpdate

### RollbackEnabledUpdate
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationVersionChangeDetails

### ApplicationVersionUpdatedFrom
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationVersionUpdatedTo
- **Type**: <class 'int'>
- **Required**: Yes


# ApplicationVersionSummary

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationStatus
- **Type**: typing.Literal['AUTOSCALING', 'DELETING', 'FORCE_STOPPING', 'MAINTENANCE', 'READY', 'ROLLED_BACK', 'ROLLING_BACK', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CSVMappingParameters

### RecordRowDelimiter
- **Type**: <class 'str'>
- **Required**: Yes

### RecordColumnDelimiter
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogConfiguration

### GlueDataCatalogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.GlueDataCatalogConfiguration'>
- **Required**: Yes


# CatalogConfigurationDescription

### GlueDataCatalogConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.GlueDataCatalogConfigurationDescription'>
- **Required**: Yes


# CatalogConfigurationUpdate

### GlueDataCatalogConfigurationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.GlueDataCatalogConfigurationUpdate'>
- **Required**: Yes


# CheckpointConfiguration

### ConfigurationType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### CheckpointingEnabled
- **Type**: typing.Optional[bool]

### CheckpointInterval
- **Type**: typing.Optional[int]

### MinPauseBetweenCheckpoints
- **Type**: typing.Optional[int]


# CheckpointConfigurationDescription

### ConfigurationType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### CheckpointingEnabled
- **Type**: typing.Optional[bool]

### CheckpointInterval
- **Type**: typing.Optional[int]

### MinPauseBetweenCheckpoints
- **Type**: typing.Optional[int]


# CheckpointConfigurationUpdate

### ConfigurationTypeUpdate
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### CheckpointingEnabledUpdate
- **Type**: typing.Optional[bool]

### CheckpointIntervalUpdate
- **Type**: typing.Optional[int]

### MinPauseBetweenCheckpointsUpdate
- **Type**: typing.Optional[int]


# CloudWatchLoggingOption

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLoggingOptionDescription

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLoggingOptionId
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# CloudWatchLoggingOptionUpdate

### CloudWatchLoggingOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### LogStreamARNUpdate
- **Type**: typing.Optional[str]


# CodeContent

### TextContent
- **Type**: typing.Optional[str]

### ZipFileContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Blob]

### S3ContentLocation
- **Type**: <class 'NoneType'>


# CodeContentDescription

### TextContent
- **Type**: typing.Optional[str]

### CodeMD5
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]

### S3ApplicationCodeLocationDescription
- **Type**: <class 'NoneType'>


# CodeContentUpdate

### TextContentUpdate
- **Type**: typing.Optional[str]

### ZipFileContentUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Blob]

### S3ContentLocationUpdate
- **Type**: <class 'NoneType'>


# CreateApplicationPresignedUrlRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### UrlType
- **Type**: typing.Literal['FLINK_DASHBOARD_URL', 'ZEPPELIN_UI_URL']
- **Required**: Yes

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreateApplicationPresignedUrlResponse

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeEnvironment
- **Type**: typing.Literal['FLINK-1_11', 'FLINK-1_13', 'FLINK-1_15', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-1_6', 'FLINK-1_8', 'SQL-1_0', 'ZEPPELIN-FLINK-1_0', 'ZEPPELIN-FLINK-2_0', 'ZEPPELIN-FLINK-3_0']
- **Required**: Yes

### ServiceExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationDescription
- **Type**: typing.Optional[str]

### ApplicationConfiguration
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOption]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Tag]]

### ApplicationMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'STREAMING']]


# CreateApplicationResponse

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApplicationSnapshotRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# CustomArtifactConfiguration

### ArtifactType
- **Type**: typing.Literal['DEPENDENCY_JAR', 'UDF']
- **Required**: Yes

### S3ContentLocation
- **Type**: <class 'NoneType'>

### MavenReference
- **Type**: <class 'NoneType'>


# CustomArtifactConfigurationDescription

### ArtifactType
- **Type**: typing.Optional[typing.Literal['DEPENDENCY_JAR', 'UDF']]

### S3ContentLocationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentLocation]

### MavenReferenceDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.MavenReference]


# DeleteApplicationCloudWatchLoggingOptionRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLoggingOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ConditionalToken
- **Type**: typing.Optional[str]


# DeleteApplicationCloudWatchLoggingOptionResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionDescription]
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationInputProcessingConfigurationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationInputProcessingConfigurationResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationOutputRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationOutputResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationReferenceDataSourceRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationReferenceDataSourceResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Timestamp'>
- **Required**: Yes


# DeleteApplicationSnapshotRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotCreationTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Timestamp'>
- **Required**: Yes


# DeleteApplicationVpcConfigurationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ConditionalToken
- **Type**: typing.Optional[str]


# DeleteApplicationVpcConfigurationResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeployAsApplicationConfiguration

### S3ContentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentBaseLocation'>
- **Required**: Yes


# DeployAsApplicationConfigurationDescription

### S3ContentLocationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentBaseLocationDescription'>
- **Required**: Yes


# DeployAsApplicationConfigurationUpdate

### S3ContentLocationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentBaseLocationUpdate]


# DescribeApplicationOperationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationOperationResponse

### ApplicationOperationInfoDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationOperationInfoDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeAdditionalDetails
- **Type**: typing.Optional[bool]


# DescribeApplicationResponse

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationSnapshotRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationSnapshotResponse

### SnapshotDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SnapshotDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationVersionRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeApplicationVersionResponse

### ApplicationVersionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationSchema

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# DiscoverInputSchemaRequest

### ServiceExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceARN
- **Type**: typing.Optional[str]

### InputStartingPositionConfiguration
- **Type**: <class 'NoneType'>

### S3Configuration
- **Type**: <class 'NoneType'>

### InputProcessingConfiguration
- **Type**: <class 'NoneType'>


# DiscoverInputSchemaResponse

### InputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaOutput'>
- **Required**: Yes

### ParsedInputRecords
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ProcessedInputRecords
- **Type**: typing.List[str]
- **Required**: Yes

### RawInputRecords
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# EnvironmentProperties

### PropertyGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PropertyGroupUnion]
- **Required**: Yes


# EnvironmentPropertyDescriptions

### PropertyGroupDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PropertyGroupOutput]]


# EnvironmentPropertyUpdates

### PropertyGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PropertyGroupUnion]
- **Required**: Yes


# ErrorInfo

### ErrorString
- **Type**: typing.Optional[str]


# FlinkApplicationConfiguration

### CheckpointConfiguration
- **Type**: <class 'NoneType'>

### MonitoringConfiguration
- **Type**: <class 'NoneType'>

### ParallelismConfiguration
- **Type**: <class 'NoneType'>


# FlinkApplicationConfigurationDescription

### CheckpointConfigurationDescription
- **Type**: <class 'NoneType'>

### MonitoringConfigurationDescription
- **Type**: <class 'NoneType'>

### ParallelismConfigurationDescription
- **Type**: <class 'NoneType'>

### JobPlanDescription
- **Type**: typing.Optional[str]


# FlinkApplicationConfigurationUpdate

### CheckpointConfigurationUpdate
- **Type**: <class 'NoneType'>

### MonitoringConfigurationUpdate
- **Type**: <class 'NoneType'>

### ParallelismConfigurationUpdate
- **Type**: <class 'NoneType'>


# FlinkRunConfiguration

### AllowNonRestoredState
- **Type**: typing.Optional[bool]


# GlueDataCatalogConfiguration

### DatabaseARN
- **Type**: <class 'str'>
- **Required**: Yes


# GlueDataCatalogConfigurationDescription

### DatabaseARN
- **Type**: <class 'str'>
- **Required**: Yes


# GlueDataCatalogConfigurationUpdate

### DatabaseARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# Input

### NamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### InputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaUnion'>
- **Required**: Yes

### InputProcessingConfiguration
- **Type**: <class 'NoneType'>

### KinesisStreamsInput
- **Type**: <class 'NoneType'>

### KinesisFirehoseInput
- **Type**: <class 'NoneType'>

### InputParallelism
- **Type**: <class 'NoneType'>


# InputDescription

### InputId
- **Type**: typing.Optional[str]

### NamePrefix
- **Type**: typing.Optional[str]

### InAppStreamNames
- **Type**: typing.Optional[typing.List[str]]

### InputProcessingConfigurationDescription
- **Type**: <class 'NoneType'>

### KinesisStreamsInputDescription
- **Type**: <class 'NoneType'>

### KinesisFirehoseInputDescription
- **Type**: <class 'NoneType'>

### InputSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaOutput]

### InputParallelism
- **Type**: <class 'NoneType'>

### InputStartingPositionConfiguration
- **Type**: <class 'NoneType'>


# InputLambdaProcessor

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# InputLambdaProcessorDescription

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# InputLambdaProcessorUpdate

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# InputParallelism

### Count
- **Type**: typing.Optional[int]


# InputParallelismUpdate

### CountUpdate
- **Type**: <class 'int'>
- **Required**: Yes


# InputProcessingConfiguration

### InputLambdaProcessor
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputLambdaProcessor'>
- **Required**: Yes


# InputProcessingConfigurationDescription

### InputLambdaProcessorDescription
- **Type**: <class 'NoneType'>


# InputProcessingConfigurationUpdate

### InputLambdaProcessorUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputLambdaProcessorUpdate'>
- **Required**: Yes


# InputSchemaUpdate

### RecordFormatUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordFormat]

### RecordEncodingUpdate
- **Type**: typing.Optional[str]

### RecordColumnUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordColumn]]


# InputStartingPositionConfiguration

### InputStartingPosition
- **Type**: typing.Optional[typing.Literal['LAST_STOPPED_POINT', 'NOW', 'TRIM_HORIZON']]


# InputUpdate

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### NamePrefixUpdate
- **Type**: typing.Optional[str]

### InputProcessingConfigurationUpdate
- **Type**: <class 'NoneType'>

### KinesisStreamsInputUpdate
- **Type**: <class 'NoneType'>

### KinesisFirehoseInputUpdate
- **Type**: <class 'NoneType'>

### InputSchemaUpdate
- **Type**: <class 'NoneType'>

### InputParallelismUpdate
- **Type**: <class 'NoneType'>


# JSONMappingParameters

### RecordRowPath
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInputDescription

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseInputUpdate

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseOutputDescription

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseOutputUpdate

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsInputDescription

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsInputUpdate

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsOutputDescription

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsOutputUpdate

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaOutputDescription

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# LambdaOutputUpdate

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# ListApplicationOperationsRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### OperationStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']]


# ListApplicationOperationsRequestPaginate

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Optional[str]

### OperationStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfig]


# ListApplicationOperationsResponse

### ApplicationOperationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationOperationInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationSnapshotsRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationSnapshotsRequestPaginate

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfig]


# ListApplicationSnapshotsResponse

### SnapshotSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SnapshotDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequestPaginate

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfig]


# ListApplicationVersionsResponse

### ApplicationVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfig]


# ListApplicationsResponse

### ApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# MappingParameters

### JSONMappingParameters
- **Type**: <class 'NoneType'>

### CSVMappingParameters
- **Type**: <class 'NoneType'>


# MavenReference

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes


# MonitoringConfiguration

### ConfigurationType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### MetricsLevel
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OPERATOR', 'PARALLELISM', 'TASK']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# MonitoringConfigurationDescription

### ConfigurationType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### MetricsLevel
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OPERATOR', 'PARALLELISM', 'TASK']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# MonitoringConfigurationUpdate

### ConfigurationTypeUpdate
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### MetricsLevelUpdate
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OPERATOR', 'PARALLELISM', 'TASK']]

### LogLevelUpdate
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# OperationFailureDetails

### RollbackOperationId
- **Type**: typing.Optional[str]

### ErrorInfo
- **Type**: <class 'NoneType'>


# Output

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DestinationSchema'>
- **Required**: Yes

### KinesisStreamsOutput
- **Type**: <class 'NoneType'>

### KinesisFirehoseOutput
- **Type**: <class 'NoneType'>

### LambdaOutput
- **Type**: <class 'NoneType'>


# OutputDescription

### OutputId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### KinesisStreamsOutputDescription
- **Type**: <class 'NoneType'>

### KinesisFirehoseOutputDescription
- **Type**: <class 'NoneType'>

### LambdaOutputDescription
- **Type**: <class 'NoneType'>

### DestinationSchema
- **Type**: <class 'NoneType'>


# OutputUpdate

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes

### NameUpdate
- **Type**: typing.Optional[str]

### KinesisStreamsOutputUpdate
- **Type**: <class 'NoneType'>

### KinesisFirehoseOutputUpdate
- **Type**: <class 'NoneType'>

### LambdaOutputUpdate
- **Type**: <class 'NoneType'>

### DestinationSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DestinationSchema]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParallelismConfiguration

### ConfigurationType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### Parallelism
- **Type**: typing.Optional[int]

### ParallelismPerKPU
- **Type**: typing.Optional[int]

### AutoScalingEnabled
- **Type**: typing.Optional[bool]


# ParallelismConfigurationDescription

### ConfigurationType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### Parallelism
- **Type**: typing.Optional[int]

### ParallelismPerKPU
- **Type**: typing.Optional[int]

### CurrentParallelism
- **Type**: typing.Optional[int]

### AutoScalingEnabled
- **Type**: typing.Optional[bool]


# ParallelismConfigurationUpdate

### ConfigurationTypeUpdate
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### ParallelismUpdate
- **Type**: typing.Optional[int]

### ParallelismPerKPUUpdate
- **Type**: typing.Optional[int]

### AutoScalingEnabledUpdate
- **Type**: typing.Optional[bool]


# PropertyGroup

### PropertyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PropertyMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# PropertyGroupOutput

### PropertyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PropertyMap
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# PropertyGroupUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordColumn

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordFormat

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### MappingParameters
- **Type**: <class 'NoneType'>


# ReferenceDataSource

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaUnion'>
- **Required**: Yes

### S3ReferenceDataSource
- **Type**: <class 'NoneType'>


# ReferenceDataSourceDescription

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### S3ReferenceDataSourceDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ReferenceDataSourceDescription'>
- **Required**: Yes

### ReferenceSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaOutput]


# ReferenceDataSourceUpdate

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableNameUpdate
- **Type**: typing.Optional[str]

### S3ReferenceDataSourceUpdate
- **Type**: <class 'NoneType'>

### ReferenceSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaUnion]


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


# RollbackApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# RollbackApplicationResponse

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetail'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# RunConfiguration

### FlinkRunConfiguration
- **Type**: <class 'NoneType'>

### SqlRunConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SqlRunConfiguration]]

### ApplicationRestoreConfiguration
- **Type**: <class 'NoneType'>


# RunConfigurationDescription

### ApplicationRestoreConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationRestoreConfiguration]

### FlinkRunConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.FlinkRunConfiguration]


# RunConfigurationUpdate

### FlinkRunConfiguration
- **Type**: <class 'NoneType'>

### ApplicationRestoreConfiguration
- **Type**: <class 'NoneType'>


# S3ApplicationCodeLocationDescription

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectVersion
- **Type**: typing.Optional[str]


# S3Configuration

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes


# S3ContentBaseLocation

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BasePath
- **Type**: typing.Optional[str]


# S3ContentBaseLocationDescription

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BasePath
- **Type**: typing.Optional[str]


# S3ContentBaseLocationUpdate

### BucketARNUpdate
- **Type**: typing.Optional[str]

### BasePathUpdate
- **Type**: typing.Optional[str]


# S3ContentLocation

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectVersion
- **Type**: typing.Optional[str]


# S3ContentLocationUpdate

### BucketARNUpdate
- **Type**: typing.Optional[str]

### FileKeyUpdate
- **Type**: typing.Optional[str]

### ObjectVersionUpdate
- **Type**: typing.Optional[str]


# S3ReferenceDataSource

### BucketARN
- **Type**: typing.Optional[str]

### FileKey
- **Type**: typing.Optional[str]


# S3ReferenceDataSourceDescription

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceRoleARN
- **Type**: typing.Optional[str]


# S3ReferenceDataSourceUpdate

### BucketARNUpdate
- **Type**: typing.Optional[str]

### FileKeyUpdate
- **Type**: typing.Optional[str]


# SnapshotDetails

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY']
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### SnapshotCreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RuntimeEnvironment
- **Type**: typing.Optional[typing.Literal['FLINK-1_11', 'FLINK-1_13', 'FLINK-1_15', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-1_6', 'FLINK-1_8', 'SQL-1_0', 'ZEPPELIN-FLINK-1_0', 'ZEPPELIN-FLINK-2_0', 'ZEPPELIN-FLINK-3_0']]


# SourceSchema

### RecordFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordFormat'>
- **Required**: Yes

### RecordColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordColumn]
- **Required**: Yes

### RecordEncoding
- **Type**: typing.Optional[str]


# SourceSchemaOutput

### RecordFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordFormat'>
- **Required**: Yes

### RecordColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordColumn]
- **Required**: Yes

### RecordEncoding
- **Type**: typing.Optional[str]


# SourceSchemaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SqlApplicationConfiguration

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Input]]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Output]]

### ReferenceDataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSource]]


# SqlApplicationConfigurationDescription

### InputDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputDescription]]

### OutputDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputDescription]]

### ReferenceDataSourceDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceDescription]]


# SqlApplicationConfigurationUpdate

### InputUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputUpdate]]

### OutputUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputUpdate]]

### ReferenceDataSourceUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceUpdate]]


# SqlRunConfiguration

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### InputStartingPositionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputStartingPositionConfiguration'>
- **Required**: Yes


# StartApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### RunConfiguration
- **Type**: <class 'NoneType'>


# StartApplicationResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# StopApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# StopApplicationResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.Tag]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationMaintenanceConfigurationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationMaintenanceConfigurationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationMaintenanceConfigurationUpdate'>
- **Required**: Yes


# UpdateApplicationMaintenanceConfigurationResponse

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationMaintenanceConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationMaintenanceConfigurationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ApplicationConfigurationUpdate
- **Type**: <class 'NoneType'>

### ServiceExecutionRoleUpdate
- **Type**: typing.Optional[str]

### RunConfigurationUpdate
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptionUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionUpdate]]

### ConditionalToken
- **Type**: typing.Optional[str]

### RuntimeEnvironmentUpdate
- **Type**: typing.Optional[typing.Literal['FLINK-1_11', 'FLINK-1_13', 'FLINK-1_15', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-1_6', 'FLINK-1_8', 'SQL-1_0', 'ZEPPELIN-FLINK-1_0', 'ZEPPELIN-FLINK-2_0', 'ZEPPELIN-FLINK-3_0']]


# UpdateApplicationResponse

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetail'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadata'>
- **Required**: Yes


# VpcConfiguration

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VpcConfigurationDescription

### VpcConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigurationUpdate

### VpcConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIdUpdates
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIdUpdates
- **Type**: typing.Optional[typing.Sequence[str]]


# ZeppelinApplicationConfiguration

### MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinMonitoringConfiguration]

### CatalogConfiguration
- **Type**: <class 'NoneType'>

### DeployAsApplicationConfiguration
- **Type**: <class 'NoneType'>

### CustomArtifactsConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CustomArtifactConfiguration]]


# ZeppelinApplicationConfigurationDescription

### MonitoringConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinMonitoringConfigurationDescription'>
- **Required**: Yes

### CatalogConfigurationDescription
- **Type**: <class 'NoneType'>

### DeployAsApplicationConfigurationDescription
- **Type**: <class 'NoneType'>

### CustomArtifactsConfigurationDescription
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CustomArtifactConfigurationDescription]]


# ZeppelinApplicationConfigurationUpdate

### MonitoringConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinMonitoringConfigurationUpdate]

### CatalogConfigurationUpdate
- **Type**: <class 'NoneType'>

### DeployAsApplicationConfigurationUpdate
- **Type**: <class 'NoneType'>

### CustomArtifactsConfigurationUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CustomArtifactConfiguration]]


# ZeppelinMonitoringConfiguration

### LogLevel
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# ZeppelinMonitoringConfigurationDescription

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# ZeppelinMonitoringConfigurationUpdate

### LogLevelUpdate
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


