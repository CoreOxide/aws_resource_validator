# Applicationcostprofiler Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteReportDefinitionRequestTypeDef

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


# GetReportDefinitionRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportApplicationUsageRequestTypeDef

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


# ListReportDefinitionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.applicationcostprofiler_classes.PaginatorConfigTypeDef]


# ListReportDefinitionsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReportDefinitionsResultTypeDef

### reportDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ReportDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutReportDefinitionResultTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReportDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# UpdateReportDefinitionResultTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


