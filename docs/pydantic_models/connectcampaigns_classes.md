# Connectcampaigns Classes

# AgentlessDialerConfig

### dialingCapacity
- **Type**: typing.Optional[float]


# AnswerMachineDetectionConfig

### enableAnswerMachineDetection
- **Type**: <class 'bool'>
- **Required**: Yes

### awaitAnswerMachinePrompt
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Campaign

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CampaignFilters

### instanceIdFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceIdFilter]


# CampaignSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCampaignRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### dialerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.DialerConfig'>
- **Required**: Yes

### outboundCallConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.OutboundCallConfig'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeleteConnectInstanceConfigRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceOnboardingJobRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCampaignResponse

### campaign
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.Campaign'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# DialRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### expirationTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.Timestamp'>
- **Required**: Yes

### attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# DialerConfig

### progressiveDialerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.ProgressiveDialerConfig]

### predictiveDialerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.PredictiveDialerConfig]

### agentlessDialerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.AgentlessDialerConfig]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfig

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### encryptionType
- **Type**: typing.Optional[typing.Literal['KMS']]

### keyArn
- **Type**: typing.Optional[str]


# FailedCampaignStateResponse

### campaignId
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['ResourceNotFound', 'UnknownError']]


# FailedRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetCampaignStateBatchRequest

### campaignIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetCampaignStateBatchResponse

### successfulRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.SuccessfulCampaignStateResponse]
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.FailedCampaignStateResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignStateResponse

### state
- **Type**: typing.Literal['Failed', 'Initialized', 'Paused', 'Running', 'Stopped']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectInstanceConfigRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectInstanceConfigResponse

### connectInstanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceOnboardingJobStatusRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceOnboardingJobStatusResponse

### connectInstanceOnboardingJobStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceOnboardingJobStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceConfig

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceLinkedRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.EncryptionConfig'>
- **Required**: Yes


# InstanceIdFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstanceOnboardingJobStatus

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### failureCode
- **Type**: typing.Optional[typing.Literal['EVENT_BRIDGE_ACCESS_DENIED', 'EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED', 'IAM_ACCESS_DENIED', 'INTERNAL_FAILURE', 'KMS_ACCESS_DENIED', 'KMS_KEY_NOT_FOUND']]


# ListCampaignsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.CampaignFilters]


# ListCampaignsRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.CampaignFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.PaginatorConfig]


# ListCampaignsResponse

### campaignSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.CampaignSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# OutboundCallConfig

### connectContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### connectSourcePhoneNumber
- **Type**: typing.Optional[str]

### connectQueueId
- **Type**: typing.Optional[str]

### answerMachineDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.AnswerMachineDetectionConfig]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredictiveDialerConfig

### bandwidthAllocation
- **Type**: <class 'float'>
- **Required**: Yes

### dialingCapacity
- **Type**: typing.Optional[float]


# ProgressiveDialerConfig

### bandwidthAllocation
- **Type**: <class 'float'>
- **Required**: Yes

### dialingCapacity
- **Type**: typing.Optional[float]


# PutDialRequestBatchResponse

### successfulRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.SuccessfulRequest]
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.FailedRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


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


# StartInstanceOnboardingJobRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.EncryptionConfig'>
- **Required**: Yes


# StartInstanceOnboardingJobResponse

### connectInstanceOnboardingJobStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceOnboardingJobStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadata'>
- **Required**: Yes


# SuccessfulCampaignStateResponse

### campaignId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Initialized', 'Paused', 'Running', 'Stopped']]


# SuccessfulRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


