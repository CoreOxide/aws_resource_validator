# Support Classes

# AddAttachmentsToSetRequest

### attachments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.support_classes.AttachmentUnion]
- **Required**: Yes

### attachmentSetId
- **Type**: typing.Optional[str]


# AddAttachmentsToSetResponse

### attachmentSetId
- **Type**: <class 'str'>
- **Required**: Yes

### expiryTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# AddCommunicationToCaseRequest

### communicationBody
- **Type**: <class 'str'>
- **Required**: Yes

### caseId
- **Type**: typing.Optional[str]

### ccEmailAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### attachmentSetId
- **Type**: typing.Optional[str]


# AddCommunicationToCaseResponse

### result
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# Attachment

### fileName
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.Blob]


# AttachmentDetails

### attachmentId
- **Type**: typing.Optional[str]

### fileName
- **Type**: typing.Optional[str]


# AttachmentOutput

### fileName
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[bytes]


# AttachmentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseDetails

### caseId
- **Type**: typing.Optional[str]

### displayId
- **Type**: typing.Optional[str]

### subject
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### serviceCode
- **Type**: typing.Optional[str]

### categoryCode
- **Type**: typing.Optional[str]

### severityCode
- **Type**: typing.Optional[str]

### submittedBy
- **Type**: typing.Optional[str]

### timeCreated
- **Type**: typing.Optional[str]

### recentCommunications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.RecentCaseCommunications]

### ccEmailAddresses
- **Type**: typing.Optional[typing.List[str]]

### language
- **Type**: typing.Optional[str]


# Category

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# Communication

### caseId
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]

### submittedBy
- **Type**: typing.Optional[str]

### timeCreated
- **Type**: typing.Optional[str]

### attachmentSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.AttachmentDetails]]


# CommunicationTypeOptions

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCaseRequest

### subject
- **Type**: <class 'str'>
- **Required**: Yes

### communicationBody
- **Type**: <class 'str'>
- **Required**: Yes

### serviceCode
- **Type**: typing.Optional[str]

### severityCode
- **Type**: typing.Optional[str]

### categoryCode
- **Type**: typing.Optional[str]

### ccEmailAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### language
- **Type**: typing.Optional[str]

### issueType
- **Type**: typing.Optional[str]

### attachmentSetId
- **Type**: typing.Optional[str]


# CreateCaseResponse

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DateInterval

### startDateTime
- **Type**: typing.Optional[str]

### endDateTime
- **Type**: typing.Optional[str]


# DescribeAttachmentRequest

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAttachmentResponse

### attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.AttachmentOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCasesRequest

### caseIdList
- **Type**: typing.Optional[typing.Sequence[str]]

### displayId
- **Type**: typing.Optional[str]

### afterTime
- **Type**: typing.Optional[str]

### beforeTime
- **Type**: typing.Optional[str]

### includeResolvedCases
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### language
- **Type**: typing.Optional[str]

### includeCommunications
- **Type**: typing.Optional[bool]


# DescribeCasesRequestPaginate

### caseIdList
- **Type**: typing.Optional[typing.Sequence[str]]

### displayId
- **Type**: typing.Optional[str]

### afterTime
- **Type**: typing.Optional[str]

### beforeTime
- **Type**: typing.Optional[str]

### includeResolvedCases
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### includeCommunications
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.PaginatorConfig]


# DescribeCasesResponse

### cases
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.CaseDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeCommunicationsRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeTime
- **Type**: typing.Optional[str]

### afterTime
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeCommunicationsRequestPaginate

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeTime
- **Type**: typing.Optional[str]

### afterTime
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.PaginatorConfig]


# DescribeCommunicationsResponse

### communications
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.Communication]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeCreateCaseOptionsRequest

### issueType
- **Type**: <class 'str'>
- **Required**: Yes

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### language
- **Type**: <class 'str'>
- **Required**: Yes

### categoryCode
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCreateCaseOptionsResponse

### languageAvailability
- **Type**: <class 'str'>
- **Required**: Yes

### communicationTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.CommunicationTypeOptions]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServicesRequest

### serviceCodeList
- **Type**: typing.Optional[typing.Sequence[str]]

### language
- **Type**: typing.Optional[str]


# DescribeServicesResponse

### services
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.Service]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSeverityLevelsRequest

### language
- **Type**: typing.Optional[str]


# DescribeSeverityLevelsResponse

### severityLevels
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.SeverityLevel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSupportedLanguagesRequest

### issueType
- **Type**: <class 'str'>
- **Required**: Yes

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### categoryCode
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSupportedLanguagesResponse

### supportedLanguages
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.SupportedLanguage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustedAdvisorCheckRefreshStatusesRequest

### checkIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTrustedAdvisorCheckRefreshStatusesResponse

### statuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckRefreshStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustedAdvisorCheckResultRequest

### checkId
- **Type**: <class 'str'>
- **Required**: Yes

### language
- **Type**: typing.Optional[str]


# DescribeTrustedAdvisorCheckResultResponse

### result
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustedAdvisorCheckSummariesRequest

### checkIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTrustedAdvisorCheckSummariesResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustedAdvisorChecksRequest

### language
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrustedAdvisorChecksResponse

### checks
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RecentCaseCommunications

### communications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.Communication]]

### nextToken
- **Type**: typing.Optional[str]


# RefreshTrustedAdvisorCheckRequest

### checkId
- **Type**: <class 'str'>
- **Required**: Yes


# RefreshTrustedAdvisorCheckResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckRefreshStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


# ResolveCaseRequest

### caseId
- **Type**: typing.Optional[str]


# ResolveCaseResponse

### initialCaseStatus
- **Type**: <class 'str'>
- **Required**: Yes

### finalCaseStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadata'>
- **Required**: Yes


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


# Service

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.Category]]


# SeverityLevel

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# SupportedHour

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]


# SupportedLanguage

### code
- **Type**: typing.Optional[str]

### language
- **Type**: typing.Optional[str]

### display
- **Type**: typing.Optional[str]


# TrustedAdvisorCategorySpecificSummary

### costOptimizing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCostOptimizingSummary]


# TrustedAdvisorCheckDescription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrustedAdvisorCheckRefreshStatus

### checkId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### millisUntilNextRefreshable
- **Type**: <class 'int'>
- **Required**: Yes


# TrustedAdvisorCheckResult

### checkId
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorResourcesSummary'>
- **Required**: Yes

### categorySpecificSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCategorySpecificSummary'>
- **Required**: Yes

### flaggedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorResourceDetail]
- **Required**: Yes


# TrustedAdvisorCheckSummary

### checkId
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorResourcesSummary'>
- **Required**: Yes

### categorySpecificSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCategorySpecificSummary'>
- **Required**: Yes

### hasFlaggedResources
- **Type**: typing.Optional[bool]


# TrustedAdvisorCostOptimizingSummary

### estimatedMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes

### estimatedPercentMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes


# TrustedAdvisorResourceDetail

### status
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.List[str]
- **Required**: Yes

### region
- **Type**: typing.Optional[str]

### isSuppressed
- **Type**: typing.Optional[bool]


# TrustedAdvisorResourcesSummary

### resourcesProcessed
- **Type**: <class 'int'>
- **Required**: Yes

### resourcesFlagged
- **Type**: <class 'int'>
- **Required**: Yes

### resourcesIgnored
- **Type**: <class 'int'>
- **Required**: Yes

### resourcesSuppressed
- **Type**: <class 'int'>
- **Required**: Yes


