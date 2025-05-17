from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.timestream_influxdb.timestream_influxdb_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DbClusterSummary(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: Optional[ClusterStatusType] = None
    endpoint: Optional[str] = None
    readerEndpoint: Optional[str] = None
    port: Optional[int] = None
    deploymentType: Optional[Literal['MULTI_NODE_READ_REPLICAS']] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    networkType: Optional[NetworkTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None


class DbInstanceForClusterSummary(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: Optional[StatusType] = None
    endpoint: Optional[str] = None
    port: Optional[int] = None
    networkType: Optional[NetworkTypeType] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None
    deploymentType: Optional[DeploymentTypeType] = None
    instanceMode: Optional[InstanceModeType] = None


class DbInstanceSummary(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: Optional[StatusType] = None
    endpoint: Optional[str] = None
    port: Optional[int] = None
    networkType: Optional[NetworkTypeType] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None
    deploymentType: Optional[DeploymentTypeType] = None


class DbParameterGroupSummary(BaseValidatorModel):
    id: str
    name: str
    arn: str
    description: Optional[str] = None


# This class is the input for the 'delete_db_cluster' function.
class DeleteDbClusterInput(BaseValidatorModel):
    dbClusterId: str


# This class is the input for the 'delete_db_instance' function.
class DeleteDbInstanceInput(BaseValidatorModel):
    identifier: str


class Duration(BaseValidatorModel):
    durationType: DurationTypeType
    value: int


# This class is the input for the 'get_db_cluster' function.
class GetDbClusterInput(BaseValidatorModel):
    dbClusterId: str


# This class is the input for the 'get_db_instance' function.
class GetDbInstanceInput(BaseValidatorModel):
    identifier: str


# This class is the input for the 'get_db_parameter_group' function.
class GetDbParameterGroupInput(BaseValidatorModel):
    identifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_db_clusters' function.
class ListDbClustersInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_db_instances_for_cluster' function.
class ListDbInstancesForClusterInput(BaseValidatorModel):
    dbClusterId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_db_instances' function.
class ListDbInstancesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_db_parameter_groups' function.
class ListDbParameterGroupsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class S3Configuration(BaseValidatorModel):
    bucketName: str
    enabled: bool


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the output for the 'create_db_cluster' function.
class CreateDbClusterOutput(BaseValidatorModel):
    dbClusterId: str
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_cluster' function.
class DeleteDbClusterOutput(BaseValidatorModel):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_db_cluster' function.
class UpdateDbClusterOutput(BaseValidatorModel):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_db_clusters' function.
class ListDbClustersOutput(BaseValidatorModel):
    items: List[DbClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_db_instances_for_cluster' function.
class ListDbInstancesForClusterOutput(BaseValidatorModel):
    items: List[DbInstanceForClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_db_instances' function.
class ListDbInstancesOutput(BaseValidatorModel):
    items: List[DbInstanceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_db_parameter_groups' function.
class ListDbParameterGroupsOutput(BaseValidatorModel):
    items: List[DbParameterGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InfluxDBv2Parameters(BaseValidatorModel):
    fluxLogEnabled: Optional[bool] = None
    logLevel: Optional[LogLevelType] = None
    noTasks: Optional[bool] = None
    queryConcurrency: Optional[int] = None
    queryQueueSize: Optional[int] = None
    tracingType: Optional[TracingTypeType] = None
    metricsDisabled: Optional[bool] = None
    httpIdleTimeout: Optional[Duration] = None
    httpReadHeaderTimeout: Optional[Duration] = None
    httpReadTimeout: Optional[Duration] = None
    httpWriteTimeout: Optional[Duration] = None
    influxqlMaxSelectBuckets: Optional[int] = None
    influxqlMaxSelectPoint: Optional[int] = None
    influxqlMaxSelectSeries: Optional[int] = None
    pprofDisabled: Optional[bool] = None
    queryInitialMemoryBytes: Optional[int] = None
    queryMaxMemoryBytes: Optional[int] = None
    queryMemoryBytes: Optional[int] = None
    sessionLength: Optional[int] = None
    sessionRenewDisabled: Optional[bool] = None
    storageCacheMaxMemorySize: Optional[int] = None
    storageCacheSnapshotMemorySize: Optional[int] = None
    storageCacheSnapshotWriteColdDuration: Optional[Duration] = None
    storageCompactFullWriteColdDuration: Optional[Duration] = None
    storageCompactThroughputBurst: Optional[int] = None
    storageMaxConcurrentCompactions: Optional[int] = None
    storageMaxIndexLogFileSize: Optional[int] = None
    storageNoValidateFieldSize: Optional[bool] = None
    storageRetentionCheckInterval: Optional[Duration] = None
    storageSeriesFileMaxConcurrentSnapshotCompactions: Optional[int] = None
    storageSeriesIdSetCacheSize: Optional[int] = None
    storageWalMaxConcurrentWrites: Optional[int] = None
    storageWalMaxWriteDelay: Optional[Duration] = None
    uiDisabled: Optional[bool] = None


class ListDbClustersInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDbInstancesForClusterInputPaginate(BaseValidatorModel):
    dbClusterId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDbInstancesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDbParameterGroupsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class LogDeliveryConfiguration(BaseValidatorModel):
    s3Configuration: S3Configuration


class Parameters(BaseValidatorModel):
    InfluxDBv2: Optional[InfluxDBv2Parameters] = None


# This class is the input for the 'create_db_cluster' function.
class CreateDbClusterInput(BaseValidatorModel):
    name: str
    password: str
    dbInstanceType: DbInstanceTypeType
    allocatedStorage: int
    vpcSubnetIds: List[str]
    vpcSecurityGroupIds: List[str]
    deploymentType: Literal['MULTI_NODE_READ_REPLICAS']
    username: Optional[str] = None
    organization: Optional[str] = None
    bucket: Optional[str] = None
    port: Optional[int] = None
    dbParameterGroupIdentifier: Optional[str] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    networkType: Optional[NetworkTypeType] = None
    publiclyAccessible: Optional[bool] = None
    failoverMode: Optional[FailoverModeType] = None
    logDeliveryConfiguration: Optional[LogDeliveryConfiguration] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_db_instance' function.
class CreateDbInstanceInput(BaseValidatorModel):
    name: str
    password: str
    dbInstanceType: DbInstanceTypeType
    vpcSubnetIds: List[str]
    vpcSecurityGroupIds: List[str]
    allocatedStorage: int
    username: Optional[str] = None
    organization: Optional[str] = None
    bucket: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    dbParameterGroupIdentifier: Optional[str] = None
    deploymentType: Optional[DeploymentTypeType] = None
    logDeliveryConfiguration: Optional[LogDeliveryConfiguration] = None
    tags: Optional[Dict[str, str]] = None
    port: Optional[int] = None
    networkType: Optional[NetworkTypeType] = None


# This class is the output for the 'create_db_instance' function.
class CreateDbInstanceOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
    port: int
    networkType: NetworkTypeType
    dbInstanceType: DbInstanceTypeType
    dbStorageType: DbStorageTypeType
    allocatedStorage: int
    deploymentType: DeploymentTypeType
    vpcSubnetIds: List[str]
    publiclyAccessible: bool
    vpcSecurityGroupIds: List[str]
    dbParameterGroupIdentifier: str
    availabilityZone: str
    secondaryAvailabilityZone: str
    logDeliveryConfiguration: LogDeliveryConfiguration
    influxAuthParametersSecretArn: str
    dbClusterId: str
    instanceMode: InstanceModeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_instance' function.
class DeleteDbInstanceOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
    port: int
    networkType: NetworkTypeType
    dbInstanceType: DbInstanceTypeType
    dbStorageType: DbStorageTypeType
    allocatedStorage: int
    deploymentType: DeploymentTypeType
    vpcSubnetIds: List[str]
    publiclyAccessible: bool
    vpcSecurityGroupIds: List[str]
    dbParameterGroupIdentifier: str
    availabilityZone: str
    secondaryAvailabilityZone: str
    logDeliveryConfiguration: LogDeliveryConfiguration
    influxAuthParametersSecretArn: str
    dbClusterId: str
    instanceMode: InstanceModeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_db_cluster' function.
class GetDbClusterOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: ClusterStatusType
    endpoint: str
    readerEndpoint: str
    port: int
    deploymentType: Literal['MULTI_NODE_READ_REPLICAS']
    dbInstanceType: DbInstanceTypeType
    networkType: NetworkTypeType
    dbStorageType: DbStorageTypeType
    allocatedStorage: int
    publiclyAccessible: bool
    dbParameterGroupIdentifier: str
    logDeliveryConfiguration: LogDeliveryConfiguration
    influxAuthParametersSecretArn: str
    vpcSubnetIds: List[str]
    vpcSecurityGroupIds: List[str]
    failoverMode: FailoverModeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_db_instance' function.
class GetDbInstanceOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
    port: int
    networkType: NetworkTypeType
    dbInstanceType: DbInstanceTypeType
    dbStorageType: DbStorageTypeType
    allocatedStorage: int
    deploymentType: DeploymentTypeType
    vpcSubnetIds: List[str]
    publiclyAccessible: bool
    vpcSecurityGroupIds: List[str]
    dbParameterGroupIdentifier: str
    availabilityZone: str
    secondaryAvailabilityZone: str
    logDeliveryConfiguration: LogDeliveryConfiguration
    influxAuthParametersSecretArn: str
    dbClusterId: str
    instanceMode: InstanceModeType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_db_cluster' function.
class UpdateDbClusterInput(BaseValidatorModel):
    dbClusterId: str
    logDeliveryConfiguration: Optional[LogDeliveryConfiguration] = None
    dbParameterGroupIdentifier: Optional[str] = None
    port: Optional[int] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    failoverMode: Optional[FailoverModeType] = None


# This class is the input for the 'update_db_instance' function.
class UpdateDbInstanceInput(BaseValidatorModel):
    identifier: str
    logDeliveryConfiguration: Optional[LogDeliveryConfiguration] = None
    dbParameterGroupIdentifier: Optional[str] = None
    port: Optional[int] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    deploymentType: Optional[DeploymentTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None


# This class is the output for the 'update_db_instance' function.
class UpdateDbInstanceOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
    port: int
    networkType: NetworkTypeType
    dbInstanceType: DbInstanceTypeType
    dbStorageType: DbStorageTypeType
    allocatedStorage: int
    deploymentType: DeploymentTypeType
    vpcSubnetIds: List[str]
    publiclyAccessible: bool
    vpcSecurityGroupIds: List[str]
    dbParameterGroupIdentifier: str
    availabilityZone: str
    secondaryAvailabilityZone: str
    logDeliveryConfiguration: LogDeliveryConfiguration
    influxAuthParametersSecretArn: str
    dbClusterId: str
    instanceMode: InstanceModeType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_db_parameter_group' function.
class CreateDbParameterGroupInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Parameters] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_db_parameter_group' function.
class CreateDbParameterGroupOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    description: str
    parameters: Parameters
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_db_parameter_group' function.
class GetDbParameterGroupOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    description: str
    parameters: Parameters
    ResponseMetadata: ResponseMetadata