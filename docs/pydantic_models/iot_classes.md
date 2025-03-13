# Iot Classes

# AbortConfigOutputTypeDef

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AbortCriteriaTypeDef]
- **Required**: Yes


# AbortConfigTypeDef

### criteriaList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.AbortCriteriaTypeDef]
- **Required**: Yes


# AbortConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AbortCriteriaTypeDef

### failureType
- **Type**: typing.Literal['ALL', 'FAILED', 'REJECTED', 'TIMED_OUT']
- **Required**: Yes

### action
- **Type**: typing.Literal['CANCEL']
- **Required**: Yes

### thresholdPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### minNumberOfExecutedThings
- **Type**: <class 'int'>
- **Required**: Yes


# AcceptCertificateTransferRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### setAsActive
- **Type**: typing.Optional[bool]


# ActionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActiveViolationTypeDef

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorOutputTypeDef]

### lastViolationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueOutputTypeDef]

### violationEventAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ViolationEventAdditionalInfoTypeDef]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### verificationStateDescription
- **Type**: typing.Optional[str]

### lastViolationTime
- **Type**: typing.Optional[datetime.datetime]

### violationStartTime
- **Type**: typing.Optional[datetime.datetime]


# AddThingToBillingGroupRequestTypeDef

### billingGroupName
- **Type**: typing.Optional[str]

### billingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# AddThingToThingGroupRequestTypeDef

### thingGroupName
- **Type**: typing.Optional[str]

### thingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# AddThingsToThingGroupParamsOutputTypeDef

### thingGroupNames
- **Type**: typing.List[str]
- **Required**: Yes

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# AddThingsToThingGroupParamsTypeDef

### thingGroupNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# AggregationTypeOutputTypeDef

### name
- **Type**: typing.Literal['Cardinality', 'Percentiles', 'Statistics']
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.List[str]]


# AggregationTypeTypeDef

### name
- **Type**: typing.Literal['Cardinality', 'Percentiles', 'Statistics']
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# AggregationTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlertTargetTypeDef

### alertTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AllowedTypeDef

### policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.PolicyTypeDef]]


# AssetPropertyTimestampTypeDef

### timeInSeconds
- **Type**: <class 'str'>
- **Required**: Yes

### offsetInNanos
- **Type**: typing.Optional[str]


# AssetPropertyValueTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AssetPropertyVariantTypeDef'>
- **Required**: Yes

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AssetPropertyTimestampTypeDef'>
- **Required**: Yes

### quality
- **Type**: typing.Optional[str]


# AssetPropertyVariantTypeDef

### stringValue
- **Type**: typing.Optional[str]

### integerValue
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[str]

### booleanValue
- **Type**: typing.Optional[str]


# AssociateSbomWithPackageVersionRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### sbom
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.SbomTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AssociateSbomWithPackageVersionResponseTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### sbom
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.SbomTypeDef'>
- **Required**: Yes

### sbomValidationStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateTargetsWithJobRequestTypeDef

### targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: typing.Optional[str]

### namespaceId
- **Type**: typing.Optional[str]


# AssociateTargetsWithJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachPolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# AttachPrincipalPolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# AttachSecurityProfileRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachThingPrincipalRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# AttributePayloadOutputTypeDef

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### merge
- **Type**: typing.Optional[bool]


# AttributePayloadTypeDef

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### merge
- **Type**: typing.Optional[bool]


# AttributePayloadUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuditCheckConfigurationOutputTypeDef

### enabled
- **Type**: typing.Optional[bool]

### configuration
- **Type**: typing.Optional[typing.Dict[typing.Literal['CERT_AGE_THRESHOLD_IN_DAYS', 'CERT_EXPIRATION_THRESHOLD_IN_DAYS'], str]]


# AuditCheckConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]

### configuration
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CERT_AGE_THRESHOLD_IN_DAYS', 'CERT_EXPIRATION_THRESHOLD_IN_DAYS'], str]]


# AuditCheckConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuditCheckDetailsTypeDef

### checkRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED_COMPLIANT', 'COMPLETED_NON_COMPLIANT', 'FAILED', 'IN_PROGRESS', 'WAITING_FOR_DATA_COLLECTION']]

### checkCompliant
- **Type**: typing.Optional[bool]

### totalResourcesCount
- **Type**: typing.Optional[int]

### nonCompliantResourcesCount
- **Type**: typing.Optional[int]

### suppressedNonCompliantResourcesCount
- **Type**: typing.Optional[int]

### errorCode
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# AuditFindingTypeDef

### findingId
- **Type**: typing.Optional[str]

### taskId
- **Type**: typing.Optional[str]

### checkName
- **Type**: typing.Optional[str]

### taskStartTime
- **Type**: typing.Optional[datetime.datetime]

### findingTime
- **Type**: typing.Optional[datetime.datetime]

### severity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM']]

### nonCompliantResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.NonCompliantResourceTypeDef]

### relatedResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.RelatedResourceTypeDef]]

### reasonForNonCompliance
- **Type**: typing.Optional[str]

### reasonForNonComplianceCode
- **Type**: typing.Optional[str]

### isSuppressed
- **Type**: typing.Optional[bool]


# AuditMitigationActionExecutionMetadataTypeDef

### taskId
- **Type**: typing.Optional[str]

### findingId
- **Type**: typing.Optional[str]

### actionName
- **Type**: typing.Optional[str]

### actionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### errorCode
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# AuditMitigationActionsTaskMetadataTypeDef

### taskId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]


# AuditMitigationActionsTaskTargetOutputTypeDef

### auditTaskId
- **Type**: typing.Optional[str]

### findingIds
- **Type**: typing.Optional[typing.List[str]]

### auditCheckToReasonCodeFilter
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# AuditMitigationActionsTaskTargetTypeDef

### auditTaskId
- **Type**: typing.Optional[str]

### findingIds
- **Type**: typing.Optional[typing.Sequence[str]]

### auditCheckToReasonCodeFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# AuditMitigationActionsTaskTargetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuditNotificationTargetTypeDef

### targetArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]


# AuditSuppressionTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes

### expirationDate
- **Type**: typing.Optional[datetime.datetime]

### suppressIndefinitely
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# AuditTaskMetadataTypeDef

### taskId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### taskType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_AUDIT_TASK', 'SCHEDULED_AUDIT_TASK']]


# AuthInfoOutputTypeDef

### resources
- **Type**: typing.List[str]
- **Required**: Yes

### actionType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'PUBLISH', 'RECEIVE', 'SUBSCRIBE']]


# AuthInfoTypeDef

### resources
- **Type**: typing.Sequence[str]
- **Required**: Yes

### actionType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'PUBLISH', 'RECEIVE', 'SUBSCRIBE']]


# AuthInfoUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthResultTypeDef

### authInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AuthInfoOutputTypeDef]

### allowed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AllowedTypeDef]

### denied
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DeniedTypeDef]

### authDecision
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'EXPLICIT_DENY', 'IMPLICIT_DENY']]

### missingContextValues
- **Type**: typing.Optional[typing.List[str]]


# AuthorizerConfigTypeDef

### defaultAuthorizerName
- **Type**: typing.Optional[str]

### allowAuthorizerOverride
- **Type**: typing.Optional[bool]


# AuthorizerDescriptionTypeDef

### authorizerName
- **Type**: typing.Optional[str]

### authorizerArn
- **Type**: typing.Optional[str]

### authorizerFunctionArn
- **Type**: typing.Optional[str]

### tokenKeyName
- **Type**: typing.Optional[str]

### tokenSigningPublicKeys
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### signingDisabled
- **Type**: typing.Optional[bool]

### enableCachingForHttp
- **Type**: typing.Optional[bool]


# AuthorizerSummaryTypeDef

### authorizerName
- **Type**: typing.Optional[str]

### authorizerArn
- **Type**: typing.Optional[str]


# AwsJobAbortConfigTypeDef

### abortCriteriaList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.AwsJobAbortCriteriaTypeDef]
- **Required**: Yes


# AwsJobAbortCriteriaTypeDef

### failureType
- **Type**: typing.Literal['ALL', 'FAILED', 'REJECTED', 'TIMED_OUT']
- **Required**: Yes

### action
- **Type**: typing.Literal['CANCEL']
- **Required**: Yes

### thresholdPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### minNumberOfExecutedThings
- **Type**: <class 'int'>
- **Required**: Yes


# AwsJobExecutionsRolloutConfigTypeDef

### maximumPerMinute
- **Type**: typing.Optional[int]

### exponentialRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AwsJobExponentialRolloutRateTypeDef]


# AwsJobExponentialRolloutRateTypeDef

### baseRatePerMinute
- **Type**: <class 'int'>
- **Required**: Yes

### incrementFactor
- **Type**: <class 'float'>
- **Required**: Yes

### rateIncreaseCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AwsJobRateIncreaseCriteriaTypeDef'>
- **Required**: Yes


# AwsJobPresignedUrlConfigTypeDef

### expiresInSec
- **Type**: typing.Optional[int]


# AwsJobRateIncreaseCriteriaTypeDef

### numberOfNotifiedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]


# AwsJobTimeoutConfigTypeDef

### inProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BehaviorCriteriaOutputTypeDef

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['greater-than', 'greater-than-equals', 'in-cidr-set', 'in-port-set', 'in-set', 'less-than', 'less-than-equals', 'not-in-cidr-set', 'not-in-port-set', 'not-in-set']]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueOutputTypeDef]

### durationSeconds
- **Type**: typing.Optional[int]

### consecutiveDatapointsToAlarm
- **Type**: typing.Optional[int]

### consecutiveDatapointsToClear
- **Type**: typing.Optional[int]

### statisticalThreshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.StatisticalThresholdTypeDef]

### mlDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MachineLearningDetectionConfigTypeDef]


# BehaviorCriteriaTypeDef

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['greater-than', 'greater-than-equals', 'in-cidr-set', 'in-port-set', 'in-set', 'less-than', 'less-than-equals', 'not-in-cidr-set', 'not-in-port-set', 'not-in-set']]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueUnionTypeDef]

### durationSeconds
- **Type**: typing.Optional[int]

### consecutiveDatapointsToAlarm
- **Type**: typing.Optional[int]

### consecutiveDatapointsToClear
- **Type**: typing.Optional[int]

### statisticalThreshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.StatisticalThresholdTypeDef]

### mlDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MachineLearningDetectionConfigTypeDef]


# BehaviorCriteriaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BehaviorModelTrainingSummaryTypeDef

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorName
- **Type**: typing.Optional[str]

### trainingDataCollectionStartDate
- **Type**: typing.Optional[datetime.datetime]

### modelStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'EXPIRED', 'PENDING_BUILD']]

### datapointsCollectionPercentage
- **Type**: typing.Optional[float]

### lastModelRefreshDate
- **Type**: typing.Optional[datetime.datetime]


# BehaviorOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### metric
- **Type**: typing.Optional[str]

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricDimensionTypeDef]

### criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorCriteriaOutputTypeDef]

### suppressAlerts
- **Type**: typing.Optional[bool]

### exportMetric
- **Type**: typing.Optional[bool]


# BehaviorTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### metric
- **Type**: typing.Optional[str]

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricDimensionTypeDef]

### criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorCriteriaUnionTypeDef]

### suppressAlerts
- **Type**: typing.Optional[bool]

### exportMetric
- **Type**: typing.Optional[bool]


# BehaviorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillingGroupMetadataTypeDef

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# BillingGroupPropertiesTypeDef

### billingGroupDescription
- **Type**: typing.Optional[str]


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BucketTypeDef

### keyValue
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]


# BucketsAggregationTypeTypeDef

### termsAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TermsAggregationTypeDef]


# CACertificateDescriptionTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### certificateId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### certificatePem
- **Type**: typing.Optional[str]

### ownedBy
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### autoRegistrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### customerVersion
- **Type**: typing.Optional[int]

### generationId
- **Type**: typing.Optional[str]

### validity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CertificateValidityTypeDef]

### certificateMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'SNI_ONLY']]


# CACertificateTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### certificateId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# CancelAuditMitigationActionsTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelAuditTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelCertificateTransferRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDetectMitigationActionsTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobExecutionRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]

### expectedVersion
- **Type**: typing.Optional[int]

### statusDetails
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CancelJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reasonCode
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# CancelJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CertificateDescriptionTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### certificateId
- **Type**: typing.Optional[str]

### caCertificateId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']]

### certificatePem
- **Type**: typing.Optional[str]

### ownedBy
- **Type**: typing.Optional[str]

### previousOwnedBy
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### customerVersion
- **Type**: typing.Optional[int]

### transferData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TransferDataTypeDef]

### generationId
- **Type**: typing.Optional[str]

### validity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CertificateValidityTypeDef]

### certificateMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'SNI_ONLY']]


# CertificateProviderSummaryTypeDef

### certificateProviderName
- **Type**: typing.Optional[str]

### certificateProviderArn
- **Type**: typing.Optional[str]


# CertificateTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### certificateId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']]

### certificateMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'SNI_ONLY']]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# CertificateValidityTypeDef

### notBefore
- **Type**: typing.Optional[datetime.datetime]

### notAfter
- **Type**: typing.Optional[datetime.datetime]


# ClientCertificateConfigTypeDef

### clientCertificateCallbackArn
- **Type**: typing.Optional[str]


# CloudwatchAlarmActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes

### stateReason
- **Type**: <class 'str'>
- **Required**: Yes

### stateValue
- **Type**: <class 'str'>
- **Required**: Yes


# CloudwatchLogsActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### batchMode
- **Type**: typing.Optional[bool]


# CloudwatchMetricActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### metricNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricValue
- **Type**: <class 'str'>
- **Required**: Yes

### metricUnit
- **Type**: <class 'str'>
- **Required**: Yes

### metricTimestamp
- **Type**: typing.Optional[str]


# CodeSigningCertificateChainTypeDef

### certificateName
- **Type**: typing.Optional[str]

### inlineDocument
- **Type**: typing.Optional[str]


# CodeSigningOutputTypeDef

### awsSignerJobId
- **Type**: typing.Optional[str]

### startSigningJobParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.StartSigningJobParameterTypeDef]

### customCodeSigning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CustomCodeSigningOutputTypeDef]


# CodeSigningSignatureOutputTypeDef

### inlineDocument
- **Type**: typing.Optional[bytes]


# CodeSigningSignatureTypeDef

### inlineDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BlobTypeDef]


# CodeSigningSignatureUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeSigningTypeDef

### awsSignerJobId
- **Type**: typing.Optional[str]

### startSigningJobParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.StartSigningJobParameterTypeDef]

### customCodeSigning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CustomCodeSigningUnionTypeDef]


# CodeSigningUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommandExecutionResultTypeDef

### S
- **Type**: typing.Optional[str]

### B
- **Type**: typing.Optional[bool]

### BIN
- **Type**: typing.Optional[bytes]


# CommandExecutionSummaryTypeDef

### commandArn
- **Type**: typing.Optional[str]

### executionId
- **Type**: typing.Optional[str]

### targetArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### completedAt
- **Type**: typing.Optional[datetime.datetime]


# CommandParameterOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CommandParameterValueOutputTypeDef]

### defaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CommandParameterValueOutputTypeDef]

### description
- **Type**: typing.Optional[str]


# CommandParameterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CommandParameterValueUnionTypeDef]

### defaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CommandParameterValueUnionTypeDef]

### description
- **Type**: typing.Optional[str]


# CommandParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommandParameterValueOutputTypeDef

### S
- **Type**: typing.Optional[str]

### B
- **Type**: typing.Optional[bool]

### I
- **Type**: typing.Optional[int]

### L
- **Type**: typing.Optional[int]

### D
- **Type**: typing.Optional[float]

### BIN
- **Type**: typing.Optional[bytes]

### UL
- **Type**: typing.Optional[str]


# CommandParameterValueTypeDef

### S
- **Type**: typing.Optional[str]

### B
- **Type**: typing.Optional[bool]

### I
- **Type**: typing.Optional[int]

### L
- **Type**: typing.Optional[int]

### D
- **Type**: typing.Optional[float]

### BIN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BlobTypeDef]

### UL
- **Type**: typing.Optional[str]


# CommandParameterValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommandPayloadOutputTypeDef

### content
- **Type**: typing.Optional[bytes]

### contentType
- **Type**: typing.Optional[str]


# CommandPayloadTypeDef

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BlobTypeDef]

### contentType
- **Type**: typing.Optional[str]


# CommandPayloadUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommandSummaryTypeDef

### commandArn
- **Type**: typing.Optional[str]

### commandId
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### deprecated
- **Type**: typing.Optional[bool]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### pendingDeletion
- **Type**: typing.Optional[bool]


# ConfigurationTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# ConfirmTopicRuleDestinationRequestTypeDef

### confirmationToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAuditSuppressionRequestTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### expirationDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### suppressIndefinitely
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# CreateAuthorizerRequestTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### tokenKeyName
- **Type**: typing.Optional[str]

### tokenSigningPublicKeys
- **Type**: typing.Optional[typing.Mapping[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### signingDisabled
- **Type**: typing.Optional[bool]

### enableCachingForHttp
- **Type**: typing.Optional[bool]


# CreateAuthorizerResponseTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBillingGroupRequestTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BillingGroupPropertiesTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateBillingGroupResponseTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCertificateFromCsrRequestTypeDef

### certificateSigningRequest
- **Type**: <class 'str'>
- **Required**: Yes

### setAsActive
- **Type**: typing.Optional[bool]


# CreateCertificateFromCsrResponseTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCertificateProviderRequestTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### lambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountDefaultForOperations
- **Type**: typing.Sequence[typing.Literal['CreateCertificateFromCsr']]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateCertificateProviderResponseTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCommandRequestTypeDef

### commandId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']]

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CommandPayloadUnionTypeDef]

### mandatoryParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.CommandParameterUnionTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateCommandResponseTypeDef

### commandId
- **Type**: <class 'str'>
- **Required**: Yes

### commandArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricType
- **Type**: typing.Literal['ip-address-list', 'number', 'number-list', 'string-list']
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateCustomMetricResponseTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDimensionResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainConfigurationRequestTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: typing.Optional[str]

### serverCertificateArns
- **Type**: typing.Optional[typing.Sequence[str]]

### validationCertificateArn
- **Type**: typing.Optional[str]

### authorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AuthorizerConfigTypeDef]

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### tlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TlsConfigTypeDef]

### serverCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ServerCertificateConfigTypeDef]

### authenticationType
- **Type**: typing.Optional[typing.Literal['AWS_SIGV4', 'AWS_X509', 'CUSTOM_AUTH', 'CUSTOM_AUTH_X509', 'DEFAULT']]

### applicationProtocol
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HTTPS', 'MQTT_WSS', 'SECURE_MQTT']]

### clientCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ClientCertificateConfigTypeDef]


# CreateDomainConfigurationResponseTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### domainConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDynamicThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesUnionTypeDef]

### indexName
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateDynamicThingGroupResponseTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationType
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AggregationTypeUnionTypeDef'>
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### aggregationField
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]

### indexName
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateFleetMetricResponseTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### documentSource
- **Type**: typing.Optional[str]

### document
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### presignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PresignedUrlConfigTypeDef]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRolloutConfigTypeDef]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigUnionTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### namespaceId
- **Type**: typing.Optional[str]

### jobTemplateArn
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigUnionTypeDef]

### documentParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### schedulingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SchedulingConfigUnionTypeDef]

### destinationPackageVersions
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobTemplateRequestTypeDef

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: typing.Optional[str]

### documentSource
- **Type**: typing.Optional[str]

### document
- **Type**: typing.Optional[str]

### presignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PresignedUrlConfigTypeDef]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRolloutConfigTypeDef]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigUnionTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigUnionTypeDef]

### maintenanceWindows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.MaintenanceWindowTypeDef]]

### destinationPackageVersions
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateJobTemplateResponseTypeDef

### jobTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeysAndCertificateRequestTypeDef

### setAsActive
- **Type**: typing.Optional[bool]


# CreateKeysAndCertificateResponseTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.KeyPairTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMitigationActionRequestTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionParams
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsUnionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateMitigationActionResponseTypeDef

### actionArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOTAUpdateRequestTypeDef

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### files
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.OTAUpdateFileUnionTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HTTP', 'MQTT']]]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### awsJobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AwsJobExecutionsRolloutConfigTypeDef]

### awsJobPresignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AwsJobPresignedUrlConfigTypeDef]

### awsJobAbortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AwsJobAbortConfigTypeDef]

### awsJobTimeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AwsJobTimeoutConfigTypeDef]

### additionalParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateOTAUpdateResponseTypeDef

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes

### awsIotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### otaUpdateArn
- **Type**: <class 'str'>
- **Required**: Yes

### awsIotJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### otaUpdateStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackageRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreatePackageResponseTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### packageArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackageVersionRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### artifact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PackageVersionArtifactTypeDef]

### recipe
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreatePackageVersionResponseTypeDef

### packageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### status
- **Type**: typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']
- **Required**: Yes

### errorReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreatePolicyResponseTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyVersionRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### setAsDefault
- **Type**: typing.Optional[bool]


# CreatePolicyVersionResponseTypeDef

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### isDefaultVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProvisioningClaimRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateProvisioningClaimResponseTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.KeyPairTypeDef'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProvisioningTemplateResponseTypeDef

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### defaultVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProvisioningTemplateVersionRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### setAsDefault
- **Type**: typing.Optional[bool]


# CreateProvisioningTemplateVersionResponseTypeDef

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'int'>
- **Required**: Yes

### isDefaultVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoleAliasRequestTypeDef

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### credentialDurationSeconds
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateRoleAliasResponseTypeDef

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScheduledAuditRequestTypeDef

### frequency
- **Type**: typing.Literal['BIWEEKLY', 'DAILY', 'MONTHLY', 'WEEKLY']
- **Required**: Yes

### targetCheckNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes

### dayOfMonth
- **Type**: typing.Optional[str]

### dayOfWeek
- **Type**: typing.Optional[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateScheduledAuditResponseTypeDef

### scheduledAuditArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityProfileRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: typing.Optional[str]

### behaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.BehaviorUnionTypeDef]]

### alertTargets
- **Type**: typing.Optional[typing.Mapping[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot_classes.AlertTargetTypeDef]]

### additionalMetricsToRetain
- **Type**: typing.Optional[typing.Sequence[str]]

### additionalMetricsToRetainV2
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.MetricToRetainTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### metricsExportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricsExportConfigTypeDef]


# CreateSecurityProfileResponseTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamRequestTypeDef

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.StreamFileTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateStreamResponseTypeDef

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### streamArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### streamVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### parentGroupName
- **Type**: typing.Optional[str]

### thingGroupProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateThingGroupResponseTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateThingRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeName
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AttributePayloadUnionTypeDef]

### billingGroupName
- **Type**: typing.Optional[str]


# CreateThingResponseTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingArn
- **Type**: <class 'str'>
- **Required**: Yes

### thingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateThingTypeRequestTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


# CreateThingTypeResponseTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeArn
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTopicRuleDestinationRequestTypeDef

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRuleDestinationConfigurationTypeDef'>
- **Required**: Yes


# CreateTopicRuleDestinationResponseTypeDef

### topicRuleDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRuleDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTopicRuleRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### topicRulePayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRulePayloadTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[str]


# CustomCodeSigningOutputTypeDef

### signature
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningSignatureOutputTypeDef]

### certificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningCertificateChainTypeDef]

### hashAlgorithm
- **Type**: typing.Optional[str]

### signatureAlgorithm
- **Type**: typing.Optional[str]


# CustomCodeSigningTypeDef

### signature
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningSignatureUnionTypeDef]

### certificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningCertificateChainTypeDef]

### hashAlgorithm
- **Type**: typing.Optional[str]

### signatureAlgorithm
- **Type**: typing.Optional[str]


# CustomCodeSigningUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAccountAuditConfigurationRequestTypeDef

### deleteScheduledAudits
- **Type**: typing.Optional[bool]


# DeleteAuditSuppressionRequestTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes


# DeleteAuthorizerRequestTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBillingGroupRequestTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteCACertificateRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateProviderRequestTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteCommandExecutionRequestTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCommandRequestTypeDef

### commandId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCommandResponseTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDimensionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainConfigurationRequestTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDynamicThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteFleetMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteJobExecutionRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### executionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]

### namespaceId
- **Type**: typing.Optional[str]


# DeleteJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]

### namespaceId
- **Type**: typing.Optional[str]


# DeleteJobTemplateRequestTypeDef

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMitigationActionRequestTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOTAUpdateRequestTypeDef

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes

### deleteStream
- **Type**: typing.Optional[bool]

### forceDeleteAWSJob
- **Type**: typing.Optional[bool]


# DeletePackageRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePackageVersionRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyVersionRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisioningTemplateRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisioningTemplateVersionRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteRoleAliasRequestTypeDef

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledAuditRequestTypeDef

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSecurityProfileRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteStreamRequestTypeDef

### streamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteThingRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteThingTypeRequestTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRuleDestinationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRuleRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteV2LoggingLevelRequestTypeDef

### targetType
- **Type**: typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']
- **Required**: Yes

### targetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeniedTypeDef

### implicitDeny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ImplicitDenyTypeDef]

### explicitDeny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ExplicitDenyTypeDef]


# DeprecateThingTypeRequestTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### undoDeprecate
- **Type**: typing.Optional[bool]


# DescribeAccountAuditConfigurationResponseTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### auditNotificationTargetConfigurations
- **Type**: typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot_classes.AuditNotificationTargetTypeDef]
- **Required**: Yes

### auditCheckConfigurations
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot_classes.AuditCheckConfigurationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAuditFindingRequestTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditFindingResponseTypeDef

### finding
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuditFindingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAuditMitigationActionsTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditMitigationActionsTaskResponseTypeDef

### taskStatus
- **Type**: typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### taskStatistics
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot_classes.TaskStatisticsForAuditCheckTypeDef]
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuditMitigationActionsTaskTargetOutputTypeDef'>
- **Required**: Yes

### auditCheckToActionsMapping
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### actionsDefinition
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MitigationActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAuditSuppressionRequestTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes


# DescribeAuditSuppressionResponseTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes

### expirationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### suppressIndefinitely
- **Type**: <class 'bool'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAuditTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditTaskResponseTypeDef

### taskStatus
- **Type**: typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### taskType
- **Type**: typing.Literal['ON_DEMAND_AUDIT_TASK', 'SCHEDULED_AUDIT_TASK']
- **Required**: Yes

### taskStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### taskStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TaskStatisticsTypeDef'>
- **Required**: Yes

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes

### auditDetails
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot_classes.AuditCheckDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAuthorizerRequestTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuthorizerResponseTypeDef

### authorizerDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuthorizerDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBillingGroupRequestTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBillingGroupResponseTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### billingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.BillingGroupPropertiesTypeDef'>
- **Required**: Yes

### billingGroupMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.BillingGroupMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCACertificateRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCACertificateResponseTypeDef

### certificateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.CACertificateDescriptionTypeDef'>
- **Required**: Yes

### registrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.RegistrationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCertificateProviderRequestTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateProviderResponseTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### lambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountDefaultForOperations
- **Type**: typing.List[typing.Literal['CreateCertificateFromCsr']]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCertificateRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateResponseTypeDef

### certificateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.CertificateDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomMetricResponseTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricArn
- **Type**: <class 'str'>
- **Required**: Yes

### metricType
- **Type**: typing.Literal['ip-address-list', 'number', 'number-list', 'string-list']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDefaultAuthorizerResponseTypeDef

### authorizerDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuthorizerDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDetectMitigationActionsTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDetectMitigationActionsTaskResponseTypeDef

### taskSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDimensionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainConfigurationRequestTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainConfigurationResponseTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### domainConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### serverCertificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ServerCertificateSummaryTypeDef]
- **Required**: Yes

### authorizerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuthorizerConfigTypeDef'>
- **Required**: Yes

### domainConfigurationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### serviceType
- **Type**: typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']
- **Required**: Yes

### domainType
- **Type**: typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED', 'ENDPOINT']
- **Required**: Yes

### lastStatusChangeDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tlsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TlsConfigTypeDef'>
- **Required**: Yes

### serverCertificateConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ServerCertificateConfigTypeDef'>
- **Required**: Yes

### authenticationType
- **Type**: typing.Literal['AWS_SIGV4', 'AWS_X509', 'CUSTOM_AUTH', 'CUSTOM_AUTH_X509', 'DEFAULT']
- **Required**: Yes

### applicationProtocol
- **Type**: typing.Literal['DEFAULT', 'HTTPS', 'MQTT_WSS', 'SECURE_MQTT']
- **Required**: Yes

### clientCertificateConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ClientCertificateConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointRequestTypeDef

### endpointType
- **Type**: typing.Optional[str]


# DescribeEndpointResponseTypeDef

### endpointAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventConfigurationsResponseTypeDef

### eventConfigurations
- **Type**: typing.Dict[typing.Literal['CA_CERTIFICATE', 'CERTIFICATE', 'JOB', 'JOB_EXECUTION', 'POLICY', 'THING', 'THING_GROUP', 'THING_GROUP_HIERARCHY', 'THING_GROUP_MEMBERSHIP', 'THING_TYPE', 'THING_TYPE_ASSOCIATION'], aws_resource_validator.pydantic_models.iot_classes.ConfigurationTypeDef]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetMetricResponseTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationType
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AggregationTypeOutputTypeDef'>
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### aggregationField
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### queryVersion
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### metricArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIndexRequestTypeDef

### indexName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIndexResponseTypeDef

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### indexStatus
- **Type**: typing.Literal['ACTIVE', 'BUILDING', 'REBUILDING']
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.iot_classes.DescribeIndexResponseTypeDef'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobExecutionRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### executionNumber
- **Type**: typing.Optional[int]


# DescribeJobExecutionResponseTypeDef

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.JobExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeSubstitution
- **Type**: typing.Optional[bool]


# DescribeJobResponseTypeDef

### documentSource
- **Type**: <class 'str'>
- **Required**: Yes

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobTemplateRequestTypeDef

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobTemplateResponseTypeDef

### jobTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### documentSource
- **Type**: <class 'str'>
- **Required**: Yes

### document
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### presignedUrlConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.PresignedUrlConfigTypeDef'>
- **Required**: Yes

### jobExecutionsRolloutConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRolloutConfigTypeDef'>
- **Required**: Yes

### abortConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AbortConfigOutputTypeDef'>
- **Required**: Yes

### timeoutConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef'>
- **Required**: Yes

### jobExecutionsRetryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigOutputTypeDef'>
- **Required**: Yes

### maintenanceWindows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MaintenanceWindowTypeDef]
- **Required**: Yes

### destinationPackageVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeManagedJobTemplateRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateVersion
- **Type**: typing.Optional[str]


# DescribeManagedJobTemplateResponseTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### templateVersion
- **Type**: <class 'str'>
- **Required**: Yes

### environments
- **Type**: typing.List[str]
- **Required**: Yes

### documentParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.DocumentParameterTypeDef]
- **Required**: Yes

### document
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMitigationActionRequestTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMitigationActionResponseTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Literal['ADD_THINGS_TO_THING_GROUP', 'ENABLE_IOT_LOGGING', 'PUBLISH_FINDING_TO_SNS', 'REPLACE_DEFAULT_POLICY_VERSION', 'UPDATE_CA_CERTIFICATE', 'UPDATE_DEVICE_CERTIFICATE']
- **Required**: Yes

### actionArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionParams
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsOutputTypeDef'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProvisioningTemplateRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProvisioningTemplateVersionRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeProvisioningTemplateVersionResponseTypeDef

### versionId
- **Type**: <class 'int'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### isDefaultVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRoleAliasRequestTypeDef

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoleAliasResponseTypeDef

### roleAliasDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.RoleAliasDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeScheduledAuditRequestTypeDef

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduledAuditResponseTypeDef

### frequency
- **Type**: typing.Literal['BIWEEKLY', 'DAILY', 'MONTHLY', 'WEEKLY']
- **Required**: Yes

### dayOfMonth
- **Type**: <class 'str'>
- **Required**: Yes

### dayOfWeek
- **Type**: typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']
- **Required**: Yes

### targetCheckNames
- **Type**: typing.List[str]
- **Required**: Yes

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes

### scheduledAuditArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSecurityProfileRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityProfileResponseTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: <class 'str'>
- **Required**: Yes

### behaviors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.BehaviorOutputTypeDef]
- **Required**: Yes

### alertTargets
- **Type**: typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot_classes.AlertTargetTypeDef]
- **Required**: Yes

### additionalMetricsToRetain
- **Type**: typing.List[str]
- **Required**: Yes

### additionalMetricsToRetainV2
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MetricToRetainTypeDef]
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### metricsExportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.MetricsExportConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStreamRequestTypeDef

### streamId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStreamResponseTypeDef

### streamInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.StreamInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingGroupResponseTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### thingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesOutputTypeDef'>
- **Required**: Yes

### thingGroupMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupMetadataTypeDef'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryVersion
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'BUILDING', 'REBUILDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThingRegistrationTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingRegistrationTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### inputFileBucket
- **Type**: <class 'str'>
- **Required**: Yes

### inputFileKey
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Cancelled', 'Cancelling', 'Completed', 'Failed', 'InProgress']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### successCount
- **Type**: <class 'int'>
- **Required**: Yes

### failureCount
- **Type**: <class 'int'>
- **Required**: Yes

### percentageProgress
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThingRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingResponseTypeDef

### defaultClientId
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingId
- **Type**: <class 'str'>
- **Required**: Yes

### thingArn
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThingTypeRequestTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingTypeResponseTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeArn
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesOutputTypeDef'>
- **Required**: Yes

### thingTypeMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingTypeMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.S3DestinationTypeDef]


# DetachPolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# DetachPrincipalPolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# DetachSecurityProfileRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachThingPrincipalRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# DetectMitigationActionExecutionTypeDef

### taskId
- **Type**: typing.Optional[str]

### violationId
- **Type**: typing.Optional[str]

### actionName
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### executionStartDate
- **Type**: typing.Optional[datetime.datetime]

### executionEndDate
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SKIPPED', 'SUCCESSFUL']]

### errorCode
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# DetectMitigationActionsTaskStatisticsTypeDef

### actionsExecuted
- **Type**: typing.Optional[int]

### actionsSkipped
- **Type**: typing.Optional[int]

### actionsFailed
- **Type**: typing.Optional[int]


# DetectMitigationActionsTaskSummaryTypeDef

### taskId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']]

### taskStartTime
- **Type**: typing.Optional[datetime.datetime]

### taskEndTime
- **Type**: typing.Optional[datetime.datetime]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskTargetOutputTypeDef]

### violationEventOccurrenceRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ViolationEventOccurrenceRangeOutputTypeDef]

### onlyActiveViolationsIncluded
- **Type**: typing.Optional[bool]

### suppressedAlertsIncluded
- **Type**: typing.Optional[bool]

### actionsDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.MitigationActionTypeDef]]

### taskStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskStatisticsTypeDef]


# DetectMitigationActionsTaskTargetOutputTypeDef

### violationIds
- **Type**: typing.Optional[typing.List[str]]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorName
- **Type**: typing.Optional[str]


# DetectMitigationActionsTaskTargetTypeDef

### violationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorName
- **Type**: typing.Optional[str]


# DetectMitigationActionsTaskTargetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisableTopicRuleRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSbomFromPackageVersionRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DocumentParameterTypeDef

### key
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### regex
- **Type**: typing.Optional[str]

### example
- **Type**: typing.Optional[str]

### optional
- **Type**: typing.Optional[bool]


# DomainConfigurationSummaryTypeDef

### domainConfigurationName
- **Type**: typing.Optional[str]

### domainConfigurationArn
- **Type**: typing.Optional[str]

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]


# DynamoDBActionTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### hashKeyField
- **Type**: <class 'str'>
- **Required**: Yes

### hashKeyValue
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: typing.Optional[str]

### hashKeyType
- **Type**: typing.Optional[typing.Literal['NUMBER', 'STRING']]

### rangeKeyField
- **Type**: typing.Optional[str]

### rangeKeyValue
- **Type**: typing.Optional[str]

### rangeKeyType
- **Type**: typing.Optional[typing.Literal['NUMBER', 'STRING']]

### payloadField
- **Type**: typing.Optional[str]


# DynamoDBv2ActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### putItem
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.PutItemInputTypeDef'>
- **Required**: Yes


# EffectivePolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### policyArn
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableIoTLoggingParamsTypeDef

### roleArnForLogging
- **Type**: <class 'str'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# EnableTopicRuleRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorInfoTypeDef

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ExplicitDenyTypeDef

### policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.PolicyTypeDef]]


# ExponentialRolloutRateTypeDef

### baseRatePerMinute
- **Type**: <class 'int'>
- **Required**: Yes

### incrementFactor
- **Type**: <class 'float'>
- **Required**: Yes

### rateIncreaseCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.RateIncreaseCriteriaTypeDef'>
- **Required**: Yes


# FieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileLocationTypeDef

### stream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.StreamTypeDef]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.S3LocationTypeDef]


# FirehoseActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### separator
- **Type**: typing.Optional[str]

### batchMode
- **Type**: typing.Optional[bool]


# FleetMetricNameAndArnTypeDef

### metricName
- **Type**: typing.Optional[str]

### metricArn
- **Type**: typing.Optional[str]


# GeoLocationTargetTypeDef

### name
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[typing.Literal['LatLon', 'LonLat']]


# GetBehaviorModelTrainingSummariesRequestPaginateTypeDef

### securityProfileName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# GetBehaviorModelTrainingSummariesRequestTypeDef

### securityProfileName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetBehaviorModelTrainingSummariesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.BehaviorModelTrainingSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBucketsAggregationRequestTypeDef

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationField
- **Type**: <class 'str'>
- **Required**: Yes

### bucketsAggregationType
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.BucketsAggregationTypeTypeDef'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# GetBucketsAggregationResponseTypeDef

### totalCount
- **Type**: <class 'int'>
- **Required**: Yes

### buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.BucketTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCardinalityRequestTypeDef

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### aggregationField
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# GetCardinalityResponseTypeDef

### cardinality
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCommandExecutionRequestTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### includeResult
- **Type**: typing.Optional[bool]


# GetCommandExecutionResponseTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### commandArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### statusReason
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.StatusReasonTypeDef'>
- **Required**: Yes

### result
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot_classes.CommandExecutionResultTypeDef]
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot_classes.CommandParameterValueOutputTypeDef]
- **Required**: Yes

### executionTimeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCommandRequestTypeDef

### commandId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommandResponseTypeDef

### commandId
- **Type**: <class 'str'>
- **Required**: Yes

### commandArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### mandatoryParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CommandParameterOutputTypeDef]
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.CommandPayloadOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deprecated
- **Type**: <class 'bool'>
- **Required**: Yes

### pendingDeletion
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEffectivePoliciesRequestTypeDef

### principal
- **Type**: typing.Optional[str]

### cognitoIdentityPoolId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]


# GetEffectivePoliciesResponseTypeDef

### effectivePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.EffectivePolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIndexingConfigurationResponseTypeDef

### thingIndexingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingIndexingConfigurationOutputTypeDef'>
- **Required**: Yes

### thingGroupIndexingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupIndexingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobDocumentRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeSubstitution
- **Type**: typing.Optional[bool]


# GetJobDocumentResponseTypeDef

### document
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoggingOptionsResponseTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOTAUpdateRequestTypeDef

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOTAUpdateResponseTypeDef

### otaUpdateInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.OTAUpdateInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPackageConfigurationResponseTypeDef

### versionUpdateByJobsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.VersionUpdateByJobsConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPackageRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPackageResponseTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### packageArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### defaultVersionName
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPackageVersionRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPackageVersionResponseTypeDef

### packageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### artifact
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.PackageVersionArtifactTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']
- **Required**: Yes

### errorReason
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sbom
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.SbomTypeDef'>
- **Required**: Yes

### sbomValidationStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### recipe
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPercentilesRequestTypeDef

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### aggregationField
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]

### percents
- **Type**: typing.Optional[typing.Sequence[float]]


# GetPercentilesResponseTypeDef

### percentiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PercentPairTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponseTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### defaultVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### generationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyVersionRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyVersionResponseTypeDef

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### isDefaultVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### generationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegistrationCodeResponseTypeDef

### registrationCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStatisticsRequestTypeDef

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### aggregationField
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# GetStatisticsResponseTypeDef

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.StatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetThingConnectivityDataRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetThingConnectivityDataResponseTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### connected
- **Type**: <class 'bool'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### disconnectReason
- **Type**: typing.Literal['AUTH_ERROR', 'CLIENT_ERROR', 'CLIENT_INITIATED_DISCONNECT', 'CONNECTION_LOST', 'CUSTOMAUTH_TTL_EXPIRATION', 'DUPLICATE_CLIENTID', 'FORBIDDEN_ACCESS', 'MQTT_KEEP_ALIVE_TIMEOUT', 'NONE', 'SERVER_ERROR', 'SERVER_INITIATED_DISCONNECT', 'THROTTLED', 'UNKNOWN', 'WEBSOCKET_TTL_EXPIRATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTopicRuleDestinationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTopicRuleDestinationResponseTypeDef

### topicRuleDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRuleDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTopicRuleRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTopicRuleResponseTypeDef

### ruleArn
- **Type**: <class 'str'>
- **Required**: Yes

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetV2LoggingOptionsResponseTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultLogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes

### disableAllLogs
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupNameAndArnTypeDef

### groupName
- **Type**: typing.Optional[str]

### groupArn
- **Type**: typing.Optional[str]


# HttpActionHeaderTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# HttpActionOutputTypeDef

### url
- **Type**: <class 'str'>
- **Required**: Yes

### confirmationUrl
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.HttpActionHeaderTypeDef]]

### auth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.HttpAuthorizationTypeDef]


# HttpActionTypeDef

### url
- **Type**: <class 'str'>
- **Required**: Yes

### confirmationUrl
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.HttpActionHeaderTypeDef]]

### auth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.HttpAuthorizationTypeDef]


# HttpAuthorizationTypeDef

### sigv4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SigV4AuthorizationTypeDef]


# HttpContextTypeDef

### headers
- **Type**: typing.Optional[typing.Mapping[str, str]]

### queryString
- **Type**: typing.Optional[str]


# HttpUrlDestinationConfigurationTypeDef

### confirmationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# HttpUrlDestinationPropertiesTypeDef

### confirmationUrl
- **Type**: typing.Optional[str]


# HttpUrlDestinationSummaryTypeDef

### confirmationUrl
- **Type**: typing.Optional[str]


# ImplicitDenyTypeDef

### policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.PolicyTypeDef]]


# IndexingFilterOutputTypeDef

### namedShadowNames
- **Type**: typing.Optional[typing.List[str]]

### geoLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.GeoLocationTargetTypeDef]]


# IndexingFilterTypeDef

### namedShadowNames
- **Type**: typing.Optional[typing.Sequence[str]]

### geoLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.GeoLocationTargetTypeDef]]


# IotAnalyticsActionTypeDef

### channelArn
- **Type**: typing.Optional[str]

### channelName
- **Type**: typing.Optional[str]

### batchMode
- **Type**: typing.Optional[bool]

### roleArn
- **Type**: typing.Optional[str]


# IotEventsActionTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageId
- **Type**: typing.Optional[str]

### batchMode
- **Type**: typing.Optional[bool]


# IotSiteWiseActionOutputTypeDef

### putAssetPropertyValueEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PutAssetPropertyValueEntryOutputTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseActionTypeDef

### putAssetPropertyValueEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.PutAssetPropertyValueEntryUnionTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IssuerCertificateIdentifierTypeDef

### issuerCertificateSubject
- **Type**: typing.Optional[str]

### issuerId
- **Type**: typing.Optional[str]

### issuerCertificateSerialNumber
- **Type**: typing.Optional[str]


# JobExecutionStatusDetailsTypeDef

### detailsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobExecutionSummaryForJobTypeDef

### thingArn
- **Type**: typing.Optional[str]

### jobExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionSummaryTypeDef]


# JobExecutionSummaryForThingTypeDef

### jobId
- **Type**: typing.Optional[str]

### jobExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionSummaryTypeDef]


# JobExecutionSummaryTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### queuedAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### executionNumber
- **Type**: typing.Optional[int]

### retryAttempt
- **Type**: typing.Optional[int]


# JobExecutionTypeDef

### jobId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### forceCanceled
- **Type**: typing.Optional[bool]

### statusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionStatusDetailsTypeDef]

### thingArn
- **Type**: typing.Optional[str]

### queuedAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### executionNumber
- **Type**: typing.Optional[int]

### versionNumber
- **Type**: typing.Optional[int]

### approximateSecondsBeforeTimedOut
- **Type**: typing.Optional[int]


# JobExecutionsRetryConfigOutputTypeDef

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.RetryCriteriaTypeDef]
- **Required**: Yes


# JobExecutionsRetryConfigTypeDef

### criteriaList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.RetryCriteriaTypeDef]
- **Required**: Yes


# JobExecutionsRetryConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobExecutionsRolloutConfigTypeDef

### maximumPerMinute
- **Type**: typing.Optional[int]

### exponentialRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ExponentialRolloutRateTypeDef]


# JobProcessDetailsTypeDef

### processingTargets
- **Type**: typing.Optional[typing.List[str]]

### numberOfCanceledThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]

### numberOfFailedThings
- **Type**: typing.Optional[int]

### numberOfRejectedThings
- **Type**: typing.Optional[int]

### numberOfQueuedThings
- **Type**: typing.Optional[int]

### numberOfInProgressThings
- **Type**: typing.Optional[int]

### numberOfRemovedThings
- **Type**: typing.Optional[int]

### numberOfTimedOutThings
- **Type**: typing.Optional[int]


# JobSummaryTypeDef

### jobArn
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### thingGroupId
- **Type**: typing.Optional[str]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'DELETION_IN_PROGRESS', 'IN_PROGRESS', 'SCHEDULED']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### completedAt
- **Type**: typing.Optional[datetime.datetime]

### isConcurrent
- **Type**: typing.Optional[bool]


# JobTemplateSummaryTypeDef

### jobTemplateArn
- **Type**: typing.Optional[str]

### jobTemplateId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# JobTypeDef

### jobArn
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'DELETION_IN_PROGRESS', 'IN_PROGRESS', 'SCHEDULED']]

### forceCanceled
- **Type**: typing.Optional[bool]

### reasonCode
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### presignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PresignedUrlConfigTypeDef]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRolloutConfigTypeDef]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigOutputTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### completedAt
- **Type**: typing.Optional[datetime.datetime]

### jobProcessDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobProcessDetailsTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef]

### namespaceId
- **Type**: typing.Optional[str]

### jobTemplateArn
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigOutputTypeDef]

### documentParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### isConcurrent
- **Type**: typing.Optional[bool]

### schedulingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SchedulingConfigOutputTypeDef]

### scheduledJobRollouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.ScheduledJobRolloutTypeDef]]

### destinationPackageVersions
- **Type**: typing.Optional[typing.List[str]]


# KafkaActionHeaderTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# KafkaActionOutputTypeDef

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### clientProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### key
- **Type**: typing.Optional[str]

### partition
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.KafkaActionHeaderTypeDef]]


# KafkaActionTypeDef

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### clientProperties
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### key
- **Type**: typing.Optional[str]

### partition
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.KafkaActionHeaderTypeDef]]


# KeyPairTypeDef

### PublicKey
- **Type**: typing.Optional[str]

### PrivateKey
- **Type**: typing.Optional[str]


# KinesisActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### streamName
- **Type**: <class 'str'>
- **Required**: Yes

### partitionKey
- **Type**: typing.Optional[str]


# LambdaActionTypeDef

### functionArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListActiveViolationsRequestPaginateTypeDef

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorCriteriaType
- **Type**: typing.Optional[typing.Literal['MACHINE_LEARNING', 'STATIC', 'STATISTICAL']]

### listSuppressedAlerts
- **Type**: typing.Optional[bool]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListActiveViolationsRequestTypeDef

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorCriteriaType
- **Type**: typing.Optional[typing.Literal['MACHINE_LEARNING', 'STATIC', 'STATISTICAL']]

### listSuppressedAlerts
- **Type**: typing.Optional[bool]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListActiveViolationsResponseTypeDef

### activeViolations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ActiveViolationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttachedPoliciesRequestPaginateTypeDef

### target
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAttachedPoliciesRequestTypeDef

### target
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListAttachedPoliciesResponseTypeDef

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PolicyTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAuditFindingsRequestPaginateTypeDef

### taskId
- **Type**: typing.Optional[str]

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### listSuppressedFindings
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditFindingsRequestTypeDef

### taskId
- **Type**: typing.Optional[str]

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### listSuppressedFindings
- **Type**: typing.Optional[bool]


# ListAuditFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuditFindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditMitigationActionsExecutionsRequestPaginateTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### actionStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditMitigationActionsExecutionsRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### actionStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAuditMitigationActionsExecutionsResponseTypeDef

### actionsExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuditMitigationActionExecutionMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditMitigationActionsTasksRequestPaginateTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### auditTaskId
- **Type**: typing.Optional[str]

### findingId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditMitigationActionsTasksRequestTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### auditTaskId
- **Type**: typing.Optional[str]

### findingId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAuditMitigationActionsTasksResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuditMitigationActionsTaskMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditSuppressionsRequestPaginateTypeDef

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditSuppressionsRequestTypeDef

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### ascendingOrder
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAuditSuppressionsResponseTypeDef

### suppressions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuditSuppressionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditTasksRequestPaginateTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### taskType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_AUDIT_TASK', 'SCHEDULED_AUDIT_TASK']]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditTasksRequestTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### taskType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_AUDIT_TASK', 'SCHEDULED_AUDIT_TASK']]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAuditTasksResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuditTaskMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuthorizersRequestPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuthorizersRequestTypeDef

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# ListAuthorizersResponseTypeDef

### authorizers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuthorizerSummaryTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBillingGroupsRequestPaginateTypeDef

### namePrefixFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListBillingGroupsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### namePrefixFilter
- **Type**: typing.Optional[str]


# ListBillingGroupsResponseTypeDef

### billingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.GroupNameAndArnTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCACertificatesRequestPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### templateName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCACertificatesRequestTypeDef

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]

### templateName
- **Type**: typing.Optional[str]


# ListCACertificatesResponseTypeDef

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CACertificateTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCertificateProvidersRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListCertificateProvidersResponseTypeDef

### certificateProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CertificateProviderSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCertificatesByCARequestPaginateTypeDef

### caCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCertificatesByCARequestTypeDef

### caCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListCertificatesByCAResponseTypeDef

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CertificateTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCertificatesRequestPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCertificatesRequestTypeDef

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListCertificatesResponseTypeDef

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CertificateTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCommandExecutionsRequestPaginateTypeDef

### namespace
- **Type**: typing.Optional[typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### startedTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeFilterTypeDef]

### completedTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeFilterTypeDef]

### targetArn
- **Type**: typing.Optional[str]

### commandArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCommandExecutionsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### startedTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeFilterTypeDef]

### completedTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeFilterTypeDef]

### targetArn
- **Type**: typing.Optional[str]

### commandArn
- **Type**: typing.Optional[str]


# ListCommandExecutionsResponseTypeDef

### commandExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CommandExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCommandsRequestPaginateTypeDef

### namespace
- **Type**: typing.Optional[typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']]

### commandParameterName
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCommandsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']]

### commandParameterName
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListCommandsResponseTypeDef

### commands
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CommandSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCustomMetricsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCustomMetricsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCustomMetricsResponseTypeDef

### metricNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsExecutionsRequestPaginateTypeDef

### taskId
- **Type**: typing.Optional[str]

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDetectMitigationActionsExecutionsRequestTypeDef

### taskId
- **Type**: typing.Optional[str]

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsExecutionsResponseTypeDef

### actionsExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsTasksRequestPaginateTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDetectMitigationActionsTasksRequestTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsTasksResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDimensionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDimensionsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDimensionsResponseTypeDef

### dimensionNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainConfigurationsRequestPaginateTypeDef

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDomainConfigurationsRequestTypeDef

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]


# ListDomainConfigurationsResponseTypeDef

### domainConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.DomainConfigurationSummaryTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetMetricsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListFleetMetricsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFleetMetricsResponseTypeDef

### fleetMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.FleetMetricNameAndArnTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIndicesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListIndicesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIndicesResponseTypeDef

### indexNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobExecutionsForJobRequestPaginateTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListJobExecutionsForJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobExecutionsForJobResponseTypeDef

### executionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.JobExecutionSummaryForJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobExecutionsForThingRequestPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### namespaceId
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListJobExecutionsForThingRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### namespaceId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]


# ListJobExecutionsForThingResponseTypeDef

### executionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.JobExecutionSummaryForThingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListJobTemplatesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesResponseTypeDef

### jobTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.JobTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequestPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'DELETION_IN_PROGRESS', 'IN_PROGRESS', 'SCHEDULED']]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### thingGroupName
- **Type**: typing.Optional[str]

### thingGroupId
- **Type**: typing.Optional[str]

### namespaceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListJobsRequestTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'DELETION_IN_PROGRESS', 'IN_PROGRESS', 'SCHEDULED']]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### thingGroupName
- **Type**: typing.Optional[str]

### thingGroupId
- **Type**: typing.Optional[str]

### namespaceId
- **Type**: typing.Optional[str]


# ListJobsResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.JobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedJobTemplatesRequestPaginateTypeDef

### templateName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListManagedJobTemplatesRequestTypeDef

### templateName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedJobTemplatesResponseTypeDef

### managedJobTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ManagedJobTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetricValuesRequestPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### dimensionName
- **Type**: typing.Optional[str]

### dimensionValueOperator
- **Type**: typing.Optional[typing.Literal['IN', 'NOT_IN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListMetricValuesRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### dimensionName
- **Type**: typing.Optional[str]

### dimensionValueOperator
- **Type**: typing.Optional[typing.Literal['IN', 'NOT_IN']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMetricValuesResponseTypeDef

### metricDatumList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MetricDatumTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMitigationActionsRequestPaginateTypeDef

### actionType
- **Type**: typing.Optional[typing.Literal['ADD_THINGS_TO_THING_GROUP', 'ENABLE_IOT_LOGGING', 'PUBLISH_FINDING_TO_SNS', 'REPLACE_DEFAULT_POLICY_VERSION', 'UPDATE_CA_CERTIFICATE', 'UPDATE_DEVICE_CERTIFICATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListMitigationActionsRequestTypeDef

### actionType
- **Type**: typing.Optional[typing.Literal['ADD_THINGS_TO_THING_GROUP', 'ENABLE_IOT_LOGGING', 'PUBLISH_FINDING_TO_SNS', 'REPLACE_DEFAULT_POLICY_VERSION', 'UPDATE_CA_CERTIFICATE', 'UPDATE_DEVICE_CERTIFICATE']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMitigationActionsResponseTypeDef

### actionIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MitigationActionIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOTAUpdatesRequestPaginateTypeDef

### otaUpdateStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListOTAUpdatesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### otaUpdateStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]


# ListOTAUpdatesResponseTypeDef

### otaUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.OTAUpdateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOutgoingCertificatesRequestPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListOutgoingCertificatesRequestTypeDef

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListOutgoingCertificatesResponseTypeDef

### outgoingCertificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.OutgoingCertificateTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackageVersionsRequestPaginateTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPackageVersionsRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPackageVersionsResponseTypeDef

### packageVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PackageVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackagesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPackagesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPackagesResponseTypeDef

### packageSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PackageSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPoliciesRequestPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPoliciesRequestTypeDef

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListPoliciesResponseTypeDef

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PolicyTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPolicyPrincipalsRequestPaginateTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPolicyPrincipalsRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListPolicyPrincipalsResponseTypeDef

### principals
- **Type**: typing.List[str]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPolicyVersionsRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes


# ListPolicyVersionsResponseTypeDef

### policyVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PolicyVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrincipalPoliciesRequestPaginateTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPrincipalPoliciesRequestTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListPrincipalPoliciesResponseTypeDef

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PolicyTypeDef]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrincipalThingsRequestPaginateTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPrincipalThingsRequestTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrincipalThingsResponseTypeDef

### things
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrincipalThingsV2RequestPaginateTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPrincipalThingsV2RequestTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# ListPrincipalThingsV2ResponseTypeDef

### principalThingObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PrincipalThingObjectTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplateVersionsRequestPaginateTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListProvisioningTemplateVersionsRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplateVersionsResponseTypeDef

### versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ProvisioningTemplateVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplatesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListProvisioningTemplatesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplatesResponseTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ProvisioningTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRelatedResourcesForAuditFindingRequestPaginateTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListRelatedResourcesForAuditFindingRequestTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRelatedResourcesForAuditFindingResponseTypeDef

### relatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.RelatedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRoleAliasesRequestPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListRoleAliasesRequestTypeDef

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListRoleAliasesResponseTypeDef

### roleAliases
- **Type**: typing.List[str]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSbomValidationResultsRequestPaginateTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### validationResult
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListSbomValidationResultsRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### validationResult
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSbomValidationResultsResponseTypeDef

### validationResultSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.SbomValidationResultSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScheduledAuditsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListScheduledAuditsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListScheduledAuditsResponseTypeDef

### scheduledAudits
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ScheduledAuditMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilesForTargetRequestPaginateTypeDef

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListSecurityProfilesForTargetRequestTypeDef

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### recursive
- **Type**: typing.Optional[bool]


# ListSecurityProfilesForTargetResponseTypeDef

### securityProfileTargetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.SecurityProfileTargetMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilesRequestPaginateTypeDef

### dimensionName
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListSecurityProfilesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### dimensionName
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]


# ListSecurityProfilesResponseTypeDef

### securityProfileIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.SecurityProfileIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStreamsRequestPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListStreamsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListStreamsResponseTypeDef

### streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.StreamSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTargetsForPolicyRequestPaginateTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTargetsForPolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListTargetsForPolicyResponseTypeDef

### targets
- **Type**: typing.List[str]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetsForSecurityProfileRequestPaginateTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTargetsForSecurityProfileRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTargetsForSecurityProfileResponseTypeDef

### securityProfileTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.SecurityProfileTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingGroupsForThingRequestPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingGroupsForThingRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingGroupsForThingResponseTypeDef

### thingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.GroupNameAndArnTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingGroupsRequestPaginateTypeDef

### parentGroup
- **Type**: typing.Optional[str]

### namePrefixFilter
- **Type**: typing.Optional[str]

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingGroupsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### parentGroup
- **Type**: typing.Optional[str]

### namePrefixFilter
- **Type**: typing.Optional[str]

### recursive
- **Type**: typing.Optional[bool]


# ListThingGroupsResponseTypeDef

### thingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.GroupNameAndArnTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingPrincipalsRequestPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingPrincipalsRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingPrincipalsResponseTypeDef

### principals
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingPrincipalsV2RequestPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingPrincipalsV2RequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# ListThingPrincipalsV2ResponseTypeDef

### thingPrincipalObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingPrincipalObjectTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingRegistrationTaskReportsRequestPaginateTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### reportType
- **Type**: typing.Literal['ERRORS', 'RESULTS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingRegistrationTaskReportsRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### reportType
- **Type**: typing.Literal['ERRORS', 'RESULTS']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingRegistrationTaskReportsResponseTypeDef

### resourceLinks
- **Type**: typing.List[str]
- **Required**: Yes

### reportType
- **Type**: typing.Literal['ERRORS', 'RESULTS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingRegistrationTasksRequestPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Completed', 'Failed', 'InProgress']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingRegistrationTasksRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Completed', 'Failed', 'InProgress']]


# ListThingRegistrationTasksResponseTypeDef

### taskIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingTypesRequestPaginateTypeDef

### thingTypeName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingTypesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### thingTypeName
- **Type**: typing.Optional[str]


# ListThingTypesResponseTypeDef

### thingTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingTypeDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingsInBillingGroupRequestPaginateTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingsInBillingGroupRequestTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingsInBillingGroupResponseTypeDef

### things
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingsInThingGroupRequestPaginateTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingsInThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingsInThingGroupResponseTypeDef

### things
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingsRequestPaginateTypeDef

### attributeName
- **Type**: typing.Optional[str]

### attributeValue
- **Type**: typing.Optional[str]

### thingTypeName
- **Type**: typing.Optional[str]

### usePrefixAttributeValue
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### attributeName
- **Type**: typing.Optional[str]

### attributeValue
- **Type**: typing.Optional[str]

### thingTypeName
- **Type**: typing.Optional[str]

### usePrefixAttributeValue
- **Type**: typing.Optional[bool]


# ListThingsResponseTypeDef

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTopicRuleDestinationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTopicRuleDestinationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTopicRuleDestinationsResponseTypeDef

### destinationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.TopicRuleDestinationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTopicRulesRequestPaginateTypeDef

### topic
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTopicRulesRequestTypeDef

### topic
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]


# ListTopicRulesResponseTypeDef

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.TopicRuleListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListV2LoggingLevelsRequestPaginateTypeDef

### targetType
- **Type**: typing.Optional[typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListV2LoggingLevelsRequestTypeDef

### targetType
- **Type**: typing.Optional[typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListV2LoggingLevelsResponseTypeDef

### logTargetConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.LogTargetConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListViolationEventsRequestPaginateTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorCriteriaType
- **Type**: typing.Optional[typing.Literal['MACHINE_LEARNING', 'STATIC', 'STATISTICAL']]

### listSuppressedAlerts
- **Type**: typing.Optional[bool]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListViolationEventsRequestTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorCriteriaType
- **Type**: typing.Optional[typing.Literal['MACHINE_LEARNING', 'STATIC', 'STATISTICAL']]

### listSuppressedAlerts
- **Type**: typing.Optional[bool]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListViolationEventsResponseTypeDef

### violationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ViolationEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LocationActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### trackerName
- **Type**: <class 'str'>
- **Required**: Yes

### deviceId
- **Type**: <class 'str'>
- **Required**: Yes

### latitude
- **Type**: <class 'str'>
- **Required**: Yes

### longitude
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.LocationTimestampTypeDef]


# LocationTimestampTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes

### unit
- **Type**: typing.Optional[str]


# LogTargetConfigurationTypeDef

### logTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.LogTargetTypeDef]

### logLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']]


# LogTargetTypeDef

### targetType
- **Type**: typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']
- **Required**: Yes

### targetName
- **Type**: typing.Optional[str]


# LoggingOptionsPayloadTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### logLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']]


# MachineLearningDetectionConfigTypeDef

### confidenceLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes


# MaintenanceWindowTypeDef

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ManagedJobTemplateSummaryTypeDef

### templateArn
- **Type**: typing.Optional[str]

### templateName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environments
- **Type**: typing.Optional[typing.List[str]]

### templateVersion
- **Type**: typing.Optional[str]


# MetricDatumTypeDef

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueOutputTypeDef]


# MetricDimensionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricToRetainTypeDef

### metric
- **Type**: <class 'str'>
- **Required**: Yes

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricDimensionTypeDef]

### exportMetric
- **Type**: typing.Optional[bool]


# MetricValueOutputTypeDef

### count
- **Type**: typing.Optional[int]

### cidrs
- **Type**: typing.Optional[typing.List[str]]

### ports
- **Type**: typing.Optional[typing.List[int]]

### number
- **Type**: typing.Optional[float]

### numbers
- **Type**: typing.Optional[typing.List[float]]

### strings
- **Type**: typing.Optional[typing.List[str]]


# MetricValueTypeDef

### count
- **Type**: typing.Optional[int]

### cidrs
- **Type**: typing.Optional[typing.Sequence[str]]

### ports
- **Type**: typing.Optional[typing.Sequence[int]]

### number
- **Type**: typing.Optional[float]

### numbers
- **Type**: typing.Optional[typing.Sequence[float]]

### strings
- **Type**: typing.Optional[typing.Sequence[str]]


# MetricValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricsExportConfigTypeDef

### mqttTopic
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# MitigationActionIdentifierTypeDef

### actionName
- **Type**: typing.Optional[str]

### actionArn
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# MitigationActionParamsOutputTypeDef

### updateDeviceCertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.UpdateDeviceCertificateParamsTypeDef]

### updateCACertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.UpdateCACertificateParamsTypeDef]

### addThingsToThingGroupParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AddThingsToThingGroupParamsOutputTypeDef]

### replaceDefaultPolicyVersionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ReplaceDefaultPolicyVersionParamsTypeDef]

### enableIoTLoggingParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.EnableIoTLoggingParamsTypeDef]

### publishFindingToSnsParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PublishFindingToSnsParamsTypeDef]


# MitigationActionParamsTypeDef

### updateDeviceCertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.UpdateDeviceCertificateParamsTypeDef]

### updateCACertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.UpdateCACertificateParamsTypeDef]

### addThingsToThingGroupParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AddThingsToThingGroupParamsTypeDef]

### replaceDefaultPolicyVersionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ReplaceDefaultPolicyVersionParamsTypeDef]

### enableIoTLoggingParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.EnableIoTLoggingParamsTypeDef]

### publishFindingToSnsParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PublishFindingToSnsParamsTypeDef]


# MitigationActionParamsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MitigationActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Mqtt5ConfigurationOutputTypeDef

### propagatingAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.PropagatingAttributeTypeDef]]


# Mqtt5ConfigurationTypeDef

### propagatingAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.PropagatingAttributeTypeDef]]


# MqttContextTypeDef

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BlobTypeDef]

### clientId
- **Type**: typing.Optional[str]


# MqttHeadersOutputTypeDef

### payloadFormatIndicator
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]

### responseTopic
- **Type**: typing.Optional[str]

### correlationData
- **Type**: typing.Optional[str]

### messageExpiry
- **Type**: typing.Optional[str]

### userProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.UserPropertyTypeDef]]


# MqttHeadersTypeDef

### payloadFormatIndicator
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]

### responseTopic
- **Type**: typing.Optional[str]

### correlationData
- **Type**: typing.Optional[str]

### messageExpiry
- **Type**: typing.Optional[str]

### userProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.UserPropertyTypeDef]]


# MqttHeadersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NonCompliantResourceTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SETTINGS', 'CA_CERTIFICATE', 'CLIENT_ID', 'COGNITO_IDENTITY_POOL', 'DEVICE_CERTIFICATE', 'IAM_ROLE', 'IOT_POLICY', 'ISSUER_CERTIFICATE', 'ROLE_ALIAS']]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]


# OTAUpdateFileOutputTypeDef

### fileName
- **Type**: typing.Optional[str]

### fileType
- **Type**: typing.Optional[int]

### fileVersion
- **Type**: typing.Optional[str]

### fileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.FileLocationTypeDef]

### codeSigning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningOutputTypeDef]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# OTAUpdateFileTypeDef

### fileName
- **Type**: typing.Optional[str]

### fileType
- **Type**: typing.Optional[int]

### fileVersion
- **Type**: typing.Optional[str]

### fileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.FileLocationTypeDef]

### codeSigning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningUnionTypeDef]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# OTAUpdateFileUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OTAUpdateInfoTypeDef

### otaUpdateId
- **Type**: typing.Optional[str]

### otaUpdateArn
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.List[str]]

### protocols
- **Type**: typing.Optional[typing.List[typing.Literal['HTTP', 'MQTT']]]

### awsJobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AwsJobExecutionsRolloutConfigTypeDef]

### awsJobPresignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AwsJobPresignedUrlConfigTypeDef]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### otaUpdateFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.OTAUpdateFileOutputTypeDef]]

### otaUpdateStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### awsIotJobId
- **Type**: typing.Optional[str]

### awsIotJobArn
- **Type**: typing.Optional[str]

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ErrorInfoTypeDef]

### additionalParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# OTAUpdateSummaryTypeDef

### otaUpdateId
- **Type**: typing.Optional[str]

### otaUpdateArn
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# OutgoingCertificateTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### certificateId
- **Type**: typing.Optional[str]

### transferredTo
- **Type**: typing.Optional[str]

### transferDate
- **Type**: typing.Optional[datetime.datetime]

### transferMessage
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# PackageSummaryTypeDef

### packageName
- **Type**: typing.Optional[str]

### defaultVersionName
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# PackageVersionArtifactTypeDef

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.S3LocationTypeDef]


# PackageVersionSummaryTypeDef

### packageName
- **Type**: typing.Optional[str]

### versionName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PercentPairTypeDef

### percent
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[float]


# PolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### policyArn
- **Type**: typing.Optional[str]


# PolicyVersionIdentifierTypeDef

### policyName
- **Type**: typing.Optional[str]

### policyVersionId
- **Type**: typing.Optional[str]


# PolicyVersionTypeDef

### versionId
- **Type**: typing.Optional[str]

### isDefaultVersion
- **Type**: typing.Optional[bool]

### createDate
- **Type**: typing.Optional[datetime.datetime]


# PresignedUrlConfigTypeDef

### roleArn
- **Type**: typing.Optional[str]

### expiresInSec
- **Type**: typing.Optional[int]


# PrincipalThingObjectTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# PropagatingAttributeTypeDef

### userPropertyKey
- **Type**: typing.Optional[str]

### thingAttribute
- **Type**: typing.Optional[str]

### connectionAttribute
- **Type**: typing.Optional[str]


# ProvisioningHookTypeDef

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### payloadVersion
- **Type**: typing.Optional[str]


# ProvisioningTemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisioningTemplateVersionSummaryTypeDef

### versionId
- **Type**: typing.Optional[int]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### isDefaultVersion
- **Type**: typing.Optional[bool]


# PublishFindingToSnsParamsTypeDef

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutAssetPropertyValueEntryOutputTypeDef

### propertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AssetPropertyValueTypeDef]
- **Required**: Yes

### entryId
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# PutAssetPropertyValueEntryTypeDef

### propertyValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.AssetPropertyValueTypeDef]
- **Required**: Yes

### entryId
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# PutAssetPropertyValueEntryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutItemInputTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# PutVerificationStateOnViolationRequestTypeDef

### violationId
- **Type**: <class 'str'>
- **Required**: Yes

### verificationState
- **Type**: typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']
- **Required**: Yes

### verificationStateDescription
- **Type**: typing.Optional[str]


# RateIncreaseCriteriaTypeDef

### numberOfNotifiedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]


# RegisterCACertificateRequestTypeDef

### caCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### verificationCertificate
- **Type**: typing.Optional[str]

### setAsActive
- **Type**: typing.Optional[bool]

### allowAutoRegistration
- **Type**: typing.Optional[bool]

### registrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.RegistrationConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### certificateMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'SNI_ONLY']]


# RegisterCACertificateResponseTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterCertificateRequestTypeDef

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### caCertificatePem
- **Type**: typing.Optional[str]

### setAsActive
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']]


# RegisterCertificateResponseTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterCertificateWithoutCARequestTypeDef

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']]


# RegisterCertificateWithoutCAResponseTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterThingRequestTypeDef

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterThingResponseTypeDef

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegistrationConfigTypeDef

### templateBody
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### templateName
- **Type**: typing.Optional[str]


# RejectCertificateTransferRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### rejectReason
- **Type**: typing.Optional[str]


# RelatedResourceTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SETTINGS', 'CA_CERTIFICATE', 'CLIENT_ID', 'COGNITO_IDENTITY_POOL', 'DEVICE_CERTIFICATE', 'IAM_ROLE', 'IOT_POLICY', 'ISSUER_CERTIFICATE', 'ROLE_ALIAS']]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]


# RemoveThingFromBillingGroupRequestTypeDef

### billingGroupName
- **Type**: typing.Optional[str]

### billingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# RemoveThingFromThingGroupRequestTypeDef

### thingGroupName
- **Type**: typing.Optional[str]

### thingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# ReplaceDefaultPolicyVersionParamsTypeDef

### templateName
- **Type**: typing.Literal['BLANK_POLICY']
- **Required**: Yes


# ReplaceTopicRuleRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### topicRulePayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRulePayloadTypeDef'>
- **Required**: Yes


# RepublishActionOutputTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### qos
- **Type**: typing.Optional[int]

### headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MqttHeadersOutputTypeDef]


# RepublishActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### qos
- **Type**: typing.Optional[int]

### headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MqttHeadersUnionTypeDef]


# ResourceIdentifierTypeDef

### deviceCertificateId
- **Type**: typing.Optional[str]

### caCertificateId
- **Type**: typing.Optional[str]

### cognitoIdentityPoolId
- **Type**: typing.Optional[str]

### clientId
- **Type**: typing.Optional[str]

### policyVersionIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PolicyVersionIdentifierTypeDef]

### account
- **Type**: typing.Optional[str]

### iamRoleArn
- **Type**: typing.Optional[str]

### roleAliasArn
- **Type**: typing.Optional[str]

### issuerCertificateIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.IssuerCertificateIdentifierTypeDef]

### deviceCertificateArn
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


# RetryCriteriaTypeDef

### failureType
- **Type**: typing.Literal['ALL', 'FAILED', 'TIMED_OUT']
- **Required**: Yes

### numberOfRetries
- **Type**: <class 'int'>
- **Required**: Yes


# RoleAliasDescriptionTypeDef

### roleAlias
- **Type**: typing.Optional[str]

### roleAliasArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### credentialDurationSeconds
- **Type**: typing.Optional[int]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# S3ActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### cannedAcl
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'log-delivery-write', 'private', 'public-read', 'public-read-write']]


# S3DestinationTypeDef

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# S3LocationTypeDef

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# SalesforceActionTypeDef

### token
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes


# SbomTypeDef

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.S3LocationTypeDef]


# SbomValidationResultSummaryTypeDef

### fileName
- **Type**: typing.Optional[str]

### validationResult
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]

### errorCode
- **Type**: typing.Optional[typing.Literal['FILE_SIZE_LIMIT_EXCEEDED', 'INCOMPATIBLE_FORMAT']]

### errorMessage
- **Type**: typing.Optional[str]


# ScheduledAuditMetadataTypeDef

### scheduledAuditName
- **Type**: typing.Optional[str]

### scheduledAuditArn
- **Type**: typing.Optional[str]

### frequency
- **Type**: typing.Optional[typing.Literal['BIWEEKLY', 'DAILY', 'MONTHLY', 'WEEKLY']]

### dayOfMonth
- **Type**: typing.Optional[str]

### dayOfWeek
- **Type**: typing.Optional[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]


# ScheduledJobRolloutTypeDef

### startTime
- **Type**: typing.Optional[str]


# SchedulingConfigOutputTypeDef

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]

### endBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL', 'FORCE_CANCEL', 'STOP_ROLLOUT']]

### maintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.MaintenanceWindowTypeDef]]


# SchedulingConfigTypeDef

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]

### endBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL', 'FORCE_CANCEL', 'STOP_ROLLOUT']]

### maintenanceWindows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.MaintenanceWindowTypeDef]]


# SchedulingConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchIndexRequestTypeDef

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### queryVersion
- **Type**: typing.Optional[str]


# SearchIndexResponseTypeDef

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingDocumentTypeDef]
- **Required**: Yes

### thingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingGroupDocumentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SecurityProfileIdentifierTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# SecurityProfileTargetMappingTypeDef

### securityProfileIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SecurityProfileIdentifierTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SecurityProfileTargetTypeDef]


# SecurityProfileTargetTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ServerCertificateConfigTypeDef

### enableOCSPCheck
- **Type**: typing.Optional[bool]

### ocspLambdaArn
- **Type**: typing.Optional[str]

### ocspAuthorizedResponderArn
- **Type**: typing.Optional[str]


# ServerCertificateSummaryTypeDef

### serverCertificateArn
- **Type**: typing.Optional[str]

### serverCertificateStatus
- **Type**: typing.Optional[typing.Literal['INVALID', 'VALID']]

### serverCertificateStatusDetail
- **Type**: typing.Optional[str]


# SetDefaultAuthorizerRequestTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes


# SetDefaultAuthorizerResponseTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetDefaultPolicyVersionRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# SetLoggingOptionsRequestTypeDef

### loggingOptionsPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.LoggingOptionsPayloadTypeDef'>
- **Required**: Yes


# SetV2LoggingLevelRequestTypeDef

### logTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.LogTargetTypeDef'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# SetV2LoggingOptionsRequestTypeDef

### roleArn
- **Type**: typing.Optional[str]

### defaultLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']]

### disableAllLogs
- **Type**: typing.Optional[bool]


# SigV4AuthorizationTypeDef

### signingRegion
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# SigningProfileParameterTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]

### certificatePathOnDevice
- **Type**: typing.Optional[str]


# SnsActionTypeDef

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'RAW']]


# SqsActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### queueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### useBase64
- **Type**: typing.Optional[bool]


# StartAuditMitigationActionsTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuditMitigationActionsTaskTargetUnionTypeDef'>
- **Required**: Yes

### auditCheckToActionsMapping
- **Type**: typing.Mapping[str, typing.Sequence[str]]
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartAuditMitigationActionsTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDetectMitigationActionsTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskTargetUnionTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### violationEventOccurrenceRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ViolationEventOccurrenceRangeUnionTypeDef]

### includeOnlyActiveViolations
- **Type**: typing.Optional[bool]

### includeSuppressedAlerts
- **Type**: typing.Optional[bool]


# StartDetectMitigationActionsTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartOnDemandAuditTaskRequestTypeDef

### targetCheckNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StartOnDemandAuditTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSigningJobParameterTypeDef

### signingProfileParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SigningProfileParameterTypeDef]

### signingProfileName
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DestinationTypeDef]


# StartThingRegistrationTaskRequestTypeDef

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### inputFileBucket
- **Type**: <class 'str'>
- **Required**: Yes

### inputFileKey
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartThingRegistrationTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatisticalThresholdTypeDef

### statistic
- **Type**: typing.Optional[str]


# StatisticsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatusReasonTypeDef

### reasonCode
- **Type**: <class 'str'>
- **Required**: Yes

### reasonDescription
- **Type**: typing.Optional[str]


# StepFunctionsActionTypeDef

### stateMachineName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionNamePrefix
- **Type**: typing.Optional[str]


# StopThingRegistrationTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# StreamFileTypeDef

### fileId
- **Type**: typing.Optional[int]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.S3LocationTypeDef]


# StreamInfoTypeDef

### streamId
- **Type**: typing.Optional[str]

### streamArn
- **Type**: typing.Optional[str]

### streamVersion
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.StreamFileTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### roleArn
- **Type**: typing.Optional[str]


# StreamSummaryTypeDef

### streamId
- **Type**: typing.Optional[str]

### streamArn
- **Type**: typing.Optional[str]

### streamVersion
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]


# StreamTypeDef

### streamId
- **Type**: typing.Optional[str]

### fileId
- **Type**: typing.Optional[int]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TaskStatisticsForAuditCheckTypeDef

### totalFindingsCount
- **Type**: typing.Optional[int]

### failedFindingsCount
- **Type**: typing.Optional[int]

### succeededFindingsCount
- **Type**: typing.Optional[int]

### skippedFindingsCount
- **Type**: typing.Optional[int]

### canceledFindingsCount
- **Type**: typing.Optional[int]


# TaskStatisticsTypeDef

### totalChecks
- **Type**: typing.Optional[int]

### inProgressChecks
- **Type**: typing.Optional[int]

### waitingForDataCollectionChecks
- **Type**: typing.Optional[int]

### compliantChecks
- **Type**: typing.Optional[int]

### nonCompliantChecks
- **Type**: typing.Optional[int]

### failedChecks
- **Type**: typing.Optional[int]

### canceledChecks
- **Type**: typing.Optional[int]


# TermsAggregationTypeDef

### maxBuckets
- **Type**: typing.Optional[int]


# TestAuthorizationRequestTypeDef

### authInfos
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.AuthInfoUnionTypeDef]
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### cognitoIdentityPoolId
- **Type**: typing.Optional[str]

### clientId
- **Type**: typing.Optional[str]

### policyNamesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### policyNamesToSkip
- **Type**: typing.Optional[typing.Sequence[str]]


# TestAuthorizationResponseTypeDef

### authResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuthResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TestInvokeAuthorizerRequestTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: typing.Optional[str]

### tokenSignature
- **Type**: typing.Optional[str]

### httpContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.HttpContextTypeDef]

### mqttContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MqttContextTypeDef]

### tlsContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TlsContextTypeDef]


# TestInvokeAuthorizerResponseTypeDef

### isAuthenticated
- **Type**: <class 'bool'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocuments
- **Type**: typing.List[str]
- **Required**: Yes

### refreshAfterInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### disconnectAfterInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ThingAttributeTypeDef

### thingName
- **Type**: typing.Optional[str]

### thingTypeName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### version
- **Type**: typing.Optional[int]


# ThingConnectivityTypeDef

### connected
- **Type**: typing.Optional[bool]

### timestamp
- **Type**: typing.Optional[int]

### disconnectReason
- **Type**: typing.Optional[str]


# ThingDocumentTypeDef

### thingName
- **Type**: typing.Optional[str]

### thingId
- **Type**: typing.Optional[str]

### thingTypeName
- **Type**: typing.Optional[str]

### thingGroupNames
- **Type**: typing.Optional[typing.List[str]]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### shadow
- **Type**: typing.Optional[str]

### deviceDefender
- **Type**: typing.Optional[str]

### connectivity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingConnectivityTypeDef]


# ThingGroupDocumentTypeDef

### thingGroupName
- **Type**: typing.Optional[str]

### thingGroupId
- **Type**: typing.Optional[str]

### thingGroupDescription
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### parentGroupNames
- **Type**: typing.Optional[typing.List[str]]


# ThingGroupIndexingConfigurationOutputTypeDef

### thingGroupIndexingMode
- **Type**: typing.Literal['OFF', 'ON']
- **Required**: Yes

### managedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]

### customFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]


# ThingGroupIndexingConfigurationTypeDef

### thingGroupIndexingMode
- **Type**: typing.Literal['OFF', 'ON']
- **Required**: Yes

### managedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]

### customFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]


# ThingGroupIndexingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThingGroupMetadataTypeDef

### parentGroupName
- **Type**: typing.Optional[str]

### rootToParentThingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.GroupNameAndArnTypeDef]]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# ThingGroupPropertiesOutputTypeDef

### thingGroupDescription
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AttributePayloadOutputTypeDef]


# ThingGroupPropertiesTypeDef

### thingGroupDescription
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AttributePayloadTypeDef]


# ThingGroupPropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThingIndexingConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThingIndexingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThingPrincipalObjectTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# ThingTypeDefinitionTypeDef

### thingTypeName
- **Type**: typing.Optional[str]

### thingTypeArn
- **Type**: typing.Optional[str]

### thingTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesOutputTypeDef]

### thingTypeMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypeMetadataTypeDef]


# ThingTypeMetadataTypeDef

### deprecated
- **Type**: typing.Optional[bool]

### deprecationDate
- **Type**: typing.Optional[datetime.datetime]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# ThingTypePropertiesOutputTypeDef

### thingTypeDescription
- **Type**: typing.Optional[str]

### searchableAttributes
- **Type**: typing.Optional[typing.List[str]]

### mqtt5Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.Mqtt5ConfigurationOutputTypeDef]


# ThingTypePropertiesTypeDef

### thingTypeDescription
- **Type**: typing.Optional[str]

### searchableAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### mqtt5Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.Mqtt5ConfigurationTypeDef]


# ThingTypePropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeFilterTypeDef

### after
- **Type**: typing.Optional[str]

### before
- **Type**: typing.Optional[str]


# TimeoutConfigTypeDef

### inProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestreamActionOutputTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.TimestreamDimensionTypeDef]
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestreamTimestampTypeDef]


# TimestreamActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### dimensions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TimestreamDimensionTypeDef]
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestreamTimestampTypeDef]


# TimestreamDimensionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestreamTimestampTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes

### unit
- **Type**: <class 'str'>
- **Required**: Yes


# TlsConfigTypeDef

### securityPolicy
- **Type**: typing.Optional[str]


# TlsContextTypeDef

### serverName
- **Type**: typing.Optional[str]


# TopicRuleDestinationConfigurationTypeDef

### httpUrlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.HttpUrlDestinationConfigurationTypeDef]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.VpcDestinationConfigurationTypeDef]


# TopicRuleDestinationSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DELETING', 'DISABLED', 'ENABLED', 'ERROR', 'IN_PROGRESS']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### statusReason
- **Type**: typing.Optional[str]

### httpUrlSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.HttpUrlDestinationSummaryTypeDef]

### vpcDestinationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.VpcDestinationSummaryTypeDef]


# TopicRuleDestinationTypeDef

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DELETING', 'DISABLED', 'ENABLED', 'ERROR', 'IN_PROGRESS']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### statusReason
- **Type**: typing.Optional[str]

### httpUrlProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.HttpUrlDestinationPropertiesTypeDef]

### vpcProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.VpcDestinationPropertiesTypeDef]


# TopicRuleListItemTypeDef

### ruleArn
- **Type**: typing.Optional[str]

### ruleName
- **Type**: typing.Optional[str]

### topicPattern
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### ruleDisabled
- **Type**: typing.Optional[bool]


# TopicRulePayloadTypeDef

### sql
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.ActionUnionTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]

### awsIotSqlVersion
- **Type**: typing.Optional[str]

### errorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ActionUnionTypeDef]


# TopicRuleTypeDef

### ruleName
- **Type**: typing.Optional[str]

### sql
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.ActionOutputTypeDef]]

### ruleDisabled
- **Type**: typing.Optional[bool]

### awsIotSqlVersion
- **Type**: typing.Optional[str]

### errorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ActionOutputTypeDef]


# TransferCertificateRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### targetAwsAccount
- **Type**: <class 'str'>
- **Required**: Yes

### transferMessage
- **Type**: typing.Optional[str]


# TransferCertificateResponseTypeDef

### transferredCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TransferDataTypeDef

### transferMessage
- **Type**: typing.Optional[str]

### rejectReason
- **Type**: typing.Optional[str]

### transferDate
- **Type**: typing.Optional[datetime.datetime]

### acceptDate
- **Type**: typing.Optional[datetime.datetime]

### rejectDate
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountAuditConfigurationRequestTypeDef

### roleArn
- **Type**: typing.Optional[str]

### auditNotificationTargetConfigurations
- **Type**: typing.Optional[typing.Mapping[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot_classes.AuditNotificationTargetTypeDef]]

### auditCheckConfigurations
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iot_classes.AuditCheckConfigurationUnionTypeDef]]


# UpdateAuditSuppressionRequestTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes

### expirationDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef]

### suppressIndefinitely
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# UpdateAuthorizerRequestTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerFunctionArn
- **Type**: typing.Optional[str]

### tokenKeyName
- **Type**: typing.Optional[str]

### tokenSigningPublicKeys
- **Type**: typing.Optional[typing.Mapping[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### enableCachingForHttp
- **Type**: typing.Optional[bool]


# UpdateAuthorizerResponseTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBillingGroupRequestTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.BillingGroupPropertiesTypeDef'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# UpdateBillingGroupResponseTypeDef

### version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCACertificateParamsTypeDef

### action
- **Type**: typing.Literal['DEACTIVATE']
- **Required**: Yes


# UpdateCACertificateRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### newStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### newAutoRegistrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### registrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.RegistrationConfigTypeDef]

### removeAutoRegistration
- **Type**: typing.Optional[bool]


# UpdateCertificateProviderRequestTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### lambdaFunctionArn
- **Type**: typing.Optional[str]

### accountDefaultForOperations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CreateCertificateFromCsr']]]


# UpdateCertificateProviderResponseTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCertificateRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### newStatus
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']
- **Required**: Yes


# UpdateCommandRequestTypeDef

### commandId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### deprecated
- **Type**: typing.Optional[bool]


# UpdateCommandResponseTypeDef

### commandId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### deprecated
- **Type**: <class 'bool'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCustomMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCustomMetricResponseTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricArn
- **Type**: <class 'str'>
- **Required**: Yes

### metricType
- **Type**: typing.Literal['ip-address-list', 'number', 'number-list', 'string-list']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDeviceCertificateParamsTypeDef

### action
- **Type**: typing.Literal['DEACTIVATE']
- **Required**: Yes


# UpdateDimensionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stringValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDomainConfigurationRequestTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AuthorizerConfigTypeDef]

### domainConfigurationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### removeAuthorizerConfig
- **Type**: typing.Optional[bool]

### tlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TlsConfigTypeDef]

### serverCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ServerCertificateConfigTypeDef]

### authenticationType
- **Type**: typing.Optional[typing.Literal['AWS_SIGV4', 'AWS_X509', 'CUSTOM_AUTH', 'CUSTOM_AUTH_X509', 'DEFAULT']]

### applicationProtocol
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HTTPS', 'MQTT_WSS', 'SECURE_MQTT']]

### clientCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ClientCertificateConfigTypeDef]


# UpdateDomainConfigurationResponseTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### domainConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDynamicThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesUnionTypeDef'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]

### indexName
- **Type**: typing.Optional[str]

### queryString
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# UpdateDynamicThingGroupResponseTypeDef

### version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventConfigurationsRequestTypeDef

### eventConfigurations
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CA_CERTIFICATE', 'CERTIFICATE', 'JOB', 'JOB_EXECUTION', 'POLICY', 'THING', 'THING_GROUP', 'THING_GROUP_HIERARCHY', 'THING_GROUP_MEMBERSHIP', 'THING_TYPE', 'THING_TYPE_ASSOCIATION'], aws_resource_validator.pydantic_models.iot_classes.ConfigurationTypeDef]]


# UpdateFleetMetricRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: typing.Optional[str]

### aggregationType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AggregationTypeUnionTypeDef]

### period
- **Type**: typing.Optional[int]

### aggregationField
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### expectedVersion
- **Type**: typing.Optional[int]


# UpdateIndexingConfigurationRequestTypeDef

### thingIndexingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingIndexingConfigurationUnionTypeDef]

### thingGroupIndexingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingGroupIndexingConfigurationUnionTypeDef]


# UpdateJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### presignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PresignedUrlConfigTypeDef]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRolloutConfigTypeDef]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigUnionTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef]

### namespaceId
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigUnionTypeDef]


# UpdateMitigationActionRequestTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### actionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsUnionTypeDef]


# UpdateMitigationActionResponseTypeDef

### actionArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePackageConfigurationRequestTypeDef

### versionUpdateByJobsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.VersionUpdateByJobsConfigTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# UpdatePackageRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### defaultVersionName
- **Type**: typing.Optional[str]

### unsetDefaultVersion
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]


# UpdatePackageVersionRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### artifact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PackageVersionArtifactTypeDef]

### action
- **Type**: typing.Optional[typing.Literal['DEPRECATE', 'PUBLISH']]

### recipe
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateProvisioningTemplateRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### defaultVersionId
- **Type**: typing.Optional[int]

### provisioningRoleArn
- **Type**: typing.Optional[str]

### preProvisioningHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ProvisioningHookTypeDef]

### removePreProvisioningHook
- **Type**: typing.Optional[bool]


# UpdateRoleAliasRequestTypeDef

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### credentialDurationSeconds
- **Type**: typing.Optional[int]


# UpdateRoleAliasResponseTypeDef

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScheduledAuditRequestTypeDef

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes

### frequency
- **Type**: typing.Optional[typing.Literal['BIWEEKLY', 'DAILY', 'MONTHLY', 'WEEKLY']]

### dayOfMonth
- **Type**: typing.Optional[str]

### dayOfWeek
- **Type**: typing.Optional[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]

### targetCheckNames
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateScheduledAuditResponseTypeDef

### scheduledAuditArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSecurityProfileRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: typing.Optional[str]

### behaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.BehaviorUnionTypeDef]]

### alertTargets
- **Type**: typing.Optional[typing.Mapping[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot_classes.AlertTargetTypeDef]]

### additionalMetricsToRetain
- **Type**: typing.Optional[typing.Sequence[str]]

### additionalMetricsToRetainV2
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.MetricToRetainTypeDef]]

### deleteBehaviors
- **Type**: typing.Optional[bool]

### deleteAlertTargets
- **Type**: typing.Optional[bool]

### deleteAdditionalMetricsToRetain
- **Type**: typing.Optional[bool]

### expectedVersion
- **Type**: typing.Optional[int]

### metricsExportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricsExportConfigTypeDef]

### deleteMetricsExportConfig
- **Type**: typing.Optional[bool]


# UpdateSecurityProfileResponseTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: <class 'str'>
- **Required**: Yes

### behaviors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.BehaviorOutputTypeDef]
- **Required**: Yes

### alertTargets
- **Type**: typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot_classes.AlertTargetTypeDef]
- **Required**: Yes

### additionalMetricsToRetain
- **Type**: typing.List[str]
- **Required**: Yes

### additionalMetricsToRetainV2
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MetricToRetainTypeDef]
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### metricsExportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.MetricsExportConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStreamRequestTypeDef

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### files
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.StreamFileTypeDef]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateStreamResponseTypeDef

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### streamArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### streamVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateThingGroupRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesUnionTypeDef'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# UpdateThingGroupResponseTypeDef

### version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateThingGroupsForThingRequestTypeDef

### thingName
- **Type**: typing.Optional[str]

### thingGroupsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### thingGroupsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# UpdateThingRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeName
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AttributePayloadUnionTypeDef]

### expectedVersion
- **Type**: typing.Optional[int]

### removeThingType
- **Type**: typing.Optional[bool]


# UpdateThingTypeRequestTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesUnionTypeDef]


# UpdateTopicRuleDestinationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETING', 'DISABLED', 'ENABLED', 'ERROR', 'IN_PROGRESS']
- **Required**: Yes


# UserPropertyTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateSecurityProfileBehaviorsRequestTypeDef

### behaviors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.BehaviorUnionTypeDef]
- **Required**: Yes


# ValidateSecurityProfileBehaviorsResponseTypeDef

### valid
- **Type**: <class 'bool'>
- **Required**: Yes

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ValidationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidationErrorTypeDef

### errorMessage
- **Type**: typing.Optional[str]


# VersionUpdateByJobsConfigTypeDef

### enabled
- **Type**: typing.Optional[bool]

### roleArn
- **Type**: typing.Optional[str]


# ViolationEventAdditionalInfoTypeDef

### confidenceLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# ViolationEventOccurrenceRangeOutputTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ViolationEventOccurrenceRangeTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimestampTypeDef'>
- **Required**: Yes


# ViolationEventOccurrenceRangeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ViolationEventTypeDef

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorOutputTypeDef]

### metricValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueOutputTypeDef]

### violationEventAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ViolationEventAdditionalInfoTypeDef]

### violationEventType
- **Type**: typing.Optional[typing.Literal['alarm-cleared', 'alarm-invalidated', 'in-alarm']]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### verificationStateDescription
- **Type**: typing.Optional[str]

### violationEventTime
- **Type**: typing.Optional[datetime.datetime]


# VpcDestinationConfigurationTypeDef

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# VpcDestinationPropertiesTypeDef

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# VpcDestinationSummaryTypeDef

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


