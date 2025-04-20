# Cleanrooms Cleanrooms Classes

# AggregateColumn

### columnNames
- **Type**: typing.List[str]
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

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### minimum
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: typing.Literal['COUNT_DISTINCT']
- **Required**: Yes


# AnalysisParameter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BIGINT', 'BINARY', 'BOOLEAN', 'BYTE', 'CHAR', 'CHARACTER', 'DATE', 'DECIMAL', 'DOUBLE', 'DOUBLE_PRECISION', 'FLOAT', 'INT', 'INTEGER', 'LONG', 'NUMERIC', 'REAL', 'SHORT', 'SMALLINT', 'STRING', 'TIME', 'TIMESTAMP', 'TIMESTAMPTZ', 'TIMESTAMP_LTZ', 'TIMESTAMP_NTZ', 'TIMETZ', 'TINYINT', 'VARBYTE', 'VARCHAR']
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[str]


# AnalysisRule

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRulePolicy'>
- **Required**: Yes


# AnalysisRuleAggregation

### aggregateColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AggregateColumn]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AggregationConstraint]
- **Required**: Yes

### joinRequired
- **Type**: typing.Optional[typing.Literal['QUERY_RUNNER']]

### allowedJoinOperators
- **Type**: typing.Optional[typing.List[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRuleAggregationOutput

### aggregateColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AggregateColumnOutput]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AggregationConstraint]
- **Required**: Yes

### joinRequired
- **Type**: typing.Optional[typing.Literal['QUERY_RUNNER']]

### allowedJoinOperators
- **Type**: typing.Optional[typing.List[typing.Literal['AND', 'OR']]]

### additionalAnalyses
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'NOT_ALLOWED', 'REQUIRED']]


# AnalysisRuleCustom

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyConfiguration]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyConfigurationOutput]


# AnalysisRuleIdMappingTable

### joinColumns
- **Type**: typing.List[str]
- **Required**: Yes

### queryConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.QueryConstraint]
- **Required**: Yes

### dimensionColumns
- **Type**: typing.Optional[typing.List[str]]


# AnalysisRuleList

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRulePolicyV1]


# AnalysisRulePolicyV1

### list
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleListOutput]

### aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleAggregationOutput]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleCustomOutput]

### idMappingTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleIdMappingTable]


# AnalysisSchema

### referencedTables
- **Type**: typing.Optional[typing.List[str]]


# AnalysisSource

### text
- **Type**: typing.Optional[str]


# AnalysisTemplate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisSchema'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplate'>>

### format
- **Type**: typing.Literal['SQL']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisSource'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### analysisParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisParameter]]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplateValidationStatusDetail]]


# AnalysisTemplateSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# AnalysisTemplateValidationStatusDetail

### type
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### status
- **Type**: typing.Literal['INVALID', 'UNABLE_TO_VALIDATE', 'VALID']
- **Required**: Yes

### reasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplateValidationStatusReason]]


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
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetCollaborationAnalysisTemplateOutput

### collaborationAnalysisTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationAnalysisTemplate]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.BatchGetCollaborationAnalysisTemplateError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetSchemaAnalysisRuleError

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetSchemaAnalysisRuleInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaAnalysisRuleRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SchemaAnalysisRuleRequest]
- **Required**: Yes


# BatchGetSchemaAnalysisRuleOutput

### analysisRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRule]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.BatchGetSchemaAnalysisRuleError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetSchemaOutput

### schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Schema]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.BatchGetSchemaError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# BilledResourceUtilization

### units
- **Type**: <class 'float'>
- **Required**: Yes


# Collaboration

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### creatorDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### memberStatus
- **Type**: typing.Literal['ACTIVE', 'INVITED', 'LEFT', 'REMOVED']
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### membershipId
- **Type**: typing.Optional[str]

### membershipArn
- **Type**: typing.Optional[str]

### dataEncryptionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DataEncryptionMetadata]

### analyticsEngine
- **Type**: typing.Optional[typing.Literal['CLEAN_ROOMS_SQL', 'SPARK']]


# CollaborationAnalysisTemplate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisSchema'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationAnalysisTemplate'>>

### format
- **Type**: typing.Literal['SQL']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisSource'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### analysisParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisParameter]]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplateValidationStatusDetail]]


# CollaborationAnalysisTemplateSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CollaborationConfiguredAudienceModelAssociation

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CollaborationConfiguredAudienceModelAssociationSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CollaborationIdNamespaceAssociation

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferenceConfig'>
- **Required**: Yes

### inputReferenceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferenceProperties'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingConfig]


# CollaborationIdNamespaceAssociationSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferenceConfig'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferencePropertiesSummary'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CollaborationPrivacyBudgetSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### budget
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudget'>
- **Required**: Yes


# CollaborationPrivacyBudgetTemplate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### autoRefresh
- **Type**: typing.Literal['CALENDAR_MONTH', 'NONE']
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplateParametersOutput'>
- **Required**: Yes


# CollaborationPrivacyBudgetTemplateSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# CollaborationSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### creatorDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### memberStatus
- **Type**: typing.Literal['ACTIVE', 'INVITED', 'LEFT', 'REMOVED']
- **Required**: Yes

### membershipId
- **Type**: typing.Optional[str]

### membershipArn
- **Type**: typing.Optional[str]

### analyticsEngine
- **Type**: typing.Optional[typing.Literal['CLEAN_ROOMS_SQL', 'SPARK']]


# Column

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes


# ComputeConfiguration

### worker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.WorkerComputeConfiguration]


# ConfigurationDetails

### directAnalysisConfigurationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DirectAnalysisConfigurationDetails]


# ConfiguredAudienceModelAssociation

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### manageResourcePolicies
- **Type**: <class 'bool'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ConfiguredAudienceModelAssociationSummary

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ConfiguredTable

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tableReference
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.TableReferenceOutput'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### analysisRuleTypes
- **Type**: typing.List[typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Literal['DIRECT_QUERY']
- **Required**: Yes

### allowedColumns
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ConfiguredTableAnalysisRule

### configuredTableId
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyOutput'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ConfiguredTableAnalysisRulePolicy

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyV1]


# ConfiguredTableAnalysisRulePolicyOutput

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyV1Output]


# ConfiguredTableAnalysisRulePolicyV1

### list
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleList]

### aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleAggregation]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleCustom]


# ConfiguredTableAnalysisRulePolicyV1Output

### list
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleListOutput]

### aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleAggregationOutput]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRuleCustomOutput]


# ConfiguredTableAssociation

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableId
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### analysisRuleTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']]]


# ConfiguredTableAssociationAnalysisRule

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyOutput'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ConfiguredTableAssociationAnalysisRuleAggregation

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleAggregationOutput

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleCustom

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleCustomOutput

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleList

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRuleListOutput

### allowedResultReceivers
- **Type**: typing.Optional[typing.List[str]]

### allowedAdditionalAnalyses
- **Type**: typing.Optional[typing.List[str]]


# ConfiguredTableAssociationAnalysisRulePolicy

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyV1]


# ConfiguredTableAssociationAnalysisRulePolicyOutput

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyV1Output]


# ConfiguredTableAssociationAnalysisRulePolicyV1

### list
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleList]

### aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleAggregation]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleCustom]


# ConfiguredTableAssociationAnalysisRulePolicyV1Output

### list
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleListOutput]

### aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleAggregationOutput]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRuleCustomOutput]


# ConfiguredTableAssociationSummary

### configuredTableId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ConfiguredTableSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### analysisRuleTypes
- **Type**: typing.List[typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Literal['DIRECT_QUERY']
- **Required**: Yes


# CreateAnalysisTemplateInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['SQL']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisSource'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### analysisParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisParameter]]


# CreateAnalysisTemplateOutput

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCollaborationInput

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MemberSpecification]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creatorMemberAbilities
- **Type**: typing.List[typing.Literal['CAN_QUERY', 'CAN_RECEIVE_RESULTS']]
- **Required**: Yes

### creatorDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### creatorMLMemberAbilities
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLMemberAbilities, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLMemberAbilitiesOutput, NoneType]

### dataEncryptionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DataEncryptionMetadata]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### creatorPaymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaymentConfiguration]

### analyticsEngine
- **Type**: typing.Optional[typing.Literal['CLEAN_ROOMS_SQL', 'SPARK']]


# CreateCollaborationOutput

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Collaboration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]

### description
- **Type**: typing.Optional[str]


# CreateConfiguredAudienceModelAssociationOutput

### configuredAudienceModelAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredTableAnalysisRuleInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRulePolicy, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyOutput]
- **Required**: Yes


# CreateConfiguredTableAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicy, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyOutput]
- **Required**: Yes


# CreateConfiguredTableAssociationAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConfiguredTableAssociationOutput

### configuredTableAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredTableInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tableReference
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.TableReference, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.TableReferenceOutput]
- **Required**: Yes

### allowedColumns
- **Type**: typing.List[str]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Literal['DIRECT_QUERY']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConfiguredTableOutput

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdMappingTableInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableInputReferenceConfig'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateIdMappingTableOutput

### idMappingTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdNamespaceAssociationInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferenceConfig'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### description
- **Type**: typing.Optional[str]

### idMappingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingConfig]


# CreateIdNamespaceAssociationOutput

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMembershipInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipProtectedQueryResultConfiguration]

### paymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipPaymentConfiguration]


# CreateMembershipOutput

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Membership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplateParametersInput'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePrivacyBudgetTemplateOutput

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyColumn]
- **Required**: Yes


# DifferentialPrivacyConfigurationOutput

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyColumn]
- **Required**: Yes


# DifferentialPrivacyParameters

### sensitivityParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacySensitivityParameters]
- **Required**: Yes


# DifferentialPrivacyPreviewAggregation

### type
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'STDDEV', 'SUM']
- **Required**: Yes

### maxCount
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPreviewParametersInput

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyBudget

### aggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyPrivacyBudgetAggregation]
- **Required**: Yes

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyBudgetAggregation

### type
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'STDDEV', 'SUM']
- **Required**: Yes

### maxCount
- **Type**: <class 'int'>
- **Required**: Yes

### remainingCount
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyImpact

### aggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyPreviewAggregation]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationAnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationIdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationOutput

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Collaboration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationPrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredTableInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredTableOutput

### configuredTable
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetMembershipInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMembershipOutput

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Membership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaAnalysisRuleInput

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']
- **Required**: Yes


# GetSchemaAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Schema'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.GetSchemaOutput'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableInputReferenceConfig'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inputReferenceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableInputReferenceProperties'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]


# IdMappingTableInputReferenceConfig

### inputReferenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### manageResourcePolicies
- **Type**: <class 'bool'>
- **Required**: Yes


# IdMappingTableInputReferenceProperties

### idMappingTableInputSource
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableInputSource]
- **Required**: Yes


# IdMappingTableInputSource

### idNamespaceAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes


# IdMappingTableSchemaTypeProperties

### idMappingTableInputSource
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableInputSource]
- **Required**: Yes


# IdMappingTableSummary

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableInputReferenceConfig'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# IdNamespaceAssociation

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferenceConfig'>
- **Required**: Yes

### inputReferenceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferenceProperties'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingConfig]


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

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferenceConfig'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### inputReferenceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationInputReferencePropertiesSummary'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListAnalysisTemplatesOutput

### analysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListCollaborationAnalysisTemplatesOutput

### collaborationAnalysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationAnalysisTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListCollaborationConfiguredAudienceModelAssociationsOutput

### collaborationConfiguredAudienceModelAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationConfiguredAudienceModelAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListCollaborationIdNamespaceAssociationsOutput

### collaborationIdNamespaceAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationIdNamespaceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListCollaborationPrivacyBudgetTemplatesOutput

### collaborationPrivacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationPrivacyBudgetTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListCollaborationPrivacyBudgetsOutput

### collaborationPrivacyBudgetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationPrivacyBudgetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListCollaborationsOutput

### collaborationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.CollaborationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListConfiguredAudienceModelAssociationsOutput

### configuredAudienceModelAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredAudienceModelAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListConfiguredTableAssociationsOutput

### configuredTableAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListConfiguredTablesOutput

### configuredTableSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListIdMappingTablesOutput

### idMappingTableSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListIdNamespaceAssociationsOutput

### idNamespaceAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListMembersOutput

### memberSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MemberSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListMembershipsOutput

### membershipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListPrivacyBudgetTemplatesOutput

### privacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListPrivacyBudgetsOutput

### privacyBudgetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListProtectedQueriesOutput

### protectedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuerySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaginatorConfig]


# ListSchemasOutput

### schemaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SchemaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# MLMemberAbilities

### customMLMemberAbilities
- **Type**: typing.List[typing.Literal['CAN_RECEIVE_INFERENCE_OUTPUT', 'CAN_RECEIVE_MODEL_OUTPUT']]
- **Required**: Yes


# MLMemberAbilitiesOutput

### customMLMemberAbilities
- **Type**: typing.List[typing.Literal['CAN_RECEIVE_INFERENCE_OUTPUT', 'CAN_RECEIVE_MODEL_OUTPUT']]
- **Required**: Yes


# MLPaymentConfig

### modelTraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ModelTrainingPaymentConfig]

### modelInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ModelInferencePaymentConfig]


# MemberSpecification

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### memberAbilities
- **Type**: typing.List[typing.Literal['CAN_QUERY', 'CAN_RECEIVE_RESULTS']]
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### mlMemberAbilities
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLMemberAbilities, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLMemberAbilitiesOutput, NoneType]

### paymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaymentConfiguration]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PaymentConfiguration'>
- **Required**: Yes

### mlAbilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLMemberAbilitiesOutput]

### membershipId
- **Type**: typing.Optional[str]

### membershipArn
- **Type**: typing.Optional[str]


# Membership

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationCreatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationCreatorDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationName
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']
- **Required**: Yes

### memberAbilities
- **Type**: typing.List[typing.Literal['CAN_QUERY', 'CAN_RECEIVE_RESULTS']]
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### paymentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipPaymentConfiguration'>
- **Required**: Yes

### mlMemberAbilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLMemberAbilitiesOutput]

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipProtectedQueryResultConfiguration]


# MembershipMLPaymentConfig

### modelTraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipModelTrainingPaymentConfig]

### modelInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipModelInferencePaymentConfig]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipQueryComputePaymentConfig'>
- **Required**: Yes

### machineLearning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipMLPaymentConfig]


# MembershipProtectedQueryOutputConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryS3OutputConfiguration]


# MembershipProtectedQueryResultConfiguration

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipProtectedQueryOutputConfiguration'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]


# MembershipQueryComputePaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# MembershipSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationCreatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationCreatorDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationName
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']
- **Required**: Yes

### memberAbilities
- **Type**: typing.List[typing.Literal['CAN_QUERY', 'CAN_RECEIVE_RESULTS']]
- **Required**: Yes

### paymentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipPaymentConfiguration'>
- **Required**: Yes

### mlMemberAbilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLMemberAbilitiesOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.QueryComputePaymentConfig'>
- **Required**: Yes

### machineLearning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MLPaymentConfig]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# PreviewPrivacyImpactInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PreviewPrivacyImpactParametersInput'>
- **Required**: Yes


# PreviewPrivacyImpactOutput

### privacyImpact
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyImpact'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# PreviewPrivacyImpactParametersInput

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyPreviewParametersInput]


# PrivacyBudget

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyPrivacyBudget]


# PrivacyBudgetSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### budget
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudget'>
- **Required**: Yes


# PrivacyBudgetTemplate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### autoRefresh
- **Type**: typing.Literal['CALENDAR_MONTH', 'NONE']
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplateParametersOutput'>
- **Required**: Yes


# PrivacyBudgetTemplateParametersInput

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyTemplateParametersInput]


# PrivacyBudgetTemplateParametersOutput

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyTemplateParametersOutput]


# PrivacyBudgetTemplateSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# PrivacyBudgetTemplateUpdateParameters

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyTemplateUpdateParameters]


# PrivacyImpact

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyPrivacyImpact]


# ProtectedQuery

### id
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'STARTED', 'SUBMITTED', 'SUCCESS', 'TIMED_OUT']
- **Required**: Yes

### sqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuerySQLParametersOutput]

### resultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryResultConfiguration]

### statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryStatistics]

### result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryResult]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryError]

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.DifferentialPrivacyParameters]

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ComputeConfiguration]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryS3Output]

### memberList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuerySingleMemberOutput]]


# ProtectedQueryOutputConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryS3OutputConfiguration]

### member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryMemberOutputConfiguration]


# ProtectedQueryResult

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryOutput'>
- **Required**: Yes


# ProtectedQueryResultConfiguration

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryOutputConfiguration'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.BilledResourceUtilization]


# ProtectedQuerySummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'STARTED', 'SUBMITTED', 'SUCCESS', 'TIMED_OUT']
- **Required**: Yes

### receiverConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ReceiverConfiguration]
- **Required**: Yes


# QueryComputePaymentConfig

### isResponsible
- **Type**: <class 'bool'>
- **Required**: Yes


# QueryConstraint

### requireOverlap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.QueryConstraintRequireOverlap]


# QueryConstraintRequireOverlap

### columns
- **Type**: typing.Optional[typing.List[str]]


# ReceiverConfiguration

### analysisType
- **Type**: typing.Literal['ADDITIONAL_ANALYSIS', 'DIRECT_ANALYSIS']
- **Required**: Yes

### configurationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfigurationDetails]


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

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Column]
- **Required**: Yes

### partitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Column]
- **Required**: Yes

### analysisRuleTypes
- **Type**: typing.List[typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']]
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ID_MAPPING_TABLE', 'TABLE']
- **Required**: Yes

### schemaStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SchemaStatusDetail]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Optional[typing.Literal['DIRECT_QUERY']]

### schemaTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SchemaTypeProperties]


# SchemaAnalysisRuleRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']
- **Required**: Yes


# SchemaStatusDetail

### status
- **Type**: typing.Literal['NOT_READY', 'READY']
- **Required**: Yes

### analysisType
- **Type**: typing.Literal['ADDITIONAL_ANALYSIS', 'DIRECT_ANALYSIS']
- **Required**: Yes

### reasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SchemaStatusReason]]

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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ID_MAPPING_TABLE', 'TABLE']
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationArn
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleTypes
- **Type**: typing.List[typing.Literal['AGGREGATION', 'CUSTOM', 'ID_MAPPING_TABLE', 'LIST']]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Optional[typing.Literal['DIRECT_QUERY']]


# SchemaTypeProperties

### idMappingTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTableSchemaTypeProperties]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SnowflakeTableSchema'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SnowflakeTableSchemaOutput'>
- **Required**: Yes


# SnowflakeTableSchema

### v1
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SnowflakeTableSchemaV1]]


# SnowflakeTableSchemaOutput

### v1
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SnowflakeTableSchemaV1]]


# SnowflakeTableSchemaV1

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnType
- **Type**: <class 'str'>
- **Required**: Yes


# StartProtectedQueryInput

### type
- **Type**: typing.Literal['SQL']
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sqlParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuerySQLParameters, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuerySQLParametersOutput]
- **Required**: Yes

### resultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQueryResultConfiguration]

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ComputeConfiguration]


# StartProtectedQueryOutput

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# TableReference

### glue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.GlueTableReference]

### snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SnowflakeTableReference]

### athena
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AthenaTableReference]


# TableReferenceOutput

### glue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.GlueTableReference]

### snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.SnowflakeTableReferenceOutput]

### athena
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AthenaTableReference]


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.AnalysisTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Collaboration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredAudienceModelAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfiguredTableAnalysisRuleInput

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRulePolicy, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyOutput]
- **Required**: Yes


# UpdateConfiguredTableAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicy, aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRulePolicyOutput]
- **Required**: Yes


# UpdateConfiguredTableAssociationAnalysisRuleOutput

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociationAnalysisRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTableAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ConfiguredTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingTable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdMappingConfig]


# UpdateIdNamespaceAssociationOutput

### idNamespaceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.IdNamespaceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMembershipInput

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryLogStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.MembershipProtectedQueryResultConfiguration]


# UpdateMembershipOutput

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.Membership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplateUpdateParameters]


# UpdatePrivacyBudgetTemplateOutput

### privacyBudgetTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.PrivacyBudgetTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ProtectedQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_classes.ResponseMetadata'>
- **Required**: Yes


# WorkerComputeConfiguration

### type
- **Type**: typing.Optional[typing.Literal['CR.1X', 'CR.4X']]

### number
- **Type**: typing.Optional[int]


