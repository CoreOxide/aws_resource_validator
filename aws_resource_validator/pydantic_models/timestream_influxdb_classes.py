from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class DbInstanceSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: Optional[StatusType] = None
    endpoint: Optional[str] = None
    dbInstanceType: Optional[DbInstanceTypeType] = None
    dbStorageType: Optional[DbStorageTypeType] = None
    allocatedStorage: Optional[int] = None
    deploymentType: Optional[DeploymentTypeType] = None

class DbParameterGroupSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    description: Optional[str] = None

class DeleteDbInstanceInputRequestTypeDef(BaseValidatorModel):
    identifier: str

class GetDbInstanceInputRequestTypeDef(BaseValidatorModel):
    identifier: str

class GetDbParameterGroupInputRequestTypeDef(BaseValidatorModel):
    identifier: str

class InfluxDBv2ParametersTypeDef(BaseValidatorModel):
    fluxLogEnabled: Optional[bool] = None
    logLevel: Optional[LogLevelType] = None
    noTasks: Optional[bool] = None
    queryConcurrency: Optional[int] = None
    queryQueueSize: Optional[int] = None
    tracingType: Optional[TracingTypeType] = None
    metricsDisabled: Optional[bool] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDbInstancesInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDbParameterGroupsInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class S3ConfigurationTypeDef(BaseValidatorModel):
    bucketName: str
    enabled: bool

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDbInstancesOutputTypeDef(BaseValidatorModel):
    items: List[DbInstanceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDbParameterGroupsOutputTypeDef(BaseValidatorModel):
    items: List[DbParameterGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParametersTypeDef(BaseValidatorModel):
    InfluxDBv2: Optional[InfluxDBv2ParametersTypeDef] = None

class ListDbInstancesInputListDbInstancesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDbParameterGroupsInputListDbParameterGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LogDeliveryConfigurationTypeDef(BaseValidatorModel):
    s3Configuration: S3ConfigurationTypeDef

class CreateDbParameterGroupInputRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[ParametersTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDbParameterGroupOutputTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    description: str
    parameters: ParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDbParameterGroupOutputTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    description: str
    parameters: ParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDbInstanceInputRequestTypeDef(BaseValidatorModel):
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

class CreateDbInstanceOutputTypeDef(BaseValidatorModel):
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

class DeleteDbInstanceOutputTypeDef(BaseValidatorModel):
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

class GetDbInstanceOutputTypeDef(BaseValidatorModel):
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

class UpdateDbInstanceInputRequestTypeDef(BaseValidatorModel):
    identifier: str
    logDeliveryConfiguration: Optional[LogDeliveryConfigurationTypeDef] = None
    dbParameterGroupIdentifier: Optional[str] = None

class UpdateDbInstanceOutputTypeDef(BaseValidatorModel):
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

