# Datazone Classes

# AcceptChoice

### predictionTarget
- **Type**: <class 'str'>
- **Required**: Yes

### editedValue
- **Type**: typing.Optional[str]

### predictionChoice
- **Type**: typing.Optional[int]


# AcceptPredictionsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### acceptChoices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.AcceptChoice]]

### acceptRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AcceptRule]

### clientToken
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]


# AcceptPredictionsOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# AcceptRule

### rule
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]

### threshold
- **Type**: typing.Optional[float]


# AcceptSubscriptionRequestInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### assetScopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.AcceptedAssetScope]]

### decisionComment
- **Type**: typing.Optional[str]


# AcceptSubscriptionRequestOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### existingSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadataForms
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### reviewerId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### subscribedListings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# AcceptedAssetScope

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### filterIds
- **Type**: typing.List[str]
- **Required**: Yes


# ActionParameters

### awsConsoleLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AwsConsoleLinkParameters]


# AddEntityOwnerInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.OwnerProperties'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AddPolicyGrantInput

### detail
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantDetail, aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantDetailOutput]
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantPrincipal, aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantPrincipalOutput]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AddToProjectMemberPoolPolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# AssetFilterConfiguration

### columnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ColumnFilterConfiguration]

### rowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RowFilterConfiguration]


# AssetFilterConfigurationOutput

### columnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ColumnFilterConfigurationOutput]

### rowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RowFilterConfigurationOutput]


# AssetFilterSummary

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### effectiveColumnNames
- **Type**: typing.Optional[typing.List[str]]

### effectiveRowFilter
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['INVALID', 'VALID']]


# AssetInDataProductListingItem

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### entityType
- **Type**: typing.Optional[str]


# AssetItem

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetItemAdditionalAttributes]

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


# AssetItemAdditionalAttributes

### formsOutput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]]

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointSummaryFormOutput]]

### readOnlyFormsOutput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]]


# AssetListing

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]

### latestTimeSeriesDataPointForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointSummaryFormOutput]]

### owningProjectId
- **Type**: typing.Optional[str]


# AssetListingDetails

### listingId
- **Type**: <class 'str'>
- **Required**: Yes

### listingStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'INACTIVE']
- **Required**: Yes


# AssetListingItem

### additionalAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetListingItemAdditionalAttributes]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]

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


# AssetListingItemAdditionalAttributes

### forms
- **Type**: typing.Optional[str]

### latestTimeSeriesDataPointForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointSummaryFormOutput]]


# AssetRevision

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### domainId
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]


# AssetScope

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


# AssetTargetNameMap

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### targetName
- **Type**: <class 'str'>
- **Required**: Yes


# AssetTypeItem

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone.datazone_classes.FormEntryOutput]
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


# AssetTypesForRule

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificAssetTypes
- **Type**: typing.Optional[typing.List[str]]


# AssetTypesForRuleOutput

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificAssetTypes
- **Type**: typing.Optional[typing.List[str]]


# AssociateEnvironmentRoleInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AthenaPropertiesInput

### workgroupName
- **Type**: typing.Optional[str]


# AthenaPropertiesOutput

### workgroupName
- **Type**: typing.Optional[str]


# AthenaPropertiesPatch

### workgroupName
- **Type**: typing.Optional[str]


# AuthenticationConfiguration

### authenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'OAUTH2']]

### oAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OAuth2PropertiesOutput]

### secretArn
- **Type**: typing.Optional[str]


# AuthenticationConfigurationInput

### authenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'OAUTH2']]

### basicAuthenticationCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.BasicAuthenticationCredentials]

### customAuthenticationCredentials
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]

### oAuth2Properties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.OAuth2Properties, aws_resource_validator.pydantic_models.datazone.datazone_classes.OAuth2PropertiesOutput, NoneType]

### secretArn
- **Type**: typing.Optional[str]


# AuthenticationConfigurationPatch

### basicAuthenticationCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.BasicAuthenticationCredentials]

### secretArn
- **Type**: typing.Optional[str]


# AuthorizationCodeProperties

### authorizationCode
- **Type**: typing.Optional[str]

### redirectUri
- **Type**: typing.Optional[str]


# AwsAccount

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountIdPath
- **Type**: typing.Optional[str]


# AwsConsoleLinkParameters

### uri
- **Type**: typing.Optional[str]


# AwsLocation

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

# BasicAuthenticationCredentials

### password
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]


# BusinessNameGenerationConfiguration

### enabled
- **Type**: typing.Optional[bool]


# CancelMetadataGenerationRunInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSubscriptionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSubscriptionOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### retainPermissions
- **Type**: <class 'bool'>
- **Required**: Yes

### status
- **Type**: typing.Literal['APPROVED', 'CANCELLED', 'REVOKED']
- **Required**: Yes

### subscribedListing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal'>
- **Required**: Yes

### subscriptionRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CloudFormationProperties

### templateUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ColumnFilterConfiguration

### includedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnFilterConfigurationOutput

### includedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ConfigurableActionParameter

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ConfigurableEnvironmentAction

### parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConfigurableActionParameter]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### auth
- **Type**: typing.Optional[typing.Literal['HTTPS', 'IAM']]


# ConnectionCredentials

### accessKeyId
- **Type**: typing.Optional[str]

### expiration
- **Type**: typing.Optional[datetime.datetime]

### secretAccessKey
- **Type**: typing.Optional[str]

### sessionToken
- **Type**: typing.Optional[str]


# ConnectionPropertiesInput

### athenaProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AthenaPropertiesInput]

### glueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GluePropertiesInput]

### hyperPodProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.HyperPodPropertiesInput]

### iamProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IamPropertiesInput]

### redshiftProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftPropertiesInput]

### sparkEmrProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SparkEmrPropertiesInput]

### sparkGlueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SparkGluePropertiesInput]


# ConnectionPropertiesOutput

### athenaProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AthenaPropertiesOutput]

### glueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GluePropertiesOutput]

### hyperPodProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.HyperPodPropertiesOutput]

### iamProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IamPropertiesOutput]

### redshiftProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftPropertiesOutput]

### sparkEmrProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SparkEmrPropertiesOutput]

### sparkGlueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SparkGluePropertiesOutput]


# ConnectionPropertiesPatch

### athenaProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AthenaPropertiesPatch]

### glueProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GluePropertiesPatch]

### iamProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IamPropertiesPatch]

### redshiftProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftPropertiesPatch]

### sparkEmrProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SparkEmrPropertiesPatch]


# ConnectionSummary

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### physicalEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.PhysicalEndpoint]
- **Required**: Yes

### type
- **Type**: typing.Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA']
- **Required**: Yes

### environmentId
- **Type**: typing.Optional[str]

### projectId
- **Type**: typing.Optional[str]

### props
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionPropertiesOutput]


# CreateAssetFilterInput

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterConfigurationOutput]
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


# CreateAssetFilterOutput

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterConfigurationOutput'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### effectiveColumnNames
- **Type**: typing.List[str]
- **Required**: Yes

### effectiveRowFilter
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['INVALID', 'VALID']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormInput]]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### predictionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PredictionConfiguration]

### typeRevision
- **Type**: typing.Optional[str]


# CreateAssetOutput

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

### externalIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### firstRevisionCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### firstRevisionCreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointSummaryFormOutput]
- **Required**: Yes

### listing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetListingDetails'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### predictionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.PredictionConfiguration'>
- **Required**: Yes

### readOnlyFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetRevisionInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormInput]]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### predictionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PredictionConfiguration]

### typeRevision
- **Type**: typing.Optional[str]


# CreateAssetRevisionOutput

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

### externalIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### firstRevisionCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### firstRevisionCreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointSummaryFormOutput]
- **Required**: Yes

### listing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetListingDetails'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### predictionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.PredictionConfiguration'>
- **Required**: Yes

### readOnlyFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetTypeInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### formsInput
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone.datazone_classes.FormEntryInput]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateAssetTypeOutput

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone.datazone_classes.FormEntryOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetTypePolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateConnectionInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AwsLocation]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### props
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionPropertiesInput]


# CreateConnectionOutput

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### physicalEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.PhysicalEndpoint]
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### props
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionPropertiesOutput'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataProductInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormInput]]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### items
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductItem, aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductItemOutput]]]


# CreateDataProductOutput

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

### firstRevisionCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### firstRevisionCreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductItemOutput]
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

### status
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataProductRevisionInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormInput]]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### items
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductItem, aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductItemOutput]]]


# CreateDataProductRevisionOutput

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

### firstRevisionCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### firstRevisionCreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductItemOutput]
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

### status
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### assetFormsInput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormInput]]

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceConfigurationInput]

### connectionIdentifier
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### enableSetting
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### environmentIdentifier
- **Type**: typing.Optional[str]

### publishOnImport
- **Type**: typing.Optional[bool]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RecommendationConfiguration]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ScheduleConfiguration]


# CreateDataSourceOutput

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceConfigurationOutput'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### enableSetting
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastRunAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastRunErrorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### lastRunStatus
- **Type**: typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### publishOnImport
- **Type**: <class 'bool'>
- **Required**: Yes

### recommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RecommendationConfiguration'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ScheduleConfiguration'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SingleSignOn]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDomainOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### domainVersion
- **Type**: typing.Literal['V1', 'V2']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### portalUrl
- **Type**: <class 'str'>
- **Required**: Yes

### rootDomainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceRole
- **Type**: <class 'str'>
- **Required**: Yes

### singleSignOn
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SingleSignOn'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainUnitInput

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


# CreateDomainUnitOutput

### ancestorDomainUnitIds
- **Type**: typing.List[str]
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

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owners
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitOwnerProperties]
- **Required**: Yes

### parentDomainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainUnitPolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateEnvironmentActionInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ActionParameters'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateEnvironmentActionOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ActionParameters'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentInput

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
- **Type**: typing.Optional[typing.List[str]]

### userParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentParameter]]


# CreateEnvironmentOutput

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountRegion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DeploymentProperties'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConfigurableEnvironmentAction]
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Deployment'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.Resource]
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningProperties'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.CustomParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentProfileInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentParameter]]


# CreateEnvironmentProfileOutput

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountRegion
- **Type**: <class 'str'>
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

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.CustomParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentProfilePolicyGrantDetail

### domainUnitId
- **Type**: typing.Optional[str]


# CreateFormTypeInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### model
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Model'>
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


# CreateFormTypeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFormTypePolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateGlossaryInput

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


# CreateGlossaryOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGlossaryPolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateGlossaryTermInput

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelations, aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelationsOutput, NoneType]


# CreateGlossaryTermOutput

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### longDescription
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### shortDescription
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### termRelations
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelationsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateGroupProfileOutput

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### groupName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'NOT_ASSIGNED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateListingChangeSetInput

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


# CreateListingChangeSetOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectFromProjectProfilePolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]

### projectProfiles
- **Type**: typing.Optional[typing.List[str]]


# CreateProjectFromProjectProfilePolicyGrantDetailOutput

### includeChildDomainUnits
- **Type**: typing.Optional[bool]

### projectProfiles
- **Type**: typing.Optional[typing.List[str]]


# CreateProjectInput

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
- **Type**: typing.Optional[typing.List[str]]

### projectProfileId
- **Type**: typing.Optional[str]

### userParameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationUserParameter, aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationUserParameterOutput]]]


# CreateProjectMembershipInput

### designation
- **Type**: typing.Literal['PROJECT_CATALOG_CONSUMER', 'PROJECT_CATALOG_STEWARD', 'PROJECT_CATALOG_VIEWER', 'PROJECT_CONTRIBUTOR', 'PROJECT_OWNER']
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Member'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CreateProjectOutput

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

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentDeploymentDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentDeploymentDetailsOutput'>
- **Required**: Yes

### failureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectDeletionError]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### projectStatus
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationUserParameterOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectPolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# CreateProjectProfileInput

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationOutput]]]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateProjectProfileOutput

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

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationOutput]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleInput

### action
- **Type**: typing.Literal['CREATE_SUBSCRIPTION_REQUEST']
- **Required**: Yes

### detail
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleDetail, aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleDetailOutput]
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScope, aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScopeOutput]
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleTarget'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateRuleOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleDetailOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScopeOutput'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleTarget'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriptionGrantInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.GrantedEntityInput'>
- **Required**: Yes

### assetTargetNames
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetTargetNameMap]]

### clientToken
- **Type**: typing.Optional[str]

### subscriptionTargetIdentifier
- **Type**: typing.Optional[str]


# CreateSubscriptionGrantOutput

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedAsset]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.GrantedEntity'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'GRANT_AND_REVOKE_FAILED', 'GRANT_FAILED', 'INACCESSIBLE', 'IN_PROGRESS', 'PENDING', 'REVOKE_FAILED']
- **Required**: Yes

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriptionRequestInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### subscribedListings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListingInput]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipalInput]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### metadataForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormInput]]


# CreateSubscriptionRequestOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### existingSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadataForms
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### reviewerId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### subscribedListings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriptionTargetInput

### applicableAssetTypes
- **Type**: typing.List[str]
- **Required**: Yes

### authorizedPrincipals
- **Type**: typing.List[str]
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionTargetForm]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### provider
- **Type**: typing.Optional[str]


# CreateSubscriptionTargetOutput

### applicableAssetTypes
- **Type**: typing.List[str]
- **Required**: Yes

### authorizedPrincipals
- **Type**: typing.List[str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionTargetForm]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserProfileInput

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


# CreateUserProfileOutput

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.UserProfileDetails'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATED', 'ASSIGNED', 'DEACTIVATED', 'NOT_ASSIGNED']
- **Required**: Yes

### type
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# CustomParameter

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


# DataProductItem

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


# DataProductItemOutput

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


# DataProductListing

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### dataProductId
- **Type**: typing.Optional[str]

### dataProductRevision
- **Type**: typing.Optional[str]

### forms
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ListingSummary]]

### owningProjectId
- **Type**: typing.Optional[str]


# DataProductListingItem

### additionalAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductListingItemAdditionalAttributes]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ListingSummaryItem]]

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


# DataProductListingItemAdditionalAttributes

### forms
- **Type**: typing.Optional[str]


# DataProductResultItem

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### firstRevisionCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### firstRevisionCreatedBy
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]


# DataProductRevision

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### domainId
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]


# DataSourceConfigurationInput

### glueRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueRunConfigurationInput]

### redshiftRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftRunConfigurationInput]

### sageMakerRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SageMakerRunConfigurationInput]


# DataSourceConfigurationOutput

### glueRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueRunConfigurationOutput]

### redshiftRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftRunConfigurationOutput]

### sageMakerRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SageMakerRunConfigurationOutput]


# DataSourceErrorMessage

### errorType
- **Type**: typing.Literal['ACCESS_DENIED_EXCEPTION', 'CONFLICT_EXCEPTION', 'INTERNAL_SERVER_EXCEPTION', 'RESOURCE_NOT_FOUND_EXCEPTION', 'SERVICE_QUOTA_EXCEEDED_EXCEPTION', 'THROTTLING_EXCEPTION', 'VALIDATION_EXCEPTION']
- **Required**: Yes

### errorDetail
- **Type**: typing.Optional[str]


# DataSourceRunActivity

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage]

### lineageSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageInfo]

### technicalDescription
- **Type**: typing.Optional[str]


# DataSourceRunLineageSummary

### importStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIALLY_SUCCEEDED', 'SUCCESS']]


# DataSourceRunSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['PRIORITIZED', 'SCHEDULED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage]

### lineageSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceRunLineageSummary]

### runStatisticsForAssets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RunStatisticsForAssets]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### stoppedAt
- **Type**: typing.Optional[datetime.datetime]


# DataSourceSummary

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### connectionId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### enableSetting
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### environmentId
- **Type**: typing.Optional[str]

### lastRunAssetCount
- **Type**: typing.Optional[int]

### lastRunAt
- **Type**: typing.Optional[datetime.datetime]

### lastRunErrorMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage]

### lastRunStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ScheduleConfiguration]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteAssetFilterInput

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssetInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssetTypeInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataProductInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceInput

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


# DeleteDataSourceOutput

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceConfigurationOutput'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### enableSetting
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastRunAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastRunErrorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### lastRunStatus
- **Type**: typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### publishOnImport
- **Type**: <class 'bool'>
- **Required**: Yes

### retainPermissionsOnRevokeFailure
- **Type**: <class 'bool'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ScheduleConfiguration'>
- **Required**: Yes

### selfGrantStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SelfGrantStatusOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### skipDeletionCheck
- **Type**: typing.Optional[bool]


# DeleteDomainOutput

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainUnitInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentActionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentBlueprintConfigurationInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFormTypeInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### formTypeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlossaryInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlossaryTermInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListingInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipDeletionCheck
- **Type**: typing.Optional[bool]


# DeleteProjectMembershipInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Member'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionGrantInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionGrantOutput

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedAsset]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.GrantedEntity'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'GRANT_AND_REVOKE_FAILED', 'GRANT_FAILED', 'INACCESSIBLE', 'IN_PROGRESS', 'PENDING', 'REVOKE_FAILED']
- **Required**: Yes

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSubscriptionRequestInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionTargetInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTimeSeriesDataPointsInput

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


# Deployment

### deploymentId
- **Type**: typing.Optional[str]

### deploymentStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING_DEPLOYMENT', 'SUCCESSFUL']]

### deploymentType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]

### failureReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentError]

### isDeploymentComplete
- **Type**: typing.Optional[bool]

### messages
- **Type**: typing.Optional[typing.List[str]]


# DeploymentProperties

### endTimeoutMinutes
- **Type**: typing.Optional[int]

### startTimeoutMinutes
- **Type**: typing.Optional[int]


# DetailedGlossaryTerm

### name
- **Type**: typing.Optional[str]

### shortDescription
- **Type**: typing.Optional[str]


# DisassociateEnvironmentRoleInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DomainSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### managedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### domainVersion
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### portalUrl
- **Type**: typing.Optional[str]


# DomainUnitFilterForProject

### domainUnit
- **Type**: <class 'str'>
- **Required**: Yes

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# DomainUnitGrantFilter

### allDomainUnitsGrantFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# DomainUnitGrantFilterOutput

### allDomainUnitsGrantFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# DomainUnitGroupProperties

### groupId
- **Type**: typing.Optional[str]


# DomainUnitOwnerProperties

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitGroupProperties]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitUserProperties]


# DomainUnitPolicyGrantPrincipal

### domainUnitDesignation
- **Type**: typing.Literal['OWNER']
- **Required**: Yes

### domainUnitGrantFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitGrantFilter]

### domainUnitIdentifier
- **Type**: typing.Optional[str]


# DomainUnitPolicyGrantPrincipalOutput

### domainUnitDesignation
- **Type**: typing.Literal['OWNER']
- **Required**: Yes

### domainUnitGrantFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitGrantFilterOutput]

### domainUnitIdentifier
- **Type**: typing.Optional[str]


# DomainUnitSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DomainUnitTarget

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# DomainUnitUserProperties

### userId
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# EnvironmentActionSummary

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ActionParameters'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# EnvironmentBlueprintConfigurationItem

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningConfigurationOutput]]

### provisioningRoleArn
- **Type**: typing.Optional[str]

### regionalParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EnvironmentBlueprintSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningProperties'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EnvironmentConfiguration

### awsAccount
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AwsAccount'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Region'>
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configurationParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationParametersDetails, aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationParametersDetailsOutput, NoneType]

### deploymentMode
- **Type**: typing.Optional[typing.Literal['ON_CREATE', 'ON_DEMAND']]

### deploymentOrder
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# EnvironmentConfigurationOutput

### awsAccount
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AwsAccount'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Region'>
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configurationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationParametersDetailsOutput]

### deploymentMode
- **Type**: typing.Optional[typing.Literal['ON_CREATE', 'ON_DEMAND']]

### deploymentOrder
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# EnvironmentConfigurationParameter

### isEditable
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EnvironmentConfigurationParametersDetails

### parameterOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationParameter]]

### resolvedParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationParameter]]

### ssmPath
- **Type**: typing.Optional[str]


# EnvironmentConfigurationParametersDetailsOutput

### parameterOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationParameter]]

### resolvedParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationParameter]]

### ssmPath
- **Type**: typing.Optional[str]


# EnvironmentConfigurationUserParameter

### environmentConfigurationName
- **Type**: typing.Optional[str]

### environmentParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentParameter]]


# EnvironmentConfigurationUserParameterOutput

### environmentConfigurationName
- **Type**: typing.Optional[str]

### environmentParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentParameter]]


# EnvironmentDeploymentDetails

### environmentFailureReasons
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentError]]]

### overallDeploymentStatus
- **Type**: typing.Optional[typing.Literal['FAILED_DEPLOYMENT', 'FAILED_VALIDATION', 'IN_PROGRESS', 'PENDING_DEPLOYMENT', 'SUCCESSFUL']]


# EnvironmentDeploymentDetailsOutput

### environmentFailureReasons
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentError]]]

### overallDeploymentStatus
- **Type**: typing.Optional[typing.Literal['FAILED_DEPLOYMENT', 'FAILED_VALIDATION', 'IN_PROGRESS', 'PENDING_DEPLOYMENT', 'SUCCESSFUL']]


# EnvironmentError

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]


# EnvironmentParameter

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EnvironmentProfileSummary

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### projectId
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EnvironmentSummary

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsAccountRegion
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### environmentProfileId
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EqualToExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# EventSummary

### openLineageRunEventSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OpenLineageRunEventSummary]


# FailureCause

### message
- **Type**: typing.Optional[str]


# Filter

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# FilterClause

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.Filter]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FilterClausePaginator

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.Filter]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FilterExpression

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EXCLUDE', 'INCLUDE']
- **Required**: Yes


# FormEntryInput

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]


# FormEntryOutput

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]


# FormInput

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### typeIdentifier
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# FormOutput

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### typeName
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# FormTypeData

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.Import]]

### model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.Model]

### originDomainId
- **Type**: typing.Optional[str]

### originProjectId
- **Type**: typing.Optional[str]

### owningProjectId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GetAssetFilterInput

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssetFilterOutput

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterConfigurationOutput'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### effectiveColumnNames
- **Type**: typing.List[str]
- **Required**: Yes

### effectiveRowFilter
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['INVALID', 'VALID']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssetInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetAssetOutput

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

### externalIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### firstRevisionCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### firstRevisionCreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointSummaryFormOutput]
- **Required**: Yes

### listing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetListingDetails'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### readOnlyFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssetTypeInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetAssetTypeOutput

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone.datazone_classes.FormEntryOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### withSecret
- **Type**: typing.Optional[bool]


# GetConnectionOutput

### connectionCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionCredentials'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentUserRole
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### physicalEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.PhysicalEndpoint]
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### props
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionPropertiesOutput'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataProductInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetDataProductOutput

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

### firstRevisionCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### firstRevisionCreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductItemOutput]
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

### status
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceOutput

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceConfigurationOutput'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### enableSetting
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastRunAssetCount
- **Type**: <class 'int'>
- **Required**: Yes

### lastRunAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastRunErrorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### lastRunStatus
- **Type**: typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### publishOnImport
- **Type**: <class 'bool'>
- **Required**: Yes

### recommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RecommendationConfiguration'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ScheduleConfiguration'>
- **Required**: Yes

### selfGrantStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SelfGrantStatusOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceRunInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceRunOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSourceConfigurationSnapshot
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lineageSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceRunLineageSummary'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### runStatisticsForAssets
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RunStatisticsForAssets'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### stoppedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: typing.Literal['PRIORITIZED', 'SCHEDULED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### domainVersion
- **Type**: typing.Literal['V1', 'V2']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### portalUrl
- **Type**: <class 'str'>
- **Required**: Yes

### rootDomainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceRole
- **Type**: <class 'str'>
- **Required**: Yes

### singleSignOn
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SingleSignOn'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainUnitInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainUnitOutput

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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owners
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitOwnerProperties]
- **Required**: Yes

### parentDomainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentActionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentActionOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ActionParameters'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentBlueprintConfigurationInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentBlueprintConfigurationOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningConfigurationOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentBlueprintInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentBlueprintOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DeploymentProperties'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningProperties'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.CustomParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentCredentialsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentCredentialsOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentOutput

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountRegion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DeploymentProperties'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConfigurableEnvironmentAction]
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Deployment'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.Resource]
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningProperties'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.CustomParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentProfileOutput

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountRegion
- **Type**: <class 'str'>
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

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.CustomParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetFormTypeInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### formTypeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetFormTypeOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.Import]
- **Required**: Yes

### model
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Model'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetGlossaryInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlossaryOutput

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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetGlossaryTermInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlossaryTermOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### longDescription
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### shortDescription
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### termRelations
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelationsOutput'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupProfileOutput

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### groupName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'NOT_ASSIGNED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetIamPortalLoginUrlInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIamPortalLoginUrlOutput

### authCodeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### userProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRunInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobRunOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.JobRunDetails'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.JobRunError'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobType
- **Type**: typing.Literal['LINEAGE']
- **Required**: Yes

### runMode
- **Type**: typing.Literal['ON_DEMAND', 'SCHEDULED']
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABORTED', 'CANCELED', 'FAILED', 'IN_PROGRESS', 'PARTIALLY_SUCCEEDED', 'SCHEDULED', 'SUCCESS', 'TIMED_OUT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetLineageEventInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLineageEventOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### eventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### processingStatus
- **Type**: typing.Literal['FAILED', 'PROCESSING', 'REQUESTED', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetLineageNodeInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### eventTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetLineageNodeOutput

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

### downstreamNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageNodeReference]
- **Required**: Yes

### eventTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### upstreamNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageNodeReference]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetListingInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### listingRevision
- **Type**: typing.Optional[str]


# GetListingOutput

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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### item
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ListingItem'>
- **Required**: Yes

### listingRevision
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'INACTIVE']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetadataGenerationRunInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetadataGenerationRunOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCEEDED']
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataGenerationRunTarget'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BUSINESS_DESCRIPTIONS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetProjectInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectOutput

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

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentDeploymentDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentDeploymentDetailsOutput'>
- **Required**: Yes

### failureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectDeletionError]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### projectStatus
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationUserParameterOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetProjectProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectProfileOutput

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

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationOutput]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuleInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetRuleOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleDetailOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScopeOutput'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleTarget'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['DOMAIN_UNIT']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionGrantInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionGrantOutput

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedAsset]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.GrantedEntity'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'GRANT_AND_REVOKE_FAILED', 'GRANT_FAILED', 'INACCESSIBLE', 'IN_PROGRESS', 'PENDING', 'REVOKE_FAILED']
- **Required**: Yes

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### retainPermissions
- **Type**: <class 'bool'>
- **Required**: Yes

### status
- **Type**: typing.Literal['APPROVED', 'CANCELLED', 'REVOKED']
- **Required**: Yes

### subscribedListing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal'>
- **Required**: Yes

### subscriptionRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionRequestDetailsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionRequestDetailsOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### existingSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadataForms
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### reviewerId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### subscribedListings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionTargetInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionTargetOutput

### applicableAssetTypes
- **Type**: typing.List[str]
- **Required**: Yes

### authorizedPrincipals
- **Type**: typing.List[str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionTargetForm]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetTimeSeriesDataPointInput

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


# GetTimeSeriesDataPointOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointFormOutput'>
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]


# GetUserProfileOutput

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.UserProfileDetails'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATED', 'ASSIGNED', 'DEACTIVATED', 'NOT_ASSIGNED']
- **Required**: Yes

### type
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# GlossaryItem

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# GlossaryTermItem

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### longDescription
- **Type**: typing.Optional[str]

### shortDescription
- **Type**: typing.Optional[str]

### termRelations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelationsOutput]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# GlueConnection

### athenaProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AuthenticationConfiguration]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PhysicalConnectionRequirementsOutput]

### pythonProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### sparkProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'READY', 'UPDATE_FAILED', 'UPDATING']]

### statusReason
- **Type**: typing.Optional[str]


# GlueConnectionInput

### athenaProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AuthenticationConfigurationInput]

### connectionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### connectionType
- **Type**: typing.Optional[typing.Literal['BIGQUERY', 'DOCUMENTDB', 'DYNAMODB', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SQLSERVER', 'TERADATA', 'VERTICA']]

### description
- **Type**: typing.Optional[str]

### matchCriteria
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### physicalConnectionRequirements
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.PhysicalConnectionRequirements, aws_resource_validator.pydantic_models.datazone.datazone_classes.PhysicalConnectionRequirementsOutput, NoneType]

### pythonProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### sparkProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### validateCredentials
- **Type**: typing.Optional[bool]

### validateForComputeEnvironments
- **Type**: typing.Optional[typing.List[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]]


# GlueConnectionPatch

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AuthenticationConfigurationPatch]

### connectionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### description
- **Type**: typing.Optional[str]


# GlueOAuth2Credentials

### accessToken
- **Type**: typing.Optional[str]

### jwtToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### userManagedClientApplicationClientSecret
- **Type**: typing.Optional[str]


# GluePropertiesInput

### glueConnectionInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueConnectionInput]


# GluePropertiesOutput

### errorMessage
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'READY', 'UPDATE_FAILED', 'UPDATING']]


# GluePropertiesPatch

### glueConnectionInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueConnectionPatch]


# GlueRunConfigurationInput

### relationalFilterConfigurations
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.RelationalFilterConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.RelationalFilterConfigurationOutput]]
- **Required**: Yes

### autoImportDataQualityResult
- **Type**: typing.Optional[bool]

### catalogName
- **Type**: typing.Optional[str]

### dataAccessRole
- **Type**: typing.Optional[str]


# GlueRunConfigurationOutput

### relationalFilterConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.RelationalFilterConfigurationOutput]
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


# GlueSelfGrantStatusOutput

### selfGrantStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SelfGrantStatusDetail]
- **Required**: Yes


# GrantedEntity

### listing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ListingRevision]


# GrantedEntityInput

### listing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ListingRevisionInput]


# GreaterThanExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# GreaterThanOrEqualToExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# GroupDetails

### groupId
- **Type**: <class 'str'>
- **Required**: Yes


# GroupPolicyGrantPrincipal

### groupIdentifier
- **Type**: typing.Optional[str]


# GroupProfileSummary

### domainId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'NOT_ASSIGNED']]


# HyperPodPropertiesInput

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# HyperPodPropertiesOutput

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### clusterArn
- **Type**: typing.Optional[str]

### orchestrator
- **Type**: typing.Optional[typing.Literal['EKS', 'SLURM']]


# IamPropertiesInput

### glueLineageSyncEnabled
- **Type**: typing.Optional[bool]


# IamPropertiesOutput

### environmentId
- **Type**: typing.Optional[str]

### glueLineageSyncEnabled
- **Type**: typing.Optional[bool]


# IamPropertiesPatch

### glueLineageSyncEnabled
- **Type**: typing.Optional[bool]


# IamUserProfileDetails

### arn
- **Type**: typing.Optional[str]


# Import

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes


# InExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# InExpressionOutput

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# IsNotNullExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes


# IsNullExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes


# JobRunDetails

### lineageRunDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageRunDetails]


# JobRunError

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobRunSummary

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### domainId
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.JobRunError]

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


# LakeFormationConfiguration

### locationRegistrationExcludeS3Locations
- **Type**: typing.Optional[typing.List[str]]

### locationRegistrationRole
- **Type**: typing.Optional[str]


# LakeFormationConfigurationOutput

### locationRegistrationExcludeS3Locations
- **Type**: typing.Optional[typing.List[str]]

### locationRegistrationRole
- **Type**: typing.Optional[str]


# LessThanExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# LessThanOrEqualToExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# LikeExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# LineageEventSummary

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### domainId
- **Type**: typing.Optional[str]

### eventSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.EventSummary]

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### processingStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'REQUESTED', 'SUCCESS']]


# LineageInfo

### errorMessage
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]

### eventStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'REQUESTED', 'SUCCESS']]


# LineageNodeReference

### eventTimestamp
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]


# LineageNodeSummary

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### eventTimestamp
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### sourceIdentifier
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# LineageNodeTypeItem

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### formsOutput
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.datazone.datazone_classes.FormEntryOutput]
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


# LineageRunDetails

### sqlQueryRunDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageSqlQueryRunDetails]


# LineageSqlQueryRunDetails

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


# LineageSyncSchedule

### schedule
- **Type**: typing.Optional[str]


# ListAssetFiltersInput

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


# ListAssetFiltersInputPaginate

### assetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['INVALID', 'VALID']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListAssetFiltersOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssetRevisionsInput

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


# ListAssetRevisionsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListAssetRevisionsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetRevision]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConnectionsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: typing.Optional[str]

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

### type
- **Type**: typing.Optional[typing.Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA']]


# ListConnectionsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### type
- **Type**: typing.Optional[typing.Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListConnectionsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataProductRevisionsInput

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


# ListDataProductRevisionsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListDataProductRevisionsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductRevision]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourceRunActivitiesInput

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


# ListDataSourceRunActivitiesInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PUBLISHING_FAILED', 'SKIPPED_ALREADY_IMPORTED', 'SKIPPED_ARCHIVED', 'SKIPPED_NO_ACCESS', 'SUCCEEDED_CREATED', 'SUCCEEDED_UPDATED', 'UNCHANGED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListDataSourceRunActivitiesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceRunActivity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourceRunsInput

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


# ListDataSourceRunsInputPaginate

### dataSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListDataSourceRunsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceRunSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### connectionIdentifier
- **Type**: typing.Optional[str]

### environmentIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']]

### type
- **Type**: typing.Optional[str]


# ListDataSourcesInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### connectionIdentifier
- **Type**: typing.Optional[str]

### environmentIdentifier
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']]

### type
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListDataSourcesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainUnitsForParentInput

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


# ListDomainUnitsForParentInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parentDomainUnitIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListDomainUnitsForParentOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']]


# ListDomainsInputPaginate

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListDomainsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEntityOwnersInput

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


# ListEntityOwnersInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListEntityOwnersOutput

### owners
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.OwnerPropertiesOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentActionsInput

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


# ListEnvironmentActionsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListEnvironmentActionsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentActionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentBlueprintConfigurationsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentBlueprintConfigurationsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListEnvironmentBlueprintConfigurationsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentBlueprintConfigurationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentBlueprintsInput

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


# ListEnvironmentBlueprintsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### managed
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListEnvironmentBlueprintsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentBlueprintSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentProfilesInput

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


# ListEnvironmentProfilesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListEnvironmentProfilesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsInput

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


# ListEnvironmentsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListEnvironmentsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsInput

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


# ListJobRunsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListJobRunsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.JobRunSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLineageEventsInput

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### timestampBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListLineageEventsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### processingStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'REQUESTED', 'SUCCESS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### timestampAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### timestampBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListLineageEventsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageEventSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLineageNodeHistoryInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Optional[typing.Literal['DOWNSTREAM', 'UPSTREAM']]

### eventTimestampGTE
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### eventTimestampLTE
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListLineageNodeHistoryInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Optional[typing.Literal['DOWNSTREAM', 'UPSTREAM']]

### eventTimestampGTE
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### eventTimestampLTE
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListLineageNodeHistoryOutput

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageNodeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetadataGenerationRunsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCEEDED']]

### type
- **Type**: typing.Optional[typing.Literal['BUSINESS_DESCRIPTIONS']]


# ListMetadataGenerationRunsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCEEDED']]

### type
- **Type**: typing.Optional[typing.Literal['BUSINESS_DESCRIPTIONS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListMetadataGenerationRunsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataGenerationRunItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EVENT', 'TASK']
- **Required**: Yes

### afterTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### beforeTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### subjects
- **Type**: typing.Optional[typing.List[str]]

### taskStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# ListNotificationsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EVENT', 'TASK']
- **Required**: Yes

### afterTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### beforeTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### subjects
- **Type**: typing.Optional[typing.List[str]]

### taskStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListNotificationsOutput

### notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.NotificationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyGrantsInput

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


# ListPolicyGrantsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListPolicyGrantsOutput

### grantList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectMembershipsInput

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


# ListProjectMembershipsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListProjectMembershipsOutput

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectProfilesInput

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


# ListProjectProfilesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListProjectProfilesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsInput

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


# ListProjectsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListProjectsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRulesInput

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
- **Type**: typing.Optional[typing.List[str]]

### dataProduct
- **Type**: typing.Optional[bool]

### includeCascaded
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### projectIds
- **Type**: typing.Optional[typing.List[str]]

### ruleType
- **Type**: typing.Optional[typing.Literal['METADATA_FORM_ENFORCEMENT']]


# ListRulesInputPaginate

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
- **Type**: typing.Optional[typing.List[str]]

### dataProduct
- **Type**: typing.Optional[bool]

### includeCascaded
- **Type**: typing.Optional[bool]

### projectIds
- **Type**: typing.Optional[typing.List[str]]

### ruleType
- **Type**: typing.Optional[typing.Literal['METADATA_FORM_ENFORCEMENT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListRulesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionGrantsInput

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


# ListSubscriptionGrantsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListSubscriptionGrantsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionGrantSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionRequestsInput

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


# ListSubscriptionRequestsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListSubscriptionRequestsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionRequestSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionTargetsInput

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


# ListSubscriptionTargetsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListSubscriptionTargetsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionTargetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsInput

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


# ListSubscriptionsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListSubscriptionsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# ListTimeSeriesDataPointsInput

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListTimeSeriesDataPointsInputPaginate

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### startedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# ListTimeSeriesDataPointsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointSummaryFormOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListingItem

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetListing]

### dataProductListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductListing]


# ListingRevision

### id
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes


# ListingRevisionInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes


# ListingSummary

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]

### listingId
- **Type**: typing.Optional[str]

### listingRevision
- **Type**: typing.Optional[str]


# ListingSummaryItem

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]

### listingId
- **Type**: typing.Optional[str]

### listingRevision
- **Type**: typing.Optional[str]


# Member

### groupIdentifier
- **Type**: typing.Optional[str]

### userIdentifier
- **Type**: typing.Optional[str]


# MemberDetails

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GroupDetails]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.UserDetails]


# MetadataFormEnforcementDetail

### requiredMetadataForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataFormReference]]


# MetadataFormEnforcementDetailOutput

### requiredMetadataForms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataFormReference]]


# MetadataFormReference

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes


# MetadataFormSummary

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### typeRevision
- **Type**: <class 'str'>
- **Required**: Yes

### formName
- **Type**: typing.Optional[str]


# MetadataGenerationRunItem

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCEEDED']]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataGenerationRunTarget]

### type
- **Type**: typing.Optional[typing.Literal['BUSINESS_DESCRIPTIONS']]


# MetadataGenerationRunTarget

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ASSET']
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# Model

### smithy
- **Type**: typing.Optional[str]


# NameIdentifier

### name
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# NotEqualToExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# NotInExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# NotInExpressionOutput

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# NotLikeExpression

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# NotificationOutput

### actionLink
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### topic
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Topic'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EVENT', 'TASK']
- **Required**: Yes

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# NotificationResource

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['PROJECT']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# OAuth2ClientApplication

### aWSManagedClientApplicationReference
- **Type**: typing.Optional[str]

### userManagedClientApplicationClientId
- **Type**: typing.Optional[str]


# OAuth2Properties

### authorizationCodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AuthorizationCodeProperties]

### oAuth2ClientApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OAuth2ClientApplication]

### oAuth2Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueOAuth2Credentials]

### oAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### tokenUrl
- **Type**: typing.Optional[str]

### tokenUrlParametersMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# OAuth2PropertiesOutput

### authorizationCodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AuthorizationCodeProperties]

### oAuth2ClientApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OAuth2ClientApplication]

### oAuth2Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueOAuth2Credentials]

### oAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### tokenUrl
- **Type**: typing.Optional[str]

### tokenUrlParametersMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# OpenLineageRunEventSummary

### eventType
- **Type**: typing.Optional[typing.Literal['ABORT', 'COMPLETE', 'FAIL', 'OTHER', 'RUNNING', 'START']]

### inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.NameIdentifier]]

### job
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.NameIdentifier]

### outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.NameIdentifier]]

### runId
- **Type**: typing.Optional[str]


# OverrideDomainUnitOwnersPolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# OverrideProjectOwnersPolicyGrantDetail

### includeChildDomainUnits
- **Type**: typing.Optional[bool]


# OwnerGroupProperties

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# OwnerGroupPropertiesOutput

### groupId
- **Type**: typing.Optional[str]


# OwnerProperties

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OwnerGroupProperties]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OwnerUserProperties]


# OwnerPropertiesOutput

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OwnerGroupPropertiesOutput]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OwnerUserPropertiesOutput]


# OwnerUserProperties

### userIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# OwnerUserPropertiesOutput

### userId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhysicalConnectionRequirements

### availabilityZone
- **Type**: typing.Optional[str]

### securityGroupIdList
- **Type**: typing.Optional[typing.List[str]]

### subnetId
- **Type**: typing.Optional[str]

### subnetIdList
- **Type**: typing.Optional[typing.List[str]]


# PhysicalConnectionRequirementsOutput

### availabilityZone
- **Type**: typing.Optional[str]

### securityGroupIdList
- **Type**: typing.Optional[typing.List[str]]

### subnetId
- **Type**: typing.Optional[str]

### subnetIdList
- **Type**: typing.Optional[typing.List[str]]


# PhysicalEndpoint

### awsLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AwsLocation]

### glueConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueConnection]

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


# PolicyGrantDetail

### addToProjectMemberPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AddToProjectMemberPoolPolicyGrantDetail]

### createAssetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateAssetTypePolicyGrantDetail]

### createDomainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateDomainUnitPolicyGrantDetail]

### createEnvironment
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createEnvironmentFromBlueprint
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createEnvironmentProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateEnvironmentProfilePolicyGrantDetail]

### createFormType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateFormTypePolicyGrantDetail]

### createGlossary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateGlossaryPolicyGrantDetail]

### createProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateProjectPolicyGrantDetail]

### createProjectFromProjectProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateProjectFromProjectProfilePolicyGrantDetail]

### delegateCreateEnvironmentProfile
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### overrideDomainUnitOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OverrideDomainUnitOwnersPolicyGrantDetail]

### overrideProjectOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OverrideProjectOwnersPolicyGrantDetail]


# PolicyGrantDetailOutput

### addToProjectMemberPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AddToProjectMemberPoolPolicyGrantDetail]

### createAssetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateAssetTypePolicyGrantDetail]

### createDomainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateDomainUnitPolicyGrantDetail]

### createEnvironment
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createEnvironmentFromBlueprint
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createEnvironmentProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateEnvironmentProfilePolicyGrantDetail]

### createFormType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateFormTypePolicyGrantDetail]

### createGlossary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateGlossaryPolicyGrantDetail]

### createProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateProjectPolicyGrantDetail]

### createProjectFromProjectProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CreateProjectFromProjectProfilePolicyGrantDetailOutput]

### delegateCreateEnvironmentProfile
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### overrideDomainUnitOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OverrideDomainUnitOwnersPolicyGrantDetail]

### overrideProjectOwners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.OverrideProjectOwnersPolicyGrantDetail]


# PolicyGrantMember

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### detail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantDetailOutput]

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantPrincipalOutput]


# PolicyGrantPrincipal

### domainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitPolicyGrantPrincipal]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GroupPolicyGrantPrincipal]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectPolicyGrantPrincipal]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.UserPolicyGrantPrincipal]


# PolicyGrantPrincipalOutput

### domainUnit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitPolicyGrantPrincipalOutput]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GroupPolicyGrantPrincipal]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectPolicyGrantPrincipal]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.UserPolicyGrantPrincipalOutput]


# PostLineageEventInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PostLineageEventOutput

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# PostTimeSeriesDataPointsInput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointFormInput]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PostTimeSeriesDataPointsOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.TimeSeriesDataPointFormOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# PredictionConfiguration

### businessNameGeneration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.BusinessNameGenerationConfiguration]


# ProjectDeletionError

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ProjectGrantFilter

### domainUnitFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitFilterForProject]


# ProjectMember

### designation
- **Type**: typing.Literal['PROJECT_CATALOG_CONSUMER', 'PROJECT_CATALOG_STEWARD', 'PROJECT_CATALOG_VIEWER', 'PROJECT_CONTRIBUTOR', 'PROJECT_OWNER']
- **Required**: Yes

### memberDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.MemberDetails'>
- **Required**: Yes


# ProjectPolicyGrantPrincipal

### projectDesignation
- **Type**: typing.Literal['CONTRIBUTOR', 'OWNER', 'PROJECT_CATALOG_STEWARD']
- **Required**: Yes

### projectGrantFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectGrantFilter]

### projectIdentifier
- **Type**: typing.Optional[str]


# ProjectProfileSummary

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### domainUnitId
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ProjectSummary

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### domainUnitId
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectDeletionError]]

### projectStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ProjectsForRule

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificProjects
- **Type**: typing.Optional[typing.List[str]]


# ProjectsForRuleOutput

### selectionMode
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### specificProjects
- **Type**: typing.Optional[typing.List[str]]


# ProvisioningConfiguration

### lakeFormationConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.LakeFormationConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.LakeFormationConfigurationOutput, NoneType]


# ProvisioningConfigurationOutput

### lakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LakeFormationConfigurationOutput]


# ProvisioningProperties

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.CloudFormationProperties]


# PutEnvironmentBlueprintConfigurationInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### enabledRegions
- **Type**: typing.List[str]
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRolePermissionBoundary
- **Type**: typing.Optional[str]

### manageAccessRoleArn
- **Type**: typing.Optional[str]

### provisioningConfigurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningConfigurationOutput]]]

### provisioningRoleArn
- **Type**: typing.Optional[str]

### regionalParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# PutEnvironmentBlueprintConfigurationOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningConfigurationOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# RecommendationConfiguration

### enableBusinessNameGeneration
- **Type**: typing.Optional[bool]


# RedshiftClusterStorage

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftCredentialConfiguration

### secretManagerArn
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftCredentials

### secretArn
- **Type**: typing.Optional[str]

### usernamePassword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.UsernamePassword]


# RedshiftLineageSyncConfigurationInput

### enabled
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageSyncSchedule]


# RedshiftLineageSyncConfigurationOutput

### enabled
- **Type**: typing.Optional[bool]

### lineageJobId
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageSyncSchedule]


# RedshiftPropertiesInput

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftCredentials]

### databaseName
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[str]

### lineageSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftLineageSyncConfigurationInput]

### port
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftStorageProperties]


# RedshiftPropertiesOutput

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftCredentials]

### databaseName
- **Type**: typing.Optional[str]

### isProvisionedSecret
- **Type**: typing.Optional[bool]

### jdbcIamUrl
- **Type**: typing.Optional[str]

### jdbcUrl
- **Type**: typing.Optional[str]

### lineageSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftLineageSyncConfigurationOutput]

### redshiftTempDir
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'READY', 'UPDATE_FAILED', 'UPDATING']]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftStorageProperties]


# RedshiftPropertiesPatch

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftCredentials]

### databaseName
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[str]

### lineageSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftLineageSyncConfigurationInput]

### port
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftStorageProperties]


# RedshiftRunConfigurationInput

### relationalFilterConfigurations
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.RelationalFilterConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.RelationalFilterConfigurationOutput]]
- **Required**: Yes

### dataAccessRole
- **Type**: typing.Optional[str]

### redshiftCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftCredentialConfiguration]

### redshiftStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftStorage]


# RedshiftRunConfigurationOutput

### redshiftStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftStorage'>
- **Required**: Yes

### relationalFilterConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.RelationalFilterConfigurationOutput]
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### dataAccessRole
- **Type**: typing.Optional[str]

### redshiftCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftCredentialConfiguration]

### region
- **Type**: typing.Optional[str]


# RedshiftSelfGrantStatusOutput

### selfGrantStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SelfGrantStatusDetail]
- **Required**: Yes


# RedshiftServerlessStorage

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftStorage

### redshiftClusterSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftClusterStorage]

### redshiftServerlessSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftServerlessStorage]


# RedshiftStorageProperties

### clusterName
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]


# Region

### regionName
- **Type**: typing.Optional[str]

### regionNamePath
- **Type**: typing.Optional[str]


# RejectChoice

### predictionTarget
- **Type**: <class 'str'>
- **Required**: Yes

### predictionChoices
- **Type**: typing.Optional[typing.List[int]]


# RejectPredictionsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### rejectChoices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.RejectChoice]]

### rejectRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RejectRule]

### revision
- **Type**: typing.Optional[str]


# RejectPredictionsOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# RejectRule

### rule
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]

### threshold
- **Type**: typing.Optional[float]


# RejectSubscriptionRequestInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: typing.Optional[str]


# RejectSubscriptionRequestOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### existingSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadataForms
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### reviewerId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### subscribedListings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# RelationalFilterConfiguration

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterExpression]]

### schemaName
- **Type**: typing.Optional[str]


# RelationalFilterConfigurationOutput

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterExpression]]

### schemaName
- **Type**: typing.Optional[str]


# RemoveEntityOwnerInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.OwnerProperties'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# RemovePolicyGrantInput

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantPrincipal, aws_resource_validator.pydantic_models.datazone.datazone_classes.PolicyGrantPrincipalOutput]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# Resource

### type
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### provider
- **Type**: typing.Optional[str]


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


# RevokeSubscriptionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### retainPermissions
- **Type**: typing.Optional[bool]


# RevokeSubscriptionOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### retainPermissions
- **Type**: <class 'bool'>
- **Required**: Yes

### status
- **Type**: typing.Literal['APPROVED', 'CANCELLED', 'REVOKED']
- **Required**: Yes

### subscribedListing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal'>
- **Required**: Yes

### subscriptionRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# RowFilter

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### expression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RowFilterExpression]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# RowFilterConfiguration

### rowFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RowFilter'>
- **Required**: Yes

### sensitive
- **Type**: typing.Optional[bool]


# RowFilterConfigurationOutput

### rowFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RowFilterOutput'>
- **Required**: Yes

### sensitive
- **Type**: typing.Optional[bool]


# RowFilterExpression

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.EqualToExpression]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GreaterThanExpression]

### greaterThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GreaterThanOrEqualToExpression]

### in_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.InExpression]

### isNotNull
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IsNotNullExpression]

### isNull
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IsNullExpression]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LessThanExpression]

### lessThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LessThanOrEqualToExpression]

### like
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LikeExpression]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.NotEqualToExpression]

### notIn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.NotInExpression]

### notLike
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.NotLikeExpression]


# RowFilterExpressionOutput

### equalTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.EqualToExpression]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GreaterThanExpression]

### greaterThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GreaterThanOrEqualToExpression]

### in_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.InExpressionOutput]

### isNotNull
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IsNotNullExpression]

### isNull
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IsNullExpression]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LessThanExpression]

### lessThanOrEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LessThanOrEqualToExpression]

### like
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LikeExpression]

### notEqualTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.NotEqualToExpression]

### notIn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.NotInExpressionOutput]

### notLike
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.NotLikeExpression]


# RowFilterOutput

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### expression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RowFilterExpressionOutput]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# RuleDetail

### metadataFormEnforcementDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataFormEnforcementDetail]


# RuleDetailOutput

### metadataFormEnforcementDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataFormEnforcementDetailOutput]


# RuleScope

### assetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetTypesForRule]

### dataProduct
- **Type**: typing.Optional[bool]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectsForRule]


# RuleScopeOutput

### assetType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetTypesForRuleOutput]

### dataProduct
- **Type**: typing.Optional[bool]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectsForRuleOutput]


# RuleSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScopeOutput]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleTarget]

### targetType
- **Type**: typing.Optional[typing.Literal['DOMAIN_UNIT']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# RuleTarget

### domainUnitTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitTarget]


# RunStatisticsForAssets

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


# SageMakerRunConfigurationInput

### trackingAssets
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes


# SageMakerRunConfigurationOutput

### trackingAssets
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# ScheduleConfiguration

### schedule
- **Type**: typing.Optional[str]

### timezone
- **Type**: typing.Optional[typing.Literal['AFRICA_JOHANNESBURG', 'AMERICA_MONTREAL', 'AMERICA_SAO_PAULO', 'ASIA_BAHRAIN', 'ASIA_BANGKOK', 'ASIA_CALCUTTA', 'ASIA_DUBAI', 'ASIA_HONG_KONG', 'ASIA_JAKARTA', 'ASIA_KUALA_LUMPUR', 'ASIA_SEOUL', 'ASIA_SHANGHAI', 'ASIA_SINGAPORE', 'ASIA_TAIPEI', 'ASIA_TOKYO', 'AUSTRALIA_MELBOURNE', 'AUSTRALIA_SYDNEY', 'CANADA_CENTRAL', 'CET', 'CST6CDT', 'ETC_GMT', 'ETC_GMT0', 'ETC_GMT_ADD_0', 'ETC_GMT_ADD_1', 'ETC_GMT_ADD_10', 'ETC_GMT_ADD_11', 'ETC_GMT_ADD_12', 'ETC_GMT_ADD_2', 'ETC_GMT_ADD_3', 'ETC_GMT_ADD_4', 'ETC_GMT_ADD_5', 'ETC_GMT_ADD_6', 'ETC_GMT_ADD_7', 'ETC_GMT_ADD_8', 'ETC_GMT_ADD_9', 'ETC_GMT_NEG_0', 'ETC_GMT_NEG_1', 'ETC_GMT_NEG_10', 'ETC_GMT_NEG_11', 'ETC_GMT_NEG_12', 'ETC_GMT_NEG_13', 'ETC_GMT_NEG_14', 'ETC_GMT_NEG_2', 'ETC_GMT_NEG_3', 'ETC_GMT_NEG_4', 'ETC_GMT_NEG_5', 'ETC_GMT_NEG_6', 'ETC_GMT_NEG_7', 'ETC_GMT_NEG_8', 'ETC_GMT_NEG_9', 'EUROPE_DUBLIN', 'EUROPE_LONDON', 'EUROPE_PARIS', 'EUROPE_STOCKHOLM', 'EUROPE_ZURICH', 'ISRAEL', 'MEXICO_GENERAL', 'MST7MDT', 'PACIFIC_AUCKLAND', 'US_CENTRAL', 'US_EASTERN', 'US_MOUNTAIN', 'US_PACIFIC', 'UTC']]


# SearchGroupProfilesInput

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


# SearchGroupProfilesInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupType
- **Type**: typing.Literal['DATAZONE_SSO_GROUP', 'SSO_GROUP']
- **Required**: Yes

### searchText
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# SearchGroupProfilesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.GroupProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchInItem

### attribute
- **Type**: <class 'str'>
- **Required**: Yes


# SearchInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET', 'DATA_PRODUCT', 'GLOSSARY', 'GLOSSARY_TERM']
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterClause]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### owningProjectIdentifier
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchInItem]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchSort]


# SearchInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET', 'DATA_PRODUCT', 'GLOSSARY', 'GLOSSARY_TERM']
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterClausePaginator]

### owningProjectIdentifier
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchInItem]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchSort]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# SearchInventoryResultItem

### assetItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetItem]

### dataProductItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductResultItem]

### glossaryItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlossaryItem]

### glossaryTermItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlossaryTermItem]


# SearchListingsInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterClause]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchInItem]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchSort]


# SearchListingsInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterClausePaginator]

### searchIn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchInItem]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchSort]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# SearchListingsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchResultItem]
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchInventoryResultItem]
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchResultItem

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetListingItem]

### dataProductListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataProductListingItem]


# SearchSort

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SearchTypesInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterClause]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### searchIn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchInItem]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchSort]


# SearchTypesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FilterClausePaginator]

### searchIn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchInItem]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchSort]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# SearchTypesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SearchTypesResultItem]
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchTypesResultItem

### assetTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetTypeItem]

### formTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormTypeData]

### lineageNodeTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.LineageNodeTypeItem]


# SearchUserProfilesInput

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


# SearchUserProfilesInputPaginate

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userType
- **Type**: typing.Literal['DATAZONE_IAM_USER', 'DATAZONE_SSO_USER', 'DATAZONE_USER', 'SSO_USER']
- **Required**: Yes

### searchText
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.PaginatorConfig]


# SearchUserProfilesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.UserProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SelfGrantStatusDetail

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


# SelfGrantStatusOutput

### glueSelfGrantStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.GlueSelfGrantStatusOutput]

### redshiftSelfGrantStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RedshiftSelfGrantStatusOutput]


# SingleSignOn

### type
- **Type**: typing.Optional[typing.Literal['DISABLED', 'IAM_IDC']]

### userAssignment
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]


# SparkEmrPropertiesInput

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


# SparkEmrPropertiesOutput

### computeArn
- **Type**: typing.Optional[str]

### credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.UsernamePassword]

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


# SparkEmrPropertiesPatch

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


# SparkGlueArgs

### connection
- **Type**: typing.Optional[str]


# SparkGluePropertiesInput

### additionalArgs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SparkGlueArgs]

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


# SparkGluePropertiesOutput

### additionalArgs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SparkGlueArgs]

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


# SsoUserProfileDetails

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### username
- **Type**: typing.Optional[str]


# StartDataSourceRunInput

### dataSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartDataSourceRunOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSourceConfigurationSnapshot
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### runStatisticsForAssets
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RunStatisticsForAssets'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### stoppedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: typing.Literal['PRIORITIZED', 'SCHEDULED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# StartMetadataGenerationRunInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataGenerationRunTarget'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BUSINESS_DESCRIPTIONS']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartMetadataGenerationRunOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCEEDED']
- **Required**: Yes

### type
- **Type**: typing.Literal['BUSINESS_DESCRIPTIONS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# SubscribedAsset

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetScope]

### failureCause
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FailureCause]

### failureTimestamp
- **Type**: typing.Optional[datetime.datetime]

### grantedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### targetName
- **Type**: typing.Optional[str]


# SubscribedAssetListing

### assetScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetScope]

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### entityType
- **Type**: typing.Optional[str]

### forms
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]


# SubscribedListing

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### item
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListingItem'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerProjectName
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]


# SubscribedListingInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# SubscribedListingItem

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedAssetListing]

### productListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedProductListing]


# SubscribedPrincipal

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedProject]


# SubscribedPrincipalInput

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedProjectInput]


# SubscribedProductListing

### assetListings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetInDataProductListingItem]]

### description
- **Type**: typing.Optional[str]

### entityId
- **Type**: typing.Optional[str]

### entityRevision
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DetailedGlossaryTerm]]

### name
- **Type**: typing.Optional[str]


# SubscribedProject

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# SubscribedProjectInput

### identifier
- **Type**: typing.Optional[str]


# SubscriptionGrantSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.GrantedEntity'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'GRANT_AND_REVOKE_FAILED', 'GRANT_FAILED', 'INACCESSIBLE', 'IN_PROGRESS', 'PENDING', 'REVOKE_FAILED']
- **Required**: Yes

### subscriptionTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedAsset]]

### subscriptionId
- **Type**: typing.Optional[str]

### updatedBy
- **Type**: typing.Optional[str]


# SubscriptionRequestSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### subscribedListings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### decisionComment
- **Type**: typing.Optional[str]

### existingSubscriptionId
- **Type**: typing.Optional[str]

### metadataFormsSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.MetadataFormSummary]]

### reviewerId
- **Type**: typing.Optional[str]

### updatedBy
- **Type**: typing.Optional[str]


# SubscriptionSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['APPROVED', 'CANCELLED', 'REVOKED']
- **Required**: Yes

### subscribedListing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### retainPermissions
- **Type**: typing.Optional[bool]

### subscriptionRequestId
- **Type**: typing.Optional[str]

### updatedBy
- **Type**: typing.Optional[str]


# SubscriptionTargetForm

### content
- **Type**: <class 'str'>
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes


# SubscriptionTargetSummary

### applicableAssetTypes
- **Type**: typing.List[str]
- **Required**: Yes

### authorizedPrincipals
- **Type**: typing.List[str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionTargetForm]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRole
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TermRelations

### classifies
- **Type**: typing.Optional[typing.List[str]]

### isA
- **Type**: typing.Optional[typing.List[str]]


# TermRelationsOutput

### classifies
- **Type**: typing.Optional[typing.List[str]]

### isA
- **Type**: typing.Optional[typing.List[str]]


# TimeSeriesDataPointFormInput

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# TimeSeriesDataPointFormOutput

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# TimeSeriesDataPointSummaryFormOutput

### formName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### typeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### contentSummary
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### typeRevision
- **Type**: typing.Optional[str]


# Topic

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.NotificationResource'>
- **Required**: Yes

### role
- **Type**: typing.Literal['DOMAIN_OWNER', 'PROJECT_CONTRIBUTOR', 'PROJECT_OWNER', 'PROJECT_SUBSCRIBER', 'PROJECT_VIEWER']
- **Required**: Yes

### subject
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAssetFilterInput

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterConfigurationOutput, NoneType]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateAssetFilterOutput

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.AssetFilterConfigurationOutput'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### effectiveColumnNames
- **Type**: typing.List[str]
- **Required**: Yes

### effectiveRowFilter
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['INVALID', 'VALID']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConnectionInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### awsLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.AwsLocation]

### description
- **Type**: typing.Optional[str]

### props
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionPropertiesPatch]


# UpdateConnectionOutput

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### physicalEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.PhysicalEndpoint]
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### props
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ConnectionPropertiesOutput'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSourceInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### assetFormsInput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormInput]]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceConfigurationInput]

### description
- **Type**: typing.Optional[str]

### enableSetting
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### name
- **Type**: typing.Optional[str]

### publishOnImport
- **Type**: typing.Optional[bool]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.RecommendationConfiguration]

### retainPermissionsOnRevokeFailure
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ScheduleConfiguration]


# UpdateDataSourceOutput

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceConfigurationOutput'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### enableSetting
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastRunAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastRunErrorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DataSourceErrorMessage'>
- **Required**: Yes

### lastRunStatus
- **Type**: typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### publishOnImport
- **Type**: <class 'bool'>
- **Required**: Yes

### recommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RecommendationConfiguration'>
- **Required**: Yes

### retainPermissionsOnRevokeFailure
- **Type**: <class 'bool'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ScheduleConfiguration'>
- **Required**: Yes

### selfGrantStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SelfGrantStatusOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SingleSignOn]


# UpdateDomainOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rootDomainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceRole
- **Type**: <class 'str'>
- **Required**: Yes

### singleSignOn
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.SingleSignOn'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainUnitInput

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


# UpdateDomainUnitOutput

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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owners
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.DomainUnitOwnerProperties]
- **Required**: Yes

### parentDomainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentActionInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.ActionParameters]


# UpdateEnvironmentActionOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ActionParameters'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]


# UpdateEnvironmentOutput

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountRegion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.DeploymentProperties'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ConfigurableEnvironmentAction]
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.Deployment'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.Resource]
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ProvisioningProperties'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.CustomParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentProfileInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentParameter]]


# UpdateEnvironmentProfileOutput

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountRegion
- **Type**: <class 'str'>
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

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.CustomParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGlossaryInput

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


# UpdateGlossaryOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGlossaryTermInput

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelations, aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelationsOutput, NoneType]


# UpdateGlossaryTermOutput

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### glossaryId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### longDescription
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### shortDescription
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### termRelations
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.TermRelationsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGroupProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'NOT_ASSIGNED']
- **Required**: Yes


# UpdateGroupProfileOutput

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### groupName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'NOT_ASSIGNED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### environmentDeploymentDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentDeploymentDetails, aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentDeploymentDetailsOutput, NoneType]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]


# UpdateProjectOutput

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

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentDeploymentDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentDeploymentDetailsOutput'>
- **Required**: Yes

### failureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.ProjectDeletionError]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### projectStatus
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationUserParameterOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectProfileInput

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfiguration, aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationOutput]]]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateProjectProfileOutput

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

### domainUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.EnvironmentConfigurationOutput]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRuleInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### detail
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleDetail, aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleDetailOutput, NoneType]

### includeChildDomainUnits
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### scope
- **Type**: typing.Union[aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScope, aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScopeOutput, NoneType]


# UpdateRuleOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleDetailOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleScopeOutput'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.RuleTarget'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubscriptionGrantStatusInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.FailureCause]

### targetName
- **Type**: typing.Optional[str]


# UpdateSubscriptionGrantStatusOutput

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedAsset]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.GrantedEntity'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'GRANT_AND_REVOKE_FAILED', 'GRANT_FAILED', 'INACCESSIBLE', 'IN_PROGRESS', 'PENDING', 'REVOKE_FAILED']
- **Required**: Yes

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubscriptionRequestInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSubscriptionRequestOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### existingSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadataForms
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.FormOutput]
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes

### reviewerId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### subscribedListings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedListing]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscribedPrincipal]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubscriptionTargetInput

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
- **Type**: typing.Optional[typing.List[str]]

### authorizedPrincipals
- **Type**: typing.Optional[typing.List[str]]

### manageAccessRole
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### provider
- **Type**: typing.Optional[str]

### subscriptionTargetConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionTargetForm]]


# UpdateSubscriptionTargetOutput

### applicableAssetTypes
- **Type**: typing.List[str]
- **Required**: Yes

### authorizedPrincipals
- **Type**: typing.List[str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionTargetConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone.datazone_classes.SubscriptionTargetForm]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserProfileInput

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATED', 'ASSIGNED', 'DEACTIVATED', 'NOT_ASSIGNED']
- **Required**: Yes

### userIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]


# UpdateUserProfileOutput

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.UserProfileDetails'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATED', 'ASSIGNED', 'DEACTIVATED', 'NOT_ASSIGNED']
- **Required**: Yes

### type
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone.datazone_classes.ResponseMetadata'>
- **Required**: Yes


# UserDetails

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# UserPolicyGrantPrincipal

### allUsersGrantFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### userIdentifier
- **Type**: typing.Optional[str]


# UserPolicyGrantPrincipalOutput

### allUsersGrantFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### userIdentifier
- **Type**: typing.Optional[str]


# UserProfileDetails

### iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.IamUserProfileDetails]

### sso
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.SsoUserProfileDetails]


# UserProfileSummary

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone.datazone_classes.UserProfileDetails]

### domainId
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'ASSIGNED', 'DEACTIVATED', 'NOT_ASSIGNED']]

### type
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]


# UsernamePassword

### password
- **Type**: <class 'str'>
- **Required**: Yes

### username
- **Type**: <class 'str'>
- **Required**: Yes


