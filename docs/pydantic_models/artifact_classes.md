# Artifact Classes

# AccountSettingsTypeDef

### notificationSubscriptionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SUBSCRIBED', 'SUBSCRIBED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccountSettingsResponseTypeDef

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReportMetadataRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportVersion
- **Type**: typing.Optional[int]


# GetReportMetadataResponseTypeDef

### reportDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ReportDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReportRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### termToken
- **Type**: <class 'str'>
- **Required**: Yes

### reportVersion
- **Type**: typing.Optional[int]


# GetReportResponseTypeDef

### documentPresignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTermForReportRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportVersion
- **Type**: typing.Optional[int]


# GetTermForReportResponseTypeDef

### documentPresignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### termToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReportsRequestListReportsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.artifact_classes.PaginatorConfigTypeDef]


# ListReportsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListReportsResponseTypeDef

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.artifact_classes.ReportSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAccountSettingsRequestRequestTypeDef

### notificationSubscriptionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SUBSCRIBED', 'SUBSCRIBED']]


# PutAccountSettingsResponseTypeDef

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReportDetailTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### periodStart
- **Type**: typing.Optional[datetime.datetime]

### periodEnd
- **Type**: typing.Optional[datetime.datetime]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### deletedAt
- **Type**: typing.Optional[datetime.datetime]

### state
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'UNPUBLISHED']]

### arn
- **Type**: typing.Optional[str]

### series
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[str]

### companyName
- **Type**: typing.Optional[str]

### productName
- **Type**: typing.Optional[str]

### termArn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[int]

### acceptanceType
- **Type**: typing.Optional[typing.Literal['EXPLICIT', 'PASSTHROUGH']]

### sequenceNumber
- **Type**: typing.Optional[int]

### uploadState
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'FAULT', 'PROCESSING']]

### statusMessage
- **Type**: typing.Optional[str]


# ReportSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'UNPUBLISHED']]

### arn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[int]

### uploadState
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'FAULT', 'PROCESSING']]

### description
- **Type**: typing.Optional[str]

### periodStart
- **Type**: typing.Optional[datetime.datetime]

### periodEnd
- **Type**: typing.Optional[datetime.datetime]

### series
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[str]

### companyName
- **Type**: typing.Optional[str]

### productName
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]

### acceptanceType
- **Type**: typing.Optional[typing.Literal['EXPLICIT', 'PASSTHROUGH']]


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


