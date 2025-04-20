# Ebs Ebs Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Block

### BlockIndex
- **Type**: typing.Optional[int]

### BlockToken
- **Type**: typing.Optional[str]


# ChangedBlock

### BlockIndex
- **Type**: typing.Optional[int]

### FirstBlockToken
- **Type**: typing.Optional[str]

### SecondBlockToken
- **Type**: typing.Optional[str]


# CompleteSnapshotRequest

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangedBlocksCount
- **Type**: <class 'int'>
- **Required**: Yes

### Checksum
- **Type**: typing.Optional[str]

### ChecksumAlgorithm
- **Type**: typing.Optional[typing.Literal['SHA256']]

### ChecksumAggregationMethod
- **Type**: typing.Optional[typing.Literal['LINEAR']]


# CompleteSnapshotResponse

### Status
- **Type**: typing.Literal['completed', 'error', 'pending']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ebs.ebs_classes.ResponseMetadata'>
- **Required**: Yes


# GetSnapshotBlockRequest

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### BlockIndex
- **Type**: <class 'int'>
- **Required**: Yes

### BlockToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetSnapshotBlockResponse

### DataLength
- **Type**: <class 'int'>
- **Required**: Yes

### BlockData
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### Checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ChecksumAlgorithm
- **Type**: typing.Literal['SHA256']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ebs.ebs_classes.ResponseMetadata'>
- **Required**: Yes


# ListChangedBlocksRequest

### SecondSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### FirstSnapshotId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartingBlockIndex
- **Type**: typing.Optional[int]


# ListChangedBlocksResponse

### ChangedBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ebs.ebs_classes.ChangedBlock]
- **Required**: Yes

### ExpiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VolumeSize
- **Type**: <class 'int'>
- **Required**: Yes

### BlockSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ebs.ebs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSnapshotBlocksRequest

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartingBlockIndex
- **Type**: typing.Optional[int]


# ListSnapshotBlocksResponse

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ebs.ebs_classes.Block]
- **Required**: Yes

### ExpiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VolumeSize
- **Type**: <class 'int'>
- **Required**: Yes

### BlockSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ebs.ebs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PutSnapshotBlockRequest

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### BlockIndex
- **Type**: <class 'int'>
- **Required**: Yes

### BlockData
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### DataLength
- **Type**: <class 'int'>
- **Required**: Yes

### Checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ChecksumAlgorithm
- **Type**: typing.Literal['SHA256']
- **Required**: Yes

### Progress
- **Type**: typing.Optional[int]


# PutSnapshotBlockResponse

### Checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ChecksumAlgorithm
- **Type**: typing.Literal['SHA256']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ebs.ebs_classes.ResponseMetadata'>
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


# StartSnapshotRequest

### VolumeSize
- **Type**: <class 'int'>
- **Required**: Yes

### ParentSnapshotId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ebs.ebs_classes.Tag]]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyArn
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]


# StartSnapshotResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['completed', 'error', 'pending']
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VolumeSize
- **Type**: <class 'int'>
- **Required**: Yes

### BlockSize
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ebs.ebs_classes.Tag]
- **Required**: Yes

### ParentSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### SseType
- **Type**: typing.Literal['none', 'sse-ebs', 'sse-kms']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ebs.ebs_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


