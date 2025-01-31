# Memorydb Classes

# ACLPendingChangesTypeDef

### UserNamesToRemove
- **Type**: typing.Optional[typing.List[str]]

### UserNamesToAdd
- **Type**: typing.Optional[typing.List[str]]


# ACLTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### UserNames
- **Type**: typing.Optional[typing.List[str]]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### PendingChanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ACLPendingChangesTypeDef]

### Clusters
- **Type**: typing.Optional[typing.List[str]]

### ARN
- **Type**: typing.Optional[str]


# ACLsUpdateStatusTypeDef

### ACLToApply
- **Type**: typing.Optional[str]


# AuthenticationModeTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['iam', 'password']]

### Passwords
- **Type**: typing.Optional[typing.Sequence[str]]


# AuthenticationTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['iam', 'no-password', 'password']]

### PasswordCount
- **Type**: typing.Optional[int]


# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateClusterRequestRequestTypeDef

### ClusterNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ServiceUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ServiceUpdateRequestTypeDef]


# BatchUpdateClusterResponseTypeDef

### ProcessedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef]
- **Required**: Yes

### UnprocessedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.UnprocessedClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterConfigurationTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### MaintenanceWindow
- **Type**: typing.Optional[str]

### TopicArn
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ParameterGroupName
- **Type**: typing.Optional[str]

### SubnetGroupName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### NumShards
- **Type**: typing.Optional[int]

### Shards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ShardDetailTypeDef]]


# ClusterPendingUpdatesTypeDef

### Resharding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ReshardingStatusTypeDef]

### ACLs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ACLsUpdateStatusTypeDef]

### ServiceUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.PendingModifiedServiceUpdateTypeDef]]


# ClusterTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### PendingUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ClusterPendingUpdatesTypeDef]

### NumberOfShards
- **Type**: typing.Optional[int]

### Shards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ShardTypeDef]]

### AvailabilityMode
- **Type**: typing.Optional[typing.Literal['multiaz', 'singleaz']]

### ClusterEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.EndpointTypeDef]

### NodeType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EnginePatchVersion
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]

### ParameterGroupStatus
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.SecurityGroupMembershipTypeDef]]

### SubnetGroupName
- **Type**: typing.Optional[str]

### TLSEnabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SnsTopicStatus
- **Type**: typing.Optional[str]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### MaintenanceWindow
- **Type**: typing.Optional[str]

### SnapshotWindow
- **Type**: typing.Optional[str]

### ACLName
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### DataTiering
- **Type**: typing.Optional[typing.Literal['false', 'true']]


# CopySnapshotRequestRequestTypeDef

### SourceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBucket
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# CopySnapshotResponseTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateACLRequestRequestTypeDef

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes

### UserNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# CreateACLResponseTypeDef

### ACL
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ACLTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterRequestRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NumShards
- **Type**: typing.Optional[int]

### NumReplicasPerShard
- **Type**: typing.Optional[int]

### SubnetGroupName
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaintenanceWindow
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### SnsTopicArn
- **Type**: typing.Optional[str]

### TLSEnabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### SnapshotArns
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotName
- **Type**: typing.Optional[str]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]

### SnapshotWindow
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### DataTiering
- **Type**: typing.Optional[bool]


# CreateClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateParameterGroupRequestRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Family
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# CreateParameterGroupResponseTypeDef

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotRequestRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# CreateSnapshotResponseTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubnetGroupRequestRequestTypeDef

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# CreateSubnetGroupResponseTypeDef

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.SubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMode
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.AuthenticationModeTypeDef'>
- **Required**: Yes

### AccessString
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# CreateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteACLRequestRequestTypeDef

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteACLResponseTypeDef

### ACL
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ACLTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterRequestRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### FinalSnapshotName
- **Type**: typing.Optional[str]


# DeleteClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteParameterGroupRequestRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParameterGroupResponseTypeDef

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSnapshotRequestRequestTypeDef

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResponseTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSubnetGroupRequestRequestTypeDef

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubnetGroupResponseTypeDef

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.SubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeACLsRequestDescribeACLsPaginateTypeDef

### ACLName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeACLsRequestRequestTypeDef

### ACLName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeACLsResponseTypeDef

### ACLs
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ACLTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClustersRequestDescribeClustersPaginateTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### ShowShardDetails
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeClustersRequestRequestTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ShowShardDetails
- **Type**: typing.Optional[bool]


# DescribeClustersResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef

### EngineVersion
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeEngineVersionsRequestRequestTypeDef

### EngineVersion
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]


# DescribeEngineVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.EngineVersionInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventsRequestDescribeEventsPaginateTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['acl', 'cluster', 'node', 'parameter-group', 'subnet-group', 'user']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeEventsRequestRequestTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['acl', 'cluster', 'node', 'parameter-group', 'subnet-group', 'user']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeParameterGroupsRequestRequestTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeParametersRequestDescribeParametersPaginateTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeParametersRequestRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef

### ReservedNodesOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeReservedNodesOfferingsRequestRequestTypeDef

### ReservedNodesOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedNodesOfferingsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodesOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ReservedNodesOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef

### ReservationId
- **Type**: typing.Optional[str]

### ReservedNodesOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeReservedNodesRequestRequestTypeDef

### ReservationId
- **Type**: typing.Optional[str]

### ReservedNodesOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedNodesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ReservedNodeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ClusterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeServiceUpdatesRequestRequestTypeDef

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ClusterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceUpdatesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ServiceUpdateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### SnapshotName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### ShowDetail
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeSnapshotsRequestRequestTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### SnapshotName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ShowDetail
- **Type**: typing.Optional[bool]


# DescribeSnapshotsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef

### SubnetGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeSubnetGroupsRequestRequestTypeDef

### SubnetGroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.SubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUsersRequestDescribeUsersPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeUsersRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.UserTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# EngineVersionInfoTypeDef

### EngineVersion
- **Type**: typing.Optional[str]

### EnginePatchVersion
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]


# EventTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['acl', 'cluster', 'node', 'parameter-group', 'subnet-group', 'user']]

### Message
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]


# FailoverShardRequestRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### ShardName
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverShardResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ListAllowedNodeTypeUpdatesRequestRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# ListAllowedNodeTypeUpdatesResponseTypeDef

### ScaleUpNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ScaleDownNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NodeTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.EndpointTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterGroupTypeDef

### Name
- **Type**: typing.Optional[str]

### Family
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# ParameterNameValueTypeDef

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# ParameterTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### MinimumEngineVersion
- **Type**: typing.Optional[str]


# PendingModifiedServiceUpdateTypeDef

### ServiceUpdateName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]


# PurchaseReservedNodesOfferingRequestRequestTypeDef

### ReservedNodesOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationId
- **Type**: typing.Optional[str]

### NodeCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# PurchaseReservedNodesOfferingResponseTypeDef

### ReservedNode
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ReservedNodeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecurringChargeTypeDef

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# ReplicaConfigurationRequestTypeDef

### ReplicaCount
- **Type**: typing.Optional[int]


# ReservedNodeTypeDef

### ReservationId
- **Type**: typing.Optional[str]

### ReservedNodesOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### NodeCount
- **Type**: typing.Optional[int]

### OfferingType
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.RecurringChargeTypeDef]]

### ARN
- **Type**: typing.Optional[str]


# ReservedNodesOfferingTypeDef

### ReservedNodesOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### OfferingType
- **Type**: typing.Optional[str]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.RecurringChargeTypeDef]]


# ResetParameterGroupRequestRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AllParameters
- **Type**: typing.Optional[bool]

### ParameterNames
- **Type**: typing.Optional[typing.Sequence[str]]


# ResetParameterGroupResponseTypeDef

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReshardingStatusTypeDef

### SlotMigration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.SlotMigrationTypeDef]


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


# SecurityGroupMembershipTypeDef

### SecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ServiceUpdateRequestTypeDef

### ServiceUpdateNameToApply
- **Type**: typing.Optional[str]


# ServiceUpdateTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]

### Type
- **Type**: typing.Optional[typing.Literal['security-update']]

### NodesUpdated
- **Type**: typing.Optional[str]

### AutoUpdateStartDate
- **Type**: typing.Optional[datetime.datetime]


# ShardConfigurationRequestTypeDef

### ShardCount
- **Type**: typing.Optional[int]


# ShardConfigurationTypeDef

### Slots
- **Type**: typing.Optional[str]

### ReplicaCount
- **Type**: typing.Optional[int]


# ShardDetailTypeDef

### Name
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ShardConfigurationTypeDef]

### Size
- **Type**: typing.Optional[str]

### SnapshotCreationTime
- **Type**: typing.Optional[datetime.datetime]


# ShardTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[str]

### Nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.NodeTypeDef]]

### NumberOfNodes
- **Type**: typing.Optional[int]


# SlotMigrationTypeDef

### ProgressPercentage
- **Type**: typing.Optional[float]


# SnapshotTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### ClusterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ClusterConfigurationTypeDef]

### DataTiering
- **Type**: typing.Optional[typing.Literal['false', 'true']]


# SubnetGroupTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.SubnetTypeDef]]

### ARN
- **Type**: typing.Optional[str]


# SubnetTypeDef

### Identifier
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.AvailabilityZoneTypeDef]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]
- **Required**: Yes


# TagResourceResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UnprocessedClusterTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateACLRequestRequestTypeDef

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes

### UserNamesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### UserNamesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateACLResponseTypeDef

### ACL
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ACLTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterRequestRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaintenanceWindow
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SnsTopicStatus
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]

### SnapshotWindow
- **Type**: typing.Optional[str]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### NodeType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### ReplicaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ReplicaConfigurationRequestTypeDef]

### ShardConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ShardConfigurationRequestTypeDef]

### ACLName
- **Type**: typing.Optional[str]


# UpdateClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateParameterGroupRequestRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterNameValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.ParameterNameValueTypeDef]
- **Required**: Yes


# UpdateParameterGroupResponseTypeDef

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSubnetGroupRequestRequestTypeDef

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateSubnetGroupResponseTypeDef

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.SubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.AuthenticationModeTypeDef]

### AccessString
- **Type**: typing.Optional[str]


# UpdateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### AccessString
- **Type**: typing.Optional[str]

### ACLNames
- **Type**: typing.Optional[typing.List[str]]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### Authentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.AuthenticationTypeDef]

### ARN
- **Type**: typing.Optional[str]


