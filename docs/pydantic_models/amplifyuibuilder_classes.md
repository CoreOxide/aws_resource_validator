# amplifyuibuilder_classes

# ActionParametersPaginatorTypeDef

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]

### url
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]

### anchor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]

### model
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]

### fields
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.MutationActionSetStateParameterPaginatorTypeDef]


# ActionParametersTypeDef

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]

### url
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]

### anchor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]

### model
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]

### fields
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.MutationActionSetStateParameterTypeDef]


# ApiConfigurationTypeDef

### graphQLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.GraphQLRenderConfigTypeDef]

### dataStoreConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### noApiConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenDependencyTypeDef

### name
- **Type**: typing.Optional[str]

### supportedVersion
- **Type**: typing.Optional[str]

### isSemVer
- **Type**: typing.Optional[bool]

### reason
- **Type**: typing.Optional[str]


# CodegenFeatureFlagsTypeDef

### isRelationshipSupported
- **Type**: typing.Optional[bool]

### isNonModelSupported
- **Type**: typing.Optional[bool]


# CodegenGenericDataEnumTypeDef

### values
- **Type**: typing.List[str]
- **Required**: Yes


# CodegenGenericDataFieldTypeDef

### dataType
- **Type**: typing.Literal['AWSDate', 'AWSDateTime', 'AWSEmail', 'AWSIPAddress', 'AWSJSON', 'AWSPhone', 'AWSTime', 'AWSTimestamp', 'AWSURL', 'Boolean', 'Enum', 'Float', 'ID', 'Int', 'Model', 'NonModel', 'String']
- **Required**: Yes

### dataTypeValue
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: <class 'bool'>
- **Required**: Yes

### readOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### isArray
- **Type**: <class 'bool'>
- **Required**: Yes

### relationship
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataRelationshipTypeTypeDef]


# CodegenGenericDataModelTypeDef

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldTypeDef]
- **Required**: Yes

### primaryKeys
- **Type**: typing.List[str]
- **Required**: Yes

### isJoinTable
- **Type**: typing.Optional[bool]


# CodegenGenericDataNonModelTypeDef

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldTypeDef]
- **Required**: Yes


# CodegenGenericDataRelationshipTypeTypeDef

### type
- **Type**: typing.Literal['BELONGS_TO', 'HAS_MANY', 'HAS_ONE']
- **Required**: Yes

### relatedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### relatedModelFields
- **Type**: typing.Optional[typing.List[str]]

### canUnlinkAssociatedModel
- **Type**: typing.Optional[bool]

### relatedJoinFieldName
- **Type**: typing.Optional[str]

### relatedJoinTableName
- **Type**: typing.Optional[str]

### belongsToFieldOnRelatedModel
- **Type**: typing.Optional[str]

### associatedFields
- **Type**: typing.Optional[typing.List[str]]

### isHasManyIndex
- **Type**: typing.Optional[bool]


# CodegenJobAssetTypeDef

### downloadUrl
- **Type**: typing.Optional[str]


# CodegenJobGenericDataSchemaTypeDef

### dataSourceType
- **Type**: typing.Literal['DataStore']
- **Required**: Yes

### models
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataModelTypeDef]
- **Required**: Yes

### enums
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataEnumTypeDef]
- **Required**: Yes

### nonModels
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataNonModelTypeDef]
- **Required**: Yes


# CodegenJobRenderConfigTypeDef

### react
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ReactStartCodegenJobDataTypeDef]


# CodegenJobSummaryTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# CodegenJobTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### renderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobRenderConfigTypeDef]

### genericDataSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobGenericDataSchemaTypeDef]

### autoGenerateForms
- **Type**: typing.Optional[bool]

### features
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenFeatureFlagsTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['failed', 'in_progress', 'succeeded']]

### statusMessage
- **Type**: typing.Optional[str]

### asset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobAssetTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### dependencies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenDependencyTypeDef]]


# ComponentBindingPropertiesValuePaginatorTypeDef

### type
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValuePropertiesPaginatorTypeDef]

### defaultValue
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValuePropertiesPaginatorTypeDef

### model
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### predicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicatePaginatorTypeDef]]

### userAttribute
- **Type**: typing.Optional[str]

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### slotName
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValuePropertiesTypeDef

### model
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### predicates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateTypeDef]]

### userAttribute
- **Type**: typing.Optional[str]

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### slotName
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValueTypeDef

### type
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValuePropertiesTypeDef]

### defaultValue
- **Type**: typing.Optional[str]


# ComponentChildPaginatorTypeDef

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventPaginatorTypeDef]]

### sourceId
- **Type**: typing.Optional[str]


# ComponentChildTypeDef

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventTypeDef]]

### sourceId
- **Type**: typing.Optional[str]


# ComponentConditionPropertyTypeDef

### property
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### then
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]

### operandType
- **Type**: typing.Optional[str]


# ComponentDataConfigurationPaginatorTypeDef

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SortPropertyTypeDef]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicatePaginatorTypeDef]

### identifiers
- **Type**: typing.Optional[typing.List[str]]


# ComponentDataConfigurationTypeDef

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SortPropertyTypeDef]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateTypeDef]

### identifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# ComponentEventPaginatorTypeDef

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ActionParametersPaginatorTypeDef]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentEventTypeDef

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ActionParametersTypeDef]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentPaginatorTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef]
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentVariantPaginatorTypeDef]
- **Required**: Yes

### overrides
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValuePaginatorTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentChildPaginatorTypeDef]]

### collectionProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentDataConfigurationPaginatorTypeDef]]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventPaginatorTypeDef]]

### schemaVersion
- **Type**: typing.Optional[str]


# ComponentPropertyBindingPropertiesTypeDef

### property
- **Type**: <class 'str'>
- **Required**: Yes

### field
- **Type**: typing.Optional[str]


# ComponentPropertyPaginatorTypeDef

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyBindingPropertiesTypeDef]

### collectionBindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyBindingPropertiesTypeDef]

### defaultValue
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### bindings
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormBindingElementTypeDef]]

### event
- **Type**: typing.Optional[str]

### userAttribute
- **Type**: typing.Optional[str]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentConditionPropertyTypeDef]

### configured
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### importedValue
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### property
- **Type**: typing.Optional[str]


# ComponentPropertyTypeDef

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyBindingPropertiesTypeDef]

### collectionBindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyBindingPropertiesTypeDef]

### defaultValue
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### bindings
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormBindingElementTypeDef]]

### event
- **Type**: typing.Optional[str]

### userAttribute
- **Type**: typing.Optional[str]

### concat
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### condition
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### configured
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### importedValue
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### property
- **Type**: typing.Optional[str]


# ComponentSummaryTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes


# ComponentTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentVariantTypeDef]
- **Required**: Yes

### overrides
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValueTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentChildTypeDef]]

### collectionProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentDataConfigurationTypeDef]]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventTypeDef]]

### schemaVersion
- **Type**: typing.Optional[str]


# ComponentVariantPaginatorTypeDef

### variantValues
- **Type**: typing.Optional[typing.Dict[str, str]]

### overrides
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# ComponentVariantTypeDef

### variantValues
- **Type**: typing.Optional[typing.Mapping[str, str]]

### overrides
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]


# CreateComponentDataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]
- **Required**: Yes

### variants
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentVariantTypeDef]
- **Required**: Yes

### overrides
- **Type**: typing.Mapping[str, typing.Mapping[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValueTypeDef]
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentChildTypeDef]]

### collectionProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentDataConfigurationTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### events
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventTypeDef]]

### schemaVersion
- **Type**: typing.Optional[str]


# CreateComponentRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### componentToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CreateComponentDataTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateComponentResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFormDataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormDataTypeConfigTypeDef'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### fields
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigTypeDef]
- **Required**: Yes

### style
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleTypeDef'>
- **Required**: Yes

### sectionalElements
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SectionalElementTypeDef]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormCTATypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# CreateFormRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### formToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CreateFormDataTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateFormResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateThemeDataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesTypeDef]
- **Required**: Yes

### overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateThemeRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### themeToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CreateThemeDataTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateThemeResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteComponentRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFormRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThemeRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExchangeCodeForTokenRequestBodyTypeDef

### code
- **Type**: <class 'str'>
- **Required**: Yes

### redirectUri
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: typing.Optional[str]


# ExchangeCodeForTokenRequestRequestTypeDef

### provider
- **Type**: typing.Literal['figma']
- **Required**: Yes

### request
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ExchangeCodeForTokenRequestBodyTypeDef'>
- **Required**: Yes


# ExchangeCodeForTokenResponseTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### refreshToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportComponentsRequestExportComponentsPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ExportComponentsRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportComponentsResponsePaginatorTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportComponentsResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportFormsRequestExportFormsPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ExportFormsRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportFormsResponsePaginatorTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportFormsResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportThemesRequestExportThemesPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ExportThemesRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportThemesResponsePaginatorTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemePaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportThemesResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FieldConfigPaginatorTypeDef

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPositionTypeDef]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldInputConfigPaginatorTypeDef]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationPaginatorTypeDef]]


# FieldConfigTypeDef

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPositionTypeDef]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldInputConfigTypeDef]

### validations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationTypeDef]]


# FieldInputConfigPaginatorTypeDef

### type
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]

### readOnly
- **Type**: typing.Optional[bool]

### placeholder
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### descriptiveText
- **Type**: typing.Optional[str]

### defaultChecked
- **Type**: typing.Optional[bool]

### defaultCountryCode
- **Type**: typing.Optional[str]

### valueMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingsPaginatorTypeDef]

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]

### step
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[str]

### isArray
- **Type**: typing.Optional[bool]

### fileUploaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FileUploaderFieldConfigPaginatorTypeDef]


# FieldInputConfigTypeDef

### type
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]

### readOnly
- **Type**: typing.Optional[bool]

### placeholder
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### descriptiveText
- **Type**: typing.Optional[str]

### defaultChecked
- **Type**: typing.Optional[bool]

### defaultCountryCode
- **Type**: typing.Optional[str]

### valueMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingsTypeDef]

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]

### step
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[str]

### isArray
- **Type**: typing.Optional[bool]

### fileUploaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FileUploaderFieldConfigTypeDef]


# FieldPositionTypeDef

### fixed
- **Type**: typing.Optional[typing.Literal['first']]

### rightOf
- **Type**: typing.Optional[str]

### below
- **Type**: typing.Optional[str]


# FieldValidationConfigurationPaginatorTypeDef

### type
- **Type**: <class 'str'>
- **Required**: Yes

### strValues
- **Type**: typing.Optional[typing.List[str]]

### numValues
- **Type**: typing.Optional[typing.List[int]]

### validationMessage
- **Type**: typing.Optional[str]


# FieldValidationConfigurationTypeDef

### type
- **Type**: <class 'str'>
- **Required**: Yes

### strValues
- **Type**: typing.Optional[typing.Sequence[str]]

### numValues
- **Type**: typing.Optional[typing.Sequence[int]]

### validationMessage
- **Type**: typing.Optional[str]


# FileUploaderFieldConfigPaginatorTypeDef

### accessLevel
- **Type**: typing.Literal['private', 'protected', 'public']
- **Required**: Yes

### acceptedFileTypes
- **Type**: typing.List[str]
- **Required**: Yes

### showThumbnails
- **Type**: typing.Optional[bool]

### isResumable
- **Type**: typing.Optional[bool]

### maxFileCount
- **Type**: typing.Optional[int]

### maxSize
- **Type**: typing.Optional[int]


# FileUploaderFieldConfigTypeDef

### accessLevel
- **Type**: typing.Literal['private', 'protected', 'public']
- **Required**: Yes

### acceptedFileTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### showThumbnails
- **Type**: typing.Optional[bool]

### isResumable
- **Type**: typing.Optional[bool]

### maxFileCount
- **Type**: typing.Optional[int]

### maxSize
- **Type**: typing.Optional[int]


# FormBindingElementTypeDef

### element
- **Type**: <class 'str'>
- **Required**: Yes

### property
- **Type**: <class 'str'>
- **Required**: Yes


# FormButtonTypeDef

### excluded
- **Type**: typing.Optional[bool]

### children
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPositionTypeDef]


# FormCTATypeDef

### position
- **Type**: typing.Optional[typing.Literal['bottom', 'top', 'top_and_bottom']]

### clear
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormButtonTypeDef]

### cancel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormButtonTypeDef]

### submit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormButtonTypeDef]


# FormDataTypeConfigTypeDef

### dataSourceType
- **Type**: typing.Literal['Custom', 'DataStore']
- **Required**: Yes

### dataTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# FormInputBindingPropertiesValuePropertiesTypeDef

### model
- **Type**: typing.Optional[str]


# FormInputBindingPropertiesValueTypeDef

### type
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValuePropertiesTypeDef]


# FormInputValuePropertyBindingPropertiesTypeDef

### property
- **Type**: <class 'str'>
- **Required**: Yes

### field
- **Type**: typing.Optional[str]


# FormInputValuePropertyPaginatorTypeDef

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyBindingPropertiesTypeDef]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FormInputValuePropertyTypeDef

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyBindingPropertiesTypeDef]

### concat
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]


# FormPaginatorTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### style
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleTypeDef'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormDataTypeConfigTypeDef'>
- **Required**: Yes

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigPaginatorTypeDef]
- **Required**: Yes

### sectionalElements
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SectionalElementTypeDef]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormCTATypeDef]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# FormStyleConfigTypeDef

### tokenReference
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# FormStyleTypeDef

### horizontalGap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleConfigTypeDef]

### verticalGap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleConfigTypeDef]

### outerPadding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleConfigTypeDef]


# FormSummaryTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormDataTypeConfigTypeDef'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# FormTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### style
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleTypeDef'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormDataTypeConfigTypeDef'>
- **Required**: Yes

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigTypeDef]
- **Required**: Yes

### sectionalElements
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SectionalElementTypeDef]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormCTATypeDef]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# GetCodegenJobRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodegenJobResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComponentRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentResponseTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFormRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFormResponseTypeDef

### form
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetadataRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetadataResponseTypeDef

### features
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetThemeRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetThemeResponseTypeDef

### theme
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GraphQLRenderConfigTypeDef

### typesFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### queriesFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### mutationsFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionsFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### fragmentsFilePath
- **Type**: <class 'str'>
- **Required**: Yes


# ListCodegenJobsRequestListCodegenJobsPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListCodegenJobsRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCodegenJobsResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListComponentsRequestListComponentsPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListComponentsRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListComponentsResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFormsRequestListFormsPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListFormsRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFormsResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThemesRequestListThemesPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListThemesRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThemesResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MutationActionSetStateParameterPaginatorTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### property
- **Type**: <class 'str'>
- **Required**: Yes

### set
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginatorTypeDef'>
- **Required**: Yes


# MutationActionSetStateParameterTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### property
- **Type**: <class 'str'>
- **Required**: Yes

### set
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredicatePaginatorTypeDef

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### operandType
- **Type**: typing.Optional[str]


# PredicateTypeDef

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### operandType
- **Type**: typing.Optional[str]


# PutMetadataFlagBodyTypeDef

### newValue
- **Type**: <class 'str'>
- **Required**: Yes


# PutMetadataFlagRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### featureName
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PutMetadataFlagBodyTypeDef'>
- **Required**: Yes


# ReactStartCodegenJobDataTypeDef

### module
- **Type**: typing.Optional[typing.Literal['es2020', 'esnext']]

### target
- **Type**: typing.Optional[typing.Literal['es2015', 'es2020']]

### script
- **Type**: typing.Optional[typing.Literal['js', 'jsx', 'tsx']]

### renderTypeDeclarations
- **Type**: typing.Optional[bool]

### inlineSourceMap
- **Type**: typing.Optional[bool]

### apiConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ApiConfigurationTypeDef]

### dependencies
- **Type**: typing.Optional[typing.Dict[str, str]]


# RefreshTokenRequestBodyTypeDef

### token
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: typing.Optional[str]


# RefreshTokenRequestRequestTypeDef

### provider
- **Type**: typing.Literal['figma']
- **Required**: Yes

### refreshTokenBody
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.RefreshTokenRequestBodyTypeDef'>
- **Required**: Yes


# RefreshTokenResponseTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
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


# SectionalElementTypeDef

### type
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPositionTypeDef]

### text
- **Type**: typing.Optional[str]

### level
- **Type**: typing.Optional[int]

### orientation
- **Type**: typing.Optional[str]

### excluded
- **Type**: typing.Optional[bool]


# SortPropertyTypeDef

### field
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# StartCodegenJobDataTypeDef

### renderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobRenderConfigTypeDef'>
- **Required**: Yes

### genericDataSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobGenericDataSchemaTypeDef]

### autoGenerateForms
- **Type**: typing.Optional[bool]

### features
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenFeatureFlagsTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartCodegenJobRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### codegenJobToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.StartCodegenJobDataTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartCodegenJobResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ThemePaginatorTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesPaginatorTypeDef]
- **Required**: Yes

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesPaginatorTypeDef]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ThemeSummaryTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ThemeTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesTypeDef]
- **Required**: Yes

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesTypeDef]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ThemeValuePaginatorTypeDef

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[ForwardRef('ThemeValuesPaginatorTypeDef')]]


# ThemeValueTypeDef

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.Sequence[ForwardRef('ThemeValuesTypeDef')]]


# ThemeValuesPaginatorTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ThemeValuesTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateComponentDataTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### sourceId
- **Type**: typing.Optional[str]

### componentType
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyTypeDef]]

### children
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentChildTypeDef]]

### variants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentVariantTypeDef]]

### overrides
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]

### bindingProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValueTypeDef]]

### collectionProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentDataConfigurationTypeDef]]

### events
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventTypeDef]]

### schemaVersion
- **Type**: typing.Optional[str]


# UpdateComponentRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### updatedComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.UpdateComponentDataTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateComponentResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFormDataTypeDef

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormDataTypeConfigTypeDef]

### formActionType
- **Type**: typing.Optional[typing.Literal['create', 'update']]

### fields
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigTypeDef]]

### style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleTypeDef]

### sectionalElements
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SectionalElementTypeDef]]

### schemaVersion
- **Type**: typing.Optional[str]

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormCTATypeDef]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# UpdateFormRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### updatedForm
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.UpdateFormDataTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateFormResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateThemeDataTypeDef

### values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesTypeDef]
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesTypeDef]]


# UpdateThemeRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### updatedTheme
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.UpdateThemeDataTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateThemeResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValueMappingPaginatorTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyPaginatorTypeDef'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyPaginatorTypeDef]


# ValueMappingTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyTypeDef'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyTypeDef]


# ValueMappingsPaginatorTypeDef

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingPaginatorTypeDef]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValueTypeDef]]


# ValueMappingsTypeDef

### values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingTypeDef]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValueTypeDef]]


