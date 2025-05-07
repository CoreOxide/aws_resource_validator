# Oam Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLinkInput

### LabelTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[typing.Literal['AWS::ApplicationInsights::Application', 'AWS::ApplicationSignals::Service', 'AWS::ApplicationSignals::ServiceLevelObjective', 'AWS::CloudWatch::Metric', 'AWS::InternetMonitor::Monitor', 'AWS::Logs::LogGroup', 'AWS::XRay::Trace']]
- **Required**: Yes

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LinkConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLinkOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.LinkConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSinkInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSinkOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLinkInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSinkInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLinkInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLinkOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.LinkConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes


# GetSinkInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSinkOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes


# GetSinkPolicyInput

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSinkPolicyOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes


# LinkConfiguration

### LogGroupConfiguration
- **Type**: <class 'NoneType'>

### MetricConfiguration
- **Type**: <class 'NoneType'>


# ListAttachedLinksInput

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAttachedLinksInputPaginate

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam.oam_classes.PaginatorConfig]


# ListAttachedLinksItem

### Label
- **Type**: typing.Optional[str]

### LinkArn
- **Type**: typing.Optional[str]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]


# ListAttachedLinksOutput

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.oam.oam_classes.ListAttachedLinksItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLinksInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLinksInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam.oam_classes.PaginatorConfig]


# ListLinksItem

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


# ListLinksOutput

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.oam.oam_classes.ListLinksItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSinksInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSinksInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.oam.oam_classes.PaginatorConfig]


# ListSinksItem

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ListSinksOutput

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.oam.oam_classes.ListSinksItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
- **Required**: Yes


# LogGroupConfiguration

### Filter
- **Type**: <class 'str'>
- **Required**: Yes


# MetricConfiguration

### Filter
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutSinkPolicyInput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### SinkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PutSinkPolicyOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.ResponseMetadata'>
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


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateLinkInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[typing.Literal['AWS::ApplicationInsights::Application', 'AWS::ApplicationSignals::Service', 'AWS::ApplicationSignals::ServiceLevelObjective', 'AWS::CloudWatch::Metric', 'AWS::InternetMonitor::Monitor', 'AWS::Logs::LogGroup', 'AWS::XRay::Trace']]
- **Required**: Yes

### LinkConfiguration
- **Type**: <class 'NoneType'>


# UpdateLinkOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.oam.oam_classes.LinkConfiguration'>
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


