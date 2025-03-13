# Resiliencehub Classes

# AcceptGroupingRecommendationEntryTypeDef

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptResourceGroupingRecommendationsRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.AcceptGroupingRecommendationEntryTypeDef]
- **Required**: Yes


# AcceptResourceGroupingRecommendationsResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### failedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.FailedGroupingRecommendationEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddDraftAppVersionResourceMappingsRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceMappingTypeDef]
- **Required**: Yes


# AddDraftAppVersionResourceMappingsResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### resourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AlarmRecommendationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmTypeDef

### alarmArn
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]


# AppAssessmentSummaryTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentStatus
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### appVersion
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### complianceStatus
- **Type**: typing.Optional[typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.CostTypeDef]

### driftStatus
- **Type**: typing.Optional[typing.Literal['Detected', 'NotChecked', 'NotDetected']]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### invoker
- **Type**: typing.Optional[typing.Literal['System', 'User']]

### message
- **Type**: typing.Optional[str]

### resiliencyScore
- **Type**: typing.Optional[float]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### versionName
- **Type**: typing.Optional[str]


# AppAssessmentTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentStatus
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### invoker
- **Type**: typing.Literal['System', 'User']
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### appVersion
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### compliance
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.DisruptionComplianceTypeDef]]

### complianceStatus
- **Type**: typing.Optional[typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.CostTypeDef]

### driftStatus
- **Type**: typing.Optional[typing.Literal['Detected', 'NotChecked', 'NotDetected']]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef]

### resiliencyScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyScoreTypeDef]

### resourceErrorsDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceErrorsDetailsTypeDef]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.AssessmentSummaryTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionName
- **Type**: typing.Optional[str]


# AppComponentComplianceTypeDef

### appComponentName
- **Type**: typing.Optional[str]

### compliance
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.DisruptionComplianceTypeDef]]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.CostTypeDef]

### message
- **Type**: typing.Optional[str]

### resiliencyScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyScoreTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']]


# AppComponentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppInputSourceTypeDef

### importType
- **Type**: typing.Literal['AppRegistryApp', 'CfnStack', 'EKS', 'Resource', 'ResourceGroup', 'Terraform']
- **Required**: Yes

### eksSourceClusterNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.EksSourceClusterNamespaceTypeDef]

### resourceCount
- **Type**: typing.Optional[int]

### sourceArn
- **Type**: typing.Optional[str]

### sourceName
- **Type**: typing.Optional[str]

### terraformSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.TerraformSourceTypeDef]


# AppSummaryTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentSchedule
- **Type**: typing.Optional[typing.Literal['Daily', 'Disabled']]

### awsApplicationArn
- **Type**: typing.Optional[str]

### complianceStatus
- **Type**: typing.Optional[typing.Literal['ChangesDetected', 'MissingPolicy', 'NotApplicable', 'NotAssessed', 'PolicyBreached', 'PolicyMet']]

### description
- **Type**: typing.Optional[str]

### driftStatus
- **Type**: typing.Optional[typing.Literal['Detected', 'NotChecked', 'NotDetected']]

### lastAppComplianceEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### resiliencyScore
- **Type**: typing.Optional[float]

### rpoInSecs
- **Type**: typing.Optional[int]

### rtoInSecs
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Deleting']]


# AppTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentSchedule
- **Type**: typing.Optional[typing.Literal['Daily', 'Disabled']]

### awsApplicationArn
- **Type**: typing.Optional[str]

### complianceStatus
- **Type**: typing.Optional[typing.Literal['ChangesDetected', 'MissingPolicy', 'NotApplicable', 'NotAssessed', 'PolicyBreached', 'PolicyMet']]

### description
- **Type**: typing.Optional[str]

### driftStatus
- **Type**: typing.Optional[typing.Literal['Detected', 'NotChecked', 'NotDetected']]

### eventSubscriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.EventSubscriptionTypeDef]]

### lastAppComplianceEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### lastDriftEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### lastResiliencyScoreEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### permissionModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PermissionModelOutputTypeDef]

### policyArn
- **Type**: typing.Optional[str]

### resiliencyScore
- **Type**: typing.Optional[float]

### rpoInSecs
- **Type**: typing.Optional[int]

### rtoInSecs
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Deleting']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AppVersionSummaryTypeDef

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### identifier
- **Type**: typing.Optional[int]

### versionName
- **Type**: typing.Optional[str]


# AssessmentRiskRecommendationTypeDef

### appComponents
- **Type**: typing.Optional[typing.List[str]]

### recommendation
- **Type**: typing.Optional[str]

### risk
- **Type**: typing.Optional[str]


# AssessmentSummaryTypeDef

### riskRecommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AssessmentRiskRecommendationTypeDef]]

### summary
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateRecommendationStatusFailedEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# BatchUpdateRecommendationStatusRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### requestEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.UpdateRecommendationStatusRequestEntryTypeDef]
- **Required**: Yes


# BatchUpdateRecommendationStatusResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### failedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.BatchUpdateRecommendationStatusFailedEntryTypeDef]
- **Required**: Yes

### successfulEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.BatchUpdateRecommendationStatusSuccessfulEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateRecommendationStatusSuccessfulEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### excluded
- **Type**: <class 'bool'>
- **Required**: Yes

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentId
- **Type**: typing.Optional[str]

### excludeReason
- **Type**: typing.Optional[typing.Literal['AlreadyImplemented', 'ComplexityOfImplementation', 'NotRelevant']]

### item
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.UpdateRecommendationStatusItemTypeDef]


# ComplianceDriftTypeDef

### actualReferenceId
- **Type**: typing.Optional[str]

### actualValue
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.DisruptionComplianceTypeDef]]

### appId
- **Type**: typing.Optional[str]

### appVersion
- **Type**: typing.Optional[str]

### diffType
- **Type**: typing.Optional[typing.Literal['Added', 'NotEqual', 'Removed']]

### driftType
- **Type**: typing.Optional[typing.Literal['AppComponentResiliencyComplianceStatus', 'ApplicationCompliance']]

### entityId
- **Type**: typing.Optional[str]

### entityType
- **Type**: typing.Optional[str]

### expectedReferenceId
- **Type**: typing.Optional[str]

### expectedValue
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.DisruptionComplianceTypeDef]]


# ComponentRecommendationTypeDef

### appComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### configRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ConfigRecommendationTypeDef]
- **Required**: Yes

### recommendationStatus
- **Type**: typing.Literal['BreachedCanMeet', 'BreachedUnattainable', 'MetCanImprove', 'MissingPolicy']
- **Required**: Yes


# ConditionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigRecommendationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### optimizationType
- **Type**: typing.Literal['BestAZRecovery', 'BestAttainable', 'BestRegionRecovery', 'LeastChange', 'LeastCost', 'LeastErrors']
- **Required**: Yes

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentName
- **Type**: typing.Optional[str]

### compliance
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.DisruptionComplianceTypeDef]]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.CostTypeDef]

### description
- **Type**: typing.Optional[str]

### haArchitecture
- **Type**: typing.Optional[typing.Literal['BackupAndRestore', 'MultiSite', 'NoRecoveryPlan', 'PilotLight', 'WarmStandby']]

### recommendationCompliance
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationDisruptionComplianceTypeDef]]

### suggestedChanges
- **Type**: typing.Optional[typing.List[str]]


# CostTypeDef

### amount
- **Type**: <class 'float'>
- **Required**: Yes

### currency
- **Type**: <class 'str'>
- **Required**: Yes

### frequency
- **Type**: typing.Literal['Daily', 'Hourly', 'Monthly', 'Yearly']
- **Required**: Yes


# CreateAppRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentSchedule
- **Type**: typing.Optional[typing.Literal['Daily', 'Disabled']]

### awsApplicationArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### eventSubscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.EventSubscriptionTypeDef]]

### permissionModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PermissionModelUnionTypeDef]

### policyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAppResponseTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppVersionAppComponentResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppComponentTypeDef'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppVersionResourceRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponents
- **Type**: typing.Sequence[str]
- **Required**: Yes

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# CreateAppVersionResourceResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecommendationTemplateResponseTypeDef

### recommendationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResiliencyPolicyRequestTypeDef

### policy
- **Type**: typing.Mapping[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.FailurePolicyTypeDef]
- **Required**: Yes

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### tier
- **Type**: typing.Literal['CoreServices', 'Critical', 'Important', 'MissionCritical', 'NonCritical', 'NotApplicable']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### dataLocationConstraint
- **Type**: typing.Optional[typing.Literal['AnyLocation', 'SameContinent', 'SameCountry']]

### policyDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateResiliencyPolicyResponseTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppAssessmentRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAppAssessmentResponseTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentStatus
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppInputSourceRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### eksSourceClusterNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.EksSourceClusterNamespaceTypeDef]

### sourceArn
- **Type**: typing.Optional[str]

### terraformSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.TerraformSourceTypeDef]


# DeleteAppInputSourceResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appInputSource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppInputSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteAppResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppVersionAppComponentResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppComponentTypeDef'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppVersionResourceRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### logicalResourceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef]

### physicalResourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# DeleteAppVersionResourceResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRecommendationTemplateRequestTypeDef

### recommendationTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteRecommendationTemplateResponseTypeDef

### recommendationTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResiliencyPolicyRequestTypeDef

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteResiliencyPolicyResponseTypeDef

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppAssessmentRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppAssessmentResponseTypeDef

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppAssessmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppResponseTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppVersionAppComponentResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppComponentTypeDef'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppVersionRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppVersionResourceRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### logicalResourceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef]

### physicalResourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# DescribeAppVersionResourceResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppVersionResourcesResolutionStatusRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### resolutionId
- **Type**: typing.Optional[str]


# DescribeAppVersionResourcesResolutionStatusResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppVersionResponseTypeDef

### additionalInfo
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppVersionTemplateRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppVersionTemplateResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appTemplateBody
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDraftAppVersionResourcesImportStatusRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDraftAppVersionResourcesImportStatusResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### errorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ErrorDetailTypeDef]
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### statusChangeTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetricsExportRequestTypeDef

### metricsExportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMetricsExportResponseTypeDef

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### exportLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.S3LocationTypeDef'>
- **Required**: Yes

### metricsExportId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResiliencyPolicyRequestTypeDef

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResiliencyPolicyResponseTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceGroupingRecommendationTaskRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### groupingId
- **Type**: typing.Optional[str]


# DescribeResourceGroupingRecommendationTaskResponseTypeDef

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### groupingId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisruptionComplianceTypeDef

### complianceStatus
- **Type**: typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']
- **Required**: Yes

### achievableRpoInSecs
- **Type**: typing.Optional[int]

### achievableRtoInSecs
- **Type**: typing.Optional[int]

### currentRpoInSecs
- **Type**: typing.Optional[int]

### currentRtoInSecs
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]

### rpoDescription
- **Type**: typing.Optional[str]

### rpoReferenceId
- **Type**: typing.Optional[str]

### rtoDescription
- **Type**: typing.Optional[str]

### rtoReferenceId
- **Type**: typing.Optional[str]


# EksSourceClusterNamespaceTypeDef

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes


# EksSourceOutputTypeDef

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaces
- **Type**: typing.List[str]
- **Required**: Yes


# EksSourceTypeDef

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaces
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EksSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ErrorDetailTypeDef

### errorMessage
- **Type**: typing.Optional[str]


# EventSubscriptionTypeDef

### eventType
- **Type**: typing.Literal['DriftDetected', 'ScheduledAssessmentFailure']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### snsTopicArn
- **Type**: typing.Optional[str]


# ExperimentTypeDef

### experimentArn
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]


# FailedGroupingRecommendationEntryTypeDef

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# FailurePolicyTypeDef

### rpoInSecs
- **Type**: <class 'int'>
- **Required**: Yes

### rtoInSecs
- **Type**: <class 'int'>
- **Required**: Yes


# FieldTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### aggregation
- **Type**: typing.Optional[typing.Literal['Avg', 'Count', 'Max', 'Min', 'Sum']]


# GroupingAppComponentTypeDef

### appComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentType
- **Type**: <class 'str'>
- **Required**: Yes


# GroupingRecommendationTypeDef

### confidenceLevel
- **Type**: typing.Literal['High', 'Medium']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### groupingAppComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.GroupingAppComponentTypeDef'>
- **Required**: Yes

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationReasons
- **Type**: typing.List[str]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.GroupingResourceTypeDef]
- **Required**: Yes

### score
- **Type**: <class 'float'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Accepted', 'PendingDecision', 'Rejected']
- **Required**: Yes

### rejectionReason
- **Type**: typing.Optional[typing.Literal['DistinctBusinessPurpose', 'DistinctUserGroupHandling', 'Other', 'SeparateDataConcern']]


# GroupingResourceTypeDef

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceIdTypeDef'>
- **Required**: Yes

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### sourceAppComponentIds
- **Type**: typing.List[str]
- **Required**: Yes


# ImportResourcesToDraftAppVersionRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### eksSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.EksSourceUnionTypeDef]]

### importStrategy
- **Type**: typing.Optional[typing.Literal['AddOnly', 'ReplaceAll']]

### sourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### terraformSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.TerraformSourceTypeDef]]


# ImportResourcesToDraftAppVersionResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### eksSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.EksSourceOutputTypeDef]
- **Required**: Yes

### sourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### terraformSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.TerraformSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAlarmRecommendationsRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAlarmRecommendationsResponseTypeDef

### alarmRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AlarmRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentComplianceDriftsRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentComplianceDriftsResponseTypeDef

### complianceDrifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ComplianceDriftTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentResourceDriftsRequestPaginateTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PaginatorConfigTypeDef]


# ListAppAssessmentResourceDriftsRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentResourceDriftsResponseTypeDef

### resourceDrifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceDriftTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentsRequestTypeDef

### appArn
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### assessmentStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Failed', 'InProgress', 'Pending', 'Success']]]

### complianceStatus
- **Type**: typing.Optional[typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']]

### invoker
- **Type**: typing.Optional[typing.Literal['System', 'User']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]


# ListAppAssessmentsResponseTypeDef

### assessmentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppAssessmentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentCompliancesRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentCompliancesResponseTypeDef

### componentCompliances
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppComponentComplianceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentRecommendationsRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentRecommendationsResponseTypeDef

### componentRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ComponentRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppInputSourcesRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppInputSourcesResponseTypeDef

### appInputSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppInputSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionAppComponentsRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionAppComponentsResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppComponentTypeDef]
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionResourceMappingsRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionResourceMappingsResponseTypeDef

### resourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionResourcesRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resolutionId
- **Type**: typing.Optional[str]


# ListAppVersionResourcesResponseTypeDef

### physicalResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceTypeDef]
- **Required**: Yes

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionsRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.TimestampTypeDef]


# ListAppVersionsResponseTypeDef

### appVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppsRequestTypeDef

### appArn
- **Type**: typing.Optional[str]

### awsApplicationArn
- **Type**: typing.Optional[str]

### fromLastAssessmentTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]

### toLastAssessmentTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.TimestampTypeDef]


# ListAppsResponseTypeDef

### appSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetricsRequestPaginateTypeDef

### conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.ConditionTypeDef]]

### dataSource
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.FieldTypeDef]]

### sorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.SortTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PaginatorConfigTypeDef]


# ListMetricsRequestTypeDef

### conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.ConditionTypeDef]]

### dataSource
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.FieldTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.SortTypeDef]]


# ListMetricsResponseTypeDef

### rows
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationTemplatesRequestTypeDef

### assessmentArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### recommendationTemplateArn
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Failed', 'InProgress', 'Pending', 'Success']]]


# ListRecommendationTemplatesResponseTypeDef

### recommendationTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResiliencyPoliciesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]


# ListResiliencyPoliciesResponseTypeDef

### resiliencyPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGroupingRecommendationsRequestPaginateTypeDef

### appArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PaginatorConfigTypeDef]


# ListResourceGroupingRecommendationsRequestTypeDef

### appArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGroupingRecommendationsResponseTypeDef

### groupingRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.GroupingRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSopRecommendationsRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSopRecommendationsResponseTypeDef

### sopRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.SopRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuggestedResiliencyPoliciesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSuggestedResiliencyPoliciesResponseTypeDef

### resiliencyPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestRecommendationsRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestRecommendationsResponseTypeDef

### testRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.TestRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUnsupportedAppVersionResourcesRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resolutionId
- **Type**: typing.Optional[str]


# ListUnsupportedAppVersionResourcesResponseTypeDef

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### unsupportedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.UnsupportedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogicalResourceIdTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### eksSourceName
- **Type**: typing.Optional[str]

### logicalStackName
- **Type**: typing.Optional[str]

### resourceGroupName
- **Type**: typing.Optional[str]

### terraformSourceName
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionModelOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PermissionModelUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PhysicalResourceIdTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PhysicalResourceTypeDef

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceIdTypeDef'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### appComponents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppComponentTypeDef]]

### excluded
- **Type**: typing.Optional[bool]

### parentResourceName
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### sourceType
- **Type**: typing.Optional[typing.Literal['AppTemplate', 'Discovered']]


# PublishAppVersionRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: typing.Optional[str]


# PublishAppVersionResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'int'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDraftAppVersionTemplateRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appTemplateBody
- **Type**: <class 'str'>
- **Required**: Yes


# PutDraftAppVersionTemplateResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecommendationDisruptionComplianceTypeDef

### expectedComplianceStatus
- **Type**: typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']
- **Required**: Yes

### expectedRpoDescription
- **Type**: typing.Optional[str]

### expectedRpoInSecs
- **Type**: typing.Optional[int]

### expectedRtoDescription
- **Type**: typing.Optional[str]

### expectedRtoInSecs
- **Type**: typing.Optional[int]


# RecommendationItemTypeDef

### alreadyImplemented
- **Type**: typing.Optional[bool]

### discoveredAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.AlarmTypeDef]

### excludeReason
- **Type**: typing.Optional[typing.Literal['AlreadyImplemented', 'ComplexityOfImplementation', 'NotRelevant']]

### excluded
- **Type**: typing.Optional[bool]

### latestDiscoveredExperiment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.ExperimentTypeDef]

### resourceId
- **Type**: typing.Optional[str]

### targetAccountId
- **Type**: typing.Optional[str]

### targetRegion
- **Type**: typing.Optional[str]


# RecommendationTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RejectGroupingRecommendationEntryTypeDef

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### rejectionReason
- **Type**: typing.Optional[typing.Literal['DistinctBusinessPurpose', 'DistinctUserGroupHandling', 'Other', 'SeparateDataConcern']]


# RejectResourceGroupingRecommendationsRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.RejectGroupingRecommendationEntryTypeDef]
- **Required**: Yes


# RejectResourceGroupingRecommendationsResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### failedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.FailedGroupingRecommendationEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveDraftAppVersionResourceMappingsRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appRegistryAppNames
- **Type**: typing.Optional[typing.Sequence[str]]

### eksSourceNames
- **Type**: typing.Optional[typing.Sequence[str]]

### logicalStackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceNames
- **Type**: typing.Optional[typing.Sequence[str]]

### terraformSourceNames
- **Type**: typing.Optional[typing.Sequence[str]]


# RemoveDraftAppVersionResourceMappingsResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResiliencyPolicyTypeDef

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### dataLocationConstraint
- **Type**: typing.Optional[typing.Literal['AnyLocation', 'SameContinent', 'SameCountry']]

### estimatedCostTier
- **Type**: typing.Optional[typing.Literal['L1', 'L2', 'L3', 'L4']]

### policy
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.FailurePolicyTypeDef]]

### policyArn
- **Type**: typing.Optional[str]

### policyDescription
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### tier
- **Type**: typing.Optional[typing.Literal['CoreServices', 'Critical', 'Important', 'MissionCritical', 'NonCritical', 'NotApplicable']]


# ResiliencyScoreTypeDef

### disruptionScore
- **Type**: typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], float]
- **Required**: Yes

### score
- **Type**: <class 'float'>
- **Required**: Yes

### componentScore
- **Type**: typing.Optional[typing.Dict[typing.Literal['Alarm', 'Compliance', 'Sop', 'Test'], aws_resource_validator.pydantic_models.resiliencehub_classes.ScoringComponentResiliencyScoreTypeDef]]


# ResolveAppVersionResourcesRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ResolveAppVersionResourcesResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceDriftTypeDef

### appArn
- **Type**: typing.Optional[str]

### appVersion
- **Type**: typing.Optional[str]

### diffType
- **Type**: typing.Optional[typing.Literal['Added', 'NotEqual', 'Removed']]

### referenceId
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceIdentifierTypeDef]


# ResourceErrorTypeDef

### logicalResourceId
- **Type**: typing.Optional[str]

### physicalResourceId
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# ResourceErrorsDetailsTypeDef

### hasMoreErrors
- **Type**: typing.Optional[bool]

### resourceErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceErrorTypeDef]]


# ResourceIdentifierTypeDef

### logicalResourceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef]

### resourceType
- **Type**: typing.Optional[str]


# ResourceMappingTypeDef

### mappingType
- **Type**: typing.Literal['AppRegistryApp', 'CfnStack', 'EKS', 'Resource', 'ResourceGroup', 'Terraform']
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceIdTypeDef'>
- **Required**: Yes

### appRegistryAppName
- **Type**: typing.Optional[str]

### eksSourceName
- **Type**: typing.Optional[str]

### logicalStackName
- **Type**: typing.Optional[str]

### resourceGroupName
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### terraformSourceName
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


# S3LocationTypeDef

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ScoringComponentResiliencyScoreTypeDef

### excludedCount
- **Type**: typing.Optional[int]

### outstandingCount
- **Type**: typing.Optional[int]

### possibleScore
- **Type**: typing.Optional[float]

### score
- **Type**: typing.Optional[float]


# SopRecommendationTypeDef

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceType
- **Type**: typing.Literal['SSM']
- **Required**: Yes

### appComponentName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationItemTypeDef]]

### name
- **Type**: typing.Optional[str]

### prerequisite
- **Type**: typing.Optional[str]

### recommendationStatus
- **Type**: typing.Optional[typing.Literal['Excluded', 'Implemented', 'Inactive', 'NotImplemented']]


# SortTypeDef

### field
- **Type**: <class 'str'>
- **Required**: Yes

### ascending
- **Type**: typing.Optional[bool]


# StartAppAssessmentRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartAppAssessmentResponseTypeDef

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppAssessmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMetricsExportRequestTypeDef

### bucketName
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# StartMetricsExportResponseTypeDef

### metricsExportId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartResourceGroupingRecommendationTaskRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartResourceGroupingRecommendationTaskResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### groupingId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TerraformSourceTypeDef

### s3StateFileUrl
- **Type**: <class 'str'>
- **Required**: Yes


# TestRecommendationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnsupportedResourceTypeDef

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceIdTypeDef'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### unsupportedResourceStatus
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentSchedule
- **Type**: typing.Optional[typing.Literal['Daily', 'Disabled']]

### clearResiliencyPolicyArn
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### eventSubscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.EventSubscriptionTypeDef]]

### permissionModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PermissionModelUnionTypeDef]

### policyArn
- **Type**: typing.Optional[str]


# UpdateAppResponseTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppVersionAppComponentResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppComponentTypeDef'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppVersionRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# UpdateAppVersionResourceRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### appComponents
- **Type**: typing.Optional[typing.Sequence[str]]

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### excluded
- **Type**: typing.Optional[bool]

### logicalResourceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.LogicalResourceIdTypeDef]

### physicalResourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]


# UpdateAppVersionResourceResponseTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppVersionResponseTypeDef

### additionalInfo
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecommendationStatusItemTypeDef

### resourceId
- **Type**: typing.Optional[str]

### targetAccountId
- **Type**: typing.Optional[str]

### targetRegion
- **Type**: typing.Optional[str]


# UpdateRecommendationStatusRequestEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### excluded
- **Type**: <class 'bool'>
- **Required**: Yes

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentId
- **Type**: typing.Optional[str]

### excludeReason
- **Type**: typing.Optional[typing.Literal['AlreadyImplemented', 'ComplexityOfImplementation', 'NotRelevant']]

### item
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.UpdateRecommendationStatusItemTypeDef]


# UpdateResiliencyPolicyRequestTypeDef

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataLocationConstraint
- **Type**: typing.Optional[typing.Literal['AnyLocation', 'SameContinent', 'SameCountry']]

### policy
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub_classes.FailurePolicyTypeDef]]

### policyDescription
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]

### tier
- **Type**: typing.Optional[typing.Literal['CoreServices', 'Critical', 'Important', 'MissionCritical', 'NonCritical', 'NotApplicable']]


# UpdateResiliencyPolicyResponseTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


