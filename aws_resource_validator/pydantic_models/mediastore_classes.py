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
from aws_resource_validator.pydantic_models.mediastore_constants import *

class ContainerTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ContainerStatusType] = None
    AccessLoggingEnabled: Optional[bool] = None


class CorsRuleOutputTypeDef(BaseValidatorModel):
    AllowedOrigins: List[str]
    AllowedHeaders: List[str]
    AllowedMethods: Optional[List[MethodNameType]] = None
    MaxAgeSeconds: Optional[int] = None
    ExposeHeaders: Optional[List[str]] = None


class CorsRuleTypeDef(BaseValidatorModel):
    AllowedOrigins: Sequence[str]
    AllowedHeaders: Sequence[str]
    AllowedMethods: Optional[Sequence[MethodNameType]] = None
    MaxAgeSeconds: Optional[int] = None
    ExposeHeaders: Optional[Sequence[str]] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteContainerInputTypeDef(BaseValidatorModel):
    ContainerName: str


class DeleteContainerPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class DeleteCorsPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class DeleteLifecyclePolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class DeleteMetricPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class DescribeContainerInputTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None


class GetContainerPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class GetCorsPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class GetLifecyclePolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class GetMetricPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListContainersInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    Resource: str


class MetricPolicyRuleTypeDef(BaseValidatorModel):
    ObjectGroup: str
    ObjectGroupName: str


class PutContainerPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str
    Policy: str


class PutLifecyclePolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str
    LifecyclePolicy: str


class StartAccessLoggingInputTypeDef(BaseValidatorModel):
    ContainerName: str


class StopAccessLoggingInputTypeDef(BaseValidatorModel):
    ContainerName: str


class UntagResourceInputTypeDef(BaseValidatorModel):
    Resource: str
    TagKeys: Sequence[str]


class CreateContainerInputTypeDef(BaseValidatorModel):
    ContainerName: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    Resource: str
    Tags: Sequence[TagTypeDef]


class GetContainerPolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCorsPolicyOutputTypeDef(BaseValidatorModel):
    CorsPolicy: List[CorsRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetLifecyclePolicyOutputTypeDef(BaseValidatorModel):
    LifecyclePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListContainersOutputTypeDef(BaseValidatorModel):
    Containers: List[ContainerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListContainersInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MetricPolicyOutputTypeDef(BaseValidatorModel):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: Optional[List[MetricPolicyRuleTypeDef]] = None


class MetricPolicyTypeDef(BaseValidatorModel):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: Optional[Sequence[MetricPolicyRuleTypeDef]] = None


class CorsRuleUnionTypeDef(BaseValidatorModel):
    pass


class PutCorsPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str
    CorsPolicy: Sequence[CorsRuleUnionTypeDef]


class GetMetricPolicyOutputTypeDef(BaseValidatorModel):
    MetricPolicy: MetricPolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MetricPolicyUnionTypeDef(BaseValidatorModel):
    pass


class PutMetricPolicyInputTypeDef(BaseValidatorModel):
    ContainerName: str
    MetricPolicy: MetricPolicyUnionTypeDef


