# Iot Classes

# AbortConfig

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AbortCriteria]
- **Required**: Yes


# AbortConfigOutput

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AbortCriteria]
- **Required**: Yes


# AbortCriteria

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


# AcceptCertificateTransferRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### setAsActive
- **Type**: typing.Optional[bool]


# Action

### dynamoDB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.DynamoDBAction]

### dynamoDBv2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.DynamoDBv2Action]

### lambda_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.LambdaAction]

### sns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SnsAction]

### sqs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SqsAction]

### kinesis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.KinesisAction]

### republish
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.RepublishAction, aws_resource_validator.pydantic_models.iot.iot_classes.RepublishActionOutput, NoneType]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.S3Action]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.FirehoseAction]

### cloudwatchMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CloudwatchMetricAction]

### cloudwatchAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CloudwatchAlarmAction]

### cloudwatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CloudwatchLogsAction]

### elasticsearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ElasticsearchAction]

### salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SalesforceAction]

### iotAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IotAnalyticsAction]

### iotEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IotEventsAction]

### iotSiteWise
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.IotSiteWiseAction, aws_resource_validator.pydantic_models.iot.iot_classes.IotSiteWiseActionOutput, NoneType]

### stepFunctions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.StepFunctionsAction]

### timestream
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.TimestreamAction, aws_resource_validator.pydantic_models.iot.iot_classes.TimestreamActionOutput, NoneType]

### http
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.HttpAction, aws_resource_validator.pydantic_models.iot.iot_classes.HttpActionOutput, NoneType]

### kafka
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.KafkaAction, aws_resource_validator.pydantic_models.iot.iot_classes.KafkaActionOutput, NoneType]

### openSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.OpenSearchAction]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.LocationAction]


# ActionOutput

### dynamoDB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.DynamoDBAction]

### dynamoDBv2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.DynamoDBv2Action]

### lambda_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.LambdaAction]

### sns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SnsAction]

### sqs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SqsAction]

### kinesis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.KinesisAction]

### republish
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.RepublishActionOutput]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.S3Action]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.FirehoseAction]

### cloudwatchMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CloudwatchMetricAction]

### cloudwatchAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CloudwatchAlarmAction]

### cloudwatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CloudwatchLogsAction]

### elasticsearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ElasticsearchAction]

### salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SalesforceAction]

### iotAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IotAnalyticsAction]

### iotEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IotEventsAction]

### iotSiteWise
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IotSiteWiseActionOutput]

### stepFunctions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.StepFunctionsAction]

### timestream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimestreamActionOutput]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.HttpActionOutput]

### kafka
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.KafkaActionOutput]

### openSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.OpenSearchAction]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.LocationAction]


# ActiveViolation

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorOutput]

### lastViolationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricValueOutput]

### violationEventAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ViolationEventAdditionalInfo]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### verificationStateDescription
- **Type**: typing.Optional[str]

### lastViolationTime
- **Type**: typing.Optional[datetime.datetime]

### violationStartTime
- **Type**: typing.Optional[datetime.datetime]


# AddThingToBillingGroupRequest

### billingGroupName
- **Type**: typing.Optional[str]

### billingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# AddThingToThingGroupRequest

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


# AddThingsToThingGroupParams

### thingGroupNames
- **Type**: typing.List[str]
- **Required**: Yes

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# AddThingsToThingGroupParamsOutput

### thingGroupNames
- **Type**: typing.List[str]
- **Required**: Yes

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# AggregationType

### name
- **Type**: typing.Literal['Cardinality', 'Percentiles', 'Statistics']
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.List[str]]


# AggregationTypeOutput

### name
- **Type**: typing.Literal['Cardinality', 'Percentiles', 'Statistics']
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.List[str]]


# AlertTarget

### alertTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# Allowed

### policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Policy]]


# AssetPropertyTimestamp

### timeInSeconds
- **Type**: <class 'str'>
- **Required**: Yes

### offsetInNanos
- **Type**: typing.Optional[str]


# AssetPropertyValue

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AssetPropertyVariant'>
- **Required**: Yes

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AssetPropertyTimestamp'>
- **Required**: Yes

### quality
- **Type**: typing.Optional[str]


# AssetPropertyVariant

### stringValue
- **Type**: typing.Optional[str]

### integerValue
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[str]

### booleanValue
- **Type**: typing.Optional[str]


# AssociateSbomWithPackageVersionRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### sbom
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.Sbom'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AssociateSbomWithPackageVersionResponse

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### sbom
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.Sbom'>
- **Required**: Yes

### sbomValidationStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateTargetsWithJobRequest

### targets
- **Type**: typing.List[str]
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: typing.Optional[str]

### namespaceId
- **Type**: typing.Optional[str]


# AssociateTargetsWithJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# AttachPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# AttachPrincipalPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# AttachSecurityProfileRequest

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachThingPrincipalRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# AttributePayload

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### merge
- **Type**: typing.Optional[bool]


# AttributePayloadOutput

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### merge
- **Type**: typing.Optional[bool]


# AuditCheckConfiguration

### enabled
- **Type**: typing.Optional[bool]

### configuration
- **Type**: typing.Optional[typing.Dict[typing.Literal['CERT_AGE_THRESHOLD_IN_DAYS', 'CERT_EXPIRATION_THRESHOLD_IN_DAYS'], str]]


# AuditCheckConfigurationOutput

### enabled
- **Type**: typing.Optional[bool]

### configuration
- **Type**: typing.Optional[typing.Dict[typing.Literal['CERT_AGE_THRESHOLD_IN_DAYS', 'CERT_EXPIRATION_THRESHOLD_IN_DAYS'], str]]


# AuditCheckDetails

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


# AuditFinding

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.NonCompliantResource]

### relatedResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.RelatedResource]]

### reasonForNonCompliance
- **Type**: typing.Optional[str]

### reasonForNonComplianceCode
- **Type**: typing.Optional[str]

### isSuppressed
- **Type**: typing.Optional[bool]


# AuditMitigationActionExecutionMetadata

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


# AuditMitigationActionsTaskMetadata

### taskId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]


# AuditMitigationActionsTaskTarget

### auditTaskId
- **Type**: typing.Optional[str]

### findingIds
- **Type**: typing.Optional[typing.List[str]]

### auditCheckToReasonCodeFilter
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# AuditMitigationActionsTaskTargetOutput

### auditTaskId
- **Type**: typing.Optional[str]

### findingIds
- **Type**: typing.Optional[typing.List[str]]

### auditCheckToReasonCodeFilter
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# AuditNotificationTarget

### targetArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]


# AuditSuppression

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier'>
- **Required**: Yes

### expirationDate
- **Type**: typing.Optional[datetime.datetime]

### suppressIndefinitely
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# AuditTaskMetadata

### taskId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### taskType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_AUDIT_TASK', 'SCHEDULED_AUDIT_TASK']]


# AuthInfo

### resources
- **Type**: typing.List[str]
- **Required**: Yes

### actionType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'PUBLISH', 'RECEIVE', 'SUBSCRIBE']]


# AuthInfoOutput

### resources
- **Type**: typing.List[str]
- **Required**: Yes

### actionType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'PUBLISH', 'RECEIVE', 'SUBSCRIBE']]


# AuthResult

### authInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AuthInfoOutput]

### allowed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.Allowed]

### denied
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.Denied]

### authDecision
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'EXPLICIT_DENY', 'IMPLICIT_DENY']]

### missingContextValues
- **Type**: typing.Optional[typing.List[str]]


# AuthorizerConfig

### defaultAuthorizerName
- **Type**: typing.Optional[str]

### allowAuthorizerOverride
- **Type**: typing.Optional[bool]


# AuthorizerDescription

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


# AuthorizerSummary

### authorizerName
- **Type**: typing.Optional[str]

### authorizerArn
- **Type**: typing.Optional[str]


# AwsJobAbortConfig

### abortCriteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobAbortCriteria]
- **Required**: Yes


# AwsJobAbortCriteria

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


# AwsJobExecutionsRolloutConfig

### maximumPerMinute
- **Type**: typing.Optional[int]

### exponentialRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobExponentialRolloutRate]


# AwsJobExponentialRolloutRate

### baseRatePerMinute
- **Type**: <class 'int'>
- **Required**: Yes

### incrementFactor
- **Type**: <class 'float'>
- **Required**: Yes

### rateIncreaseCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobRateIncreaseCriteria'>
- **Required**: Yes


# AwsJobPresignedUrlConfig

### expiresInSec
- **Type**: typing.Optional[int]


# AwsJobRateIncreaseCriteria

### numberOfNotifiedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]


# AwsJobTimeoutConfig

### inProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Behavior

### name
- **Type**: <class 'str'>
- **Required**: Yes

### metric
- **Type**: typing.Optional[str]

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricDimension]

### criteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorCriteria, aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorCriteriaOutput, NoneType]

### suppressAlerts
- **Type**: typing.Optional[bool]

### exportMetric
- **Type**: typing.Optional[bool]


# BehaviorCriteria

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['greater-than', 'greater-than-equals', 'in-cidr-set', 'in-port-set', 'in-set', 'less-than', 'less-than-equals', 'not-in-cidr-set', 'not-in-port-set', 'not-in-set']]

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.MetricValue, aws_resource_validator.pydantic_models.iot.iot_classes.MetricValueOutput, NoneType]

### durationSeconds
- **Type**: typing.Optional[int]

### consecutiveDatapointsToAlarm
- **Type**: typing.Optional[int]

### consecutiveDatapointsToClear
- **Type**: typing.Optional[int]

### statisticalThreshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.StatisticalThreshold]

### mlDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MachineLearningDetectionConfig]


# BehaviorCriteriaOutput

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['greater-than', 'greater-than-equals', 'in-cidr-set', 'in-port-set', 'in-set', 'less-than', 'less-than-equals', 'not-in-cidr-set', 'not-in-port-set', 'not-in-set']]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricValueOutput]

### durationSeconds
- **Type**: typing.Optional[int]

### consecutiveDatapointsToAlarm
- **Type**: typing.Optional[int]

### consecutiveDatapointsToClear
- **Type**: typing.Optional[int]

### statisticalThreshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.StatisticalThreshold]

### mlDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MachineLearningDetectionConfig]


# BehaviorModelTrainingSummary

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


# BehaviorOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### metric
- **Type**: typing.Optional[str]

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricDimension]

### criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorCriteriaOutput]

### suppressAlerts
- **Type**: typing.Optional[bool]

### exportMetric
- **Type**: typing.Optional[bool]


# BillingGroupMetadata

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# BillingGroupProperties

### billingGroupDescription
- **Type**: typing.Optional[str]


# Bucket

### keyValue
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]


# BucketsAggregationType

### termsAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TermsAggregation]


# CACertificate

### certificateArn
- **Type**: typing.Optional[str]

### certificateId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# CACertificateDescription

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CertificateValidity]

### certificateMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'SNI_ONLY']]


# CancelAuditMitigationActionsTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelAuditTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelCertificateTransferRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDetectMitigationActionsTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobExecutionRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CancelJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reasonCode
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# CancelJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# Certificate

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


# CertificateDescription

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TransferData]

### generationId
- **Type**: typing.Optional[str]

### validity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CertificateValidity]

### certificateMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'SNI_ONLY']]


# CertificateProviderSummary

### certificateProviderName
- **Type**: typing.Optional[str]

### certificateProviderArn
- **Type**: typing.Optional[str]


# CertificateValidity

### notBefore
- **Type**: typing.Optional[datetime.datetime]

### notAfter
- **Type**: typing.Optional[datetime.datetime]


# ClientCertificateConfig

### clientCertificateCallbackArn
- **Type**: typing.Optional[str]


# CloudwatchAlarmAction

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


# CloudwatchLogsAction

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### batchMode
- **Type**: typing.Optional[bool]


# CloudwatchMetricAction

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


# CodeSigning

### awsSignerJobId
- **Type**: typing.Optional[str]

### startSigningJobParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.StartSigningJobParameter]

### customCodeSigning
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.CustomCodeSigning, aws_resource_validator.pydantic_models.iot.iot_classes.CustomCodeSigningOutput, NoneType]


# CodeSigningCertificateChain

### certificateName
- **Type**: typing.Optional[str]

### inlineDocument
- **Type**: typing.Optional[str]


# CodeSigningOutput

### awsSignerJobId
- **Type**: typing.Optional[str]

### startSigningJobParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.StartSigningJobParameter]

### customCodeSigning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CustomCodeSigningOutput]


# CodeSigningSignature

### inlineDocument
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# CodeSigningSignatureOutput

### inlineDocument
- **Type**: typing.Optional[bytes]


# CommandExecutionResult

### S
- **Type**: typing.Optional[str]

### B
- **Type**: typing.Optional[bool]

### BIN
- **Type**: typing.Optional[bytes]


# CommandExecutionSummary

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


# CommandParameter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterValue, aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterValueOutput, NoneType]

### defaultValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterValue, aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterValueOutput, NoneType]

### description
- **Type**: typing.Optional[str]


# CommandParameterOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterValueOutput]

### defaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterValueOutput]

### description
- **Type**: typing.Optional[str]


# CommandParameterValue

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### UL
- **Type**: typing.Optional[str]


# CommandParameterValueOutput

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


# CommandPayload

### content
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### contentType
- **Type**: typing.Optional[str]


# CommandPayloadOutput

### content
- **Type**: typing.Optional[bytes]

### contentType
- **Type**: typing.Optional[str]


# CommandSummary

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


# Configuration

### Enabled
- **Type**: typing.Optional[bool]


# ConfirmTopicRuleDestinationRequest

### confirmationToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAuditSuppressionRequest

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier'>
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


# CreateAuthorizerRequest

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### tokenKeyName
- **Type**: typing.Optional[str]

### tokenSigningPublicKeys
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]

### signingDisabled
- **Type**: typing.Optional[bool]

### enableCachingForHttp
- **Type**: typing.Optional[bool]


# CreateAuthorizerResponse

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBillingGroupRequest

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.BillingGroupProperties]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateBillingGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCertificateFromCsrRequest

### certificateSigningRequest
- **Type**: <class 'str'>
- **Required**: Yes

### setAsActive
- **Type**: typing.Optional[bool]


# CreateCertificateFromCsrResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCertificateProviderRequest

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### lambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountDefaultForOperations
- **Type**: typing.List[typing.Literal['CreateCertificateFromCsr']]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateCertificateProviderResponse

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCommandRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.CommandPayload, aws_resource_validator.pydantic_models.iot.iot_classes.CommandPayloadOutput, NoneType]

### mandatoryParameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameter, aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterOutput]]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateCommandResponse

### commandId
- **Type**: <class 'str'>
- **Required**: Yes

### commandArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomMetricRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateCustomMetricResponse

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDimensionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TOPIC_FILTER']
- **Required**: Yes

### stringValues
- **Type**: typing.List[str]
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateDimensionResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainConfigurationRequest

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: typing.Optional[str]

### serverCertificateArns
- **Type**: typing.Optional[typing.List[str]]

### validationCertificateArn
- **Type**: typing.Optional[str]

### authorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AuthorizerConfig]

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]

### tlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TlsConfig]

### serverCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ServerCertificateConfig]

### authenticationType
- **Type**: typing.Optional[typing.Literal['AWS_SIGV4', 'AWS_X509', 'CUSTOM_AUTH', 'CUSTOM_AUTH_X509', 'DEFAULT']]

### applicationProtocol
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HTTPS', 'MQTT_WSS', 'SECURE_MQTT']]

### clientCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ClientCertificateConfig]


# CreateDomainConfigurationResponse

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### domainConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDynamicThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupProperties, aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupPropertiesOutput, NoneType]

### indexName
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateDynamicThingGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetMetricRequest

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationType
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AggregationType, aws_resource_validator.pydantic_models.iot.iot_classes.AggregationTypeOutput]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateFleetMetricResponse

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.List[str]
- **Required**: Yes

### documentSource
- **Type**: typing.Optional[str]

### document
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### presignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PresignedUrlConfig]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRolloutConfig]

### abortConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfig, aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfigOutput, NoneType]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeoutConfig]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]

### namespaceId
- **Type**: typing.Optional[str]

### jobTemplateArn
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfig, aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfigOutput, NoneType]

### documentParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### schedulingConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.SchedulingConfig, aws_resource_validator.pydantic_models.iot.iot_classes.SchedulingConfigOutput, NoneType]

### destinationPackageVersions
- **Type**: typing.Optional[typing.List[str]]


# CreateJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobTemplateRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PresignedUrlConfig]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRolloutConfig]

### abortConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfig, aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfigOutput, NoneType]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeoutConfig]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]

### jobExecutionsRetryConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfig, aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfigOutput, NoneType]

### maintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MaintenanceWindow]]

### destinationPackageVersions
- **Type**: typing.Optional[typing.List[str]]


# CreateJobTemplateResponse

### jobTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeysAndCertificateRequest

### setAsActive
- **Type**: typing.Optional[bool]


# CreateKeysAndCertificateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.KeyPair'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMitigationActionRequest

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionParams
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.MitigationActionParams, aws_resource_validator.pydantic_models.iot.iot_classes.MitigationActionParamsOutput]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateMitigationActionResponse

### actionArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOTAUpdateRequest

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.List[str]
- **Required**: Yes

### files
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.OTAUpdateFile, aws_resource_validator.pydantic_models.iot.iot_classes.OTAUpdateFileOutput]]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### protocols
- **Type**: typing.Optional[typing.List[typing.Literal['HTTP', 'MQTT']]]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### awsJobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobExecutionsRolloutConfig]

### awsJobPresignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobPresignedUrlConfig]

### awsJobAbortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobAbortConfig]

### awsJobTimeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobTimeoutConfig]

### additionalParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateOTAUpdateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackageRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreatePackageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackageVersionRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### artifact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PackageVersionArtifact]

### recipe
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreatePackageVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreatePolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyVersionRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### setAsDefault
- **Type**: typing.Optional[bool]


# CreatePolicyVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProvisioningClaimRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateProvisioningClaimResponse

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.KeyPair'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProvisioningTemplateRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ProvisioningHook]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]

### type
- **Type**: typing.Optional[typing.Literal['FLEET_PROVISIONING', 'JITP']]


# CreateProvisioningTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProvisioningTemplateVersionRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### setAsDefault
- **Type**: typing.Optional[bool]


# CreateProvisioningTemplateVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoleAliasRequest

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### credentialDurationSeconds
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateRoleAliasResponse

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScheduledAuditRequest

### frequency
- **Type**: typing.Literal['BIWEEKLY', 'DAILY', 'MONTHLY', 'WEEKLY']
- **Required**: Yes

### targetCheckNames
- **Type**: typing.List[str]
- **Required**: Yes

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes

### dayOfMonth
- **Type**: typing.Optional[str]

### dayOfWeek
- **Type**: typing.Optional[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateScheduledAuditResponse

### scheduledAuditArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityProfileRequest

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: typing.Optional[str]

### behaviors
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.Behavior, aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorOutput]]]

### alertTargets
- **Type**: typing.Optional[typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot.iot_classes.AlertTarget]]

### additionalMetricsToRetain
- **Type**: typing.Optional[typing.List[str]]

### additionalMetricsToRetainV2
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MetricToRetain]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]

### metricsExportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricsExportConfig]


# CreateSecurityProfileResponse

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamRequest

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.StreamFile]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateStreamResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### parentGroupName
- **Type**: typing.Optional[str]

### thingGroupProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupProperties, aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupPropertiesOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateThingGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThingRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeName
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AttributePayload, aws_resource_validator.pydantic_models.iot.iot_classes.AttributePayloadOutput, NoneType]

### billingGroupName
- **Type**: typing.Optional[str]


# CreateThingResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThingTypeRequest

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypeProperties, aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypePropertiesOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]


# CreateThingTypeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTopicRuleDestinationRequest

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TopicRuleDestinationConfiguration'>
- **Required**: Yes


# CreateTopicRuleDestinationResponse

### topicRuleDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TopicRuleDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTopicRuleRequest

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### topicRulePayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TopicRulePayload'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[str]


# CustomCodeSigning

### signature
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigningSignature, aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigningSignatureOutput, NoneType]

### certificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigningCertificateChain]

### hashAlgorithm
- **Type**: typing.Optional[str]

### signatureAlgorithm
- **Type**: typing.Optional[str]


# CustomCodeSigningOutput

### signature
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigningSignatureOutput]

### certificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigningCertificateChain]

### hashAlgorithm
- **Type**: typing.Optional[str]

### signatureAlgorithm
- **Type**: typing.Optional[str]


# DeleteAccountAuditConfigurationRequest

### deleteScheduledAudits
- **Type**: typing.Optional[bool]


# DeleteAuditSuppressionRequest

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier'>
- **Required**: Yes


# DeleteAuthorizerRequest

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBillingGroupRequest

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteCACertificateRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateProviderRequest

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteCommandExecutionRequest

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCommandRequest

### commandId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCommandResponse

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomMetricRequest

### metricName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDimensionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainConfigurationRequest

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDynamicThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteFleetMetricRequest

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteJobExecutionRequest

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


# DeleteJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]

### namespaceId
- **Type**: typing.Optional[str]


# DeleteJobTemplateRequest

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMitigationActionRequest

### actionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOTAUpdateRequest

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes

### deleteStream
- **Type**: typing.Optional[bool]

### forceDeleteAWSJob
- **Type**: typing.Optional[bool]


# DeletePackageRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePackageVersionRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyVersionRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisioningTemplateRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisioningTemplateVersionRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteRoleAliasRequest

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledAuditRequest

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSecurityProfileRequest

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteStreamRequest

### streamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteThingRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# DeleteThingTypeRequest

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRuleDestinationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRuleRequest

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteV2LoggingLevelRequest

### targetType
- **Type**: typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']
- **Required**: Yes

### targetName
- **Type**: <class 'str'>
- **Required**: Yes


# Denied

### implicitDeny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ImplicitDeny]

### explicitDeny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ExplicitDeny]


# DeprecateThingTypeRequest

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### undoDeprecate
- **Type**: typing.Optional[bool]


# DescribeAccountAuditConfigurationResponse

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### auditNotificationTargetConfigurations
- **Type**: typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot.iot_classes.AuditNotificationTarget]
- **Required**: Yes

### auditCheckConfigurations
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot.iot_classes.AuditCheckConfigurationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAuditFindingRequest

### findingId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditFindingResponse

### finding
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AuditFinding'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAuditMitigationActionsTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditMitigationActionsTaskResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot.iot_classes.TaskStatisticsForAuditCheck]
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AuditMitigationActionsTaskTargetOutput'>
- **Required**: Yes

### auditCheckToActionsMapping
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### actionsDefinition
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MitigationAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAuditSuppressionRequest

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier'>
- **Required**: Yes


# DescribeAuditSuppressionResponse

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAuditTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditTaskResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TaskStatistics'>
- **Required**: Yes

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes

### auditDetails
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot.iot_classes.AuditCheckDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAuthorizerRequest

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuthorizerResponse

### authorizerDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AuthorizerDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBillingGroupRequest

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBillingGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.BillingGroupProperties'>
- **Required**: Yes

### billingGroupMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.BillingGroupMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCACertificateRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCACertificateResponse

### certificateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.CACertificateDescription'>
- **Required**: Yes

### registrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.RegistrationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCertificateProviderRequest

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateProviderResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCertificateRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateResponse

### certificateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.CertificateDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomMetricRequest

### metricName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomMetricResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDefaultAuthorizerResponse

### authorizerDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AuthorizerDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDetectMitigationActionsTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDetectMitigationActionsTaskResponse

### taskSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.DetectMitigationActionsTaskSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDimensionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDimensionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainConfigurationRequest

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainConfigurationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ServerCertificateSummary]
- **Required**: Yes

### authorizerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AuthorizerConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TlsConfig'>
- **Required**: Yes

### serverCertificateConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ServerCertificateConfig'>
- **Required**: Yes

### authenticationType
- **Type**: typing.Literal['AWS_SIGV4', 'AWS_X509', 'CUSTOM_AUTH', 'CUSTOM_AUTH_X509', 'DEFAULT']
- **Required**: Yes

### applicationProtocol
- **Type**: typing.Literal['DEFAULT', 'HTTPS', 'MQTT_WSS', 'SECURE_MQTT']
- **Required**: Yes

### clientCertificateConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ClientCertificateConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointRequest

### endpointType
- **Type**: typing.Optional[str]


# DescribeEndpointResponse

### endpointAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventConfigurationsResponse

### eventConfigurations
- **Type**: typing.Dict[typing.Literal['CA_CERTIFICATE', 'CERTIFICATE', 'JOB', 'JOB_EXECUTION', 'POLICY', 'THING', 'THING_GROUP', 'THING_GROUP_HIERARCHY', 'THING_GROUP_MEMBERSHIP', 'THING_TYPE', 'THING_TYPE_ASSOCIATION'], aws_resource_validator.pydantic_models.iot.iot_classes.Configuration]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetMetricRequest

### metricName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetMetricResponse

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationType
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AggregationTypeOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIndexRequest

### indexName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIndexResponse

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### indexStatus
- **Type**: typing.Literal['ACTIVE', 'BUILDING', 'REBUILDING']
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.iot.iot_classes.DescribeIndexResponse'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobExecutionRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### executionNumber
- **Type**: typing.Optional[int]


# DescribeJobExecutionResponse

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.JobExecution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeSubstitution
- **Type**: typing.Optional[bool]


# DescribeJobResponse

### documentSource
- **Type**: <class 'str'>
- **Required**: Yes

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobTemplateRequest

### jobTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.PresignedUrlConfig'>
- **Required**: Yes

### jobExecutionsRolloutConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRolloutConfig'>
- **Required**: Yes

### abortConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfigOutput'>
- **Required**: Yes

### timeoutConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TimeoutConfig'>
- **Required**: Yes

### jobExecutionsRetryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfigOutput'>
- **Required**: Yes

### maintenanceWindows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MaintenanceWindow]
- **Required**: Yes

### destinationPackageVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeManagedJobTemplateRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateVersion
- **Type**: typing.Optional[str]


# DescribeManagedJobTemplateResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.DocumentParameter]
- **Required**: Yes

### document
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMitigationActionRequest

### actionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMitigationActionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.MitigationActionParamsOutput'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProvisioningTemplateRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProvisioningTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ProvisioningHook'>
- **Required**: Yes

### type
- **Type**: typing.Literal['FLEET_PROVISIONING', 'JITP']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProvisioningTemplateVersionRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeProvisioningTemplateVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRoleAliasRequest

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoleAliasResponse

### roleAliasDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.RoleAliasDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeScheduledAuditRequest

### scheduledAuditName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduledAuditResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSecurityProfileRequest

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityProfileResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorOutput]
- **Required**: Yes

### alertTargets
- **Type**: typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot.iot_classes.AlertTarget]
- **Required**: Yes

### additionalMetricsToRetain
- **Type**: typing.List[str]
- **Required**: Yes

### additionalMetricsToRetainV2
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MetricToRetain]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.MetricsExportConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStreamRequest

### streamId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStreamResponse

### streamInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.StreamInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupPropertiesOutput'>
- **Required**: Yes

### thingGroupMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThingRegistrationTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingRegistrationTaskResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThingRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThingTypeRequest

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThingTypeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypePropertiesOutput'>
- **Required**: Yes

### thingTypeMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypeMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.S3Destination]


# DetachPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# DetachPrincipalPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# DetachSecurityProfileRequest

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachThingPrincipalRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# DetectMitigationActionExecution

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


# DetectMitigationActionsTaskStatistics

### actionsExecuted
- **Type**: typing.Optional[int]

### actionsSkipped
- **Type**: typing.Optional[int]

### actionsFailed
- **Type**: typing.Optional[int]


# DetectMitigationActionsTaskSummary

### taskId
- **Type**: typing.Optional[str]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUCCESSFUL']]

### taskStartTime
- **Type**: typing.Optional[datetime.datetime]

### taskEndTime
- **Type**: typing.Optional[datetime.datetime]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.DetectMitigationActionsTaskTargetOutput]

### violationEventOccurrenceRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ViolationEventOccurrenceRangeOutput]

### onlyActiveViolationsIncluded
- **Type**: typing.Optional[bool]

### suppressedAlertsIncluded
- **Type**: typing.Optional[bool]

### actionsDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MitigationAction]]

### taskStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.DetectMitigationActionsTaskStatistics]


# DetectMitigationActionsTaskTarget

### violationIds
- **Type**: typing.Optional[typing.List[str]]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorName
- **Type**: typing.Optional[str]


# DetectMitigationActionsTaskTargetOutput

### violationIds
- **Type**: typing.Optional[typing.List[str]]

### securityProfileName
- **Type**: typing.Optional[str]

### behaviorName
- **Type**: typing.Optional[str]


# DisableTopicRuleRequest

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSbomFromPackageVersionRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DocumentParameter

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


# DomainConfigurationSummary

### domainConfigurationName
- **Type**: typing.Optional[str]

### domainConfigurationArn
- **Type**: typing.Optional[str]

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]


# DynamoDBAction

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


# DynamoDBv2Action

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### putItem
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.PutItemInput'>
- **Required**: Yes


# EffectivePolicy

### policyName
- **Type**: typing.Optional[str]

### policyArn
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]


# ElasticsearchAction

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# EnableIoTLoggingParams

### roleArnForLogging
- **Type**: <class 'str'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# EnableTopicRuleRequest

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorInfo

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ExplicitDeny

### policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Policy]]


# ExponentialRolloutRate

### baseRatePerMinute
- **Type**: <class 'int'>
- **Required**: Yes

### incrementFactor
- **Type**: <class 'float'>
- **Required**: Yes

### rateIncreaseCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.RateIncreaseCriteria'>
- **Required**: Yes


# Field

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Boolean', 'Number', 'String']]


# FileLocation

### stream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.Stream]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.S3Location]


# FirehoseAction

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


# FleetMetricNameAndArn

### metricName
- **Type**: typing.Optional[str]

### metricArn
- **Type**: typing.Optional[str]


# GeoLocationTarget

### name
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[typing.Literal['LatLon', 'LonLat']]


# GetBehaviorModelTrainingSummariesRequest

### securityProfileName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetBehaviorModelTrainingSummariesRequestPaginate

### securityProfileName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# GetBehaviorModelTrainingSummariesResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorModelTrainingSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBucketsAggregationRequest

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationField
- **Type**: <class 'str'>
- **Required**: Yes

### bucketsAggregationType
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.BucketsAggregationType'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# GetBucketsAggregationResponse

### totalCount
- **Type**: <class 'int'>
- **Required**: Yes

### buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Bucket]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetCardinalityRequest

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### aggregationField
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# GetCardinalityResponse

### cardinality
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetCommandExecutionRequest

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### includeResult
- **Type**: typing.Optional[bool]


# GetCommandExecutionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.StatusReason'>
- **Required**: Yes

### result
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot.iot_classes.CommandExecutionResult]
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterValueOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetCommandRequest

### commandId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommandResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.CommandParameterOutput]
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.CommandPayloadOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetEffectivePoliciesRequest

### principal
- **Type**: typing.Optional[str]

### cognitoIdentityPoolId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]


# GetEffectivePoliciesResponse

### effectivePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.EffectivePolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetIndexingConfigurationResponse

### thingIndexingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ThingIndexingConfigurationOutput'>
- **Required**: Yes

### thingGroupIndexingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupIndexingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobDocumentRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeSubstitution
- **Type**: typing.Optional[bool]


# GetJobDocumentResponse

### document
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoggingOptionsResponse

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetOTAUpdateRequest

### otaUpdateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOTAUpdateResponse

### otaUpdateInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.OTAUpdateInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetPackageConfigurationResponse

### versionUpdateByJobsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.VersionUpdateByJobsConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetPackageRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPackageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetPackageVersionRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPackageVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.PackageVersionArtifact'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.Sbom'>
- **Required**: Yes

### sbomValidationStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### recipe
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetPercentilesRequest

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
- **Type**: typing.Optional[typing.List[float]]


# GetPercentilesResponse

### percentiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PercentPair]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyVersionRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegistrationCodeResponse

### registrationCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetStatisticsRequest

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: typing.Optional[str]

### aggregationField
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# GetStatisticsResponse

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.Statistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetThingConnectivityDataRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetThingConnectivityDataResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetTopicRuleDestinationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTopicRuleDestinationResponse

### topicRuleDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TopicRuleDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetTopicRuleRequest

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTopicRuleResponse

### ruleArn
- **Type**: <class 'str'>
- **Required**: Yes

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TopicRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GetV2LoggingOptionsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# GroupNameAndArn

### groupName
- **Type**: typing.Optional[str]

### groupArn
- **Type**: typing.Optional[str]


# HttpAction

### url
- **Type**: <class 'str'>
- **Required**: Yes

### confirmationUrl
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.HttpActionHeader]]

### auth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.HttpAuthorization]


# HttpActionHeader

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# HttpActionOutput

### url
- **Type**: <class 'str'>
- **Required**: Yes

### confirmationUrl
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.HttpActionHeader]]

### auth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.HttpAuthorization]


# HttpAuthorization

### sigv4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SigV4Authorization]


# HttpContext

### headers
- **Type**: typing.Optional[typing.Dict[str, str]]

### queryString
- **Type**: typing.Optional[str]


# HttpUrlDestinationConfiguration

### confirmationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# HttpUrlDestinationProperties

### confirmationUrl
- **Type**: typing.Optional[str]


# HttpUrlDestinationSummary

### confirmationUrl
- **Type**: typing.Optional[str]


# ImplicitDeny

### policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Policy]]


# IndexingFilter

### namedShadowNames
- **Type**: typing.Optional[typing.List[str]]

### geoLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.GeoLocationTarget]]


# IndexingFilterOutput

### namedShadowNames
- **Type**: typing.Optional[typing.List[str]]

### geoLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.GeoLocationTarget]]


# IotAnalyticsAction

### channelArn
- **Type**: typing.Optional[str]

### channelName
- **Type**: typing.Optional[str]

### batchMode
- **Type**: typing.Optional[bool]

### roleArn
- **Type**: typing.Optional[str]


# IotEventsAction

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


# IotSiteWiseAction

### putAssetPropertyValueEntries
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.PutAssetPropertyValueEntry, aws_resource_validator.pydantic_models.iot.iot_classes.PutAssetPropertyValueEntryOutput]]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseActionOutput

### putAssetPropertyValueEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PutAssetPropertyValueEntryOutput]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IssuerCertificateIdentifier

### issuerCertificateSubject
- **Type**: typing.Optional[str]

### issuerId
- **Type**: typing.Optional[str]

### issuerCertificateSerialNumber
- **Type**: typing.Optional[str]


# Job

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PresignedUrlConfig]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRolloutConfig]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfigOutput]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### completedAt
- **Type**: typing.Optional[datetime.datetime]

### jobProcessDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobProcessDetails]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeoutConfig]

### namespaceId
- **Type**: typing.Optional[str]

### jobTemplateArn
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfigOutput]

### documentParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### isConcurrent
- **Type**: typing.Optional[bool]

### schedulingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SchedulingConfigOutput]

### scheduledJobRollouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ScheduledJobRollout]]

### destinationPackageVersions
- **Type**: typing.Optional[typing.List[str]]


# JobExecution

### jobId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### forceCanceled
- **Type**: typing.Optional[bool]

### statusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionStatusDetails]

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


# JobExecutionStatusDetails

### detailsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobExecutionSummary

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


# JobExecutionSummaryForJob

### thingArn
- **Type**: typing.Optional[str]

### jobExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionSummary]


# JobExecutionSummaryForThing

### jobId
- **Type**: typing.Optional[str]

### jobExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionSummary]


# JobExecutionsRetryConfig

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.RetryCriteria]
- **Required**: Yes


# JobExecutionsRetryConfigOutput

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.RetryCriteria]
- **Required**: Yes


# JobExecutionsRolloutConfig

### maximumPerMinute
- **Type**: typing.Optional[int]

### exponentialRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ExponentialRolloutRate]


# JobProcessDetails

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


# JobSummary

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


# JobTemplateSummary

### jobTemplateArn
- **Type**: typing.Optional[str]

### jobTemplateId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# KafkaAction

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.KafkaActionHeader]]


# KafkaActionHeader

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# KafkaActionOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.KafkaActionHeader]]


# KeyPair

### PublicKey
- **Type**: typing.Optional[str]

### PrivateKey
- **Type**: typing.Optional[str]


# KinesisAction

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### streamName
- **Type**: <class 'str'>
- **Required**: Yes

### partitionKey
- **Type**: typing.Optional[str]


# LambdaAction

### functionArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListActiveViolationsRequest

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


# ListActiveViolationsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListActiveViolationsResponse

### activeViolations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ActiveViolation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttachedPoliciesRequest

### target
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListAttachedPoliciesRequestPaginate

### target
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListAttachedPoliciesResponse

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Policy]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListAuditFindingsRequest

### taskId
- **Type**: typing.Optional[str]

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier]

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


# ListAuditFindingsRequestPaginate

### taskId
- **Type**: typing.Optional[str]

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### listSuppressedFindings
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListAuditFindingsResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AuditFinding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditMitigationActionsExecutionsRequest

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


# ListAuditMitigationActionsExecutionsRequestPaginate

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### actionStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListAuditMitigationActionsExecutionsResponse

### actionsExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AuditMitigationActionExecutionMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditMitigationActionsTasksRequest

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


# ListAuditMitigationActionsTasksRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListAuditMitigationActionsTasksResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AuditMitigationActionsTaskMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditSuppressionsRequest

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier]

### ascendingOrder
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAuditSuppressionsRequestPaginate

### checkName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier]

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListAuditSuppressionsResponse

### suppressions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AuditSuppression]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuditTasksRequest

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


# ListAuditTasksRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListAuditTasksResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AuditTaskMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAuthorizersRequest

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# ListAuthorizersRequestPaginate

### ascendingOrder
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListAuthorizersResponse

### authorizers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AuthorizerSummary]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListBillingGroupsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### namePrefixFilter
- **Type**: typing.Optional[str]


# ListBillingGroupsRequestPaginate

### namePrefixFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListBillingGroupsResponse

### billingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.GroupNameAndArn]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCACertificatesRequest

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]

### templateName
- **Type**: typing.Optional[str]


# ListCACertificatesRequestPaginate

### ascendingOrder
- **Type**: typing.Optional[bool]

### templateName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListCACertificatesResponse

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.CACertificate]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListCertificateProvidersRequest

### nextToken
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListCertificateProvidersResponse

### certificateProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.CertificateProviderSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCertificatesByCARequest

### caCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListCertificatesByCARequestPaginate

### caCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListCertificatesByCAResponse

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Certificate]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListCertificatesRequest

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListCertificatesRequestPaginate

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListCertificatesResponse

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Certificate]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListCommandExecutionsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeFilter]

### completedTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeFilter]

### targetArn
- **Type**: typing.Optional[str]

### commandArn
- **Type**: typing.Optional[str]


# ListCommandExecutionsRequestPaginate

### namespace
- **Type**: typing.Optional[typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### startedTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeFilter]

### completedTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeFilter]

### targetArn
- **Type**: typing.Optional[str]

### commandArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListCommandExecutionsResponse

### commandExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.CommandExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCommandsRequest

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


# ListCommandsRequestPaginate

### namespace
- **Type**: typing.Optional[typing.Literal['AWS-IoT', 'AWS-IoT-FleetWise']]

### commandParameterName
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListCommandsResponse

### commands
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.CommandSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCustomMetricsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCustomMetricsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListCustomMetricsResponse

### metricNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsExecutionsRequest

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


# ListDetectMitigationActionsExecutionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListDetectMitigationActionsExecutionsResponse

### actionsExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.DetectMitigationActionExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectMitigationActionsTasksRequest

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


# ListDetectMitigationActionsTasksRequestPaginate

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListDetectMitigationActionsTasksResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.DetectMitigationActionsTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDimensionsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDimensionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListDimensionsResponse

### dimensionNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainConfigurationsRequest

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]


# ListDomainConfigurationsRequestPaginate

### serviceType
- **Type**: typing.Optional[typing.Literal['CREDENTIAL_PROVIDER', 'DATA', 'JOBS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListDomainConfigurationsResponse

### domainConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.DomainConfigurationSummary]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListFleetMetricsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFleetMetricsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListFleetMetricsResponse

### fleetMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.FleetMetricNameAndArn]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIndicesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIndicesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListIndicesResponse

### indexNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobExecutionsForJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobExecutionsForJobRequestPaginate

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListJobExecutionsForJobResponse

### executionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionSummaryForJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobExecutionsForThingRequest

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


# ListJobExecutionsForThingRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListJobExecutionsForThingResponse

### executionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionSummaryForThing]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListJobTemplatesResponse

### jobTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.JobTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

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


# ListJobsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListJobsResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedJobTemplatesRequest

### templateName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedJobTemplatesRequestPaginate

### templateName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListManagedJobTemplatesResponse

### managedJobTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ManagedJobTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetricValuesRequest

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


# ListMetricValuesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListMetricValuesResponse

### metricDatumList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MetricDatum]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMitigationActionsRequest

### actionType
- **Type**: typing.Optional[typing.Literal['ADD_THINGS_TO_THING_GROUP', 'ENABLE_IOT_LOGGING', 'PUBLISH_FINDING_TO_SNS', 'REPLACE_DEFAULT_POLICY_VERSION', 'UPDATE_CA_CERTIFICATE', 'UPDATE_DEVICE_CERTIFICATE']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMitigationActionsRequestPaginate

### actionType
- **Type**: typing.Optional[typing.Literal['ADD_THINGS_TO_THING_GROUP', 'ENABLE_IOT_LOGGING', 'PUBLISH_FINDING_TO_SNS', 'REPLACE_DEFAULT_POLICY_VERSION', 'UPDATE_CA_CERTIFICATE', 'UPDATE_DEVICE_CERTIFICATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListMitigationActionsResponse

### actionIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MitigationActionIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOTAUpdatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### otaUpdateStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]


# ListOTAUpdatesRequestPaginate

### otaUpdateStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListOTAUpdatesResponse

### otaUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.OTAUpdateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOutgoingCertificatesRequest

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListOutgoingCertificatesRequestPaginate

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListOutgoingCertificatesResponse

### outgoingCertificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.OutgoingCertificate]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListPackageVersionsRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPackageVersionsRequestPaginate

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'DRAFT', 'PUBLISHED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListPackageVersionsResponse

### packageVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PackageVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackagesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPackagesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListPackagesResponse

### packageSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PackageSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPoliciesRequest

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListPoliciesRequestPaginate

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListPoliciesResponse

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Policy]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListPolicyPrincipalsRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListPolicyPrincipalsRequestPaginate

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListPolicyPrincipalsResponse

### principals
- **Type**: typing.List[str]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListPolicyVersionsRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes


# ListPolicyVersionsResponse

### policyVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PolicyVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListPrincipalPoliciesRequest

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListPrincipalPoliciesRequestPaginate

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListPrincipalPoliciesResponse

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Policy]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListPrincipalThingsRequest

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrincipalThingsRequestPaginate

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListPrincipalThingsResponse

### things
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrincipalThingsV2Request

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# ListPrincipalThingsV2RequestPaginate

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListPrincipalThingsV2Response

### principalThingObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PrincipalThingObject]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplateVersionsRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplateVersionsRequestPaginate

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListProvisioningTemplateVersionsResponse

### versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ProvisioningTemplateVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProvisioningTemplatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListProvisioningTemplatesResponse

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ProvisioningTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRelatedResourcesForAuditFindingRequest

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRelatedResourcesForAuditFindingRequestPaginate

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListRelatedResourcesForAuditFindingResponse

### relatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.RelatedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRoleAliasesRequest

### pageSize
- **Type**: typing.Optional[int]

### marker
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListRoleAliasesRequestPaginate

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListRoleAliasesResponse

### roleAliases
- **Type**: typing.List[str]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListSbomValidationResultsRequest

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


# ListSbomValidationResultsRequestPaginate

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### validationResult
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListSbomValidationResultsResponse

### validationResultSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.SbomValidationResultSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScheduledAuditsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListScheduledAuditsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListScheduledAuditsResponse

### scheduledAudits
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ScheduledAuditMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilesForTargetRequest

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### recursive
- **Type**: typing.Optional[bool]


# ListSecurityProfilesForTargetRequestPaginate

### securityProfileTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListSecurityProfilesForTargetResponse

### securityProfileTargetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.SecurityProfileTargetMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### dimensionName
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]


# ListSecurityProfilesRequestPaginate

### dimensionName
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListSecurityProfilesResponse

### securityProfileIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.SecurityProfileIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStreamsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ascendingOrder
- **Type**: typing.Optional[bool]


# ListStreamsRequestPaginate

### ascendingOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListStreamsResponse

### streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.StreamSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTargetsForPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### marker
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListTargetsForPolicyRequestPaginate

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListTargetsForPolicyResponse

### targets
- **Type**: typing.List[str]
- **Required**: Yes

### nextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ListTargetsForSecurityProfileRequest

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTargetsForSecurityProfileRequestPaginate

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListTargetsForSecurityProfileResponse

### securityProfileTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.SecurityProfileTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingGroupsForThingRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingGroupsForThingRequestPaginate

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingGroupsForThingResponse

### thingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.GroupNameAndArn]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingGroupsRequest

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


# ListThingGroupsRequestPaginate

### parentGroup
- **Type**: typing.Optional[str]

### namePrefixFilter
- **Type**: typing.Optional[str]

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingGroupsResponse

### thingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.GroupNameAndArn]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingPrincipalsRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingPrincipalsRequestPaginate

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingPrincipalsResponse

### principals
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingPrincipalsV2Request

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# ListThingPrincipalsV2RequestPaginate

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingPrincipalsV2Response

### thingPrincipalObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ThingPrincipalObject]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingRegistrationTaskReportsRequest

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


# ListThingRegistrationTaskReportsRequestPaginate

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### reportType
- **Type**: typing.Literal['ERRORS', 'RESULTS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingRegistrationTaskReportsResponse

### resourceLinks
- **Type**: typing.List[str]
- **Required**: Yes

### reportType
- **Type**: typing.Literal['ERRORS', 'RESULTS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingRegistrationTasksRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Completed', 'Failed', 'InProgress']]


# ListThingRegistrationTasksRequestPaginate

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Completed', 'Failed', 'InProgress']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingRegistrationTasksResponse

### taskIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingTypesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### thingTypeName
- **Type**: typing.Optional[str]


# ListThingTypesRequestPaginate

### thingTypeName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingTypesResponse

### thingTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Thinginition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingsInBillingGroupRequest

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingsInBillingGroupRequestPaginate

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingsInBillingGroupResponse

### things
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingsInThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThingsInThingGroupRequestPaginate

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### recursive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingsInThingGroupResponse

### things
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListThingsRequest

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


# ListThingsRequestPaginate

### attributeName
- **Type**: typing.Optional[str]

### attributeValue
- **Type**: typing.Optional[str]

### thingTypeName
- **Type**: typing.Optional[str]

### usePrefixAttributeValue
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListThingsResponse

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ThingAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTopicRuleDestinationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTopicRuleDestinationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListTopicRuleDestinationsResponse

### destinationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.TopicRuleDestinationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTopicRulesRequest

### topic
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]


# ListTopicRulesRequestPaginate

### topic
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListTopicRulesResponse

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.TopicRuleListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListV2LoggingLevelsRequest

### targetType
- **Type**: typing.Optional[typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListV2LoggingLevelsRequestPaginate

### targetType
- **Type**: typing.Optional[typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListV2LoggingLevelsResponse

### logTargetConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.LogTargetConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListViolationEventsRequest

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


# ListViolationEventsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PaginatorConfig]


# ListViolationEventsResponse

### violationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ViolationEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LocationAction

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.LocationTimestamp]


# LocationTimestamp

### value
- **Type**: <class 'str'>
- **Required**: Yes

### unit
- **Type**: typing.Optional[str]


# LogTarget

### targetType
- **Type**: typing.Literal['CLIENT_ID', 'DEFAULT', 'PRINCIPAL_ID', 'SOURCE_IP', 'THING_GROUP']
- **Required**: Yes

### targetName
- **Type**: typing.Optional[str]


# LogTargetConfiguration

### logTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.LogTarget]

### logLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']]


# LoggingOptionsPayload

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### logLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']]


# MachineLearningDetectionConfig

### confidenceLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes


# MaintenanceWindow

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ManagedJobTemplateSummary

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


# MetricDatum

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricValueOutput]


# MetricDimension

### dimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Optional[typing.Literal['IN', 'NOT_IN']]


# MetricToRetain

### metric
- **Type**: <class 'str'>
- **Required**: Yes

### metricDimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricDimension]

### exportMetric
- **Type**: typing.Optional[bool]


# MetricValue

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


# MetricValueOutput

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


# MetricsExportConfig

### mqttTopic
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# MitigationAction

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### actionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MitigationActionParamsOutput]


# MitigationActionIdentifier

### actionName
- **Type**: typing.Optional[str]

### actionArn
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# MitigationActionParams

### updateDeviceCertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.UpdateDeviceCertificateParams]

### updateCACertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.UpdateCACertificateParams]

### addThingsToThingGroupParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AddThingsToThingGroupParams]

### replaceDefaultPolicyVersionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ReplaceDefaultPolicyVersionParams]

### enableIoTLoggingParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.EnableIoTLoggingParams]

### publishFindingToSnsParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PublishFindingToSnsParams]


# MitigationActionParamsOutput

### updateDeviceCertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.UpdateDeviceCertificateParams]

### updateCACertificateParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.UpdateCACertificateParams]

### addThingsToThingGroupParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AddThingsToThingGroupParamsOutput]

### replaceDefaultPolicyVersionParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ReplaceDefaultPolicyVersionParams]

### enableIoTLoggingParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.EnableIoTLoggingParams]

### publishFindingToSnsParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PublishFindingToSnsParams]


# Mqtt5Configuration

### propagatingAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PropagatingAttribute]]


# Mqtt5ConfigurationOutput

### propagatingAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.PropagatingAttribute]]


# MqttContext

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### clientId
- **Type**: typing.Optional[str]


# MqttHeaders

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.UserProperty]]


# MqttHeadersOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.UserProperty]]


# NonCompliantResource

### resourceType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SETTINGS', 'CA_CERTIFICATE', 'CLIENT_ID', 'COGNITO_IDENTITY_POOL', 'DEVICE_CERTIFICATE', 'IAM_ROLE', 'IOT_POLICY', 'ISSUER_CERTIFICATE', 'ROLE_ALIAS']]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier]

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]


# OTAUpdateFile

### fileName
- **Type**: typing.Optional[str]

### fileType
- **Type**: typing.Optional[int]

### fileVersion
- **Type**: typing.Optional[str]

### fileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.FileLocation]

### codeSigning
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigning, aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigningOutput, NoneType]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# OTAUpdateFileOutput

### fileName
- **Type**: typing.Optional[str]

### fileType
- **Type**: typing.Optional[int]

### fileVersion
- **Type**: typing.Optional[str]

### fileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.FileLocation]

### codeSigning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.CodeSigningOutput]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# OTAUpdateInfo

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobExecutionsRolloutConfig]

### awsJobPresignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AwsJobPresignedUrlConfig]

### targetSelection
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'SNAPSHOT']]

### otaUpdateFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.OTAUpdateFileOutput]]

### otaUpdateStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### awsIotJobId
- **Type**: typing.Optional[str]

### awsIotJobArn
- **Type**: typing.Optional[str]

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ErrorInfo]

### additionalParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# OTAUpdateSummary

### otaUpdateId
- **Type**: typing.Optional[str]

### otaUpdateArn
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# OpenSearchAction

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


# OutgoingCertificate

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


# PackageSummary

### packageName
- **Type**: typing.Optional[str]

### defaultVersionName
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# PackageVersionArtifact

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.S3Location]


# PackageVersionSummary

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PercentPair

### percent
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[float]


# Policy

### policyName
- **Type**: typing.Optional[str]

### policyArn
- **Type**: typing.Optional[str]


# PolicyVersion

### versionId
- **Type**: typing.Optional[str]

### isDefaultVersion
- **Type**: typing.Optional[bool]

### createDate
- **Type**: typing.Optional[datetime.datetime]


# PolicyVersionIdentifier

### policyName
- **Type**: typing.Optional[str]

### policyVersionId
- **Type**: typing.Optional[str]


# PresignedUrlConfig

### roleArn
- **Type**: typing.Optional[str]

### expiresInSec
- **Type**: typing.Optional[int]


# PrincipalThingObject

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# PropagatingAttribute

### userPropertyKey
- **Type**: typing.Optional[str]

### thingAttribute
- **Type**: typing.Optional[str]

### connectionAttribute
- **Type**: typing.Optional[str]


# ProvisioningHook

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### payloadVersion
- **Type**: typing.Optional[str]


# ProvisioningTemplateSummary

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


# ProvisioningTemplateVersionSummary

### versionId
- **Type**: typing.Optional[int]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### isDefaultVersion
- **Type**: typing.Optional[bool]


# PublishFindingToSnsParams

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutAssetPropertyValueEntry

### propertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AssetPropertyValue]
- **Required**: Yes

### entryId
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# PutAssetPropertyValueEntryOutput

### propertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AssetPropertyValue]
- **Required**: Yes

### entryId
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# PutItemInput

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# PutVerificationStateOnViolationRequest

### violationId
- **Type**: <class 'str'>
- **Required**: Yes

### verificationState
- **Type**: typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']
- **Required**: Yes

### verificationStateDescription
- **Type**: typing.Optional[str]


# RateIncreaseCriteria

### numberOfNotifiedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]


# RegisterCACertificateRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.RegistrationConfig]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]]

### certificateMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'SNI_ONLY']]


# RegisterCACertificateResponse

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterCertificateRequest

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### caCertificatePem
- **Type**: typing.Optional[str]

### setAsActive
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']]


# RegisterCertificateResponse

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterCertificateWithoutCARequest

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']]


# RegisterCertificateWithoutCAResponse

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterThingRequest

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# RegisterThingResponse

### certificatePem
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# RegistrationConfig

### templateBody
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### templateName
- **Type**: typing.Optional[str]


# RejectCertificateTransferRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### rejectReason
- **Type**: typing.Optional[str]


# RelatedResource

### resourceType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SETTINGS', 'CA_CERTIFICATE', 'CLIENT_ID', 'COGNITO_IDENTITY_POOL', 'DEVICE_CERTIFICATE', 'IAM_ROLE', 'IOT_POLICY', 'ISSUER_CERTIFICATE', 'ROLE_ALIAS']]

### resourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier]

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]


# RemoveThingFromBillingGroupRequest

### billingGroupName
- **Type**: typing.Optional[str]

### billingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# RemoveThingFromThingGroupRequest

### thingGroupName
- **Type**: typing.Optional[str]

### thingGroupArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# ReplaceDefaultPolicyVersionParams

### templateName
- **Type**: typing.Literal['BLANK_POLICY']
- **Required**: Yes


# ReplaceTopicRuleRequest

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### topicRulePayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.TopicRulePayload'>
- **Required**: Yes


# RepublishAction

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### qos
- **Type**: typing.Optional[int]

### headers
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.MqttHeaders, aws_resource_validator.pydantic_models.iot.iot_classes.MqttHeadersOutput, NoneType]


# RepublishActionOutput

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### qos
- **Type**: typing.Optional[int]

### headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MqttHeadersOutput]


# ResourceIdentifier

### deviceCertificateId
- **Type**: typing.Optional[str]

### caCertificateId
- **Type**: typing.Optional[str]

### cognitoIdentityPoolId
- **Type**: typing.Optional[str]

### clientId
- **Type**: typing.Optional[str]

### policyVersionIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PolicyVersionIdentifier]

### account
- **Type**: typing.Optional[str]

### iamRoleArn
- **Type**: typing.Optional[str]

### roleAliasArn
- **Type**: typing.Optional[str]

### issuerCertificateIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IssuerCertificateIdentifier]

### deviceCertificateArn
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


# RetryCriteria

### failureType
- **Type**: typing.Literal['ALL', 'FAILED', 'TIMED_OUT']
- **Required**: Yes

### numberOfRetries
- **Type**: <class 'int'>
- **Required**: Yes


# RoleAliasDescription

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


# S3Action

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


# S3Destination

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# S3Location

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# SalesforceAction

### token
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes


# Sbom

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.S3Location]


# SbomValidationResultSummary

### fileName
- **Type**: typing.Optional[str]

### validationResult
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]

### errorCode
- **Type**: typing.Optional[typing.Literal['FILE_SIZE_LIMIT_EXCEEDED', 'INCOMPATIBLE_FORMAT']]

### errorMessage
- **Type**: typing.Optional[str]


# ScheduledAuditMetadata

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


# ScheduledJobRollout

### startTime
- **Type**: typing.Optional[str]


# SchedulingConfig

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]

### endBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL', 'FORCE_CANCEL', 'STOP_ROLLOUT']]

### maintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MaintenanceWindow]]


# SchedulingConfigOutput

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]

### endBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL', 'FORCE_CANCEL', 'STOP_ROLLOUT']]

### maintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MaintenanceWindow]]


# SearchIndexRequest

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


# SearchIndexResponse

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ThingDocument]
- **Required**: Yes

### thingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SecurityProfileIdentifier

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# SecurityProfileTarget

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# SecurityProfileTargetMapping

### securityProfileIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SecurityProfileIdentifier]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SecurityProfileTarget]


# ServerCertificateConfig

### enableOCSPCheck
- **Type**: typing.Optional[bool]

### ocspLambdaArn
- **Type**: typing.Optional[str]

### ocspAuthorizedResponderArn
- **Type**: typing.Optional[str]


# ServerCertificateSummary

### serverCertificateArn
- **Type**: typing.Optional[str]

### serverCertificateStatus
- **Type**: typing.Optional[typing.Literal['INVALID', 'VALID']]

### serverCertificateStatusDetail
- **Type**: typing.Optional[str]


# SetDefaultAuthorizerRequest

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes


# SetDefaultAuthorizerResponse

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# SetDefaultPolicyVersionRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# SetLoggingOptionsRequest

### loggingOptionsPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.LoggingOptionsPayload'>
- **Required**: Yes


# SetV2LoggingLevelRequest

### logTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.LogTarget'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# SetV2LoggingOptionsRequest

### roleArn
- **Type**: typing.Optional[str]

### defaultLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARN']]

### disableAllLogs
- **Type**: typing.Optional[bool]


# SigV4Authorization

### signingRegion
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# SigningProfileParameter

### certificateArn
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]

### certificatePathOnDevice
- **Type**: typing.Optional[str]


# SnsAction

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'RAW']]


# SqsAction

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### queueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### useBase64
- **Type**: typing.Optional[bool]


# StartAuditMitigationActionsTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AuditMitigationActionsTaskTarget, aws_resource_validator.pydantic_models.iot.iot_classes.AuditMitigationActionsTaskTargetOutput]
- **Required**: Yes

### auditCheckToActionsMapping
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartAuditMitigationActionsTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# StartDetectMitigationActionsTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.DetectMitigationActionsTaskTarget, aws_resource_validator.pydantic_models.iot.iot_classes.DetectMitigationActionsTaskTargetOutput]
- **Required**: Yes

### actions
- **Type**: typing.List[str]
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### violationEventOccurrenceRange
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ViolationEventOccurrenceRange, aws_resource_validator.pydantic_models.iot.iot_classes.ViolationEventOccurrenceRangeOutput, NoneType]

### includeOnlyActiveViolations
- **Type**: typing.Optional[bool]

### includeSuppressedAlerts
- **Type**: typing.Optional[bool]


# StartDetectMitigationActionsTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# StartOnDemandAuditTaskRequest

### targetCheckNames
- **Type**: typing.List[str]
- **Required**: Yes


# StartOnDemandAuditTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# StartSigningJobParameter

### signingProfileParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.SigningProfileParameter]

### signingProfileName
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.Destination]


# StartThingRegistrationTaskRequest

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


# StartThingRegistrationTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# StatisticalThreshold

### statistic
- **Type**: typing.Optional[str]


# Statistics

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


# StatusReason

### reasonCode
- **Type**: <class 'str'>
- **Required**: Yes

### reasonDescription
- **Type**: typing.Optional[str]


# StepFunctionsAction

### stateMachineName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionNamePrefix
- **Type**: typing.Optional[str]


# StopThingRegistrationTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# Stream

### streamId
- **Type**: typing.Optional[str]

### fileId
- **Type**: typing.Optional[int]


# StreamFile

### fileId
- **Type**: typing.Optional[int]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.S3Location]


# StreamInfo

### streamId
- **Type**: typing.Optional[str]

### streamArn
- **Type**: typing.Optional[str]

### streamVersion
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.StreamFile]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### roleArn
- **Type**: typing.Optional[str]


# StreamSummary

### streamId
- **Type**: typing.Optional[str]

### streamArn
- **Type**: typing.Optional[str]

### streamVersion
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Tag]
- **Required**: Yes


# TaskStatistics

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


# TaskStatisticsForAuditCheck

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


# TermsAggregation

### maxBuckets
- **Type**: typing.Optional[int]


# TestAuthorizationRequest

### authInfos
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AuthInfo, aws_resource_validator.pydantic_models.iot.iot_classes.AuthInfoOutput]]
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### cognitoIdentityPoolId
- **Type**: typing.Optional[str]

### clientId
- **Type**: typing.Optional[str]

### policyNamesToAdd
- **Type**: typing.Optional[typing.List[str]]

### policyNamesToSkip
- **Type**: typing.Optional[typing.List[str]]


# TestAuthorizationResponse

### authResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.AuthResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# TestInvokeAuthorizerRequest

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: typing.Optional[str]

### tokenSignature
- **Type**: typing.Optional[str]

### httpContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.HttpContext]

### mqttContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MqttContext]

### tlsContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TlsContext]


# TestInvokeAuthorizerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ThingAttribute

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


# ThingConnectivity

### connected
- **Type**: typing.Optional[bool]

### timestamp
- **Type**: typing.Optional[int]

### disconnectReason
- **Type**: typing.Optional[str]


# ThingDocument

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ThingConnectivity]


# ThingGroupDocument

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


# ThingGroupIndexingConfiguration

### thingGroupIndexingMode
- **Type**: typing.Literal['OFF', 'ON']
- **Required**: Yes

### managedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]

### customFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]


# ThingGroupIndexingConfigurationOutput

### thingGroupIndexingMode
- **Type**: typing.Literal['OFF', 'ON']
- **Required**: Yes

### managedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]

### customFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]


# ThingGroupMetadata

### parentGroupName
- **Type**: typing.Optional[str]

### rootToParentThingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.GroupNameAndArn]]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# ThingGroupProperties

### thingGroupDescription
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AttributePayload]


# ThingGroupPropertiesOutput

### thingGroupDescription
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AttributePayloadOutput]


# ThingIndexingConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]

### customFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IndexingFilter]


# ThingIndexingConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]

### customFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.Field]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.IndexingFilterOutput]


# ThingPrincipalObject

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### thingPrincipalType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING']]


# ThingTypeMetadata

### deprecated
- **Type**: typing.Optional[bool]

### deprecationDate
- **Type**: typing.Optional[datetime.datetime]

### creationDate
- **Type**: typing.Optional[datetime.datetime]


# ThingTypeProperties

### thingTypeDescription
- **Type**: typing.Optional[str]

### searchableAttributes
- **Type**: typing.Optional[typing.List[str]]

### mqtt5Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.Mqtt5Configuration]


# ThingTypePropertiesOutput

### thingTypeDescription
- **Type**: typing.Optional[str]

### searchableAttributes
- **Type**: typing.Optional[typing.List[str]]

### mqtt5Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.Mqtt5ConfigurationOutput]


# Thinginition

### thingTypeName
- **Type**: typing.Optional[str]

### thingTypeArn
- **Type**: typing.Optional[str]

### thingTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypePropertiesOutput]

### thingTypeMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypeMetadata]


# TimeFilter

### after
- **Type**: typing.Optional[str]

### before
- **Type**: typing.Optional[str]


# TimeoutConfig

### inProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


# TimestreamAction

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.TimestreamDimension]
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimestreamTimestamp]


# TimestreamActionOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.TimestreamDimension]
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimestreamTimestamp]


# TimestreamDimension

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestreamTimestamp

### value
- **Type**: <class 'str'>
- **Required**: Yes

### unit
- **Type**: <class 'str'>
- **Required**: Yes


# TlsConfig

### securityPolicy
- **Type**: typing.Optional[str]


# TlsContext

### serverName
- **Type**: typing.Optional[str]


# TopicRule

### ruleName
- **Type**: typing.Optional[str]

### sql
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ActionOutput]]

### ruleDisabled
- **Type**: typing.Optional[bool]

### awsIotSqlVersion
- **Type**: typing.Optional[str]

### errorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ActionOutput]


# TopicRuleDestination

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.HttpUrlDestinationProperties]

### vpcProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.VpcDestinationProperties]


# TopicRuleDestinationConfiguration

### httpUrlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.HttpUrlDestinationConfiguration]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.VpcDestinationConfiguration]


# TopicRuleDestinationSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.HttpUrlDestinationSummary]

### vpcDestinationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.VpcDestinationSummary]


# TopicRuleListItem

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


# TopicRulePayload

### sql
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.Action, aws_resource_validator.pydantic_models.iot.iot_classes.ActionOutput]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### ruleDisabled
- **Type**: typing.Optional[bool]

### awsIotSqlVersion
- **Type**: typing.Optional[str]

### errorAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.Action, aws_resource_validator.pydantic_models.iot.iot_classes.ActionOutput, NoneType]


# TransferCertificateRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### targetAwsAccount
- **Type**: <class 'str'>
- **Required**: Yes

### transferMessage
- **Type**: typing.Optional[str]


# TransferCertificateResponse

### transferredCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# TransferData

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


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccountAuditConfigurationRequest

### roleArn
- **Type**: typing.Optional[str]

### auditNotificationTargetConfigurations
- **Type**: typing.Optional[typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot.iot_classes.AuditNotificationTarget]]

### auditCheckConfigurations
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AuditCheckConfiguration, aws_resource_validator.pydantic_models.iot.iot_classes.AuditCheckConfigurationOutput]]]


# UpdateAuditSuppressionRequest

### checkName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResourceIdentifier'>
- **Required**: Yes

### expirationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### suppressIndefinitely
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# UpdateAuthorizerRequest

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerFunctionArn
- **Type**: typing.Optional[str]

### tokenKeyName
- **Type**: typing.Optional[str]

### tokenSigningPublicKeys
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### enableCachingForHttp
- **Type**: typing.Optional[bool]


# UpdateAuthorizerResponse

### authorizerName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBillingGroupRequest

### billingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### billingGroupProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.BillingGroupProperties'>
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# UpdateBillingGroupResponse

### version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCACertificateParams

### action
- **Type**: typing.Literal['DEACTIVATE']
- **Required**: Yes


# UpdateCACertificateRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### newStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### newAutoRegistrationStatus
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### registrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.RegistrationConfig]

### removeAutoRegistration
- **Type**: typing.Optional[bool]


# UpdateCertificateProviderRequest

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### lambdaFunctionArn
- **Type**: typing.Optional[str]

### accountDefaultForOperations
- **Type**: typing.Optional[typing.List[typing.Literal['CreateCertificateFromCsr']]]


# UpdateCertificateProviderResponse

### certificateProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCertificateRequest

### certificateId
- **Type**: <class 'str'>
- **Required**: Yes

### newStatus
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'REVOKED']
- **Required**: Yes


# UpdateCommandRequest

### commandId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### deprecated
- **Type**: typing.Optional[bool]


# UpdateCommandResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomMetricRequest

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCustomMetricResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDeviceCertificateParams

### action
- **Type**: typing.Literal['DEACTIVATE']
- **Required**: Yes


# UpdateDimensionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stringValues
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDimensionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainConfigurationRequest

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.AuthorizerConfig]

### domainConfigurationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### removeAuthorizerConfig
- **Type**: typing.Optional[bool]

### tlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TlsConfig]

### serverCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ServerCertificateConfig]

### authenticationType
- **Type**: typing.Optional[typing.Literal['AWS_SIGV4', 'AWS_X509', 'CUSTOM_AUTH', 'CUSTOM_AUTH_X509', 'DEFAULT']]

### applicationProtocol
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HTTPS', 'MQTT_WSS', 'SECURE_MQTT']]

### clientCertificateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ClientCertificateConfig]


# UpdateDomainConfigurationResponse

### domainConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### domainConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDynamicThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupProperties, aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupPropertiesOutput]
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]

### indexName
- **Type**: typing.Optional[str]

### queryString
- **Type**: typing.Optional[str]

### queryVersion
- **Type**: typing.Optional[str]


# UpdateDynamicThingGroupResponse

### version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEventConfigurationsRequest

### eventConfigurations
- **Type**: typing.Optional[typing.Dict[typing.Literal['CA_CERTIFICATE', 'CERTIFICATE', 'JOB', 'JOB_EXECUTION', 'POLICY', 'THING', 'THING_GROUP', 'THING_GROUP_HIERARCHY', 'THING_GROUP_MEMBERSHIP', 'THING_TYPE', 'THING_TYPE_ASSOCIATION'], aws_resource_validator.pydantic_models.iot.iot_classes.Configuration]]


# UpdateFleetMetricRequest

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: typing.Optional[str]

### aggregationType
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AggregationType, aws_resource_validator.pydantic_models.iot.iot_classes.AggregationTypeOutput, NoneType]

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


# UpdateIndexingConfigurationRequest

### thingIndexingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingIndexingConfiguration, aws_resource_validator.pydantic_models.iot.iot_classes.ThingIndexingConfigurationOutput, NoneType]

### thingGroupIndexingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupIndexingConfiguration, aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupIndexingConfigurationOutput, NoneType]


# UpdateJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### presignedUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PresignedUrlConfig]

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRolloutConfig]

### abortConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfig, aws_resource_validator.pydantic_models.iot.iot_classes.AbortConfigOutput, NoneType]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.TimeoutConfig]

### namespaceId
- **Type**: typing.Optional[str]

### jobExecutionsRetryConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfig, aws_resource_validator.pydantic_models.iot.iot_classes.JobExecutionsRetryConfigOutput, NoneType]


# UpdateMitigationActionRequest

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### actionParams
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.MitigationActionParams, aws_resource_validator.pydantic_models.iot.iot_classes.MitigationActionParamsOutput, NoneType]


# UpdateMitigationActionResponse

### actionArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePackageConfigurationRequest

### versionUpdateByJobsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.VersionUpdateByJobsConfig]

### clientToken
- **Type**: typing.Optional[str]


# UpdatePackageRequest

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


# UpdatePackageVersionRequest

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### artifact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.PackageVersionArtifact]

### action
- **Type**: typing.Optional[typing.Literal['DEPRECATE', 'PUBLISH']]

### recipe
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateProvisioningTemplateRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ProvisioningHook]

### removePreProvisioningHook
- **Type**: typing.Optional[bool]


# UpdateRoleAliasRequest

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### credentialDurationSeconds
- **Type**: typing.Optional[int]


# UpdateRoleAliasResponse

### roleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### roleAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScheduledAuditRequest

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
- **Type**: typing.Optional[typing.List[str]]


# UpdateScheduledAuditResponse

### scheduledAuditArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSecurityProfileRequest

### securityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### securityProfileDescription
- **Type**: typing.Optional[str]

### behaviors
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.Behavior, aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorOutput]]]

### alertTargets
- **Type**: typing.Optional[typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot.iot_classes.AlertTarget]]

### additionalMetricsToRetain
- **Type**: typing.Optional[typing.List[str]]

### additionalMetricsToRetainV2
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MetricToRetain]]

### deleteBehaviors
- **Type**: typing.Optional[bool]

### deleteAlertTargets
- **Type**: typing.Optional[bool]

### deleteAdditionalMetricsToRetain
- **Type**: typing.Optional[bool]

### expectedVersion
- **Type**: typing.Optional[int]

### metricsExportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricsExportConfig]

### deleteMetricsExportConfig
- **Type**: typing.Optional[bool]


# UpdateSecurityProfileResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorOutput]
- **Required**: Yes

### alertTargets
- **Type**: typing.Dict[typing.Literal['SNS'], aws_resource_validator.pydantic_models.iot.iot_classes.AlertTarget]
- **Required**: Yes

### additionalMetricsToRetain
- **Type**: typing.List[str]
- **Required**: Yes

### additionalMetricsToRetainV2
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.MetricToRetain]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.MetricsExportConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStreamRequest

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.StreamFile]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateStreamResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThingGroupRequest

### thingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### thingGroupProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupProperties, aws_resource_validator.pydantic_models.iot.iot_classes.ThingGroupPropertiesOutput]
- **Required**: Yes

### expectedVersion
- **Type**: typing.Optional[int]


# UpdateThingGroupResponse

### version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThingGroupsForThingRequest

### thingName
- **Type**: typing.Optional[str]

### thingGroupsToAdd
- **Type**: typing.Optional[typing.List[str]]

### thingGroupsToRemove
- **Type**: typing.Optional[typing.List[str]]

### overrideDynamicGroups
- **Type**: typing.Optional[bool]


# UpdateThingRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeName
- **Type**: typing.Optional[str]

### attributePayload
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.AttributePayload, aws_resource_validator.pydantic_models.iot.iot_classes.AttributePayloadOutput, NoneType]

### expectedVersion
- **Type**: typing.Optional[int]

### removeThingType
- **Type**: typing.Optional[bool]


# UpdateThingTypeRequest

### thingTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### thingTypeProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypeProperties, aws_resource_validator.pydantic_models.iot.iot_classes.ThingTypePropertiesOutput, NoneType]


# UpdateTopicRuleDestinationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETING', 'DISABLED', 'ENABLED', 'ERROR', 'IN_PROGRESS']
- **Required**: Yes


# UserProperty

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateSecurityProfileBehaviorsRequest

### behaviors
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iot.iot_classes.Behavior, aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorOutput]]
- **Required**: Yes


# ValidateSecurityProfileBehaviorsResponse

### valid
- **Type**: <class 'bool'>
- **Required**: Yes

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot.iot_classes.ValidationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot.iot_classes.ResponseMetadata'>
- **Required**: Yes


# ValidationError

### errorMessage
- **Type**: typing.Optional[str]


# VersionUpdateByJobsConfig

### enabled
- **Type**: typing.Optional[bool]

### roleArn
- **Type**: typing.Optional[str]


# ViolationEvent

### violationId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### securityProfileName
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.BehaviorOutput]

### metricValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.MetricValueOutput]

### violationEventAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot.iot_classes.ViolationEventAdditionalInfo]

### violationEventType
- **Type**: typing.Optional[typing.Literal['alarm-cleared', 'alarm-invalidated', 'in-alarm']]

### verificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### verificationStateDescription
- **Type**: typing.Optional[str]

### violationEventTime
- **Type**: typing.Optional[datetime.datetime]


# ViolationEventAdditionalInfo

### confidenceLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# ViolationEventOccurrenceRange

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# ViolationEventOccurrenceRangeOutput

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# VpcDestinationConfiguration

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.List[str]]


# VpcDestinationProperties

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# VpcDestinationSummary

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


