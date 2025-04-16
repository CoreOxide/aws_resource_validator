# Bcm Data Exports Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Column

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateExportRequest

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportUnion'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTag]]


# CreateExportResponse

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes


# DataQuery

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### TableConfigurations
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]


# DataQueryOutput

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### TableConfigurations
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# DeleteExportRequest

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExportResponse

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationConfigurations

### S3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.S3Destination'>
- **Required**: Yes


# ExecutionReference

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExecutionStatus'>
- **Required**: Yes


# ExecutionStatus

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


# Export

### DataQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DataQuery'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DestinationConfigurations'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshCadence
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.RefreshCadence'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ExportArn
- **Type**: typing.Optional[str]


# ExportOutput

### DataQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DataQueryOutput'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.DestinationConfigurations'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshCadence
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.RefreshCadence'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ExportArn
- **Type**: typing.Optional[str]


# ExportReference

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportName
- **Type**: <class 'str'>
- **Required**: Yes

### ExportStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportStatus'>
- **Required**: Yes


# ExportStatus

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


# ExportUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetExecutionRequest

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetExecutionResponse

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExecutionStatus'>
- **Required**: Yes

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes


# GetExportRequest

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportResponse

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportOutput'>
- **Required**: Yes

### ExportStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableRequest

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TableProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetTableResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.Column]
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TableProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes


# ListExecutionsRequest

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExecutionsRequestPaginate

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfig]


# ListExecutionsResponse

### Executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExecutionReference]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExportsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExportsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfig]


# ListExportsResponse

### Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportReference]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTablesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTablesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_data_exports_classes.PaginatorConfig]


# ListTablesResponse

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.Table]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponse

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RefreshCadence

### Frequency
- **Type**: typing.Literal['SYNCHRONOUS']
- **Required**: Yes


# ResourceTag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


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


# S3Destination

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3OutputConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.S3OutputConfigurations'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### S3Region
- **Type**: <class 'str'>
- **Required**: Yes


# S3OutputConfigurations

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


# Table

### Description
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### TableProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_data_exports_classes.TablePropertyDescription]]


# TablePropertyDescription

### DefaultValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ValidValues
- **Type**: typing.Optional[typing.List[str]]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResourceTag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateExportRequest

### Export
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ExportUnion'>
- **Required**: Yes

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateExportResponse

### ExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_data_exports_classes.ResponseMetadata'>
- **Required**: Yes


