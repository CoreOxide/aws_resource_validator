# connectcases_classes

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

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.AuditEventFieldTypeDef]
- **Required**: Yes

### performedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Case.Created', 'Case.Updated', 'RelatedItem.Created']
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.AuditEventPerformedByTypeDef]

### relatedItemType
- **Type**: typing.Optional[typing.Literal['Comment', 'Contact', 'File']]


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


# BatchGetFieldRequestRequestTypeDef

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


# BatchPutFieldOptionsRequestRequestTypeDef

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


# CaseEventIncludedDataOutputTypeDef

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]
- **Required**: Yes


# CaseEventIncludedDataTypeDef

### fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]
- **Required**: Yes


# CaseFilterTypeDef

### andAll
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### field
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldFilterTypeDef]

### orAll
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]


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


# CreateCaseRequestRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef, aws_resource_validator.pydantic_models.connectcases_classes.FieldValueExtraOutputTypeDef]]
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


# CreateDomainRequestRequestTypeDef

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


# CreateFieldRequestRequestTypeDef

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


# CreateLayoutRequestRequestTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentTypeDef'>
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


# CreateRelatedItemRequestRequestTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemInputContentTypeDef'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Comment', 'Contact', 'File']
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnionTypeDef]


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


# CreateTemplateRequestRequestTypeDef

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


# DeleteDomainRequestRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFieldRequestRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fieldId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLayoutRequestRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateRequestRequestTypeDef

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

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# FieldFilterTypeDef

### contains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef]

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef]

### greaterThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef]

### lessThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef]


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

### id
- **Type**: <class 'str'>
- **Required**: Yes


# FieldItemTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


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


# FieldValueExtraOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionExtraOutputTypeDef'>
- **Required**: Yes


# FieldValueOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionOutputTypeDef'>
- **Required**: Yes


# FieldValueTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.FieldValueUnionTypeDef'>
- **Required**: Yes


# FieldValueUnionExtraOutputTypeDef

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


# GetCaseAuditEventsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCaseEventConfigurationRequestRequestTypeDef

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


# GetCaseRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
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


# GetDomainRequestRequestTypeDef

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


# GetLayoutRequestRequestTypeDef

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


# GetTemplateRequestRequestTypeDef

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


# ListCasesForContactRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsResponseTypeDef

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.DomainSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFieldOptionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.FieldOptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFieldsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLayoutsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListTemplatesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutCaseEventConfigurationRequestRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### eventBridge
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.EventBridgeConfigurationTypeDef'>
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


# SearchCasesRequestRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]]

### filter
- **Type**: typing.Optional[ForwardRef('CaseFilterTypeDef')]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchTerm
- **Type**: typing.Optional[str]

### sorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.SortTypeDef]]


# SearchCasesRequestSearchCasesPaginateTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.FieldIdentifierTypeDef]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.CaseFilterTypeDef]

### searchTerm
- **Type**: typing.Optional[str]

### sorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connectcases_classes.SortTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.PaginatorConfigTypeDef]


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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchRelatedItemsRequestRequestTypeDef

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


# SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef

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


# SearchRelatedItemsResponseItemTypeDef

### associationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.RelatedItemContentTypeDef'>
- **Required**: Yes

### relatedItemId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Comment', 'Contact', 'File']
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SearchRelatedItemsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### relatedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcases_classes.SearchRelatedItemsResponseItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcases_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# TagResourceRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
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


# UntagResourceRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCaseRequestRequestTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.connectcases_classes.FieldValueTypeDef, aws_resource_validator.pydantic_models.connectcases_classes.FieldValueExtraOutputTypeDef]]
- **Required**: Yes

### performedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.UserUnionTypeDef]


# UpdateFieldRequestRequestTypeDef

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


# UpdateLayoutRequestRequestTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### layoutId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcases_classes.LayoutContentTypeDef]

### name
- **Type**: typing.Optional[str]


# UpdateTemplateRequestRequestTypeDef

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

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UserUnionTypeDef

### userArn
- **Type**: typing.Optional[str]


