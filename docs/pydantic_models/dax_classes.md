# Dax Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClusterTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.EndpointTypeDef]

### NodeIdsToRemove
- **Type**: typing.Optional[typing.List[str]]

### Nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.NodeTypeDef]]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.NotificationConfigurationTypeDef]

### SubnetGroup
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.SecurityGroupMembershipTypeDef]]

### IamRoleArn
- **Type**: typing.Optional[str]

### ParameterGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.ParameterGroupStatusTypeDef]

### SSEDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.SSEDescriptionTypeDef]

### ClusterEndpointEncryptionType
- **Type**: typing.Optional[typing.Literal['NONE', 'TLS']]


# CreateClusterRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dax_classes.TagTypeDef]]

### SSESpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.SSESpecificationTypeDef]

### ClusterEndpointEncryptionType
- **Type**: typing.Optional[typing.Literal['NONE', 'TLS']]


# CreateClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateParameterGroupRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateParameterGroupResponseTypeDef

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
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


# CreateSubnetGroupResponseTypeDef

### SubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.SubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DecreaseReplicationFactorRequestTypeDef

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


# DecreaseReplicationFactorResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteParameterGroupRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParameterGroupResponseTypeDef

### DeletionMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSubnetGroupRequestTypeDef

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubnetGroupResponseTypeDef

### DeletionMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClustersRequestPaginateTypeDef

### ClusterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfigTypeDef]


# DescribeClustersRequestTypeDef

### ClusterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeClustersResponseTypeDef

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.ClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDefaultParametersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfigTypeDef]


# DescribeDefaultParametersRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDefaultParametersResponseTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.ParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsRequestPaginateTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'PARAMETER_GROUP', 'SUBNET_GROUP']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfigTypeDef]


# DescribeEventsRequestTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'PARAMETER_GROUP', 'SUBNET_GROUP']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsResponseTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsRequestPaginateTypeDef

### ParameterGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfigTypeDef]


# DescribeParameterGroupsRequestTypeDef

### ParameterGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParameterGroupsResponseTypeDef

### ParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.ParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequestPaginateTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfigTypeDef]


# DescribeParametersRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersResponseTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.ParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsRequestPaginateTypeDef

### SubnetGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfigTypeDef]


# DescribeSubnetGroupsRequestTypeDef

### SubnetGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubnetGroupsResponseTypeDef

### SubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.SubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# EndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### URL
- **Type**: typing.Optional[str]


# EventTypeDef

### SourceName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'PARAMETER_GROUP', 'SUBNET_GROUP']]

### Message
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]


# IncreaseReplicationFactorRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NewReplicationFactor
- **Type**: <class 'int'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]


# IncreaseReplicationFactorResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsRequestPaginateTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.PaginatorConfigTypeDef]


# ListTagsRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NodeTypeDef

### NodeId
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dax_classes.EndpointTypeDef]

### NodeCreateTime
- **Type**: typing.Optional[datetime.datetime]

### AvailabilityZone
- **Type**: typing.Optional[str]

### NodeStatus
- **Type**: typing.Optional[str]

### ParameterGroupStatus
- **Type**: typing.Optional[str]


# NodeTypeSpecificValueTypeDef

### NodeType
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# NotificationConfigurationTypeDef

### TopicArn
- **Type**: typing.Optional[str]

### TopicStatus
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterGroupStatusTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### NodeIdsToReboot
- **Type**: typing.Optional[typing.List[str]]


# ParameterGroupTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ParameterNameValueTypeDef

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# ParameterTypeDef

### ParameterName
- **Type**: typing.Optional[str]

### ParameterType
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NODE_TYPE_SPECIFIC']]

### ParameterValue
- **Type**: typing.Optional[str]

### NodeTypeSpecificValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.NodeTypeSpecificValueTypeDef]]

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


# RebootNodeRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# RebootNodeResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
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


# SSEDescriptionTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']]


# SSESpecificationTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SecurityGroupMembershipTypeDef

### SecurityGroupIdentifier
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# SubnetGroupTypeDef

### SubnetGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dax_classes.SubnetTypeDef]]


# SubnetTypeDef

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dax_classes.TagTypeDef]
- **Required**: Yes


# TagResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.dax_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterRequestTypeDef

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


# UpdateClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateParameterGroupRequestTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterNameValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dax_classes.ParameterNameValueTypeDef]
- **Required**: Yes


# UpdateParameterGroupResponseTypeDef

### ParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.SubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dax_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


