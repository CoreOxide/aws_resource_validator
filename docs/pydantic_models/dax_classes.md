# Dax Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Cluster

### ClusterName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### TotalNodes
- **Type**: typing.Optional[int]

### ActiveNodes
- **Type**: typing.Optional[int]

### NodeType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ClusterDiscoveryEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.Endpoint]

### NodeIdsToRemove
- **Type**: typing.Optional[typing.List[str]]

### Nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.Node]]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: <class 'NoneType'>

### SubnetGroup
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.SecurityGroupMembership]]

### IamRoleArn
- **Type**: typing.Optional[str]

### ParameterGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.ParameterGroupStatus]

### SSEDescription
- **Type**: <class 'NoneType'>

### ClusterEndpointEncryptionType
- **Type**: typing.Optional[typing.Literal['NONE', 'TLS']]


# CreateClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationFactor
- **Type**: <class 'int'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetGroupName
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### NotificationTopicArn
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dax_classes.Tag]]

### SSESpecification
- **Type**: <class 'NoneType'>

### ClusterEndpointEncryptionType
- **Type**: typing.Optional[typing.Literal['NONE', 'TLS']]


# CreateClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# CreateParameterGroupRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateParameterGroupResponse

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubnetGroupRequest

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateSubnetGroupResponse

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.SubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# DecreaseReplicationFactorRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NewReplicationFactor
- **Type**: <class 'int'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### NodeIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# DecreaseReplicationFactorResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteParameterGroupRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParameterGroupResponse

### DeletionMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSubnetGroupRequest

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubnetGroupResponse

### DeletionMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClustersRequest

### ClusterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeClustersRequestPaginate

### ClusterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfig]


# DescribeClustersResponse

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.Cluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDefaultParametersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDefaultParametersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfig]


# DescribeDefaultParametersResponse

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.Parameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsRequest

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'PARAMETER_GROUP', 'SUBNET_GROUP']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.Timestamp]

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
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'PARAMETER_GROUP', 'SUBNET_GROUP']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.Timestamp]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfig]


# DescribeEventsResponse

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsRequest

### ParameterGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsRequestPaginate

### ParameterGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfig]


# DescribeParameterGroupsResponse

### ParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.ParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequestPaginate

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfig]


# DescribeParametersResponse

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.Parameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsRequest

### SubnetGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsRequestPaginate

### SubnetGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfig]


# DescribeSubnetGroupsResponse

### SubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.SubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Endpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### URL
- **Type**: typing.Optional[str]


# Event

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'PARAMETER_GROUP', 'SUBNET_GROUP']]

### Message
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]


# IncreaseReplicationFactorRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NewReplicationFactor
- **Type**: <class 'int'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]


# IncreaseReplicationFactorResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsRequest

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestPaginate

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfig]


# ListTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Node

### NodeId
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: <class 'NoneType'>

### NodeCreateTime
- **Type**: typing.Optional[datetime.datetime]

### AvailabilityZone
- **Type**: typing.Optional[str]

### NodeStatus
- **Type**: typing.Optional[str]

### ParameterGroupStatus
- **Type**: typing.Optional[str]


# NodeTypeSpecificValue

### NodeType
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# NotificationConfiguration

### TopicArn
- **Type**: typing.Optional[str]

### TopicStatus
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

### ParameterName
- **Type**: typing.Optional[str]

### ParameterType
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NODE_TYPE_SPECIFIC']]

### ParameterValue
- **Type**: typing.Optional[str]

### NodeTypeSpecificValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.NodeTypeSpecificValue]]

### Description
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### IsModifiable
- **Type**: typing.Optional[typing.Literal['CONDITIONAL', 'FALSE', 'TRUE']]

### ChangeType
- **Type**: typing.Optional[typing.Literal['IMMEDIATE', 'REQUIRES_REBOOT']]


# ParameterGroup

### ParameterGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ParameterGroupStatus

### ParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### NodeIdsToReboot
- **Type**: typing.Optional[typing.List[str]]


# ParameterNameValue

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# RebootNodeRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# RebootNodeResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
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


# SSEDescription

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']]


# SSESpecification

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SecurityGroupMembership

### SecurityGroupIdentifier
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# Subnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]


# SubnetGroup

### SubnetGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.Subnet]]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dax_classes.Tag]
- **Required**: Yes


# TagResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### NotificationTopicArn
- **Type**: typing.Optional[str]

### NotificationTopicStatus
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateParameterGroupRequest

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterNameValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dax_classes.ParameterNameValue]
- **Required**: Yes


# UpdateParameterGroupResponse

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubnetGroupRequest

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateSubnetGroupResponse

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.SubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadata'>
- **Required**: Yes


