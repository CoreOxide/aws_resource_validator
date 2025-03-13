# Artifact Classes

# AccountSettingsTypeDef

### notificationSubscriptionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SUBSCRIBED', 'SUBSCRIBED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomerAgreementSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccountSettingsResponseTypeDef

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReportMetadataRequestTypeDef

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


# GetReportRequestTypeDef

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


# GetTermForReportRequestTypeDef

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


# ListCustomerAgreementsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.artifact_classes.PaginatorConfigTypeDef]


# ListCustomerAgreementsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomerAgreementsResponseTypeDef

### customerAgreements
- **Type**: typing.List[aws_resource_validator.pydantic_models.artifact_classes.CustomerAgreementSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.artifact_classes.PaginatorConfigTypeDef]


# ListReportsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListReportsResponseTypeDef

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.artifact_classes.ReportSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact_classes.ResponseMetadataTypeDef'>
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


# PutAccountSettingsRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReportSummaryTypeDef

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


