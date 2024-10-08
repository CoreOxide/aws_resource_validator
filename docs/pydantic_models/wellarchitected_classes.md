# Pydantic Models in wellarchitected_classes

# AccountJiraConfigurationInputTypeDef

### IssueManagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IssueManagementType
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### JiraProjectKey
- **Type**: typing.Optional[str]

### IntegrationStatus
- **Type**: typing.Optional[typing.Literal['NOT_CONFIGURED']]


# AccountJiraConfigurationOutputTypeDef

### IntegrationStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURED', 'NOT_CONFIGURED']]

### IssueManagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IssueManagementType
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### Subdomain
- **Type**: typing.Optional[str]

### JiraProjectKey
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# AdditionalResourcesTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['HELPFUL_RESOURCE', 'IMPROVEMENT_PLAN']]

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceContentTypeDef]]


# AnswerSummaryTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### PillarId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### Choices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceTypeDef]]

### SelectedChoices
- **Type**: typing.Optional[typing.List[str]]

### ChoiceAnswerSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceAnswerSummaryTypeDef]]

### IsApplicable
- **Type**: typing.Optional[bool]

### Risk
- **Type**: typing.Optional[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED']]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### QuestionType
- **Type**: typing.Optional[typing.Literal['NON_PRIORITIZED', 'PRIORITIZED']]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.JiraConfigurationTypeDef]


# AnswerTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### PillarId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### QuestionDescription
- **Type**: typing.Optional[str]

### ImprovementPlanUrl
- **Type**: typing.Optional[str]

### HelpfulResourceUrl
- **Type**: typing.Optional[str]

### HelpfulResourceDisplayText
- **Type**: typing.Optional[str]

### Choices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceTypeDef]]

### SelectedChoices
- **Type**: typing.Optional[typing.List[str]]

### ChoiceAnswers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceAnswerTypeDef]]

### IsApplicable
- **Type**: typing.Optional[bool]

### Risk
- **Type**: typing.Optional[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED']]

### Notes
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.JiraConfigurationTypeDef]


# AssociateLensesInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAliases
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociateProfilesInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BestPracticeTypeDef

### ChoiceId
- **Type**: typing.Optional[str]

### ChoiceTitle
- **Type**: typing.Optional[str]


# CheckDetailTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Provider
- **Type**: typing.Optional[typing.Literal['TRUSTED_ADVISOR']]

### LensArn
- **Type**: typing.Optional[str]

### PillarId
- **Type**: typing.Optional[str]

### QuestionId
- **Type**: typing.Optional[str]

### ChoiceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'FETCH_FAILED', 'NOT_AVAILABLE', 'OKAY', 'WARNING']]

### AccountId
- **Type**: typing.Optional[str]

### FlaggedResources
- **Type**: typing.Optional[int]

### Reason
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'ASSUME_ROLE_ERROR', 'PREMIUM_SUPPORT_REQUIRED', 'UNKNOWN_ERROR']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# CheckSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Provider
- **Type**: typing.Optional[typing.Literal['TRUSTED_ADVISOR']]

### Description
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### LensArn
- **Type**: typing.Optional[str]

### PillarId
- **Type**: typing.Optional[str]

### QuestionId
- **Type**: typing.Optional[str]

### ChoiceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'FETCH_FAILED', 'NOT_AVAILABLE', 'OKAY', 'WARNING']]

### AccountSummary
- **Type**: typing.Optional[typing.Dict[typing.Literal['ERROR', 'FETCH_FAILED', 'NOT_AVAILABLE', 'OKAY', 'WARNING'], int]]


# ChoiceAnswerSummaryTypeDef

### ChoiceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['NOT_APPLICABLE', 'SELECTED', 'UNSELECTED']]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# ChoiceAnswerTypeDef

### ChoiceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['NOT_APPLICABLE', 'SELECTED', 'UNSELECTED']]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### Notes
- **Type**: typing.Optional[str]


# ChoiceContentTypeDef

### DisplayText
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ChoiceImprovementPlanTypeDef

### ChoiceId
- **Type**: typing.Optional[str]

### DisplayText
- **Type**: typing.Optional[str]

### ImprovementPlanUrl
- **Type**: typing.Optional[str]


# ChoiceTypeDef

### ChoiceId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HelpfulResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceContentTypeDef]

### ImprovementPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceContentTypeDef]

### AdditionalResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.AdditionalResourcesTypeDef]]


# ChoiceUpdateTypeDef

### Status
- **Type**: typing.Literal['NOT_APPLICABLE', 'SELECTED', 'UNSELECTED']
- **Required**: Yes

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### Notes
- **Type**: typing.Optional[str]


# ConsolidatedReportMetricTypeDef

### MetricType
- **Type**: typing.Optional[typing.Literal['WORKLOAD']]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### WorkloadId
- **Type**: typing.Optional[str]

### WorkloadName
- **Type**: typing.Optional[str]

### WorkloadArn
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Lenses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensMetricTypeDef]]

### LensesAppliedCount
- **Type**: typing.Optional[int]


# CreateLensShareInputRequestTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWith
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateLensShareOutputTypeDef

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLensVersionInputRequestTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### IsMajorVersion
- **Type**: typing.Optional[bool]


# CreateLensVersionOutputTypeDef

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMilestoneInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMilestoneOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProfileInputRequestTypeDef

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileQuestions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileQuestionUpdateTypeDef]
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProfileOutputTypeDef

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProfileShareInputRequestTypeDef

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWith
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateProfileShareOutputTypeDef

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReviewTemplateInputRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Lenses
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Notes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateReviewTemplateOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTemplateShareInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWith
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTemplateShareOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkloadInputRequestTypeDef

### WorkloadName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Literal['PREPRODUCTION', 'PRODUCTION']
- **Required**: Yes

### Lenses
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AwsRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### NonAwsRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### PillarPriorities
- **Type**: typing.Optional[typing.Sequence[str]]

### ArchitecturalDesign
- **Type**: typing.Optional[str]

### ReviewOwner
- **Type**: typing.Optional[str]

### IndustryType
- **Type**: typing.Optional[str]

### Industry
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DiscoveryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadDiscoveryConfigTypeDef]

### Applications
- **Type**: typing.Optional[typing.Sequence[str]]

### ProfileArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ReviewTemplateArns
- **Type**: typing.Optional[typing.Sequence[str]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadJiraConfigurationInputTypeDef]


# CreateWorkloadOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkloadShareInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWith
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionType
- **Type**: typing.Literal['CONTRIBUTOR', 'READONLY']
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWorkloadShareOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLensInputRequestTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### LensStatus
- **Type**: typing.Literal['ALL', 'DRAFT', 'PUBLISHED']
- **Required**: Yes


# DeleteLensShareInputRequestTypeDef

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileInputRequestTypeDef

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileShareInputRequestTypeDef

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReviewTemplateInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateShareInputRequestTypeDef

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkloadInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkloadShareInputRequestTypeDef

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateLensesInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAliases
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociateProfilesInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportLensInputRequestTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensVersion
- **Type**: typing.Optional[str]


# ExportLensOutputTypeDef

### LensJSON
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAnswerInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: typing.Optional[int]


# GetAnswerOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### Answer
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.AnswerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConsolidatedReportInputRequestTypeDef

### Format
- **Type**: typing.Literal['JSON', 'PDF']
- **Required**: Yes

### IncludeSharedResources
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetConsolidatedReportOutputTypeDef

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ConsolidatedReportMetricTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Base64String
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGlobalSettingsOutputTypeDef

### OrganizationSharingStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DiscoveryIntegrationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### JiraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.AccountJiraConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLensInputRequestTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensVersion
- **Type**: typing.Optional[str]


# GetLensOutputTypeDef

### Lens
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.LensTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLensReviewInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: typing.Optional[int]


# GetLensReviewOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.LensReviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLensReviewReportInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: typing.Optional[int]


# GetLensReviewReportOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensReviewReport
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.LensReviewReportTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLensVersionDifferenceInputRequestTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### BaseLensVersion
- **Type**: typing.Optional[str]

### TargetLensVersion
- **Type**: typing.Optional[str]


# GetLensVersionDifferenceOutputTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaseLensVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLensVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestLensVersion
- **Type**: <class 'str'>
- **Required**: Yes

### VersionDifferences
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.VersionDifferencesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMilestoneInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetMilestoneOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### Milestone
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.MilestoneTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileInputRequestTypeDef

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileVersion
- **Type**: typing.Optional[str]


# GetProfileOutputTypeDef

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileTemplateOutputTypeDef

### ProfileTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReviewTemplateAnswerInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReviewTemplateAnswerOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### Answer
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateAnswerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReviewTemplateInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetReviewTemplateLensReviewInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes


# GetReviewTemplateLensReviewOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateLensReviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReviewTemplateOutputTypeDef

### ReviewTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkloadInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkloadOutputTypeDef

### Workload
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportLensInputRequestTypeDef

### JSONString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ImportLensOutputTypeDef

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'ERROR', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImprovementSummaryTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### PillarId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### Risk
- **Type**: typing.Optional[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED']]

### ImprovementPlanUrl
- **Type**: typing.Optional[str]

### ImprovementPlans
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceImprovementPlanTypeDef]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.JiraConfigurationTypeDef]


# JiraConfigurationTypeDef

### JiraIssueUrl
- **Type**: typing.Optional[str]

### LastSyncedTime
- **Type**: typing.Optional[datetime.datetime]


# JiraSelectedQuestionConfigurationTypeDef

### SelectedPillars
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.SelectedPillarTypeDef]]


# LensMetricTypeDef

### LensArn
- **Type**: typing.Optional[str]

### Pillars
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.PillarMetricTypeDef]]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# LensReviewReportTypeDef

### LensAlias
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### Base64String
- **Type**: typing.Optional[str]


# LensReviewSummaryTypeDef

### LensAlias
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### LensVersion
- **Type**: typing.Optional[str]

### LensName
- **Type**: typing.Optional[str]

### LensStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'DELETED', 'DEPRECATED', 'NOT_CURRENT', 'UNSHARED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### Profiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfileTypeDef]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# LensReviewTypeDef

### LensAlias
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### LensVersion
- **Type**: typing.Optional[str]

### LensName
- **Type**: typing.Optional[str]

### LensStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'DELETED', 'DEPRECATED', 'NOT_CURRENT', 'UNSHARED']]

### PillarReviewSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.PillarReviewSummaryTypeDef]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.JiraSelectedQuestionConfigurationTypeDef]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Notes
- **Type**: typing.Optional[str]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### NextToken
- **Type**: typing.Optional[str]

### Profiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfileTypeDef]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# LensShareSummaryTypeDef

### ShareId
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### StatusMessage
- **Type**: typing.Optional[str]


# LensSummaryTypeDef

### LensArn
- **Type**: typing.Optional[str]

### LensAlias
- **Type**: typing.Optional[str]

### LensName
- **Type**: typing.Optional[str]

### LensType
- **Type**: typing.Optional[typing.Literal['AWS_OFFICIAL', 'CUSTOM_SELF', 'CUSTOM_SHARED']]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### LensVersion
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### LensStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'DELETED', 'DEPRECATED', 'NOT_CURRENT', 'UNSHARED']]


# LensTypeDef

### LensArn
- **Type**: typing.Optional[str]

### LensVersion
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ShareInvitationId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# LensUpgradeSummaryTypeDef

### WorkloadId
- **Type**: typing.Optional[str]

### WorkloadName
- **Type**: typing.Optional[str]

### LensAlias
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### CurrentLensVersion
- **Type**: typing.Optional[str]

### LatestLensVersion
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]


# ListAnswersInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### PillarId
- **Type**: typing.Optional[str]

### MilestoneNumber
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### QuestionPriority
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIORITIZED']]


# ListAnswersOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnswerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.AnswerSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCheckDetailsInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### PillarId
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionId
- **Type**: <class 'str'>
- **Required**: Yes

### ChoiceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCheckDetailsOutputTypeDef

### CheckDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.CheckDetailTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCheckSummariesInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### PillarId
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionId
- **Type**: <class 'str'>
- **Required**: Yes

### ChoiceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCheckSummariesOutputTypeDef

### CheckSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.CheckSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLensReviewImprovementsInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### PillarId
- **Type**: typing.Optional[str]

### MilestoneNumber
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### QuestionPriority
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIORITIZED']]


# ListLensReviewImprovementsOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImprovementSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ImprovementSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLensReviewsInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLensReviewsOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensReviewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensReviewSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLensSharesInputRequestTypeDef

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWithPrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]


# ListLensSharesOutputTypeDef

### LensShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensShareSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLensesInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### LensType
- **Type**: typing.Optional[typing.Literal['AWS_OFFICIAL', 'CUSTOM_SELF', 'CUSTOM_SHARED']]

### LensStatus
- **Type**: typing.Optional[typing.Literal['ALL', 'DRAFT', 'PUBLISHED']]

### LensName
- **Type**: typing.Optional[str]


# ListLensesOutputTypeDef

### LensSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMilestonesInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMilestonesOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.MilestoneSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNotificationsInputRequestTypeDef

### WorkloadId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceArn
- **Type**: typing.Optional[str]


# ListNotificationsOutputTypeDef

### NotificationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.NotificationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfileNotificationsInputRequestTypeDef

### WorkloadId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfileNotificationsOutputTypeDef

### NotificationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileNotificationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfileSharesInputRequestTypeDef

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWithPrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]


# ListProfileSharesOutputTypeDef

### ProfileShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileShareSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfilesInputRequestTypeDef

### ProfileNamePrefix
- **Type**: typing.Optional[str]

### ProfileOwnerType
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfilesOutputTypeDef

### ProfileSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReviewTemplateAnswersInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### PillarId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReviewTemplateAnswersOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### AnswerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateAnswerSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReviewTemplatesInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReviewTemplatesOutputTypeDef

### ReviewTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListShareInvitationsInputRequestTypeDef

### WorkloadNamePrefix
- **Type**: typing.Optional[str]

### LensNamePrefix
- **Type**: typing.Optional[str]

### ShareResourceType
- **Type**: typing.Optional[typing.Literal['LENS', 'PROFILE', 'TEMPLATE', 'WORKLOAD']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ProfileNamePrefix
- **Type**: typing.Optional[str]

### TemplateNamePrefix
- **Type**: typing.Optional[str]


# ListShareInvitationsOutputTypeDef

### ShareInvitationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ShareInvitationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplateSharesInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWithPrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]


# ListTemplateSharesOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.TemplateShareSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkloadSharesInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWithPrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]


# ListWorkloadSharesOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadShareSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkloadsInputRequestTypeDef

### WorkloadNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkloadsOutputTypeDef

### WorkloadSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MilestoneSummaryTypeDef

### MilestoneNumber
- **Type**: typing.Optional[int]

### MilestoneName
- **Type**: typing.Optional[str]

### RecordedAt
- **Type**: typing.Optional[datetime.datetime]

### WorkloadSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadSummaryTypeDef]


# MilestoneTypeDef

### MilestoneNumber
- **Type**: typing.Optional[int]

### MilestoneName
- **Type**: typing.Optional[str]

### RecordedAt
- **Type**: typing.Optional[datetime.datetime]

### Workload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadTypeDef]


# NotificationSummaryTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['LENS_VERSION_DEPRECATED', 'LENS_VERSION_UPGRADED']]

### LensUpgradeSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.LensUpgradeSummaryTypeDef]


# PillarDifferenceTypeDef

### PillarId
- **Type**: typing.Optional[str]

### PillarName
- **Type**: typing.Optional[str]

### DifferenceStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'NEW', 'UPDATED']]

### QuestionDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.QuestionDifferenceTypeDef]]


# PillarMetricTypeDef

### PillarId
- **Type**: typing.Optional[str]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### Questions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.QuestionMetricTypeDef]]


# PillarReviewSummaryTypeDef

### PillarId
- **Type**: typing.Optional[str]

### PillarName
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# ProfileChoiceTypeDef

### ChoiceId
- **Type**: typing.Optional[str]

### ChoiceTitle
- **Type**: typing.Optional[str]

### ChoiceDescription
- **Type**: typing.Optional[str]


# ProfileNotificationSummaryTypeDef

### CurrentProfileVersion
- **Type**: typing.Optional[str]

### LatestProfileVersion
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['PROFILE_ANSWERS_UPDATED', 'PROFILE_DELETED']]

### ProfileArn
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]

### WorkloadId
- **Type**: typing.Optional[str]

### WorkloadName
- **Type**: typing.Optional[str]


# ProfileQuestionTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### QuestionDescription
- **Type**: typing.Optional[str]

### QuestionChoices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileChoiceTypeDef]]

### SelectedChoiceIds
- **Type**: typing.Optional[typing.List[str]]

### MinSelectedChoices
- **Type**: typing.Optional[int]

### MaxSelectedChoices
- **Type**: typing.Optional[int]


# ProfileQuestionUpdateTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### SelectedChoiceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ProfileShareSummaryTypeDef

### ShareId
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### StatusMessage
- **Type**: typing.Optional[str]


# ProfileSummaryTypeDef

### ProfileArn
- **Type**: typing.Optional[str]

### ProfileVersion
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]

### ProfileDescription
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ProfileTemplateChoiceTypeDef

### ChoiceId
- **Type**: typing.Optional[str]

### ChoiceTitle
- **Type**: typing.Optional[str]

### ChoiceDescription
- **Type**: typing.Optional[str]


# ProfileTemplateQuestionTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### QuestionDescription
- **Type**: typing.Optional[str]

### QuestionChoices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTemplateChoiceTypeDef]]

### MinSelectedChoices
- **Type**: typing.Optional[int]

### MaxSelectedChoices
- **Type**: typing.Optional[int]


# ProfileTemplateTypeDef

### TemplateName
- **Type**: typing.Optional[str]

### TemplateQuestions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTemplateQuestionTypeDef]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ProfileTypeDef

### ProfileArn
- **Type**: typing.Optional[str]

### ProfileVersion
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]

### ProfileDescription
- **Type**: typing.Optional[str]

### ProfileQuestions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileQuestionTypeDef]]

### Owner
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ShareInvitationId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# QuestionDifferenceTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### DifferenceStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'NEW', 'UPDATED']]


# QuestionMetricTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### Risk
- **Type**: typing.Optional[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED']]

### BestPractices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.BestPracticeTypeDef]]


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


# ReviewTemplateAnswerSummaryTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### PillarId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### Choices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceTypeDef]]

### SelectedChoices
- **Type**: typing.Optional[typing.List[str]]

### ChoiceAnswerSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceAnswerSummaryTypeDef]]

### IsApplicable
- **Type**: typing.Optional[bool]

### AnswerStatus
- **Type**: typing.Optional[typing.Literal['ANSWERED', 'UNANSWERED']]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### QuestionType
- **Type**: typing.Optional[typing.Literal['NON_PRIORITIZED', 'PRIORITIZED']]


# ReviewTemplateAnswerTypeDef

### QuestionId
- **Type**: typing.Optional[str]

### PillarId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### QuestionDescription
- **Type**: typing.Optional[str]

### ImprovementPlanUrl
- **Type**: typing.Optional[str]

### HelpfulResourceUrl
- **Type**: typing.Optional[str]

### HelpfulResourceDisplayText
- **Type**: typing.Optional[str]

### Choices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceTypeDef]]

### SelectedChoices
- **Type**: typing.Optional[typing.List[str]]

### ChoiceAnswers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceAnswerTypeDef]]

### IsApplicable
- **Type**: typing.Optional[bool]

### AnswerStatus
- **Type**: typing.Optional[typing.Literal['ANSWERED', 'UNANSWERED']]

### Notes
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# ReviewTemplateLensReviewTypeDef

### LensAlias
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### LensVersion
- **Type**: typing.Optional[str]

### LensName
- **Type**: typing.Optional[str]

### LensStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'DELETED', 'DEPRECATED', 'NOT_CURRENT', 'UNSHARED']]

### PillarReviewSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplatePillarReviewSummaryTypeDef]]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Notes
- **Type**: typing.Optional[str]

### QuestionCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWERED', 'UNANSWERED'], int]]

### NextToken
- **Type**: typing.Optional[str]


# ReviewTemplatePillarReviewSummaryTypeDef

### PillarId
- **Type**: typing.Optional[str]

### PillarName
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### QuestionCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWERED', 'UNANSWERED'], int]]


# ReviewTemplateSummaryTypeDef

### Description
- **Type**: typing.Optional[str]

### Lenses
- **Type**: typing.Optional[typing.List[str]]

### Owner
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### TemplateArn
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'LENS_NOT_CURRENT']]


# ReviewTemplateTypeDef

### Description
- **Type**: typing.Optional[str]

### Lenses
- **Type**: typing.Optional[typing.List[str]]

### Notes
- **Type**: typing.Optional[str]

### QuestionCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWERED', 'UNANSWERED'], int]]

### Owner
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### TemplateArn
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'LENS_NOT_CURRENT']]

### ShareInvitationId
- **Type**: typing.Optional[str]


# SelectedPillarTypeDef

### PillarId
- **Type**: typing.Optional[str]

### SelectedQuestionIds
- **Type**: typing.Optional[typing.List[str]]


# ShareInvitationSummaryTypeDef

### ShareInvitationId
- **Type**: typing.Optional[str]

### SharedBy
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### PermissionType
- **Type**: typing.Optional[typing.Literal['CONTRIBUTOR', 'READONLY']]

### ShareResourceType
- **Type**: typing.Optional[typing.Literal['LENS', 'PROFILE', 'TEMPLATE', 'WORKLOAD']]

### WorkloadName
- **Type**: typing.Optional[str]

### WorkloadId
- **Type**: typing.Optional[str]

### LensName
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]

### ProfileArn
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]


# ShareInvitationTypeDef

### ShareInvitationId
- **Type**: typing.Optional[str]

### ShareResourceType
- **Type**: typing.Optional[typing.Literal['LENS', 'PROFILE', 'TEMPLATE', 'WORKLOAD']]

### WorkloadId
- **Type**: typing.Optional[str]

### LensAlias
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### ProfileArn
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]


# TagResourceInputRequestTypeDef

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateShareSummaryTypeDef

### ShareId
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### StatusMessage
- **Type**: typing.Optional[str]


# UntagResourceInputRequestTypeDef

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnswerInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectedChoices
- **Type**: typing.Optional[typing.Sequence[str]]

### ChoiceUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceUpdateTypeDef]]

### Notes
- **Type**: typing.Optional[str]

### IsApplicable
- **Type**: typing.Optional[bool]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# UpdateAnswerOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### Answer
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.AnswerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlobalSettingsInputRequestTypeDef

### OrganizationSharingStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DiscoveryIntegrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.AccountJiraConfigurationInputTypeDef]


# UpdateIntegrationInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### IntegratingService
- **Type**: typing.Literal['JIRA']
- **Required**: Yes


# UpdateLensReviewInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensNotes
- **Type**: typing.Optional[str]

### PillarNotes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.JiraSelectedQuestionConfigurationTypeDef]


# UpdateLensReviewOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.LensReviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProfileInputRequestTypeDef

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileDescription
- **Type**: typing.Optional[str]

### ProfileQuestions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileQuestionUpdateTypeDef]]


# UpdateProfileOutputTypeDef

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReviewTemplateAnswerInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectedChoices
- **Type**: typing.Optional[typing.Sequence[str]]

### ChoiceUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceUpdateTypeDef]]

### Notes
- **Type**: typing.Optional[str]

### IsApplicable
- **Type**: typing.Optional[bool]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# UpdateReviewTemplateAnswerOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### Answer
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateAnswerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReviewTemplateInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### LensesToAssociate
- **Type**: typing.Optional[typing.Sequence[str]]

### LensesToDisassociate
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateReviewTemplateLensReviewInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensNotes
- **Type**: typing.Optional[str]

### PillarNotes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateReviewTemplateLensReviewOutputTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateLensReviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReviewTemplateOutputTypeDef

### ReviewTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateShareInvitationInputRequestTypeDef

### ShareInvitationId
- **Type**: <class 'str'>
- **Required**: Yes

### ShareInvitationAction
- **Type**: typing.Literal['ACCEPT', 'REJECT']
- **Required**: Yes


# UpdateShareInvitationOutputTypeDef

### ShareInvitation
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ShareInvitationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkloadInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Literal['PREPRODUCTION', 'PRODUCTION']]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AwsRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### NonAwsRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### PillarPriorities
- **Type**: typing.Optional[typing.Sequence[str]]

### ArchitecturalDesign
- **Type**: typing.Optional[str]

### ReviewOwner
- **Type**: typing.Optional[str]

### IsReviewOwnerUpdateAcknowledged
- **Type**: typing.Optional[bool]

### IndustryType
- **Type**: typing.Optional[str]

### Industry
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### ImprovementStatus
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'IN_PROGRESS', 'NOT_APPLICABLE', 'NOT_STARTED', 'RISK_ACKNOWLEDGED']]

### DiscoveryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadDiscoveryConfigTypeDef]

### Applications
- **Type**: typing.Optional[typing.Sequence[str]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadJiraConfigurationInputTypeDef]


# UpdateWorkloadOutputTypeDef

### Workload
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkloadShareInputRequestTypeDef

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionType
- **Type**: typing.Literal['CONTRIBUTOR', 'READONLY']
- **Required**: Yes


# UpdateWorkloadShareOutputTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadShare
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadShareTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpgradeLensReviewInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpgradeProfileVersionInputRequestTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpgradeReviewTemplateLensReviewInputRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# VersionDifferencesTypeDef

### PillarDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.PillarDifferenceTypeDef]]


# WorkloadDiscoveryConfigTypeDef

### TrustedAdvisorIntegrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WorkloadResourceDefinition
- **Type**: typing.Optional[typing.Sequence[typing.Literal['APP_REGISTRY', 'WORKLOAD_METADATA']]]


# WorkloadJiraConfigurationInputTypeDef

### IssueManagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'INHERIT']]

### IssueManagementType
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### JiraProjectKey
- **Type**: typing.Optional[str]


# WorkloadJiraConfigurationOutputTypeDef

### IssueManagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'INHERIT']]

### IssueManagementType
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### JiraProjectKey
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# WorkloadProfileTypeDef

### ProfileArn
- **Type**: typing.Optional[str]

### ProfileVersion
- **Type**: typing.Optional[str]


# WorkloadShareSummaryTypeDef

### ShareId
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### PermissionType
- **Type**: typing.Optional[typing.Literal['CONTRIBUTOR', 'READONLY']]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### StatusMessage
- **Type**: typing.Optional[str]


# WorkloadShareTypeDef

### ShareId
- **Type**: typing.Optional[str]

### SharedBy
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### PermissionType
- **Type**: typing.Optional[typing.Literal['CONTRIBUTOR', 'READONLY']]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### WorkloadName
- **Type**: typing.Optional[str]

### WorkloadId
- **Type**: typing.Optional[str]


# WorkloadSummaryTypeDef

### WorkloadId
- **Type**: typing.Optional[str]

### WorkloadArn
- **Type**: typing.Optional[str]

### WorkloadName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Lenses
- **Type**: typing.Optional[typing.List[str]]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### ImprovementStatus
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'IN_PROGRESS', 'NOT_APPLICABLE', 'NOT_STARTED', 'RISK_ACKNOWLEDGED']]

### Profiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfileTypeDef]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# WorkloadTypeDef

### WorkloadId
- **Type**: typing.Optional[str]

### WorkloadArn
- **Type**: typing.Optional[str]

### WorkloadName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Literal['PREPRODUCTION', 'PRODUCTION']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### AwsRegions
- **Type**: typing.Optional[typing.List[str]]

### NonAwsRegions
- **Type**: typing.Optional[typing.List[str]]

### ArchitecturalDesign
- **Type**: typing.Optional[str]

### ReviewOwner
- **Type**: typing.Optional[str]

### ReviewRestrictionDate
- **Type**: typing.Optional[datetime.datetime]

### IsReviewOwnerUpdateAcknowledged
- **Type**: typing.Optional[bool]

### IndustryType
- **Type**: typing.Optional[str]

### Industry
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### ImprovementStatus
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'IN_PROGRESS', 'NOT_APPLICABLE', 'NOT_STARTED', 'RISK_ACKNOWLEDGED']]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### PillarPriorities
- **Type**: typing.Optional[typing.List[str]]

### Lenses
- **Type**: typing.Optional[typing.List[str]]

### Owner
- **Type**: typing.Optional[str]

### ShareInvitationId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### DiscoveryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadDiscoveryConfigTypeDef]

### Applications
- **Type**: typing.Optional[typing.List[str]]

### Profiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfileTypeDef]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadJiraConfigurationOutputTypeDef]


