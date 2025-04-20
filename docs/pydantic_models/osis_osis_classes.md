# Osis Osis Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BufferOptions

### PersistentBufferEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ChangeProgressStage

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING']]

### Description
- **Type**: typing.Optional[str]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ChangeProgressStatus

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING']]

### TotalNumberOfStages
- **Type**: typing.Optional[int]

### ChangeProgressStages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.ChangeProgressStage]]


# CloudWatchLogDestination

### LogGroup
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### MinUnits
- **Type**: <class 'int'>
- **Required**: Yes

### MaxUnits
- **Type**: <class 'int'>
- **Required**: Yes

### PipelineConfigurationBody
- **Type**: <class 'str'>
- **Required**: Yes

### LogPublishingOptions
- **Type**: <class 'NoneType'>

### VpcOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.osis.osis_classes.VpcOptions, aws_resource_validator.pydantic_models.osis.osis_classes.VpcOptionsOutput, NoneType]

### BufferOptions
- **Type**: <class 'NoneType'>

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.Tag]]


# CreatePipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# EncryptionAtRestOptions

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineBlueprintRequest

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[str]


# GetPipelineBlueprintResponse

### Blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.PipelineBlueprint'>
- **Required**: Yes

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# GetPipelineChangeProgressRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineChangeProgressResponse

### ChangeProgressStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.ChangeProgressStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# GetPipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# ListPipelineBlueprintsResponse

### Blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.PipelineBlueprintSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# ListPipelinesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPipelinesResponse

### Pipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.PipelineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# LogPublishingOptions

### IsLoggingEnabled
- **Type**: typing.Optional[bool]

### CloudWatchLogDestination
- **Type**: <class 'NoneType'>


# Pipeline

### PipelineName
- **Type**: typing.Optional[str]

### PipelineArn
- **Type**: typing.Optional[str]

### MinUnits
- **Type**: typing.Optional[int]

### MaxUnits
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']]

### StatusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis.osis_classes.PipelineStatusReason]

### PipelineConfigurationBody
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### IngestEndpointUrls
- **Type**: typing.Optional[typing.List[str]]

### LogPublishingOptions
- **Type**: <class 'NoneType'>

### VpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.VpcEndpoint]]

### BufferOptions
- **Type**: <class 'NoneType'>

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>

### VpcEndpointService
- **Type**: typing.Optional[str]

### ServiceVpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.ServiceVpcEndpoint]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.PipelineDestination]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.Tag]]


# PipelineBlueprint

### BlueprintName
- **Type**: typing.Optional[str]

### PipelineConfigurationBody
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### DisplayDescription
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]

### UseCase
- **Type**: typing.Optional[str]


# PipelineBlueprintSummary

### BlueprintName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### DisplayDescription
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]

### UseCase
- **Type**: typing.Optional[str]


# PipelineDestination

### ServiceName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]


# PipelineStatusReason

### Description
- **Type**: typing.Optional[str]


# PipelineSummary

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']]

### StatusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis.osis_classes.PipelineStatusReason]

### PipelineName
- **Type**: typing.Optional[str]

### PipelineArn
- **Type**: typing.Optional[str]

### MinUnits
- **Type**: typing.Optional[int]

### MaxUnits
- **Type**: typing.Optional[int]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.PipelineDestination]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.Tag]]


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


# ServiceVpcEndpoint

### ServiceName
- **Type**: typing.Optional[typing.Literal['OPENSEARCH_SERVERLESS']]

### VpcEndpointId
- **Type**: typing.Optional[str]


# StartPipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# StopPipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdatePipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### MinUnits
- **Type**: typing.Optional[int]

### MaxUnits
- **Type**: typing.Optional[int]

### PipelineConfigurationBody
- **Type**: typing.Optional[str]

### LogPublishingOptions
- **Type**: <class 'NoneType'>

### BufferOptions
- **Type**: <class 'NoneType'>

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>


# UpdatePipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# ValidatePipelineRequest

### PipelineConfigurationBody
- **Type**: <class 'str'>
- **Required**: Yes


# ValidatePipelineResponse

### isValid
- **Type**: <class 'bool'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis.osis_classes.ValidationMessage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis.osis_classes.ResponseMetadata'>
- **Required**: Yes


# ValidationMessage

### Message
- **Type**: typing.Optional[str]


# VpcAttachmentOptions

### AttachToVpc
- **Type**: <class 'bool'>
- **Required**: Yes

### CidrBlock
- **Type**: typing.Optional[str]


# VpcEndpoint

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis.osis_classes.VpcOptionsOutput]


# VpcOptions

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### VpcAttachmentOptions
- **Type**: <class 'NoneType'>

### VpcEndpointManagement
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


# VpcOptionsOutput

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### VpcAttachmentOptions
- **Type**: <class 'NoneType'>

### VpcEndpointManagement
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


