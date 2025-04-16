# Cleanrooms Classes

# AggregateColumn

### columnNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### function
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'SUM', 'SUM_DISTINCT']
- **Required**: Yes


# AggregateColumnOutput

### columnNames
- **Type**: typing.List[str]
- **Required**: Yes

### function
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'SUM', 'SUM_DISTINCT']
- **Required**: Yes


# AggregationConstraint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisRule

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisRuleAggregation

### aggregateColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregateColumn]
- **Required**: Yes

### joinColumns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### dimensionColumns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### scalarFunctions
- **Type**: typing.Sequence[typing.Literal['ABS', 'CAST', 'CEILING', 'COALESCE', 'CONVERT', 'CURRENT_DATE', 'DATEADD', 'EXTRACT', 'FLOOR', 'GETDATE', 'LN', 'LOG', 'LOWER', 'ROUND', 'RTRIM', 'SQRT', 'SUBSTRING', 'TO_CHAR', 'TO_DATE', 'TO_NUMBER', 'TO_TIMESTAMP', 'TRIM', 'TRUNC', 'UPPER']]
- **Required**: Yes

### outputConstraints
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregationConstraint]
- **Required**: Yes

### joinRequired
- **Type**: typing.Optional[typing.Literal['QUERY_RUNNER']]

### allowedJoinOperators
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRuleAggregationOutput

### aggregateColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregateColumnOutput]
- **Required**: Yes

### joinColumns
- **Type**: typing.List[str]
- **Required**: Yes

### dimensionColumns
- **Type**: typing.List[str]
- **Required**: Yes

### scalarFunctions
- **Type**: typing.List[typing.Literal['ABS', 'CAST', 'CEILING', 'COALESCE', 'CONVERT', 'CURRENT_DATE', 'DATEADD', 'EXTRACT', 'FLOOR', 'GETDATE', 'LN', 'LOG', 'LOWER', 'ROUND', 'RTRIM', 'SQRT', 'SUBSTRING', 'TO_CHAR', 'TO_DATE', 'TO_NUMBER', 'TO_TIMESTAMP', 'TRIM', 'TRUNC', 'UPPER']]
- **Required**: Yes

### outputConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregationConstraint]
- **Required**: Yes

### joinRequired
- **Type**: typing.Optional[typing.Literal['QUERY_RUNNER']]

### allowedJoinOperators
- **Type**: typing.Optional[typing.List[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRuleCustom

### allowedAnalyses
- **Type**: typing.Sequence[str]
- **Required**: Yes

### allowedAnalysisProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]

### disallowedOutputColumns
- **Type**: typing.Optional[typing.Sequence[str]]

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyConfiguration]


# AnalysisRuleCustomOutput

### allowedAnalyses
- **Type**: typing.List[str]
- **Required**: Yes

### allowedAnalysisProviders
- **Type**: typing.Optional[typing.List[str]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]

### disallowedOutputColumns
- **Type**: typing.Optional[typing.List[str]]

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyConfigurationOutput]


# AnalysisRuleIdMappingTable

### joinColumns
- **Type**: typing.List[str]
- **Required**: Yes

### queryConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.QueryConstraint]
- **Required**: Yes

### dimensionColumns
- **Type**: typing.Optional[typing.List[str]]


# AnalysisRuleList

### joinColumns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### listColumns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### allowedJoinOperators
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRuleListOutput

### joinColumns
- **Type**: typing.List[str]
- **Required**: Yes

### listColumns
- **Type**: typing.List[str]
- **Required**: Yes

### allowedJoinOperators
- **Type**: typing.Optional[typing.List[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRulePolicy

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRulePolicyV1]


# AnalysisRulePolicyV1

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisSchema

### referencedTables
- **Type**: typing.Optional[typing.List[str]]


# AnalysisSource

### text
- **Type**: typing.Optional[str]


# AnalysisTemplate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisTemplateSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisTemplateValidationStatusReason

### message
- **Type**: <class 'str'>
- **Required**: Yes


# AthenaTableReference

### workGroup
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### outputLocation
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCollaborationAnalysisTemplateError

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCollaborationAnalysisTemplateInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetCollaborationAnalysisTemplateOutput

### collaborationAnalysisTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplate]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.BatchGetCollaborationAnalysisTemplateError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetSchemaAnalysisRuleError

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetSchemaAnalysisRuleInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaAnalysisRuleRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaAnalysisRuleRequest]
- **Required**: Yes


# BatchGetSchemaAnalysisRuleOutput

### analysisRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRule]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.BatchGetSchemaAnalysisRuleError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetSchemaError

### name
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetSchemaInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetSchemaOutput

### schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.Schema]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.BatchGetSchemaError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# BilledResourceUtilization

### units
- **Type**: <class 'float'>
- **Required**: Yes


# Collaboration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationAnalysisTemplate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationAnalysisTemplateSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationConfiguredAudienceModelAssociation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationConfiguredAudienceModelAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationIdNamespaceAssociation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationIdNamespaceAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationPrivacyBudgetSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationPrivacyBudgetTemplate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationPrivacyBudgetTemplateSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComputeConfiguration

### worker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.WorkerComputeConfiguration]


# ConfigurationDetails

### directAnalysisConfigurationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DirectAnalysisConfigurationDetails]


# ConfiguredAudienceModelAssociation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredAudienceModelAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTable

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRule

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRulePolicy

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyV1]


# ConfiguredTableAnalysisRulePolicyOutput

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyV1Output]


# ConfiguredTableAnalysisRulePolicyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRulePolicyV1

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRulePolicyV1Output

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRule

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRuleAggregation

### allowedResultReceivers
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfiguredTableAssociationAnalysisRuleAggregationOutput

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleCustom

### allowedResultReceivers
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfiguredTableAssociationAnalysisRuleCustomOutput

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleList

### allowedResultReceivers
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfiguredTableAssociationAnalysisRuleListOutput

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRulePolicy

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyV1]


# ConfiguredTableAssociationAnalysisRulePolicyOutput

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyV1Output]


# ConfiguredTableAssociationAnalysisRulePolicyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRulePolicyV1

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRulePolicyV1Output

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAnalysisTemplateOutput

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCollaborationInput

### members
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.MemberSpecification]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creatorMemberAbilities
- **Type**: typing.Sequence[typing.Literal['CAN_QUERY', 'CAN_RECEIVE_RESULTS']]
- **Required**: Yes

### creatorDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### creatorMLMemberAbilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLMemberAbilitiesUnion]

### dataEncryptionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DataEncryptionMetadata]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### creatorPaymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaymentConfiguration]

### analyticsEngine
- **Type**: typing.Optional[typing.Literal['CLEAN_ROOMS_SQL', 'SPARK']]


# CreateCollaborationOutput

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.Collaboration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredAudienceModelAssociationInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelAssociationName
- **Type**: <class 'str'>
- **Required**: Yes

### manageResourcePolicies
- **Type**: <class 'bool'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### description
- **Type**: typing.Optional[str]


# CreateConfiguredAudienceModelAssociationOutput

### configuredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredTableAnalysisRuleInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyUnion'>
- **Required**: Yes


# CreateConfiguredTableAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredTableAssociationAnalysisRuleInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyUnion'>
- **Required**: Yes


# CreateConfiguredTableAssociationAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredTableAssociationInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfiguredTableAssociationOutput

### configuredTableAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredTableInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tableReference
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.TableReferenceUnion'>
- **Required**: Yes

### allowedColumns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Literal['DIRECT_QUERY']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfiguredTableOutput

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdMappingTableInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableInputReferenceConfig'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateIdMappingTableOutput

### idMappingTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdNamespaceAssociationInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociationInputReferenceConfig'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### description
- **Type**: typing.Optional[str]

### idMappingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingConfig]


# CreateIdNamespaceAssociationOutput

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMembershipInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipProtectedQueryResultConfiguration]

### paymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipPaymentConfiguration]


# CreateMembershipOutput

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.Membership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePrivacyBudgetTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### autoRefresh
- **Type**: typing.Literal['CALENDAR_MONTH', 'NONE']
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateParametersInput'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePrivacyBudgetTemplateOutput

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# DataEncryptionMetadata

### allowCleartext
- **Type**: <class 'bool'>
- **Required**: Yes

### allowDuplicates
- **Type**: <class 'bool'>
- **Required**: Yes

### allowJoinsOnColumnsWithDifferentNames
- **Type**: <class 'bool'>
- **Required**: Yes

### preserveNulls
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteAnalysisTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCollaborationInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelAssociationInput

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredTableAnalysisRuleInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# DeleteConfiguredTableAssociationAnalysisRuleInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# DeleteConfiguredTableAssociationInput

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredTableInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdMappingTableInput

### idMappingTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdNamespaceAssociationInput

### idNamespaceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMemberInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMembershipInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrivacyBudgetTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DifferentialPrivacyColumn

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DifferentialPrivacyConfiguration

### columns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyColumn]
- **Required**: Yes


# DifferentialPrivacyConfigurationOutput

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyColumn]
- **Required**: Yes


# DifferentialPrivacyParameters

### sensitivityParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacySensitivityParameters]
- **Required**: Yes


# DifferentialPrivacyPreviewAggregation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DifferentialPrivacyPreviewParametersInput

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyBudget

### aggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPrivacyBudgetAggregation]
- **Required**: Yes

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyBudgetAggregation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DifferentialPrivacyPrivacyImpact

### aggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPreviewAggregation]
- **Required**: Yes


# DifferentialPrivacySensitivityParameters

### aggregationType
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'STDDEV', 'SUM']
- **Required**: Yes

### aggregationExpression
- **Type**: <class 'str'>
- **Required**: Yes

### userContributionLimit
- **Type**: <class 'int'>
- **Required**: Yes

### minColumnValue
- **Type**: typing.Optional[float]

### maxColumnValue
- **Type**: typing.Optional[float]


# DifferentialPrivacyTemplateParametersInput

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyTemplateParametersOutput

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyTemplateUpdateParameters

### epsilon
- **Type**: typing.Optional[int]

### usersNoisePerQuery
- **Type**: typing.Optional[int]


# DirectAnalysisConfigurationDetails

### receiverAccountIds
- **Type**: typing.Optional[typing.List[str]]


# GetAnalysisTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnalysisTemplateOutput

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationAnalysisTemplateInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationAnalysisTemplateOutput

### collaborationAnalysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationConfiguredAudienceModelAssociationInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationConfiguredAudienceModelAssociationOutput

### collaborationConfiguredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationIdNamespaceAssociationInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationIdNamespaceAssociationOutput

### collaborationIdNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationIdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationOutput

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.Collaboration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationPrivacyBudgetTemplateInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationPrivacyBudgetTemplateOutput

### collaborationPrivacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationPrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredAudienceModelAssociationInput

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredAudienceModelAssociationOutput

### configuredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredTableAnalysisRuleInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# GetConfiguredTableAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredTableAssociationAnalysisRuleInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# GetConfiguredTableAssociationAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredTableAssociationInput

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredTableAssociationOutput

### configuredTableAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredTableInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredTableOutput

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdMappingTableInput

### idMappingTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdMappingTableOutput

### idMappingTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdNamespaceAssociationInput

### idNamespaceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdNamespaceAssociationOutput

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetMembershipInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMembershipOutput

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.Membership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetPrivacyBudgetTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrivacyBudgetTemplateOutput

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetProtectedQueryInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### protectedQueryIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProtectedQueryOutput

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaOutput

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.Schema'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.GetSchemaOutput'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GlueTableReference

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# IdMappingConfig

### allowUseAsDimensionColumn
- **Type**: <class 'bool'>
- **Required**: Yes


# IdMappingTable

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdMappingTableInputReferenceConfig

### inputReferenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### manageResourcePolicies
- **Type**: <class 'bool'>
- **Required**: Yes


# IdMappingTableInputReferenceProperties

### idMappingTableInputSource
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableInputSource]
- **Required**: Yes


# IdMappingTableInputSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdMappingTableSchemaTypeProperties

### idMappingTableInputSource
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableInputSource]
- **Required**: Yes


# IdMappingTableSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdNamespaceAssociation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdNamespaceAssociationInputReferenceConfig

### inputReferenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### manageResourcePolicies
- **Type**: <class 'bool'>
- **Required**: Yes


# IdNamespaceAssociationInputReferenceProperties

### idNamespaceType
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### idMappingWorkflowsSupported
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# IdNamespaceAssociationInputReferencePropertiesSummary

### idNamespaceType
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes


# IdNamespaceAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAnalysisTemplatesInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAnalysisTemplatesInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListAnalysisTemplatesOutput

### analysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationAnalysisTemplatesInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationAnalysisTemplatesInputPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListCollaborationAnalysisTemplatesOutput

### collaborationAnalysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationConfiguredAudienceModelAssociationsInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationConfiguredAudienceModelAssociationsInputPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListCollaborationConfiguredAudienceModelAssociationsOutput

### collaborationConfiguredAudienceModelAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationConfiguredAudienceModelAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationIdNamespaceAssociationsInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationIdNamespaceAssociationsInputPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListCollaborationIdNamespaceAssociationsOutput

### collaborationIdNamespaceAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationIdNamespaceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationPrivacyBudgetTemplatesInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationPrivacyBudgetTemplatesInputPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListCollaborationPrivacyBudgetTemplatesOutput

### collaborationPrivacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationPrivacyBudgetTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationPrivacyBudgetsInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationPrivacyBudgetsInputPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListCollaborationPrivacyBudgetsOutput

### collaborationPrivacyBudgetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationPrivacyBudgetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### memberStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INVITED']]


# ListCollaborationsInputPaginate

### memberStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INVITED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListCollaborationsOutput

### collaborationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredAudienceModelAssociationsInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredAudienceModelAssociationsInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListConfiguredAudienceModelAssociationsOutput

### configuredAudienceModelAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredTableAssociationsInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredTableAssociationsInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListConfiguredTableAssociationsOutput

### configuredTableAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredTablesInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredTablesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListConfiguredTablesOutput

### configuredTableSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingTablesInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIdMappingTablesInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListIdMappingTablesOutput

### idMappingTableSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdNamespaceAssociationsInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIdNamespaceAssociationsInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListIdNamespaceAssociationsOutput

### idNamespaceAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMembersInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMembersInputPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListMembersOutput

### memberSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.MemberSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMembershipsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']]


# ListMembershipsInputPaginate

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListMembershipsOutput

### membershipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrivacyBudgetTemplatesInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrivacyBudgetTemplatesInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListPrivacyBudgetTemplatesOutput

### privacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrivacyBudgetsInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrivacyBudgetsInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListPrivacyBudgetsOutput

### privacyBudgetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProtectedQueriesInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'STARTED', 'SUBMITTED', 'SUCCESS', 'TIMED_OUT']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProtectedQueriesInputPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'STARTED', 'SUBMITTED', 'SUCCESS', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListProtectedQueriesOutput

### protectedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuerySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSchemasInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaType
- **Type**: typing.Optional[typing.Literal['ID_MAPPING_TABLE', 'TABLE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSchemasInputPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaType
- **Type**: typing.Optional[typing.Literal['ID_MAPPING_TABLE', 'TABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfig]


# ListSchemasOutput

### schemaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# MLMemberAbilities

### customMLMemberAbilities
- **Type**: typing.Sequence[typing.Literal['CAN_RECEIVE_INFERENCE_OUTPUT', 'CAN_RECEIVE_MODEL_OUTPUT']]
- **Required**: Yes


# MLMemberAbilitiesOutput

### customMLMemberAbilities
- **Type**: typing.List[typing.Literal['CAN_RECEIVE_INFERENCE_OUTPUT', 'CAN_RECEIVE_MODEL_OUTPUT']]
- **Required**: Yes


# MLMemberAbilitiesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MLPaymentConfig

### modelTraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ModelTrainingPaymentConfig]

### modelInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ModelInferencePaymentConfig]


# MemberSpecification

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### memberAbilities
- **Type**: typing.Sequence[typing.Literal['CAN_QUERY', 'CAN_RECEIVE_RESULTS']]
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### mlMemberAbilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLMemberAbilitiesUnion]

### paymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaymentConfiguration]


# MemberSummary

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INVITED', 'LEFT', 'REMOVED']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### abilities
- **Type**: typing.List[typing.Literal['CAN_QUERY', 'CAN_RECEIVE_RESULTS']]
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### paymentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PaymentConfiguration'>
- **Required**: Yes

### mlAbilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLMemberAbilitiesOutput]

### membershipId
- **Type**: typing.Optional[str]

### membershipArn
- **Type**: typing.Optional[str]


# Membership

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MembershipMLPaymentConfig

### modelTraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipModelTrainingPaymentConfig]

### modelInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipModelInferencePaymentConfig]


# MembershipModelInferencePaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# MembershipModelTrainingPaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# MembershipPaymentConfiguration

### queryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipQueryComputePaymentConfig'>
- **Required**: Yes

### machineLearning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipMLPaymentConfig]


# MembershipProtectedQueryOutputConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryS3OutputConfiguration]


# MembershipProtectedQueryResultConfiguration

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipProtectedQueryOutputConfiguration'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]


# MembershipQueryComputePaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# MembershipSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelInferencePaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# ModelTrainingPaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PaymentConfiguration

### queryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.QueryComputePaymentConfig'>
- **Required**: Yes

### machineLearning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLPaymentConfig]


# PopulateIdMappingTableInput

### idMappingTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PopulateIdMappingTableOutput

### idMappingJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# PreviewPrivacyImpactInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PreviewPrivacyImpactParametersInput'>
- **Required**: Yes


# PreviewPrivacyImpactOutput

### privacyImpact
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyImpact'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# PreviewPrivacyImpactParametersInput

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPreviewParametersInput]


# PrivacyBudget

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPrivacyBudget]


# PrivacyBudgetSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrivacyBudgetTemplate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrivacyBudgetTemplateParametersInput

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateParametersInput]


# PrivacyBudgetTemplateParametersOutput

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateParametersOutput]


# PrivacyBudgetTemplateSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrivacyBudgetTemplateUpdateParameters

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateUpdateParameters]


# PrivacyImpact

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPrivacyImpact]


# ProtectedQuery

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProtectedQueryError

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryMemberOutputConfiguration

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryOutput

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryS3Output]

### memberList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuerySingleMemberOutput]]


# ProtectedQueryOutputConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryS3OutputConfiguration]

### member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryMemberOutputConfiguration]


# ProtectedQueryResult

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryOutput'>
- **Required**: Yes


# ProtectedQueryResultConfiguration

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryOutputConfiguration'>
- **Required**: Yes


# ProtectedQueryS3Output

### location
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryS3OutputConfiguration

### resultFormat
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]

### singleFileOutput
- **Type**: typing.Optional[bool]


# ProtectedQuerySQLParameters

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ProtectedQuerySQLParametersOutput

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProtectedQuerySingleMemberOutput

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryStatistics

### totalDurationInMillis
- **Type**: typing.Optional[int]

### billedResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.BilledResourceUtilization]


# ProtectedQuerySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryComputePaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# QueryConstraint

### requireOverlap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.QueryConstraintRequireOverlap]


# QueryConstraintRequireOverlap

### columns
- **Type**: typing.Optional[typing.List[str]]


# ReceiverConfiguration

### analysisType
- **Type**: typing.Literal['ADDITIONAL_ANALYSIS', 'DIRECT_ANALYSIS']
- **Required**: Yes

### configurationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfigurationDetails]


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


# Schema

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaAnalysisRuleRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaStatusDetail

### status
- **Type**: typing.Literal['NOT_READY', 'READY']
- **Required**: Yes

### analysisType
- **Type**: typing.Literal['ADDITIONAL_ANALYSIS', 'DIRECT_ANALYSIS']
- **Required**: Yes

### reasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaStatusReason]]

### analysisRuleType
- **Type**: typing.Optional[typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']]

### configurations
- **Type**: typing.Optional[typing.List[typing.Literal['DIFFERENTIAL_PRIVACY']]]


# SchemaStatusReason

### code
- **Type**: typing.Literal['ADDITIONAL_ANALYSES_NOT_ALLOWED', 'ADDITIONAL_ANALYSES_NOT_CONFIGURED', 'ANALYSIS_PROVIDERS_NOT_CONFIGURED', 'ANALYSIS_RULE_MISSING', 'ANALYSIS_RULE_TYPES_NOT_COMPATIBLE', 'ANALYSIS_TEMPLATES_NOT_CONFIGURED', 'COLLABORATION_ANALYSIS_RULE_NOT_CONFIGURED', 'DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED', 'ID_MAPPING_TABLE_NOT_POPULATED', 'RESULT_RECEIVERS_NOT_ALLOWED', 'RESULT_RECEIVERS_NOT_CONFIGURED']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaTypeProperties

### idMappingTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableSchemaTypeProperties]


# SnowflakeTableReference

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### tableSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchema'>
- **Required**: Yes


# SnowflakeTableReferenceOutput

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### tableSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchemaOutput'>
- **Required**: Yes


# SnowflakeTableSchema

### v1
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchemaV1]]


# SnowflakeTableSchemaOutput

### v1
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchemaV1]]


# SnowflakeTableSchemaV1

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnType
- **Type**: <class 'str'>
- **Required**: Yes


# StartProtectedQueryOutput

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# TableReference

### glue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.GlueTableReference]

### snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableReference]

### athena
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AthenaTableReference]


# TableReferenceOutput

### glue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.GlueTableReference]

### snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableReferenceOutput]

### athena
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AthenaTableReference]


# TableReferenceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnalysisTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnalysisTemplateOutput

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCollaborationInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateCollaborationOutput

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.Collaboration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfiguredAudienceModelAssociationInput

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateConfiguredAudienceModelAssociationOutput

### configuredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfiguredTableAnalysisRuleInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyUnion'>
- **Required**: Yes


# UpdateConfiguredTableAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfiguredTableAssociationAnalysisRuleInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyUnion'>
- **Required**: Yes


# UpdateConfiguredTableAssociationAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfiguredTableAssociationInput

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateConfiguredTableAssociationOutput

### configuredTableAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfiguredTableInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateConfiguredTableOutput

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIdMappingTableInput

### idMappingTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]


# UpdateIdMappingTableOutput

### idMappingTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIdNamespaceAssociationInput

### idNamespaceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### idMappingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingConfig]


# UpdateIdNamespaceAssociationOutput

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMembershipInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipProtectedQueryResultConfiguration]


# UpdateMembershipOutput

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.Membership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePrivacyBudgetTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateUpdateParameters]


# UpdatePrivacyBudgetTemplateOutput

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProtectedQueryInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### protectedQueryIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetStatus
- **Type**: typing.Literal['CANCELLED']
- **Required**: Yes


# UpdateProtectedQueryOutput

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# WorkerComputeConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

