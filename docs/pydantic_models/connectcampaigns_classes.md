# Connectcampaigns Classes

# AgentlessDialerConfigTypeDef

### dialingCapacity
- **Type**: typing.Optional[float]


# AnswerMachineDetectionConfigTypeDef

### enableAnswerMachineDetection
- **Type**: <class 'bool'>
- **Required**: Yes

### awaitAnswerMachinePrompt
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CampaignFiltersTypeDef

### instanceIdFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceIdFilterTypeDef]


# CampaignSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CampaignTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCampaignRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### dialerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.DialerConfigTypeDef'>
- **Required**: Yes

### outboundCallConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.OutboundCallConfigTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeleteConnectInstanceConfigRequestTypeDef

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceOnboardingJobRequestTypeDef

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCampaignResponseTypeDef

### campaign
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.CampaignTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DialRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### expirationTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.TimestampTypeDef'>
- **Required**: Yes

### attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# DialerConfigTypeDef

### progressiveDialerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.ProgressiveDialerConfigTypeDef]

### predictiveDialerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.PredictiveDialerConfigTypeDef]

### agentlessDialerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.AgentlessDialerConfigTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### encryptionType
- **Type**: typing.Optional[typing.Literal['KMS']]

### keyArn
- **Type**: typing.Optional[str]


# FailedCampaignStateResponseTypeDef

### campaignId
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['ResourceNotFound', 'UnknownError']]


# FailedRequestTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetCampaignStateBatchRequestTypeDef

### campaignIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetCampaignStateBatchResponseTypeDef

### successfulRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.SuccessfulCampaignStateResponseTypeDef]
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.FailedCampaignStateResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCampaignStateResponseTypeDef

### state
- **Type**: typing.Literal['Failed', 'Initialized', 'Paused', 'Running', 'Stopped']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectInstanceConfigRequestTypeDef

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectInstanceConfigResponseTypeDef

### connectInstanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceOnboardingJobStatusRequestTypeDef

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceOnboardingJobStatusResponseTypeDef

### connectInstanceOnboardingJobStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceOnboardingJobStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceConfigTypeDef

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceLinkedRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.EncryptionConfigTypeDef'>
- **Required**: Yes


# InstanceIdFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstanceOnboardingJobStatusTypeDef

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### failureCode
- **Type**: typing.Optional[typing.Literal['EVENT_BRIDGE_ACCESS_DENIED', 'EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED', 'IAM_ACCESS_DENIED', 'INTERNAL_FAILURE', 'KMS_ACCESS_DENIED', 'KMS_KEY_NOT_FOUND']]


# ListCampaignsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.CampaignFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.PaginatorConfigTypeDef]


# ListCampaignsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.CampaignFiltersTypeDef]


# ListCampaignsResponseTypeDef

### campaignSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.CampaignSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OutboundCallConfigTypeDef

### connectContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### connectSourcePhoneNumber
- **Type**: typing.Optional[str]

### connectQueueId
- **Type**: typing.Optional[str]

### answerMachineDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaigns_classes.AnswerMachineDetectionConfigTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredictiveDialerConfigTypeDef

### bandwidthAllocation
- **Type**: <class 'float'>
- **Required**: Yes

### dialingCapacity
- **Type**: typing.Optional[float]


# ProgressiveDialerConfigTypeDef

### bandwidthAllocation
- **Type**: <class 'float'>
- **Required**: Yes

### dialingCapacity
- **Type**: typing.Optional[float]


# PutDialRequestBatchResponseTypeDef

### successfulRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.SuccessfulRequestTypeDef]
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaigns_classes.FailedRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StartInstanceOnboardingJobRequestTypeDef

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.EncryptionConfigTypeDef'>
- **Required**: Yes


# StartInstanceOnboardingJobResponseTypeDef

### connectInstanceOnboardingJobStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.InstanceOnboardingJobStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaigns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SuccessfulCampaignStateResponseTypeDef

### campaignId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Initialized', 'Paused', 'Running', 'Stopped']]


# SuccessfulRequestTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


