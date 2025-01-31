# Cur Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteReportDefinitionRequestRequestTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportDefinitionResponseTypeDef

### ResponseMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cur_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReportDefinitionsRequestDescribeReportDefinitionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cur_classes.PaginatorConfigTypeDef]


# DescribeReportDefinitionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReportDefinitionsResponseTypeDef

### ReportDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cur_classes.ReportDefinitionExtraOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cur_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cur_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cur_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyReportDefinitionRequestRequestTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.cur_classes.ReportDefinitionTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutReportDefinitionRequestRequestTypeDef

### ReportDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.cur_classes.ReportDefinitionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cur_classes.TagTypeDef]]


# ReportDefinitionExtraOutputTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeUnit
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Format
- **Type**: typing.Literal['Parquet', 'textORcsv']
- **Required**: Yes

### Compression
- **Type**: typing.Literal['GZIP', 'Parquet', 'ZIP']
- **Required**: Yes

### AdditionalSchemaElements
- **Type**: typing.List[typing.Literal['MANUAL_DISCOUNT_COMPATIBILITY', 'RESOURCES', 'SPLIT_COST_ALLOCATION_DATA']]
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### S3Region
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
- **Required**: Yes

### AdditionalArtifacts
- **Type**: typing.Optional[typing.List[typing.Literal['ATHENA', 'QUICKSIGHT', 'REDSHIFT']]]

### RefreshClosedReports
- **Type**: typing.Optional[bool]

### ReportVersioning
- **Type**: typing.Optional[typing.Literal['CREATE_NEW_REPORT', 'OVERWRITE_REPORT']]

### BillingViewArn
- **Type**: typing.Optional[str]

### ReportStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cur_classes.ReportStatusTypeDef]


# ReportDefinitionOutputTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeUnit
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Format
- **Type**: typing.Literal['Parquet', 'textORcsv']
- **Required**: Yes

### Compression
- **Type**: typing.Literal['GZIP', 'Parquet', 'ZIP']
- **Required**: Yes

### AdditionalSchemaElements
- **Type**: typing.List[typing.Literal['MANUAL_DISCOUNT_COMPATIBILITY', 'RESOURCES', 'SPLIT_COST_ALLOCATION_DATA']]
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### S3Region
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
- **Required**: Yes

### AdditionalArtifacts
- **Type**: typing.Optional[typing.List[typing.Literal['ATHENA', 'QUICKSIGHT', 'REDSHIFT']]]

### RefreshClosedReports
- **Type**: typing.Optional[bool]

### ReportVersioning
- **Type**: typing.Optional[typing.Literal['CREATE_NEW_REPORT', 'OVERWRITE_REPORT']]

### BillingViewArn
- **Type**: typing.Optional[str]

### ReportStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cur_classes.ReportStatusTypeDef]


# ReportDefinitionTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeUnit
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Format
- **Type**: typing.Literal['Parquet', 'textORcsv']
- **Required**: Yes

### Compression
- **Type**: typing.Literal['GZIP', 'Parquet', 'ZIP']
- **Required**: Yes

### AdditionalSchemaElements
- **Type**: typing.Sequence[typing.Literal['MANUAL_DISCOUNT_COMPATIBILITY', 'RESOURCES', 'SPLIT_COST_ALLOCATION_DATA']]
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### S3Region
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
- **Required**: Yes

### AdditionalArtifacts
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ATHENA', 'QUICKSIGHT', 'REDSHIFT']]]

### RefreshClosedReports
- **Type**: typing.Optional[bool]

### ReportVersioning
- **Type**: typing.Optional[typing.Literal['CREATE_NEW_REPORT', 'OVERWRITE_REPORT']]

### BillingViewArn
- **Type**: typing.Optional[str]

### ReportStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cur_classes.ReportStatusTypeDef]


# ReportStatusTypeDef

### lastDelivery
- **Type**: typing.Optional[str]

### lastStatus
- **Type**: typing.Optional[typing.Literal['ERROR_NO_BUCKET', 'ERROR_PERMISSIONS', 'SUCCESS']]


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


# TagResourceRequestRequestTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cur_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ReportName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


