# Pydantic Models in resiliencehub_classes

# AddDraftAppVersionResourceMappingsRequestRequestTypeDef

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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Canary', 'Composite', 'Event', 'Logs', 'Metric']
- **Required**: Yes

### appComponentName
- **Type**: typing.Optional[str]

### appComponentNames
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationItemTypeDef]]

### prerequisite
- **Type**: typing.Optional[str]

### recommendationStatus
- **Type**: typing.Optional[typing.Literal['Excluded', 'Implemented', 'Inactive', 'NotImplemented']]


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
- **Type**: typing.Optional[typing.Literal['PolicyBreached', 'PolicyMet']]

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
- **Type**: typing.Optional[typing.Literal['PolicyBreached', 'PolicyMet']]

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
- **Type**: typing.Optional[typing.Literal['PolicyBreached', 'PolicyMet']]


# AppComponentTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### id
- **Type**: typing.Optional[str]


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

### complianceStatus
- **Type**: typing.Optional[typing.Literal['ChangesDetected', 'NotAssessed', 'PolicyBreached', 'PolicyMet']]

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

### complianceStatus
- **Type**: typing.Optional[typing.Literal['ChangesDetected', 'NotAssessed', 'PolicyBreached', 'PolicyMet']]

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


# BatchUpdateRecommendationStatusRequestRequestTypeDef

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

### item
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.UpdateRecommendationStatusItemTypeDef'>
- **Required**: Yes

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeReason
- **Type**: typing.Optional[typing.Literal['AlreadyImplemented', 'ComplexityOfImplementation', 'NotRelevant']]


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
- **Type**: typing.Literal['BreachedCanMeet', 'BreachedUnattainable', 'MetCanImprove']
- **Required**: Yes


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


# CreateAppRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentSchedule
- **Type**: typing.Optional[typing.Literal['Daily', 'Disabled']]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### eventSubscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resiliencehub_classes.EventSubscriptionTypeDef]]

### permissionModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PermissionModelTypeDef]

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


# CreateAppVersionAppComponentRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### clientToken
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


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


# CreateAppVersionResourceRequestRequestTypeDef

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


# CreateRecommendationTemplateRequestRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### bucketName
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[typing.Literal['CfnJson', 'CfnYaml']]

### recommendationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### recommendationTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Alarm', 'Sop', 'Test']]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRecommendationTemplateResponseTypeDef

### recommendationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResiliencyPolicyRequestRequestTypeDef

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


# DeleteAppAssessmentRequestRequestTypeDef

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


# DeleteAppInputSourceRequestRequestTypeDef

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


# DeleteAppRequestRequestTypeDef

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


# DeleteAppVersionAppComponentRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


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


# DeleteAppVersionResourceRequestRequestTypeDef

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


# DeleteRecommendationTemplateRequestRequestTypeDef

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


# DeleteResiliencyPolicyRequestRequestTypeDef

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


# DescribeAppAssessmentRequestRequestTypeDef

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


# DescribeAppRequestRequestTypeDef

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


# DescribeAppVersionAppComponentRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
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


# DescribeAppVersionRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppVersionResourceRequestRequestTypeDef

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


# DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef

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


# DescribeAppVersionTemplateRequestRequestTypeDef

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


# DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef

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


# DescribeResiliencyPolicyRequestRequestTypeDef

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


# DisruptionComplianceTypeDef

### complianceStatus
- **Type**: typing.Literal['PolicyBreached', 'PolicyMet']
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


# EventSubscriptionTypeDef

### eventType
- **Type**: typing.Literal['DriftDetected', 'ScheduledAssessmentFailure']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### snsTopicArn
- **Type**: typing.Optional[str]


# FailurePolicyTypeDef

### rpoInSecs
- **Type**: <class 'int'>
- **Required**: Yes

### rtoInSecs
- **Type**: <class 'int'>
- **Required**: Yes


# ImportResourcesToDraftAppVersionRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### eksSources
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.resiliencehub_classes.EksSourceTypeDef, aws_resource_validator.pydantic_models.resiliencehub_classes.EksSourceOutputTypeDef]]]

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


# ListAlarmRecommendationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppAssessmentComplianceDriftsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppAssessmentResourceDriftsRequestListAppAssessmentResourceDriftsPaginateTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PaginatorConfigTypeDef]


# ListAppAssessmentResourceDriftsRequestRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentResourceDriftsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resourceDrifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceDriftTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppAssessmentsRequestRequestTypeDef

### appArn
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### assessmentStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Failed', 'InProgress', 'Pending', 'Success']]]

### complianceStatus
- **Type**: typing.Optional[typing.Literal['PolicyBreached', 'PolicyMet']]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppComponentCompliancesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppComponentRecommendationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppInputSourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppVersionAppComponentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppVersionResourceMappingsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResourceMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppVersionResourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.PhysicalResourceTypeDef]
- **Required**: Yes

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppVersionsRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListAppVersionsResponseTypeDef

### appVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppVersionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppsRequestRequestTypeDef

### appArn
- **Type**: typing.Optional[str]

### fromLastAssessmentTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]

### toLastAssessmentTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListAppsResponseTypeDef

### appSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.AppSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationTemplatesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResiliencyPoliciesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]


# ListResiliencyPoliciesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resiliencyPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSopRecommendationsRequestRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSopRecommendationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sopRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.SopRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSuggestedResiliencyPoliciesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSuggestedResiliencyPoliciesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resiliencyPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.ResiliencyPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestRecommendationsRequestRequestTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestRecommendationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### testRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.TestRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUnsupportedAppVersionResourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### unsupportedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.UnsupportedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### type
- **Type**: typing.Literal['LegacyIAMUser', 'RoleBased']
- **Required**: Yes

### crossAccountRoleArns
- **Type**: typing.Optional[typing.List[str]]

### invokerRoleName
- **Type**: typing.Optional[str]


# PermissionModelTypeDef

### type
- **Type**: typing.Literal['LegacyIAMUser', 'RoleBased']
- **Required**: Yes

### crossAccountRoleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### invokerRoleName
- **Type**: typing.Optional[str]


# PhysicalResourceIdTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Arn', 'Native']
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]


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


# PublishAppVersionRequestRequestTypeDef

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


# PutDraftAppVersionTemplateRequestRequestTypeDef

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
- **Type**: typing.Literal['PolicyBreached', 'PolicyMet']
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

### excludeReason
- **Type**: typing.Optional[typing.Literal['AlreadyImplemented', 'ComplexityOfImplementation', 'NotRelevant']]

### excluded
- **Type**: typing.Optional[bool]

### resourceId
- **Type**: typing.Optional[str]

### targetAccountId
- **Type**: typing.Optional[str]

### targetRegion
- **Type**: typing.Optional[str]


# RecommendationTemplateTypeDef

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['CfnJson', 'CfnYaml']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationTypes
- **Type**: typing.List[typing.Literal['Alarm', 'Sop', 'Test']]
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]

### needsReplacements
- **Type**: typing.Optional[bool]

### recommendationIds
- **Type**: typing.Optional[typing.List[str]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### templatesLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.S3LocationTypeDef]


# RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef

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


# ResolveAppVersionResourcesRequestRequestTypeDef

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


# StartAppAssessmentRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentName
- **Type**: typing.Optional[str]

### dependsOnAlarms
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### intent
- **Type**: typing.Optional[str]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub_classes.RecommendationItemTypeDef]]

### name
- **Type**: typing.Optional[str]

### prerequisite
- **Type**: typing.Optional[str]

### recommendationId
- **Type**: typing.Optional[str]

### recommendationStatus
- **Type**: typing.Optional[typing.Literal['Excluded', 'Implemented', 'Inactive', 'NotImplemented']]

### risk
- **Type**: typing.Optional[typing.Literal['High', 'Medium', 'Small']]

### type
- **Type**: typing.Optional[typing.Literal['AZ', 'Hardware', 'Region', 'Software']]


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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub_classes.PermissionModelTypeDef]

### policyArn
- **Type**: typing.Optional[str]


# UpdateAppResponseTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppVersionAppComponentRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


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


# UpdateAppVersionRequestRequestTypeDef

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# UpdateAppVersionResourceRequestRequestTypeDef

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

### item
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub_classes.UpdateRecommendationStatusItemTypeDef'>
- **Required**: Yes

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeReason
- **Type**: typing.Optional[typing.Literal['AlreadyImplemented', 'ComplexityOfImplementation', 'NotRelevant']]


# UpdateResiliencyPolicyRequestRequestTypeDef

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


