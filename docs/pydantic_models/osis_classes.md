# osis_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BufferOptionsTypeDef

### PersistentBufferEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ChangeProgressStageTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING']]

### Description
- **Type**: typing.Optional[str]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ChangeProgressStatusTypeDef

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING']]

### TotalNumberOfStages
- **Type**: typing.Optional[int]

### ChangeProgressStages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis_classes.ChangeProgressStageTypeDef]]


# CloudWatchLogDestinationTypeDef

### LogGroup
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePipelineRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.LogPublishingOptionsTypeDef]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.VpcOptionsTypeDef]

### BufferOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.BufferOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.EncryptionAtRestOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.osis_classes.TagTypeDef]]


# CreatePipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePipelineRequestRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# EncryptionAtRestOptionsTypeDef

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineBlueprintRequestRequestTypeDef

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[str]


# GetPipelineBlueprintResponseTypeDef

### Blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.PipelineBlueprintTypeDef'>
- **Required**: Yes

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPipelineChangeProgressRequestRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineChangeProgressResponseTypeDef

### ChangeProgressStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis_classes.ChangeProgressStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPipelineRequestRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPipelineBlueprintsResponseTypeDef

### Blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis_classes.PipelineBlueprintSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPipelinesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPipelinesResponseTypeDef

### Pipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis_classes.PipelineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogPublishingOptionsTypeDef

### IsLoggingEnabled
- **Type**: typing.Optional[bool]

### CloudWatchLogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.CloudWatchLogDestinationTypeDef]


# PipelineBlueprintSummaryTypeDef

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


# PipelineBlueprintTypeDef

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


# PipelineDestinationTypeDef

### ServiceName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]


# PipelineStatusReasonTypeDef

### Description
- **Type**: typing.Optional[str]


# PipelineSummaryTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']]

### StatusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.PipelineStatusReasonTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis_classes.PipelineDestinationTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis_classes.TagTypeDef]]


# PipelineTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.PipelineStatusReasonTypeDef]

### PipelineConfigurationBody
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### IngestEndpointUrls
- **Type**: typing.Optional[typing.List[str]]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.LogPublishingOptionsTypeDef]

### VpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis_classes.VpcEndpointTypeDef]]

### BufferOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.BufferOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.EncryptionAtRestOptionsTypeDef]

### VpcEndpointService
- **Type**: typing.Optional[str]

### ServiceVpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis_classes.ServiceVpcEndpointTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis_classes.PipelineDestinationTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.osis_classes.TagTypeDef]]


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


# ServiceVpcEndpointTypeDef

### ServiceName
- **Type**: typing.Optional[typing.Literal['OPENSEARCH_SERVERLESS']]

### VpcEndpointId
- **Type**: typing.Optional[str]


# StartPipelineRequestRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopPipelineRequestRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.osis_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdatePipelineRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.LogPublishingOptionsTypeDef]

### BufferOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.BufferOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.EncryptionAtRestOptionsTypeDef]


# UpdatePipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidatePipelineRequestRequestTypeDef

### PipelineConfigurationBody
- **Type**: <class 'str'>
- **Required**: Yes


# ValidatePipelineResponseTypeDef

### isValid
- **Type**: <class 'bool'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.osis_classes.ValidationMessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.osis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidationMessageTypeDef

### Message
- **Type**: typing.Optional[str]


# VpcAttachmentOptionsTypeDef

### AttachToVpc
- **Type**: <class 'bool'>
- **Required**: Yes

### CidrBlock
- **Type**: typing.Optional[str]


# VpcEndpointTypeDef

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.VpcOptionsOutputTypeDef]


# VpcOptionsOutputTypeDef

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### VpcAttachmentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.VpcAttachmentOptionsTypeDef]

### VpcEndpointManagement
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


# VpcOptionsTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcAttachmentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.osis_classes.VpcAttachmentOptionsTypeDef]

### VpcEndpointManagement
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


