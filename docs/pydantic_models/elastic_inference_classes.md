# Elastic Inference Classes

# AcceleratorTypeOfferingTypeDef

### acceleratorType
- **Type**: typing.Optional[str]

### locationType
- **Type**: typing.Optional[typing.Literal['availability-zone', 'availability-zone-id', 'region']]

### location
- **Type**: typing.Optional[str]


# AcceleratorTypeTypeDef

### acceleratorTypeName
- **Type**: typing.Optional[str]

### memoryInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastic_inference_classes.MemoryInfoTypeDef]

### throughputInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastic_inference_classes.KeyValuePairTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeAcceleratorOfferingsRequestRequestTypeDef

### locationType
- **Type**: typing.Literal['availability-zone', 'availability-zone-id', 'region']
- **Required**: Yes

### acceleratorTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeAcceleratorOfferingsResponseTypeDef

### acceleratorTypeOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastic_inference_classes.AcceleratorTypeOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastic_inference_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAcceleratorTypesResponseTypeDef

### acceleratorTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastic_inference_classes.AcceleratorTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastic_inference_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAcceleratorsRequestDescribeAcceleratorsPaginateTypeDef

### acceleratorIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastic_inference_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastic_inference_classes.PaginatorConfigTypeDef]


# DescribeAcceleratorsRequestRequestTypeDef

### acceleratorIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastic_inference_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeAcceleratorsResponseTypeDef

### acceleratorSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastic_inference_classes.ElasticInferenceAcceleratorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastic_inference_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ElasticInferenceAcceleratorHealthTypeDef

### status
- **Type**: typing.Optional[str]


# ElasticInferenceAcceleratorTypeDef

### acceleratorHealth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastic_inference_classes.ElasticInferenceAcceleratorHealthTypeDef]

### acceleratorType
- **Type**: typing.Optional[str]

### acceleratorId
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### attachedResource
- **Type**: typing.Optional[str]


# FilterTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# KeyValuePairTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[int]


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastic_inference_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MemoryInfoTypeDef

### sizeInMiB
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


