# Datazone Classes

# AcceptChoiceTypeDef

### predictionTarget
- **Type**: <class 'str'>
- **Required**: Yes

### editedValue
- **Type**: typing.Optional[str]

### predictionChoice
- **Type**: typing.Optional[int]


# AcceptPredictionsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### acceptChoices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.AcceptChoiceTypeDef]]

### acceptRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AcceptRuleTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]


# AcceptPredictionsOutputTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AcceptRuleTypeDef

### rule
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]

### threshold
- **Type**: typing.Optional[float]


# AcceptSubscriptionRequestInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### assetScopes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.AcceptedAssetScopeTypeDef]]

### decisionComment
- **Type**: typing.Optional[str]


# AcceptedAssetScopeTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### filterIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ActionParametersTypeDef

### awsConsoleLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AwsConsoleLinkParametersTypeDef]


# AddEntityOwnerInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### owner
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.OwnerPropertiesTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AddPolicyGrantInputTypeDef

### detail
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.PolicyGrantDetailUnionTypeDef'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT', 'ENVIRONMENT_BLUEPRINT_CONFIGURATION', 'ENVIRONMENT_PROFILE']
- **Required**: Yes

### policyType
- **Type**: typing.Literal['ADD_TO_PROJECT_MEMBER_POOL', 'CREATE_ASSET_TYPE', 'CREATE_DOMAIN_UNIT', 'CREATE_ENVIRONMENT', 'CREATE_ENVIRONMENT_FROM_BLUEPRINT', 'CREATE_ENVIRONMENT_PROFILE', 'CREATE_FORM_TYPE', 'CREATE_GLOSSARY', 'CREATE_PROJECT', 'CREATE_PROJECT_FROM_PROJECT_PROFILE', 'DELEGATE_CREATE_ENVIRONMENT_PROFILE', 'OVERRIDE_DOMAIN_UNIT_OWNERS', 'OVERRIDE_PROJECT_OWNERS']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.PolicyGrantPrincipalUnionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AddToProjectMemberPoolPolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# AssetFilterConfigurationOutputTypeDef

### columnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ColumnFilterConfigurationOutputTypeDef]

### rowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RowFilterConfigurationOutputTypeDef]


# AssetFilterConfigurationTypeDef

### columnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ColumnFilterConfigurationTypeDef]

### rowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RowFilterConfigurationTypeDef]


# AssetFilterConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetFilterSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetInDataProductListingItemTypeDef

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### entityType
- **Type**: typing.Optional[str]


# AssetItemAdditionalAttributesTypeDef

### formsOutput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]]

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]]

### readOnlyFormsOutput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]]


# AssetItemTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetItemAdditionalAttributesTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### externalIdentifier
- **Type**: typing.Optional[str]

### firstRevisionCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### firstRevisionCreatedBy
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]


# AssetListingDetailsTypeDef

### listingId
- **Type**: <class 'str'>
- **Required**: Yes

### listingStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'INACTIVE']
- **Required**: Yes


# AssetListingItemAdditionalAttributesTypeDef

### forms
- **Type**: typing.Optional[str]

### latestTimeSeriesDataPointForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]]


# AssetListingItemTypeDef

### additionalAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetListingItemAdditionalAttributesTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### entityType
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]

### listingCreatedBy
- **Type**: typing.Optional[str]

### listingId
- **Type**: typing.Optional[str]

### listingRevision
- **Type**: typing.Optional[str]

### listingUpdatedBy
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]


# AssetListingTypeDef

### assetId
- **Type**: typing.Optional[str]

### assetRevision
- **Type**: typing.Optional[str]

### assetType
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### forms
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]

### latestTimeSeriesDataPointForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]]

### owningProjectId
- **Type**: typing.Optional[str]


# AssetRevisionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetScopeTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### filterIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[str]


# AssetTargetNameMapTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### targetName
- **Type**: <class 'str'>
- **Required**: Yes


# AssetTypeItemTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone_classes.FormEntryOutputTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### originDomainId
- **Type**: typing.Optional[str]

### originProjectId
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# AssetTypesForRuleOutputTypeDef

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificAssetTypes
- **Type**: typing.Optional[typing.List[str]]


# AssetTypesForRuleTypeDef

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificAssetTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# AssociateEnvironmentRoleInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AthenaPropertiesInputTypeDef

### workgroupName
- **Type**: typing.Optional[str]


# AthenaPropertiesOutputTypeDef

### workgroupName
- **Type**: typing.Optional[str]


# AthenaPropertiesPatchTypeDef

### workgroupName
- **Type**: typing.Optional[str]


# AuthenticationConfigurationInputTypeDef

### authenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'OAUTH2']]

### basicAuthenticationCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.BasicAuthenticationCredentialsTypeDef]

### customAuthenticationCredentials
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]

### oAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OAuth2PropertiesUnionTypeDef]

### secretArn
- **Type**: typing.Optional[str]


# AuthenticationConfigurationPatchTypeDef

### basicAuthenticationCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.BasicAuthenticationCredentialsTypeDef]

### secretArn
- **Type**: typing.Optional[str]


# AuthenticationConfigurationTypeDef

### authenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'OAUTH2']]

### oAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OAuth2PropertiesOutputTypeDef]

### secretArn
- **Type**: typing.Optional[str]


# AuthorizationCodePropertiesTypeDef

### authorizationCode
- **Type**: typing.Optional[str]

### redirectUri
- **Type**: typing.Optional[str]


# AwsAccountTypeDef

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountIdPath
- **Type**: typing.Optional[str]


# AwsConsoleLinkParametersTypeDef

### uri
- **Type**: typing.Optional[str]


# AwsLocationTypeDef

### accessRole
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### iamConnectionId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthenticationCredentialsTypeDef

### password
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BusinessNameGenerationConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]


# CancelMetadataGenerationRunInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSubscriptionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# CloudFormationPropertiesTypeDef

### templateUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ColumnFilterConfigurationOutputTypeDef

### includedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnFilterConfigurationTypeDef

### includedColumnNames
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfigurableActionParameterTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ConnectionCredentialsTypeDef

### accessKeyId
- **Type**: typing.Optional[str]

### expiration
- **Type**: typing.Optional[datetime.datetime]

### secretAccessKey
- **Type**: typing.Optional[str]

### sessionToken
- **Type**: typing.Optional[str]


# ConnectionPropertiesInputTypeDef

### athenaProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AthenaPropertiesInputTypeDef]

### glueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GluePropertiesInputTypeDef]

### hyperPodProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.HyperPodPropertiesInputTypeDef]

### iamProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.IamPropertiesInputTypeDef]

### redshiftProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftPropertiesInputTypeDef]

### sparkEmrProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SparkEmrPropertiesInputTypeDef]

### sparkGlueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SparkGluePropertiesInputTypeDef]


# ConnectionPropertiesOutputTypeDef

### athenaProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AthenaPropertiesOutputTypeDef]

### glueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GluePropertiesOutputTypeDef]

### hyperPodProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.HyperPodPropertiesOutputTypeDef]

### iamProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.IamPropertiesOutputTypeDef]

### redshiftProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftPropertiesOutputTypeDef]

### sparkEmrProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SparkEmrPropertiesOutputTypeDef]

### sparkGlueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SparkGluePropertiesOutputTypeDef]


# ConnectionPropertiesPatchTypeDef

### athenaProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AthenaPropertiesPatchTypeDef]

### glueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GluePropertiesPatchTypeDef]

### iamProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.IamPropertiesPatchTypeDef]

### redshiftProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftPropertiesPatchTypeDef]

### sparkEmrProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SparkEmrPropertiesPatchTypeDef]


# ConnectionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAssetFilterInputTypeDef

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.AssetFilterConfigurationUnionTypeDef'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateAssetInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### externalIdentifier
- **Type**: typing.Optional[str]

### formsInput
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FormInputTypeDef]]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### predictionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PredictionConfigurationTypeDef]

### typeRevision
- **Type**: typing.Optional[str]


# CreateAssetRevisionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### formsInput
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FormInputTypeDef]]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### predictionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PredictionConfigurationTypeDef]

### typeRevision
- **Type**: typing.Optional[str]


# CreateAssetTypeInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### formsInput
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.datazone_classes.FormEntryInputTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateAssetTypeOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone_classes.FormEntryOutputTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### originDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### originProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssetTypePolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateConnectionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### awsLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AwsLocationTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### props
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ConnectionPropertiesInputTypeDef]


# CreateDataProductInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### formsInput
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FormInputTypeDef]]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.DataProductItemUnionTypeDef]]


# CreateDataProductRevisionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### formsInput
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FormInputTypeDef]]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.DataProductItemUnionTypeDef]]


# CreateDomainInputTypeDef

### domainExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### domainVersion
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### kmsKeyIdentifier
- **Type**: typing.Optional[str]

### serviceRole
- **Type**: typing.Optional[str]

### singleSignOn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SingleSignOnTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDomainUnitInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parentDomainUnitIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateDomainUnitPolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateEnvironmentActionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ActionParametersTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateEnvironmentInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentOrder
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### environmentAccountIdentifier
- **Type**: typing.Optional[str]

### environmentAccountRegion
- **Type**: typing.Optional[str]

### environmentBlueprintIdentifier
- **Type**: typing.Optional[str]

### environmentConfigurationId
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### userParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentParameterTypeDef]]


# CreateEnvironmentProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### userParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentParameterTypeDef]]


# CreateEnvironmentProfilePolicyGrantDetailTypeDef

### domainUnitId
- **Type**: typing.Optional[str]


# CreateFormTypeInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### model
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ModelTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateFormTypeOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### originDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### originProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFormTypePolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateGlossaryInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateGlossaryPolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateGlossaryTermInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### longDescription
- **Type**: typing.Optional[str]

### shortDescription
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### termRelations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TermRelationsUnionTypeDef]


# CreateGroupProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateListingChangeSetInputTypeDef

### action
- **Type**: typing.Literal['PUBLISH', 'UNPUBLISH']
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'DATA_PRODUCT']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]


# CreateListingChangeSetOutputTypeDef

### listingId
- **Type**: <class 'str'>
- **Required**: Yes

### listingRevision
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'INACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]

### projectProfiles
- **Type**: typing.Optional[typing.List[str]]


# CreateProjectFromProjectProfilePolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]

### projectProfiles
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateProjectInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### domainUnitId
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### projectProfileId
- **Type**: typing.Optional[str]

### userParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentConfigurationUserParameterUnionTypeDef]]


# CreateProjectMembershipInputTypeDef

### designation
- **Type**: typing.Literal['PROJECT_CATALOG_CONSUMER', 'PROJECT_CATALOG_STEWARD', 'PROJECT_CATALOG_VIEWER', 'PROJECT_CONTRIBUTOR', 'PROJECT_OWNER']
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.MemberTypeDef'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CreateProjectPolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateProjectProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### domainUnitIdentifier
- **Type**: typing.Optional[str]

### environmentConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentConfigurationUnionTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateRuleInputTypeDef

### action
- **Type**: typing.Literal['CREATE_SUBSCRIPTION_REQUEST']
- **Required**: Yes

### detail
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleDetailUnionTypeDef'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleScopeUnionTypeDef'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleTargetTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateRuleOutputTypeDef

### action
- **Type**: typing.Literal['CREATE_SUBSCRIPTION_REQUEST']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### detail
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleDetailOutputTypeDef'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ruleType
- **Type**: typing.Literal['METADATA_FORM_ENFORCEMENT']
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleScopeOutputTypeDef'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleTargetTypeDef'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriptionGrantInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.GrantedEntityInputTypeDef'>
- **Required**: Yes

### assetTargetNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.AssetTargetNameMapTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### subscriptionTargetIdentifier
- **Type**: typing.Optional[str]


# CreateSubscriptionRequestInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### subscribedListings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingInputTypeDef]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalInputTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### metadataForms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FormInputTypeDef]]


# CreateUserProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### userType
- **Type**: typing.Optional[typing.Literal['IAM_ROLE', 'IAM_USER', 'SSO_USER']]


# CustomParameterTypeDef

### fieldType
- **Type**: <class 'str'>
- **Required**: Yes

### keyName
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### isEditable
- **Type**: typing.Optional[bool]

### isOptional
- **Type**: typing.Optional[bool]


# DataProductItemOutputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### itemType
- **Type**: typing.Literal['ASSET']
- **Required**: Yes

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### revision
- **Type**: typing.Optional[str]


# DataProductItemTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### itemType
- **Type**: typing.Literal['ASSET']
- **Required**: Yes

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### revision
- **Type**: typing.Optional[str]


# DataProductItemUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataProductListingItemAdditionalAttributesTypeDef

### forms
- **Type**: typing.Optional[str]


# DataProductListingItemTypeDef

### additionalAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataProductListingItemAdditionalAttributesTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.ListingSummaryItemTypeDef]]

### listingCreatedBy
- **Type**: typing.Optional[str]

### listingId
- **Type**: typing.Optional[str]

### listingRevision
- **Type**: typing.Optional[str]

### listingUpdatedBy
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]


# DataProductListingTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### dataProductId
- **Type**: typing.Optional[str]

### dataProductRevision
- **Type**: typing.Optional[str]

### forms
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.ListingSummaryTypeDef]]

### owningProjectId
- **Type**: typing.Optional[str]


# DataProductResultItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataProductRevisionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceConfigurationInputTypeDef

### glueRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueRunConfigurationInputTypeDef]

### redshiftRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftRunConfigurationInputTypeDef]

### sageMakerRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SageMakerRunConfigurationInputTypeDef]


# DataSourceConfigurationOutputTypeDef

### glueRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueRunConfigurationOutputTypeDef]

### redshiftRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftRunConfigurationOutputTypeDef]

### sageMakerRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SageMakerRunConfigurationOutputTypeDef]


# DataSourceErrorMessageTypeDef

### errorType
- **Type**: typing.Literal['ACCESS_DENIED_EXCEPTION', 'CONFLICT_EXCEPTION', 'INTERNAL_SERVER_EXCEPTION', 'RESOURCE_NOT_FOUND_EXCEPTION', 'SERVICE_QUOTA_EXCEEDED_EXCEPTION', 'THROTTLING_EXCEPTION', 'VALIDATION_EXCEPTION']
- **Required**: Yes

### errorDetail
- **Type**: typing.Optional[str]


# DataSourceRunActivityTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataAssetStatus
- **Type**: typing.Literal['FAILED', 'PUBLISHING_FAILED', 'SKIPPED_ALREADY_IMPORTED', 'SKIPPED_ARCHIVED', 'SKIPPED_NO_ACCESS', 'SUCCEEDED_CREATED', 'SUCCEEDED_UPDATED', 'UNCHANGED']
- **Required**: Yes

### dataSourceRunId
- **Type**: <class 'str'>
- **Required**: Yes

### database
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### technicalName
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataAssetId
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef]

### lineageSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LineageInfoTypeDef]

### technicalDescription
- **Type**: typing.Optional[str]


# DataSourceRunLineageSummaryTypeDef

### importStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIALLY_SUCCEEDED', 'SUCCESS']]


# DataSourceRunSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAssetFilterInputTypeDef

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssetInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssetTypeInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataProductInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### retainPermissionsOnRevokeFailure
- **Type**: typing.Optional[bool]


# DeleteDomainInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### skipDeletionCheck
- **Type**: typing.Optional[bool]


# DeleteDomainOutputTypeDef

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainUnitInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentActionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentBlueprintConfigurationInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFormTypeInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### formTypeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlossaryInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlossaryTermInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListingInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipDeletionCheck
- **Type**: typing.Optional[bool]


# DeleteProjectMembershipInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.MemberTypeDef'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionGrantInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionRequestInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionTargetInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTimeSeriesDataPointsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'LISTING']
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeploymentPropertiesTypeDef

### endTimeoutMinutes
- **Type**: typing.Optional[int]

### startTimeoutMinutes
- **Type**: typing.Optional[int]


# DeploymentTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### deploymentStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING_DEPLOYMENT', 'SUCCESSFUL']]

### deploymentType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]

### failureReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentErrorTypeDef]

### isDeploymentComplete
- **Type**: typing.Optional[bool]

### messages
- **Type**: typing.Optional[typing.List[str]]


# DetailedGlossaryTermTypeDef

### name
- **Type**: typing.Optional[str]

### shortDescription
- **Type**: typing.Optional[str]


# DisassociateEnvironmentRoleInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DomainSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainUnitFilterForProjectTypeDef

### domainUnit
- **Type**: <class 'str'>
- **Required**: Yes

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# DomainUnitGrantFilterOutputTypeDef

### allDomainUnitsGrantFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# DomainUnitGrantFilterTypeDef

### allDomainUnitsGrantFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# DomainUnitGroupPropertiesTypeDef

### groupId
- **Type**: typing.Optional[str]


# DomainUnitOwnerPropertiesTypeDef

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitGroupPropertiesTypeDef]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitUserPropertiesTypeDef]


# DomainUnitPolicyGrantPrincipalOutputTypeDef

### domainUnitDesignation
- **Type**: typing.Literal['OWNER']
- **Required**: Yes

### domainUnitGrantFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitGrantFilterOutputTypeDef]

### domainUnitIdentifier
- **Type**: typing.Optional[str]


# DomainUnitPolicyGrantPrincipalTypeDef

### domainUnitDesignation
- **Type**: typing.Literal['OWNER']
- **Required**: Yes

### domainUnitGrantFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitGrantFilterTypeDef]

### domainUnitIdentifier
- **Type**: typing.Optional[str]


# DomainUnitSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainUnitTargetTypeDef

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# DomainUnitUserPropertiesTypeDef

### userId
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentActionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentBlueprintConfigurationItemTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### enabledRegions
- **Type**: typing.Optional[typing.List[str]]

### environmentRolePermissionBoundary
- **Type**: typing.Optional[str]

### manageAccessRoleArn
- **Type**: typing.Optional[str]

### provisioningConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProvisioningConfigurationOutputTypeDef]]

### provisioningRoleArn
- **Type**: typing.Optional[str]

### regionalParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EnvironmentBlueprintSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentConfigurationParameterTypeDef

### isEditable
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EnvironmentConfigurationParametersDetailsOutputTypeDef

### parameterOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentConfigurationParameterTypeDef]]

### resolvedParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentConfigurationParameterTypeDef]]

### ssmPath
- **Type**: typing.Optional[str]


# EnvironmentConfigurationParametersDetailsTypeDef

### parameterOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentConfigurationParameterTypeDef]]

### resolvedParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentConfigurationParameterTypeDef]]

### ssmPath
- **Type**: typing.Optional[str]


# EnvironmentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentConfigurationUserParameterOutputTypeDef

### environmentConfigurationName
- **Type**: typing.Optional[str]

### environmentParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentParameterTypeDef]]


# EnvironmentConfigurationUserParameterTypeDef

### environmentConfigurationName
- **Type**: typing.Optional[str]

### environmentParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentParameterTypeDef]]


# EnvironmentConfigurationUserParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentDeploymentDetailsOutputTypeDef

### environmentFailureReasons
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentErrorTypeDef]]]

### overallDeploymentStatus
- **Type**: typing.Optional[typing.Literal['FAILED_DEPLOYMENT', 'FAILED_VALIDATION', 'IN_PROGRESS', 'PENDING_DEPLOYMENT', 'SUCCESSFUL']]


# EnvironmentDeploymentDetailsTypeDef

### environmentFailureReasons
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentErrorTypeDef]]]

### overallDeploymentStatus
- **Type**: typing.Optional[typing.Literal['FAILED_DEPLOYMENT', 'FAILED_VALIDATION', 'IN_PROGRESS', 'PENDING_DEPLOYMENT', 'SUCCESSFUL']]


# EnvironmentDeploymentDetailsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentErrorTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]


# EnvironmentParameterTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EnvironmentProfileSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EqualToExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# EventSummaryTypeDef

### openLineageRunEventSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OpenLineageRunEventSummaryTypeDef]


# FailureCauseTypeDef

### message
- **Type**: typing.Optional[str]


# FilterClausePaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterClauseTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterExpressionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterTypeDef

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# FormEntryInputTypeDef

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]


# FormEntryOutputTypeDef

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]


# FormInputTypeDef

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### typeIdentifier
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# FormOutputTypeDef

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### typeName
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# FormTypeDataTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### imports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.ImportTypeDef]]

### model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ModelTypeDef]

### originDomainId
- **Type**: typing.Optional[str]

### originProjectId
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GetAssetFilterInputTypeDef

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssetInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetAssetTypeInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetAssetTypeOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone_classes.FormEntryOutputTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### originDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### originProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### withSecret
- **Type**: typing.Optional[bool]


# GetDataProductInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetDataSourceInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceRunInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainUnitInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentActionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentBlueprintConfigurationInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentBlueprintConfigurationOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### enabledRegions
- **Type**: typing.List[str]
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRolePermissionBoundary
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### provisioningConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProvisioningConfigurationOutputTypeDef]
- **Required**: Yes

### provisioningRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### regionalParameters
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentBlueprintInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentCredentialsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentCredentialsOutputTypeDef

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### secretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFormTypeInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### formTypeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetFormTypeOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### imports
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ImportTypeDef]
- **Required**: Yes

### model
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ModelTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### originDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### originProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGlossaryInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlossaryTermInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIamPortalLoginUrlInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIamPortalLoginUrlOutputTypeDef

### authCodeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### userProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRunInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLineageEventInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLineageNodeInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### eventTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]


# GetListingInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### listingRevision
- **Type**: typing.Optional[str]


# GetMetadataGenerationRunInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetRuleOutputTypeDef

### action
- **Type**: typing.Literal['CREATE_SUBSCRIPTION_REQUEST']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### detail
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleDetailOutputTypeDef'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### ruleType
- **Type**: typing.Literal['METADATA_FORM_ENFORCEMENT']
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleScopeOutputTypeDef'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleTargetTypeDef'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionGrantInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionRequestDetailsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionTargetInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTimeSeriesDataPointInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'LISTING']
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTimeSeriesDataPointOutputTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'LISTING']
- **Required**: Yes

### form
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointFormOutputTypeDef'>
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlossaryItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GlossaryTermItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GlueConnectionInputTypeDef

### athenaProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AuthenticationConfigurationInputTypeDef]

### connectionProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### connectionType
- **Type**: typing.Optional[typing.Literal['BIGQUERY', 'DOCUMENTDB', 'DYNAMODB', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SQLSERVER', 'TERADATA', 'VERTICA']]

### description
- **Type**: typing.Optional[str]

### matchCriteria
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### physicalConnectionRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PhysicalConnectionRequirementsUnionTypeDef]

### pythonProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### sparkProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### validateCredentials
- **Type**: typing.Optional[bool]

### validateForComputeEnvironments
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]]


# GlueConnectionPatchTypeDef

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AuthenticationConfigurationPatchTypeDef]

### connectionProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### description
- **Type**: typing.Optional[str]


# GlueConnectionTypeDef

### athenaProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AuthenticationConfigurationTypeDef]

### compatibleComputeEnvironments
- **Type**: typing.Optional[typing.List[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]]

### connectionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### connectionSchemaVersion
- **Type**: typing.Optional[int]

### connectionType
- **Type**: typing.Optional[typing.Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### lastConnectionValidationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### matchCriteria
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]

### physicalConnectionRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PhysicalConnectionRequirementsOutputTypeDef]

### pythonProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### sparkProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'READY', 'UPDATE_FAILED', 'UPDATING']]

### statusReason
- **Type**: typing.Optional[str]


# GlueOAuth2CredentialsTypeDef

### accessToken
- **Type**: typing.Optional[str]

### jwtToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### userManagedClientApplicationClientSecret
- **Type**: typing.Optional[str]


# GluePropertiesInputTypeDef

### glueConnectionInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueConnectionInputTypeDef]


# GluePropertiesOutputTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'READY', 'UPDATE_FAILED', 'UPDATING']]


# GluePropertiesPatchTypeDef

### glueConnectionInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueConnectionPatchTypeDef]


# GlueRunConfigurationInputTypeDef

### relationalFilterConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.RelationalFilterConfigurationUnionTypeDef]
- **Required**: Yes

### autoImportDataQualityResult
- **Type**: typing.Optional[bool]

### catalogName
- **Type**: typing.Optional[str]

### dataAccessRole
- **Type**: typing.Optional[str]


# GlueRunConfigurationOutputTypeDef

### relationalFilterConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.RelationalFilterConfigurationOutputTypeDef]
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### autoImportDataQualityResult
- **Type**: typing.Optional[bool]

### catalogName
- **Type**: typing.Optional[str]

### dataAccessRole
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# GlueSelfGrantStatusOutputTypeDef

### selfGrantStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SelfGrantStatusDetailTypeDef]
- **Required**: Yes


# GrantedEntityInputTypeDef

### listing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ListingRevisionInputTypeDef]


# GrantedEntityTypeDef

### listing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ListingRevisionTypeDef]


# GreaterThanExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# GreaterThanOrEqualToExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# GroupDetailsTypeDef

### groupId
- **Type**: <class 'str'>
- **Required**: Yes


# GroupPolicyGrantPrincipalTypeDef

### groupIdentifier
- **Type**: typing.Optional[str]


# GroupProfileSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperPodPropertiesInputTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# HyperPodPropertiesOutputTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### clusterArn
- **Type**: typing.Optional[str]

### orchestrator
- **Type**: typing.Optional[typing.Literal['EKS', 'SLURM']]


# IamPropertiesInputTypeDef

### glueLineageSyncEnabled
- **Type**: typing.Optional[bool]


# IamPropertiesOutputTypeDef

### environmentId
- **Type**: typing.Optional[str]

### glueLineageSyncEnabled
- **Type**: typing.Optional[bool]


# IamPropertiesPatchTypeDef

### glueLineageSyncEnabled
- **Type**: typing.Optional[bool]


# IamUserProfileDetailsTypeDef

### arn
- **Type**: typing.Optional[str]


# ImportTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes


# InExpressionOutputTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# InExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# IsNotNullExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes


# IsNullExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes


# JobRunDetailsTypeDef

### lineageRunDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LineageRunDetailsTypeDef]


# JobRunErrorTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobRunSummaryTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### domainId
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.JobRunErrorTypeDef]

### jobId
- **Type**: typing.Optional[str]

### jobType
- **Type**: typing.Optional[typing.Literal['LINEAGE']]

### runId
- **Type**: typing.Optional[str]

### runMode
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SCHEDULED']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'CANCELED', 'FAILED', 'IN_PROGRESS', 'PARTIALLY_SUCCEEDED', 'SCHEDULED', 'SUCCESS', 'TIMED_OUT']]


# LakeFormationConfigurationOutputTypeDef

### locationRegistrationExcludeS3Locations
- **Type**: typing.Optional[typing.List[str]]

### locationRegistrationRole
- **Type**: typing.Optional[str]


# LakeFormationConfigurationTypeDef

### locationRegistrationExcludeS3Locations
- **Type**: typing.Optional[typing.Sequence[str]]

### locationRegistrationRole
- **Type**: typing.Optional[str]


# LakeFormationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LessThanExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# LessThanOrEqualToExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# LikeExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# LineageEventSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LineageInfoTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]

### eventStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'REQUESTED', 'SUCCESS']]


# LineageNodeSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LineageNodeTypeItemTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone_classes.FormEntryOutputTypeDef]
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# LineageRunDetailsTypeDef

### sqlQueryRunDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LineageSqlQueryRunDetailsTypeDef]


# LineageSqlQueryRunDetailsTypeDef

### errorMessages
- **Type**: typing.Optional[typing.List[str]]

### numQueriesFailed
- **Type**: typing.Optional[int]

### queryEndTime
- **Type**: typing.Optional[datetime.datetime]

### queryStartTime
- **Type**: typing.Optional[datetime.datetime]

### totalQueriesProcessed
- **Type**: typing.Optional[int]


# LineageSyncScheduleTypeDef

### schedule
- **Type**: typing.Optional[str]


# ListAssetFiltersInputPaginateTypeDef

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['INVALID', 'VALID']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListAssetFiltersInputTypeDef

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['INVALID', 'VALID']]


# ListAssetFiltersOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.AssetFilterSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssetRevisionsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListAssetRevisionsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssetRevisionsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.AssetRevisionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConnectionsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ConnectionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataProductRevisionsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListDataProductRevisionsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataProductRevisionsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.DataProductRevisionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourceRunActivitiesInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PUBLISHING_FAILED', 'SKIPPED_ALREADY_IMPORTED', 'SKIPPED_ARCHIVED', 'SKIPPED_NO_ACCESS', 'SUCCEEDED_CREATED', 'SUCCEEDED_UPDATED', 'UNCHANGED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListDataSourceRunActivitiesInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PUBLISHING_FAILED', 'SKIPPED_ALREADY_IMPORTED', 'SKIPPED_ARCHIVED', 'SKIPPED_NO_ACCESS', 'SUCCEEDED_CREATED', 'SUCCEEDED_UPDATED', 'UNCHANGED']]


# ListDataSourceRunActivitiesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.DataSourceRunActivityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourceRunsInputPaginateTypeDef

### dataSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListDataSourceRunsInputTypeDef

### dataSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']]


# ListDataSourceRunsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.DataSourceRunSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.DataSourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainUnitsForParentInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parentDomainUnitIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListDomainUnitsForParentInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parentDomainUnitIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDomainUnitsForParentOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsInputPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListDomainsInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']]


# ListDomainsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.DomainSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEntityOwnersInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEntityOwnersInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEntityOwnersOutputTypeDef

### owners
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.OwnerPropertiesOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentActionsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentActionsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentActionsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentActionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentBlueprintConfigurationsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentBlueprintConfigurationsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentBlueprintConfigurationItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentBlueprintsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### managed
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentBlueprintsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### managed
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentBlueprintsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentBlueprintSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentProfilesInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### environmentBlueprintIdentifier
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### projectIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentProfilesInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### environmentBlueprintIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### projectIdentifier
- **Type**: typing.Optional[str]


# ListEnvironmentProfilesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### environmentBlueprintIdentifier
- **Type**: typing.Optional[str]

### environmentProfileIdentifier
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### provider
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### environmentBlueprintIdentifier
- **Type**: typing.Optional[str]

### environmentProfileIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### provider
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']]


# ListEnvironmentsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'CANCELED', 'FAILED', 'IN_PROGRESS', 'PARTIALLY_SUCCEEDED', 'SCHEDULED', 'SUCCESS', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListJobRunsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'CANCELED', 'FAILED', 'IN_PROGRESS', 'PARTIALLY_SUCCEEDED', 'SCHEDULED', 'SUCCESS', 'TIMED_OUT']]


# ListJobRunsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.JobRunSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLineageEventsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### processingStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'REQUESTED', 'SUCCESS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### timestampAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### timestampBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListLineageEventsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### processingStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'REQUESTED', 'SUCCESS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### timestampAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### timestampBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]


# ListLineageEventsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.LineageEventSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLineageNodeHistoryInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Optional[typing.Literal['DOWNSTREAM', 'UPSTREAM']]

### eventTimestampGTE
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### eventTimestampLTE
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListLineageNodeHistoryInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Optional[typing.Literal['DOWNSTREAM', 'UPSTREAM']]

### eventTimestampGTE
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### eventTimestampLTE
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListLineageNodeHistoryOutputTypeDef

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.LineageNodeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetadataGenerationRunsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.MetadataGenerationRunItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationsOutputTypeDef

### notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.NotificationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyGrantsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT', 'ENVIRONMENT_BLUEPRINT_CONFIGURATION', 'ENVIRONMENT_PROFILE']
- **Required**: Yes

### policyType
- **Type**: typing.Literal['ADD_TO_PROJECT_MEMBER_POOL', 'CREATE_ASSET_TYPE', 'CREATE_DOMAIN_UNIT', 'CREATE_ENVIRONMENT', 'CREATE_ENVIRONMENT_FROM_BLUEPRINT', 'CREATE_ENVIRONMENT_PROFILE', 'CREATE_FORM_TYPE', 'CREATE_GLOSSARY', 'CREATE_PROJECT', 'CREATE_PROJECT_FROM_PROJECT_PROFILE', 'DELEGATE_CREATE_ENVIRONMENT_PROFILE', 'OVERRIDE_DOMAIN_UNIT_OWNERS', 'OVERRIDE_PROJECT_OWNERS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListPolicyGrantsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT', 'ENVIRONMENT_BLUEPRINT_CONFIGURATION', 'ENVIRONMENT_PROFILE']
- **Required**: Yes

### policyType
- **Type**: typing.Literal['ADD_TO_PROJECT_MEMBER_POOL', 'CREATE_ASSET_TYPE', 'CREATE_DOMAIN_UNIT', 'CREATE_ENVIRONMENT', 'CREATE_ENVIRONMENT_FROM_BLUEPRINT', 'CREATE_ENVIRONMENT_PROFILE', 'CREATE_FORM_TYPE', 'CREATE_GLOSSARY', 'CREATE_PROJECT', 'CREATE_PROJECT_FROM_PROJECT_PROFILE', 'DELEGATE_CREATE_ENVIRONMENT_PROFILE', 'OVERRIDE_DOMAIN_UNIT_OWNERS', 'OVERRIDE_PROJECT_OWNERS']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyGrantsOutputTypeDef

### grantList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.PolicyGrantMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectMembershipsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[typing.Literal['NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListProjectMembershipsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListProjectMembershipsOutputTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProjectMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectProfilesInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListProjectProfilesInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListProjectProfilesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProjectProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### userIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListProjectsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### userIdentifier
- **Type**: typing.Optional[str]


# ListProjectsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRulesInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### action
- **Type**: typing.Optional[typing.Literal['CREATE_SUBSCRIPTION_REQUEST']]

### assetTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### dataProduct
- **Type**: typing.Optional[bool]

### includeCascaded
- **Type**: typing.Optional[bool]

### projectIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ruleType
- **Type**: typing.Optional[typing.Literal['METADATA_FORM_ENFORCEMENT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListRulesInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### action
- **Type**: typing.Optional[typing.Literal['CREATE_SUBSCRIPTION_REQUEST']]

### assetTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### dataProduct
- **Type**: typing.Optional[bool]

### includeCascaded
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### projectIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ruleType
- **Type**: typing.Optional[typing.Literal['METADATA_FORM_ENFORCEMENT']]


# ListRulesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.RuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionGrantsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### subscribedListingId
- **Type**: typing.Optional[str]

### subscriptionId
- **Type**: typing.Optional[str]

### subscriptionTargetId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListSubscriptionGrantsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### subscribedListingId
- **Type**: typing.Optional[str]

### subscriptionId
- **Type**: typing.Optional[str]

### subscriptionTargetId
- **Type**: typing.Optional[str]


# ListSubscriptionGrantsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionGrantSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionRequestsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### approverProjectId
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']]

### subscribedListingId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListSubscriptionRequestsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### approverProjectId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']]

### subscribedListingId
- **Type**: typing.Optional[str]


# ListSubscriptionRequestsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionRequestSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionTargetsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListSubscriptionTargetsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListSubscriptionTargetsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionTargetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### approverProjectId
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CANCELLED', 'REVOKED']]

### subscribedListingId
- **Type**: typing.Optional[str]

### subscriptionRequestIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListSubscriptionsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### approverProjectId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT', 'UPDATED_AT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CANCELLED', 'REVOKED']]

### subscribedListingId
- **Type**: typing.Optional[str]

### subscriptionRequestIdentifier
- **Type**: typing.Optional[str]


# ListSubscriptionsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTimeSeriesDataPointsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'LISTING']
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### startedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListTimeSeriesDataPointsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'LISTING']
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef]


# ListTimeSeriesDataPointsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListingItemTypeDef

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetListingTypeDef]

### dataProductListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataProductListingTypeDef]


# ListingRevisionInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes


# ListingRevisionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListingSummaryItemTypeDef

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]

### listingId
- **Type**: typing.Optional[str]

### listingRevision
- **Type**: typing.Optional[str]


# ListingSummaryTypeDef

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]

### listingId
- **Type**: typing.Optional[str]

### listingRevision
- **Type**: typing.Optional[str]


# MemberDetailsTypeDef

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GroupDetailsTypeDef]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.UserDetailsTypeDef]


# MemberTypeDef

### groupIdentifier
- **Type**: typing.Optional[str]

### userIdentifier
- **Type**: typing.Optional[str]


# MetadataFormEnforcementDetailOutputTypeDef

### requiredMetadataForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.MetadataFormReferenceTypeDef]]


# MetadataFormEnforcementDetailTypeDef

### requiredMetadataForms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.MetadataFormReferenceTypeDef]]


# MetadataFormReferenceTypeDef

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes


# MetadataFormSummaryTypeDef

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### formName
- **Type**: typing.Optional[str]


# MetadataGenerationRunItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelTypeDef

### smithy
- **Type**: typing.Optional[str]


# NameIdentifierTypeDef

### name
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# NotEqualToExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# NotInExpressionOutputTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# NotInExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# NotLikeExpressionTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# NotificationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OAuth2ClientApplicationTypeDef

### aWSManagedClientApplicationReference
- **Type**: typing.Optional[str]

### userManagedClientApplicationClientId
- **Type**: typing.Optional[str]


# OAuth2PropertiesOutputTypeDef

### authorizationCodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AuthorizationCodePropertiesTypeDef]

### oAuth2ClientApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OAuth2ClientApplicationTypeDef]

### oAuth2Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueOAuth2CredentialsTypeDef]

### oAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### tokenUrl
- **Type**: typing.Optional[str]

### tokenUrlParametersMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# OAuth2PropertiesTypeDef

### authorizationCodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AuthorizationCodePropertiesTypeDef]

### oAuth2ClientApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OAuth2ClientApplicationTypeDef]

### oAuth2Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueOAuth2CredentialsTypeDef]

### oAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### tokenUrl
- **Type**: typing.Optional[str]

### tokenUrlParametersMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# OAuth2PropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OpenLineageRunEventSummaryTypeDef

### eventType
- **Type**: typing.Optional[typing.Literal['ABORT', 'COMPLETE', 'FAIL', 'OTHER', 'RUNNING', 'START']]

### inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.NameIdentifierTypeDef]]

### job
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.NameIdentifierTypeDef]

### outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.NameIdentifierTypeDef]]

### runId
- **Type**: typing.Optional[str]


# OverrideDomainUnitOwnersPolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# OverrideProjectOwnersPolicyGrantDetailTypeDef

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# OwnerGroupPropertiesOutputTypeDef

### groupId
- **Type**: typing.Optional[str]


# OwnerGroupPropertiesTypeDef

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# OwnerPropertiesOutputTypeDef

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OwnerGroupPropertiesOutputTypeDef]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OwnerUserPropertiesOutputTypeDef]


# OwnerPropertiesTypeDef

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OwnerGroupPropertiesTypeDef]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OwnerUserPropertiesTypeDef]


# OwnerUserPropertiesOutputTypeDef

### userId
- **Type**: typing.Optional[str]


# OwnerUserPropertiesTypeDef

### userIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhysicalConnectionRequirementsOutputTypeDef

### availabilityZone
- **Type**: typing.Optional[str]

### securityGroupIdList
- **Type**: typing.Optional[typing.List[str]]

### subnetId
- **Type**: typing.Optional[str]

### subnetIdList
- **Type**: typing.Optional[typing.List[str]]


# PhysicalConnectionRequirementsTypeDef

### availabilityZone
- **Type**: typing.Optional[str]

### securityGroupIdList
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetId
- **Type**: typing.Optional[str]

### subnetIdList
- **Type**: typing.Optional[typing.Sequence[str]]


# PhysicalConnectionRequirementsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PhysicalEndpointTypeDef

### awsLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AwsLocationTypeDef]

### glueConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueConnectionTypeDef]

### glueConnectionName
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['ATHENA', 'GLUE_INTERACTIVE_SESSION', 'HTTPS', 'JDBC', 'LIVY', 'ODBC', 'PRISM']]

### stage
- **Type**: typing.Optional[str]


# PolicyGrantDetailOutputTypeDef

### addToProjectMemberPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AddToProjectMemberPoolPolicyGrantDetailTypeDef]

### createAssetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateAssetTypePolicyGrantDetailTypeDef]

### createDomainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateDomainUnitPolicyGrantDetailTypeDef]

### createEnvironment
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createEnvironmentFromBlueprint
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createEnvironmentProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateEnvironmentProfilePolicyGrantDetailTypeDef]

### createFormType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateFormTypePolicyGrantDetailTypeDef]

### createGlossary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateGlossaryPolicyGrantDetailTypeDef]

### createProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateProjectPolicyGrantDetailTypeDef]

### createProjectFromProjectProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef]

### delegateCreateEnvironmentProfile
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### overrideDomainUnitOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OverrideDomainUnitOwnersPolicyGrantDetailTypeDef]

### overrideProjectOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OverrideProjectOwnersPolicyGrantDetailTypeDef]


# PolicyGrantDetailTypeDef

### addToProjectMemberPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AddToProjectMemberPoolPolicyGrantDetailTypeDef]

### createAssetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateAssetTypePolicyGrantDetailTypeDef]

### createDomainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateDomainUnitPolicyGrantDetailTypeDef]

### createEnvironment
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### createEnvironmentFromBlueprint
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### createEnvironmentProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateEnvironmentProfilePolicyGrantDetailTypeDef]

### createFormType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateFormTypePolicyGrantDetailTypeDef]

### createGlossary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateGlossaryPolicyGrantDetailTypeDef]

### createProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateProjectPolicyGrantDetailTypeDef]

### createProjectFromProjectProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CreateProjectFromProjectProfilePolicyGrantDetailTypeDef]

### delegateCreateEnvironmentProfile
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### overrideDomainUnitOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OverrideDomainUnitOwnersPolicyGrantDetailTypeDef]

### overrideProjectOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.OverrideProjectOwnersPolicyGrantDetailTypeDef]


# PolicyGrantDetailUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PolicyGrantMemberTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### detail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PolicyGrantDetailOutputTypeDef]

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PolicyGrantPrincipalOutputTypeDef]


# PolicyGrantPrincipalOutputTypeDef

### domainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitPolicyGrantPrincipalOutputTypeDef]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GroupPolicyGrantPrincipalTypeDef]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ProjectPolicyGrantPrincipalTypeDef]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.UserPolicyGrantPrincipalOutputTypeDef]


# PolicyGrantPrincipalTypeDef

### domainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitPolicyGrantPrincipalTypeDef]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GroupPolicyGrantPrincipalTypeDef]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ProjectPolicyGrantPrincipalTypeDef]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.UserPolicyGrantPrincipalTypeDef]


# PolicyGrantPrincipalUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PostLineageEventInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.BlobTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PostTimeSeriesDataPointsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'LISTING']
- **Required**: Yes

### forms
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointFormInputTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PostTimeSeriesDataPointsOutputTypeDef

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ASSET', 'LISTING']
- **Required**: Yes

### forms
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointFormOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PredictionConfigurationTypeDef

### businessNameGeneration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.BusinessNameGenerationConfigurationTypeDef]


# ProjectDeletionErrorTypeDef

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ProjectGrantFilterTypeDef

### domainUnitFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitFilterForProjectTypeDef]


# ProjectMemberTypeDef

### designation
- **Type**: typing.Literal['PROJECT_CATALOG_CONSUMER', 'PROJECT_CATALOG_STEWARD', 'PROJECT_CATALOG_VIEWER', 'PROJECT_CONTRIBUTOR', 'PROJECT_OWNER']
- **Required**: Yes

### memberDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.MemberDetailsTypeDef'>
- **Required**: Yes


# ProjectPolicyGrantPrincipalTypeDef

### projectDesignation
- **Type**: typing.Literal['CONTRIBUTOR', 'OWNER', 'PROJECT_CATALOG_STEWARD']
- **Required**: Yes

### projectGrantFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ProjectGrantFilterTypeDef]

### projectIdentifier
- **Type**: typing.Optional[str]


# ProjectProfileSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectsForRuleOutputTypeDef

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificProjects
- **Type**: typing.Optional[typing.List[str]]


# ProjectsForRuleTypeDef

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificProjects
- **Type**: typing.Optional[typing.Sequence[str]]


# ProvisioningConfigurationOutputTypeDef

### lakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LakeFormationConfigurationOutputTypeDef]


# ProvisioningConfigurationTypeDef

### lakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LakeFormationConfigurationUnionTypeDef]


# ProvisioningConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisioningPropertiesTypeDef

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CloudFormationPropertiesTypeDef]


# PutEnvironmentBlueprintConfigurationInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### enabledRegions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRolePermissionBoundary
- **Type**: typing.Optional[str]

### manageAccessRoleArn
- **Type**: typing.Optional[str]

### provisioningConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.ProvisioningConfigurationUnionTypeDef]]

### provisioningRoleArn
- **Type**: typing.Optional[str]

### regionalParameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]


# PutEnvironmentBlueprintConfigurationOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### enabledRegions
- **Type**: typing.List[str]
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRolePermissionBoundary
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### provisioningConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProvisioningConfigurationOutputTypeDef]
- **Required**: Yes

### provisioningRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### regionalParameters
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecommendationConfigurationTypeDef

### enableBusinessNameGeneration
- **Type**: typing.Optional[bool]


# RedshiftClusterStorageTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftCredentialConfigurationTypeDef

### secretManagerArn
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftCredentialsTypeDef

### secretArn
- **Type**: typing.Optional[str]

### usernamePassword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.UsernamePasswordTypeDef]


# RedshiftLineageSyncConfigurationInputTypeDef

### enabled
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LineageSyncScheduleTypeDef]


# RedshiftLineageSyncConfigurationOutputTypeDef

### enabled
- **Type**: typing.Optional[bool]

### lineageJobId
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LineageSyncScheduleTypeDef]


# RedshiftPropertiesInputTypeDef

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftCredentialsTypeDef]

### databaseName
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[str]

### lineageSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftLineageSyncConfigurationInputTypeDef]

### port
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftStoragePropertiesTypeDef]


# RedshiftPropertiesOutputTypeDef

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftCredentialsTypeDef]

### databaseName
- **Type**: typing.Optional[str]

### isProvisionedSecret
- **Type**: typing.Optional[bool]

### jdbcIamUrl
- **Type**: typing.Optional[str]

### jdbcUrl
- **Type**: typing.Optional[str]

### lineageSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftLineageSyncConfigurationOutputTypeDef]

### redshiftTempDir
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'READY', 'UPDATE_FAILED', 'UPDATING']]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftStoragePropertiesTypeDef]


# RedshiftPropertiesPatchTypeDef

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftCredentialsTypeDef]

### databaseName
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[str]

### lineageSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftLineageSyncConfigurationInputTypeDef]

### port
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftStoragePropertiesTypeDef]


# RedshiftRunConfigurationInputTypeDef

### relationalFilterConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.RelationalFilterConfigurationUnionTypeDef]
- **Required**: Yes

### dataAccessRole
- **Type**: typing.Optional[str]

### redshiftCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftCredentialConfigurationTypeDef]

### redshiftStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftStorageTypeDef]


# RedshiftRunConfigurationOutputTypeDef

### redshiftStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RedshiftStorageTypeDef'>
- **Required**: Yes

### relationalFilterConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.RelationalFilterConfigurationOutputTypeDef]
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### dataAccessRole
- **Type**: typing.Optional[str]

### redshiftCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftCredentialConfigurationTypeDef]

### region
- **Type**: typing.Optional[str]


# RedshiftSelfGrantStatusOutputTypeDef

### selfGrantStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SelfGrantStatusDetailTypeDef]
- **Required**: Yes


# RedshiftServerlessStorageTypeDef

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftStoragePropertiesTypeDef

### clusterName
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]


# RedshiftStorageTypeDef

### redshiftClusterSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftClusterStorageTypeDef]

### redshiftServerlessSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftServerlessStorageTypeDef]


# RegionTypeDef

### regionName
- **Type**: typing.Optional[str]

### regionNamePath
- **Type**: typing.Optional[str]


# RejectChoiceTypeDef

### predictionTarget
- **Type**: <class 'str'>
- **Required**: Yes

### predictionChoices
- **Type**: typing.Optional[typing.Sequence[int]]


# RejectPredictionsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### rejectChoices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.RejectChoiceTypeDef]]

### rejectRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RejectRuleTypeDef]

### revision
- **Type**: typing.Optional[str]


# RejectPredictionsOutputTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetRevision
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RejectRuleTypeDef

### rule
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]

### threshold
- **Type**: typing.Optional[float]


# RejectSubscriptionRequestInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: typing.Optional[str]


# RelationalFilterConfigurationOutputTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.FilterExpressionTypeDef]]

### schemaName
- **Type**: typing.Optional[str]


# RelationalFilterConfigurationTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FilterExpressionTypeDef]]

### schemaName
- **Type**: typing.Optional[str]


# RelationalFilterConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemoveEntityOwnerInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### owner
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.OwnerPropertiesTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# RemovePolicyGrantInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['DOMAIN_UNIT', 'ENVIRONMENT_BLUEPRINT_CONFIGURATION', 'ENVIRONMENT_PROFILE']
- **Required**: Yes

### policyType
- **Type**: typing.Literal['ADD_TO_PROJECT_MEMBER_POOL', 'CREATE_ASSET_TYPE', 'CREATE_DOMAIN_UNIT', 'CREATE_ENVIRONMENT', 'CREATE_ENVIRONMENT_FROM_BLUEPRINT', 'CREATE_ENVIRONMENT_PROFILE', 'CREATE_FORM_TYPE', 'CREATE_GLOSSARY', 'CREATE_PROJECT', 'CREATE_PROJECT_FROM_PROJECT_PROFILE', 'DELEGATE_CREATE_ENVIRONMENT_PROFILE', 'OVERRIDE_DOMAIN_UNIT_OWNERS', 'OVERRIDE_PROJECT_OWNERS']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.PolicyGrantPrincipalUnionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


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


# RevokeSubscriptionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### retainPermissions
- **Type**: typing.Optional[bool]


# RowFilterConfigurationOutputTypeDef

### rowFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RowFilterOutputTypeDef'>
- **Required**: Yes

### sensitive
- **Type**: typing.Optional[bool]


# RowFilterConfigurationTypeDef

### rowFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RowFilterTypeDef'>
- **Required**: Yes

### sensitive
- **Type**: typing.Optional[bool]


# RowFilterOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RowFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleDetailOutputTypeDef

### metadataFormEnforcementDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.MetadataFormEnforcementDetailOutputTypeDef]


# RuleDetailTypeDef

### metadataFormEnforcementDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.MetadataFormEnforcementDetailTypeDef]


# RuleDetailUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleScopeOutputTypeDef

### assetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetTypesForRuleOutputTypeDef]

### dataProduct
- **Type**: typing.Optional[bool]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ProjectsForRuleOutputTypeDef]


# RuleScopeTypeDef

### assetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetTypesForRuleTypeDef]

### dataProduct
- **Type**: typing.Optional[bool]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ProjectsForRuleTypeDef]


# RuleScopeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleSummaryTypeDef

### action
- **Type**: typing.Optional[typing.Literal['CREATE_SUBSCRIPTION_REQUEST']]

### identifier
- **Type**: typing.Optional[str]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]

### ruleType
- **Type**: typing.Optional[typing.Literal['METADATA_FORM_ENFORCEMENT']]

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RuleScopeOutputTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RuleTargetTypeDef]

### targetType
- **Type**: typing.Optional[typing.Literal['DOMAIN_UNIT']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# RuleTargetTypeDef

### domainUnitTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DomainUnitTargetTypeDef]


# RunStatisticsForAssetsTypeDef

### added
- **Type**: typing.Optional[int]

### failed
- **Type**: typing.Optional[int]

### skipped
- **Type**: typing.Optional[int]

### unchanged
- **Type**: typing.Optional[int]

### updated
- **Type**: typing.Optional[int]


# SageMakerRunConfigurationInputTypeDef

### trackingAssets
- **Type**: typing.Mapping[str, typing.Sequence[str]]
- **Required**: Yes


# SageMakerRunConfigurationOutputTypeDef

### trackingAssets
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# ScheduleConfigurationTypeDef

### schedule
- **Type**: typing.Optional[str]

### timezone
- **Type**: typing.Optional[typing.Literal['AFRICA_JOHANNESBURG', 'AMERICA_MONTREAL', 'AMERICA_SAO_PAULO', 'ASIA_BAHRAIN', 'ASIA_BANGKOK', 'ASIA_CALCUTTA', 'ASIA_DUBAI', 'ASIA_HONG_KONG', 'ASIA_JAKARTA', 'ASIA_KUALA_LUMPUR', 'ASIA_SEOUL', 'ASIA_SHANGHAI', 'ASIA_SINGAPORE', 'ASIA_TAIPEI', 'ASIA_TOKYO', 'AUSTRALIA_MELBOURNE', 'AUSTRALIA_SYDNEY', 'CANADA_CENTRAL', 'CET', 'CST6CDT', 'ETC_GMT', 'ETC_GMT0', 'ETC_GMT_ADD_0', 'ETC_GMT_ADD_1', 'ETC_GMT_ADD_10', 'ETC_GMT_ADD_11', 'ETC_GMT_ADD_12', 'ETC_GMT_ADD_2', 'ETC_GMT_ADD_3', 'ETC_GMT_ADD_4', 'ETC_GMT_ADD_5', 'ETC_GMT_ADD_6', 'ETC_GMT_ADD_7', 'ETC_GMT_ADD_8', 'ETC_GMT_ADD_9', 'ETC_GMT_NEG_0', 'ETC_GMT_NEG_1', 'ETC_GMT_NEG_10', 'ETC_GMT_NEG_11', 'ETC_GMT_NEG_12', 'ETC_GMT_NEG_13', 'ETC_GMT_NEG_14', 'ETC_GMT_NEG_2', 'ETC_GMT_NEG_3', 'ETC_GMT_NEG_4', 'ETC_GMT_NEG_5', 'ETC_GMT_NEG_6', 'ETC_GMT_NEG_7', 'ETC_GMT_NEG_8', 'ETC_GMT_NEG_9', 'EUROPE_DUBLIN', 'EUROPE_LONDON', 'EUROPE_PARIS', 'EUROPE_STOCKHOLM', 'EUROPE_ZURICH', 'ISRAEL', 'MEXICO_GENERAL', 'MST7MDT', 'PACIFIC_AUCKLAND', 'US_CENTRAL', 'US_EASTERN', 'US_MOUNTAIN', 'US_PACIFIC', 'UTC']]


# SearchGroupProfilesInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupType
- **Type**: typing.Literal['DATAZONE_SSO_GROUP', 'SSO_GROUP']
- **Required**: Yes

### searchText
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# SearchGroupProfilesInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupType
- **Type**: typing.Literal['DATAZONE_SSO_GROUP', 'SSO_GROUP']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchText
- **Type**: typing.Optional[str]


# SearchGroupProfilesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.GroupProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchInItemTypeDef

### attribute
- **Type**: <class 'str'>
- **Required**: Yes


# SearchInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET', 'DATA_PRODUCT', 'GLOSSARY', 'GLOSSARY_TERM']
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClausePaginatorTypeDef]

### owningProjectIdentifier
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# SearchInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET', 'DATA_PRODUCT', 'GLOSSARY', 'GLOSSARY_TERM']
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClauseTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### owningProjectIdentifier
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]


# SearchInventoryResultItemTypeDef

### assetItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetItemTypeDef]

### dataProductItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataProductResultItemTypeDef]

### glossaryItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlossaryItemTypeDef]

### glossaryTermItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlossaryTermItemTypeDef]


# SearchListingsInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClausePaginatorTypeDef]

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# SearchListingsInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClauseTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]


# SearchListingsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SearchResultItemTypeDef]
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SearchInventoryResultItemTypeDef]
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchResultItemTypeDef

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetListingItemTypeDef]

### dataProductListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataProductListingItemTypeDef]


# SearchSortTypeDef

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SearchTypesInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### managed
- **Type**: <class 'bool'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET_TYPE', 'FORM_TYPE', 'LINEAGE_NODE_TYPE']
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClausePaginatorTypeDef]

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# SearchTypesInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### managed
- **Type**: <class 'bool'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET_TYPE', 'FORM_TYPE', 'LINEAGE_NODE_TYPE']
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClauseTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]


# SearchTypesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SearchTypesResultItemTypeDef]
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchTypesResultItemTypeDef

### assetTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetTypeItemTypeDef]

### formTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FormTypeDataTypeDef]

### lineageNodeTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LineageNodeTypeItemTypeDef]


# SearchUserProfilesInputPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userType
- **Type**: typing.Literal['DATAZONE_IAM_USER', 'DATAZONE_SSO_USER', 'DATAZONE_USER', 'SSO_USER']
- **Required**: Yes

### searchText
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# SearchUserProfilesInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userType
- **Type**: typing.Literal['DATAZONE_IAM_USER', 'DATAZONE_SSO_USER', 'DATAZONE_USER', 'SSO_USER']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchText
- **Type**: typing.Optional[str]


# SearchUserProfilesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.UserProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SelfGrantStatusDetailTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['GRANTED', 'GRANT_FAILED', 'GRANT_IN_PROGRESS', 'GRANT_PENDING', 'REVOKE_FAILED', 'REVOKE_IN_PROGRESS', 'REVOKE_PENDING']
- **Required**: Yes

### failureCause
- **Type**: typing.Optional[str]

### schemaName
- **Type**: typing.Optional[str]


# SelfGrantStatusOutputTypeDef

### glueSelfGrantStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueSelfGrantStatusOutputTypeDef]

### redshiftSelfGrantStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftSelfGrantStatusOutputTypeDef]


# SingleSignOnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SparkEmrPropertiesInputTypeDef

### computeArn
- **Type**: typing.Optional[str]

### instanceProfileArn
- **Type**: typing.Optional[str]

### javaVirtualEnv
- **Type**: typing.Optional[str]

### logUri
- **Type**: typing.Optional[str]

### pythonVirtualEnv
- **Type**: typing.Optional[str]

### runtimeRole
- **Type**: typing.Optional[str]

### trustedCertificatesS3Uri
- **Type**: typing.Optional[str]


# SparkEmrPropertiesOutputTypeDef

### computeArn
- **Type**: typing.Optional[str]

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.UsernamePasswordTypeDef]

### credentialsExpiration
- **Type**: typing.Optional[datetime.datetime]

### governanceType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'USER_MANAGED']]

### instanceProfileArn
- **Type**: typing.Optional[str]

### javaVirtualEnv
- **Type**: typing.Optional[str]

### livyEndpoint
- **Type**: typing.Optional[str]

### logUri
- **Type**: typing.Optional[str]

### pythonVirtualEnv
- **Type**: typing.Optional[str]

### runtimeRole
- **Type**: typing.Optional[str]

### trustedCertificatesS3Uri
- **Type**: typing.Optional[str]


# SparkEmrPropertiesPatchTypeDef

### computeArn
- **Type**: typing.Optional[str]

### instanceProfileArn
- **Type**: typing.Optional[str]

### javaVirtualEnv
- **Type**: typing.Optional[str]

### logUri
- **Type**: typing.Optional[str]

### pythonVirtualEnv
- **Type**: typing.Optional[str]

### runtimeRole
- **Type**: typing.Optional[str]

### trustedCertificatesS3Uri
- **Type**: typing.Optional[str]


# SparkGlueArgsTypeDef

### connection
- **Type**: typing.Optional[str]


# SparkGluePropertiesInputTypeDef

### additionalArgs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SparkGlueArgsTypeDef]

### glueConnectionName
- **Type**: typing.Optional[str]

### glueVersion
- **Type**: typing.Optional[str]

### idleTimeout
- **Type**: typing.Optional[int]

### javaVirtualEnv
- **Type**: typing.Optional[str]

### numberOfWorkers
- **Type**: typing.Optional[int]

### pythonVirtualEnv
- **Type**: typing.Optional[str]

### workerType
- **Type**: typing.Optional[str]


# SparkGluePropertiesOutputTypeDef

### additionalArgs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SparkGlueArgsTypeDef]

### glueConnectionName
- **Type**: typing.Optional[str]

### glueVersion
- **Type**: typing.Optional[str]

### idleTimeout
- **Type**: typing.Optional[int]

### javaVirtualEnv
- **Type**: typing.Optional[str]

### numberOfWorkers
- **Type**: typing.Optional[int]

### pythonVirtualEnv
- **Type**: typing.Optional[str]

### workerType
- **Type**: typing.Optional[str]


# SsoUserProfileDetailsTypeDef

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### username
- **Type**: typing.Optional[str]


# StartDataSourceRunInputTypeDef

### dataSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# SubscribedAssetListingTypeDef

### assetScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetScopeTypeDef]

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### entityType
- **Type**: typing.Optional[str]

### forms
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]


# SubscribedAssetTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetRevision
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['GRANTED', 'GRANT_FAILED', 'GRANT_IN_PROGRESS', 'GRANT_PENDING', 'REVOKED', 'REVOKE_FAILED', 'REVOKE_IN_PROGRESS', 'REVOKE_PENDING']
- **Required**: Yes

### assetScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetScopeTypeDef]

### failureCause
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FailureCauseTypeDef]

### failureTimestamp
- **Type**: typing.Optional[datetime.datetime]

### grantedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### targetName
- **Type**: typing.Optional[str]


# SubscribedListingInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# SubscribedListingItemTypeDef

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SubscribedAssetListingTypeDef]

### productListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SubscribedProductListingTypeDef]


# SubscribedPrincipalInputTypeDef

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SubscribedProjectInputTypeDef]


# SubscribedPrincipalTypeDef

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SubscribedProjectTypeDef]


# SubscribedProductListingTypeDef

### assetListings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.AssetInDataProductListingItemTypeDef]]

### description
- **Type**: typing.Optional[str]

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DetailedGlossaryTermTypeDef]]

### name
- **Type**: typing.Optional[str]


# SubscribedProjectInputTypeDef

### identifier
- **Type**: typing.Optional[str]


# SubscribedProjectTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubscriptionGrantSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubscriptionRequestSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubscriptionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubscriptionTargetFormTypeDef

### content
- **Type**: <class 'str'>
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes


# SubscriptionTargetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TermRelationsOutputTypeDef

### classifies
- **Type**: typing.Optional[typing.List[str]]

### isA
- **Type**: typing.Optional[typing.List[str]]


# TermRelationsTypeDef

### classifies
- **Type**: typing.Optional[typing.Sequence[str]]

### isA
- **Type**: typing.Optional[typing.Sequence[str]]


# TermRelationsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeSeriesDataPointFormInputTypeDef

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.TimestampTypeDef'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# TimeSeriesDataPointFormOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeSeriesDataPointSummaryFormOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicTypeDef

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.NotificationResourceTypeDef'>
- **Required**: Yes

### role
- **Type**: typing.Literal['DOMAIN_OWNER', 'PROJECT_CONTRIBUTOR', 'PROJECT_OWNER', 'PROJECT_SUBSCRIBER', 'PROJECT_VIEWER']
- **Required**: Yes

### subject
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAssetFilterInputTypeDef

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetFilterConfigurationUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateConnectionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AwsLocationTypeDef]

### description
- **Type**: typing.Optional[str]

### props
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ConnectionPropertiesPatchTypeDef]


# UpdateDataSourceInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### assetFormsInput
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FormInputTypeDef]]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataSourceConfigurationInputTypeDef]

### description
- **Type**: typing.Optional[str]

### enableSetting
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### name
- **Type**: typing.Optional[str]

### publishOnImport
- **Type**: typing.Optional[bool]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RecommendationConfigurationTypeDef]

### retainPermissionsOnRevokeFailure
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ScheduleConfigurationTypeDef]


# UpdateDomainInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### domainExecutionRole
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serviceRole
- **Type**: typing.Optional[str]

### singleSignOn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SingleSignOnTypeDef]


# UpdateDomainUnitInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateEnvironmentActionInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ActionParametersTypeDef]


# UpdateEnvironmentInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### name
- **Type**: typing.Optional[str]


# UpdateEnvironmentProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### userParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentParameterTypeDef]]


# UpdateGlossaryInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateGlossaryTermInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryIdentifier
- **Type**: typing.Optional[str]

### longDescription
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### shortDescription
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### termRelations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TermRelationsUnionTypeDef]


# UpdateGroupProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'NOT_ASSIGNED']
- **Required**: Yes


# UpdateProjectInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### environmentDeploymentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentDeploymentDetailsUnionTypeDef]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### name
- **Type**: typing.Optional[str]


# UpdateProjectProfileInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### domainUnitIdentifier
- **Type**: typing.Optional[str]

### environmentConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentConfigurationUnionTypeDef]]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateRuleInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### detail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RuleDetailUnionTypeDef]

### includeChildDomainUnits
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RuleScopeUnionTypeDef]


# UpdateRuleOutputTypeDef

### action
- **Type**: typing.Literal['CREATE_SUBSCRIPTION_REQUEST']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### detail
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleDetailOutputTypeDef'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### ruleType
- **Type**: typing.Literal['METADATA_FORM_ENFORCEMENT']
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleScopeOutputTypeDef'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RuleTargetTypeDef'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSubscriptionGrantStatusInputTypeDef

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['GRANTED', 'GRANT_FAILED', 'GRANT_IN_PROGRESS', 'GRANT_PENDING', 'REVOKED', 'REVOKE_FAILED', 'REVOKE_IN_PROGRESS', 'REVOKE_PENDING']
- **Required**: Yes

### failureCause
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FailureCauseTypeDef]

### targetName
- **Type**: typing.Optional[str]


# UpdateSubscriptionRequestInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSubscriptionTargetInputTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### applicableAssetTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### authorizedPrincipals
- **Type**: typing.Optional[typing.Sequence[str]]

### manageAccessRole
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### provider
- **Type**: typing.Optional[str]

### subscriptionTargetConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionTargetFormTypeDef]]


# UserDetailsTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# UserPolicyGrantPrincipalOutputTypeDef

### allUsersGrantFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### userIdentifier
- **Type**: typing.Optional[str]


# UserPolicyGrantPrincipalTypeDef

### allUsersGrantFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### userIdentifier
- **Type**: typing.Optional[str]


# UserProfileDetailsTypeDef

### iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.IamUserProfileDetailsTypeDef]

### sso
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SsoUserProfileDetailsTypeDef]


# UserProfileSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsernamePasswordTypeDef

### password
- **Type**: <class 'str'>
- **Required**: Yes

### username
- **Type**: <class 'str'>
- **Required**: Yes


