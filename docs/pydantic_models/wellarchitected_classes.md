# Wellarchitected Classes

# AccountJiraConfigurationInput

### IssueManagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IssueManagementType
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### JiraProjectKey
- **Type**: typing.Optional[str]

### IntegrationStatus
- **Type**: typing.Optional[typing.Literal['NOT_CONFIGURED']]


# AccountJiraConfigurationOutput

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


# AdditionalResources

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Answer

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.Choice]]

### SelectedChoices
- **Type**: typing.Optional[typing.List[str]]

### ChoiceAnswers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceAnswer]]

### IsApplicable
- **Type**: typing.Optional[bool]

### Risk
- **Type**: typing.Optional[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED']]

### Notes
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### JiraConfiguration
- **Type**: <class 'NoneType'>


# AnswerSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateLensesInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAliases
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociateProfilesInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BestPractice

### ChoiceId
- **Type**: typing.Optional[str]

### ChoiceTitle
- **Type**: typing.Optional[str]


# CheckDetail

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


# CheckSummary

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


# Choice

### ChoiceId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HelpfulResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceContent]

### ImprovementPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceContent]

### AdditionalResources
- **Type**: typing.Optional[typing.List[NoneType]]


# ChoiceAnswer

### ChoiceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['NOT_APPLICABLE', 'SELECTED', 'UNSELECTED']]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### Notes
- **Type**: typing.Optional[str]


# ChoiceAnswerSummary

### ChoiceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['NOT_APPLICABLE', 'SELECTED', 'UNSELECTED']]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# ChoiceContent

### DisplayText
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ChoiceImprovementPlan

### ChoiceId
- **Type**: typing.Optional[str]

### DisplayText
- **Type**: typing.Optional[str]

### ImprovementPlanUrl
- **Type**: typing.Optional[str]


# ChoiceUpdate

### Status
- **Type**: typing.Literal['NOT_APPLICABLE', 'SELECTED', 'UNSELECTED']
- **Required**: Yes

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]

### Notes
- **Type**: typing.Optional[str]


# ConsolidatedReportMetric

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensMetric]]

### LensesAppliedCount
- **Type**: typing.Optional[int]


# CreateLensShareInput

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWith
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateLensShareOutput

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLensVersionInput

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


# CreateLensVersionOutput

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMilestoneInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMilestoneOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfileInput

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileQuestions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileQuestionUpdate]
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProfileOutput

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfileShareInput

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWith
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateProfileShareOutput

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReviewTemplateInput

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


# CreateReviewTemplateOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTemplateShareInput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### SharedWith
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTemplateShareOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkloadInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadDiscoveryConfigUnion]

### Applications
- **Type**: typing.Optional[typing.Sequence[str]]

### ProfileArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ReviewTemplateArns
- **Type**: typing.Optional[typing.Sequence[str]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadJiraConfigurationInput]


# CreateWorkloadOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkloadShareInput

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


# CreateWorkloadShareOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLensInput

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### LensStatus
- **Type**: typing.Literal['ALL', 'DRAFT', 'PUBLISHED']
- **Required**: Yes


# DeleteLensShareInput

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileInput

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileShareInput

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReviewTemplateInput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateShareInput

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkloadInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkloadShareInput

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateLensesInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAliases
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociateProfilesInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# ExportLensInput

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensVersion
- **Type**: typing.Optional[str]


# ExportLensOutput

### LensJSON
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetAnswerInput

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


# GetAnswerOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Answer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetConsolidatedReportInput

### Format
- **Type**: typing.Literal['JSON', 'PDF']
- **Required**: Yes

### IncludeSharedResources
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetConsolidatedReportOutput

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ConsolidatedReportMetric]
- **Required**: Yes

### Base64String
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetGlobalSettingsOutput

### OrganizationSharingStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DiscoveryIntegrationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### JiraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.AccountJiraConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetLensInput

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### LensVersion
- **Type**: typing.Optional[str]


# GetLensOutput

### Lens
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Lens'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetLensReviewInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: typing.Optional[int]


# GetLensReviewOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.LensReview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetLensReviewReportInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: typing.Optional[int]


# GetLensReviewReportOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensReviewReport
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.LensReviewReport'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetLensVersionDifferenceInput

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### BaseLensVersion
- **Type**: typing.Optional[str]

### TargetLensVersion
- **Type**: typing.Optional[str]


# GetLensVersionDifferenceOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.VersionDifferences'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetMilestoneInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetMilestoneOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### Milestone
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Milestone'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileInput

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileVersion
- **Type**: typing.Optional[str]


# GetProfileOutput

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Profile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileTemplateOutput

### ProfileTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetReviewTemplateAnswerInput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReviewTemplateAnswerOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### Answer
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateAnswer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetReviewTemplateInput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetReviewTemplateLensReviewInput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes


# GetReviewTemplateLensReviewOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateLensReview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetReviewTemplateOutput

### ReviewTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkloadInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkloadOutput

### Workload
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Workload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# ImportLensInput

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


# ImportLensOutput

### LensArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'ERROR', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# ImprovementSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceImprovementPlan]]

### JiraConfiguration
- **Type**: <class 'NoneType'>


# JiraConfiguration

### JiraIssueUrl
- **Type**: typing.Optional[str]

### LastSyncedTime
- **Type**: typing.Optional[datetime.datetime]


# JiraSelectedQuestionConfiguration

### SelectedPillars
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wellarchitected_classes.SelectedPillar]]


# JiraSelectedQuestionConfigurationOutput

### SelectedPillars
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.SelectedPillarOutput]]


# JiraSelectedQuestionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Lens

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


# LensMetric

### LensArn
- **Type**: typing.Optional[str]

### Pillars
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.PillarMetric]]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# LensReview

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.PillarReviewSummary]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.JiraSelectedQuestionConfigurationOutput]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Notes
- **Type**: typing.Optional[str]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### NextToken
- **Type**: typing.Optional[str]

### Profiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfile]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# LensReviewReport

### LensAlias
- **Type**: typing.Optional[str]

### LensArn
- **Type**: typing.Optional[str]

### Base64String
- **Type**: typing.Optional[str]


# LensReviewSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfile]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


# LensShareSummary

### ShareId
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### StatusMessage
- **Type**: typing.Optional[str]


# LensSummary

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


# LensUpgradeSummary

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


# ListAnswersInput

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


# ListAnswersOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.AnswerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCheckDetailsInput

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


# ListCheckDetailsOutput

### CheckDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.CheckDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCheckSummariesInput

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


# ListCheckSummariesOutput

### CheckSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.CheckSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLensReviewImprovementsInput

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


# ListLensReviewImprovementsOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ImprovementSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLensReviewsInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLensReviewsOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LensReviewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensReviewSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLensSharesInput

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


# ListLensSharesOutput

### LensShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensShareSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLensesInput

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


# ListLensesOutput

### LensSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.LensSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMilestonesInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMilestonesOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### MilestoneSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.MilestoneSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationsInput

### WorkloadId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceArn
- **Type**: typing.Optional[str]


# ListNotificationsOutput

### NotificationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.NotificationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileNotificationsInput

### WorkloadId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfileNotificationsOutput

### NotificationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileNotificationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileSharesInput

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


# ListProfileSharesOutput

### ProfileShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileShareSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfilesInput

### ProfileNamePrefix
- **Type**: typing.Optional[str]

### ProfileOwnerType
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfilesOutput

### ProfileSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReviewTemplateAnswersInput

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


# ListReviewTemplateAnswersOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### AnswerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateAnswerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReviewTemplatesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReviewTemplatesOutput

### ReviewTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListShareInvitationsInput

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


# ListShareInvitationsOutput

### ShareInvitationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ShareInvitationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplateSharesInput

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


# ListTemplateSharesOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.TemplateShareSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkloadSharesInput

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


# ListWorkloadSharesOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadShareSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadShareSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkloadsInput

### WorkloadNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkloadsOutput

### WorkloadSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Milestone

### MilestoneNumber
- **Type**: typing.Optional[int]

### MilestoneName
- **Type**: typing.Optional[str]

### RecordedAt
- **Type**: typing.Optional[datetime.datetime]

### Workload
- **Type**: <class 'NoneType'>


# MilestoneSummary

### MilestoneNumber
- **Type**: typing.Optional[int]

### MilestoneName
- **Type**: typing.Optional[str]

### RecordedAt
- **Type**: typing.Optional[datetime.datetime]

### WorkloadSummary
- **Type**: <class 'NoneType'>


# NotificationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PillarDifference

### PillarId
- **Type**: typing.Optional[str]

### PillarName
- **Type**: typing.Optional[str]

### DifferenceStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'NEW', 'UPDATED']]

### QuestionDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.QuestionDifference]]


# PillarMetric

### PillarId
- **Type**: typing.Optional[str]

### RiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### Questions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.QuestionMetric]]


# PillarReviewSummary

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


# Profile

### ProfileArn
- **Type**: typing.Optional[str]

### ProfileVersion
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]

### ProfileDescription
- **Type**: typing.Optional[str]

### ProfileQuestions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileQuestion]]

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


# ProfileChoice

### ChoiceId
- **Type**: typing.Optional[str]

### ChoiceTitle
- **Type**: typing.Optional[str]

### ChoiceDescription
- **Type**: typing.Optional[str]


# ProfileNotificationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProfileQuestion

### QuestionId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### QuestionDescription
- **Type**: typing.Optional[str]

### QuestionChoices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileChoice]]

### SelectedChoiceIds
- **Type**: typing.Optional[typing.List[str]]

### MinSelectedChoices
- **Type**: typing.Optional[int]

### MaxSelectedChoices
- **Type**: typing.Optional[int]


# ProfileQuestionUpdate

### QuestionId
- **Type**: typing.Optional[str]

### SelectedChoiceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ProfileShareSummary

### ShareId
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### StatusMessage
- **Type**: typing.Optional[str]


# ProfileSummary

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


# ProfileTemplate

### TemplateName
- **Type**: typing.Optional[str]

### TemplateQuestions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTemplateQuestion]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ProfileTemplateChoice

### ChoiceId
- **Type**: typing.Optional[str]

### ChoiceTitle
- **Type**: typing.Optional[str]

### ChoiceDescription
- **Type**: typing.Optional[str]


# ProfileTemplateQuestion

### QuestionId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### QuestionDescription
- **Type**: typing.Optional[str]

### QuestionChoices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileTemplateChoice]]

### MinSelectedChoices
- **Type**: typing.Optional[int]

### MaxSelectedChoices
- **Type**: typing.Optional[int]


# QuestionDifference

### QuestionId
- **Type**: typing.Optional[str]

### QuestionTitle
- **Type**: typing.Optional[str]

### DifferenceStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'NEW', 'UPDATED']]


# QuestionMetric

### QuestionId
- **Type**: typing.Optional[str]

### Risk
- **Type**: typing.Optional[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED']]

### BestPractices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.BestPractice]]


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


# ReviewTemplate

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


# ReviewTemplateAnswer

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.Choice]]

### SelectedChoices
- **Type**: typing.Optional[typing.List[str]]

### ChoiceAnswers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceAnswer]]

### IsApplicable
- **Type**: typing.Optional[bool]

### AnswerStatus
- **Type**: typing.Optional[typing.Literal['ANSWERED', 'UNANSWERED']]

### Notes
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# ReviewTemplateAnswerSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReviewTemplateLensReview

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplatePillarReviewSummary]]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Notes
- **Type**: typing.Optional[str]

### QuestionCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWERED', 'UNANSWERED'], int]]

### NextToken
- **Type**: typing.Optional[str]


# ReviewTemplatePillarReviewSummary

### PillarId
- **Type**: typing.Optional[str]

### PillarName
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### QuestionCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWERED', 'UNANSWERED'], int]]


# ReviewTemplateSummary

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


# SelectedPillar

### PillarId
- **Type**: typing.Optional[str]

### SelectedQuestionIds
- **Type**: typing.Optional[typing.Sequence[str]]


# SelectedPillarOutput

### PillarId
- **Type**: typing.Optional[str]

### SelectedQuestionIds
- **Type**: typing.Optional[typing.List[str]]


# ShareInvitation

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


# ShareInvitationSummary

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


# TagResourceInput

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateShareSummary

### ShareId
- **Type**: typing.Optional[str]

### SharedWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ASSOCIATED', 'ASSOCIATING', 'EXPIRED', 'FAILED', 'PENDING', 'REJECTED', 'REVOKED']]

### StatusMessage
- **Type**: typing.Optional[str]


# UntagResourceInput

### WorkloadArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnswerInput

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceUpdate]]

### Notes
- **Type**: typing.Optional[str]

### IsApplicable
- **Type**: typing.Optional[bool]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# UpdateAnswerOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Answer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGlobalSettingsInput

### OrganizationSharingStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DiscoveryIntegrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.AccountJiraConfigurationInput]


# UpdateIntegrationInput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### IntegratingService
- **Type**: typing.Literal['JIRA']
- **Required**: Yes


# UpdateLensReviewInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.JiraSelectedQuestionConfigurationUnion]


# UpdateLensReviewOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.LensReview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProfileInput

### ProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileDescription
- **Type**: typing.Optional[str]

### ProfileQuestions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wellarchitected_classes.ProfileQuestionUpdate]]


# UpdateProfileOutput

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Profile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReviewTemplateAnswerInput

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wellarchitected_classes.ChoiceUpdate]]

### Notes
- **Type**: typing.Optional[str]

### IsApplicable
- **Type**: typing.Optional[bool]

### Reason
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_CONSTRAINTS', 'BUSINESS_PRIORITIES', 'NONE', 'OTHER', 'OUT_OF_SCOPE']]


# UpdateReviewTemplateAnswerOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### Answer
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateAnswer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReviewTemplateInput

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


# UpdateReviewTemplateLensReviewInput

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


# UpdateReviewTemplateLensReviewOutput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensReview
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplateLensReview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReviewTemplateOutput

### ReviewTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ReviewTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateShareInvitationInput

### ShareInvitationId
- **Type**: <class 'str'>
- **Required**: Yes

### ShareInvitationAction
- **Type**: typing.Literal['ACCEPT', 'REJECT']
- **Required**: Yes


# UpdateShareInvitationOutput

### ShareInvitation
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ShareInvitation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkloadInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadDiscoveryConfigUnion]

### Applications
- **Type**: typing.Optional[typing.Sequence[str]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadJiraConfigurationInput]


# UpdateWorkloadOutput

### Workload
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.Workload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkloadShareInput

### ShareId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionType
- **Type**: typing.Literal['CONTRIBUTOR', 'READONLY']
- **Required**: Yes


# UpdateWorkloadShareOutput

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadShare
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadShare'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wellarchitected_classes.ResponseMetadata'>
- **Required**: Yes


# UpgradeLensReviewInput

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


# UpgradeProfileVersionInput

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


# UpgradeReviewTemplateLensReviewInput

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### LensAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# VersionDifferences

### PillarDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.PillarDifference]]


# Workload

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadDiscoveryConfigOutput]

### Applications
- **Type**: typing.Optional[typing.List[str]]

### Profiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfile]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadJiraConfigurationOutput]


# WorkloadDiscoveryConfig

### TrustedAdvisorIntegrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WorkloadResourceDefinition
- **Type**: typing.Optional[typing.Sequence[typing.Literal['APP_REGISTRY', 'WORKLOAD_METADATA']]]


# WorkloadDiscoveryConfigOutput

### TrustedAdvisorIntegrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WorkloadResourceDefinition
- **Type**: typing.Optional[typing.List[typing.Literal['APP_REGISTRY', 'WORKLOAD_METADATA']]]


# WorkloadDiscoveryConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkloadJiraConfigurationInput

### IssueManagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'INHERIT']]

### IssueManagementType
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### JiraProjectKey
- **Type**: typing.Optional[str]


# WorkloadJiraConfigurationOutput

### IssueManagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'INHERIT']]

### IssueManagementType
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### JiraProjectKey
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# WorkloadProfile

### ProfileArn
- **Type**: typing.Optional[str]

### ProfileVersion
- **Type**: typing.Optional[str]


# WorkloadShare

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


# WorkloadShareSummary

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


# WorkloadSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wellarchitected_classes.WorkloadProfile]]

### PrioritizedRiskCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['HIGH', 'MEDIUM', 'NONE', 'NOT_APPLICABLE', 'UNANSWERED'], int]]


