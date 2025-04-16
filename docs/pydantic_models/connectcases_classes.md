# Connectcases Classes

# AuditEvent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuditEventField

### eventFieldId
- **Type**: <class 'str'>
- **Required**: Yes

### newValue
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.AuditEventFieldValueUnion'>
- **Required**: Yes

### oldValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.AuditEventFieldValueUnion]


# AuditEventFieldValueUnion

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


# AuditEventPerformedBy

### iamPrincipalArn
- **Type**: <class 'str'>
- **Required**: Yes

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnion]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicLayout

### moreInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSections]

### topPanel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSections]


# BasicLayoutOutput

### moreInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSectionsOutput]

### topPanel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSectionsOutput]


# BatchGetCaseRuleRequest

### caseRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleIdentifier]
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCaseRuleResponse

### caseRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.GetCaseRuleResponse]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetFieldRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifier]
- **Required**: Yes


# BatchGetFieldResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldError]
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.GetFieldResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutFieldOptionsRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldOption]
- **Required**: Yes


# BatchPutFieldOptionsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldOptionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# BooleanCondition

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperands]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperands]


# BooleanConditionOutput

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperandsOutput]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BooleanOperandsOutput]


# BooleanOperands

### operandOne
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandOne'>
- **Required**: Yes

### operandTwo
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandTwo'>
- **Required**: Yes

### result
- **Type**: <class 'bool'>
- **Required**: Yes


# BooleanOperandsOutput

### operandOne
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandOne'>
- **Required**: Yes

### operandTwo
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.OperandTwoOutput'>
- **Required**: Yes

### result
- **Type**: <class 'bool'>
- **Required**: Yes


# CaseEventIncludedData

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifier]
- **Required**: Yes


# CaseEventIncludedDataOutput

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifier]
- **Required**: Yes


# CaseRuleDetails

### required
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RequiredCaseRule]


# CaseRuleDetailsOutput

### required
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RequiredCaseRuleOutput]


# CaseRuleDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseRuleError

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseRuleIdentifier

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaseRuleSummary

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


# CaseSummary

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes


# CommentContent

### body
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Literal['Text/Plain']
- **Required**: Yes


# Contact

### contactArn
- **Type**: <class 'str'>
- **Required**: Yes


# ContactContent

### channel
- **Type**: <class 'str'>
- **Required**: Yes

### connectedToSystemTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### contactArn
- **Type**: <class 'str'>
- **Required**: Yes


# ContactFilter

### channel
- **Type**: typing.Optional[typing.Sequence[str]]

### contactArn
- **Type**: typing.Optional[str]


# CreateCaseRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnion]


# CreateCaseResponse

### caseArn
- **Type**: <class 'str'>
- **Required**: Yes

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCaseRuleRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleDetailsUnion'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateCaseRuleResponse

### caseRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDomainResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFieldResponse

### fieldArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLayoutRequest

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentUnion'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateLayoutResponse

### layoutArn
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRelatedItemResponse

### relatedItemArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedItemId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTemplateRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### layoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutConfiguration]

### requiredFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RequiredField]]

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.TemplateRule]]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# CreateTemplateResponse

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCaseRuleRequest

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFieldRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLayoutRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes


# DomainSummary

### domainArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# EventBridgeConfiguration

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.EventIncludedData]


# EventBridgeConfigurationOutput

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.EventIncludedDataOutput]


# EventBridgeConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventIncludedData

### caseData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CaseEventIncludedData]

### relatedItemData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemEventIncludedData]


# EventIncludedDataOutput

### caseData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CaseEventIncludedDataOutput]

### relatedItemData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemEventIncludedData]


# FieldError

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldFilter

### contains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]

### greaterThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]

### lessThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]


# FieldGroup

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldItem]
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# FieldGroupOutput

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldItem]
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# FieldIdentifier

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldOption

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# FieldOptionError

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# FieldSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValueOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValueUnion

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


# FieldValueUnionExtra

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValueUnionOutput

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


# FileContent

### fileArn
- **Type**: <class 'str'>
- **Required**: Yes


# FileFilter

### fileArn
- **Type**: typing.Optional[str]


# GetCaseAuditEventsRequest

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


# GetCaseAuditEventsResponse

### auditEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.AuditEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseEventConfigurationRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCaseEventConfigurationResponse

### eventBridge
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.EventBridgeConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# GetCaseRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifier]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseResponse

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueOutput]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleDetailsOutput'>
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


# GetDomainRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# GetFieldResponse

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetLayoutRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLayoutResponse

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.LayoutConfiguration'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### requiredFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.RequiredField]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.TemplateRule]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# LayoutConfiguration

### defaultLayout
- **Type**: typing.Optional[str]


# LayoutContent

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BasicLayout]


# LayoutContentOutput

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.BasicLayoutOutput]


# LayoutContentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LayoutSections

### sections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.Section]]


# LayoutSectionsOutput

### sections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases_classes.SectionOutput]]


# LayoutSummary

### layoutArn
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ListCaseRulesRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCaseRulesRequestPaginate

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.PaginatorConfig]


# ListCaseRulesResponse

### caseRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCasesForContactRequest

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


# ListCasesForContactResponse

### cases
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.CaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsResponse

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.DomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFieldOptionsRequest

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


# ListFieldOptionsResponse

### options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldOption]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFieldsRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFieldsResponse

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLayoutsRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLayoutsResponse

### layouts
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.LayoutSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplatesRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'Inactive']]]


# ListTemplatesResponse

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.TemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# OperandOne

### fieldId
- **Type**: typing.Optional[str]


# OperandTwo

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### emptyValue
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### stringValue
- **Type**: typing.Optional[str]


# OperandTwoOutput

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### emptyValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### stringValue
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutCaseEventConfigurationRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### eventBridge
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.EventBridgeConfigurationUnion'>
- **Required**: Yes


# RelatedItemContent

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CommentContent]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.ContactContent]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FileContent]


# RelatedItemEventIncludedData

### includeContent
- **Type**: <class 'bool'>
- **Required**: Yes


# RelatedItemInputContent

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CommentContent]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.Contact]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FileContent]


# RelatedItemTypeFilter

### comment
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.ContactFilter]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FileFilter]


# RequiredCaseRule

### conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.BooleanCondition]
- **Required**: Yes

### defaultValue
- **Type**: <class 'bool'>
- **Required**: Yes


# RequiredCaseRuleOutput

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.BooleanConditionOutput]
- **Required**: Yes

### defaultValue
- **Type**: <class 'bool'>
- **Required**: Yes


# RequiredField

### fieldId
- **Type**: <class 'str'>
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


# SearchCasesResponse

### cases
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.SearchCasesResponseItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchCasesResponseItem

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueOutput]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SearchRelatedItemsRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemTypeFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchRelatedItemsRequestPaginate

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemTypeFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.PaginatorConfig]


# SearchRelatedItemsResponse

### relatedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.SearchRelatedItemsResponseItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchRelatedItemsResponseItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Section

### fieldGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldGroup]


# SectionOutput

### fieldGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldGroupOutput]


# Sort

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Literal['Asc', 'Desc']
- **Required**: Yes


# TagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateRule

### caseRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateSummary

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


# UntagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCaseRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtra]
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnion]


# UpdateCaseRuleRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CaseRuleDetailsUnion]


# UpdateFieldRequest

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


# UpdateLayoutRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentUnion]

### name
- **Type**: typing.Optional[str]


# UpdateTemplateRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### layoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutConfiguration]

### name
- **Type**: typing.Optional[str]

### requiredFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.RequiredField]]

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.TemplateRule]]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UserUnion

### userArn
- **Type**: typing.Optional[str]


