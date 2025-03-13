# M2 Classes

# AlternateKeyTypeDef

### length
- **Type**: <class 'int'>
- **Required**: Yes

### offset
- **Type**: <class 'int'>
- **Required**: Yes

### allowDuplicates
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]


# ApplicationSummaryTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### engineType
- **Type**: typing.Literal['bluage', 'microfocus']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Available', 'Created', 'Creating', 'Deleting', 'Deleting From Environment', 'Failed', 'Ready', 'Running', 'Starting', 'Stopped', 'Stopping']
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Optional[typing.Literal['Deployed', 'Deploying']]

### description
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### lastStartTime
- **Type**: typing.Optional[datetime.datetime]

### roleArn
- **Type**: typing.Optional[str]

### versionStatus
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Failed']]


# ApplicationVersionSummaryTypeDef

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Available', 'Creating', 'Failed']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchJobDefinitionTypeDef

### fileBatchJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.FileBatchJobDefinitionTypeDef]

### scriptBatchJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.ScriptBatchJobDefinitionTypeDef]


# BatchJobExecutionSummaryTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']
- **Required**: Yes

### batchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.BatchJobIdentifierTypeDef]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### jobId
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### jobType
- **Type**: typing.Optional[typing.Literal['JES2', 'JES3', 'VSE']]

### returnCode
- **Type**: typing.Optional[str]


# BatchJobIdentifierTypeDef

### fileBatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.FileBatchJobIdentifierTypeDef]

### restartBatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.RestartBatchJobIdentifierTypeDef]

### s3BatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.S3BatchJobIdentifierTypeDef]

### scriptBatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.ScriptBatchJobIdentifierTypeDef]


# CancelBatchJobExecutionRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### authSecretsManagerArn
- **Type**: typing.Optional[str]


# CreateApplicationRequestTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DefinitionTypeDef'>
- **Required**: Yes

### engineType
- **Type**: typing.Literal['bluage', 'microfocus']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateApplicationResponseTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSetImportTaskRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### importConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSetImportConfigTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateDataSetImportTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateDeploymentResponseTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentRequestTypeDef

### engineType
- **Type**: typing.Literal['bluage', 'microfocus']
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### engineVersion
- **Type**: typing.Optional[str]

### highAvailabilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.HighAvailabilityConfigTypeDef]

### kmsKeyId
- **Type**: typing.Optional[str]

### networkType
- **Type**: typing.Optional[typing.Literal['dual', 'ipv4']]

### preferredMaintenanceWindow
- **Type**: typing.Optional[str]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### storageConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.m2_classes.StorageConfigurationTypeDef]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEnvironmentResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSetImportConfigTypeDef

### dataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.m2_classes.DataSetImportItemTypeDef]]

### s3Location
- **Type**: typing.Optional[str]


# DataSetImportItemTypeDef

### dataSet
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSetTypeDef'>
- **Required**: Yes

### externalLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ExternalLocationTypeDef'>
- **Required**: Yes


# DataSetImportSummaryTypeDef

### failed
- **Type**: <class 'int'>
- **Required**: Yes

### inProgress
- **Type**: <class 'int'>
- **Required**: Yes

### pending
- **Type**: <class 'int'>
- **Required**: Yes

### succeeded
- **Type**: <class 'int'>
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes


# DataSetImportTaskTypeDef

### status
- **Type**: typing.Literal['Completed', 'Creating', 'Failed', 'Running']
- **Required**: Yes

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSetImportSummaryTypeDef'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# DataSetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSetTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetOrg
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DatasetOrgAttributesTypeDef'>
- **Required**: Yes

### recordLength
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.RecordLengthTypeDef'>
- **Required**: Yes

### relativePath
- **Type**: typing.Optional[str]

### storageType
- **Type**: typing.Optional[str]


# DatasetDetailOrgAttributesTypeDef

### gdg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.GdgDetailAttributesTypeDef]

### po
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PoDetailAttributesTypeDef]

### ps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PsDetailAttributesTypeDef]

### vsam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.VsamDetailAttributesTypeDef]


# DatasetOrgAttributesTypeDef

### gdg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.GdgAttributesTypeDef]

### po
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PoAttributesTypeDef]

### ps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PsAttributesTypeDef]

### vsam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.VsamAttributesTypeDef]


# DefinitionTypeDef

### content
- **Type**: typing.Optional[str]

### s3Location
- **Type**: typing.Optional[str]


# DeleteApplicationFromEnvironmentRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeployedVersionSummaryTypeDef

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Deploying', 'Failed', 'Succeeded', 'Updating Deployment']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# DeploymentSummaryTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Deploying', 'Failed', 'Succeeded', 'Updating Deployment']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# EfsStorageConfigurationTypeDef

### fileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### mountPoint
- **Type**: <class 'str'>
- **Required**: Yes


# EngineVersionsSummaryTypeDef

### engineType
- **Type**: <class 'str'>
- **Required**: Yes

### engineVersion
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentSummaryTypeDef

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### engineType
- **Type**: typing.Literal['bluage', 'microfocus']
- **Required**: Yes

### engineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### environmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'UnHealthy', 'Updating']
- **Required**: Yes

### networkType
- **Type**: typing.Optional[typing.Literal['dual', 'ipv4']]


# ExternalLocationTypeDef

### s3Location
- **Type**: typing.Optional[str]


# FileBatchJobDefinitionTypeDef

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### folderPath
- **Type**: typing.Optional[str]


# FileBatchJobIdentifierTypeDef

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### folderPath
- **Type**: typing.Optional[str]


# FsxStorageConfigurationTypeDef

### fileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### mountPoint
- **Type**: <class 'str'>
- **Required**: Yes


# GdgAttributesTypeDef

### limit
- **Type**: typing.Optional[int]

### rollDisposition
- **Type**: typing.Optional[str]


# GdgDetailAttributesTypeDef

### limit
- **Type**: typing.Optional[int]

### rollDisposition
- **Type**: typing.Optional[str]


# GetApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponseTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deployedVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DeployedVersionSummaryTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### engineType
- **Type**: typing.Literal['bluage', 'microfocus']
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### lastStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ApplicationVersionSummaryTypeDef'>
- **Required**: Yes

### listenerArns
- **Type**: typing.List[str]
- **Required**: Yes

### listenerPorts
- **Type**: typing.List[int]
- **Required**: Yes

### loadBalancerDnsName
- **Type**: <class 'str'>
- **Required**: Yes

### logGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.LogGroupSummaryTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Available', 'Created', 'Creating', 'Deleting', 'Deleting From Environment', 'Failed', 'Ready', 'Running', 'Starting', 'Stopped', 'Stopping']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### targetGroupArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationVersionRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes


# GetApplicationVersionResponseTypeDef

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### definitionContent
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Available', 'Creating', 'Failed']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBatchJobExecutionRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBatchJobExecutionResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.BatchJobIdentifierTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobStepRestartMarker
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.JobStepRestartMarkerTypeDef'>
- **Required**: Yes

### jobType
- **Type**: typing.Literal['JES2', 'JES3', 'VSE']
- **Required**: Yes

### jobUser
- **Type**: <class 'str'>
- **Required**: Yes

### returnCode
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSetDetailsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSetDetailsResponseTypeDef

### blocksize
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSetName
- **Type**: <class 'str'>
- **Required**: Yes

### dataSetOrg
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DatasetDetailOrgAttributesTypeDef'>
- **Required**: Yes

### fileSize
- **Type**: <class 'int'>
- **Required**: Yes

### lastReferencedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### recordLength
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSetImportTaskRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSetImportTaskResponseTypeDef

### status
- **Type**: typing.Literal['Completed', 'Creating', 'Failed', 'Running']
- **Required**: Yes

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSetImportSummaryTypeDef'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Deploying', 'Failed', 'Succeeded', 'Updating Deployment']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponseTypeDef

### actualCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### engineType
- **Type**: typing.Literal['bluage', 'microfocus']
- **Required**: Yes

### engineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### environmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### highAvailabilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.HighAvailabilityConfigTypeDef'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### loadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### networkType
- **Type**: typing.Literal['dual', 'ipv4']
- **Required**: Yes

### pendingMaintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.PendingMaintenanceTypeDef'>
- **Required**: Yes

### preferredMaintenanceWindow
- **Type**: <class 'str'>
- **Required**: Yes

### publiclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'UnHealthy', 'Updating']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### storageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.StorageConfigurationTypeDef]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSignedBluinsightsUrlResponseTypeDef

### signedBiUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HighAvailabilityConfigTypeDef

### desiredCapacity
- **Type**: <class 'int'>
- **Required**: Yes


# JobIdentifierTypeDef

### fileName
- **Type**: typing.Optional[str]

### scriptName
- **Type**: typing.Optional[str]


# JobStepRestartMarkerTypeDef

### fromStep
- **Type**: <class 'str'>
- **Required**: Yes

### fromProcStep
- **Type**: typing.Optional[str]

### toProcStep
- **Type**: typing.Optional[str]

### toStep
- **Type**: typing.Optional[str]


# JobStepTypeDef

### procStepName
- **Type**: typing.Optional[str]

### procStepNumber
- **Type**: typing.Optional[int]

### stepCondCode
- **Type**: typing.Optional[str]

### stepName
- **Type**: typing.Optional[str]

### stepNumber
- **Type**: typing.Optional[int]

### stepRestartable
- **Type**: typing.Optional[bool]


# ListApplicationVersionsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListApplicationVersionsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsResponseTypeDef

### applicationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.ApplicationVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginateTypeDef

### environmentId
- **Type**: typing.Optional[str]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### environmentId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBatchJobDefinitionsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListBatchJobDefinitionsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ListBatchJobDefinitionsResponseTypeDef

### batchJobDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.BatchJobDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBatchJobExecutionsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### jobName
- **Type**: typing.Optional[str]

### startedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.TimestampTypeDef]

### startedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.TimestampTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListBatchJobExecutionsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### jobName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### startedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.TimestampTypeDef]

### startedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.TimestampTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']]


# ListBatchJobExecutionsResponseTypeDef

### batchJobExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.BatchJobExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBatchJobRestartPointsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### authSecretsManagerArn
- **Type**: typing.Optional[str]


# ListBatchJobRestartPointsResponseTypeDef

### batchJobSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.JobStepTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSetImportHistoryRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListDataSetImportHistoryRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataSetImportHistoryResponseTypeDef

### dataSetImportTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.DataSetImportTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSetsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nameFilter
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListDataSetsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nameFilter
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ListDataSetsResponseTypeDef

### dataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.DataSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListDeploymentsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsResponseTypeDef

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.DeploymentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEngineVersionsRequestPaginateTypeDef

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListEngineVersionsRequestTypeDef

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEngineVersionsResponseTypeDef

### engineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.EngineVersionsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequestPaginateTypeDef

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestTypeDef

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### maxResults
- **Type**: typing.Optional[int]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsResponseTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.EnvironmentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogGroupSummaryTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logType
- **Type**: <class 'str'>
- **Required**: Yes


# MaintenanceScheduleTypeDef

### endTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingMaintenanceTypeDef

### engineVersion
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.MaintenanceScheduleTypeDef]


# PoAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PoDetailAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrimaryKeyTypeDef

### length
- **Type**: <class 'int'>
- **Required**: Yes

### offset
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# PsAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PsDetailAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordLengthTypeDef

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


# RestartBatchJobIdentifierTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStepRestartMarker
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.JobStepRestartMarkerTypeDef'>
- **Required**: Yes


# S3BatchJobIdentifierTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.JobIdentifierTypeDef'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# ScriptBatchJobDefinitionTypeDef

### scriptName
- **Type**: <class 'str'>
- **Required**: Yes


# ScriptBatchJobIdentifierTypeDef

### scriptName
- **Type**: <class 'str'>
- **Required**: Yes


# StartApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartBatchJobRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.BatchJobIdentifierTypeDef'>
- **Required**: Yes

### authSecretsManagerArn
- **Type**: typing.Optional[str]

### jobParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartBatchJobResponseTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### forceStop
- **Type**: typing.Optional[bool]


# StorageConfigurationTypeDef

### efs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.EfsStorageConfigurationTypeDef]

### fsx
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.FsxStorageConfigurationTypeDef]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### currentApplicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.DefinitionTypeDef]

### description
- **Type**: typing.Optional[str]


# UpdateApplicationResponseTypeDef

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### applyDuringMaintenanceWindow
- **Type**: typing.Optional[bool]

### desiredCapacity
- **Type**: typing.Optional[int]

### engineVersion
- **Type**: typing.Optional[str]

### forceUpdate
- **Type**: typing.Optional[bool]

### instanceType
- **Type**: typing.Optional[str]

### preferredMaintenanceWindow
- **Type**: typing.Optional[str]


# UpdateEnvironmentResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VsamAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VsamDetailAttributesTypeDef

### alternateKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.m2_classes.AlternateKeyTypeDef]]

### cacheAtStartup
- **Type**: typing.Optional[bool]

### compressed
- **Type**: typing.Optional[bool]

### encoding
- **Type**: typing.Optional[str]

### primaryKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PrimaryKeyTypeDef]

### recordFormat
- **Type**: typing.Optional[str]


