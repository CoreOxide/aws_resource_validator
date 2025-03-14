# Keyspaces Classes

# AutoScalingPolicyTypeDef

### targetTrackingScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.TargetTrackingScalingPolicyConfigurationTypeDef]


# AutoScalingSettingsTypeDef

### autoScalingDisabled
- **Type**: typing.Optional[bool]

### minimumUnits
- **Type**: typing.Optional[int]

### maximumUnits
- **Type**: typing.Optional[int]

### scalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingPolicyTypeDef]


# AutoScalingSpecificationTypeDef

### writeCapacityAutoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSettingsTypeDef]

### readCapacityAutoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSettingsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacitySpecificationSummaryTypeDef

### throughputMode
- **Type**: typing.Literal['PAY_PER_REQUEST', 'PROVISIONED']
- **Required**: Yes

### readCapacityUnits
- **Type**: typing.Optional[int]

### writeCapacityUnits
- **Type**: typing.Optional[int]

### lastUpdateToPayPerRequestTimestamp
- **Type**: typing.Optional[datetime.datetime]


# CapacitySpecificationTypeDef

### throughputMode
- **Type**: typing.Literal['PAY_PER_REQUEST', 'PROVISIONED']
- **Required**: Yes

### readCapacityUnits
- **Type**: typing.Optional[int]

### writeCapacityUnits
- **Type**: typing.Optional[int]


# ClientSideTimestampsTypeDef

### status
- **Type**: typing.Literal['ENABLED']
- **Required**: Yes


# ClusteringKeyTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### orderBy
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# ColumnDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommentTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# CreateKeyspaceRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.TagTypeDef]]

### replicationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.ReplicationSpecificationTypeDef]


# CreateKeyspaceResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTableRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### schemaDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.SchemaDefinitionUnionTypeDef'>
- **Required**: Yes

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.CommentTypeDef]

### capacitySpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.CapacitySpecificationTypeDef]

### encryptionSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.EncryptionSpecificationTypeDef]

### pointInTimeRecovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.PointInTimeRecoveryTypeDef]

### ttl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.TimeToLiveTypeDef]

### defaultTimeToLive
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.TagTypeDef]]

### clientSideTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.ClientSideTimestampsTypeDef]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSpecificationTypeDef]

### replicaSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.ReplicaSpecificationTypeDef]]


# CreateTableResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTypeRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.FieldDefinitionTypeDef]
- **Required**: Yes


# CreateTypeResponseTypeDef

### keyspaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteKeyspaceRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTableRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTypeRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTypeResponseTypeDef

### keyspaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionSpecificationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetKeyspaceRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyspaceResponseTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### replicationStrategy
- **Type**: typing.Literal['MULTI_REGION', 'SINGLE_REGION']
- **Required**: Yes

### replicationRegions
- **Type**: typing.List[str]
- **Required**: Yes

### replicationGroupStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.ReplicationGroupStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableAutoScalingSettingsRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableAutoScalingSettingsResponseTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### autoScalingSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSpecificationTypeDef'>
- **Required**: Yes

### replicaSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.ReplicaAutoScalingSpecificationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableResponseTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS', 'RESTORING', 'UPDATING']
- **Required**: Yes

### schemaDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.SchemaDefinitionOutputTypeDef'>
- **Required**: Yes

### capacitySpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.CapacitySpecificationSummaryTypeDef'>
- **Required**: Yes

### encryptionSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.EncryptionSpecificationTypeDef'>
- **Required**: Yes

### pointInTimeRecovery
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.PointInTimeRecoverySummaryTypeDef'>
- **Required**: Yes

### ttl
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.TimeToLiveTypeDef'>
- **Required**: Yes

### defaultTimeToLive
- **Type**: <class 'int'>
- **Required**: Yes

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.CommentTypeDef'>
- **Required**: Yes

### clientSideTimestamps
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ClientSideTimestampsTypeDef'>
- **Required**: Yes

### replicaSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.ReplicaSpecificationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTypeRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTypeResponseTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.FieldDefinitionTypeDef]
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'RESTORING']
- **Required**: Yes

### directReferringTables
- **Type**: typing.List[str]
- **Required**: Yes

### directParentTypes
- **Type**: typing.List[str]
- **Required**: Yes

### maxNestingDepth
- **Type**: <class 'int'>
- **Required**: Yes

### keyspaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KeyspaceSummaryTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### replicationStrategy
- **Type**: typing.Literal['MULTI_REGION', 'SINGLE_REGION']
- **Required**: Yes

### replicationRegions
- **Type**: typing.Optional[typing.List[str]]


# ListKeyspacesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.PaginatorConfigTypeDef]


# ListKeyspacesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKeyspacesResponseTypeDef

### keyspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.KeyspaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTablesRequestPaginateTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.PaginatorConfigTypeDef]


# ListTablesRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTablesResponseTypeDef

### tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.TableSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTypesRequestPaginateTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.PaginatorConfigTypeDef]


# ListTypesRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartitionKeyTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# PointInTimeRecoverySummaryTypeDef

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### earliestRestorableTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PointInTimeRecoveryTypeDef

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# ReplicaAutoScalingSpecificationTypeDef

### region
- **Type**: typing.Optional[str]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSpecificationTypeDef]


# ReplicaSpecificationSummaryTypeDef

### region
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS', 'RESTORING', 'UPDATING']]

### capacitySpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.CapacitySpecificationSummaryTypeDef]


# ReplicaSpecificationTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### readCapacityUnits
- **Type**: typing.Optional[int]

### readCapacityAutoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSettingsTypeDef]


# ReplicationGroupStatusTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### keyspaceStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']
- **Required**: Yes

### tablesReplicationProgress
- **Type**: typing.Optional[str]


# ReplicationSpecificationTypeDef

### replicationStrategy
- **Type**: typing.Literal['MULTI_REGION', 'SINGLE_REGION']
- **Required**: Yes

### regionList
- **Type**: typing.Optional[typing.Sequence[str]]


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


# RestoreTableRequestTypeDef

### sourceKeyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceTableName
- **Type**: <class 'str'>
- **Required**: Yes

### targetKeyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### targetTableName
- **Type**: <class 'str'>
- **Required**: Yes

### restoreTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.TimestampTypeDef]

### capacitySpecificationOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.CapacitySpecificationTypeDef]

### encryptionSpecificationOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.EncryptionSpecificationTypeDef]

### pointInTimeRecoveryOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.PointInTimeRecoveryTypeDef]

### tagsOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.TagTypeDef]]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSpecificationTypeDef]

### replicaSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.ReplicaSpecificationTypeDef]]


# RestoreTableResponseTypeDef

### restoredTableARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SchemaDefinitionOutputTypeDef

### allColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.ColumnDefinitionTypeDef]
- **Required**: Yes

### partitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.PartitionKeyTypeDef]
- **Required**: Yes

### clusteringKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.ClusteringKeyTypeDef]]

### staticColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces_classes.StaticColumnTypeDef]]


# SchemaDefinitionTypeDef

### allColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.ColumnDefinitionTypeDef]
- **Required**: Yes

### partitionKeys
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.PartitionKeyTypeDef]
- **Required**: Yes

### clusteringKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.ClusteringKeyTypeDef]]

### staticColumns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.StaticColumnTypeDef]]


# SchemaDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StaticColumnTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# TableSummaryTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetTrackingScalingPolicyConfigurationTypeDef

### targetValue
- **Type**: <class 'float'>
- **Required**: Yes

### disableScaleIn
- **Type**: typing.Optional[bool]

### scaleInCooldown
- **Type**: typing.Optional[int]

### scaleOutCooldown
- **Type**: typing.Optional[int]


# TimeToLiveTypeDef

### status
- **Type**: typing.Literal['ENABLED']
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.TagTypeDef]
- **Required**: Yes


# UpdateKeyspaceRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### replicationSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ReplicationSpecificationTypeDef'>
- **Required**: Yes

### clientSideTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.ClientSideTimestampsTypeDef]


# UpdateKeyspaceResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTableRequestTypeDef

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### addColumns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.ColumnDefinitionTypeDef]]

### capacitySpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.CapacitySpecificationTypeDef]

### encryptionSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.EncryptionSpecificationTypeDef]

### pointInTimeRecovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.PointInTimeRecoveryTypeDef]

### ttl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.TimeToLiveTypeDef]

### defaultTimeToLive
- **Type**: typing.Optional[int]

### clientSideTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.ClientSideTimestampsTypeDef]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces_classes.AutoScalingSpecificationTypeDef]

### replicaSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.keyspaces_classes.ReplicaSpecificationTypeDef]]


# UpdateTableResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


