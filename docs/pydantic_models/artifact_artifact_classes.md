# Artifact Artifact Classes

# AccountSettings

### notificationSubscriptionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SUBSCRIBED', 'SUBSCRIBED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomerAgreementSummary

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### agreementArn
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]

### organizationArn
- **Type**: typing.Optional[str]

### effectiveStart
- **Type**: typing.Optional[datetime.datetime]

### effectiveEnd
- **Type**: typing.Optional[datetime.datetime]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AWS_TERMINATED', 'CUSTOMER_TERMINATED']]

### description
- **Type**: typing.Optional[str]

### acceptanceTerms
- **Type**: typing.Optional[typing.List[str]]

### terminateTerms
- **Type**: typing.Optional[typing.List[str]]

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT', 'MODIFIED']]


# GetAccountSettingsResponse

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetReportMetadataRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### reportVersion
- **Type**: typing.Optional[int]


# GetReportMetadataResponse

### reportDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ReportDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# ListCustomerAgreementsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomerAgreementsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.artifact.artifact_classes.PaginatorConfig]


# ListCustomerAgreementsResponse

### customerAgreements
- **Type**: typing.List[aws_resource_validator.pydantic_models.artifact.artifact_classes.CustomerAgreementSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.artifact.artifact_classes.PaginatorConfig]


# ListReportsResponse

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.artifact.artifact_classes.ReportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.artifact.artifact_classes.ResponseMetadata'>
- **Required**: Yes


# ReportDetail

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


# ReportSummary

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


