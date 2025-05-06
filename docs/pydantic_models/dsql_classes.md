# Dsql Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClusterSummary

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateClusterInput

### deletionProtectionEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateClusterOutput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMultiRegionClustersInput

### linkedRegionList
- **Type**: typing.List[str]
- **Required**: Yes

### witnessRegion
- **Type**: <class 'str'>
- **Required**: Yes

### clusterProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.dsql.dsql_classes.LinkedClusterProperties]]

### clientToken
- **Type**: typing.Optional[str]


# CreateMultiRegionClustersOutput

### linkedClusterArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteClusterOutput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMultiRegionClustersInput

### linkedClusterArns
- **Type**: typing.List[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes


# GetClusterInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterInputWait

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetClusterInputWaitExtra

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetClusterOutput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### witnessRegion
- **Type**: <class 'str'>
- **Required**: Yes

### linkedClusterArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes


# LinkedClusterProperties

### deletionProtectionEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListClustersInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListClustersInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dsql.dsql_classes.PaginatorConfig]


# ListClustersOutput

### clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.dsql.dsql_classes.ClusterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateClusterInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtectionEnabled
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]


# UpdateClusterOutput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### witnessRegion
- **Type**: <class 'str'>
- **Required**: Yes

### linkedClusterArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dsql.dsql_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


