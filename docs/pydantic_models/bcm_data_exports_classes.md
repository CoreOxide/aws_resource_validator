# Bcm Data Exports Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateExportRequestTypeDef

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportUnionTypeDef'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTagTypeDef]]


# CreateExportResponseTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataQueryOutputTypeDef

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### TableConfigurations
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# DataQueryTypeDef

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### TableConfigurations
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]


# DeleteExportRequestTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExportResponseTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationConfigurationsTypeDef

### S3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.S3DestinationTypeDef'>
- **Required**: Yes


# ExecutionReferenceTypeDef

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExecutionStatusTypeDef'>
- **Required**: Yes


# ExecutionStatusTypeDef

### CompletedAt
- **Type**: typing.Optional[datetime.datetime]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### StatusCode
- **Type**: typing.Optional[typing.Literal['DELIVERY_FAILURE', 'DELIVERY_IN_PROCESS', 'DELIVERY_SUCCESS', 'INITIATION_IN_PROCESS', 'QUERY_FAILURE', 'QUERY_IN_PROCESS', 'QUERY_QUEUED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['BILL_OWNER_CHANGED', 'INSUFFICIENT_PERMISSION', 'INTERNAL_FAILURE']]


# ExportOutputTypeDef

### DataQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DataQueryOutputTypeDef'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DestinationConfigurationsTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshCadence
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.RefreshCadenceTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ExportArn
- **Type**: typing.Optional[str]


# ExportReferenceTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportName
- **Type**: <class 'str'>
- **Required**: Yes

### ExportStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportStatusTypeDef'>
- **Required**: Yes


# ExportStatusTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastRefreshedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### StatusCode
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['BILL_OWNER_CHANGED', 'INSUFFICIENT_PERMISSION', 'INTERNAL_FAILURE']]


# ExportTypeDef

### DataQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DataQueryTypeDef'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DestinationConfigurationsTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshCadence
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.RefreshCadenceTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ExportArn
- **Type**: typing.Optional[str]


# ExportUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetExecutionRequestTypeDef

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetExecutionResponseTypeDef

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExecutionStatusTypeDef'>
- **Required**: Yes

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExportRequestTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportResponseTypeDef

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportOutputTypeDef'>
- **Required**: Yes

### ExportStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableRequestTypeDef

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TableProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetTableResponseTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ColumnTypeDef]
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TableProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExecutionsRequestPaginateTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfigTypeDef]


# ListExecutionsRequestTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExecutionsResponseTypeDef

### Executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExecutionReferenceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExportsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfigTypeDef]


# ListExportsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExportsResponseTypeDef

### Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportReferenceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTablesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfigTypeDef]


# ListTablesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTablesResponseTypeDef

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.TableTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RefreshCadenceTypeDef

### Frequency
- **Type**: typing.Literal['SYNCHRONOUS']
- **Required**: Yes


# ResourceTagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
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


# S3DestinationTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3OutputConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.S3OutputConfigurationsTypeDef'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### S3Region
- **Type**: <class 'str'>
- **Required**: Yes


# S3OutputConfigurationsTypeDef

### Compression
- **Type**: typing.Literal['GZIP', 'PARQUET']
- **Required**: Yes

### Format
- **Type**: typing.Literal['PARQUET', 'TEXT_OR_CSV']
- **Required**: Yes

### OutputType
- **Type**: typing.Literal['CUSTOM']
- **Required**: Yes

### Overwrite
- **Type**: typing.Literal['CREATE_NEW_REPORT', 'OVERWRITE_REPORT']
- **Required**: Yes


# TablePropertyDescriptionTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ValidValues
- **Type**: typing.Optional[typing.List[str]]


# TableTypeDef

### Description
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### TableProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.TablePropertyDescriptionTypeDef]]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTagTypeDef]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateExportRequestTypeDef

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportUnionTypeDef'>
- **Required**: Yes

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateExportResponseTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


