# Pydantic Models in verifiedpermissions_classes

# ActionIdentifierTypeDef

### actionType
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeValueOutputTypeDef

### boolean
- **Type**: typing.Optional[bool]

### entityIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### long
- **Type**: typing.Optional[int]

### string
- **Type**: typing.Optional[str]

### set
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### record
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# AttributeValueTypeDef

### boolean
- **Type**: typing.Optional[bool]

### entityIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### long
- **Type**: typing.Optional[int]

### string
- **Type**: typing.Optional[str]

### set
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### record
- **Type**: typing.Optional[typing.Mapping[str, typing.Dict[str, typing.Any]]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchIsAuthorizedInputItemOutputTypeDef

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ContextDefinitionOutputTypeDef]


# BatchIsAuthorizedInputItemTypeDef

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ContextDefinitionTypeDef]


# BatchIsAuthorizedInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### requests
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedInputItemTypeDef, aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedInputItemOutputTypeDef]]
- **Required**: Yes

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntitiesDefinitionTypeDef]


# BatchIsAuthorizedOutputItemTypeDef

### request
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedInputItemOutputTypeDef'>
- **Required**: Yes

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.DeterminingPolicyItemTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EvaluationErrorItemTypeDef]
- **Required**: Yes


# BatchIsAuthorizedOutputTypeDef

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedOutputItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchIsAuthorizedWithTokenInputItemOutputTypeDef

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ContextDefinitionOutputTypeDef]


# BatchIsAuthorizedWithTokenInputItemTypeDef

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ContextDefinitionTypeDef]


# BatchIsAuthorizedWithTokenInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### requests
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedWithTokenInputItemTypeDef, aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedWithTokenInputItemOutputTypeDef]]
- **Required**: Yes

### identityToken
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntitiesDefinitionTypeDef]


# BatchIsAuthorizedWithTokenOutputItemTypeDef

### request
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedWithTokenInputItemOutputTypeDef'>
- **Required**: Yes

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.DeterminingPolicyItemTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EvaluationErrorItemTypeDef]
- **Required**: Yes


# BatchIsAuthorizedWithTokenOutputTypeDef

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.BatchIsAuthorizedWithTokenOutputItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CognitoGroupConfigurationDetailTypeDef

### groupEntityType
- **Type**: typing.Optional[str]


# CognitoGroupConfigurationItemTypeDef

### groupEntityType
- **Type**: typing.Optional[str]


# CognitoGroupConfigurationTypeDef

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# CognitoUserPoolConfigurationDetailTypeDef

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.List[str]
- **Required**: Yes

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.CognitoGroupConfigurationDetailTypeDef]


# CognitoUserPoolConfigurationItemTypeDef

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.List[str]
- **Required**: Yes

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.CognitoGroupConfigurationItemTypeDef]


# CognitoUserPoolConfigurationTypeDef

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.Optional[typing.Sequence[str]]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.CognitoGroupConfigurationTypeDef]


# ConfigurationDetailTypeDef

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.CognitoUserPoolConfigurationDetailTypeDef]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectConfigurationDetailTypeDef]


# ConfigurationItemTypeDef

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.CognitoUserPoolConfigurationItemTypeDef]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectConfigurationItemTypeDef]


# ConfigurationTypeDef

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.CognitoUserPoolConfigurationTypeDef]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectConfigurationTypeDef]


# ContextDefinitionOutputTypeDef

### contextMap
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.verifiedpermissions_classes.AttributeValueOutputTypeDef]]


# ContextDefinitionTypeDef

### contextMap
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.verifiedpermissions_classes.AttributeValueTypeDef]]


# CreateIdentitySourceInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ConfigurationTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### principalEntityType
- **Type**: typing.Optional[str]


# CreateIdentitySourceOutputTypeDef

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyDefinitionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreatePolicyOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Forbid', 'Permit']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyStoreInputRequestTypeDef

### validationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ValidationSettingsTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreatePolicyStoreOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyTemplateInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreatePolicyTemplateOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIdentitySourceInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyStoreInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyTemplateInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeterminingPolicyItemTypeDef

### policyId
- **Type**: <class 'str'>
- **Required**: Yes


# EntitiesDefinitionTypeDef

### entityList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityItemTypeDef]]


# EntityIdentifierTypeDef

### entityType
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# EntityItemTypeDef

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.verifiedpermissions_classes.AttributeValueTypeDef]]

### parents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]]


# EntityReferenceTypeDef

### unspecified
- **Type**: typing.Optional[bool]

### identifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]


# EvaluationErrorItemTypeDef

### errorDescription
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentitySourceInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentitySourceOutputTypeDef

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.IdentitySourceDetailsTypeDef'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### principalEntityType
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ConfigurationDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyDefinitionDetailTypeDef'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Forbid', 'Permit']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyStoreInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyStoreOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### validationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ValidationSettingsTypeDef'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyTemplateInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyTemplateOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.GetSchemaOutputTypeDef'>>

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### namespaces
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentitySourceDetailsTypeDef

### clientIds
- **Type**: typing.Optional[typing.List[str]]

### userPoolArn
- **Type**: typing.Optional[str]

### discoveryUrl
- **Type**: typing.Optional[str]

### openIdIssuer
- **Type**: typing.Optional[typing.Literal['COGNITO']]


# IdentitySourceFilterTypeDef

### principalEntityType
- **Type**: typing.Optional[str]


# IdentitySourceItemDetailsTypeDef

### clientIds
- **Type**: typing.Optional[typing.List[str]]

### userPoolArn
- **Type**: typing.Optional[str]

### discoveryUrl
- **Type**: typing.Optional[str]

### openIdIssuer
- **Type**: typing.Optional[typing.Literal['COGNITO']]


# IdentitySourceItemTypeDef

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### principalEntityType
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.IdentitySourceItemDetailsTypeDef]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ConfigurationItemTypeDef]


# IsAuthorizedInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ContextDefinitionTypeDef]

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntitiesDefinitionTypeDef]


# IsAuthorizedOutputTypeDef

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.DeterminingPolicyItemTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EvaluationErrorItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IsAuthorizedWithTokenInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identityToken
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ContextDefinitionTypeDef]

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntitiesDefinitionTypeDef]


# IsAuthorizedWithTokenOutputTypeDef

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.DeterminingPolicyItemTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EvaluationErrorItemTypeDef]
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIdentitySourcesInputListIdentitySourcesPaginateTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.verifiedpermissions_classes.IdentitySourceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PaginatorConfigTypeDef]


# ListIdentitySourcesInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.verifiedpermissions_classes.IdentitySourceFilterTypeDef]]


# ListIdentitySourcesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### identitySources
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.IdentitySourceItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPoliciesInputListPoliciesPaginateTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PaginatorConfigTypeDef]


# ListPoliciesInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyFilterTypeDef]


# ListPoliciesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPolicyStoresInputListPolicyStoresPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PaginatorConfigTypeDef]


# ListPolicyStoresInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPolicyStoresOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### policyStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyStoreItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPolicyTemplatesInputListPolicyTemplatesPaginateTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PaginatorConfigTypeDef]


# ListPolicyTemplatesInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPolicyTemplatesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyTemplateItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OpenIdConnectAccessTokenConfigurationDetailTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectAccessTokenConfigurationItemTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectAccessTokenConfigurationTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.Sequence[str]]


# OpenIdConnectConfigurationDetailTypeDef

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectTokenSelectionDetailTypeDef'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectGroupConfigurationDetailTypeDef]


# OpenIdConnectConfigurationItemTypeDef

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectTokenSelectionItemTypeDef'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectGroupConfigurationItemTypeDef]


# OpenIdConnectConfigurationTypeDef

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectTokenSelectionTypeDef'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectGroupConfigurationTypeDef]


# OpenIdConnectGroupConfigurationDetailTypeDef

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# OpenIdConnectGroupConfigurationItemTypeDef

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# OpenIdConnectGroupConfigurationTypeDef

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# OpenIdConnectIdentityTokenConfigurationDetailTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectIdentityTokenConfigurationItemTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectIdentityTokenConfigurationTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.Sequence[str]]


# OpenIdConnectTokenSelectionDetailTypeDef

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectAccessTokenConfigurationDetailTypeDef]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectIdentityTokenConfigurationDetailTypeDef]


# OpenIdConnectTokenSelectionItemTypeDef

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectAccessTokenConfigurationItemTypeDef]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectIdentityTokenConfigurationItemTypeDef]


# OpenIdConnectTokenSelectionTypeDef

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectAccessTokenConfigurationTypeDef]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.OpenIdConnectIdentityTokenConfigurationTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyDefinitionDetailTypeDef

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.StaticPolicyDefinitionDetailTypeDef]

### templateLinked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.TemplateLinkedPolicyDefinitionDetailTypeDef]


# PolicyDefinitionItemTypeDef

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.StaticPolicyDefinitionItemTypeDef]

### templateLinked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.TemplateLinkedPolicyDefinitionItemTypeDef]


# PolicyDefinitionTypeDef

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.StaticPolicyDefinitionTypeDef]

### templateLinked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.TemplateLinkedPolicyDefinitionTypeDef]


# PolicyFilterTypeDef

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityReferenceTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityReferenceTypeDef]

### policyType
- **Type**: typing.Optional[typing.Literal['STATIC', 'TEMPLATE_LINKED']]

### policyTemplateId
- **Type**: typing.Optional[str]


# PolicyItemTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.PolicyDefinitionItemTypeDef'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]]

### effect
- **Type**: typing.Optional[typing.Literal['Forbid', 'Permit']]


# PolicyStoreItemTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]


# PolicyTemplateItemTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# PutSchemaInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.SchemaDefinitionTypeDef'>
- **Required**: Yes


# PutSchemaOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### namespaces
- **Type**: typing.List[str]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
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


# SchemaDefinitionTypeDef

### cedarJson
- **Type**: typing.Optional[str]


# StaticPolicyDefinitionDetailTypeDef

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StaticPolicyDefinitionItemTypeDef

### description
- **Type**: typing.Optional[str]


# StaticPolicyDefinitionTypeDef

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# TemplateLinkedPolicyDefinitionDetailTypeDef

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]


# TemplateLinkedPolicyDefinitionItemTypeDef

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]


# TemplateLinkedPolicyDefinitionTypeDef

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef]


# UpdateCognitoGroupConfigurationTypeDef

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCognitoUserPoolConfigurationTypeDef

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.Optional[typing.Sequence[str]]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateCognitoGroupConfigurationTypeDef]


# UpdateConfigurationTypeDef

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateCognitoUserPoolConfigurationTypeDef]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateOpenIdConnectConfigurationTypeDef]


# UpdateIdentitySourceInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### updateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateConfigurationTypeDef'>
- **Required**: Yes

### principalEntityType
- **Type**: typing.Optional[str]


# UpdateIdentitySourceOutputTypeDef

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOpenIdConnectAccessTokenConfigurationTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateOpenIdConnectConfigurationTypeDef

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateOpenIdConnectTokenSelectionTypeDef'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateOpenIdConnectGroupConfigurationTypeDef]


# UpdateOpenIdConnectGroupConfigurationTypeDef

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateOpenIdConnectIdentityTokenConfigurationTypeDef

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateOpenIdConnectTokenSelectionTypeDef

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateOpenIdConnectAccessTokenConfigurationTypeDef]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateOpenIdConnectIdentityTokenConfigurationTypeDef]


# UpdatePolicyDefinitionTypeDef

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdateStaticPolicyDefinitionTypeDef]


# UpdatePolicyInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.UpdatePolicyDefinitionTypeDef'>
- **Required**: Yes


# UpdatePolicyOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.EntityIdentifierTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions_classes.ActionIdentifierTypeDef]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Forbid', 'Permit']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePolicyStoreInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### validationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ValidationSettingsTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdatePolicyStoreOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePolicyTemplateInputRequestTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdatePolicyTemplateOutputTypeDef

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStaticPolicyDefinitionTypeDef

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ValidationSettingsTypeDef

### mode
- **Type**: typing.Literal['OFF', 'STRICT']
- **Required**: Yes


