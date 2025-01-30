# cleanrooms_classes

# AggregateColumnTypeDef

### columnNames
- **Type**: typing.List[str]
- **Required**: Yes

### function
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'SUM', 'SUM_DISTINCT']
- **Required**: Yes


# AggregationConstraintTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### minimum
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: typing.Literal['COUNT_DISTINCT']
- **Required**: Yes


# AnalysisParameterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'CHAR', 'DATE', 'DECIMAL', 'DOUBLE_PRECISION', 'INTEGER', 'REAL', 'SMALLINT', 'TIME', 'TIMESTAMP', 'TIMESTAMPTZ', 'TIMETZ', 'VARBYTE', 'VARCHAR']
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[str]


# AnalysisRuleAggregationTypeDef

### aggregateColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AggregateColumnTypeDef]
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


# AnalysisRuleCustomTypeDef

### allowedAnalyses
- **Type**: typing.List[str]
- **Required**: Yes

### allowedAnalysisProviders
- **Type**: typing.Optional[typing.List[str]]

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyConfigurationTypeDef]


# AnalysisRuleListTypeDef

### joinColumns
- **Type**: typing.List[str]
- **Required**: Yes

### listColumns
- **Type**: typing.List[str]
- **Required**: Yes

### allowedJoinOperators
- **Type**: typing.Optional[typing.List[typing.Literal['AND', 'OR']]]


# AnalysisRulePolicyTypeDef

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRulePolicyV1TypeDef]


# AnalysisRulePolicyV1TypeDef

### list
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleListTypeDef]

### aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleAggregationTypeDef]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleCustomTypeDef]


# AnalysisRuleTypeDef

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRulePolicyTypeDef'>
- **Required**: Yes


# AnalysisSchemaTypeDef

### referencedTables
- **Type**: typing.Optional[typing.List[str]]


# AnalysisSourceTypeDef

### text
- **Type**: typing.Optional[str]


# AnalysisTemplateSummaryTypeDef

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


# AnalysisTemplateTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisSchemaTypeDef'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateTypeDef'>>

### format
- **Type**: typing.Literal['SQL']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisSourceTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### analysisParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisParameterTypeDef]]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateValidationStatusDetailTypeDef]]


# AnalysisTemplateValidationStatusDetailTypeDef

### type
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### status
- **Type**: typing.Literal['INVALID', 'UNABLE_TO_VALIDATE', 'VALID']
- **Required**: Yes

### reasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateValidationStatusReasonTypeDef]]


# AnalysisTemplateValidationStatusReasonTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


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


# BatchGetCollaborationAnalysisTemplateInputRequestTypeDef

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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetSchemaAnalysisRuleInputRequestTypeDef

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


# BatchGetSchemaInputRequestTypeDef

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


# CollaborationAnalysisTemplateSummaryTypeDef

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


# CollaborationAnalysisTemplateTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisSchemaTypeDef'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplateTypeDef'>>

### format
- **Type**: typing.Literal['SQL']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisSourceTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### analysisParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisParameterTypeDef]]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateValidationStatusDetailTypeDef]]


# CollaborationConfiguredAudienceModelAssociationSummaryTypeDef

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


# CollaborationConfiguredAudienceModelAssociationTypeDef

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


# CollaborationPrivacyBudgetSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTypeDef'>
- **Required**: Yes


# CollaborationPrivacyBudgetTemplateSummaryTypeDef

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


# CollaborationPrivacyBudgetTemplateTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateParametersOutputTypeDef'>
- **Required**: Yes


# CollaborationSummaryTypeDef

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


# CollaborationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DataEncryptionMetadataTypeDef]


# ColumnTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes


# ConfiguredAudienceModelAssociationSummaryTypeDef

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


# ConfiguredAudienceModelAssociationTypeDef

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


# ConfiguredTableAnalysisRulePolicyTypeDef

### v1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyV1TypeDef]


# ConfiguredTableAnalysisRulePolicyV1TypeDef

### list
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleListTypeDef]

### aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleAggregationTypeDef]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleCustomTypeDef]


# ConfiguredTableAnalysisRuleTypeDef

### configuredTableId
- **Type**: <class 'str'>
- **Required**: Yes

### configuredTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyTypeDef'>
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


# ConfiguredTableAssociationSummaryTypeDef

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


# ConfiguredTableAssociationTypeDef

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


# ConfiguredTableSummaryTypeDef

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


# ConfiguredTableTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.TableReferenceTypeDef'>
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


# CreateAnalysisTemplateInputRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisSourceTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### analysisParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisParameterTypeDef]]


# CreateAnalysisTemplateOutputTypeDef

### analysisTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCollaborationInputRequestTypeDef

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

### dataEncryptionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DataEncryptionMetadataTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### creatorPaymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaymentConfigurationTypeDef]


# CreateCollaborationOutputTypeDef

### collaboration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredAudienceModelAssociationInputRequestTypeDef

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


# CreateConfiguredTableAnalysisRuleInputRequestTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyTypeDef'>
- **Required**: Yes


# CreateConfiguredTableAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredTableAssociationInputRequestTypeDef

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


# CreateConfiguredTableInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tableReference
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.TableReferenceTypeDef'>
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


# CreateMembershipInputRequestTypeDef

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


# CreatePrivacyBudgetTemplateInputRequestTypeDef

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


# DeleteAnalysisTemplateInputRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCollaborationInputRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelAssociationInputRequestTypeDef

### configuredAudienceModelAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredTableAnalysisRuleInputRequestTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# DeleteConfiguredTableAssociationInputRequestTypeDef

### configuredTableAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredTableInputRequestTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMemberInputRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMembershipInputRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrivacyBudgetTemplateInputRequestTypeDef

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


# DifferentialPrivacyConfigurationTypeDef

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyColumnTypeDef]
- **Required**: Yes


# DifferentialPrivacyParametersTypeDef

### sensitivityParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacySensitivityParametersTypeDef]
- **Required**: Yes


# DifferentialPrivacyPreviewAggregationTypeDef

### type
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'STDDEV', 'SUM']
- **Required**: Yes

### maxCount
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPreviewParametersInputTypeDef

### epsilon
- **Type**: <class 'int'>
- **Required**: Yes

### usersNoisePerQuery
- **Type**: <class 'int'>
- **Required**: Yes


# DifferentialPrivacyPrivacyBudgetAggregationTypeDef

### type
- **Type**: typing.Literal['AVG', 'COUNT', 'COUNT_DISTINCT', 'STDDEV', 'SUM']
- **Required**: Yes

### maxCount
- **Type**: <class 'int'>
- **Required**: Yes

### remainingCount
- **Type**: <class 'int'>
- **Required**: Yes


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


# GetAnalysisTemplateInputRequestTypeDef

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


# GetCollaborationAnalysisTemplateInputRequestTypeDef

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


# GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef

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


# GetCollaborationInputRequestTypeDef

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


# GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef

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


# GetConfiguredAudienceModelAssociationInputRequestTypeDef

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


# GetConfiguredTableAnalysisRuleInputRequestTypeDef

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


# GetConfiguredTableAssociationInputRequestTypeDef

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


# GetConfiguredTableInputRequestTypeDef

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


# GetMembershipInputRequestTypeDef

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


# GetPrivacyBudgetTemplateInputRequestTypeDef

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


# GetProtectedQueryInputRequestTypeDef

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


# GetSchemaAnalysisRuleInputRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# GetSchemaAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaInputRequestTypeDef

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


# ListAnalysisTemplatesInputListAnalysisTemplatesPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListAnalysisTemplatesInputRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAnalysisTemplatesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### analysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.AnalysisTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCollaborationAnalysisTemplatesInputRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationAnalysisTemplatesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationAnalysisTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationAnalysisTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCollaborationConfiguredAudienceModelAssociationsInputListCollaborationConfiguredAudienceModelAssociationsPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCollaborationPrivacyBudgetTemplatesInputListCollaborationPrivacyBudgetTemplatesPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationPrivacyBudgetTemplatesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationPrivacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationPrivacyBudgetTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCollaborationPrivacyBudgetsInputListCollaborationPrivacyBudgetsPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationPrivacyBudgetsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCollaborationsInputListCollaborationsPaginateTypeDef

### memberStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INVITED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListCollaborationsInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### memberStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INVITED']]


# ListCollaborationsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.CollaborationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConfiguredAudienceModelAssociationsInputListConfiguredAudienceModelAssociationsPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListConfiguredAudienceModelAssociationsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConfiguredTableAssociationsInputListConfiguredTableAssociationsPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListConfiguredTableAssociationsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConfiguredTablesInputListConfiguredTablesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListConfiguredTablesInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredTablesOutputTypeDef

### configuredTableSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMembersInputListMembersPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListMembersInputRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMembersOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### memberSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.MemberSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMembershipsInputListMembershipsPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListMembershipsInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COLLABORATION_DELETED', 'REMOVED']]


# ListMembershipsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### membershipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrivacyBudgetTemplatesInputListPrivacyBudgetTemplatesPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListPrivacyBudgetTemplatesInputRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrivacyBudgetTemplatesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrivacyBudgetsInputListPrivacyBudgetsPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### privacyBudgetType
- **Type**: typing.Literal['DIFFERENTIAL_PRIVACY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListPrivacyBudgetsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProtectedQueriesInputListProtectedQueriesPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'STARTED', 'SUBMITTED', 'SUCCESS', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListProtectedQueriesInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### protectedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuerySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchemasInputListSchemasPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaType
- **Type**: typing.Optional[typing.Literal['TABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.PaginatorConfigTypeDef]


# ListSchemasInputRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### schemaType
- **Type**: typing.Optional[typing.Literal['TABLE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSchemasOutputTypeDef

### schemaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

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

### membershipId
- **Type**: typing.Optional[str]

### membershipArn
- **Type**: typing.Optional[str]


# MembershipPaymentConfigurationTypeDef

### queryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipQueryComputePaymentConfigTypeDef'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipPaymentConfigurationTypeDef'>
- **Required**: Yes


# MembershipTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipPaymentConfigurationTypeDef'>
- **Required**: Yes

### defaultResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.MembershipProtectedQueryResultConfigurationTypeDef]


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


# PreviewPrivacyImpactInputRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTypeDef'>
- **Required**: Yes


# PrivacyBudgetTemplateParametersInputTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateParametersInputTypeDef]


# PrivacyBudgetTemplateParametersOutputTypeDef

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyTemplateParametersOutputTypeDef]


# PrivacyBudgetTemplateSummaryTypeDef

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


# PrivacyBudgetTemplateTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.PrivacyBudgetTemplateParametersOutputTypeDef'>
- **Required**: Yes


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


# ProtectedQueryOutputConfigurationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryS3OutputConfigurationTypeDef]


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


# ProtectedQueryS3OutputTypeDef

### location
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQuerySQLParametersTypeDef

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProtectedQuerySingleMemberOutputTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# ProtectedQueryStatisticsTypeDef

### totalDurationInMillis
- **Type**: typing.Optional[int]


# ProtectedQuerySummaryTypeDef

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


# ProtectedQueryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuerySQLParametersTypeDef]

### resultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryResultConfigurationTypeDef]

### statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryStatisticsTypeDef]

### result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryResultTypeDef]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryErrorTypeDef]

### differentialPrivacy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.DifferentialPrivacyParametersTypeDef]


# QueryComputePaymentConfigTypeDef

### isResponsible
- **Type**: <class 'bool'>
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


# SchemaAnalysisRuleRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes


# SchemaStatusDetailTypeDef

### status
- **Type**: typing.Literal['NOT_READY', 'READY']
- **Required**: Yes

### reasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaStatusReasonTypeDef]]

### analysisRuleType
- **Type**: typing.Optional[typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']]

### configurations
- **Type**: typing.Optional[typing.List[typing.Literal['DIFFERENTIAL_PRIVACY']]]


# SchemaStatusReasonTypeDef

### code
- **Type**: typing.Literal['ANALYSIS_PROVIDERS_NOT_CONFIGURED', 'ANALYSIS_RULE_MISSING', 'ANALYSIS_TEMPLATES_NOT_CONFIGURED', 'DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaSummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TABLE']
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
- **Type**: typing.List[typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Optional[typing.Literal['DIRECT_QUERY']]


# SchemaTypeDef

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ColumnTypeDef]
- **Required**: Yes

### partitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.ColumnTypeDef]
- **Required**: Yes

### analysisRuleTypes
- **Type**: typing.List[typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']]
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
- **Type**: typing.Literal['TABLE']
- **Required**: Yes

### schemaStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanrooms_classes.SchemaStatusDetailTypeDef]
- **Required**: Yes

### analysisMethod
- **Type**: typing.Optional[typing.Literal['DIRECT_QUERY']]


# StartProtectedQueryInputRequestTypeDef

### type
- **Type**: typing.Literal['SQL']
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sqlParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQuerySQLParametersTypeDef'>
- **Required**: Yes

### resultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryResultConfigurationTypeDef]


# StartProtectedQueryOutputTypeDef

### protectedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ProtectedQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TableReferenceTypeDef

### glue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanrooms_classes.GlueTableReferenceTypeDef]


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnalysisTemplateInputRequestTypeDef

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


# UpdateCollaborationInputRequestTypeDef

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


# UpdateConfiguredAudienceModelAssociationInputRequestTypeDef

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


# UpdateConfiguredTableAnalysisRuleInputRequestTypeDef

### configuredTableIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### analysisRuleType
- **Type**: typing.Literal['AGGREGATION', 'CUSTOM', 'LIST']
- **Required**: Yes

### analysisRulePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRulePolicyTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableAnalysisRuleOutputTypeDef

### analysisRule
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ConfiguredTableAnalysisRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanrooms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfiguredTableAssociationInputRequestTypeDef

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


# UpdateConfiguredTableInputRequestTypeDef

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


# UpdateMembershipInputRequestTypeDef

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


# UpdatePrivacyBudgetTemplateInputRequestTypeDef

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


# UpdateProtectedQueryInputRequestTypeDef

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


