# datazone_classes

# AcceptChoiceTypeDef

### predictionTarget
- **Type**: <class 'str'>
- **Required**: Yes

### editedValue
- **Type**: typing.Optional[str]

### predictionChoice
- **Type**: typing.Optional[int]


# AcceptPredictionsInputRequestTypeDef

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


# AcceptSubscriptionRequestInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: typing.Optional[str]


# AcceptSubscriptionRequestOutputTypeDef

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

### id
- **Type**: <class 'str'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef]
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


# ActionParametersTypeDef

### awsConsoleLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AwsConsoleLinkParametersTypeDef]


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


# AssociateEnvironmentRoleInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AwsConsoleLinkParametersTypeDef

### uri
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BusinessNameGenerationConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]


# CancelMetadataGenerationRunInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSubscriptionInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSubscriptionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudFormationPropertiesTypeDef

### templateUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurableActionParameterTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ConfigurableEnvironmentActionTypeDef

### parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ConfigurableActionParameterTypeDef]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### auth
- **Type**: typing.Optional[typing.Literal['HTTPS', 'IAM']]


# CreateAssetInputRequestTypeDef

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


# CreateAssetOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]
- **Required**: Yes

### listing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.AssetListingDetailsTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### predictionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.PredictionConfigurationTypeDef'>
- **Required**: Yes

### readOnlyFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssetRevisionInputRequestTypeDef

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


# CreateAssetRevisionOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]
- **Required**: Yes

### listing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.AssetListingDetailsTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### predictionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.PredictionConfigurationTypeDef'>
- **Required**: Yes

### readOnlyFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssetTypeInputRequestTypeDef

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


# CreateDataSourceInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.FormInputTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataSourceConfigurationInputTypeDef]

### description
- **Type**: typing.Optional[str]

### enableSetting
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### publishOnImport
- **Type**: typing.Optional[bool]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RecommendationConfigurationTypeDef]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ScheduleConfigurationTypeDef]


# CreateDataSourceOutputTypeDef

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceConfigurationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastRunAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastRunErrorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RecommendationConfigurationTypeDef'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ScheduleConfigurationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainInputRequestTypeDef

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

### kmsKeyIdentifier
- **Type**: typing.Optional[str]

### singleSignOn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SingleSignOnTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDomainOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainExecutionRole
- **Type**: <class 'str'>
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

### singleSignOn
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SingleSignOnTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentActionInputRequestTypeDef

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


# CreateEnvironmentActionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ActionParametersTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentInputRequestTypeDef

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

### description
- **Type**: typing.Optional[str]

### environmentAccountIdentifier
- **Type**: typing.Optional[str]

### environmentAccountRegion
- **Type**: typing.Optional[str]

### environmentBlueprintIdentifier
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]

### userParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.EnvironmentParameterTypeDef]]


# CreateEnvironmentOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DeploymentPropertiesTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ConfigurableEnvironmentActionTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DeploymentTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ResourceTypeDef]
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ProvisioningPropertiesTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.CustomParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentProfileInputRequestTypeDef

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


# CreateEnvironmentProfileOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.CustomParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFormTypeInputRequestTypeDef

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


# CreateGlossaryInputRequestTypeDef

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


# CreateGlossaryOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGlossaryTermInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TermRelationsTypeDef]


# CreateGlossaryTermOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.TermRelationsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupProfileInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateGroupProfileOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateListingChangeSetInputRequestTypeDef

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
- **Type**: typing.Literal['ASSET']
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


# CreateProjectInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateProjectMembershipInputRequestTypeDef

### designation
- **Type**: typing.Literal['PROJECT_CONTRIBUTOR', 'PROJECT_OWNER']
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


# CreateProjectOutputTypeDef

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

### failureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProjectDeletionErrorTypeDef]
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

### projectStatus
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriptionGrantInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### grantedEntity
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.GrantedEntityInputTypeDef'>
- **Required**: Yes

### subscriptionTargetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### assetTargetNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.AssetTargetNameMapTypeDef]]

### clientToken
- **Type**: typing.Optional[str]


# CreateSubscriptionGrantOutputTypeDef

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedAssetTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.GrantedEntityTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriptionRequestInputRequestTypeDef

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


# CreateSubscriptionRequestOutputTypeDef

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

### id
- **Type**: <class 'str'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef]
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


# CreateSubscriptionTargetInputRequestTypeDef

### applicableAssetTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### authorizedPrincipals
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionTargetFormTypeDef]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### provider
- **Type**: typing.Optional[str]


# CreateSubscriptionTargetOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionTargetFormTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserProfileInputRequestTypeDef

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


# CreateUserProfileOutputTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.UserProfileDetailsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# DataProductItemTypeDef

### domainId
- **Type**: typing.Optional[str]

### itemId
- **Type**: typing.Optional[str]


# DataProductSummaryTypeDef

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

### dataProductItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.DataProductItemTypeDef]]

### description
- **Type**: typing.Optional[str]

### glossaryTerms
- **Type**: typing.Optional[typing.List[str]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# DataSourceConfigurationInputTypeDef

### glueRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueRunConfigurationInputTypeDef]

### redshiftRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftRunConfigurationInputTypeDef]


# DataSourceConfigurationOutputTypeDef

### glueRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlueRunConfigurationOutputTypeDef]

### redshiftRunConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftRunConfigurationOutputTypeDef]


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

### technicalDescription
- **Type**: typing.Optional[str]


# DataSourceRunSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef]

### runStatisticsForAssets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RunStatisticsForAssetsTypeDef]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### stoppedAt
- **Type**: typing.Optional[datetime.datetime]


# DataSourceSummaryTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
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

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### enableSetting
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### lastRunAssetCount
- **Type**: typing.Optional[int]

### lastRunAt
- **Type**: typing.Optional[datetime.datetime]

### lastRunErrorMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef]

### lastRunStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PARTIALLY_SUCCEEDED', 'REQUESTED', 'RUNNING', 'SUCCESS']]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.ScheduleConfigurationTypeDef]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteAssetInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssetTypeInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceInputRequestTypeDef

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


# DeleteDataSourceOutputTypeDef

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceConfigurationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastRunAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastRunErrorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### selfGrantStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SelfGrantStatusOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainInputRequestTypeDef

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


# DeleteEnvironmentActionInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentProfileInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFormTypeInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### formTypeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlossaryInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlossaryTermInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListingInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipDeletionCheck
- **Type**: typing.Optional[bool]


# DeleteProjectMembershipInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.MemberTypeDef'>
- **Required**: Yes

### projectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionGrantInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionGrantOutputTypeDef

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedAssetTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.GrantedEntityTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSubscriptionRequestInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionTargetInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTimeSeriesDataPointsInputRequestTypeDef

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


# DisassociateEnvironmentRoleInputRequestTypeDef

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

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### portalUrl
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentActionSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ActionParametersTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


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

### manageAccessRoleArn
- **Type**: typing.Optional[str]

### provisioningRoleArn
- **Type**: typing.Optional[str]

### regionalParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EnvironmentBlueprintSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ProvisioningPropertiesTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


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


# EnvironmentSummaryTypeDef

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


# FailureCauseTypeDef

### message
- **Type**: typing.Optional[str]


# FilterClauseTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterTypeDef]


# FilterExpressionTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EXCLUDE', 'INCLUDE']
- **Required**: Yes


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


# GetAssetInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# GetAssetOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
- **Required**: Yes

### glossaryTerms
- **Type**: typing.List[str]
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### latestTimeSeriesDataPointFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]
- **Required**: Yes

### listing
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.AssetListingDetailsTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### readOnlyFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssetTypeInputRequestTypeDef

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


# GetDataSourceInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceOutputTypeDef

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceConfigurationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RecommendationConfigurationTypeDef'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### selfGrantStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SelfGrantStatusOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceRunInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceRunOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### runStatisticsForAssets
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RunStatisticsForAssetsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainInputRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainOutputTypeDef

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

### singleSignOn
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SingleSignOnTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentActionInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentActionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ActionParametersTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentBlueprintConfigurationInputRequestTypeDef

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

### manageAccessRoleArn
- **Type**: <class 'str'>
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


# GetEnvironmentBlueprintInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentBlueprintOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DeploymentPropertiesTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ProvisioningPropertiesTypeDef'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.CustomParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DeploymentPropertiesTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ConfigurableEnvironmentActionTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DeploymentTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ResourceTypeDef]
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ProvisioningPropertiesTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.CustomParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentProfileInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentProfileOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.CustomParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFormTypeInputRequestTypeDef

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


# GetGlossaryInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlossaryOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGlossaryTermInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlossaryTermOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.TermRelationsOutputTypeDef'>
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


# GetGroupProfileInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupProfileOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIamPortalLoginUrlInputRequestTypeDef

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


# GetLineageNodeInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### eventTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetLineageNodeOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.LineageNodeReferenceTypeDef]
- **Required**: Yes

### eventTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### formsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.LineageNodeReferenceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetListingInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### listingRevision
- **Type**: typing.Optional[str]


# GetListingOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ListingItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetadataGenerationRunInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetadataGenerationRunOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.MetadataGenerationRunTargetTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BUSINESS_DESCRIPTIONS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProjectInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectOutputTypeDef

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

### failureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProjectDeletionErrorTypeDef]
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

### projectStatus
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionGrantInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionGrantOutputTypeDef

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedAssetTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.GrantedEntityTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionRequestDetailsInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionRequestDetailsOutputTypeDef

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

### id
- **Type**: <class 'str'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef]
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


# GetSubscriptionTargetInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionTargetOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionTargetFormTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTimeSeriesDataPointInputRequestTypeDef

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


# GetUserProfileInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]


# GetUserProfileOutputTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.UserProfileDetailsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlossaryItemTypeDef

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


# GlossaryTermItemTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TermRelationsOutputTypeDef]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# GlueRunConfigurationInputTypeDef

### relationalFilterConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.RelationalFilterConfigurationTypeDef]
- **Required**: Yes

### autoImportDataQualityResult
- **Type**: typing.Optional[bool]

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


# GroupDetailsTypeDef

### groupId
- **Type**: <class 'str'>
- **Required**: Yes


# GroupProfileSummaryTypeDef

### domainId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'NOT_ASSIGNED']]


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


# LineageNodeReferenceTypeDef

### eventTimestamp
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]


# LineageNodeSummaryTypeDef

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


# ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListAssetRevisionsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef

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


# ListDataSourceRunActivitiesInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef

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


# ListDataSourceRunsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourcesInputListDataSourcesPaginateTypeDef

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

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']]

### type
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListDataSourcesInputRequestTypeDef

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

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'READY', 'RUNNING', 'UPDATING']]

### type
- **Type**: typing.Optional[str]


# ListDataSourcesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.DataSourceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsInputListDomainsPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListDomainsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentActionsInputListEnvironmentActionsPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentActionsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentBlueprintConfigurationsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### managed
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListEnvironmentBlueprintsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef

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


# ListEnvironmentProfilesInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentsInputListEnvironmentsPaginateTypeDef

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


# ListEnvironmentsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLineageNodeHistoryInputListLineageNodeHistoryPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListLineageNodeHistoryInputRequestTypeDef

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


# ListLineageNodeHistoryOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.LineageNodeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetadataGenerationRunsInputListMetadataGenerationRunsPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCEEDED']]

### type
- **Type**: typing.Optional[typing.Literal['BUSINESS_DESCRIPTIONS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListMetadataGenerationRunsInputRequestTypeDef

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


# ListMetadataGenerationRunsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.MetadataGenerationRunItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNotificationsInputListNotificationsPaginateTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### taskStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListNotificationsInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### taskStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# ListNotificationsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.NotificationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef

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


# ListProjectMembershipsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsInputListProjectsPaginateTypeDef

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


# ListProjectsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
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


# ListSubscriptionGrantsInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef

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


# ListSubscriptionRequestsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef

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


# ListSubscriptionTargetsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscriptionsInputListSubscriptionsPaginateTypeDef

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


# ListSubscriptionsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTimeSeriesDataPointsInputListTimeSeriesDataPointsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# ListTimeSeriesDataPointsInputRequestTypeDef

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


# ListTimeSeriesDataPointsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.TimeSeriesDataPointSummaryFormOutputTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListingItemTypeDef

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetListingTypeDef]


# ListingRevisionInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes


# ListingRevisionTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'str'>
- **Required**: Yes


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


# MetadataGenerationRunItemTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.MetadataGenerationRunTargetTypeDef]

### type
- **Type**: typing.Optional[typing.Literal['BUSINESS_DESCRIPTIONS']]


# MetadataGenerationRunTargetTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ASSET']
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]


# ModelTypeDef

### smithy
- **Type**: typing.Optional[str]


# NotificationOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.TopicTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EVENT', 'TASK']
- **Required**: Yes

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# NotificationResourceTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['PROJECT']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PostLineageEventInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PostTimeSeriesDataPointsInputRequestTypeDef

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


# ProjectMemberTypeDef

### designation
- **Type**: typing.Literal['PROJECT_CONTRIBUTOR', 'PROJECT_OWNER']
- **Required**: Yes

### memberDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.MemberDetailsTypeDef'>
- **Required**: Yes


# ProjectSummaryTypeDef

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

### failureReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProjectDeletionErrorTypeDef]]

### projectStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ProvisioningPropertiesTypeDef

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.CloudFormationPropertiesTypeDef]


# PutEnvironmentBlueprintConfigurationInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### enabledRegions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### environmentBlueprintIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### manageAccessRoleArn
- **Type**: typing.Optional[str]

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

### manageAccessRoleArn
- **Type**: <class 'str'>
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


# RedshiftRunConfigurationInputTypeDef

### redshiftCredentialConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RedshiftCredentialConfigurationTypeDef'>
- **Required**: Yes

### redshiftStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RedshiftStorageTypeDef'>
- **Required**: Yes

### relationalFilterConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.RelationalFilterConfigurationTypeDef]
- **Required**: Yes

### dataAccessRole
- **Type**: typing.Optional[str]


# RedshiftRunConfigurationOutputTypeDef

### redshiftCredentialConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RedshiftCredentialConfigurationTypeDef'>
- **Required**: Yes

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


# RedshiftStorageTypeDef

### redshiftClusterSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftClusterStorageTypeDef]

### redshiftServerlessSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.RedshiftServerlessStorageTypeDef]


# RejectChoiceTypeDef

### predictionTarget
- **Type**: <class 'str'>
- **Required**: Yes

### predictionChoices
- **Type**: typing.Optional[typing.Sequence[int]]


# RejectPredictionsInputRequestTypeDef

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


# RejectSubscriptionRequestInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### decisionComment
- **Type**: typing.Optional[str]


# RejectSubscriptionRequestOutputTypeDef

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

### id
- **Type**: <class 'str'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef]
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


# ResourceTypeDef

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


# RevokeSubscriptionInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### retainPermissions
- **Type**: typing.Optional[bool]


# RevokeSubscriptionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ScheduleConfigurationTypeDef

### schedule
- **Type**: typing.Optional[str]

### timezone
- **Type**: typing.Optional[typing.Literal['AFRICA_JOHANNESBURG', 'AMERICA_MONTREAL', 'AMERICA_SAO_PAULO', 'ASIA_BAHRAIN', 'ASIA_BANGKOK', 'ASIA_CALCUTTA', 'ASIA_DUBAI', 'ASIA_HONG_KONG', 'ASIA_JAKARTA', 'ASIA_KUALA_LUMPUR', 'ASIA_SEOUL', 'ASIA_SHANGHAI', 'ASIA_SINGAPORE', 'ASIA_TAIPEI', 'ASIA_TOKYO', 'AUSTRALIA_MELBOURNE', 'AUSTRALIA_SYDNEY', 'CANADA_CENTRAL', 'CET', 'CST6CDT', 'ETC_GMT', 'ETC_GMT0', 'ETC_GMT_ADD_0', 'ETC_GMT_ADD_1', 'ETC_GMT_ADD_10', 'ETC_GMT_ADD_11', 'ETC_GMT_ADD_12', 'ETC_GMT_ADD_2', 'ETC_GMT_ADD_3', 'ETC_GMT_ADD_4', 'ETC_GMT_ADD_5', 'ETC_GMT_ADD_6', 'ETC_GMT_ADD_7', 'ETC_GMT_ADD_8', 'ETC_GMT_ADD_9', 'ETC_GMT_NEG_0', 'ETC_GMT_NEG_1', 'ETC_GMT_NEG_10', 'ETC_GMT_NEG_11', 'ETC_GMT_NEG_12', 'ETC_GMT_NEG_13', 'ETC_GMT_NEG_14', 'ETC_GMT_NEG_2', 'ETC_GMT_NEG_3', 'ETC_GMT_NEG_4', 'ETC_GMT_NEG_5', 'ETC_GMT_NEG_6', 'ETC_GMT_NEG_7', 'ETC_GMT_NEG_8', 'ETC_GMT_NEG_9', 'EUROPE_DUBLIN', 'EUROPE_LONDON', 'EUROPE_PARIS', 'EUROPE_STOCKHOLM', 'EUROPE_ZURICH', 'ISRAEL', 'MEXICO_GENERAL', 'MST7MDT', 'PACIFIC_AUCKLAND', 'US_CENTRAL', 'US_EASTERN', 'US_MOUNTAIN', 'US_PACIFIC', 'UTC']]


# SearchGroupProfilesInputRequestTypeDef

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


# SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef

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


# SearchGroupProfilesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.GroupProfileSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchInItemTypeDef

### attribute
- **Type**: <class 'str'>
- **Required**: Yes


# SearchInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET', 'GLOSSARY', 'GLOSSARY_TERM']
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


# SearchInputSearchPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### searchScope
- **Type**: typing.Literal['ASSET', 'GLOSSARY', 'GLOSSARY_TERM']
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClauseTypeDef]

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


# SearchInventoryResultItemTypeDef

### assetItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetItemTypeDef]

### dataProductItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.DataProductSummaryTypeDef]

### glossaryItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlossaryItemTypeDef]

### glossaryTermItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.GlossaryTermItemTypeDef]


# SearchListingsInputRequestTypeDef

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


# SearchListingsInputSearchListingsPaginateTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS']]]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FilterClauseTypeDef]

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# SearchListingsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SearchResultItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SearchInventoryResultItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchResultItemTypeDef

### assetListing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetListingItemTypeDef]


# SearchSortTypeDef

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SearchTypesInputRequestTypeDef

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


# SearchTypesInputSearchTypesPaginateTypeDef

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

### searchIn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datazone_classes.SearchInItemTypeDef]]

### searchText
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SearchSortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.PaginatorConfigTypeDef]


# SearchTypesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SearchTypesResultItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### totalMatchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchTypesResultItemTypeDef

### assetTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.AssetTypeItemTypeDef]

### formTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.FormTypeDataTypeDef]

### lineageNodeTypeItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.LineageNodeTypeItemTypeDef]


# SearchUserProfilesInputRequestTypeDef

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


# SearchUserProfilesInputSearchUserProfilesPaginateTypeDef

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


# SearchUserProfilesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.UserProfileSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### type
- **Type**: typing.Optional[typing.Literal['DISABLED', 'IAM_IDC']]

### userAssignment
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]


# SsoUserProfileDetailsTypeDef

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### username
- **Type**: typing.Optional[str]


# StartDataSourceRunInputRequestTypeDef

### dataSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartDataSourceRunOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### runStatisticsForAssets
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RunStatisticsForAssetsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMetadataGenerationRunInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### owningProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.MetadataGenerationRunTargetTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BUSINESS_DESCRIPTIONS']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartMetadataGenerationRunOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubscribedAssetListingTypeDef

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


# SubscribedListingTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### item
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingItemTypeDef'>
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


# SubscribedPrincipalInputTypeDef

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SubscribedProjectInputTypeDef]


# SubscribedPrincipalTypeDef

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SubscribedProjectTypeDef]


# SubscribedProjectInputTypeDef

### identifier
- **Type**: typing.Optional[str]


# SubscribedProjectTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# SubscriptionGrantSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.GrantedEntityTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedAssetTypeDef]]

### subscriptionId
- **Type**: typing.Optional[str]

### updatedBy
- **Type**: typing.Optional[str]


# SubscriptionRequestSummaryTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### decisionComment
- **Type**: typing.Optional[str]

### reviewerId
- **Type**: typing.Optional[str]

### updatedBy
- **Type**: typing.Optional[str]


# SubscriptionSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef'>
- **Required**: Yes

### subscribedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef'>
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


# SubscriptionTargetFormTypeDef

### content
- **Type**: <class 'str'>
- **Required**: Yes

### formName
- **Type**: <class 'str'>
- **Required**: Yes


# SubscriptionTargetSummaryTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionTargetFormTypeDef]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TermRelationsExtraOutputTypeDef

### classifies
- **Type**: typing.Optional[typing.List[str]]

### isA
- **Type**: typing.Optional[typing.List[str]]


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


# TimeSeriesDataPointFormInputTypeDef

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


# TimeSeriesDataPointFormOutputTypeDef

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


# TimeSeriesDataPointSummaryFormOutputTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDataSourceInputRequestTypeDef

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


# UpdateDataSourceOutputTypeDef

### assetFormsOutput
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.FormOutputTypeDef]
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceConfigurationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastRunAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastRunErrorMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DataSourceErrorMessageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.RecommendationConfigurationTypeDef'>
- **Required**: Yes

### retainPermissionsOnRevokeFailure
- **Type**: <class 'bool'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### selfGrantStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SelfGrantStatusOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainInputRequestTypeDef

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

### singleSignOn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SingleSignOnTypeDef]


# UpdateDomainOutputTypeDef

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

### singleSignOn
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.SingleSignOnTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentActionInputRequestTypeDef

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


# UpdateEnvironmentActionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ActionParametersTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentInputRequestTypeDef

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


# UpdateEnvironmentOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DeploymentPropertiesTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### domainId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ConfigurableEnvironmentActionTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.DeploymentTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ResourceTypeDef]
- **Required**: Yes

### provisioningProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ProvisioningPropertiesTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'DISABLED', 'EXPIRED', 'INACCESSIBLE', 'SUSPENDED', 'UPDATE_FAILED', 'UPDATING', 'VALIDATION_FAILED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### userParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.CustomParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentProfileInputRequestTypeDef

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


# UpdateEnvironmentProfileOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.CustomParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlossaryInputRequestTypeDef

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


# UpdateGlossaryOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlossaryTermInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.TermRelationsTypeDef]


# UpdateGlossaryTermOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.TermRelationsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGroupProfileInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### groupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'NOT_ASSIGNED']
- **Required**: Yes


# UpdateGroupProfileOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectInputRequestTypeDef

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


# UpdateProjectOutputTypeDef

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

### failureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.ProjectDeletionErrorTypeDef]
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

### projectStatus
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSubscriptionGrantStatusInputRequestTypeDef

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


# UpdateSubscriptionGrantStatusOutputTypeDef

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedAssetTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.GrantedEntityTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSubscriptionRequestInputRequestTypeDef

### domainIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### requestReason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSubscriptionRequestOutputTypeDef

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

### id
- **Type**: <class 'str'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedListingTypeDef]
- **Required**: Yes

### subscribedPrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscribedPrincipalTypeDef]
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


# UpdateSubscriptionTargetInputRequestTypeDef

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


# UpdateSubscriptionTargetOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datazone_classes.SubscriptionTargetFormTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserProfileInputRequestTypeDef

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


# UpdateUserProfileOutputTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.UserProfileDetailsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datazone_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserDetailsTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# UserProfileDetailsTypeDef

### iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.IamUserProfileDetailsTypeDef]

### sso
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.SsoUserProfileDetailsTypeDef]


# UserProfileSummaryTypeDef

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datazone_classes.UserProfileDetailsTypeDef]

### domainId
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'ASSIGNED', 'DEACTIVATED', 'NOT_ASSIGNED']]

### type
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]


