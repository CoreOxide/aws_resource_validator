# Timestream Influxdb Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDbClusterInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes

### dbInstanceType
- **Type**: typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']
- **Required**: Yes

### allocatedStorage
- **Type**: <class 'int'>
- **Required**: Yes

### vpcSubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### deploymentType
- **Type**: typing.Literal['MULTI_NODE_READ_REPLICAS']
- **Required**: Yes

### username
- **Type**: typing.Optional[str]

### organization
- **Type**: typing.Optional[str]

### bucket
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### dbParameterGroupIdentifier
- **Type**: typing.Optional[str]

### dbStorageType
- **Type**: typing.Optional[typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']]

### networkType
- **Type**: typing.Optional[typing.Literal['DUAL', 'IPV4']]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### failoverMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'NO_FAILOVER']]

### logDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDbClusterOutputTypeDef

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### dbClusterStatus
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDbInstanceInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes

### dbInstanceType
- **Type**: typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']
- **Required**: Yes

### vpcSubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### allocatedStorage
- **Type**: <class 'int'>
- **Required**: Yes

### username
- **Type**: typing.Optional[str]

### organization
- **Type**: typing.Optional[str]

### bucket
- **Type**: typing.Optional[str]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### dbStorageType
- **Type**: typing.Optional[typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']]

### dbParameterGroupIdentifier
- **Type**: typing.Optional[str]

### deploymentType
- **Type**: typing.Optional[typing.Literal['SINGLE_AZ', 'WITH_MULTIAZ_STANDBY']]

### logDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### port
- **Type**: typing.Optional[int]

### networkType
- **Type**: typing.Optional[typing.Literal['DUAL', 'IPV4']]


# CreateDbParameterGroupInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.ParametersTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DbClusterSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DbInstanceForClusterSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DbInstanceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DbParameterGroupSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteDbClusterInputTypeDef

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDbClusterOutputTypeDef

### dbClusterStatus
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDbInstanceInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DurationTypeDef

### durationType
- **Type**: typing.Literal['hours', 'milliseconds', 'minutes', 'seconds']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDbClusterInputTypeDef

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDbInstanceInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDbParameterGroupInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# InfluxDBv2ParametersTypeDef

### fluxLogEnabled
- **Type**: typing.Optional[bool]

### logLevel
- **Type**: typing.Optional[typing.Literal['debug', 'error', 'info']]

### noTasks
- **Type**: typing.Optional[bool]

### queryConcurrency
- **Type**: typing.Optional[int]

### queryQueueSize
- **Type**: typing.Optional[int]

### tracingType
- **Type**: typing.Optional[typing.Literal['jaeger', 'log']]

### metricsDisabled
- **Type**: typing.Optional[bool]

### httpIdleTimeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### httpReadHeaderTimeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### httpReadTimeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### httpWriteTimeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### influxqlMaxSelectBuckets
- **Type**: typing.Optional[int]

### influxqlMaxSelectPoint
- **Type**: typing.Optional[int]

### influxqlMaxSelectSeries
- **Type**: typing.Optional[int]

### pprofDisabled
- **Type**: typing.Optional[bool]

### queryInitialMemoryBytes
- **Type**: typing.Optional[int]

### queryMaxMemoryBytes
- **Type**: typing.Optional[int]

### queryMemoryBytes
- **Type**: typing.Optional[int]

### sessionLength
- **Type**: typing.Optional[int]

### sessionRenewDisabled
- **Type**: typing.Optional[bool]

### storageCacheMaxMemorySize
- **Type**: typing.Optional[int]

### storageCacheSnapshotMemorySize
- **Type**: typing.Optional[int]

### storageCacheSnapshotWriteColdDuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### storageCompactFullWriteColdDuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### storageCompactThroughputBurst
- **Type**: typing.Optional[int]

### storageMaxConcurrentCompactions
- **Type**: typing.Optional[int]

### storageMaxIndexLogFileSize
- **Type**: typing.Optional[int]

### storageNoValidateFieldSize
- **Type**: typing.Optional[bool]

### storageRetentionCheckInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### storageSeriesFileMaxConcurrentSnapshotCompactions
- **Type**: typing.Optional[int]

### storageSeriesIdSetCacheSize
- **Type**: typing.Optional[int]

### storageWalMaxConcurrentWrites
- **Type**: typing.Optional[int]

### storageWalMaxWriteDelay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DurationTypeDef]

### uiDisabled
- **Type**: typing.Optional[bool]


# ListDbClustersInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfigTypeDef]


# ListDbClustersInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbClustersOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbClusterSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDbInstancesForClusterInputPaginateTypeDef

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfigTypeDef]


# ListDbInstancesForClusterInputTypeDef

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbInstancesForClusterOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbInstanceForClusterSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDbInstancesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfigTypeDef]


# ListDbInstancesInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbInstancesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbInstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDbParameterGroupsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfigTypeDef]


# ListDbParameterGroupsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbParameterGroupsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbParameterGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogDeliveryConfigurationTypeDef

### s3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.S3ConfigurationTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParametersTypeDef

### InfluxDBv2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.InfluxDBv2ParametersTypeDef]


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


# S3ConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDbClusterInputTypeDef

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef]

### dbParameterGroupIdentifier
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### dbInstanceType
- **Type**: typing.Optional[typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']]

### failoverMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'NO_FAILOVER']]


# UpdateDbClusterOutputTypeDef

### dbClusterStatus
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDbInstanceInputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef]

### dbParameterGroupIdentifier
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### dbInstanceType
- **Type**: typing.Optional[typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']]

### deploymentType
- **Type**: typing.Optional[typing.Literal['SINGLE_AZ', 'WITH_MULTIAZ_STANDBY']]

### dbStorageType
- **Type**: typing.Optional[typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']]

### allocatedStorage
- **Type**: typing.Optional[int]


