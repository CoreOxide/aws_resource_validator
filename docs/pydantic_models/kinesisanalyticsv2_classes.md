# Kinesisanalyticsv2 Classes

# AddApplicationCloudWatchLoggingOptionRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLoggingOption
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionTypeDef'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ConditionalToken
- **Type**: typing.Optional[str]


# AddApplicationCloudWatchLoggingOptionResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionDescriptionTypeDef]
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddApplicationInputProcessingConfigurationRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfigurationTypeDef'>
- **Required**: Yes


# AddApplicationInputProcessingConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfigurationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddApplicationInputRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputTypeDef'>
- **Required**: Yes


# AddApplicationInputResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddApplicationOutputRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputTypeDef'>
- **Required**: Yes


# AddApplicationOutputResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### OutputDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddApplicationReferenceDataSourceRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceTypeDef'>
- **Required**: Yes


# AddApplicationReferenceDataSourceResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceDataSourceDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddApplicationVpcConfigurationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationTypeDef'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ConditionalToken
- **Type**: typing.Optional[str]


# AddApplicationVpcConfigurationResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### VpcConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationDescriptionTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationCodeConfigurationDescriptionTypeDef

### CodeContentType
- **Type**: typing.Literal['PLAINTEXT', 'ZIPFILE']
- **Required**: Yes

### CodeContentDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CodeContentDescriptionTypeDef]


# ApplicationCodeConfigurationTypeDef

### CodeContentType
- **Type**: typing.Literal['PLAINTEXT', 'ZIPFILE']
- **Required**: Yes

### CodeContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CodeContentTypeDef]


# ApplicationCodeConfigurationUpdateTypeDef

### CodeContentTypeUpdate
- **Type**: typing.Optional[typing.Literal['PLAINTEXT', 'ZIPFILE']]

### CodeContentUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CodeContentUpdateTypeDef]


# ApplicationConfigurationDescriptionTypeDef

### SqlApplicationConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SqlApplicationConfigurationDescriptionTypeDef]

### ApplicationCodeConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationCodeConfigurationDescriptionTypeDef]

### RunConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RunConfigurationDescriptionTypeDef]

### FlinkApplicationConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.FlinkApplicationConfigurationDescriptionTypeDef]

### EnvironmentPropertyDescriptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.EnvironmentPropertyDescriptionsTypeDef]

### ApplicationSnapshotConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSnapshotConfigurationDescriptionTypeDef]

### ApplicationSystemRollbackConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSystemRollbackConfigurationDescriptionTypeDef]

### VpcConfigurationDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationDescriptionTypeDef]]

### ZeppelinApplicationConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinApplicationConfigurationDescriptionTypeDef]


# ApplicationConfigurationTypeDef

### SqlApplicationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SqlApplicationConfigurationTypeDef]

### FlinkApplicationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.FlinkApplicationConfigurationTypeDef]

### EnvironmentProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.EnvironmentPropertiesTypeDef]

### ApplicationCodeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationCodeConfigurationTypeDef]

### ApplicationSnapshotConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSnapshotConfigurationTypeDef]

### ApplicationSystemRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSystemRollbackConfigurationTypeDef]

### VpcConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationTypeDef]]

### ZeppelinApplicationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinApplicationConfigurationTypeDef]


# ApplicationConfigurationUpdateTypeDef

### SqlApplicationConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SqlApplicationConfigurationUpdateTypeDef]

### ApplicationCodeConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationCodeConfigurationUpdateTypeDef]

### FlinkApplicationConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.FlinkApplicationConfigurationUpdateTypeDef]

### EnvironmentPropertyUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.EnvironmentPropertyUpdatesTypeDef]

### ApplicationSnapshotConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSnapshotConfigurationUpdateTypeDef]

### ApplicationSystemRollbackConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSystemRollbackConfigurationUpdateTypeDef]

### VpcConfigurationUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.VpcConfigurationUpdateTypeDef]]

### ZeppelinApplicationConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinApplicationConfigurationUpdateTypeDef]


# ApplicationDetailTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationConfigurationDescriptionTypeDef]

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionDescriptionTypeDef]]

### ApplicationMaintenanceConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationMaintenanceConfigurationDescriptionTypeDef]

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


# ApplicationMaintenanceConfigurationDescriptionTypeDef

### ApplicationMaintenanceWindowStartTime
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationMaintenanceWindowEndTime
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationMaintenanceConfigurationUpdateTypeDef

### ApplicationMaintenanceWindowStartTimeUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationOperationInfoDetailsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationVersionChangeDetailsTypeDef]

### OperationFailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OperationFailureDetailsTypeDef]


# ApplicationOperationInfoTypeDef

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


# ApplicationRestoreConfigurationTypeDef

### ApplicationRestoreType
- **Type**: typing.Literal['RESTORE_FROM_CUSTOM_SNAPSHOT', 'RESTORE_FROM_LATEST_SNAPSHOT', 'SKIP_RESTORE_FROM_SNAPSHOT']
- **Required**: Yes

### SnapshotName
- **Type**: typing.Optional[str]


# ApplicationSnapshotConfigurationDescriptionTypeDef

### SnapshotsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSnapshotConfigurationTypeDef

### SnapshotsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSnapshotConfigurationUpdateTypeDef

### SnapshotsEnabledUpdate
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSummaryTypeDef

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


# ApplicationSystemRollbackConfigurationDescriptionTypeDef

### RollbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSystemRollbackConfigurationTypeDef

### RollbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationSystemRollbackConfigurationUpdateTypeDef

### RollbackEnabledUpdate
- **Type**: <class 'bool'>
- **Required**: Yes


# ApplicationVersionChangeDetailsTypeDef

### ApplicationVersionUpdatedFrom
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationVersionUpdatedTo
- **Type**: <class 'int'>
- **Required**: Yes


# ApplicationVersionSummaryTypeDef

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationStatus
- **Type**: typing.Literal['AUTOSCALING', 'DELETING', 'FORCE_STOPPING', 'MAINTENANCE', 'READY', 'ROLLED_BACK', 'ROLLING_BACK', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CSVMappingParametersTypeDef

### RecordRowDelimiter
- **Type**: <class 'str'>
- **Required**: Yes

### RecordColumnDelimiter
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogConfigurationDescriptionTypeDef

### GlueDataCatalogConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.GlueDataCatalogConfigurationDescriptionTypeDef'>
- **Required**: Yes


# CatalogConfigurationTypeDef

### GlueDataCatalogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.GlueDataCatalogConfigurationTypeDef'>
- **Required**: Yes


# CatalogConfigurationUpdateTypeDef

### GlueDataCatalogConfigurationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.GlueDataCatalogConfigurationUpdateTypeDef'>
- **Required**: Yes


# CheckpointConfigurationDescriptionTypeDef

### ConfigurationType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### CheckpointingEnabled
- **Type**: typing.Optional[bool]

### CheckpointInterval
- **Type**: typing.Optional[int]

### MinPauseBetweenCheckpoints
- **Type**: typing.Optional[int]


# CheckpointConfigurationTypeDef

### ConfigurationType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### CheckpointingEnabled
- **Type**: typing.Optional[bool]

### CheckpointInterval
- **Type**: typing.Optional[int]

### MinPauseBetweenCheckpoints
- **Type**: typing.Optional[int]


# CheckpointConfigurationUpdateTypeDef

### ConfigurationTypeUpdate
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### CheckpointingEnabledUpdate
- **Type**: typing.Optional[bool]

### CheckpointIntervalUpdate
- **Type**: typing.Optional[int]

### MinPauseBetweenCheckpointsUpdate
- **Type**: typing.Optional[int]


# CloudWatchLoggingOptionDescriptionTypeDef

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLoggingOptionId
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# CloudWatchLoggingOptionTypeDef

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLoggingOptionUpdateTypeDef

### CloudWatchLoggingOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### LogStreamARNUpdate
- **Type**: typing.Optional[str]


# CodeContentDescriptionTypeDef

### TextContent
- **Type**: typing.Optional[str]

### CodeMD5
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]

### S3ApplicationCodeLocationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ApplicationCodeLocationDescriptionTypeDef]


# CodeContentTypeDef

### TextContent
- **Type**: typing.Optional[str]

### ZipFileContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.BlobTypeDef]

### S3ContentLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentLocationTypeDef]


# CodeContentUpdateTypeDef

### TextContentUpdate
- **Type**: typing.Optional[str]

### ZipFileContentUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.BlobTypeDef]

### S3ContentLocationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentLocationUpdateTypeDef]


# CreateApplicationPresignedUrlRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### UrlType
- **Type**: typing.Literal['FLINK_DASHBOARD_URL', 'ZEPPELIN_UI_URL']
- **Required**: Yes

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreateApplicationPresignedUrlResponseTypeDef

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.TagTypeDef]]

### ApplicationMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'STREAMING']]


# CreateApplicationResponseTypeDef

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationSnapshotRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# CustomArtifactConfigurationDescriptionTypeDef

### ArtifactType
- **Type**: typing.Optional[typing.Literal['DEPENDENCY_JAR', 'UDF']]

### S3ContentLocationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentLocationTypeDef]

### MavenReferenceDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.MavenReferenceTypeDef]


# CustomArtifactConfigurationTypeDef

### ArtifactType
- **Type**: typing.Literal['DEPENDENCY_JAR', 'UDF']
- **Required**: Yes

### S3ContentLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentLocationTypeDef]

### MavenReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.MavenReferenceTypeDef]


# DeleteApplicationCloudWatchLoggingOptionRequestTypeDef

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


# DeleteApplicationCloudWatchLoggingOptionResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionDescriptionTypeDef]
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationInputProcessingConfigurationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationInputProcessingConfigurationResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationOutputRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationOutputResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationReferenceDataSourceRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationReferenceDataSourceResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.TimestampTypeDef'>
- **Required**: Yes


# DeleteApplicationSnapshotRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotCreationTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.TimestampTypeDef'>
- **Required**: Yes


# DeleteApplicationVpcConfigurationRequestTypeDef

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


# DeleteApplicationVpcConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeployAsApplicationConfigurationDescriptionTypeDef

### S3ContentLocationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentBaseLocationDescriptionTypeDef'>
- **Required**: Yes


# DeployAsApplicationConfigurationTypeDef

### S3ContentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentBaseLocationTypeDef'>
- **Required**: Yes


# DeployAsApplicationConfigurationUpdateTypeDef

### S3ContentLocationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ContentBaseLocationUpdateTypeDef]


# DescribeApplicationOperationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationOperationResponseTypeDef

### ApplicationOperationInfoDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationOperationInfoDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeAdditionalDetails
- **Type**: typing.Optional[bool]


# DescribeApplicationResponseTypeDef

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationSnapshotRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationSnapshotResponseTypeDef

### SnapshotDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SnapshotDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationVersionRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeApplicationVersionResponseTypeDef

### ApplicationVersionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationSchemaTypeDef

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# DiscoverInputSchemaRequestTypeDef

### ServiceExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceARN
- **Type**: typing.Optional[str]

### InputStartingPositionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputStartingPositionConfigurationTypeDef]

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ConfigurationTypeDef]

### InputProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfigurationTypeDef]


# DiscoverInputSchemaResponseTypeDef

### InputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentPropertiesTypeDef

### PropertyGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PropertyGroupUnionTypeDef]
- **Required**: Yes


# EnvironmentPropertyDescriptionsTypeDef

### PropertyGroupDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PropertyGroupOutputTypeDef]]


# EnvironmentPropertyUpdatesTypeDef

### PropertyGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PropertyGroupUnionTypeDef]
- **Required**: Yes


# ErrorInfoTypeDef

### ErrorString
- **Type**: typing.Optional[str]


# FlinkApplicationConfigurationDescriptionTypeDef

### CheckpointConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CheckpointConfigurationDescriptionTypeDef]

### MonitoringConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.MonitoringConfigurationDescriptionTypeDef]

### ParallelismConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ParallelismConfigurationDescriptionTypeDef]

### JobPlanDescription
- **Type**: typing.Optional[str]


# FlinkApplicationConfigurationTypeDef

### CheckpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CheckpointConfigurationTypeDef]

### MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.MonitoringConfigurationTypeDef]

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ParallelismConfigurationTypeDef]


# FlinkApplicationConfigurationUpdateTypeDef

### CheckpointConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CheckpointConfigurationUpdateTypeDef]

### MonitoringConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.MonitoringConfigurationUpdateTypeDef]

### ParallelismConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ParallelismConfigurationUpdateTypeDef]


# FlinkRunConfigurationTypeDef

### AllowNonRestoredState
- **Type**: typing.Optional[bool]


# GlueDataCatalogConfigurationDescriptionTypeDef

### DatabaseARN
- **Type**: <class 'str'>
- **Required**: Yes


# GlueDataCatalogConfigurationTypeDef

### DatabaseARN
- **Type**: <class 'str'>
- **Required**: Yes


# GlueDataCatalogConfigurationUpdateTypeDef

### DatabaseARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# InputDescriptionTypeDef

### InputId
- **Type**: typing.Optional[str]

### NamePrefix
- **Type**: typing.Optional[str]

### InAppStreamNames
- **Type**: typing.Optional[typing.List[str]]

### InputProcessingConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfigurationDescriptionTypeDef]

### KinesisStreamsInputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisStreamsInputDescriptionTypeDef]

### KinesisFirehoseInputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisFirehoseInputDescriptionTypeDef]

### InputSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaOutputTypeDef]

### InputParallelism
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputParallelismTypeDef]

### InputStartingPositionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputStartingPositionConfigurationTypeDef]


# InputLambdaProcessorDescriptionTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# InputLambdaProcessorTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# InputLambdaProcessorUpdateTypeDef

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# InputParallelismTypeDef

### Count
- **Type**: typing.Optional[int]


# InputParallelismUpdateTypeDef

### CountUpdate
- **Type**: <class 'int'>
- **Required**: Yes


# InputProcessingConfigurationDescriptionTypeDef

### InputLambdaProcessorDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputLambdaProcessorDescriptionTypeDef]


# InputProcessingConfigurationTypeDef

### InputLambdaProcessor
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputLambdaProcessorTypeDef'>
- **Required**: Yes


# InputProcessingConfigurationUpdateTypeDef

### InputLambdaProcessorUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputLambdaProcessorUpdateTypeDef'>
- **Required**: Yes


# InputSchemaUpdateTypeDef

### RecordFormatUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordFormatTypeDef]

### RecordEncodingUpdate
- **Type**: typing.Optional[str]

### RecordColumnUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordColumnTypeDef]]


# InputStartingPositionConfigurationTypeDef

### InputStartingPosition
- **Type**: typing.Optional[typing.Literal['LAST_STOPPED_POINT', 'NOW', 'TRIM_HORIZON']]


# InputTypeDef

### NamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### InputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaUnionTypeDef'>
- **Required**: Yes

### InputProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfigurationTypeDef]

### KinesisStreamsInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisStreamsInputTypeDef]

### KinesisFirehoseInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisFirehoseInputTypeDef]

### InputParallelism
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputParallelismTypeDef]


# InputUpdateTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### NamePrefixUpdate
- **Type**: typing.Optional[str]

### InputProcessingConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputProcessingConfigurationUpdateTypeDef]

### KinesisStreamsInputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisStreamsInputUpdateTypeDef]

### KinesisFirehoseInputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisFirehoseInputUpdateTypeDef]

### InputSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputSchemaUpdateTypeDef]

### InputParallelismUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputParallelismUpdateTypeDef]


# JSONMappingParametersTypeDef

### RecordRowPath
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInputDescriptionTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInputUpdateTypeDef

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseOutputDescriptionTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseOutputUpdateTypeDef

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsInputDescriptionTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsInputUpdateTypeDef

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsOutputDescriptionTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsOutputUpdateTypeDef

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaOutputDescriptionTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]


# LambdaOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaOutputUpdateTypeDef

### ResourceARNUpdate
- **Type**: <class 'str'>
- **Required**: Yes


# ListApplicationOperationsRequestPaginateTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Optional[str]

### OperationStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfigTypeDef]


# ListApplicationOperationsRequestTypeDef

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


# ListApplicationOperationsResponseTypeDef

### ApplicationOperationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationOperationInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationSnapshotsRequestPaginateTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfigTypeDef]


# ListApplicationSnapshotsRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationSnapshotsResponseTypeDef

### SnapshotSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SnapshotDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequestPaginateTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfigTypeDef]


# ListApplicationVersionsRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsResponseTypeDef

### ApplicationVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### ApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MappingParametersTypeDef

### JSONMappingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.JSONMappingParametersTypeDef]

### CSVMappingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CSVMappingParametersTypeDef]


# MavenReferenceTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes


# MonitoringConfigurationDescriptionTypeDef

### ConfigurationType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### MetricsLevel
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OPERATOR', 'PARALLELISM', 'TASK']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# MonitoringConfigurationTypeDef

### ConfigurationType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### MetricsLevel
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OPERATOR', 'PARALLELISM', 'TASK']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# MonitoringConfigurationUpdateTypeDef

### ConfigurationTypeUpdate
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### MetricsLevelUpdate
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OPERATOR', 'PARALLELISM', 'TASK']]

### LogLevelUpdate
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# OperationFailureDetailsTypeDef

### RollbackOperationId
- **Type**: typing.Optional[str]

### ErrorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ErrorInfoTypeDef]


# OutputDescriptionTypeDef

### OutputId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### KinesisStreamsOutputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisStreamsOutputDescriptionTypeDef]

### KinesisFirehoseOutputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisFirehoseOutputDescriptionTypeDef]

### LambdaOutputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.LambdaOutputDescriptionTypeDef]

### DestinationSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DestinationSchemaTypeDef]


# OutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DestinationSchemaTypeDef'>
- **Required**: Yes

### KinesisStreamsOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisStreamsOutputTypeDef]

### KinesisFirehoseOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisFirehoseOutputTypeDef]

### LambdaOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.LambdaOutputTypeDef]


# OutputUpdateTypeDef

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes

### NameUpdate
- **Type**: typing.Optional[str]

### KinesisStreamsOutputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisStreamsOutputUpdateTypeDef]

### KinesisFirehoseOutputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.KinesisFirehoseOutputUpdateTypeDef]

### LambdaOutputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.LambdaOutputUpdateTypeDef]

### DestinationSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DestinationSchemaTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParallelismConfigurationDescriptionTypeDef

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


# ParallelismConfigurationTypeDef

### ConfigurationType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### Parallelism
- **Type**: typing.Optional[int]

### ParallelismPerKPU
- **Type**: typing.Optional[int]

### AutoScalingEnabled
- **Type**: typing.Optional[bool]


# ParallelismConfigurationUpdateTypeDef

### ConfigurationTypeUpdate
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### ParallelismUpdate
- **Type**: typing.Optional[int]

### ParallelismPerKPUUpdate
- **Type**: typing.Optional[int]

### AutoScalingEnabledUpdate
- **Type**: typing.Optional[bool]


# PropertyGroupOutputTypeDef

### PropertyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PropertyMap
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# PropertyGroupTypeDef

### PropertyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PropertyMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# PropertyGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordColumnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordFormatTypeDef

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### MappingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.MappingParametersTypeDef]


# ReferenceDataSourceDescriptionTypeDef

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### S3ReferenceDataSourceDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ReferenceDataSourceDescriptionTypeDef'>
- **Required**: Yes

### ReferenceSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaOutputTypeDef]


# ReferenceDataSourceTypeDef

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaUnionTypeDef'>
- **Required**: Yes

### S3ReferenceDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ReferenceDataSourceTypeDef]


# ReferenceDataSourceUpdateTypeDef

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableNameUpdate
- **Type**: typing.Optional[str]

### S3ReferenceDataSourceUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.S3ReferenceDataSourceUpdateTypeDef]

### ReferenceSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SourceSchemaUnionTypeDef]


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


# RollbackApplicationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# RollbackApplicationResponseTypeDef

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetailTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RunConfigurationDescriptionTypeDef

### ApplicationRestoreConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationRestoreConfigurationTypeDef]

### FlinkRunConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.FlinkRunConfigurationTypeDef]


# RunConfigurationTypeDef

### FlinkRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.FlinkRunConfigurationTypeDef]

### SqlRunConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.SqlRunConfigurationTypeDef]]

### ApplicationRestoreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationRestoreConfigurationTypeDef]


# RunConfigurationUpdateTypeDef

### FlinkRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.FlinkRunConfigurationTypeDef]

### ApplicationRestoreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationRestoreConfigurationTypeDef]


# S3ApplicationCodeLocationDescriptionTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectVersion
- **Type**: typing.Optional[str]


# S3ConfigurationTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes


# S3ContentBaseLocationDescriptionTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BasePath
- **Type**: typing.Optional[str]


# S3ContentBaseLocationTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BasePath
- **Type**: typing.Optional[str]


# S3ContentBaseLocationUpdateTypeDef

### BucketARNUpdate
- **Type**: typing.Optional[str]

### BasePathUpdate
- **Type**: typing.Optional[str]


# S3ContentLocationTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectVersion
- **Type**: typing.Optional[str]


# S3ContentLocationUpdateTypeDef

### BucketARNUpdate
- **Type**: typing.Optional[str]

### FileKeyUpdate
- **Type**: typing.Optional[str]

### ObjectVersionUpdate
- **Type**: typing.Optional[str]


# S3ReferenceDataSourceDescriptionTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceRoleARN
- **Type**: typing.Optional[str]


# S3ReferenceDataSourceTypeDef

### BucketARN
- **Type**: typing.Optional[str]

### FileKey
- **Type**: typing.Optional[str]


# S3ReferenceDataSourceUpdateTypeDef

### BucketARNUpdate
- **Type**: typing.Optional[str]

### FileKeyUpdate
- **Type**: typing.Optional[str]


# SnapshotDetailsTypeDef

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


# SourceSchemaOutputTypeDef

### RecordFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordFormatTypeDef'>
- **Required**: Yes

### RecordColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordColumnTypeDef]
- **Required**: Yes

### RecordEncoding
- **Type**: typing.Optional[str]


# SourceSchemaTypeDef

### RecordFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordFormatTypeDef'>
- **Required**: Yes

### RecordColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RecordColumnTypeDef]
- **Required**: Yes

### RecordEncoding
- **Type**: typing.Optional[str]


# SourceSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SqlApplicationConfigurationDescriptionTypeDef

### InputDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputDescriptionTypeDef]]

### OutputDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputDescriptionTypeDef]]

### ReferenceDataSourceDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceDescriptionTypeDef]]


# SqlApplicationConfigurationTypeDef

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputTypeDef]]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputTypeDef]]

### ReferenceDataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceTypeDef]]


# SqlApplicationConfigurationUpdateTypeDef

### InputUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputUpdateTypeDef]]

### OutputUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.OutputUpdateTypeDef]]

### ReferenceDataSourceUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ReferenceDataSourceUpdateTypeDef]]


# SqlRunConfigurationTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### InputStartingPositionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.InputStartingPositionConfigurationTypeDef'>
- **Required**: Yes


# StartApplicationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### RunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RunConfigurationTypeDef]


# StartApplicationResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopApplicationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# StopApplicationResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationMaintenanceConfigurationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationMaintenanceConfigurationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationMaintenanceConfigurationUpdateTypeDef'>
- **Required**: Yes


# UpdateApplicationMaintenanceConfigurationResponseTypeDef

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationMaintenanceConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationMaintenanceConfigurationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApplicationRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: typing.Optional[int]

### ApplicationConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationConfigurationUpdateTypeDef]

### ServiceExecutionRoleUpdate
- **Type**: typing.Optional[str]

### RunConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.RunConfigurationUpdateTypeDef]

### CloudWatchLoggingOptionUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CloudWatchLoggingOptionUpdateTypeDef]]

### ConditionalToken
- **Type**: typing.Optional[str]

### RuntimeEnvironmentUpdate
- **Type**: typing.Optional[typing.Literal['FLINK-1_11', 'FLINK-1_13', 'FLINK-1_15', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-1_6', 'FLINK-1_8', 'SQL-1_0', 'ZEPPELIN-FLINK-1_0', 'ZEPPELIN-FLINK-2_0', 'ZEPPELIN-FLINK-3_0']]


# UpdateApplicationResponseTypeDef

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ApplicationDetailTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConfigurationDescriptionTypeDef

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


# VpcConfigurationTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VpcConfigurationUpdateTypeDef

### VpcConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIdUpdates
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIdUpdates
- **Type**: typing.Optional[typing.Sequence[str]]


# ZeppelinApplicationConfigurationDescriptionTypeDef

### MonitoringConfigurationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinMonitoringConfigurationDescriptionTypeDef'>
- **Required**: Yes

### CatalogConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CatalogConfigurationDescriptionTypeDef]

### DeployAsApplicationConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DeployAsApplicationConfigurationDescriptionTypeDef]

### CustomArtifactsConfigurationDescription
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CustomArtifactConfigurationDescriptionTypeDef]]


# ZeppelinApplicationConfigurationTypeDef

### MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinMonitoringConfigurationTypeDef]

### CatalogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CatalogConfigurationTypeDef]

### DeployAsApplicationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DeployAsApplicationConfigurationTypeDef]

### CustomArtifactsConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CustomArtifactConfigurationTypeDef]]


# ZeppelinApplicationConfigurationUpdateTypeDef

### MonitoringConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.ZeppelinMonitoringConfigurationUpdateTypeDef]

### CatalogConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CatalogConfigurationUpdateTypeDef]

### DeployAsApplicationConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.DeployAsApplicationConfigurationUpdateTypeDef]

### CustomArtifactsConfigurationUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalyticsv2_classes.CustomArtifactConfigurationTypeDef]]


# ZeppelinMonitoringConfigurationDescriptionTypeDef

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# ZeppelinMonitoringConfigurationTypeDef

### LogLevel
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# ZeppelinMonitoringConfigurationUpdateTypeDef

### LogLevelUpdate
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


