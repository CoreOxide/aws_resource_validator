# Connectcases Classes

# AuditEventFieldTypeDef

### eventFieldId
- **Type**: <class 'str'>
- **Required**: Yes

### newValue
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.AuditEventFieldValueUnionTypeDef'>
- **Required**: Yes

### oldValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.AuditEventFieldValueUnionTypeDef]


# AuditEventFieldValueUnionTypeDef

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### emptyValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### stringValue
- **Type**: typing.Optional[str]

### userArnValue
- **Type**: typing.Optional[str]


# AuditEventPerformedByTypeDef

### iamPrincipalArn
- **Type**: <class 'str'>
- **Required**: Yes

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnionTypeDef]


# AuditEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicLayoutOutputTypeDef

### moreInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSectionsOutputTypeDef]

### topPanel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSectionsOutputTypeDef]


# BasicLayoutTypeDef

### moreInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSectionsTypeDef]

### topPanel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSectionsTypeDef]


# BatchGetCaseRuleRequestTypeDef

### caseRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleIdentifierTypeDef]
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCaseRuleResponseTypeDef

### caseRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.GetCaseRuleResponseTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetFieldRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]
- **Required**: Yes


# BatchGetFieldResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldErrorTypeDef]
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.GetFieldResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutFieldOptionsRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldOptionTypeDef]
- **Required**: Yes


# BatchPutFieldOptionsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldOptionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BooleanConditionOutputTypeDef

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperandsOutputTypeDef]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperandsOutputTypeDef]


# BooleanConditionTypeDef

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperandsTypeDef]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperandsTypeDef]


# BooleanOperandsOutputTypeDef

### operandOne
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandOneTypeDef'>
- **Required**: Yes

### operandTwo
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandTwoOutputTypeDef'>
- **Required**: Yes

### result
- **Type**: <class 'bool'>
- **Required**: Yes


# BooleanOperandsTypeDef

### operandOne
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandOneTypeDef'>
- **Required**: Yes

### operandTwo
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandTwoTypeDef'>
- **Required**: Yes

### result
- **Type**: <class 'bool'>
- **Required**: Yes


# CaseEventIncludedDataOutputTypeDef

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]
- **Required**: Yes


# CaseEventIncludedDataTypeDef

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]
- **Required**: Yes


# CaseRuleDetailsOutputTypeDef

### required
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RequiredCaseRuleOutputTypeDef]


# CaseRuleDetailsTypeDef

### required
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RequiredCaseRuleTypeDef]


# CaseRuleDetailsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseRuleErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseRuleIdentifierTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseRuleSummaryTypeDef

### caseRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ruleType
- **Type**: typing.Literal['Required']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CaseSummaryTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes


# CommentContentTypeDef

### body
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Literal['Text/Plain']
- **Required**: Yes


# ContactContentTypeDef

### channel
- **Type**: <class 'str'>
- **Required**: Yes

### connectedToSystemTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### contactArn
- **Type**: <class 'str'>
- **Required**: Yes


# ContactFilterTypeDef

### channel
- **Type**: typing.Optional[typing.Sequence[str]]

### contactArn
- **Type**: typing.Optional[str]


# ContactTypeDef

### contactArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCaseRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnionTypeDef]


# CreateCaseResponseTypeDef

### caseArn
- **Type**: <class 'str'>
- **Required**: Yes

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCaseRuleRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleDetailsUnionTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateCaseRuleResponseTypeDef

### caseRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDomainResponseTypeDef

### domainArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### domainStatus
- **Type**: typing.Literal['Active', 'CreationFailed', 'CreationInProgress']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFieldResponseTypeDef

### fieldArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLayoutRequestTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentUnionTypeDef'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateLayoutResponseTypeDef

### layoutArn
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRelatedItemResponseTypeDef

### relatedItemArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedItemId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTemplateRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### layoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutConfigurationTypeDef]

### requiredFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RequiredFieldTypeDef]]

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.TemplateRuleTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# CreateTemplateResponseTypeDef

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCaseRuleRequestTypeDef

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFieldRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLayoutRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes


# DomainSummaryTypeDef

### domainArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventBridgeConfigurationOutputTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.EventIncludedDataOutputTypeDef]


# EventBridgeConfigurationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.EventIncludedDataTypeDef]


# EventBridgeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventIncludedDataOutputTypeDef

### caseData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CaseEventIncludedDataOutputTypeDef]

### relatedItemData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemEventIncludedDataTypeDef]


# EventIncludedDataTypeDef

### caseData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CaseEventIncludedDataTypeDef]

### relatedItemData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemEventIncludedDataTypeDef]


# FieldErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldFilterTypeDef

### contains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]

### greaterThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]

### lessThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]


# FieldGroupOutputTypeDef

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldItemTypeDef]
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# FieldGroupTypeDef

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldItemTypeDef]
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# FieldIdentifierTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldOptionErrorTypeDef

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# FieldOptionTypeDef

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# FieldSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValueOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValueUnionExtraTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValueUnionOutputTypeDef

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### emptyValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### stringValue
- **Type**: typing.Optional[str]

### userArnValue
- **Type**: typing.Optional[str]


# FieldValueUnionTypeDef

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### emptyValue
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### stringValue
- **Type**: typing.Optional[str]

### userArnValue
- **Type**: typing.Optional[str]


# FileContentTypeDef

### fileArn
- **Type**: <class 'str'>
- **Required**: Yes


# FileFilterTypeDef

### fileArn
- **Type**: typing.Optional[str]


# GetCaseAuditEventsRequestTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetCaseAuditEventsResponseTypeDef

### auditEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.AuditEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseEventConfigurationRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCaseEventConfigurationResponseTypeDef

### eventBridge
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.EventBridgeConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCaseRequestTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseResponseTypeDef

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueOutputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseRuleResponseTypeDef

### caseRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleDetailsOutputTypeDef'>
- **Required**: Yes

### createdTime
- **Type**: typing.Optional[datetime.datetime]

### deleted
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### lastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetDomainRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainResponseTypeDef

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### domainArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### domainStatus
- **Type**: typing.Literal['Active', 'CreationFailed', 'CreationInProgress']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFieldResponseTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetLayoutRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLayoutResponseTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentOutputTypeDef'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deleted
- **Type**: <class 'bool'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### layoutArn
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateResponseTypeDef

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deleted
- **Type**: <class 'bool'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### layoutConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.LayoutConfigurationTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### requiredFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.RequiredFieldTypeDef]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.TemplateRuleTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LayoutConfigurationTypeDef

### defaultLayout
- **Type**: typing.Optional[str]


# LayoutContentOutputTypeDef

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BasicLayoutOutputTypeDef]


# LayoutContentTypeDef

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BasicLayoutTypeDef]


# LayoutContentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LayoutSectionsOutputTypeDef

### sections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases_classes.SectionOutputTypeDef]]


# LayoutSectionsTypeDef

### sections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.SectionTypeDef]]


# LayoutSummaryTypeDef

### layoutArn
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ListCaseRulesRequestPaginateTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.PaginatorConfigTypeDef]


# ListCaseRulesRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCaseRulesResponseTypeDef

### caseRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCasesForContactRequestTypeDef

### contactArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCasesForContactResponseTypeDef

### cases
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.CaseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsResponseTypeDef

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.DomainSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFieldOptionsRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# ListFieldOptionsResponseTypeDef

### options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldOptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFieldsRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFieldsResponseTypeDef

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLayoutsRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLayoutsResponseTypeDef

### layouts
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplatesRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'Inactive']]]


# ListTemplatesResponseTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# OperandOneTypeDef

### fieldId
- **Type**: typing.Optional[str]


# OperandTwoOutputTypeDef

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### emptyValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### stringValue
- **Type**: typing.Optional[str]


# OperandTwoTypeDef

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### emptyValue
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### stringValue
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutCaseEventConfigurationRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### eventBridge
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.EventBridgeConfigurationUnionTypeDef'>
- **Required**: Yes


# RelatedItemContentTypeDef

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CommentContentTypeDef]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.ContactContentTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FileContentTypeDef]


# RelatedItemEventIncludedDataTypeDef

### includeContent
- **Type**: <class 'bool'>
- **Required**: Yes


# RelatedItemInputContentTypeDef

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CommentContentTypeDef]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.ContactTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FileContentTypeDef]


# RelatedItemTypeFilterTypeDef

### comment
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.ContactFilterTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FileFilterTypeDef]


# RequiredCaseRuleOutputTypeDef

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.BooleanConditionOutputTypeDef]
- **Required**: Yes

### defaultValue
- **Type**: <class 'bool'>
- **Required**: Yes


# RequiredCaseRuleTypeDef

### conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.BooleanConditionTypeDef]
- **Required**: Yes

### defaultValue
- **Type**: <class 'bool'>
- **Required**: Yes


# RequiredFieldTypeDef

### fieldId
- **Type**: <class 'str'>
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


# SearchCasesResponseItemTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueOutputTypeDef]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SearchCasesResponseTypeDef

### cases
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.SearchCasesResponseItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchRelatedItemsRequestPaginateTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemTypeFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.PaginatorConfigTypeDef]


# SearchRelatedItemsRequestTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemTypeFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchRelatedItemsResponseItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchRelatedItemsResponseTypeDef

### relatedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.SearchRelatedItemsResponseItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SectionOutputTypeDef

### fieldGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldGroupOutputTypeDef]


# SectionTypeDef

### fieldGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldGroupTypeDef]


# SortTypeDef

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Literal['Asc', 'Desc']
- **Required**: Yes


# TagResourceRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateRuleTypeDef

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateSummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCaseRequestTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraTypeDef]
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnionTypeDef]


# UpdateCaseRuleRequestTypeDef

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### rule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleDetailsUnionTypeDef]


# UpdateFieldRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateLayoutRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentUnionTypeDef]

### name
- **Type**: typing.Optional[str]


# UpdateTemplateRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### layoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutConfigurationTypeDef]

### name
- **Type**: typing.Optional[str]

### requiredFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RequiredFieldTypeDef]]

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.TemplateRuleTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UserUnionTypeDef

### userArn
- **Type**: typing.Optional[str]


