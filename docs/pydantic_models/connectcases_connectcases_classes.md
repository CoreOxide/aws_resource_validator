# Connectcases Connectcases Classes

# AuditEvent

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.AuditEventField]
- **Required**: Yes

### performedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Case.Created', 'Case.Updated', 'RelatedItem.Created']
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.AuditEventPerformedBy]

### relatedItemType
- **Type**: typing.Optional[typing.Literal['Comment', 'Contact', 'File']]


# AuditEventField

### eventFieldId
- **Type**: <class 'str'>
- **Required**: Yes

### newValue
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.AuditEventFieldValueUnion'>
- **Required**: Yes

### oldValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.AuditEventFieldValueUnion]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.UserUnion]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicLayout

### moreInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutSections]

### topPanel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutSections]


# BasicLayoutOutput

### moreInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutSectionsOutput]

### topPanel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutSectionsOutput]


# BatchGetCaseRuleRequest

### caseRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleIdentifier]
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCaseRuleResponse

### caseRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.GetCaseRuleResponse]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetFieldRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldIdentifier]
- **Required**: Yes


# BatchGetFieldResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldError]
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.GetFieldResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutFieldOptionsRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldOption]
- **Required**: Yes


# BatchPutFieldOptionsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldOptionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# BooleanCondition

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BooleanOperands]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BooleanOperands]


# BooleanConditionOutput

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BooleanOperandsOutput]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BooleanOperandsOutput]


# BooleanOperands

### operandOne
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.OperandOne'>
- **Required**: Yes

### operandTwo
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.OperandTwo'>
- **Required**: Yes

### result
- **Type**: <class 'bool'>
- **Required**: Yes


# BooleanOperandsOutput

### operandOne
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.OperandOne'>
- **Required**: Yes

### operandTwo
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.OperandTwoOutput'>
- **Required**: Yes

### result
- **Type**: <class 'bool'>
- **Required**: Yes


# CaseEventIncludedData

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldIdentifier]
- **Required**: Yes


# CaseEventIncludedDataOutput

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldIdentifier]
- **Required**: Yes


# CaseFilter

### andAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### field
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldFilter]

### not_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### orAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# CaseFilterPaginator

### andAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### field
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldFilter]

### not_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### orAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# CaseRuleDetails

### required
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RequiredCaseRule]


# CaseRuleDetailsOutput

### required
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RequiredCaseRuleOutput]


# CaseRuleError

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# CaseRuleIdentifier

### id
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[str]]

### contactArn
- **Type**: typing.Optional[str]


# CreateCaseRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput]]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.UserUnion]


# CreateCaseResponse

### caseArn
- **Type**: <class 'str'>
- **Required**: Yes

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCaseRuleRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleDetails, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleDetailsOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFieldRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Boolean', 'DateTime', 'Number', 'SingleSelect', 'Text', 'Url', 'User']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateFieldResponse

### fieldArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLayoutRequest

### content
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutContent, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutContentOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRelatedItemRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RelatedItemInputContent'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Comment', 'Contact', 'File']
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.UserUnion]


# CreateRelatedItemResponse

### relatedItemArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedItemId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutConfiguration]

### requiredFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RequiredField]]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.TemplateRule]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# EventBridgeConfiguration

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.EventIncludedData]


# EventBridgeConfigurationOutput

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.EventIncludedDataOutput]


# EventIncludedData

### caseData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseEventIncludedData]

### relatedItemData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RelatedItemEventIncludedData]


# EventIncludedDataOutput

### caseData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseEventIncludedDataOutput]

### relatedItemData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RelatedItemEventIncludedData]


# FieldError

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# FieldFilter

### contains
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput, NoneType]

### equalTo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput, NoneType]

### greaterThan
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput, NoneType]

### greaterThanOrEqualTo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput, NoneType]

### lessThan
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput, NoneType]

### lessThanOrEqualTo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput, NoneType]


# FieldGroup

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldItem]
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# FieldGroupOutput

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldItem]
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# FieldIdentifier

### id
- **Type**: <class 'str'>
- **Required**: Yes


# FieldItem

### id
- **Type**: <class 'str'>
- **Required**: Yes


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

### fieldArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Literal['Custom', 'System']
- **Required**: Yes

### type
- **Type**: typing.Literal['Boolean', 'DateTime', 'Number', 'SingleSelect', 'Text', 'Url', 'User']
- **Required**: Yes


# FieldValue

### id
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueUnion, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueUnionOutput]
- **Required**: Yes


# FieldValueOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueUnionOutput'>
- **Required**: Yes


# FieldValueUnion

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.AuditEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseEventConfigurationRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCaseEventConfigurationResponse

### eventBridge
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.EventBridgeConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# GetCaseRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldIdentifier]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCaseResponse

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleDetailsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# GetFieldResponse

### fieldArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Literal['Custom', 'System']
- **Required**: Yes

### type
- **Type**: typing.Literal['Boolean', 'DateTime', 'Number', 'SingleSelect', 'Text', 'Url', 'User']
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


# GetLayoutRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLayoutResponse

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutContentOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutConfiguration'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### requiredFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RequiredField]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.TemplateRule]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes


# LayoutConfiguration

### defaultLayout
- **Type**: typing.Optional[str]


# LayoutContent

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BasicLayout]


# LayoutContentOutput

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BasicLayoutOutput]


# LayoutSections

### sections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.Section]]


# LayoutSectionsOutput

### sections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.SectionOutput]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.PaginatorConfig]


# ListCaseRulesResponse

### caseRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.DomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[str]]


# ListFieldOptionsResponse

### options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldOption]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'Inactive']]]


# ListTemplatesResponse

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.TemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.EventBridgeConfiguration, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.EventBridgeConfigurationOutput]
- **Required**: Yes


# RelatedItemContent

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CommentContent]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ContactContent]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FileContent]


# RelatedItemEventIncludedData

### includeContent
- **Type**: <class 'bool'>
- **Required**: Yes


# RelatedItemInputContent

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CommentContent]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.Contact]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FileContent]


# RelatedItemTypeFilter

### comment
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### contact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ContactFilter]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FileFilter]


# RequiredCaseRule

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BooleanCondition]
- **Required**: Yes

### defaultValue
- **Type**: <class 'bool'>
- **Required**: Yes


# RequiredCaseRuleOutput

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.BooleanConditionOutput]
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


# SearchCasesRequest

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldIdentifier]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseFilter]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchTerm
- **Type**: typing.Optional[str]

### sorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.Sort]]


# SearchCasesRequestPaginate

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldIdentifier]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseFilterPaginator]

### searchTerm
- **Type**: typing.Optional[str]

### sorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.Sort]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.PaginatorConfig]


# SearchCasesResponse

### cases
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.SearchCasesResponseItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchCasesResponseItem

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RelatedItemTypeFilter]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RelatedItemTypeFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.PaginatorConfig]


# SearchRelatedItemsResponse

### relatedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.SearchRelatedItemsResponseItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchRelatedItemsResponseItem

### associationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RelatedItemContent'>
- **Required**: Yes

### relatedItemId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Comment', 'Contact', 'File']
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.UserUnion]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# Section

### fieldGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldGroup]


# SectionOutput

### fieldGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldGroupOutput]


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
- **Type**: typing.Dict[str, str]
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
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCaseRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValue, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.FieldValueOutput]]
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.UserUnion]


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleDetails, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.CaseRuleDetailsOutput, NoneType]


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutContent, aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutContentOutput, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.LayoutConfiguration]

### name
- **Type**: typing.Optional[str]

### requiredFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.RequiredField]]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcases.connectcases_classes.TemplateRule]]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UserUnion

### userArn
- **Type**: typing.Optional[str]


