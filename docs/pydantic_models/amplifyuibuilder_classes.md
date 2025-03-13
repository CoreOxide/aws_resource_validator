# Amplifyuibuilder Classes

# ActionParametersOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionParametersPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiConfigurationOutputTypeDef

### graphQLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.GraphQLRenderConfigTypeDef]

### dataStoreConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### noApiConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ApiConfigurationTypeDef

### graphQLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.GraphQLRenderConfigTypeDef]

### dataStoreConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### noApiConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ApiConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CodegenGenericDataEnumOutputTypeDef

### values
- **Type**: typing.List[str]
- **Required**: Yes


# CodegenGenericDataEnumTypeDef

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CodegenGenericDataEnumUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataFieldOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataRelationshipTypeOutputTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataRelationshipTypeUnionTypeDef]


# CodegenGenericDataFieldUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataModelOutputTypeDef

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldOutputTypeDef]
- **Required**: Yes

### primaryKeys
- **Type**: typing.List[str]
- **Required**: Yes

### isJoinTable
- **Type**: typing.Optional[bool]


# CodegenGenericDataModelTypeDef

### fields
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldTypeDef]
- **Required**: Yes

### primaryKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### isJoinTable
- **Type**: typing.Optional[bool]


# CodegenGenericDataModelUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataNonModelOutputTypeDef

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldOutputTypeDef]
- **Required**: Yes


# CodegenGenericDataNonModelTypeDef

### fields
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldUnionTypeDef]
- **Required**: Yes


# CodegenGenericDataNonModelUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataRelationshipTypeOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataRelationshipTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJobAssetTypeDef

### downloadUrl
- **Type**: typing.Optional[str]


# CodegenJobGenericDataSchemaOutputTypeDef

### dataSourceType
- **Type**: typing.Literal['DataStore']
- **Required**: Yes

### models
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataModelOutputTypeDef]
- **Required**: Yes

### enums
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataEnumOutputTypeDef]
- **Required**: Yes

### nonModels
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataNonModelOutputTypeDef]
- **Required**: Yes


# CodegenJobGenericDataSchemaTypeDef

### dataSourceType
- **Type**: typing.Literal['DataStore']
- **Required**: Yes

### models
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataModelUnionTypeDef]
- **Required**: Yes

### enums
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataEnumUnionTypeDef]
- **Required**: Yes

### nonModels
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataNonModelUnionTypeDef]
- **Required**: Yes


# CodegenJobGenericDataSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJobRenderConfigOutputTypeDef

### react
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ReactStartCodegenJobDataOutputTypeDef]


# CodegenJobRenderConfigTypeDef

### react
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ReactStartCodegenJobDataUnionTypeDef]


# CodegenJobRenderConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJobSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentBindingPropertiesValuePropertiesOutputTypeDef

### model
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### predicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateOutputTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateUnionTypeDef]]

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


# ComponentBindingPropertiesValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentChildOutputTypeDef

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyOutputTypeDef]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventOutputTypeDef]]

### sourceId
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
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventTypeDef]]

### sourceId
- **Type**: typing.Optional[str]


# ComponentChildUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentDataConfigurationOutputTypeDef

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SortPropertyTypeDef]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateOutputTypeDef]

### identifiers
- **Type**: typing.Optional[typing.List[str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateUnionTypeDef]

### identifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# ComponentDataConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentEventOutputTypeDef

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ActionParametersOutputTypeDef]

### bindingEvent
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ActionParametersUnionTypeDef]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentEventUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentVariantOutputTypeDef

### variantValues
- **Type**: typing.Optional[typing.Dict[str, str]]

### overrides
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# ComponentVariantTypeDef

### variantValues
- **Type**: typing.Optional[typing.Mapping[str, str]]

### overrides
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]


# ComponentVariantUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateComponentDataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyUnionTypeDef]
- **Required**: Yes

### variants
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentVariantUnionTypeDef]
- **Required**: Yes

### overrides
- **Type**: typing.Mapping[str, typing.Mapping[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValueUnionTypeDef]
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentChildUnionTypeDef]]

### collectionProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentDataConfigurationUnionTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### events
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventUnionTypeDef]]

### schemaVersion
- **Type**: typing.Optional[str]


# CreateComponentRequestTypeDef

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
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigUnionTypeDef]
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


# CreateFormRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesUnionTypeDef]
- **Required**: Yes

### overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateThemeRequestTypeDef

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


# ExchangeCodeForTokenRequestTypeDef

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


# ExportComponentsRequestPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ExportComponentsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportComponentsResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportFormsRequestPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ExportFormsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportFormsResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportThemesRequestPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ExportThemesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportThemesResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# FieldConfigOutputTypeDef

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPositionTypeDef]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldInputConfigOutputTypeDef]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationOutputTypeDef]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationOutputTypeDef]]


# FieldConfigTypeDef

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPositionTypeDef]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldInputConfigUnionTypeDef]

### validations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationUnionTypeDef]]


# FieldConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldInputConfigOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldInputConfigPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldInputConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldPositionTypeDef

### fixed
- **Type**: typing.Optional[typing.Literal['first']]

### rightOf
- **Type**: typing.Optional[str]

### below
- **Type**: typing.Optional[str]


# FieldValidationConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValidationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileUploaderFieldConfigOutputTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputValuePropertyBindingPropertiesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputValuePropertyOutputTypeDef

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyBindingPropertiesTypeDef]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


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
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# FormInputValuePropertyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetCodegenJobResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComponentResponseTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFormResponseTypeDef

### form
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetadataRequestTypeDef

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


# ListCodegenJobsRequestPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListCodegenJobsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequestPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListComponentsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFormsRequestPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListFormsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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


# ListThemesRequestPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfigTypeDef]


# ListThemesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredicateOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PredicatePaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PredicateUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutMetadataFlagBodyTypeDef

### newValue
- **Type**: <class 'str'>
- **Required**: Yes


# PutMetadataFlagRequestTypeDef

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


# ReactStartCodegenJobDataOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ApiConfigurationOutputTypeDef]

### dependencies
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ApiConfigurationUnionTypeDef]

### dependencies
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ReactStartCodegenJobDataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RefreshTokenRequestBodyTypeDef

### token
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: typing.Optional[str]


# RefreshTokenRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SortPropertyTypeDef

### field
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# StartCodegenJobDataTypeDef

### renderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobRenderConfigUnionTypeDef'>
- **Required**: Yes

### genericDataSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobGenericDataSchemaUnionTypeDef]

### autoGenerateForms
- **Type**: typing.Optional[bool]

### features
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenFeatureFlagsTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartCodegenJobRequestTypeDef

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


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ThemePaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeValueOutputTypeDef

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ThemeValuePaginatorTypeDef

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ThemeValueTypeDef

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# ThemeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeValuesOutputTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValueOutputTypeDef]


# ThemeValuesPaginatorTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuePaginatorTypeDef]


# ThemeValuesTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValueUnionTypeDef]


# ThemeValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigUnionTypeDef]]

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


# UpdateFormResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateThemeResponseTypeDef

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValueMappingOutputTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyOutputTypeDef'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyOutputTypeDef]


# ValueMappingPaginatorTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyPaginatorTypeDef'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyPaginatorTypeDef]


# ValueMappingTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyUnionTypeDef'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyUnionTypeDef]


# ValueMappingUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValueMappingsOutputTypeDef

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingOutputTypeDef]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValueTypeDef]]


# ValueMappingsPaginatorTypeDef

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingPaginatorTypeDef]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValueTypeDef]]


# ValueMappingsTypeDef

### values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingUnionTypeDef]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValueTypeDef]]


