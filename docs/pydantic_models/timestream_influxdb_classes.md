# timestream_influxdb_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDbInstanceInputRequestTypeDef

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


# CreateDbInstanceOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'MODIFYING', 'UPDATING']
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### dbInstanceType
- **Type**: typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']
- **Required**: Yes

### dbStorageType
- **Type**: typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']
- **Required**: Yes

### allocatedStorage
- **Type**: <class 'int'>
- **Required**: Yes

### deploymentType
- **Type**: typing.Literal['SINGLE_AZ', 'WITH_MULTIAZ_STANDBY']
- **Required**: Yes

### vpcSubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### publiclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### dbParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### secondaryAvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef'>
- **Required**: Yes

### influxAuthParametersSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDbParameterGroupInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.ParametersTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDbParameterGroupOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ParametersTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DbInstanceSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'MODIFYING', 'UPDATING']]

### endpoint
- **Type**: typing.Optional[str]

### dbInstanceType
- **Type**: typing.Optional[typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']]

### dbStorageType
- **Type**: typing.Optional[typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']]

### allocatedStorage
- **Type**: typing.Optional[int]

### deploymentType
- **Type**: typing.Optional[typing.Literal['SINGLE_AZ', 'WITH_MULTIAZ_STANDBY']]


# DbParameterGroupSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# DeleteDbInstanceInputRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDbInstanceOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'MODIFYING', 'UPDATING']
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### dbInstanceType
- **Type**: typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']
- **Required**: Yes

### dbStorageType
- **Type**: typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']
- **Required**: Yes

### allocatedStorage
- **Type**: <class 'int'>
- **Required**: Yes

### deploymentType
- **Type**: typing.Literal['SINGLE_AZ', 'WITH_MULTIAZ_STANDBY']
- **Required**: Yes

### vpcSubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### publiclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### dbParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### secondaryAvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef'>
- **Required**: Yes

### influxAuthParametersSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDbInstanceInputRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDbInstanceOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'MODIFYING', 'UPDATING']
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### dbInstanceType
- **Type**: typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']
- **Required**: Yes

### dbStorageType
- **Type**: typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']
- **Required**: Yes

### allocatedStorage
- **Type**: <class 'int'>
- **Required**: Yes

### deploymentType
- **Type**: typing.Literal['SINGLE_AZ', 'WITH_MULTIAZ_STANDBY']
- **Required**: Yes

### vpcSubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### publiclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### dbParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### secondaryAvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef'>
- **Required**: Yes

### influxAuthParametersSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDbParameterGroupInputRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDbParameterGroupOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ParametersTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
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


# ListDbInstancesInputListDbInstancesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfigTypeDef]


# ListDbInstancesInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbInstancesOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbInstanceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDbParameterGroupsInputListDbParameterGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.PaginatorConfigTypeDef]


# ListDbParameterGroupsInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDbParameterGroupsOutputTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_influxdb_classes.DbParameterGroupSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDbInstanceInputRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef]

### dbParameterGroupIdentifier
- **Type**: typing.Optional[str]


# UpdateDbInstanceOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'MODIFYING', 'UPDATING']
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### dbInstanceType
- **Type**: typing.Literal['db.influx.12xlarge', 'db.influx.16xlarge', 'db.influx.2xlarge', 'db.influx.4xlarge', 'db.influx.8xlarge', 'db.influx.large', 'db.influx.medium', 'db.influx.xlarge']
- **Required**: Yes

### dbStorageType
- **Type**: typing.Literal['InfluxIOIncludedT1', 'InfluxIOIncludedT2', 'InfluxIOIncludedT3']
- **Required**: Yes

### allocatedStorage
- **Type**: <class 'int'>
- **Required**: Yes

### deploymentType
- **Type**: typing.Literal['SINGLE_AZ', 'WITH_MULTIAZ_STANDBY']
- **Required**: Yes

### vpcSubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### publiclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### dbParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### secondaryAvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### logDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.LogDeliveryConfigurationTypeDef'>
- **Required**: Yes

### influxAuthParametersSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_influxdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


