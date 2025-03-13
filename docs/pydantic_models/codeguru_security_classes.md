# Codeguru Security Classes

# AccountFindingsMetricTypeDef

### closedFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverityTypeDef]

### date
- **Type**: typing.Optional[datetime.datetime]

### meanTimeToClose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverityTypeDef]

### newFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverityTypeDef]

### openFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverityTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetFindingsErrorTypeDef

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


# BatchGetFindingsRequestTypeDef

### findingIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingIdentifierTypeDef]
- **Required**: Yes


# BatchGetFindingsResponseTypeDef

### failedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.BatchGetFindingsErrorTypeDef]
- **Required**: Yes

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CategoryWithFindingNumTypeDef

### categoryName
- **Type**: typing.Optional[str]

### findingNumber
- **Type**: typing.Optional[int]


# CodeLineTypeDef

### content
- **Type**: typing.Optional[str]

### number
- **Type**: typing.Optional[int]


# CreateScanRequestTypeDef

### resourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResourceIdTypeDef'>
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


# CreateScanResponseTypeDef

### resourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResourceIdTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUploadUrlRequestTypeDef

### scanName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateUploadUrlResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigTypeDef

### kmsKeyArn
- **Type**: typing.Optional[str]


# FilePathTypeDef

### codeSnippet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.CodeLineTypeDef]]

### endLine
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### startLine
- **Type**: typing.Optional[int]


# FindingIdentifierTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: <class 'str'>
- **Required**: Yes


# FindingMetricsValuePerSeverityTypeDef

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


# FindingTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccountConfigurationResponseTypeDef

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsRequestPaginateTypeDef

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['All', 'Closed', 'Open']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.PaginatorConfigTypeDef]


# GetFindingsRequestTypeDef

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['All', 'Closed', 'Open']]


# GetFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetMetricsSummaryRequestTypeDef

### date
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.TimestampTypeDef'>
- **Required**: Yes


# GetMetricsSummaryResponseTypeDef

### metricsSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.MetricsSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetScanRequestTypeDef

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]


# GetScanResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsMetricsRequestPaginateTypeDef

### endDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.TimestampTypeDef'>
- **Required**: Yes

### startDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.TimestampTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.PaginatorConfigTypeDef]


# ListFindingsMetricsRequestTypeDef

### endDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.TimestampTypeDef'>
- **Required**: Yes

### startDate
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.TimestampTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsMetricsResponseTypeDef

### findingsMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.AccountFindingsMetricTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScansRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.PaginatorConfigTypeDef]


# ListScansRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListScansResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.ScanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricsSummaryTypeDef

### categoriesWithMostFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.CategoryWithFindingNumTypeDef]]

### date
- **Type**: typing.Optional[datetime.datetime]

### openFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.FindingMetricsValuePerSeverityTypeDef]

### scansWithMostOpenCriticalFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.ScanNameWithFindingNumTypeDef]]

### scansWithMostOpenFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.ScanNameWithFindingNumTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RecommendationTypeDef

### text
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# RemediationTypeDef

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_security_classes.RecommendationTypeDef]

### suggestedFixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguru_security_classes.SuggestedFixTypeDef]]


# ResourceIdTypeDef

### codeArtifactId
- **Type**: typing.Optional[str]


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


# ScanNameWithFindingNumTypeDef

### findingNumber
- **Type**: typing.Optional[int]

### scanName
- **Type**: typing.Optional[str]


# ScanSummaryTypeDef

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


# SuggestedFixTypeDef

### code
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountConfigurationRequestTypeDef

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.EncryptionConfigTypeDef'>
- **Required**: Yes


# UpdateAccountConfigurationResponseTypeDef

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_security_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


