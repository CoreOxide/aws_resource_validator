# Cleanrooms Classes

# AggregateColumnOutputTypeDef

### columnNames
- **Type**: typing.List[str]
- **Required**: Yes

### function
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'SUM', 'SUM_DISTINCT']
- **Required**: Yes


# AggregateColumnTypeDef

### columnNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### function
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'SUM', 'SUM_DISTINCT']
- **Required**: Yes


# AggregationConstraintTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisRuleAggregationOutputTypeDef

### aggregateColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregateColumnOutputTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregationConstraintTypeDef]
- **Required**: Yes

### joinRequired
- **Type**: typing.Optional[typing.Literal['QUERY_RUNNER']]

### allowedJoinOperators
- **Type**: typing.Optional[typing.List[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRuleAggregationTypeDef

### aggregateColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregateColumnTypeDef]
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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregationConstraintTypeDef]
- **Required**: Yes

### joinRequired
- **Type**: typing.Optional[typing.Literal['QUERY_RUNNER']]

### allowedJoinOperators
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRuleCustomOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyConfigurationOutputTypeDef]


# AnalysisRuleCustomTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyConfigurationTypeDef]


# AnalysisRuleIdMappingTableTypeDef

### joinColumns
- **Type**: typing.List[str]
- **Required**: Yes

### queryConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.QueryConstraintTypeDef]
- **Required**: Yes

### dimensionColumns
- **Type**: typing.Optional[typing.List[str]]


# AnalysisRuleListOutputTypeDef

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


# AnalysisRuleListTypeDef

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


# AnalysisRulePolicyTypeDef

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRulePolicyV1TypeDef]


# AnalysisRulePolicyV1TypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisRuleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisSchemaTypeDef

### referencedTables
- **Type**: typing.Optional[typing.List[str]]


# AnalysisSourceTypeDef

### text
- **Type**: typing.Optional[str]


# AnalysisTemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisTemplateValidationStatusReasonTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# AthenaTableReferenceTypeDef

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

# BatchGetCollaborationAnalysisTemplateErrorTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCollaborationAnalysisTemplateInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetCollaborationAnalysisTemplateOutputTypeDef

### collaborationAnalysisTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplateTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.BatchGetCollaborationAnalysisTemplateErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetSchemaAnalysisRuleErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetSchemaAnalysisRuleInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaAnalysisRuleRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaAnalysisRuleRequestTypeDef]
- **Required**: Yes


# BatchGetSchemaAnalysisRuleOutputTypeDef

### analysisRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.BatchGetSchemaAnalysisRuleErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetSchemaErrorTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetSchemaInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetSchemaOutputTypeDef

### schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.BatchGetSchemaErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BilledResourceUtilizationTypeDef

### units
- **Type**: <class 'float'>
- **Required**: Yes


# CollaborationAnalysisTemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationAnalysisTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationConfiguredAudienceModelAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationConfiguredAudienceModelAssociationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationIdNamespaceAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationIdNamespaceAssociationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationPrivacyBudgetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationPrivacyBudgetTemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationPrivacyBudgetTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollaborationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComputeConfigurationTypeDef

### worker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.WorkerComputeConfigurationTypeDef]


# ConfigurationDetailsTypeDef

### directAnalysisConfigurationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DirectAnalysisConfigurationDetailsTypeDef]


# ConfiguredAudienceModelAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredAudienceModelAssociationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRulePolicyOutputTypeDef

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyV1OutputTypeDef]


# ConfiguredTableAnalysisRulePolicyTypeDef

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyV1TypeDef]


# ConfiguredTableAnalysisRulePolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRulePolicyV1OutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRulePolicyV1TypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAnalysisRuleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleAggregationTypeDef

### allowedResultReceivers
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleCustomTypeDef

### allowedResultReceivers
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfiguredTableAssociationAnalysisRuleListOutputTypeDef

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleListTypeDef

### allowedResultReceivers
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef]


# ConfiguredTableAssociationAnalysisRulePolicyTypeDef

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef]


# ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationAnalysisRuleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableAssociationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfiguredTableTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAnalysisTemplateOutputTypeDef

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCollaborationInputTypeDef

### members
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.MemberSpecificationTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLMemberAbilitiesUnionTypeDef]

### dataEncryptionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DataEncryptionMetadataTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### creatorPaymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaymentConfigurationTypeDef]

### analyticsEngine
- **Type**: typing.Optional[typing.Literal['CLEAN_ROOMS_SQL', 'SPARK']]


# CreateCollaborationOutputTypeDef

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredAudienceModelAssociationInputTypeDef

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


# CreateConfiguredAudienceModelAssociationOutputTypeDef

### configuredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredTableAnalysisRuleInputTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyUnionTypeDef'>
- **Required**: Yes


# CreateConfiguredTableAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredTableAssociationAnalysisRuleInputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef'>
- **Required**: Yes


# CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredTableAssociationInputTypeDef

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


# CreateConfiguredTableAssociationOutputTypeDef

### configuredTableAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredTableInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tableReference
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.TableReferenceUnionTypeDef'>
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


# CreateConfiguredTableOutputTypeDef

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIdMappingTableInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableInputReferenceConfigTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateIdMappingTableOutputTypeDef

### idMappingTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIdNamespaceAssociationInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociationInputReferenceConfigTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### description
- **Type**: typing.Optional[str]

### idMappingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingConfigTypeDef]


# CreateIdNamespaceAssociationOutputTypeDef

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMembershipInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipProtectedQueryResultConfigurationTypeDef]

### paymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipPaymentConfigurationTypeDef]


# CreateMembershipOutputTypeDef

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePrivacyBudgetTemplateInputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateParametersInputTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePrivacyBudgetTemplateOutputTypeDef

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataEncryptionMetadataTypeDef

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


# DeleteAnalysisTemplateInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCollaborationInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelAssociationInputTypeDef

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredTableAnalysisRuleInputTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# DeleteConfiguredTableAssociationInputTypeDef

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredTableInputTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdMappingTableInputTypeDef

### idMappingTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdNamespaceAssociationInputTypeDef

### idNamespaceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMemberInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMembershipInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrivacyBudgetTemplateInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DifferentialPrivacyColumnTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DifferentialPrivacyConfigurationOutputTypeDef

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyColumnTypeDef]
- **Required**: Yes


# DifferentialPrivacyConfigurationTypeDef

### columns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyColumnTypeDef]
- **Required**: Yes


# DifferentialPrivacyParametersTypeDef

### sensitivityParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacySensitivityParametersTypeDef]
- **Required**: Yes


# DifferentialPrivacyPreviewAggregationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DifferentialPrivacyPreviewParametersInputTypeDef

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyBudgetAggregationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DifferentialPrivacyPrivacyBudgetTypeDef

### aggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPrivacyBudgetAggregationTypeDef]
- **Required**: Yes

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyImpactTypeDef

### aggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPreviewAggregationTypeDef]
- **Required**: Yes


# DifferentialPrivacySensitivityParametersTypeDef

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


# DifferentialPrivacyTemplateParametersInputTypeDef

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyTemplateParametersOutputTypeDef

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyTemplateUpdateParametersTypeDef

### epsilon
- **Type**: typing.Optional[int]

### usersNoisePerQuery
- **Type**: typing.Optional[int]


# DirectAnalysisConfigurationDetailsTypeDef

### receiverAccountIds
- **Type**: typing.Optional[typing.List[str]]


# GetAnalysisTemplateInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnalysisTemplateOutputTypeDef

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationAnalysisTemplateInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationAnalysisTemplateOutputTypeDef

### collaborationAnalysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationConfiguredAudienceModelAssociationInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef

### collaborationConfiguredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationConfiguredAudienceModelAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationIdNamespaceAssociationInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationIdNamespaceAssociationOutputTypeDef

### collaborationIdNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationIdNamespaceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationOutputTypeDef

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationPrivacyBudgetTemplateInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationPrivacyBudgetTemplateOutputTypeDef

### collaborationPrivacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationPrivacyBudgetTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredAudienceModelAssociationInputTypeDef

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredAudienceModelAssociationOutputTypeDef

### configuredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredTableAnalysisRuleInputTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# GetConfiguredTableAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredTableAssociationAnalysisRuleInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# GetConfiguredTableAssociationAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredTableAssociationInputTypeDef

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredTableAssociationOutputTypeDef

### configuredTableAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredTableInputTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredTableOutputTypeDef

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdMappingTableInputTypeDef

### idMappingTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdMappingTableOutputTypeDef

### idMappingTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdNamespaceAssociationInputTypeDef

### idNamespaceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdNamespaceAssociationOutputTypeDef

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMembershipInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMembershipOutputTypeDef

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPrivacyBudgetTemplateInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrivacyBudgetTemplateOutputTypeDef

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProtectedQueryInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### protectedQueryIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProtectedQueryOutputTypeDef

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaOutputTypeDef

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaTypeDef'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.GetSchemaOutputTypeDef'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlueTableReferenceTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# IdMappingConfigTypeDef

### allowUseAsDimensionColumn
- **Type**: <class 'bool'>
- **Required**: Yes


# IdMappingTableInputReferenceConfigTypeDef

### inputReferenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### manageResourcePolicies
- **Type**: <class 'bool'>
- **Required**: Yes


# IdMappingTableInputReferencePropertiesTypeDef

### idMappingTableInputSource
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableInputSourceTypeDef]
- **Required**: Yes


# IdMappingTableInputSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdMappingTableSchemaTypePropertiesTypeDef

### idMappingTableInputSource
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableInputSourceTypeDef]
- **Required**: Yes


# IdMappingTableSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdMappingTableTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdNamespaceAssociationInputReferenceConfigTypeDef

### inputReferenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### manageResourcePolicies
- **Type**: <class 'bool'>
- **Required**: Yes


# IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef

### idNamespaceType
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes


# IdNamespaceAssociationInputReferencePropertiesTypeDef

### idNamespaceType
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### idMappingWorkflowsSupported
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# IdNamespaceAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdNamespaceAssociationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAnalysisTemplatesInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListAnalysisTemplatesInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAnalysisTemplatesOutputTypeDef

### analysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationAnalysisTemplatesInputPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationAnalysisTemplatesInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationAnalysisTemplatesOutputTypeDef

### collaborationAnalysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef

### collaborationConfiguredAudienceModelAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationConfiguredAudienceModelAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationIdNamespaceAssociationsInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationIdNamespaceAssociationsOutputTypeDef

### collaborationIdNamespaceAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationIdNamespaceAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationPrivacyBudgetTemplatesInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationPrivacyBudgetTemplatesOutputTypeDef

### collaborationPrivacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationPrivacyBudgetTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationPrivacyBudgetsInputPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationPrivacyBudgetsInputTypeDef

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


# ListCollaborationPrivacyBudgetsOutputTypeDef

### collaborationPrivacyBudgetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationPrivacyBudgetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationsInputPaginateTypeDef

### memberStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INVITED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### memberStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INVITED']]


# ListCollaborationsOutputTypeDef

### collaborationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredAudienceModelAssociationsInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListConfiguredAudienceModelAssociationsInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredAudienceModelAssociationsOutputTypeDef

### configuredAudienceModelAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredTableAssociationsInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListConfiguredTableAssociationsInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredTableAssociationsOutputTypeDef

### configuredTableAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredTablesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListConfiguredTablesInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredTablesOutputTypeDef

### configuredTableSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingTablesInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListIdMappingTablesInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIdMappingTablesOutputTypeDef

### idMappingTableSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdNamespaceAssociationsInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListIdNamespaceAssociationsInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIdNamespaceAssociationsOutputTypeDef

### idNamespaceAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMembersInputPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListMembersInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMembersOutputTypeDef

### memberSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.MemberSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMembershipsInputPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListMembershipsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']]


# ListMembershipsOutputTypeDef

### membershipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrivacyBudgetTemplatesInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListPrivacyBudgetTemplatesInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrivacyBudgetTemplatesOutputTypeDef

### privacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrivacyBudgetsInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListPrivacyBudgetsInputTypeDef

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


# ListPrivacyBudgetsOutputTypeDef

### privacyBudgetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProtectedQueriesInputPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'STARTED', 'SUBMITTED', 'SUCCESS', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListProtectedQueriesInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'STARTED', 'SUBMITTED', 'SUCCESS', 'TIMED_OUT']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProtectedQueriesOutputTypeDef

### protectedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuerySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSchemasInputPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaType
- **Type**: typing.Optional[typing.Literal['ID_MAPPING_TABLE', 'TABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListSchemasInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaType
- **Type**: typing.Optional[typing.Literal['ID_MAPPING_TABLE', 'TABLE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSchemasOutputTypeDef

### schemaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MLMemberAbilitiesOutputTypeDef

### customMLMemberAbilities
- **Type**: typing.List[typing.Literal['CAN_RECEIVE_INFERENCE_OUTPUT', 'CAN_RECEIVE_MODEL_OUTPUT']]
- **Required**: Yes


# MLMemberAbilitiesTypeDef

### customMLMemberAbilities
- **Type**: typing.Sequence[typing.Literal['CAN_RECEIVE_INFERENCE_OUTPUT', 'CAN_RECEIVE_MODEL_OUTPUT']]
- **Required**: Yes


# MLMemberAbilitiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MLPaymentConfigTypeDef

### modelTraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ModelTrainingPaymentConfigTypeDef]

### modelInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ModelInferencePaymentConfigTypeDef]


# MemberSpecificationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLMemberAbilitiesUnionTypeDef]

### paymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaymentConfigurationTypeDef]


# MemberSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PaymentConfigurationTypeDef'>
- **Required**: Yes

### mlAbilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLMemberAbilitiesOutputTypeDef]

### membershipId
- **Type**: typing.Optional[str]

### membershipArn
- **Type**: typing.Optional[str]


# MembershipMLPaymentConfigTypeDef

### modelTraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipModelTrainingPaymentConfigTypeDef]

### modelInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipModelInferencePaymentConfigTypeDef]


# MembershipModelInferencePaymentConfigTypeDef

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# MembershipModelTrainingPaymentConfigTypeDef

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# MembershipPaymentConfigurationTypeDef

### queryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipQueryComputePaymentConfigTypeDef'>
- **Required**: Yes

### machineLearning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipMLPaymentConfigTypeDef]


# MembershipProtectedQueryOutputConfigurationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryS3OutputConfigurationTypeDef]


# MembershipProtectedQueryResultConfigurationTypeDef

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipProtectedQueryOutputConfigurationTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]


# MembershipQueryComputePaymentConfigTypeDef

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# MembershipSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MembershipTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelInferencePaymentConfigTypeDef

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# ModelTrainingPaymentConfigTypeDef

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PaymentConfigurationTypeDef

### queryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.QueryComputePaymentConfigTypeDef'>
- **Required**: Yes

### machineLearning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MLPaymentConfigTypeDef]


# PopulateIdMappingTableInputTypeDef

### idMappingTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PopulateIdMappingTableOutputTypeDef

### idMappingJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PreviewPrivacyImpactInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PreviewPrivacyImpactParametersInputTypeDef'>
- **Required**: Yes


# PreviewPrivacyImpactOutputTypeDef

### privacyImpact
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyImpactTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PreviewPrivacyImpactParametersInputTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPreviewParametersInputTypeDef]


# PrivacyBudgetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrivacyBudgetTemplateParametersInputTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateParametersInputTypeDef]


# PrivacyBudgetTemplateParametersOutputTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateParametersOutputTypeDef]


# PrivacyBudgetTemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrivacyBudgetTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrivacyBudgetTemplateUpdateParametersTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateUpdateParametersTypeDef]


# PrivacyBudgetTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPrivacyBudgetTypeDef]


# PrivacyImpactTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyPrivacyImpactTypeDef]


# ProtectedQueryErrorTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryMemberOutputConfigurationTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryOutputConfigurationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryS3OutputConfigurationTypeDef]

### member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryMemberOutputConfigurationTypeDef]


# ProtectedQueryOutputTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryS3OutputTypeDef]

### memberList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuerySingleMemberOutputTypeDef]]


# ProtectedQueryResultConfigurationTypeDef

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryOutputConfigurationTypeDef'>
- **Required**: Yes


# ProtectedQueryResultTypeDef

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryOutputTypeDef'>
- **Required**: Yes


# ProtectedQueryS3OutputConfigurationTypeDef

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


# ProtectedQueryS3OutputTypeDef

### location
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQuerySQLParametersOutputTypeDef

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProtectedQuerySQLParametersTypeDef

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ProtectedQuerySingleMemberOutputTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryStatisticsTypeDef

### totalDurationInMillis
- **Type**: typing.Optional[int]

### billedResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.BilledResourceUtilizationTypeDef]


# ProtectedQuerySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProtectedQueryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryComputePaymentConfigTypeDef

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# QueryConstraintRequireOverlapTypeDef

### columns
- **Type**: typing.Optional[typing.List[str]]


# QueryConstraintTypeDef

### requireOverlap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.QueryConstraintRequireOverlapTypeDef]


# ReceiverConfigurationTypeDef

### analysisType
- **Type**: typing.Literal['ADDITIONAL_ANALYSIS', 'DIRECT_ANALYSIS']
- **Required**: Yes

### configurationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfigurationDetailsTypeDef]


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


# SchemaAnalysisRuleRequestTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaStatusDetailTypeDef

### status
- **Type**: typing.Literal['NOT_READY', 'READY']
- **Required**: Yes

### analysisType
- **Type**: typing.Literal['ADDITIONAL_ANALYSIS', 'DIRECT_ANALYSIS']
- **Required**: Yes

### reasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaStatusReasonTypeDef]]

### analysisRuleType
- **Type**: typing.Optional[typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']]

### configurations
- **Type**: typing.Optional[typing.List[typing.Literal['DIFFERENTIAL_PRIVACY']]]


# SchemaStatusReasonTypeDef

### code
- **Type**: typing.Literal['ADDITIONAL_ANALYSES_NOT_ALLOWED', 'ADDITIONAL_ANALYSES_NOT_CONFIGURED', 'ANALYSIS_PROVIDERS_NOT_CONFIGURED', 'ANALYSIS_RULE_MISSING', 'ANALYSIS_RULE_TYPES_NOT_COMPATIBLE', 'ANALYSIS_TEMPLATES_NOT_CONFIGURED', 'COLLABORATION_ANALYSIS_RULE_NOT_CONFIGURED', 'DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED', 'ID_MAPPING_TABLE_NOT_POPULATED', 'RESULT_RECEIVERS_NOT_ALLOWED', 'RESULT_RECEIVERS_NOT_CONFIGURED']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaTypePropertiesTypeDef

### idMappingTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableSchemaTypePropertiesTypeDef]


# SnowflakeTableReferenceOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchemaOutputTypeDef'>
- **Required**: Yes


# SnowflakeTableReferenceTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchemaTypeDef'>
- **Required**: Yes


# SnowflakeTableSchemaOutputTypeDef

### v1
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchemaV1TypeDef]]


# SnowflakeTableSchemaTypeDef

### v1
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableSchemaV1TypeDef]]


# SnowflakeTableSchemaV1TypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnType
- **Type**: <class 'str'>
- **Required**: Yes


# StartProtectedQueryOutputTypeDef

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TableReferenceOutputTypeDef

### glue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.GlueTableReferenceTypeDef]

### snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableReferenceOutputTypeDef]

### athena
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AthenaTableReferenceTypeDef]


# TableReferenceTypeDef

### glue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.GlueTableReferenceTypeDef]

### snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.SnowflakeTableReferenceTypeDef]

### athena
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AthenaTableReferenceTypeDef]


# TableReferenceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnalysisTemplateInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnalysisTemplateOutputTypeDef

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCollaborationInputTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateCollaborationOutputTypeDef

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfiguredAudienceModelAssociationInputTypeDef

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


# UpdateConfiguredAudienceModelAssociationOutputTypeDef

### configuredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredAudienceModelAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableAnalysisRuleInputTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyUnionTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableAssociationInputTypeDef

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


# UpdateConfiguredTableAssociationOutputTypeDef

### configuredTableAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableInputTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateConfiguredTableOutputTypeDef

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIdMappingTableInputTypeDef

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


# UpdateIdMappingTableOutputTypeDef

### idMappingTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingTableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIdNamespaceAssociationInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.IdMappingConfigTypeDef]


# UpdateIdNamespaceAssociationOutputTypeDef

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.IdNamespaceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMembershipInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipProtectedQueryResultConfigurationTypeDef]


# UpdateMembershipOutputTypeDef

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePrivacyBudgetTemplateInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateUpdateParametersTypeDef]


# UpdatePrivacyBudgetTemplateOutputTypeDef

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProtectedQueryInputTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### protectedQueryIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetStatus
- **Type**: typing.Literal['CANCELLED']
- **Required**: Yes


# UpdateProtectedQueryOutputTypeDef

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkerComputeConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

