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
from aws_resource_validator.pydantic_models.mediastore_constants import *

class ContainerTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ContainerStatusType] = None
    AccessLoggingEnabled: Optional[bool] = None

class CorsRuleTypeDef(BaseValidatorModel):
    AllowedOrigins: List[str]
    AllowedHeaders: List[str]
    AllowedMethods: Optional[List[MethodNameType]] = None
    MaxAgeSeconds: Optional[int] = None
    ExposeHeaders: Optional[List[str]] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteContainerInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class DeleteContainerPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class DeleteCorsPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class DeleteLifecyclePolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class DeleteMetricPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class DescribeContainerInputRequestTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None

class GetContainerPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class GetCorsPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class GetLifecyclePolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class GetMetricPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListContainersInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    Resource: str

class MetricPolicyRuleTypeDef(BaseValidatorModel):
    ObjectGroup: str
    ObjectGroupName: str

class PutContainerPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str
    Policy: str

class PutLifecyclePolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str
    LifecyclePolicy: str

class StartAccessLoggingInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class StopAccessLoggingInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    Resource: str
    TagKeys: Sequence[str]

class PutCorsPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str
    CorsPolicy: Sequence[CorsRuleTypeDef]

class CreateContainerInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    Resource: str
    Tags: Sequence[TagTypeDef]

class CreateContainerOutputTypeDef(BaseValidatorModel):
    Container: ContainerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContainerOutputTypeDef(BaseValidatorModel):
    Container: ContainerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerPolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCorsPolicyOutputTypeDef(BaseValidatorModel):
    CorsPolicy: List[CorsRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyOutputTypeDef(BaseValidatorModel):
    LifecyclePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainersOutputTypeDef(BaseValidatorModel):
    Containers: List[ContainerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainersInputListContainersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MetricPolicyTypeDef(BaseValidatorModel):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: Optional[List[MetricPolicyRuleTypeDef]] = None

class GetMetricPolicyOutputTypeDef(BaseValidatorModel):
    MetricPolicy: MetricPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricPolicyInputRequestTypeDef(BaseValidatorModel):
    ContainerName: str
    MetricPolicy: MetricPolicyTypeDef

