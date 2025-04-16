from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.timestream_influxdb_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteDbClusterInput(BaseValidatorModel):
    dbClusterId: str


class DeleteDbInstanceInput(BaseValidatorModel):
    identifier: str


class Duration(BaseValidatorModel):
    durationType: DurationTypeType
    value: int


class GetDbClusterInput(BaseValidatorModel):
    dbClusterId: str


class GetDbInstanceInput(BaseValidatorModel):
    identifier: str


class GetDbParameterGroupInput(BaseValidatorModel):
    identifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDbClustersInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDbInstancesForClusterInput(BaseValidatorModel):
    dbClusterId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDbInstancesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDbParameterGroupsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class S3Configuration(BaseValidatorModel):
    bucketName: str
    enabled: bool


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateDbClusterOutput(BaseValidatorModel):
    dbClusterId: str
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadata


class DeleteDbClusterOutput(BaseValidatorModel):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateDbClusterOutput(BaseValidatorModel):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadata


class DbClusterSummary(BaseValidatorModel):
    pass


class ListDbClustersOutput(BaseValidatorModel):
    items: List[DbClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DbInstanceForClusterSummary(BaseValidatorModel):
    pass


class ListDbInstancesForClusterOutput(BaseValidatorModel):
    items: List[DbInstanceForClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DbInstanceSummary(BaseValidatorModel):
    pass


class ListDbInstancesOutput(BaseValidatorModel):
    items: List[DbInstanceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DbParameterGroupSummary(BaseValidatorModel):
    pass


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


class CreateDbClusterInput(BaseValidatorModel):
    name: str
    password: str
    dbInstanceType: DbInstanceTypeType
    allocatedStorage: int
    vpcSubnetIds: Sequence[str]
    vpcSecurityGroupIds: Sequence[str]
    deploymentType: Literal["MULTI_NODE_READ_REPLICAS"]
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
    tags: Optional[Mapping[str, str]] = None


class CreateDbInstanceInput(BaseValidatorModel):
    name: str
    password: str
    dbInstanceType: DbInstanceTypeType
    vpcSubnetIds: Sequence[str]
    vpcSecurityGroupIds: Sequence[str]
    allocatedStorage: int
    username: Optional[str] = None
    organization: Optional[str] = None
    bucket: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    dbParameterGroupIdentifier: Optional[str] = None
    deploymentType: Optional[DeploymentTypeType] = None
    logDeliveryConfiguration: Optional[LogDeliveryConfiguration] = None
    tags: Optional[Mapping[str, str]] = None
    port: Optional[int] = None
    networkType: Optional[NetworkTypeType] = None


class UpdateDbClusterInput(BaseValidatorModel):
    dbClusterId: str
    logDeliveryConfiguration: Optional[LogDeliveryConfiguration] = None
    dbParameterGroupIdentifier: Optional[str] = None
    port: Optional[int] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    failoverMode: Optional[FailoverModeType] = None


class UpdateDbInstanceInput(BaseValidatorModel):
    identifier: str
    logDeliveryConfiguration: Optional[LogDeliveryConfiguration] = None
    dbParameterGroupIdentifier: Optional[str] = None
    port: Optional[int] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    deploymentType: Optional[DeploymentTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None


class CreateDbParameterGroupInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Parameters] = None
    tags: Optional[Mapping[str, str]] = None


