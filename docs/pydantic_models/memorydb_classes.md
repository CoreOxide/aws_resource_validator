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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthenticationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateClusterRequestTypeDef

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

### Engine
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

### MultiRegionParameterGroupName
- **Type**: typing.Optional[str]

### MultiRegionClusterName
- **Type**: typing.Optional[str]


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

### MultiRegionClusterName
- **Type**: typing.Optional[str]

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

### Engine
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


# CopySnapshotRequestTypeDef

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


# CreateACLRequestTypeDef

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


# CreateClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiRegionClusterName
- **Type**: typing.Optional[str]

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

### Engine
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


# CreateMultiRegionClusterRequestTypeDef

### MultiRegionClusterNameSuffix
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### MultiRegionParameterGroupName
- **Type**: typing.Optional[str]

### NumShards
- **Type**: typing.Optional[int]

### TLSEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.TagTypeDef]]


# CreateMultiRegionClusterResponseTypeDef

### MultiRegionCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.MultiRegionClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateParameterGroupRequestTypeDef

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


# CreateSnapshotRequestTypeDef

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


# CreateSubnetGroupRequestTypeDef

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


# CreateUserRequestTypeDef

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


# DeleteACLRequestTypeDef

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


# DeleteClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### FinalSnapshotName
- **Type**: typing.Optional[str]


# DeleteClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMultiRegionClusterRequestTypeDef

### MultiRegionClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionClusterResponseTypeDef

### MultiRegionCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.MultiRegionClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteParameterGroupRequestTypeDef

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


# DeleteSnapshotRequestTypeDef

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


# DeleteSubnetGroupRequestTypeDef

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


# DeleteUserRequestTypeDef

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


# DescribeACLsRequestPaginateTypeDef

### ACLName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeACLsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeClustersRequestPaginateTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### ShowShardDetails
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeClustersRequestTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ShowShardDetails
- **Type**: typing.Optional[bool]


# DescribeClustersResponseTypeDef

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEngineVersionsRequestPaginateTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeEngineVersionsRequestTypeDef

### Engine
- **Type**: typing.Optional[str]

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

### EngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.EngineVersionInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsRequestPaginateTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['acl', 'cluster', 'node', 'parameter-group', 'subnet-group', 'user']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeEventsRequestTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['acl', 'cluster', 'node', 'parameter-group', 'subnet-group', 'user']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsResponseTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMultiRegionClustersRequestPaginateTypeDef

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### ShowClusterDetails
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeMultiRegionClustersRequestTypeDef

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ShowClusterDetails
- **Type**: typing.Optional[bool]


# DescribeMultiRegionClustersResponseTypeDef

### MultiRegionClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.MultiRegionClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsRequestPaginateTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeParameterGroupsRequestTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsResponseTypeDef

### ParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequestPaginateTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeParametersRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersResponseTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedNodesOfferingsRequestPaginateTypeDef

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


# DescribeReservedNodesOfferingsRequestTypeDef

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

### ReservedNodesOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ReservedNodesOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedNodesRequestPaginateTypeDef

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


# DescribeReservedNodesRequestTypeDef

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

### ReservedNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ReservedNodeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceUpdatesRequestPaginateTypeDef

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ClusterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeServiceUpdatesRequestTypeDef

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

### ServiceUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.ServiceUpdateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSnapshotsRequestPaginateTypeDef

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


# DescribeSnapshotsRequestTypeDef

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

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsRequestPaginateTypeDef

### SubnetGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeSubnetGroupsRequestTypeDef

### SubnetGroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsResponseTypeDef

### SubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb_classes.SubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsersRequestPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.memorydb_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.PaginatorConfigTypeDef]


# DescribeUsersRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# EndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# EngineVersionInfoTypeDef

### Engine
- **Type**: typing.Optional[str]

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


# FailoverShardRequestTypeDef

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


# ListAllowedMultiRegionClusterUpdatesRequestTypeDef

### MultiRegionClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# ListAllowedMultiRegionClusterUpdatesResponseTypeDef

### ScaleUpNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ScaleDownNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAllowedNodeTypeUpdatesRequestTypeDef

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


# ListTagsRequestTypeDef

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


# MultiRegionClusterTypeDef

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### NumberOfShards
- **Type**: typing.Optional[int]

### Clusters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb_classes.RegionalClusterTypeDef]]

### MultiRegionParameterGroupName
- **Type**: typing.Optional[str]

### TLSEnabled
- **Type**: typing.Optional[bool]

### ARN
- **Type**: typing.Optional[str]


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


# PurchaseReservedNodesOfferingRequestTypeDef

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


# RegionalClusterTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ARN
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


# ResetParameterGroupRequestTypeDef

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


# SecurityGroupMembershipTypeDef

### SecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ServiceUpdateRequestTypeDef

### ServiceUpdateNameToApply
- **Type**: typing.Optional[str]


# ServiceUpdateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# TagResourceRequestTypeDef

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


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnprocessedClusterTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

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


# UpdateACLRequestTypeDef

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


# UpdateClusterRequestTypeDef

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

### Engine
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


# UpdateMultiRegionClusterRequestTypeDef

### MultiRegionClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### ShardConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb_classes.ShardConfigurationRequestTypeDef]

### MultiRegionParameterGroupName
- **Type**: typing.Optional[str]

### UpdateStrategy
- **Type**: typing.Optional[typing.Literal['coordinated', 'uncoordinated']]


# UpdateMultiRegionClusterResponseTypeDef

### MultiRegionCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.MultiRegionClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateParameterGroupRequestTypeDef

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


# UpdateSubnetGroupRequestTypeDef

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


# UpdateUserRequestTypeDef

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


