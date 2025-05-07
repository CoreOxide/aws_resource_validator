# Memorydb Classes

# ACL

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### UserNames
- **Type**: typing.Optional[typing.List[str]]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### PendingChanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ACLPendingChanges]

### Clusters
- **Type**: typing.Optional[typing.List[str]]

### ARN
- **Type**: typing.Optional[str]


# ACLPendingChanges

### UserNamesToRemove
- **Type**: typing.Optional[typing.List[str]]

### UserNamesToAdd
- **Type**: typing.Optional[typing.List[str]]


# ACLsUpdateStatus

### ACLToApply
- **Type**: typing.Optional[str]


# Authentication

### Type
- **Type**: typing.Optional[typing.Literal['iam', 'no-password', 'password']]

### PasswordCount
- **Type**: typing.Optional[int]


# AuthenticationMode

### Type
- **Type**: typing.Optional[typing.Literal['iam', 'password']]

### Passwords
- **Type**: typing.Optional[typing.List[str]]


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateClusterRequest

### ClusterNames
- **Type**: typing.List[str]
- **Required**: Yes

### ServiceUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ServiceUpdateRequest]


# BatchUpdateClusterResponse

### ProcessedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Cluster]
- **Required**: Yes

### UnprocessedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.UnprocessedCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# Cluster

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### PendingUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ClusterPendingUpdates]

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### NumberOfShards
- **Type**: typing.Optional[int]

### Shards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Shard]]

### AvailabilityMode
- **Type**: typing.Optional[typing.Literal['multiaz', 'singleaz']]

### ClusterEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Endpoint]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.SecurityGroupMembership]]

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


# ClusterConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ShardDetail]]

### MultiRegionParameterGroupName
- **Type**: typing.Optional[str]

### MultiRegionClusterName
- **Type**: typing.Optional[str]


# ClusterPendingUpdates

### Resharding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ReshardingStatus]

### ACLs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ACLsUpdateStatus]

### ServiceUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PendingModifiedServiceUpdate]]


# CopySnapshotRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# CopySnapshotResponse

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateACLRequest

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes

### UserNames
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# CreateACLResponse

### ACL
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ACL'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterRequest

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
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[str]]

### SnapshotName
- **Type**: typing.Optional[str]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]

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


# CreateClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMultiRegionClusterRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# CreateMultiRegionClusterResponse

### MultiRegionCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.MultiRegionCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateParameterGroupRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Family
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# CreateParameterGroupResponse

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# CreateSnapshotResponse

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubnetGroupRequest

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# CreateSubnetGroupResponse

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.SubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMode
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.AuthenticationMode'>
- **Required**: Yes

### AccessString
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# CreateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteACLRequest

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteACLResponse

### ACL
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ACL'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### FinalSnapshotName
- **Type**: typing.Optional[str]


# DeleteClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMultiRegionClusterRequest

### MultiRegionClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionClusterResponse

### MultiRegionCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.MultiRegionCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteParameterGroupRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParameterGroupResponse

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSnapshotRequest

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResponse

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSubnetGroupRequest

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubnetGroupResponse

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.SubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeACLsRequest

### ACLName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeACLsRequestPaginate

### ACLName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeACLsResponse

### ACLs
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ACL]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeClustersRequest

### ClusterName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ShowShardDetails
- **Type**: typing.Optional[bool]


# DescribeClustersRequestPaginate

### ClusterName
- **Type**: typing.Optional[str]

### ShowShardDetails
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeClustersResponse

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Cluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEngineVersionsRequest

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


# DescribeEngineVersionsRequestPaginate

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeEngineVersionsResponse

### EngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.EngineVersionInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsRequest

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


# DescribeEventsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeEventsResponse

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMultiRegionClustersRequest

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ShowClusterDetails
- **Type**: typing.Optional[bool]


# DescribeMultiRegionClustersRequestPaginate

### MultiRegionClusterName
- **Type**: typing.Optional[str]

### ShowClusterDetails
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeMultiRegionClustersResponse

### MultiRegionClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.MultiRegionCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsRequest

### ParameterGroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsRequestPaginate

### ParameterGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeParameterGroupsResponse

### ParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequestPaginate

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeParametersResponse

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Parameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedNodesOfferingsRequest

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


# DescribeReservedNodesOfferingsRequestPaginate

### ReservedNodesOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeReservedNodesOfferingsResponse

### ReservedNodesOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ReservedNodesOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedNodesRequest

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


# DescribeReservedNodesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeReservedNodesResponse

### ReservedNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ReservedNode]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceUpdatesRequest

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ClusterNames
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[typing.List[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceUpdatesRequestPaginate

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ClusterNames
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[typing.List[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeServiceUpdatesResponse

### ServiceUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ServiceUpdate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSnapshotsRequest

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


# DescribeSnapshotsRequestPaginate

### ClusterName
- **Type**: typing.Optional[str]

### SnapshotName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### ShowDetail
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeSnapshotsResponse

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Snapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsRequest

### SubnetGroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsRequestPaginate

### SubnetGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeSubnetGroupsResponse

### SubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.SubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsersRequest

### UserName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsersRequestPaginate

### UserName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.PaginatorConfig]


# DescribeUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Endpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# EngineVersionInfo

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EnginePatchVersion
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]


# Event

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['acl', 'cluster', 'node', 'parameter-group', 'subnet-group', 'user']]

### Message
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]


# FailoverShardRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### ShardName
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverShardResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ListAllowedMultiRegionClusterUpdatesRequest

### MultiRegionClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# ListAllowedMultiRegionClusterUpdatesResponse

### ScaleUpNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ScaleDownNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# ListAllowedNodeTypeUpdatesRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# ListAllowedNodeTypeUpdatesResponse

### ScaleUpNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ScaleDownNodeTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# MultiRegionCluster

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.RegionalCluster]]

### MultiRegionParameterGroupName
- **Type**: typing.Optional[str]

### TLSEnabled
- **Type**: typing.Optional[bool]

### ARN
- **Type**: typing.Optional[str]


# Node

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoint
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

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


# ParameterGroup

### Name
- **Type**: typing.Optional[str]

### Family
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# ParameterNameValue

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# PendingModifiedServiceUpdate

### ServiceUpdateName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['available', 'complete', 'in-progress', 'scheduled']]


# PurchaseReservedNodesOfferingRequest

### ReservedNodesOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationId
- **Type**: typing.Optional[str]

### NodeCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]]


# PurchaseReservedNodesOfferingResponse

### ReservedNode
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ReservedNode'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# RecurringCharge

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RegionalCluster

### ClusterName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# ReplicaConfigurationRequest

### ReplicaCount
- **Type**: typing.Optional[int]


# ReservedNode

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.RecurringCharge]]

### ARN
- **Type**: typing.Optional[str]


# ReservedNodesOffering

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.RecurringCharge]]


# ResetParameterGroupRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AllParameters
- **Type**: typing.Optional[bool]

### ParameterNames
- **Type**: typing.Optional[typing.List[str]]


# ResetParameterGroupResponse

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# ReshardingStatus

### SlotMigration
- **Type**: <class 'NoneType'>


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


# SecurityGroupMembership

### SecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ServiceUpdate

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

### Engine
- **Type**: typing.Optional[str]

### NodesUpdated
- **Type**: typing.Optional[str]

### AutoUpdateStartDate
- **Type**: typing.Optional[datetime.datetime]


# ServiceUpdateRequest

### ServiceUpdateNameToApply
- **Type**: typing.Optional[str]


# Shard

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[str]

### Nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Node]]

### NumberOfNodes
- **Type**: typing.Optional[int]


# ShardConfiguration

### Slots
- **Type**: typing.Optional[str]

### ReplicaCount
- **Type**: typing.Optional[int]


# ShardConfigurationRequest

### ShardCount
- **Type**: typing.Optional[int]


# ShardDetail

### Name
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ShardConfiguration]

### Size
- **Type**: typing.Optional[str]

### SnapshotCreationTime
- **Type**: typing.Optional[datetime.datetime]


# SlotMigration

### ProgressPercentage
- **Type**: typing.Optional[float]


# Snapshot

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
- **Type**: <class 'NoneType'>

### DataTiering
- **Type**: typing.Optional[typing.Literal['false', 'true']]


# Subnet

### Identifier
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: <class 'NoneType'>


# SubnetGroup

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Subnet]]

### ARN
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]
- **Required**: Yes


# TagResourceResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# UnprocessedCluster

### ClusterName
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagResourceResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateACLRequest

### ACLName
- **Type**: <class 'str'>
- **Required**: Yes

### UserNamesToAdd
- **Type**: typing.Optional[typing.List[str]]

### UserNamesToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateACLResponse

### ACL
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ACL'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ReplicaConfigurationRequest]

### ShardConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ShardConfigurationRequest]

### ACLName
- **Type**: typing.Optional[str]


# UpdateClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMultiRegionClusterRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ShardConfigurationRequest]

### MultiRegionParameterGroupName
- **Type**: typing.Optional[str]

### UpdateStrategy
- **Type**: typing.Optional[typing.Literal['coordinated', 'uncoordinated']]


# UpdateMultiRegionClusterResponse

### MultiRegionCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.MultiRegionCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateParameterGroupRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterNameValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ParameterNameValue]
- **Required**: Yes


# UpdateParameterGroupResponse

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubnetGroupRequest

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]


# UpdateSubnetGroupResponse

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.SubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMode
- **Type**: <class 'NoneType'>

### AccessString
- **Type**: typing.Optional[str]


# UpdateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.memorydb.memorydb_classes.ResponseMetadata'>
- **Required**: Yes


# User

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
- **Type**: <class 'NoneType'>

### ARN
- **Type**: typing.Optional[str]


