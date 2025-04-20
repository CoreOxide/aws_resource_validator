# Supplychain Supplychain Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillOfMaterialsImportJob

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


# CreateBillOfMaterialsImportJobRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### s3uri
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateBillOfMaterialsImportJobResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataIntegrationFlowRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowSource]
- **Required**: Yes

### transformation
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowTransformation'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowTarget'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDataIntegrationFlowResponse

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataLakeDatasetRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDatasetSchema, aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDatasetSchemaOutput, NoneType]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDataLakeDatasetResponse

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDataset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceRequest

### instanceName
- **Type**: typing.Optional[str]

### instanceDescription
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### webAppDnsDomain
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateInstanceResponse

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.Instance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# DataIntegrationFlow

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowSource]
- **Required**: Yes

### transformation
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowTransformation'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowTarget'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# DataIntegrationFlowDatasetOptions

### loadType
- **Type**: typing.Optional[typing.Literal['INCREMENTAL', 'REPLACE']]

### dedupeRecords
- **Type**: typing.Optional[bool]


# DataIntegrationFlowDatasetSourceConfiguration

### datasetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowDatasetOptions]


# DataIntegrationFlowDatasetTargetConfiguration

### datasetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowDatasetOptions]


# DataIntegrationFlowS3Options

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]


# DataIntegrationFlowS3SourceConfiguration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowS3Options]


# DataIntegrationFlowS3TargetConfiguration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowS3Options]


# DataIntegrationFlowSQLTransformationConfiguration

### query
- **Type**: <class 'str'>
- **Required**: Yes


# DataIntegrationFlowSource

### sourceType
- **Type**: typing.Literal['DATASET', 'S3']
- **Required**: Yes

### sourceName
- **Type**: <class 'str'>
- **Required**: Yes

### s3Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowS3SourceConfiguration]

### datasetSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowDatasetSourceConfiguration]


# DataIntegrationFlowTarget

### targetType
- **Type**: typing.Literal['DATASET', 'S3']
- **Required**: Yes

### s3Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowS3TargetConfiguration]

### datasetTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowDatasetTargetConfiguration]


# DataIntegrationFlowTransformation

### transformationType
- **Type**: typing.Literal['NONE', 'SQL']
- **Required**: Yes

### sqlTransformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowSQLTransformationConfiguration]


# DataLakeDataset

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
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDatasetSchemaOutput'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDataset'>>

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# DataLakeDatasetSchema

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDatasetSchemaField]
- **Required**: Yes


# DataLakeDatasetSchemaField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DOUBLE', 'INT', 'STRING', 'TIMESTAMP']
- **Required**: Yes

### isRequired
- **Type**: <class 'bool'>
- **Required**: Yes


# DataLakeDatasetSchemaOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDatasetSchemaField]
- **Required**: Yes


# DeleteDataIntegrationFlowRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataIntegrationFlowResponse

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataLakeDatasetRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataLakeDatasetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInstanceRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceResponse

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.Instance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# GetBillOfMaterialsImportJobRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBillOfMaterialsImportJobResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.BillOfMaterialsImportJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataIntegrationFlowRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataIntegrationFlowResponse

### flow
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataLakeDatasetRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataLakeDatasetResponse

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDataset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceResponse

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.Instance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# Instance

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


# ListDataIntegrationFlowsRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataIntegrationFlowsRequestPaginate

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.PaginatorConfig]


# ListDataIntegrationFlowsResponse

### flows
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlow]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataLakeDatasetsRequest

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


# ListDataLakeDatasetsRequestPaginate

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.PaginatorConfig]


# ListDataLakeDatasetsResponse

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDataset]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInstancesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### instanceNameFilter
- **Type**: typing.Optional[typing.List[str]]

### instanceStateFilter
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'CreateFailed', 'DeleteFailed', 'Deleted', 'Deleting', 'Initializing']]]


# ListInstancesRequestPaginate

### instanceNameFilter
- **Type**: typing.Optional[typing.List[str]]

### instanceStateFilter
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'CreateFailed', 'DeleteFailed', 'Deleted', 'Deleting', 'Initializing']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.PaginatorConfig]


# ListInstancesResponse

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.Instance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SendDataIntegrationEventRequest

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### clientToken
- **Type**: typing.Optional[str]


# SendDataIntegrationEventResponse

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDataIntegrationFlowRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowSource]]

### transformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowTransformation]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlowTarget]


# UpdateDataIntegrationFlowResponse

### flow
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataIntegrationFlow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataLakeDatasetRequest

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


# UpdateDataLakeDatasetResponse

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.DataLakeDataset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInstanceRequest

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceName
- **Type**: typing.Optional[str]

### instanceDescription
- **Type**: typing.Optional[str]


# UpdateInstanceResponse

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.Instance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain.supplychain_classes.ResponseMetadata'>
- **Required**: Yes


