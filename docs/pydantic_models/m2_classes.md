# M2 Classes

# AlternateKey

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


# ApplicationSummary

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


# ApplicationVersionSummary

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

# BatchJobDefinition

### fileBatchJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.FileBatchJobDefinition]

### scriptBatchJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.ScriptBatchJobDefinition]


# BatchJobExecutionSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.BatchJobIdentifier]

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


# BatchJobIdentifier

### fileBatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.FileBatchJobIdentifier]

### restartBatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.RestartBatchJobIdentifier]

### s3BatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.S3BatchJobIdentifier]

### scriptBatchJobIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.ScriptBatchJobIdentifier]


# CancelBatchJobExecutionRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### authSecretsManagerArn
- **Type**: typing.Optional[str]


# CreateApplicationRequest

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.Definition'>
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


# CreateApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSetImportTaskRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### importConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSetImportConfig'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateDataSetImportTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentRequest

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


# CreateDeploymentResponse

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.HighAvailabilityConfig]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.m2_classes.StorageConfiguration]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEnvironmentResponse

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# DataSet

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetOrg
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DatasetOrgAttributes'>
- **Required**: Yes

### recordLength
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.RecordLength'>
- **Required**: Yes

### relativePath
- **Type**: typing.Optional[str]

### storageType
- **Type**: typing.Optional[str]


# DataSetImportConfig

### dataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.m2_classes.DataSetImportItem]]

### s3Location
- **Type**: typing.Optional[str]


# DataSetImportItem

### dataSet
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSet'>
- **Required**: Yes

### externalLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ExternalLocation'>
- **Required**: Yes


# DataSetImportSummary

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


# DataSetImportTask

### status
- **Type**: typing.Literal['Completed', 'Creating', 'Failed', 'Running']
- **Required**: Yes

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSetImportSummary'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# DataSetSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatasetDetailOrgAttributes

### gdg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.GdgDetailAttributes]

### po
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PoDetailAttributes]

### ps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PsDetailAttributes]

### vsam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.VsamDetailAttributes]


# DatasetOrgAttributes

### gdg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.GdgAttributes]

### po
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PoAttributes]

### ps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PsAttributes]

### vsam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.VsamAttributes]


# Definition

### content
- **Type**: typing.Optional[str]

### s3Location
- **Type**: typing.Optional[str]


# DeleteApplicationFromEnvironmentRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeployedVersionSummary

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Deploying', 'Failed', 'Succeeded', 'Updating Deployment']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# DeploymentSummary

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


# EfsStorageConfiguration

### fileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### mountPoint
- **Type**: <class 'str'>
- **Required**: Yes


# EngineVersionsSummary

### engineType
- **Type**: <class 'str'>
- **Required**: Yes

### engineVersion
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentSummary

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


# ExternalLocation

### s3Location
- **Type**: typing.Optional[str]


# FileBatchJobDefinition

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### folderPath
- **Type**: typing.Optional[str]


# FileBatchJobIdentifier

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### folderPath
- **Type**: typing.Optional[str]


# FsxStorageConfiguration

### fileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### mountPoint
- **Type**: <class 'str'>
- **Required**: Yes


# GdgAttributes

### limit
- **Type**: typing.Optional[int]

### rollDisposition
- **Type**: typing.Optional[str]


# GdgDetailAttributes

### limit
- **Type**: typing.Optional[int]

### rollDisposition
- **Type**: typing.Optional[str]


# GetApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DeployedVersionSummary'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ApplicationVersionSummary'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.LogGroupSummary]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationVersionRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes


# GetApplicationVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# GetBatchJobExecutionRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBatchJobExecutionResponse

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.BatchJobIdentifier'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.JobStepRestartMarker'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSetDetailsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSetDetailsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DatasetDetailOrgAttributes'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSetImportTaskRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSetImportTaskResponse

### status
- **Type**: typing.Literal['Completed', 'Creating', 'Failed', 'Running']
- **Required**: Yes

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.DataSetImportSummary'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.HighAvailabilityConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.PendingMaintenance'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.StorageConfiguration]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# GetSignedBluinsightsUrlResponse

### signedBiUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# HighAvailabilityConfig

### desiredCapacity
- **Type**: <class 'int'>
- **Required**: Yes


# JobIdentifier

### fileName
- **Type**: typing.Optional[str]

### scriptName
- **Type**: typing.Optional[str]


# JobStep

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


# JobStepRestartMarker

### fromStep
- **Type**: <class 'str'>
- **Required**: Yes

### fromProcStep
- **Type**: typing.Optional[str]

### toProcStep
- **Type**: typing.Optional[str]

### toStep
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListApplicationVersionsResponse

### applicationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.ApplicationVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### environmentId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginate

### environmentId
- **Type**: typing.Optional[str]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListApplicationsResponse

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBatchJobDefinitionsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ListBatchJobDefinitionsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListBatchJobDefinitionsResponse

### batchJobDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.BatchJobDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBatchJobExecutionsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.Timestamp]

### startedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.Timestamp]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']]


# ListBatchJobExecutionsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### jobName
- **Type**: typing.Optional[str]

### startedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.Timestamp]

### startedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.Timestamp]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Dispatching', 'Failed', 'Holding', 'Purged', 'Running', 'Submitting', 'Succeeded', 'Succeeded With Warning']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListBatchJobExecutionsResponse

### batchJobExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.BatchJobExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBatchJobRestartPointsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### authSecretsManagerArn
- **Type**: typing.Optional[str]


# ListBatchJobRestartPointsResponse

### batchJobSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.JobStep]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# ListDataSetImportHistoryRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataSetImportHistoryRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListDataSetImportHistoryResponse

### dataSetImportTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.DataSetImportTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSetsRequest

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


# ListDataSetsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nameFilter
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListDataSetsResponse

### dataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.DataSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListDeploymentsResponse

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.DeploymentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEngineVersionsRequest

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEngineVersionsRequestPaginate

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListEngineVersionsResponse

### engineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.EngineVersionsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequest

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### maxResults
- **Type**: typing.Optional[int]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequestPaginate

### engineType
- **Type**: typing.Optional[typing.Literal['bluage', 'microfocus']]

### names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PaginatorConfig]


# ListEnvironmentsResponse

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.m2_classes.EnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# LogGroupSummary

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logType
- **Type**: <class 'str'>
- **Required**: Yes


# MaintenanceSchedule

### endTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingMaintenance

### engineVersion
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.MaintenanceSchedule]


# PoAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PoDetailAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrimaryKey

### length
- **Type**: <class 'int'>
- **Required**: Yes

### offset
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# PsAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PsDetailAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordLength

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


# RestartBatchJobIdentifier

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStepRestartMarker
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.JobStepRestartMarker'>
- **Required**: Yes


# S3BatchJobIdentifier

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.JobIdentifier'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# ScriptBatchJobDefinition

### scriptName
- **Type**: <class 'str'>
- **Required**: Yes


# ScriptBatchJobIdentifier

### scriptName
- **Type**: <class 'str'>
- **Required**: Yes


# StartApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartBatchJobRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.BatchJobIdentifier'>
- **Required**: Yes

### authSecretsManagerArn
- **Type**: typing.Optional[str]

### jobParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartBatchJobResponse

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# StopApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### forceStop
- **Type**: typing.Optional[bool]


# StorageConfiguration

### efs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.EfsStorageConfiguration]

### fsx
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.FsxStorageConfiguration]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### currentApplicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.Definition]

### description
- **Type**: typing.Optional[str]


# UpdateApplicationResponse

### applicationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentRequest

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


# UpdateEnvironmentResponse

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.m2_classes.ResponseMetadata'>
- **Required**: Yes


# VsamAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VsamDetailAttributes

### alternateKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.m2_classes.AlternateKey]]

### cacheAtStartup
- **Type**: typing.Optional[bool]

### compressed
- **Type**: typing.Optional[bool]

### encoding
- **Type**: typing.Optional[str]

### primaryKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.m2_classes.PrimaryKey]

### recordFormat
- **Type**: typing.Optional[str]


