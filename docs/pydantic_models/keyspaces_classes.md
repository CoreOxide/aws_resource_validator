# Keyspaces Classes

# AutoScalingPolicy

### targetTrackingScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.TargetTrackingScalingPolicyConfiguration]


# AutoScalingSettings

### autoScalingDisabled
- **Type**: typing.Optional[bool]

### minimumUnits
- **Type**: typing.Optional[int]

### maximumUnits
- **Type**: typing.Optional[int]

### scalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingPolicy]


# AutoScalingSpecification

### writeCapacityAutoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSettings]

### readCapacityAutoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSettings]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacitySpecification

### throughputMode
- **Type**: typing.Literal['PAY_PER_REQUEST', 'PROVISIONED']
- **Required**: Yes

### readCapacityUnits
- **Type**: typing.Optional[int]

### writeCapacityUnits
- **Type**: typing.Optional[int]


# CapacitySpecificationSummary

### throughputMode
- **Type**: typing.Literal['PAY_PER_REQUEST', 'PROVISIONED']
- **Required**: Yes

### readCapacityUnits
- **Type**: typing.Optional[int]

### writeCapacityUnits
- **Type**: typing.Optional[int]

### lastUpdateToPayPerRequestTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ClientSideTimestamps

### status
- **Type**: typing.Literal['ENABLED']
- **Required**: Yes


# ClusteringKey

### name
- **Type**: <class 'str'>
- **Required**: Yes

### orderBy
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# ColumnDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes


# Comment

### message
- **Type**: <class 'str'>
- **Required**: Yes


# CreateKeyspaceRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Tag]]

### replicationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicationSpecification]


# CreateKeyspaceResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTableRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### schemaDefinition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.SchemaDefinition, aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.SchemaDefinitionOutput]
- **Required**: Yes

### comment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Comment]

### capacitySpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.CapacitySpecification]

### encryptionSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.EncryptionSpecification]

### pointInTimeRecovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PointInTimeRecovery]

### ttl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.TimeToLive]

### defaultTimeToLive
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Tag]]

### clientSideTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ClientSideTimestamps]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSpecification]

### replicaSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicaSpecification]]


# CreateTableResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTypeRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.FieldDefinition]
- **Required**: Yes


# CreateTypeResponse

### keyspaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteKeyspaceRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTableRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTypeRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTypeResponse

### keyspaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionSpecification

### type
- **Type**: typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_MANAGED_KMS_KEY']
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: typing.Optional[str]


# FieldDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyspaceRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyspaceResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicationGroupStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableAutoScalingSettingsRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableAutoScalingSettingsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSpecification'>
- **Required**: Yes

### replicaSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicaAutoScalingSpecification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.SchemaDefinitionOutput'>
- **Required**: Yes

### capacitySpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.CapacitySpecificationSummary'>
- **Required**: Yes

### encryptionSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.EncryptionSpecification'>
- **Required**: Yes

### pointInTimeRecovery
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PointInTimeRecoverySummary'>
- **Required**: Yes

### ttl
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.TimeToLive'>
- **Required**: Yes

### defaultTimeToLive
- **Type**: <class 'int'>
- **Required**: Yes

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Comment'>
- **Required**: Yes

### clientSideTimestamps
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ClientSideTimestamps'>
- **Required**: Yes

### replicaSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicaSpecificationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# GetTypeRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTypeResponse

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.FieldDefinition]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# KeyspaceSummary

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


# ListKeyspacesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKeyspacesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PaginatorConfig]


# ListKeyspacesResponse

### keyspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.KeyspaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTablesRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTablesRequestPaginate

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PaginatorConfig]


# ListTablesResponse

### tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.TableSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceRequestPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PaginatorConfig]


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTypesRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTypesRequestPaginate

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PaginatorConfig]


# ListTypesResponse

### types
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartitionKey

### name
- **Type**: <class 'str'>
- **Required**: Yes


# PointInTimeRecovery

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# PointInTimeRecoverySummary

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### earliestRestorableTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ReplicaAutoScalingSpecification

### region
- **Type**: typing.Optional[str]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSpecification]


# ReplicaSpecification

### region
- **Type**: <class 'str'>
- **Required**: Yes

### readCapacityUnits
- **Type**: typing.Optional[int]

### readCapacityAutoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSettings]


# ReplicaSpecificationSummary

### region
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS', 'RESTORING', 'UPDATING']]

### capacitySpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.CapacitySpecificationSummary]


# ReplicationGroupStatus

### region
- **Type**: <class 'str'>
- **Required**: Yes

### keyspaceStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']
- **Required**: Yes

### tablesReplicationProgress
- **Type**: typing.Optional[str]


# ReplicationSpecification

### replicationStrategy
- **Type**: typing.Literal['MULTI_REGION', 'SINGLE_REGION']
- **Required**: Yes

### regionList
- **Type**: typing.Optional[typing.List[str]]


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


# RestoreTableRequest

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### capacitySpecificationOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.CapacitySpecification]

### encryptionSpecificationOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.EncryptionSpecification]

### pointInTimeRecoveryOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PointInTimeRecovery]

### tagsOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Tag]]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSpecification]

### replicaSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicaSpecification]]


# RestoreTableResponse

### restoredTableARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# SchemaDefinition

### allColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ColumnDefinition]
- **Required**: Yes

### partitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PartitionKey]
- **Required**: Yes

### clusteringKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ClusteringKey]]

### staticColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.StaticColumn]]


# SchemaDefinitionOutput

### allColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ColumnDefinition]
- **Required**: Yes

### partitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PartitionKey]
- **Required**: Yes

### clusteringKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ClusteringKey]]

### staticColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.StaticColumn]]


# StaticColumn

### name
- **Type**: <class 'str'>
- **Required**: Yes


# TableSummary

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Tag]
- **Required**: Yes


# TargetTrackingScalingPolicyConfiguration

### targetValue
- **Type**: <class 'float'>
- **Required**: Yes

### disableScaleIn
- **Type**: typing.Optional[bool]

### scaleInCooldown
- **Type**: typing.Optional[int]

### scaleOutCooldown
- **Type**: typing.Optional[int]


# TimeToLive

### status
- **Type**: typing.Literal['ENABLED']
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.Tag]
- **Required**: Yes


# UpdateKeyspaceRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### replicationSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicationSpecification'>
- **Required**: Yes

### clientSideTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ClientSideTimestamps]


# UpdateKeyspaceResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTableRequest

### keyspaceName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### addColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ColumnDefinition]]

### capacitySpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.CapacitySpecification]

### encryptionSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.EncryptionSpecification]

### pointInTimeRecovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.PointInTimeRecovery]

### ttl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.TimeToLive]

### defaultTimeToLive
- **Type**: typing.Optional[int]

### clientSideTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ClientSideTimestamps]

### autoScalingSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.AutoScalingSpecification]

### replicaSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ReplicaSpecification]]


# UpdateTableResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.keyspaces.keyspaces_classes.ResponseMetadata'>
- **Required**: Yes


