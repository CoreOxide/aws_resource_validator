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
from aws_resource_validator.pydantic_models.mediastore_constants import *

class ContainerTypeDef(BaseModel):
    Endpoint: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ContainerStatusType] = None
    AccessLoggingEnabled: Optional[bool] = None

class CorsRuleTypeDef(BaseModel):
    AllowedOrigins: List[str]
    AllowedHeaders: List[str]
    AllowedMethods: Optional[List[MethodNameType]] = None
    MaxAgeSeconds: Optional[int] = None
    ExposeHeaders: Optional[List[str]] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteContainerInputRequestTypeDef(BaseModel):
    ContainerName: str

class DeleteContainerPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class DeleteCorsPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class DeleteLifecyclePolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class DeleteMetricPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class DescribeContainerInputRequestTypeDef(BaseModel):
    ContainerName: Optional[str] = None

class GetContainerPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class GetCorsPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class GetLifecyclePolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class GetMetricPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListContainersInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    Resource: str

class MetricPolicyRuleTypeDef(BaseModel):
    ObjectGroup: str
    ObjectGroupName: str

class PutContainerPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str
    Policy: str

class PutLifecyclePolicyInputRequestTypeDef(BaseModel):
    ContainerName: str
    LifecyclePolicy: str

class StartAccessLoggingInputRequestTypeDef(BaseModel):
    ContainerName: str

class StopAccessLoggingInputRequestTypeDef(BaseModel):
    ContainerName: str

class UntagResourceInputRequestTypeDef(BaseModel):
    Resource: str
    TagKeys: Sequence[str]

class PutCorsPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str
    CorsPolicy: Sequence[CorsRuleTypeDef]

class CreateContainerInputRequestTypeDef(BaseModel):
    ContainerName: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    Resource: str
    Tags: Sequence[TagTypeDef]

class CreateContainerOutputTypeDef(BaseModel):
    Container: ContainerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContainerOutputTypeDef(BaseModel):
    Container: ContainerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerPolicyOutputTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCorsPolicyOutputTypeDef(BaseModel):
    CorsPolicy: List[CorsRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyOutputTypeDef(BaseModel):
    LifecyclePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainersOutputTypeDef(BaseModel):
    Containers: List[ContainerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainersInputListContainersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MetricPolicyTypeDef(BaseModel):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: Optional[List[MetricPolicyRuleTypeDef]] = None

class GetMetricPolicyOutputTypeDef(BaseModel):
    MetricPolicy: MetricPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricPolicyInputRequestTypeDef(BaseModel):
    ContainerName: str
    MetricPolicy: MetricPolicyTypeDef

