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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteDbClusterInputTypeDef(BaseValidatorModel):
    dbClusterId: str


class DeleteDbInstanceInputTypeDef(BaseValidatorModel):
    identifier: str


class DurationTypeDef(BaseValidatorModel):
    durationType: DurationTypeType
    value: int


class GetDbClusterInputTypeDef(BaseValidatorModel):
    dbClusterId: str


class GetDbInstanceInputTypeDef(BaseValidatorModel):
    identifier: str


class GetDbParameterGroupInputTypeDef(BaseValidatorModel):
    identifier: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDbClustersInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDbInstancesForClusterInputTypeDef(BaseValidatorModel):
    dbClusterId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDbInstancesInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDbParameterGroupsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class S3ConfigurationTypeDef(BaseValidatorModel):
    bucketName: str
    enabled: bool


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateDbClusterOutputTypeDef(BaseValidatorModel):
    dbClusterId: str
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDbClusterOutputTypeDef(BaseValidatorModel):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDbClusterOutputTypeDef(BaseValidatorModel):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DbClusterSummaryTypeDef(BaseValidatorModel):
    pass


class ListDbClustersOutputTypeDef(BaseValidatorModel):
    items: List[DbClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DbInstanceForClusterSummaryTypeDef(BaseValidatorModel):
    pass


class ListDbInstancesForClusterOutputTypeDef(BaseValidatorModel):
    items: List[DbInstanceForClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DbInstanceSummaryTypeDef(BaseValidatorModel):
    pass


class ListDbInstancesOutputTypeDef(BaseValidatorModel):
    items: List[DbInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DbParameterGroupSummaryTypeDef(BaseValidatorModel):
    pass


class ListDbParameterGroupsOutputTypeDef(BaseValidatorModel):
    items: List[DbParameterGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class InfluxDBv2ParametersTypeDef(BaseValidatorModel):
    fluxLogEnabled: Optional[bool] = None
    logLevel: Optional[LogLevelType] = None
    noTasks: Optional[bool] = None
    queryConcurrency: Optional[int] = None
    queryQueueSize: Optional[int] = None
    tracingType: Optional[TracingTypeType] = None
    metricsDisabled: Optional[bool] = None
    httpIdleTimeout: Optional[DurationTypeDef] = None
    httpReadHeaderTimeout: Optional[DurationTypeDef] = None
    httpReadTimeout: Optional[DurationTypeDef] = None
    httpWriteTimeout: Optional[DurationTypeDef] = None
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
    storageCacheSnapshotWriteColdDuration: Optional[DurationTypeDef] = None
    storageCompactFullWriteColdDuration: Optional[DurationTypeDef] = None
    storageCompactThroughputBurst: Optional[int] = None
    storageMaxConcurrentCompactions: Optional[int] = None
    storageMaxIndexLogFileSize: Optional[int] = None
    storageNoValidateFieldSize: Optional[bool] = None
    storageRetentionCheckInterval: Optional[DurationTypeDef] = None
    storageSeriesFileMaxConcurrentSnapshotCompactions: Optional[int] = None
    storageSeriesIdSetCacheSize: Optional[int] = None
    storageWalMaxConcurrentWrites: Optional[int] = None
    storageWalMaxWriteDelay: Optional[DurationTypeDef] = None
    uiDisabled: Optional[bool] = None


class ListDbClustersInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDbInstancesForClusterInputPaginateTypeDef(BaseValidatorModel):
    dbClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDbInstancesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDbParameterGroupsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class LogDeliveryConfigurationTypeDef(BaseValidatorModel):
    s3Configuration: S3ConfigurationTypeDef


class ParametersTypeDef(BaseValidatorModel):
    InfluxDBv2: Optional[InfluxDBv2ParametersTypeDef] = None


class CreateDbClusterInputTypeDef(BaseValidatorModel):
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
    logDeliveryConfiguration: Optional[LogDeliveryConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class CreateDbInstanceInputTypeDef(BaseValidatorModel):
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
    logDeliveryConfiguration: Optional[LogDeliveryConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    port: Optional[int] = None
    networkType: Optional[NetworkTypeType] = None


class UpdateDbClusterInputTypeDef(BaseValidatorModel):
    dbClusterId: str
    logDeliveryConfiguration: Optional[LogDeliveryConfigurationTypeDef] = None
    dbParameterGroupIdentifier: Optional[str] = None
    port: Optional[int] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    failoverMode: Optional[FailoverModeType] = None


class UpdateDbInstanceInputTypeDef(BaseValidatorModel):
    identifier: str
    logDeliveryConfiguration: Optional[LogDeliveryConfigurationTypeDef] = None
    dbParameterGroupIdentifier: Optional[str] = None
    port: Optional[int] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    deploymentType: Optional[DeploymentTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None


class CreateDbParameterGroupInputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[ParametersTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


