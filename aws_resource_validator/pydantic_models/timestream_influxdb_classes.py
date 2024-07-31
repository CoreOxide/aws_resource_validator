from datetime import datetime
from pydantic import BaseModel
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DbInstanceSummaryTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: Optional[StatusType] = None
    endpoint: Optional[str] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None
    deploymentType: Optional[DeploymentTypeType] = None

class DbParameterGroupSummaryTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    description: Optional[str] = None

class DeleteDbInstanceInputRequestTypeDef(BaseModel):
    identifier: str

class GetDbInstanceInputRequestTypeDef(BaseModel):
    identifier: str

class GetDbParameterGroupInputRequestTypeDef(BaseModel):
    identifier: str

class InfluxDBv2ParametersTypeDef(BaseModel):
    fluxLogEnabled: Optional[bool] = None
    logLevel: Optional[LogLevelType] = None
    noTasks: Optional[bool] = None
    queryConcurrency: Optional[int] = None
    queryQueueSize: Optional[int] = None
    tracingType: Optional[TracingTypeType] = None
    metricsDisabled: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDbInstancesInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDbParameterGroupsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class S3ConfigurationTypeDef(BaseModel):
    bucketName: str
    enabled: bool

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDbInstancesOutputTypeDef(BaseModel):
    items: List[DbInstanceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDbParameterGroupsOutputTypeDef(BaseModel):
    items: List[DbParameterGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParametersTypeDef(BaseModel):
    InfluxDBv2: Optional[InfluxDBv2ParametersTypeDef] = None

class ListDbInstancesInputListDbInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDbParameterGroupsInputListDbParameterGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LogDeliveryConfigurationTypeDef(BaseModel):
    s3Configuration: S3ConfigurationTypeDef

class CreateDbParameterGroupInputRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[ParametersTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDbParameterGroupOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    description: str
    parameters: ParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDbParameterGroupOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    description: str
    parameters: ParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDbInstanceInputRequestTypeDef(BaseModel):
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

class CreateDbInstanceOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
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
    logDeliveryConfiguration: LogDeliveryConfigurationTypeDef
    influxAuthParametersSecretArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDbInstanceOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
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
    logDeliveryConfiguration: LogDeliveryConfigurationTypeDef
    influxAuthParametersSecretArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDbInstanceOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
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
    logDeliveryConfiguration: LogDeliveryConfigurationTypeDef
    influxAuthParametersSecretArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDbInstanceInputRequestTypeDef(BaseModel):
    identifier: str
    logDeliveryConfiguration: Optional[LogDeliveryConfigurationTypeDef] = None
    dbParameterGroupIdentifier: Optional[str] = None

class UpdateDbInstanceOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: StatusType
    endpoint: str
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
    logDeliveryConfiguration: LogDeliveryConfigurationTypeDef
    influxAuthParametersSecretArn: str
    ResponseMetadata: ResponseMetadataTypeDef

