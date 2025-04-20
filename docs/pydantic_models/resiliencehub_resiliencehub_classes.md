# Resiliencehub Resiliencehub Classes

# AcceptGroupingRecommendationEntry

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptResourceGroupingRecommendationsRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AcceptGroupingRecommendationEntry]
- **Required**: Yes


# AcceptResourceGroupingRecommendationsResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### failedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.FailedGroupingRecommendationEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# AddDraftAppVersionResourceMappingsRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResourceMapping]
- **Required**: Yes


# AddDraftAppVersionResourceMappingsResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### resourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResourceMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# Alarm

### alarmArn
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]


# AlarmRecommendation

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.RecommendationItem]]

### prerequisite
- **Type**: typing.Optional[str]

### recommendationStatus
- **Type**: typing.Optional[typing.Literal['Excluded', 'Implemented', 'Inactive', 'NotImplemented']]


# App

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EventSubscription]]

### lastAppComplianceEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### lastDriftEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### lastResiliencyScoreEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### permissionModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PermissionModelOutput]

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


# AppAssessment

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.DisruptionCompliance]]

### complianceStatus
- **Type**: typing.Optional[typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Cost]

### driftStatus
- **Type**: typing.Optional[typing.Literal['Detected', 'NotChecked', 'NotDetected']]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyPolicy]

### resiliencyScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyScore]

### resourceErrorsDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResourceErrorsDetails]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AssessmentSummary]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionName
- **Type**: typing.Optional[str]


# AppAssessmentSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Cost]

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


# AppComponent

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


# AppComponentCompliance

### appComponentName
- **Type**: typing.Optional[str]

### compliance
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.DisruptionCompliance]]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Cost]

### message
- **Type**: typing.Optional[str]

### resiliencyScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyScore]

### status
- **Type**: typing.Optional[typing.Literal['MissingPolicy', 'NotApplicable', 'PolicyBreached', 'PolicyMet']]


# AppInputSource

### importType
- **Type**: typing.Literal['AppRegistryApp', 'CfnStack', 'EKS', 'Resource', 'ResourceGroup', 'Terraform']
- **Required**: Yes

### eksSourceClusterNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EksSourceClusterNamespace]

### resourceCount
- **Type**: typing.Optional[int]

### sourceArn
- **Type**: typing.Optional[str]

### sourceName
- **Type**: typing.Optional[str]

### terraformSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.TerraformSource]


# AppSummary

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


# AppVersionSummary

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### identifier
- **Type**: typing.Optional[int]

### versionName
- **Type**: typing.Optional[str]


# AssessmentRiskRecommendation

### appComponents
- **Type**: typing.Optional[typing.List[str]]

### recommendation
- **Type**: typing.Optional[str]

### risk
- **Type**: typing.Optional[str]


# AssessmentSummary

### riskRecommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AssessmentRiskRecommendation]]

### summary
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateRecommendationStatusFailedEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# BatchUpdateRecommendationStatusRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### requestEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.UpdateRecommendationStatusRequestEntry]
- **Required**: Yes


# BatchUpdateRecommendationStatusResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### failedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.BatchUpdateRecommendationStatusFailedEntry]
- **Required**: Yes

### successfulEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.BatchUpdateRecommendationStatusSuccessfulEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateRecommendationStatusSuccessfulEntry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.UpdateRecommendationStatusItem]


# ComplianceDrift

### actualReferenceId
- **Type**: typing.Optional[str]

### actualValue
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.DisruptionCompliance]]

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.DisruptionCompliance]]


# ComponentRecommendation

### appComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### configRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ConfigRecommendation]
- **Required**: Yes

### recommendationStatus
- **Type**: typing.Literal['BreachedCanMeet', 'BreachedUnattainable', 'MetCanImprove', 'MissingPolicy']
- **Required**: Yes


# Condition

### field
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['Equals', 'GreaterOrEquals', 'GreaterThen', 'LessOrEquals', 'LessThen', 'NotEquals']
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# ConfigRecommendation

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.DisruptionCompliance]]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Cost]

### description
- **Type**: typing.Optional[str]

### haArchitecture
- **Type**: typing.Optional[typing.Literal['BackupAndRestore', 'MultiSite', 'NoRecoveryPlan', 'PilotLight', 'WarmStandby']]

### recommendationCompliance
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.RecommendationDisruptionCompliance]]

### suggestedChanges
- **Type**: typing.Optional[typing.List[str]]


# Cost

### amount
- **Type**: <class 'float'>
- **Required**: Yes

### currency
- **Type**: <class 'str'>
- **Required**: Yes

### frequency
- **Type**: typing.Literal['Daily', 'Hourly', 'Monthly', 'Yearly']
- **Required**: Yes


# CreateAppRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EventSubscription]]

### permissionModel
- **Type**: typing.Union[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PermissionModel, aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PermissionModelOutput, NoneType]

### policyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAppResponse

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.App'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppVersionAppComponentRequest

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### clientToken
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# CreateAppVersionAppComponentResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppComponent'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppVersionResourceRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponents
- **Type**: typing.List[str]
- **Required**: Yes

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# CreateAppVersionResourceResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecommendationTemplateRequest

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
- **Type**: typing.Optional[typing.List[str]]

### recommendationTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Alarm', 'Sop', 'Test']]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRecommendationTemplateResponse

### recommendationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.RecommendationTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResiliencyPolicyRequest

### policy
- **Type**: typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.FailurePolicy]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateResiliencyPolicyResponse

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppAssessmentRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAppAssessmentResponse

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentStatus
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppInputSourceRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### eksSourceClusterNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EksSourceClusterNamespace]

### sourceArn
- **Type**: typing.Optional[str]

### terraformSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.TerraformSource]


# DeleteAppInputSourceResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appInputSource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppInputSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteAppResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppVersionAppComponentRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAppVersionAppComponentResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppComponent'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppVersionResourceRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId]

### physicalResourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# DeleteAppVersionResourceResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRecommendationTemplateRequest

### recommendationTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteRecommendationTemplateResponse

### recommendationTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResiliencyPolicyRequest

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteResiliencyPolicyResponse

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppAssessmentRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppAssessmentResponse

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppAssessment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppResponse

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.App'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppVersionAppComponentRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppVersionAppComponentResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppComponent'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppVersionRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppVersionResourceRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId]

### physicalResourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# DescribeAppVersionResourceResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppVersionResourcesResolutionStatusRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### resolutionId
- **Type**: typing.Optional[str]


# DescribeAppVersionResourcesResolutionStatusResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppVersionTemplateRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppVersionTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDraftAppVersionResourcesImportStatusRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDraftAppVersionResourcesImportStatusResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### errorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ErrorDetail]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetricsExportRequest

### metricsExportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMetricsExportResponse

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### exportLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.S3Location'>
- **Required**: Yes

### metricsExportId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResiliencyPolicyRequest

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResiliencyPolicyResponse

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourceGroupingRecommendationTaskRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### groupingId
- **Type**: typing.Optional[str]


# DescribeResourceGroupingRecommendationTaskResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# DisruptionCompliance

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


# EksSource

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaces
- **Type**: typing.List[str]
- **Required**: Yes


# EksSourceClusterNamespace

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes


# EksSourceOutput

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaces
- **Type**: typing.List[str]
- **Required**: Yes


# ErrorDetail

### errorMessage
- **Type**: typing.Optional[str]


# EventSubscription

### eventType
- **Type**: typing.Literal['DriftDetected', 'ScheduledAssessmentFailure']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### snsTopicArn
- **Type**: typing.Optional[str]


# Experiment

### experimentArn
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]


# FailedGroupingRecommendationEntry

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# FailurePolicy

### rpoInSecs
- **Type**: <class 'int'>
- **Required**: Yes

### rtoInSecs
- **Type**: <class 'int'>
- **Required**: Yes


# Field

### name
- **Type**: <class 'str'>
- **Required**: Yes

### aggregation
- **Type**: typing.Optional[typing.Literal['Avg', 'Count', 'Max', 'Min', 'Sum']]


# GroupingAppComponent

### appComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentType
- **Type**: <class 'str'>
- **Required**: Yes


# GroupingRecommendation

### confidenceLevel
- **Type**: typing.Literal['High', 'Medium']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### groupingAppComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.GroupingAppComponent'>
- **Required**: Yes

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationReasons
- **Type**: typing.List[str]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.GroupingResource]
- **Required**: Yes

### score
- **Type**: <class 'float'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Accepted', 'PendingDecision', 'Rejected']
- **Required**: Yes

### rejectionReason
- **Type**: typing.Optional[typing.Literal['DistinctBusinessPurpose', 'DistinctUserGroupHandling', 'Other', 'SeparateDataConcern']]


# GroupingResource

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResourceId'>
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


# ImportResourcesToDraftAppVersionRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### eksSources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EksSource, aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EksSourceOutput]]]

### importStrategy
- **Type**: typing.Optional[typing.Literal['AddOnly', 'ReplaceAll']]

### sourceArns
- **Type**: typing.Optional[typing.List[str]]

### terraformSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.TerraformSource]]


# ImportResourcesToDraftAppVersionResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### eksSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EksSourceOutput]
- **Required**: Yes

### sourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### terraformSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.TerraformSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# ListAlarmRecommendationsRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAlarmRecommendationsResponse

### alarmRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AlarmRecommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentComplianceDriftsRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentComplianceDriftsResponse

### complianceDrifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ComplianceDrift]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentResourceDriftsRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentResourceDriftsRequestPaginate

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PaginatorConfig]


# ListAppAssessmentResourceDriftsResponse

### resourceDrifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResourceDrift]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppAssessmentsRequest

### appArn
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### assessmentStatus
- **Type**: typing.Optional[typing.List[typing.Literal['Failed', 'InProgress', 'Pending', 'Success']]]

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


# ListAppAssessmentsResponse

### assessmentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppAssessmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentCompliancesRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentCompliancesResponse

### componentCompliances
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppComponentCompliance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentRecommendationsRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppComponentRecommendationsResponse

### componentRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ComponentRecommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppInputSourcesRequest

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


# ListAppInputSourcesResponse

### appInputSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppInputSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionAppComponentsRequest

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


# ListAppVersionAppComponentsResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppComponent]
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionResourceMappingsRequest

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


# ListAppVersionResourceMappingsResponse

### resourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResourceMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionResourcesRequest

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


# ListAppVersionResourcesResponse

### physicalResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResource]
- **Required**: Yes

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppVersionsRequest

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


# ListAppVersionsResponse

### appVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppsRequest

### appArn
- **Type**: typing.Optional[str]

### awsApplicationArn
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


# ListAppsResponse

### appSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetricsRequest

### conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Condition]]

### dataSource
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Field]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Sort]]


# ListMetricsRequestPaginate

### conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Condition]]

### dataSource
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Field]]

### sorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Sort]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PaginatorConfig]


# ListMetricsResponse

### rows
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationTemplatesRequest

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
- **Type**: typing.Optional[typing.List[typing.Literal['Failed', 'InProgress', 'Pending', 'Success']]]


# ListRecommendationTemplatesResponse

### recommendationTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.RecommendationTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResiliencyPoliciesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]


# ListResiliencyPoliciesResponse

### resiliencyPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGroupingRecommendationsRequest

### appArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGroupingRecommendationsRequestPaginate

### appArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PaginatorConfig]


# ListResourceGroupingRecommendationsResponse

### groupingRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.GroupingRecommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSopRecommendationsRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSopRecommendationsResponse

### sopRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.SopRecommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuggestedResiliencyPoliciesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSuggestedResiliencyPoliciesResponse

### resiliencyPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# ListTestRecommendationsRequest

### assessmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestRecommendationsResponse

### testRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.TestRecommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUnsupportedAppVersionResourcesRequest

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


# ListUnsupportedAppVersionResourcesResponse

### resolutionId
- **Type**: <class 'str'>
- **Required**: Yes

### unsupportedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.UnsupportedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogicalResourceId

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionModel

### type
- **Type**: typing.Literal['LegacyIAMUser', 'RoleBased']
- **Required**: Yes

### crossAccountRoleArns
- **Type**: typing.Optional[typing.List[str]]

### invokerRoleName
- **Type**: typing.Optional[str]


# PermissionModelOutput

### type
- **Type**: typing.Literal['LegacyIAMUser', 'RoleBased']
- **Required**: Yes

### crossAccountRoleArns
- **Type**: typing.Optional[typing.List[str]]

### invokerRoleName
- **Type**: typing.Optional[str]


# PhysicalResource

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResourceId'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### appComponents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppComponent]]

### excluded
- **Type**: typing.Optional[bool]

### parentResourceName
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### sourceType
- **Type**: typing.Optional[typing.Literal['AppTemplate', 'Discovered']]


# PhysicalResourceId

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


# PublishAppVersionRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: typing.Optional[str]


# PublishAppVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# PutDraftAppVersionTemplateRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appTemplateBody
- **Type**: <class 'str'>
- **Required**: Yes


# PutDraftAppVersionTemplateResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# RecommendationDisruptionCompliance

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


# RecommendationItem

### alreadyImplemented
- **Type**: typing.Optional[bool]

### discoveredAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Alarm]

### excludeReason
- **Type**: typing.Optional[typing.Literal['AlreadyImplemented', 'ComplexityOfImplementation', 'NotRelevant']]

### excluded
- **Type**: typing.Optional[bool]

### latestDiscoveredExperiment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.Experiment]

### resourceId
- **Type**: typing.Optional[str]

### targetAccountId
- **Type**: typing.Optional[str]

### targetRegion
- **Type**: typing.Optional[str]


# RecommendationTemplate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.S3Location]


# RejectGroupingRecommendationEntry

### groupingRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### rejectionReason
- **Type**: typing.Optional[typing.Literal['DistinctBusinessPurpose', 'DistinctUserGroupHandling', 'Other', 'SeparateDataConcern']]


# RejectResourceGroupingRecommendationsRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.RejectGroupingRecommendationEntry]
- **Required**: Yes


# RejectResourceGroupingRecommendationsResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### failedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.FailedGroupingRecommendationEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveDraftAppVersionResourceMappingsRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appRegistryAppNames
- **Type**: typing.Optional[typing.List[str]]

### eksSourceNames
- **Type**: typing.Optional[typing.List[str]]

### logicalStackNames
- **Type**: typing.Optional[typing.List[str]]

### resourceGroupNames
- **Type**: typing.Optional[typing.List[str]]

### resourceNames
- **Type**: typing.Optional[typing.List[str]]

### terraformSourceNames
- **Type**: typing.Optional[typing.List[str]]


# RemoveDraftAppVersionResourceMappingsResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# ResiliencyPolicy

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### dataLocationConstraint
- **Type**: typing.Optional[typing.Literal['AnyLocation', 'SameContinent', 'SameCountry']]

### estimatedCostTier
- **Type**: typing.Optional[typing.Literal['L1', 'L2', 'L3', 'L4']]

### policy
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.FailurePolicy]]

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


# ResiliencyScore

### disruptionScore
- **Type**: typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], float]
- **Required**: Yes

### score
- **Type**: <class 'float'>
- **Required**: Yes

### componentScore
- **Type**: typing.Optional[typing.Dict[typing.Literal['Alarm', 'Compliance', 'Sop', 'Test'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ScoringComponentResiliencyScore]]


# ResolveAppVersionResourcesRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ResolveAppVersionResourcesResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceDrift

### appArn
- **Type**: typing.Optional[str]

### appVersion
- **Type**: typing.Optional[str]

### diffType
- **Type**: typing.Optional[typing.Literal['Added', 'NotEqual', 'Removed']]

### referenceId
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResourceIdentifier]


# ResourceError

### logicalResourceId
- **Type**: typing.Optional[str]

### physicalResourceId
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# ResourceErrorsDetails

### hasMoreErrors
- **Type**: typing.Optional[bool]

### resourceErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResourceError]]


# ResourceIdentifier

### logicalResourceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId]

### resourceType
- **Type**: typing.Optional[str]


# ResourceMapping

### mappingType
- **Type**: typing.Literal['AppRegistryApp', 'CfnStack', 'EKS', 'Resource', 'ResourceGroup', 'Terraform']
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResourceId'>
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


# S3Location

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ScoringComponentResiliencyScore

### excludedCount
- **Type**: typing.Optional[int]

### outstandingCount
- **Type**: typing.Optional[int]

### possibleScore
- **Type**: typing.Optional[float]

### score
- **Type**: typing.Optional[float]


# SopRecommendation

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.RecommendationItem]]

### name
- **Type**: typing.Optional[str]

### prerequisite
- **Type**: typing.Optional[str]

### recommendationStatus
- **Type**: typing.Optional[typing.Literal['Excluded', 'Implemented', 'Inactive', 'NotImplemented']]


# Sort

### field
- **Type**: <class 'str'>
- **Required**: Yes

### ascending
- **Type**: typing.Optional[bool]


# StartAppAssessmentRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartAppAssessmentResponse

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppAssessment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# StartMetricsExportRequest

### bucketName
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# StartMetricsExportResponse

### metricsExportId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# StartResourceGroupingRecommendationTaskRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartResourceGroupingRecommendationTaskResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TerraformSource

### s3StateFileUrl
- **Type**: <class 'str'>
- **Required**: Yes


# TestRecommendation

### referenceId
- **Type**: <class 'str'>
- **Required**: Yes

### appComponentId
- **Type**: typing.Optional[str]

### appComponentName
- **Type**: typing.Optional[str]

### dependsOnAlarms
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### intent
- **Type**: typing.Optional[str]

### items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.RecommendationItem]]

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


# UnsupportedResource

### logicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId'>
- **Required**: Yes

### physicalResourceId
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResourceId'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### unsupportedResourceStatus
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAppRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.EventSubscription]]

### permissionModel
- **Type**: typing.Union[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PermissionModel, aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PermissionModelOutput, NoneType]

### policyArn
- **Type**: typing.Optional[str]


# UpdateAppResponse

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.App'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAppVersionAppComponentRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# UpdateAppVersionAppComponentResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.AppComponent'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAppVersionRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# UpdateAppVersionResourceRequest

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### appComponents
- **Type**: typing.Optional[typing.List[str]]

### awsAccountId
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### excluded
- **Type**: typing.Optional[bool]

### logicalResourceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.LogicalResourceId]

### physicalResourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]


# UpdateAppVersionResourceResponse

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'str'>
- **Required**: Yes

### physicalResource
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.PhysicalResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAppVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecommendationStatusItem

### resourceId
- **Type**: typing.Optional[str]

### targetAccountId
- **Type**: typing.Optional[str]

### targetRegion
- **Type**: typing.Optional[str]


# UpdateRecommendationStatusRequestEntry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.UpdateRecommendationStatusItem]


# UpdateResiliencyPolicyRequest

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataLocationConstraint
- **Type**: typing.Optional[typing.Literal['AnyLocation', 'SameContinent', 'SameCountry']]

### policy
- **Type**: typing.Optional[typing.Dict[typing.Literal['AZ', 'Hardware', 'Region', 'Software'], aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.FailurePolicy]]

### policyDescription
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]

### tier
- **Type**: typing.Optional[typing.Literal['CoreServices', 'Critical', 'Important', 'MissionCritical', 'NonCritical', 'NotApplicable']]


# UpdateResiliencyPolicyResponse

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResiliencyPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_classes.ResponseMetadata'>
- **Required**: Yes


