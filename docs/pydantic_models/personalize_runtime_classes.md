# Pydantic Models in personalize_runtime_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetActionRecommendationsRequestRequestTypeDef

### campaignArn
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### filterArn
- **Type**: typing.Optional[str]

### filterValues
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetActionRecommendationsResponseTypeDef

### actionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_runtime_classes.PredictedActionTypeDef]
- **Required**: Yes

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPersonalizedRankingRequestRequestTypeDef

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes

### inputList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### filterArn
- **Type**: typing.Optional[str]

### filterValues
- **Type**: typing.Optional[typing.Mapping[str, str]]

### metadataColumns
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# GetPersonalizedRankingResponseTypeDef

### personalizedRanking
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_runtime_classes.PredictedItemTypeDef]
- **Required**: Yes

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommendationsRequestRequestTypeDef

### campaignArn
- **Type**: typing.Optional[str]

### itemId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### filterArn
- **Type**: typing.Optional[str]

### filterValues
- **Type**: typing.Optional[typing.Mapping[str, str]]

### recommenderArn
- **Type**: typing.Optional[str]

### promotions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_runtime_classes.PromotionTypeDef]]

### metadataColumns
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# GetRecommendationsResponseTypeDef

### itemList
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_runtime_classes.PredictedItemTypeDef]
- **Required**: Yes

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PredictedActionTypeDef

### actionId
- **Type**: typing.Optional[str]

### score
- **Type**: typing.Optional[float]


# PredictedItemTypeDef

### itemId
- **Type**: typing.Optional[str]

### score
- **Type**: typing.Optional[float]

### promotionName
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### reason
- **Type**: typing.Optional[typing.List[str]]


# PromotionTypeDef

### name
- **Type**: typing.Optional[str]

### percentPromotedItems
- **Type**: typing.Optional[int]

### filterArn
- **Type**: typing.Optional[str]

### filterValues
- **Type**: typing.Optional[typing.Mapping[str, str]]


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


