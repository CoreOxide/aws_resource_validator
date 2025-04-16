# Applicationcostprofiler Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteReportDefinitionRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportDefinitionResult

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# GetReportDefinitionRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportApplicationUsageRequest

### sourceS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.SourceS3Location'>
- **Required**: Yes


# ImportApplicationUsageResult

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# ListReportDefinitionsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReportDefinitionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.applicationcostprofiler_classes.PaginatorConfig]


# ListReportDefinitionsResult

### reportDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ReportDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutReportDefinitionResult

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# ReportDefinition

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# S3Location

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes


# SourceS3Location

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'eu-south-1', 'me-south-1']]


# UpdateReportDefinitionResult

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.applicationcostprofiler_classes.ResponseMetadata'>
- **Required**: Yes


