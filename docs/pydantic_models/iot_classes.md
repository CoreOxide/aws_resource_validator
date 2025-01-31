# Iot Classes

# AbortConfigTypeDef

### criteriaList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.AbortCriteriaTypeDef]
- **Required**: Yes


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


# AcceptCertificateTransferRequestRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### setAsActive
- **Type**: typing.Optional[bool]


# ActionTypeDef

### dynamoDB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DynamoDBActionTypeDef]

### dynamoDBv2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DynamoDBv2ActionTypeDef]

### sns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SnsActionTypeDef]

### sqs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SqsActionTypeDef]

### kinesis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.KinesisActionTypeDef]

### republish
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.RepublishActionTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.S3ActionTypeDef]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.FirehoseActionTypeDef]

### cloudwatchMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CloudwatchMetricActionTypeDef]

### cloudwatchAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CloudwatchAlarmActionTypeDef]

### cloudwatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CloudwatchLogsActionTypeDef]

### elasticsearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ElasticsearchActionTypeDef]

### salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SalesforceActionTypeDef]

### iotAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.IotAnalyticsActionTypeDef]

### iotEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.IotEventsActionTypeDef]

### iotSiteWise
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.IotSiteWiseActionTypeDef]

### stepFunctions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.StepFunctionsActionTypeDef]

### timestream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimestreamActionTypeDef]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.HttpActionTypeDef]

### kafka
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.KafkaActionTypeDef]

### openSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.OpenSearchActionTypeDef]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.LocationActionTypeDef]


# ActiveViolationPaginatorTypeDef

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorPaginatorTypeDef]

### lastViolationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValuePaginatorTypeDef]

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


# ActiveViolationTypeDef

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorTypeDef]

### lastViolationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueTypeDef]

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


# AddThingToBillingGroupRequestRequestTypeDef

### billingGroupName
- **Type**: typing.Optional[str]

### billingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# AddThingToThingGroupRequestRequestTypeDef

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


# AddThingsToThingGroupParamsPaginatorTypeDef

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


# AggregationTypeTypeDef

### name
- **Type**: typing.Literal['Cardinality', 'Percentiles', 'Statistics']
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.Sequence[str]]


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


# AssociateTargetsWithJobRequestRequestTypeDef

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


# AttachPolicyRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# AttachPrincipalPolicyRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# AttachSecurityProfileRequestRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachThingPrincipalRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# AttributePayloadTypeDef

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### merge
- **Type**: typing.Optional[bool]


# AuditCheckConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]


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


# AuditMitigationActionsTaskTargetTypeDef

### auditTaskId
- **Type**: typing.Optional[str]

### findingIds
- **Type**: typing.Optional[typing.List[str]]

### auditCheckToReasonCodeFilter
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


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


# AuthInfoTypeDef

### resources
- **Type**: typing.Sequence[str]
- **Required**: Yes

### actionType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'PUBLISH', 'RECEIVE', 'SUBSCRIBE']]


# AuthResultTypeDef

### authInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AuthInfoTypeDef]

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

# BehaviorCriteriaPaginatorTypeDef

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['greater-than', 'greater-than-equals', 'in-cidr-set', 'in-port-set', 'in-set', 'less-than', 'less-than-equals', 'not-in-cidr-set', 'not-in-port-set', 'not-in-set']]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValuePaginatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueTypeDef]

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


# BehaviorPaginatorTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### metric
- **Type**: typing.Optional[str]

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricDimensionTypeDef]

### criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorCriteriaPaginatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorCriteriaTypeDef]

### suppressAlerts
- **Type**: typing.Optional[bool]

### exportMetric
- **Type**: typing.Optional[bool]


# BillingGroupMetadataTypeDef

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# BillingGroupPropertiesTypeDef

### billingGroupDescription
- **Type**: typing.Optional[str]


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


# CancelAuditMitigationActionsTaskRequestRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelAuditTaskRequestRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelCertificateTransferRequestRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDetectMitigationActionsTaskRequestRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobExecutionRequestRequestTypeDef

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


# CancelJobRequestRequestTypeDef

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


# CodeSigningSignatureTypeDef

### inlineDocument
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# CodeSigningTypeDef

### awsSignerJobId
- **Type**: typing.Optional[str]

### startSigningJobParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.StartSigningJobParameterTypeDef]

### customCodeSigning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CustomCodeSigningTypeDef]


# ConfigurationTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# ConfirmTopicRuleDestinationRequestRequestTypeDef

### confirmationToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAuditSuppressionRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### suppressIndefinitely
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# CreateAuthorizerRequestRequestTypeDef

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


# CreateBillingGroupRequestRequestTypeDef

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


# CreateCertificateFromCsrRequestRequestTypeDef

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


# CreateCertificateProviderRequestRequestTypeDef

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


# CreateCustomMetricRequestRequestTypeDef

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


# CreateDimensionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TOPIC_FILTER']
- **Required**: Yes

### stringValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]


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


# CreateDomainConfigurationRequestRequestTypeDef

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


# CreateDynamicThingGroupRequestRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesTypeDef]

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


# CreateFleetMetricRequestRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationType
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AggregationTypeTypeDef'>
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


# CreateJobRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### namespaceId
- **Type**: typing.Optional[str]

### jobTemplateArn
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigTypeDef]

### documentParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### schedulingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SchedulingConfigTypeDef]

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


# CreateJobTemplateRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigTypeDef]

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


# CreateKeysAndCertificateRequestRequestTypeDef

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


# CreateMitigationActionRequestRequestTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionParams
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsTypeDef'>
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


# CreateOTAUpdateRequestRequestTypeDef

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### files
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.OTAUpdateFileTypeDef]
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


# CreatePackageRequestRequestTypeDef

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


# CreatePackageVersionRequestRequestTypeDef

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


# CreatePolicyRequestRequestTypeDef

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


# CreatePolicyVersionRequestRequestTypeDef

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


# CreateProvisioningClaimRequestRequestTypeDef

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


# CreateProvisioningTemplateRequestRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### provisioningRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### preProvisioningHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ProvisioningHookTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]]

### type
- **Type**: typing.Optional[typing.Literal['FLEET_PROVISIONING', 'JITP']]


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


# CreateProvisioningTemplateVersionRequestRequestTypeDef

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


# CreateRoleAliasRequestRequestTypeDef

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


# CreateScheduledAuditRequestRequestTypeDef

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


# CreateSecurityProfileRequestRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: typing.Optional[str]

### behaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.BehaviorTypeDef]]

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


# CreateStreamRequestRequestTypeDef

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


# CreateThingGroupRequestRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### parentGroupName
- **Type**: typing.Optional[str]

### thingGroupProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesTypeDef]

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


# CreateThingRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeName
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AttributePayloadTypeDef]

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


# CreateThingTypeRequestRequestTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesTypeDef]

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


# CreateTopicRuleDestinationRequestRequestTypeDef

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


# CreateTopicRuleRequestRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### topicRulePayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRulePayloadTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[str]


# CustomCodeSigningTypeDef

### signature
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningSignatureTypeDef]

### certificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningCertificateChainTypeDef]

### hashAlgorithm
- **Type**: typing.Optional[str]

### signatureAlgorithm
- **Type**: typing.Optional[str]


# DeleteAccountAuditConfigurationRequestRequestTypeDef

### deleteScheduledAudits
- **Type**: typing.Optional[bool]


# DeleteAuditSuppressionRequestRequestTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes


# DeleteAuthorizerRequestRequestTypeDef

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBillingGroupRequestRequestTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteCACertificateRequestRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateProviderRequestRequestTypeDef

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateRequestRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteCustomMetricRequestRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDimensionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainConfigurationRequestRequestTypeDef

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDynamicThingGroupRequestRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteFleetMetricRequestRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteJobExecutionRequestRequestTypeDef

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


# DeleteJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]

### namespaceId
- **Type**: typing.Optional[str]


# DeleteJobTemplateRequestRequestTypeDef

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMitigationActionRequestRequestTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOTAUpdateRequestRequestTypeDef

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes

### deleteStream
- **Type**: typing.Optional[bool]

### forceDeleteAWSJob
- **Type**: typing.Optional[bool]


# DeletePackageRequestRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePackageVersionRequestRequestTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePolicyRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyVersionRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisioningTemplateRequestRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisioningTemplateVersionRequestRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteRoleAliasRequestRequestTypeDef

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledAuditRequestRequestTypeDef

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSecurityProfileRequestRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteStreamRequestRequestTypeDef

### streamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThingGroupRequestRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteThingRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteThingTypeRequestRequestTypeDef

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRuleDestinationRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRuleRequestRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteV2LoggingLevelRequestRequestTypeDef

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


# DeprecateThingTypeRequestRequestTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot_classes.AuditCheckConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAuditFindingRequestRequestTypeDef

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


# DescribeAuditMitigationActionsTaskRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuditMitigationActionsTaskTargetTypeDef'>
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


# DescribeAuditSuppressionRequestRequestTypeDef

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


# DescribeAuditTaskRequestRequestTypeDef

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


# DescribeAuthorizerRequestRequestTypeDef

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


# DescribeBillingGroupRequestRequestTypeDef

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


# DescribeCACertificateRequestRequestTypeDef

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


# DescribeCertificateProviderRequestRequestTypeDef

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


# DescribeCertificateRequestRequestTypeDef

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


# DescribeCustomMetricRequestRequestTypeDef

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


# DescribeDetectMitigationActionsTaskRequestRequestTypeDef

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


# DescribeDimensionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDimensionResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TOPIC_FILTER']
- **Required**: Yes

### stringValues
- **Type**: typing.List[str]
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


# DescribeDomainConfigurationRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointRequestRequestTypeDef

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


# DescribeFleetMetricRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AggregationTypeTypeDef'>
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


# DescribeIndexRequestRequestTypeDef

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


# DescribeJobExecutionRequestRequestTypeDef

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


# DescribeJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


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


# DescribeJobTemplateRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AbortConfigTypeDef'>
- **Required**: Yes

### timeoutConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef'>
- **Required**: Yes

### jobExecutionsRetryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigTypeDef'>
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


# DescribeManagedJobTemplateRequestRequestTypeDef

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


# DescribeMitigationActionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsTypeDef'>
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


# DescribeProvisioningTemplateRequestRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProvisioningTemplateResponseTypeDef

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### defaultVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### provisioningRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### preProvisioningHook
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ProvisioningHookTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['FLEET_PROVISIONING', 'JITP']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProvisioningTemplateVersionRequestRequestTypeDef

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


# DescribeRoleAliasRequestRequestTypeDef

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


# DescribeScheduledAuditRequestRequestTypeDef

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


# DescribeSecurityProfileRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.BehaviorTypeDef]
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


# DescribeStreamRequestRequestTypeDef

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


# DescribeThingGroupRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesTypeDef'>
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


# DescribeThingRegistrationTaskRequestRequestTypeDef

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


# DescribeThingRequestRequestTypeDef

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


# DescribeThingTypeRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesTypeDef'>
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


# DetachPolicyRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# DetachPrincipalPolicyRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# DetachSecurityProfileRequestRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachThingPrincipalRequestRequestTypeDef

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


# DetectMitigationActionsTaskSummaryPaginatorTypeDef

### taskId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']]

### taskStartTime
- **Type**: typing.Optional[datetime.datetime]

### taskEndTime
- **Type**: typing.Optional[datetime.datetime]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskTargetTypeDef]

### violationEventOccurrenceRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ViolationEventOccurrenceRangeTypeDef]

### onlyActiveViolationsIncluded
- **Type**: typing.Optional[bool]

### suppressedAlertsIncluded
- **Type**: typing.Optional[bool]

### actionsDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.MitigationActionPaginatorTypeDef]]

### taskStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskStatisticsTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskTargetTypeDef]

### violationEventOccurrenceRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ViolationEventOccurrenceRangeTypeDef]

### onlyActiveViolationsIncluded
- **Type**: typing.Optional[bool]

### suppressedAlertsIncluded
- **Type**: typing.Optional[bool]

### actionsDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.MitigationActionTypeDef]]

### taskStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskStatisticsTypeDef]


# DetectMitigationActionsTaskTargetTypeDef

### violationIds
- **Type**: typing.Optional[typing.List[str]]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorName
- **Type**: typing.Optional[str]


# DisableTopicRuleRequestRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


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


# ElasticsearchActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### index
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


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


# EnableTopicRuleRequestRequestTypeDef

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

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Boolean', 'Number', 'String']]


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


# GetBehaviorModelTrainingSummariesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketsAggregationRequestRequestTypeDef

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


# GetCardinalityRequestRequestTypeDef

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


# GetEffectivePoliciesRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingIndexingConfigurationTypeDef'>
- **Required**: Yes

### thingGroupIndexingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupIndexingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobDocumentRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


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


# GetOTAUpdateRequestRequestTypeDef

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


# GetPackageRequestRequestTypeDef

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


# GetPackageVersionRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPercentilesRequestRequestTypeDef

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


# GetPolicyRequestRequestTypeDef

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


# GetPolicyVersionRequestRequestTypeDef

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


# GetStatisticsRequestRequestTypeDef

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


# GetTopicRuleDestinationRequestRequestTypeDef

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


# GetTopicRuleRequestRequestTypeDef

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


# IndexingFilterTypeDef

### namedShadowNames
- **Type**: typing.Optional[typing.List[str]]

### geoLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.GeoLocationTargetTypeDef]]


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


# IotSiteWiseActionTypeDef

### putAssetPropertyValueEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.PutAssetPropertyValueEntryTypeDef]
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


# JobExecutionsRetryConfigTypeDef

### criteriaList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.RetryCriteriaTypeDef]
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigTypeDef]

### documentParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### isConcurrent
- **Type**: typing.Optional[bool]

### schedulingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.SchedulingConfigTypeDef]

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


# ListActiveViolationsRequestListActiveViolationsPaginateTypeDef

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


# ListActiveViolationsRequestRequestTypeDef

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


# ListActiveViolationsResponsePaginatorTypeDef

### activeViolations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ActiveViolationPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListActiveViolationsResponseTypeDef

### activeViolations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ActiveViolationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef

### target
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAttachedPoliciesRequestRequestTypeDef

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


# ListAuditFindingsRequestListAuditFindingsPaginateTypeDef

### taskId
- **Type**: typing.Optional[str]

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### listSuppressedFindings
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditFindingsRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### listSuppressedFindings
- **Type**: typing.Optional[bool]


# ListAuditFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.AuditFindingTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef

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


# ListAuditMitigationActionsExecutionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### auditTaskId
- **Type**: typing.Optional[str]

### findingId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditMitigationActionsTasksRequestRequestTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAuditSuppressionsRequestListAuditSuppressionsPaginateTypeDef

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditSuppressionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAuditTasksRequestListAuditTasksPaginateTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### taskType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_AUDIT_TASK', 'SCHEDULED_AUDIT_TASK']]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuditTasksRequestRequestTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAuthorizersRequestListAuthorizersPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListAuthorizersRequestRequestTypeDef

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


# ListBillingGroupsRequestListBillingGroupsPaginateTypeDef

### namePrefixFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListBillingGroupsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCACertificatesRequestListCACertificatesPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### templateName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCACertificatesRequestRequestTypeDef

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


# ListCertificateProvidersRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListCertificateProvidersResponseTypeDef

### certificateProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.CertificateProviderSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCertificatesByCARequestListCertificatesByCAPaginateTypeDef

### caCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCertificatesByCARequestRequestTypeDef

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


# ListCertificatesRequestListCertificatesPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCertificatesRequestRequestTypeDef

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


# ListCustomMetricsRequestListCustomMetricsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListCustomMetricsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCustomMetricsResponseTypeDef

### metricNames
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDetectMitigationActionsExecutionsRequestListDetectMitigationActionsExecutionsPaginateTypeDef

### taskId
- **Type**: typing.Optional[str]

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDetectMitigationActionsExecutionsRequestRequestTypeDef

### taskId
- **Type**: typing.Optional[str]

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsExecutionsResponseTypeDef

### actionsExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionExecutionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDetectMitigationActionsTasksRequestRequestTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsTasksResponsePaginatorTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskSummaryPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDetectMitigationActionsTasksResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDimensionsRequestListDimensionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDimensionsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDimensionsResponseTypeDef

### dimensionNames
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainConfigurationsRequestListDomainConfigurationsPaginateTypeDef

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListDomainConfigurationsRequestRequestTypeDef

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


# ListFleetMetricsRequestListFleetMetricsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListFleetMetricsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFleetMetricsResponseTypeDef

### fleetMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.FleetMetricNameAndArnTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIndicesRequestListIndicesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListIndicesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIndicesResponseTypeDef

### indexNames
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListJobExecutionsForJobRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef

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


# ListJobExecutionsForThingRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobTemplatesRequestListJobTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListJobTemplatesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesResponseTypeDef

### jobTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.JobTemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsRequestListJobsPaginateTypeDef

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


# ListJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedJobTemplatesRequestListManagedJobTemplatesPaginateTypeDef

### templateName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListManagedJobTemplatesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricValuesRequestListMetricValuesPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### dimensionName
- **Type**: typing.Optional[str]

### dimensionValueOperator
- **Type**: typing.Optional[typing.Literal['IN', 'NOT_IN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListMetricValuesRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### dimensionName
- **Type**: typing.Optional[str]

### dimensionValueOperator
- **Type**: typing.Optional[typing.Literal['IN', 'NOT_IN']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMetricValuesResponsePaginatorTypeDef

### metricDatumList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MetricDatumPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricValuesResponseTypeDef

### metricDatumList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.MetricDatumTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMitigationActionsRequestListMitigationActionsPaginateTypeDef

### actionType
- **Type**: typing.Optional[typing.Literal['ADD_THINGS_TO_THING_GROUP', 'ENABLE_IOT_LOGGING', 'PUBLISH_FINDING_TO_SNS', 'REPLACE_DEFAULT_POLICY_VERSION', 'UPDATE_CA_CERTIFICATE', 'UPDATE_DEVICE_CERTIFICATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListMitigationActionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOTAUpdatesRequestListOTAUpdatesPaginateTypeDef

### otaUpdateStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListOTAUpdatesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOutgoingCertificatesRequestListOutgoingCertificatesPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListOutgoingCertificatesRequestRequestTypeDef

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


# ListPackageVersionsRequestListPackageVersionsPaginateTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPackageVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackagesRequestListPackagesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPackagesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPackagesResponseTypeDef

### packageSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.PackageSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPoliciesRequestListPoliciesPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPoliciesRequestRequestTypeDef

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


# ListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPolicyPrincipalsRequestRequestTypeDef

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


# ListPolicyVersionsRequestRequestTypeDef

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


# ListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPrincipalPoliciesRequestRequestTypeDef

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


# ListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListPrincipalThingsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListProvisioningTemplateVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisioningTemplatesRequestListProvisioningTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListProvisioningTemplatesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplatesResponseTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ProvisioningTemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListRelatedResourcesForAuditFindingRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoleAliasesRequestListRoleAliasesPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListRoleAliasesRequestRequestTypeDef

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


# ListScheduledAuditsRequestListScheduledAuditsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListScheduledAuditsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListScheduledAuditsResponseTypeDef

### scheduledAudits
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ScheduledAuditMetadataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListSecurityProfilesForTargetRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef

### dimensionName
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListSecurityProfilesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamsRequestListStreamsPaginateTypeDef

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListStreamsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.TagTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTargetsForPolicyRequestRequestTypeDef

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


# ListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTargetsForSecurityProfileRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingGroupsForThingRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingGroupsRequestListThingGroupsPaginateTypeDef

### parentGroup
- **Type**: typing.Optional[str]

### namePrefixFilter
- **Type**: typing.Optional[str]

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingGroupsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingPrincipalsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### reportType
- **Type**: typing.Literal['ERRORS', 'RESULTS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingRegistrationTaskReportsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingRegistrationTasksRequestListThingRegistrationTasksPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Completed', 'Failed', 'InProgress']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingRegistrationTasksRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingTypesRequestListThingTypesPaginateTypeDef

### thingTypeName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingTypesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### thingTypeName
- **Type**: typing.Optional[str]


# ListThingTypesResponsePaginatorTypeDef

### thingTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingTypeDefinitionPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingTypesResponseTypeDef

### thingTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingTypeDefinitionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingsInBillingGroupRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListThingsInThingGroupRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThingsRequestListThingsPaginateTypeDef

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


# ListThingsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTopicRuleDestinationsRequestListTopicRuleDestinationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTopicRuleDestinationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTopicRuleDestinationsResponseTypeDef

### destinationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.TopicRuleDestinationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTopicRulesRequestListTopicRulesPaginateTypeDef

### topic
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListTopicRulesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListV2LoggingLevelsRequestListV2LoggingLevelsPaginateTypeDef

### targetType
- **Type**: typing.Optional[typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.PaginatorConfigTypeDef]


# ListV2LoggingLevelsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListViolationEventsRequestListViolationEventsPaginateTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
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


# ListViolationEventsRequestRequestTypeDef

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
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


# ListViolationEventsResponsePaginatorTypeDef

### violationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ViolationEventPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListViolationEventsResponseTypeDef

### violationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ViolationEventTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# MetricDatumPaginatorTypeDef

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValuePaginatorTypeDef]


# MetricDatumTypeDef

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueTypeDef]


# MetricDimensionTypeDef

### dimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Optional[typing.Literal['IN', 'NOT_IN']]


# MetricToRetainTypeDef

### metric
- **Type**: <class 'str'>
- **Required**: Yes

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricDimensionTypeDef]

### exportMetric
- **Type**: typing.Optional[bool]


# MetricValuePaginatorTypeDef

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


# MitigationActionPaginatorTypeDef

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### actionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsPaginatorTypeDef]


# MitigationActionParamsPaginatorTypeDef

### updateDeviceCertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.UpdateDeviceCertificateParamsTypeDef]

### updateCACertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.UpdateCACertificateParamsTypeDef]

### addThingsToThingGroupParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AddThingsToThingGroupParamsPaginatorTypeDef]

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


# MitigationActionTypeDef

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### actionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsTypeDef]


# MqttContextTypeDef

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### clientId
- **Type**: typing.Optional[str]


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


# NonCompliantResourceTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SETTINGS', 'CA_CERTIFICATE', 'CLIENT_ID', 'COGNITO_IDENTITY_POOL', 'DEVICE_CERTIFICATE', 'IAM_ROLE', 'IOT_POLICY', 'ISSUER_CERTIFICATE', 'ROLE_ALIAS']]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef]

### additionalInfo
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.CodeSigningTypeDef]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.OTAUpdateFileTypeDef]]

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


# OpenSearchActionTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### index
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


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


# ProvisioningHookTypeDef

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### payloadVersion
- **Type**: typing.Optional[str]


# ProvisioningTemplateSummaryTypeDef

### templateArn
- **Type**: typing.Optional[str]

### templateName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### enabled
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[typing.Literal['FLEET_PROVISIONING', 'JITP']]


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


# PutItemInputTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# PutVerificationStateOnViolationRequestRequestTypeDef

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


# RegisterCACertificateRequestRequestTypeDef

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


# RegisterCertificateRequestRequestTypeDef

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


# RegisterCertificateWithoutCARequestRequestTypeDef

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


# RegisterThingRequestRequestTypeDef

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


# RejectCertificateTransferRequestRequestTypeDef

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


# RemoveThingFromBillingGroupRequestRequestTypeDef

### billingGroupName
- **Type**: typing.Optional[str]

### billingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# RemoveThingFromThingGroupRequestRequestTypeDef

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


# ReplaceTopicRuleRequestRequestTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### topicRulePayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.TopicRulePayloadTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MqttHeadersTypeDef]


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


# SchedulingConfigTypeDef

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]

### endBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL', 'FORCE_CANCEL', 'STOP_ROLLOUT']]

### maintenanceWindows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.MaintenanceWindowTypeDef]]


# SearchIndexRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingDocumentTypeDef]
- **Required**: Yes

### thingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.ThingGroupDocumentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ServerCertificateSummaryTypeDef

### serverCertificateArn
- **Type**: typing.Optional[str]

### serverCertificateStatus
- **Type**: typing.Optional[typing.Literal['INVALID', 'VALID']]

### serverCertificateStatusDetail
- **Type**: typing.Optional[str]


# SetDefaultAuthorizerRequestRequestTypeDef

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


# SetDefaultPolicyVersionRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# SetLoggingOptionsRequestRequestTypeDef

### loggingOptionsPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.LoggingOptionsPayloadTypeDef'>
- **Required**: Yes


# SetV2LoggingLevelRequestRequestTypeDef

### logTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.LogTargetTypeDef'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# SetV2LoggingOptionsRequestRequestTypeDef

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


# StartAuditMitigationActionsTaskRequestRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.AuditMitigationActionsTaskTargetTypeDef'>
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


# StartDetectMitigationActionsTaskRequestRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.DetectMitigationActionsTaskTargetTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### violationEventOccurrenceRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ViolationEventOccurrenceRangeTypeDef]

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


# StartOnDemandAuditTaskRequestRequestTypeDef

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


# StartThingRegistrationTaskRequestRequestTypeDef

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

### count
- **Type**: typing.Optional[int]

### average
- **Type**: typing.Optional[float]

### sum
- **Type**: typing.Optional[float]

### minimum
- **Type**: typing.Optional[float]

### maximum
- **Type**: typing.Optional[float]

### sumOfSquares
- **Type**: typing.Optional[float]

### variance
- **Type**: typing.Optional[float]

### stdDeviation
- **Type**: typing.Optional[float]


# StepFunctionsActionTypeDef

### stateMachineName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionNamePrefix
- **Type**: typing.Optional[str]


# StopThingRegistrationTaskRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# TestAuthorizationRequestRequestTypeDef

### authInfos
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.AuthInfoTypeDef]
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


# TestInvokeAuthorizerRequestRequestTypeDef

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


# ThingGroupIndexingConfigurationTypeDef

### thingGroupIndexingMode
- **Type**: typing.Literal['OFF', 'ON']
- **Required**: Yes

### managedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]

### customFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]


# ThingGroupMetadataTypeDef

### parentGroupName
- **Type**: typing.Optional[str]

### rootToParentThingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.GroupNameAndArnTypeDef]]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# ThingGroupPropertiesTypeDef

### thingGroupDescription
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AttributePayloadTypeDef]


# ThingIndexingConfigurationTypeDef

### thingIndexingMode
- **Type**: typing.Literal['OFF', 'REGISTRY', 'REGISTRY_AND_SHADOW']
- **Required**: Yes

### thingConnectivityIndexingMode
- **Type**: typing.Optional[typing.Literal['OFF', 'STATUS']]

### deviceDefenderIndexingMode
- **Type**: typing.Optional[typing.Literal['OFF', 'VIOLATIONS']]

### namedShadowIndexingMode
- **Type**: typing.Optional[typing.Literal['OFF', 'ON']]

### managedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]

### customFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.FieldTypeDef]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.IndexingFilterTypeDef]


# ThingTypeDefinitionPaginatorTypeDef

### thingTypeName
- **Type**: typing.Optional[str]

### thingTypeArn
- **Type**: typing.Optional[str]

### thingTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesPaginatorTypeDef]

### thingTypeMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypeMetadataTypeDef]


# ThingTypeDefinitionTypeDef

### thingTypeName
- **Type**: typing.Optional[str]

### thingTypeArn
- **Type**: typing.Optional[str]

### thingTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypePropertiesTypeDef]

### thingTypeMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingTypeMetadataTypeDef]


# ThingTypeMetadataTypeDef

### deprecated
- **Type**: typing.Optional[bool]

### deprecationDate
- **Type**: typing.Optional[datetime.datetime]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# ThingTypePropertiesPaginatorTypeDef

### thingTypeDescription
- **Type**: typing.Optional[str]

### searchableAttributes
- **Type**: typing.Optional[typing.List[str]]


# ThingTypePropertiesTypeDef

### thingTypeDescription
- **Type**: typing.Optional[str]

### searchableAttributes
- **Type**: typing.Optional[typing.Sequence[str]]


# TimeoutConfigTypeDef

### inProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.ActionTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]

### awsIotSqlVersion
- **Type**: typing.Optional[str]

### errorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ActionTypeDef]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_classes.ActionTypeDef]]

### ruleDisabled
- **Type**: typing.Optional[bool]

### awsIotSqlVersion
- **Type**: typing.Optional[str]

### errorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ActionTypeDef]


# TransferCertificateRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountAuditConfigurationRequestRequestTypeDef

### roleArn
- **Type**: typing.Optional[str]

### auditNotificationTargetConfigurations
- **Type**: typing.Optional[typing.Mapping[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot_classes.AuditNotificationTargetTypeDef]]

### auditCheckConfigurations
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iot_classes.AuditCheckConfigurationTypeDef]]


# UpdateAuditSuppressionRequestRequestTypeDef

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ResourceIdentifierTypeDef'>
- **Required**: Yes

### expirationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### suppressIndefinitely
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# UpdateAuthorizerRequestRequestTypeDef

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


# UpdateBillingGroupRequestRequestTypeDef

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


# UpdateCACertificateRequestRequestTypeDef

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


# UpdateCertificateProviderRequestRequestTypeDef

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


# UpdateCertificateRequestRequestTypeDef

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### newStatus
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']
- **Required**: Yes


# UpdateCustomMetricRequestRequestTypeDef

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


# UpdateDimensionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stringValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDimensionResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TOPIC_FILTER']
- **Required**: Yes

### stringValues
- **Type**: typing.List[str]
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


# UpdateDomainConfigurationRequestRequestTypeDef

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


# UpdateDynamicThingGroupRequestRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesTypeDef'>
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


# UpdateEventConfigurationsRequestRequestTypeDef

### eventConfigurations
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CA_CERTIFICATE', 'CERTIFICATE', 'JOB', 'JOB_EXECUTION', 'POLICY', 'THING', 'THING_GROUP', 'THING_GROUP_HIERARCHY', 'THING_GROUP_MEMBERSHIP', 'THING_TYPE', 'THING_TYPE_ASSOCIATION'], aws_resource_validator.pydantic_models.iot_classes.ConfigurationTypeDef]]


# UpdateFleetMetricRequestRequestTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: typing.Optional[str]

### aggregationType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AggregationTypeTypeDef]

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


# UpdateIndexingConfigurationRequestRequestTypeDef

### thingIndexingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingIndexingConfigurationTypeDef]

### thingGroupIndexingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.ThingGroupIndexingConfigurationTypeDef]


# UpdateJobRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AbortConfigTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.TimeoutConfigTypeDef]

### namespaceId
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.JobExecutionsRetryConfigTypeDef]


# UpdateMitigationActionRequestRequestTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### actionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MitigationActionParamsTypeDef]


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


# UpdatePackageConfigurationRequestRequestTypeDef

### versionUpdateByJobsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.VersionUpdateByJobsConfigTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# UpdatePackageRequestRequestTypeDef

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


# UpdatePackageVersionRequestRequestTypeDef

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

### action
- **Type**: typing.Optional[typing.Literal['DEPRECATE', 'PUBLISH']]

### clientToken
- **Type**: typing.Optional[str]


# UpdateProvisioningTemplateRequestRequestTypeDef

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


# UpdateRoleAliasRequestRequestTypeDef

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


# UpdateScheduledAuditRequestRequestTypeDef

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


# UpdateSecurityProfileRequestRequestTypeDef

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: typing.Optional[str]

### behaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.BehaviorTypeDef]]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_classes.BehaviorTypeDef]
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


# UpdateStreamRequestRequestTypeDef

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


# UpdateThingGroupRequestRequestTypeDef

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_classes.ThingGroupPropertiesTypeDef'>
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


# UpdateThingGroupsForThingRequestRequestTypeDef

### thingName
- **Type**: typing.Optional[str]

### thingGroupsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### thingGroupsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# UpdateThingRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeName
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.AttributePayloadTypeDef]

### expectedVersion
- **Type**: typing.Optional[int]

### removeThingType
- **Type**: typing.Optional[bool]


# UpdateTopicRuleDestinationRequestRequestTypeDef

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


# ValidateSecurityProfileBehaviorsRequestRequestTypeDef

### behaviors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iot_classes.BehaviorTypeDef]
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


# ViolationEventOccurrenceRangeTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ViolationEventPaginatorTypeDef

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorPaginatorTypeDef]

### metricValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValuePaginatorTypeDef]

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


# ViolationEventTypeDef

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.BehaviorTypeDef]

### metricValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_classes.MetricValueTypeDef]

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


