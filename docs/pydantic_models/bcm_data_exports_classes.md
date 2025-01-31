# Bcm Data Exports Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnTypeDef

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# CreateExportRequestRequestTypeDef

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportTypeDef'>
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


# DataQueryTypeDef

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### TableConfigurations
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]


# DeleteExportRequestRequestTypeDef

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


# GetExecutionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExportRequestRequestTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportResponseTypeDef

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportTypeDef'>
- **Required**: Yes

### ExportStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableRequestRequestTypeDef

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


# ListExecutionsRequestListExecutionsPaginateTypeDef

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfigTypeDef]


# ListExecutionsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExportsRequestListExportsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfigTypeDef]


# ListExportsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExportsResponseTypeDef

### Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportReferenceTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTablesRequestListTablesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfigTypeDef]


# ListTablesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTablesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.TableTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTagTypeDef]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateExportRequestRequestTypeDef

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportTypeDef'>
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


