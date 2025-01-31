# Lookoutvision Classes

# AnomalyTypeDef

### Name
- **Type**: typing.Optional[str]

### PixelAnomaly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PixelAnomalyTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDatasetRequestRequestTypeDef

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


# CreateModelRequestRequestTypeDef

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


# CreateProjectRequestRequestTypeDef

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


# DeleteDatasetRequestRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteModelRequestRequestTypeDef

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


# DeleteProjectRequestRequestTypeDef

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


# DescribeDatasetRequestRequestTypeDef

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


# DescribeModelPackagingJobRequestRequestTypeDef

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


# DescribeModelRequestRequestTypeDef

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


# DescribeProjectRequestRequestTypeDef

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


# DetectAnomaliesRequestRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.TagTypeDef]]


# GreengrassOutputDetailsTypeDef

### ComponentVersionArn
- **Type**: typing.Optional[str]

### ComponentName
- **Type**: typing.Optional[str]

### ComponentVersion
- **Type**: typing.Optional[str]


# ImageSourceTypeDef

### Type
- **Type**: typing.Optional[str]


# InputS3ObjectTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListDatasetEntriesRequestRequestTypeDef

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


# ListDatasetEntriesResponseTypeDef

### DatasetEntries
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListModelPackagingJobsRequestListModelPackagingJobsPaginateTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListModelPackagingJobsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListModelsRequestListModelsPaginateTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListModelsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProjectsResponseTypeDef

### Projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutvision_classes.ProjectMetadataTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ModelPackagingConfigurationTypeDef

### Greengrass
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.GreengrassConfigurationTypeDef'>
- **Required**: Yes


# ModelPackagingDescriptionTypeDef

### JobName
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### ModelPackagingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPackagingConfigurationTypeDef]

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

### HostId
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


# S3LocationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# StartModelPackagingJobRequestRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutvision_classes.ModelPackagingConfigurationTypeDef'>
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


# StartModelRequestRequestTypeDef

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


# StopModelRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetEntriesRequestRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetType
- **Type**: <class 'str'>
- **Required**: Yes

### Changes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


