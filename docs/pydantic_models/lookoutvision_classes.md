# Lookoutvision Classes

# AnomalyTypeDef

### Name
- **Type**: typing.Optional[str]

### PixelAnomaly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PixelAnomalyTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDatasetRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.DatasetSourceTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# CreateDatasetResponseTypeDef

### DatasetMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.DatasetMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.OutputConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutvision_classes.TagTypeDef]]


# CreateModelResponseTypeDef

### ModelMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ModelMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateProjectResponseTypeDef

### ProjectMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ProjectMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DatasetDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.DatasetImageStatsTypeDef]


# DatasetGroundTruthManifestTypeDef

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.InputS3ObjectTypeDef]


# DatasetImageStatsTypeDef

### Total
- **Type**: typing.Optional[int]

### Labeled
- **Type**: typing.Optional[int]

### Normal
- **Type**: typing.Optional[int]

### Anomaly
- **Type**: typing.Optional[int]


# DatasetMetadataTypeDef

### DatasetType
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED_ROLLBACK_COMPLETE', 'UPDATE_FAILED_ROLLBACK_IN_PROGRESS', 'UPDATE_IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]


# DatasetSourceTypeDef

### GroundTruthManifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.DatasetGroundTruthManifestTypeDef]


# DeleteDatasetRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteModelRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteModelResponseTypeDef

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteProjectResponseTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### DatasetDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.DatasetDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelPackagingJobRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelPackagingJobResponseTypeDef

### ModelPackagingDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPackagingDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelResponseTypeDef

### ModelDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ModelDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResponseTypeDef

### ProjectDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ProjectDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectAnomaliesRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.BlobTypeDef'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# DetectAnomaliesResponseTypeDef

### DetectAnomalyResult
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.DetectAnomalyResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectAnomalyResultTypeDef

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.ImageSourceTypeDef]

### IsAnomalous
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]

### Anomalies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.AnomalyTypeDef]]

### AnomalyMask
- **Type**: typing.Optional[bytes]


# GreengrassConfigurationOutputTypeDef

### S3OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.S3LocationTypeDef'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilerOptions
- **Type**: typing.Optional[str]

### TargetDevice
- **Type**: typing.Optional[typing.Literal['jetson_xavier']]

### TargetPlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.TargetPlatformTypeDef]

### ComponentVersion
- **Type**: typing.Optional[str]

### ComponentDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.TagTypeDef]]


# GreengrassConfigurationTypeDef

### S3OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.S3LocationTypeDef'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilerOptions
- **Type**: typing.Optional[str]

### TargetDevice
- **Type**: typing.Optional[typing.Literal['jetson_xavier']]

### TargetPlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.TargetPlatformTypeDef]

### ComponentVersion
- **Type**: typing.Optional[str]

### ComponentDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutvision_classes.TagTypeDef]]


# GreengrassOutputDetailsTypeDef

### ComponentVersionArn
- **Type**: typing.Optional[str]

### ComponentName
- **Type**: typing.Optional[str]

### ComponentVersion
- **Type**: typing.Optional[str]


# ImageSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputS3ObjectTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# ListDatasetEntriesRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.TimestampTypeDef]

### AfterCreationDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.TimestampTypeDef]

### SourceRefContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListDatasetEntriesRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.TimestampTypeDef]

### AfterCreationDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.TimestampTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SourceRefContains
- **Type**: typing.Optional[str]


# ListDatasetEntriesResponseTypeDef

### DatasetEntries
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelPackagingJobsRequestPaginateTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListModelPackagingJobsRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelPackagingJobsResponseTypeDef

### ModelPackagingJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPackagingJobMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelsRequestPaginateTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListModelsRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelsResponseTypeDef

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.ModelMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProjectsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListProjectsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProjectsResponseTypeDef

### Projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.ProjectMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModelDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPerformanceTypeDef]

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.OutputConfigTypeDef]

### EvaluationManifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.OutputS3ObjectTypeDef]

### EvaluationResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.OutputS3ObjectTypeDef]

### EvaluationEndTimestamp
- **Type**: typing.Optional[datetime.datetime]

### KmsKeyId
- **Type**: typing.Optional[str]

### MinInferenceUnits
- **Type**: typing.Optional[int]

### MaxInferenceUnits
- **Type**: typing.Optional[int]


# ModelMetadataTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPerformanceTypeDef]


# ModelPackagingConfigurationOutputTypeDef

### Greengrass
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.GreengrassConfigurationOutputTypeDef'>
- **Required**: Yes


# ModelPackagingConfigurationTypeDef

### Greengrass
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.GreengrassConfigurationTypeDef'>
- **Required**: Yes


# ModelPackagingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelPackagingDescriptionTypeDef

### JobName
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### ModelPackagingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPackagingConfigurationOutputTypeDef]

### ModelPackagingJobDescription
- **Type**: typing.Optional[str]

### ModelPackagingMethod
- **Type**: typing.Optional[str]

### ModelPackagingOutputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPackagingOutputDetailsTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'RUNNING', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ModelPackagingJobMetadataTypeDef

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


# ModelPackagingOutputDetailsTypeDef

### Greengrass
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.GreengrassOutputDetailsTypeDef]


# ModelPerformanceTypeDef

### F1Score
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### Precision
- **Type**: typing.Optional[float]


# OutputConfigTypeDef

### S3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.S3LocationTypeDef'>
- **Required**: Yes


# OutputS3ObjectTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PixelAnomalyTypeDef

### TotalPercentageArea
- **Type**: typing.Optional[float]

### Color
- **Type**: typing.Optional[str]


# ProjectDescriptionTypeDef

### ProjectArn
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Datasets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.DatasetMetadataTypeDef]]


# ProjectMetadataTypeDef

### ProjectArn
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]


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


# S3LocationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# StartModelPackagingJobRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPackagingConfigurationUnionTypeDef'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# StartModelPackagingJobResponseTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartModelRequestTypeDef

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


# StartModelResponseTypeDef

### Status
- **Type**: typing.Literal['HOSTED', 'HOSTING_FAILED', 'STARTING_HOSTING', 'STOPPING_HOSTING', 'SYSTEM_UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopModelRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StopModelResponseTypeDef

### Status
- **Type**: typing.Literal['HOSTED', 'HOSTING_FAILED', 'STARTING_HOSTING', 'STOPPING_HOSTING', 'SYSTEM_UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lookoutvision_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetPlatformTypeDef

### Os
- **Type**: typing.Literal['LINUX']
- **Required**: Yes

### Arch
- **Type**: typing.Literal['ARM64', 'X86_64']
- **Required**: Yes

### Accelerator
- **Type**: typing.Optional[typing.Literal['NVIDIA']]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetEntriesRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### Changes
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.BlobTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# UpdateDatasetEntriesResponseTypeDef

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED_ROLLBACK_COMPLETE', 'UPDATE_FAILED_ROLLBACK_IN_PROGRESS', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


