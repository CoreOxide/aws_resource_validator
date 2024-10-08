# Pydantic Models in applicationcostprofiler_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteReportDefinitionRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportDefinitionResultTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReportDefinitionRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReportDefinitionResultTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportDescription
- **Type**: <class 'str'>
- **Required**: Yes

### reportFrequency
- **Type**: typing.Literal['ALL', 'DAILY', 'MONTHLY']
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destinationS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.S3LocationTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportApplicationUsageRequestRequestTypeDef

### sourceS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.SourceS3LocationTypeDef'>
- **Required**: Yes


# ImportApplicationUsageResultTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReportDefinitionsRequestListReportDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.applicationcostprofiler_classes.PaginatorConfigTypeDef]


# ListReportDefinitionsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReportDefinitionsResultTypeDef

### reportDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ReportDefinitionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutReportDefinitionRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportDescription
- **Type**: <class 'str'>
- **Required**: Yes

### reportFrequency
- **Type**: typing.Literal['ALL', 'DAILY', 'MONTHLY']
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destinationS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.S3LocationTypeDef'>
- **Required**: Yes


# PutReportDefinitionResultTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReportDefinitionTypeDef

### reportId
- **Type**: typing.Optional[str]

### reportDescription
- **Type**: typing.Optional[str]

### reportFrequency
- **Type**: typing.Optional[typing.Literal['ALL', 'DAILY', 'MONTHLY']]

### format
- **Type**: typing.Optional[typing.Literal['CSV', 'PARQUET']]

### destinationS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.applicationcostprofiler_classes.S3LocationTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
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

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes


# SourceS3LocationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'eu-south-1', 'me-south-1']]


# UpdateReportDefinitionRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportDescription
- **Type**: <class 'str'>
- **Required**: Yes

### reportFrequency
- **Type**: typing.Literal['ALL', 'DAILY', 'MONTHLY']
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destinationS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.S3LocationTypeDef'>
- **Required**: Yes


# UpdateReportDefinitionResultTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


