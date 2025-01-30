# m2_classes

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


# CancelBatchJobExecutionRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateApplicationRequestRequestTypeDef

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


# CreateDataSetImportTaskRequestRequestTypeDef

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


# CreateDeploymentRequestRequestTypeDef

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


# CreateEnvironmentRequestRequestTypeDef

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

### dataSetName
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### dataSetOrg
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[str]

### lastReferencedTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


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


# DeleteApplicationFromEnvironmentRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequestRequestTypeDef

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
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Updating']
- **Required**: Yes


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


# GetApplicationRequestRequestTypeDef

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


# GetApplicationVersionRequestRequestTypeDef

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


# GetBatchJobExecutionRequestRequestTypeDef

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


# GetDataSetDetailsRequestRequestTypeDef

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


# GetDataSetImportTaskRequestRequestTypeDef

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


# GetDeploymentRequestRequestTypeDef

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


# GetEnvironmentRequestRequestTypeDef

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
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Updating']
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


# ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListApplicationVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationsRequestListApplicationsPaginateTypeDef

### environmentId
- **Type**: typing.Optional[str]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBatchJobDefinitionsRequestListBatchJobDefinitionsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListBatchJobDefinitionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBatchJobExecutionsRequestListBatchJobExecutionsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### jobName
- **Type**: typing.Optional[str]

### startedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### startedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListBatchJobExecutionsRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### startedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']]


# ListBatchJobExecutionsResponseTypeDef

### batchJobExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.BatchJobExecutionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBatchJobRestartPointsRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes


# ListBatchJobRestartPointsResponseTypeDef

### batchJobSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.JobStepTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSetImportHistoryRequestListDataSetImportHistoryPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListDataSetImportHistoryRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSetsRequestListDataSetsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nameFilter
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListDataSetsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeploymentsRequestListDeploymentsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListDeploymentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEngineVersionsRequestListEngineVersionsPaginateTypeDef

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListEngineVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentsRequestListEnvironmentsPaginateTypeDef

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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

### format
- **Type**: <class 'str'>
- **Required**: Yes

### memberFileExtensions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### encoding
- **Type**: typing.Optional[str]


# PoDetailAttributesTypeDef

### encoding
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: <class 'str'>
- **Required**: Yes


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

### format
- **Type**: <class 'str'>
- **Required**: Yes

### encoding
- **Type**: typing.Optional[str]


# PsDetailAttributesTypeDef

### encoding
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: <class 'str'>
- **Required**: Yes


# RecordLengthTypeDef

### max
- **Type**: <class 'int'>
- **Required**: Yes

### min
- **Type**: <class 'int'>
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


# StartApplicationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartBatchJobRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.BatchJobIdentifierTypeDef'>
- **Required**: Yes

### jobParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartBatchJobResponseTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopApplicationRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

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


# UpdateEnvironmentRequestRequestTypeDef

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

### format
- **Type**: <class 'str'>
- **Required**: Yes

### alternateKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.m2_classes.AlternateKeyTypeDef]]

### compressed
- **Type**: typing.Optional[bool]

### encoding
- **Type**: typing.Optional[str]

### primaryKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PrimaryKeyTypeDef]


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


