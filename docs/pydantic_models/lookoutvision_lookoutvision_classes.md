# Lookoutvision Lookoutvision Classes

# Anomaly

### Name
- **Type**: typing.Optional[str]

### PixelAnomaly
- **Type**: <class 'NoneType'>


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDatasetRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetSource
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]


# CreateDatasetResponse

### DatasetMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.DatasetMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.OutputConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.Tag]]


# CreateModelResponse

### ModelMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateProjectResponse

### ProjectMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ProjectMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DatasetDescription

### ProjectName
- **Type**: typing.Optional[str]

### DatasetType
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED_ROLLBACK_COMPLETE', 'UPDATE_FAILED_ROLLBACK_IN_PROGRESS', 'UPDATE_IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### ImageStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.DatasetImageStats]


# DatasetGroundTruthManifest

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.InputS3Object]


# DatasetImageStats

### Total
- **Type**: typing.Optional[int]

### Labeled
- **Type**: typing.Optional[int]

### Normal
- **Type**: typing.Optional[int]

### Anomaly
- **Type**: typing.Optional[int]


# DatasetMetadata

### DatasetType
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED_ROLLBACK_COMPLETE', 'UPDATE_FAILED_ROLLBACK_IN_PROGRESS', 'UPDATE_IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]


# DatasetSource

### GroundTruthManifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.DatasetGroundTruthManifest]


# DeleteDatasetRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteModelRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteModelResponse

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteProjectResponse

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### DatasetDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.DatasetDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelPackagingJobRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelPackagingJobResponse

### ModelPackagingDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelPackagingDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelResponse

### ModelDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProjectRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResponse

### ProjectDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ProjectDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DetectAnomaliesRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# DetectAnomaliesResponse

### DetectAnomalyResult
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.DetectAnomalyResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# DetectAnomalyResult

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ImageSource]

### IsAnomalous
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]

### Anomalies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.Anomaly]]

### AnomalyMask
- **Type**: typing.Optional[bytes]


# GreengrassConfiguration

### S3OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.S3Location'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilerOptions
- **Type**: typing.Optional[str]

### TargetDevice
- **Type**: typing.Optional[typing.Literal['jetson_xavier']]

### TargetPlatform
- **Type**: <class 'NoneType'>

### ComponentVersion
- **Type**: typing.Optional[str]

### ComponentDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.Tag]]


# GreengrassConfigurationOutput

### S3OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.S3Location'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilerOptions
- **Type**: typing.Optional[str]

### TargetDevice
- **Type**: typing.Optional[typing.Literal['jetson_xavier']]

### TargetPlatform
- **Type**: <class 'NoneType'>

### ComponentVersion
- **Type**: typing.Optional[str]

### ComponentDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.Tag]]


# GreengrassOutputDetails

### ComponentVersionArn
- **Type**: typing.Optional[str]

### ComponentName
- **Type**: typing.Optional[str]

### ComponentVersion
- **Type**: typing.Optional[str]


# ImageSource

### Type
- **Type**: typing.Optional[str]


# InputS3Object

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# ListDatasetEntriesRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### Labeled
- **Type**: typing.Optional[bool]

### AnomalyClass
- **Type**: typing.Optional[str]

### BeforeCreationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### AfterCreationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SourceRefContains
- **Type**: typing.Optional[str]


# ListDatasetEntriesRequestPaginate

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### Labeled
- **Type**: typing.Optional[bool]

### AnomalyClass
- **Type**: typing.Optional[str]

### BeforeCreationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### AfterCreationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SourceRefContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.PaginatorConfig]


# ListDatasetEntriesResponse

### DatasetEntries
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelPackagingJobsRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelPackagingJobsRequestPaginate

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.PaginatorConfig]


# ListModelPackagingJobsResponse

### ModelPackagingJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelPackagingJobMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelsRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelsRequestPaginate

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.PaginatorConfig]


# ListModelsResponse

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProjectsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProjectsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.PaginatorConfig]


# ListProjectsResponse

### Projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ProjectMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# ModelDescription

### ModelVersion
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'HOSTED', 'HOSTING_FAILED', 'STARTING_HOSTING', 'STOPPING_HOSTING', 'SYSTEM_UPDATING', 'TRAINED', 'TRAINING', 'TRAINING_FAILED']]

### StatusMessage
- **Type**: typing.Optional[str]

### Performance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelPerformance]

### OutputConfig
- **Type**: <class 'NoneType'>

### EvaluationManifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.OutputS3Object]

### EvaluationResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.OutputS3Object]

### EvaluationEndTimestamp
- **Type**: typing.Optional[datetime.datetime]

### KmsKeyId
- **Type**: typing.Optional[str]

### MinInferenceUnits
- **Type**: typing.Optional[int]

### MaxInferenceUnits
- **Type**: typing.Optional[int]


# ModelMetadata

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ModelVersion
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'HOSTED', 'HOSTING_FAILED', 'STARTING_HOSTING', 'STOPPING_HOSTING', 'SYSTEM_UPDATING', 'TRAINED', 'TRAINING', 'TRAINING_FAILED']]

### StatusMessage
- **Type**: typing.Optional[str]

### Performance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelPerformance]


# ModelPackagingConfiguration

### Greengrass
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.GreengrassConfiguration'>
- **Required**: Yes


# ModelPackagingConfigurationOutput

### Greengrass
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.GreengrassConfigurationOutput'>
- **Required**: Yes


# ModelPackagingDescription

### JobName
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### ModelPackagingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelPackagingConfigurationOutput]

### ModelPackagingJobDescription
- **Type**: typing.Optional[str]

### ModelPackagingMethod
- **Type**: typing.Optional[str]

### ModelPackagingOutputDetails
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'RUNNING', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ModelPackagingJobMetadata

### JobName
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### ModelPackagingJobDescription
- **Type**: typing.Optional[str]

### ModelPackagingMethod
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'RUNNING', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ModelPackagingOutputDetails

### Greengrass
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.GreengrassOutputDetails]


# ModelPerformance

### F1Score
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### Precision
- **Type**: typing.Optional[float]


# OutputConfig

### S3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.S3Location'>
- **Required**: Yes


# OutputS3Object

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PixelAnomaly

### TotalPercentageArea
- **Type**: typing.Optional[float]

### Color
- **Type**: typing.Optional[str]


# ProjectDescription

### ProjectArn
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Datasets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.DatasetMetadata]]


# ProjectMetadata

### ProjectArn
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]


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


# S3Location

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# StartModelPackagingJobRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelPackagingConfiguration, aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ModelPackagingConfigurationOutput]
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# StartModelPackagingJobResponse

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# StartModelRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### MinInferenceUnits
- **Type**: <class 'int'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### MaxInferenceUnits
- **Type**: typing.Optional[int]


# StartModelResponse

### Status
- **Type**: typing.Literal['HOSTED', 'HOSTING_FAILED', 'STARTING_HOSTING', 'STOPPING_HOSTING', 'SYSTEM_UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# StopModelRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StopModelResponse

### Status
- **Type**: typing.Literal['HOSTED', 'HOSTING_FAILED', 'STARTING_HOSTING', 'STOPPING_HOSTING', 'SYSTEM_UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.Tag]
- **Required**: Yes


# TargetPlatform

### Os
- **Type**: typing.Literal['LINUX']
- **Required**: Yes

### Arch
- **Type**: typing.Literal['ARM64', 'X86_64']
- **Required**: Yes

### Accelerator
- **Type**: typing.Optional[typing.Literal['NVIDIA']]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDatasetEntriesRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### Changes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# UpdateDatasetEntriesResponse

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED_ROLLBACK_COMPLETE', 'UPDATE_FAILED_ROLLBACK_IN_PROGRESS', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_classes.ResponseMetadata'>
- **Required**: Yes


