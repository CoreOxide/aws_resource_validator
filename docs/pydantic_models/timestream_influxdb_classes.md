# Timestream Influxdb Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDbClusterInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfiguration]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDbClusterOutput

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### dbClusterStatus
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDbInstanceInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfiguration]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### port
- **Type**: typing.Optional[int]

### networkType
- **Type**: typing.Optional[typing.Literal['DUAL', 'IPV4']]


# CreateDbParameterGroupInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Parameters]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DbClusterSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DbInstanceForClusterSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DbInstanceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DbParameterGroupSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteDbClusterInput

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDbClusterOutput

### dbClusterStatus
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDbInstanceInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# Duration

### durationType
- **Type**: typing.Literal['hours', 'milliseconds', 'minutes', 'seconds']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes


# GetDbClusterInput

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDbInstanceInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDbParameterGroupInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# InfluxDBv2Parameters

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

### httpReadHeaderTimeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

### httpReadTimeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

### httpWriteTimeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

### storageCompactFullWriteColdDuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

### storageCompactThroughputBurst
- **Type**: typing.Optional[int]

### storageMaxConcurrentCompactions
- **Type**: typing.Optional[int]

### storageMaxIndexLogFileSize
- **Type**: typing.Optional[int]

### storageNoValidateFieldSize
- **Type**: typing.Optional[bool]

### storageRetentionCheckInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

### storageSeriesFileMaxConcurrentSnapshotCompactions
- **Type**: typing.Optional[int]

### storageSeriesIdSetCacheSize
- **Type**: typing.Optional[int]

### storageWalMaxConcurrentWrites
- **Type**: typing.Optional[int]

### storageWalMaxWriteDelay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.Duration]

### uiDisabled
- **Type**: typing.Optional[bool]


# ListDbClustersInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbClustersInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfig]


# ListDbClustersOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbClusterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDbInstancesForClusterInput

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbInstancesForClusterInputPaginate

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfig]


# ListDbInstancesForClusterOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbInstanceForClusterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDbInstancesInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbInstancesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfig]


# ListDbInstancesOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbInstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDbParameterGroupsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbParameterGroupsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfig]


# ListDbParameterGroupsOutput

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbParameterGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes


# LogDeliveryConfiguration

### s3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.S3Configuration'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameters

### InfluxDBv2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.InfluxDBv2Parameters]


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


# S3Configuration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDbClusterInput

### dbClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfiguration]

### dbParameterGroupIdentifier
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### dbInstanceType
- **Type**: typing.Optional[typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']]

### failoverMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'NO_FAILOVER']]


# UpdateDbClusterOutput

### dbClusterStatus
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDbInstanceInput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfiguration]

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


