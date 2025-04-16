# Codeguru Security Classes

# AccountFindingsMetric

### closedFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverity]

### date
- **Type**: typing.Optional[datetime.datetime]

### meanTimeToClose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverity]

### newFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverity]

### openFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverity]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetFindingsError

### errorCode
- **Type**: typing.Literal['DUPLICATE_IDENTIFIER', 'INTERNAL_ERROR', 'INVALID_FINDING_ID', 'INVALID_SCAN_NAME', 'ITEM_DOES_NOT_EXIST']
- **Required**: Yes

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetFindingsRequest

### findingIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingIdentifier]
- **Required**: Yes


# BatchGetFindingsResponse

### failedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.BatchGetFindingsError]
- **Required**: Yes

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.Finding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


# CategoryWithFindingNum

### categoryName
- **Type**: typing.Optional[str]

### findingNumber
- **Type**: typing.Optional[int]


# CodeLine

### content
- **Type**: typing.Optional[str]

### number
- **Type**: typing.Optional[int]


# CreateScanRequest

### resourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResourceId'>
- **Required**: Yes

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### analysisType
- **Type**: typing.Optional[typing.Literal['All', 'Security']]

### clientToken
- **Type**: typing.Optional[str]

### scanType
- **Type**: typing.Optional[typing.Literal['Express', 'Standard']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateScanResponse

### resourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResourceId'>
- **Required**: Yes

### runId
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### scanNameArn
- **Type**: <class 'str'>
- **Required**: Yes

### scanState
- **Type**: typing.Literal['Failed', 'InProgress', 'Successful']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUploadUrlRequest

### scanName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateUploadUrlResponse

### codeArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### requestHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### s3Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfig

### kmsKeyArn
- **Type**: typing.Optional[str]


# FilePath

### codeSnippet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.CodeLine]]

### endLine
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### startLine
- **Type**: typing.Optional[int]


# Finding

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingIdentifier

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: <class 'str'>
- **Required**: Yes


# FindingMetricsValuePerSeverity

### critical
- **Type**: typing.Optional[float]

### high
- **Type**: typing.Optional[float]

### info
- **Type**: typing.Optional[float]

### low
- **Type**: typing.Optional[float]

### medium
- **Type**: typing.Optional[float]


# GetAccountConfigurationResponse

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.EncryptionConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsRequest

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['All', 'Closed', 'Open']]


# GetFindingsRequestPaginate

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['All', 'Closed', 'Open']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.PaginatorConfig]


# GetFindingsResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.Finding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetMetricsSummaryRequest

### date
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.Timestamp'>
- **Required**: Yes


# GetMetricsSummaryResponse

### metricsSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.MetricsSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


# GetScanRequest

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]


# GetScanResponse

### analysisType
- **Type**: typing.Literal['All', 'Security']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### numberOfRevisions
- **Type**: <class 'int'>
- **Required**: Yes

### runId
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### scanNameArn
- **Type**: <class 'str'>
- **Required**: Yes

### scanState
- **Type**: typing.Literal['Failed', 'InProgress', 'Successful']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


# ListFindingsMetricsRequest

### endDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.Timestamp'>
- **Required**: Yes

### startDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.Timestamp'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsMetricsRequestPaginate

### endDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.Timestamp'>
- **Required**: Yes

### startDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.Timestamp'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.PaginatorConfig]


# ListFindingsMetricsResponse

### findingsMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.AccountFindingsMetric]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScansRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListScansRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.PaginatorConfig]


# ListScansResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.ScanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


# MetricsSummary

### categoriesWithMostFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.CategoryWithFindingNum]]

### date
- **Type**: typing.Optional[datetime.datetime]

### openFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverity]

### scansWithMostOpenCriticalFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.ScanNameWithFindingNum]]

### scansWithMostOpenFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.ScanNameWithFindingNum]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Recommendation

### text
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# Remediation

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.Recommendation]

### suggestedFixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.SuggestedFix]]


# ResourceId

### codeArtifactId
- **Type**: typing.Optional[str]


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


# ScanNameWithFindingNum

### findingNumber
- **Type**: typing.Optional[int]

### scanName
- **Type**: typing.Optional[str]


# ScanSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### runId
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### scanState
- **Type**: typing.Literal['Failed', 'InProgress', 'Successful']
- **Required**: Yes

### scanNameArn
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# SuggestedFix

### code
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountConfigurationRequest

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.EncryptionConfig'>
- **Required**: Yes


# UpdateAccountConfigurationResponse

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.EncryptionConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadata'>
- **Required**: Yes


