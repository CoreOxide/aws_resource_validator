# support_classes

# AddAttachmentsToSetRequestRequestTypeDef

### attachments
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.support_classes.AttachmentTypeDef, aws_resource_validator.pydantic_models.support_classes.AttachmentOutputTypeDef]]
- **Required**: Yes

### attachmentSetId
- **Type**: typing.Optional[str]


# AddAttachmentsToSetResponseTypeDef

### attachmentSetId
- **Type**: <class 'str'>
- **Required**: Yes

### expiryTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddCommunicationToCaseRequestRequestTypeDef

### communicationBody
- **Type**: <class 'str'>
- **Required**: Yes

### caseId
- **Type**: typing.Optional[str]

### ccEmailAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### attachmentSetId
- **Type**: typing.Optional[str]


# AddCommunicationToCaseResponseTypeDef

### result
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachmentDetailsTypeDef

### attachmentId
- **Type**: typing.Optional[str]

### fileName
- **Type**: typing.Optional[str]


# AttachmentOutputTypeDef

### fileName
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[bytes]


# AttachmentTypeDef

### fileName
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseDetailsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.RecentCaseCommunicationsTypeDef]

### ccEmailAddresses
- **Type**: typing.Optional[typing.List[str]]

### language
- **Type**: typing.Optional[str]


# CategoryTypeDef

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# CommunicationTypeDef

### caseId
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]

### submittedBy
- **Type**: typing.Optional[str]

### timeCreated
- **Type**: typing.Optional[str]

### attachmentSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.AttachmentDetailsTypeDef]]


# CommunicationTypeOptionsTypeDef

### type
- **Type**: typing.Optional[str]

### supportedHours
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.SupportedHourTypeDef]]

### datesWithoutSupport
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.DateIntervalTypeDef]]


# CreateCaseRequestRequestTypeDef

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


# CreateCaseResponseTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DateIntervalTypeDef

### startDateTime
- **Type**: typing.Optional[str]

### endDateTime
- **Type**: typing.Optional[str]


# DescribeAttachmentRequestRequestTypeDef

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAttachmentResponseTypeDef

### attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.AttachmentOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCasesRequestDescribeCasesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.PaginatorConfigTypeDef]


# DescribeCasesRequestRequestTypeDef

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


# DescribeCasesResponseTypeDef

### cases
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.CaseDetailsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCommunicationsRequestDescribeCommunicationsPaginateTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeTime
- **Type**: typing.Optional[str]

### afterTime
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.PaginatorConfigTypeDef]


# DescribeCommunicationsRequestRequestTypeDef

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


# DescribeCommunicationsResponseTypeDef

### communications
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.CommunicationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCreateCaseOptionsRequestRequestTypeDef

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


# DescribeCreateCaseOptionsResponseTypeDef

### languageAvailability
- **Type**: <class 'str'>
- **Required**: Yes

### communicationTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.CommunicationTypeOptionsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServicesRequestRequestTypeDef

### serviceCodeList
- **Type**: typing.Optional[typing.Sequence[str]]

### language
- **Type**: typing.Optional[str]


# DescribeServicesResponseTypeDef

### services
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.ServiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSeverityLevelsRequestRequestTypeDef

### language
- **Type**: typing.Optional[str]


# DescribeSeverityLevelsResponseTypeDef

### severityLevels
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.SeverityLevelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSupportedLanguagesRequestRequestTypeDef

### issueType
- **Type**: <class 'str'>
- **Required**: Yes

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### categoryCode
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSupportedLanguagesResponseTypeDef

### supportedLanguages
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.SupportedLanguageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef

### checkIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef

### statuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckRefreshStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustedAdvisorCheckResultRequestRequestTypeDef

### checkId
- **Type**: <class 'str'>
- **Required**: Yes

### language
- **Type**: typing.Optional[str]


# DescribeTrustedAdvisorCheckResultResponseTypeDef

### result
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef

### checkIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTrustedAdvisorCheckSummariesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustedAdvisorChecksRequestRequestTypeDef

### language
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrustedAdvisorChecksResponseTypeDef

### checks
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RecentCaseCommunicationsTypeDef

### communications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.CommunicationTypeDef]]

### nextToken
- **Type**: typing.Optional[str]


# RefreshTrustedAdvisorCheckRequestRequestTypeDef

### checkId
- **Type**: <class 'str'>
- **Required**: Yes


# RefreshTrustedAdvisorCheckResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCheckRefreshStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolveCaseRequestRequestTypeDef

### caseId
- **Type**: typing.Optional[str]


# ResolveCaseResponseTypeDef

### initialCaseStatus
- **Type**: <class 'str'>
- **Required**: Yes

### finalCaseStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ServiceTypeDef

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.support_classes.CategoryTypeDef]]


# SeverityLevelTypeDef

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# SupportedHourTypeDef

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]


# SupportedLanguageTypeDef

### code
- **Type**: typing.Optional[str]

### language
- **Type**: typing.Optional[str]

### display
- **Type**: typing.Optional[str]


# TrustedAdvisorCategorySpecificSummaryTypeDef

### costOptimizing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCostOptimizingSummaryTypeDef]


# TrustedAdvisorCheckDescriptionTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### category
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.List[str]
- **Required**: Yes


# TrustedAdvisorCheckRefreshStatusTypeDef

### checkId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### millisUntilNextRefreshable
- **Type**: <class 'int'>
- **Required**: Yes


# TrustedAdvisorCheckResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorResourcesSummaryTypeDef'>
- **Required**: Yes

### categorySpecificSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCategorySpecificSummaryTypeDef'>
- **Required**: Yes

### flaggedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorResourceDetailTypeDef]
- **Required**: Yes


# TrustedAdvisorCheckSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorResourcesSummaryTypeDef'>
- **Required**: Yes

### categorySpecificSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.support_classes.TrustedAdvisorCategorySpecificSummaryTypeDef'>
- **Required**: Yes

### hasFlaggedResources
- **Type**: typing.Optional[bool]


# TrustedAdvisorCostOptimizingSummaryTypeDef

### estimatedMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes

### estimatedPercentMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes


# TrustedAdvisorResourceDetailTypeDef

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


# TrustedAdvisorResourcesSummaryTypeDef

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


