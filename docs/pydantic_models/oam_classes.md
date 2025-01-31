# oam_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLinkInputRequestTypeDef

### LabelTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Sequence[typing.Literal['AWS::ApplicationInsights::Application', 'AWS::CloudWatch::Metric', 'AWS::InternetMonitor::Monitor', 'AWS::Logs::LogGroup', 'AWS::XRay::Trace']]
- **Required**: Yes

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam_classes.LinkConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLinkOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### LabelTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### LinkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.LinkConfigurationTypeDef'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSinkInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSinkOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLinkInputRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSinkInputRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLinkInputRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLinkOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### LabelTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### LinkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.LinkConfigurationTypeDef'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSinkInputRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSinkOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSinkPolicyInputRequestTypeDef

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSinkPolicyOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### SinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LinkConfigurationTypeDef

### LogGroupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam_classes.LogGroupConfigurationTypeDef]

### MetricConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam_classes.MetricConfigurationTypeDef]


# ListAttachedLinksInputListAttachedLinksPaginateTypeDef

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam_classes.PaginatorConfigTypeDef]


# ListAttachedLinksInputRequestTypeDef

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAttachedLinksItemTypeDef

### Label
- **Type**: typing.Optional[str]

### LinkArn
- **Type**: typing.Optional[str]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]


# ListAttachedLinksOutputTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.oam_classes.ListAttachedLinksItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLinksInputListLinksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam_classes.PaginatorConfigTypeDef]


# ListLinksInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLinksItemTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### SinkArn
- **Type**: typing.Optional[str]


# ListLinksOutputTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.oam_classes.ListLinksItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSinksInputListSinksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam_classes.PaginatorConfigTypeDef]


# ListSinksInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSinksItemTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ListSinksOutputTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.oam_classes.ListSinksItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogGroupConfigurationTypeDef

### Filter
- **Type**: <class 'str'>
- **Required**: Yes


# MetricConfigurationTypeDef

### Filter
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutSinkPolicyInputRequestTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PutSinkPolicyOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### SinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
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


# TagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLinkInputRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Sequence[typing.Literal['AWS::ApplicationInsights::Application', 'AWS::CloudWatch::Metric', 'AWS::InternetMonitor::Monitor', 'AWS::Logs::LogGroup', 'AWS::XRay::Trace']]
- **Required**: Yes

### LinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam_classes.LinkConfigurationTypeDef]


# UpdateLinkOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### LabelTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### LinkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.LinkConfigurationTypeDef'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


