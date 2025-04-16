# Artifact Classes

# AccountSettings

### notificationSubscriptionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SUBSCRIBED', 'SUBSCRIBED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomerAgreementSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccountSettingsResponse

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetReportMetadataRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportVersion
- **Type**: typing.Optional[int]


# GetReportMetadataResponse

### reportDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ReportDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetReportRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### termToken
- **Type**: <class 'str'>
- **Required**: Yes

### reportVersion
- **Type**: typing.Optional[int]


# GetReportResponse

### documentPresignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetTermForReportRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportVersion
- **Type**: typing.Optional[int]


# GetTermForReportResponse

### documentPresignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### termToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# ListCustomerAgreementsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomerAgreementsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.artifact_classes.PaginatorConfig]


# ListCustomerAgreementsResponse

### customerAgreements
- **Type**: typing.List[aws_resource_validator.pydantic_models.artifact_classes.CustomerAgreementSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListReportsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.artifact_classes.PaginatorConfig]


# ListReportsResponse

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.artifact_classes.ReportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadata'>
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


# PutAccountSettingsRequest

### notificationSubscriptionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SUBSCRIBED', 'SUBSCRIBED']]


# PutAccountSettingsResponse

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# ReportDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReportSummary

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


