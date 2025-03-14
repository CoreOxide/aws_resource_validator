# Supplychain Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillOfMaterialsImportJobTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'NEW', 'QUEUED', 'SUCCESS']
- **Required**: Yes

### s3uri
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# CreateBillOfMaterialsImportJobRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### s3uri
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateBillOfMaterialsImportJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataIntegrationFlowRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowSourceTypeDef]
- **Required**: Yes

### transformation
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTransformationTypeDef'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTargetTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDataIntegrationFlowResponseTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataLakeDatasetRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetSchemaUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDataLakeDatasetResponseTypeDef

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceRequestTypeDef

### instanceName
- **Type**: typing.Optional[str]

### instanceDescription
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### webAppDnsDomain
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateInstanceResponseTypeDef

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.InstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataIntegrationFlowDatasetOptionsTypeDef

### loadType
- **Type**: typing.Optional[typing.Literal['INCREMENTAL', 'REPLACE']]

### dedupeRecords
- **Type**: typing.Optional[bool]


# DataIntegrationFlowDatasetSourceConfigurationTypeDef

### datasetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowDatasetOptionsTypeDef]


# DataIntegrationFlowDatasetTargetConfigurationTypeDef

### datasetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowDatasetOptionsTypeDef]


# DataIntegrationFlowS3OptionsTypeDef

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]


# DataIntegrationFlowS3SourceConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowS3OptionsTypeDef]


# DataIntegrationFlowS3TargetConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowS3OptionsTypeDef]


# DataIntegrationFlowSQLTransformationConfigurationTypeDef

### query
- **Type**: <class 'str'>
- **Required**: Yes


# DataIntegrationFlowSourceTypeDef

### sourceType
- **Type**: typing.Literal['DATASET', 'S3']
- **Required**: Yes

### sourceName
- **Type**: <class 'str'>
- **Required**: Yes

### s3Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowS3SourceConfigurationTypeDef]

### datasetSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowDatasetSourceConfigurationTypeDef]


# DataIntegrationFlowTargetTypeDef

### targetType
- **Type**: typing.Literal['DATASET', 'S3']
- **Required**: Yes

### s3Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowS3TargetConfigurationTypeDef]

### datasetTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowDatasetTargetConfigurationTypeDef]


# DataIntegrationFlowTransformationTypeDef

### transformationType
- **Type**: typing.Literal['NONE', 'SQL']
- **Required**: Yes

### sqlTransformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowSQLTransformationConfigurationTypeDef]


# DataIntegrationFlowTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowSourceTypeDef]
- **Required**: Yes

### transformation
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTransformationTypeDef'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTargetTypeDef'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# DataLakeDatasetSchemaFieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataLakeDatasetSchemaOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetSchemaFieldTypeDef]
- **Required**: Yes


# DataLakeDatasetSchemaTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetSchemaFieldTypeDef]
- **Required**: Yes


# DataLakeDatasetSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataLakeDatasetTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetSchemaOutputTypeDef'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetTypeDef'>>

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# DeleteDataIntegrationFlowRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataIntegrationFlowResponseTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataLakeDatasetRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataLakeDatasetResponseTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInstanceRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceResponseTypeDef

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.InstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBillOfMaterialsImportJobRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBillOfMaterialsImportJobResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.BillOfMaterialsImportJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataIntegrationFlowRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataIntegrationFlowResponseTypeDef

### flow
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataLakeDatasetRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataLakeDatasetResponseTypeDef

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceResponseTypeDef

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.InstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['Active', 'CreateFailed', 'DeleteFailed', 'Deleted', 'Deleting', 'Initializing']
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[str]

### webAppDnsDomain
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### instanceName
- **Type**: typing.Optional[str]

### instanceDescription
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### versionNumber
- **Type**: typing.Optional[float]


# ListDataIntegrationFlowsRequestPaginateTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.PaginatorConfigTypeDef]


# ListDataIntegrationFlowsRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataIntegrationFlowsResponseTypeDef

### flows
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataLakeDatasetsRequestPaginateTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.PaginatorConfigTypeDef]


# ListDataLakeDatasetsRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataLakeDatasetsResponseTypeDef

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInstancesRequestPaginateTypeDef

### instanceNameFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### instanceStateFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'CreateFailed', 'DeleteFailed', 'Deleted', 'Deleting', 'Initializing']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.PaginatorConfigTypeDef]


# ListInstancesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### instanceNameFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### instanceStateFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'CreateFailed', 'DeleteFailed', 'Deleted', 'Deleting', 'Initializing']]]


# ListInstancesResponseTypeDef

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain_classes.InstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SendDataIntegrationEventRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: typing.Literal['scn.data.forecast', 'scn.data.inboundorder', 'scn.data.inboundorderline', 'scn.data.inboundorderlineschedule', 'scn.data.inventorylevel', 'scn.data.outboundorderline', 'scn.data.outboundshipment', 'scn.data.processheader', 'scn.data.processoperation', 'scn.data.processproduct', 'scn.data.reservation', 'scn.data.shipment', 'scn.data.shipmentstop', 'scn.data.shipmentstoporder', 'scn.data.supplyplan']
- **Required**: Yes

### data
- **Type**: <class 'str'>
- **Required**: Yes

### eventGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.TimestampTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# SendDataIntegrationEventResponseTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# UpdateDataIntegrationFlowRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowSourceTypeDef]]

### transformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTransformationTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTargetTypeDef]


# UpdateDataIntegrationFlowResponseTypeDef

### flow
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataIntegrationFlowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataLakeDatasetRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateDataLakeDatasetResponseTypeDef

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.DataLakeDatasetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInstanceRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceName
- **Type**: typing.Optional[str]

### instanceDescription
- **Type**: typing.Optional[str]


# UpdateInstanceResponseTypeDef

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.InstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


