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

class Container(BaseValidatorModel):
    Endpoint: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ContainerStatusType] = None
    AccessLoggingEnabled: Optional[bool] = None


class CorsRuleOutput(BaseValidatorModel):
    AllowedOrigins: List[str]
    AllowedHeaders: List[str]
    AllowedMethods: Optional[List[MethodNameType]] = None
    MaxAgeSeconds: Optional[int] = None
    ExposeHeaders: Optional[List[str]] = None


class CorsRule(BaseValidatorModel):
    AllowedOrigins: Sequence[str]
    AllowedHeaders: Sequence[str]
    AllowedMethods: Optional[Sequence[MethodNameType]] = None
    MaxAgeSeconds: Optional[int] = None
    ExposeHeaders: Optional[Sequence[str]] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteContainerInput(BaseValidatorModel):
    ContainerName: str


class DeleteContainerPolicyInput(BaseValidatorModel):
    ContainerName: str


class DeleteCorsPolicyInput(BaseValidatorModel):
    ContainerName: str


class DeleteLifecyclePolicyInput(BaseValidatorModel):
    ContainerName: str


class DeleteMetricPolicyInput(BaseValidatorModel):
    ContainerName: str


class DescribeContainerInput(BaseValidatorModel):
    ContainerName: Optional[str] = None


class GetContainerPolicyInput(BaseValidatorModel):
    ContainerName: str


class GetCorsPolicyInput(BaseValidatorModel):
    ContainerName: str


class GetLifecyclePolicyInput(BaseValidatorModel):
    ContainerName: str


class GetMetricPolicyInput(BaseValidatorModel):
    ContainerName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListContainersInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceInput(BaseValidatorModel):
    Resource: str


class MetricPolicyRule(BaseValidatorModel):
    ObjectGroup: str
    ObjectGroupName: str


class PutContainerPolicyInput(BaseValidatorModel):
    ContainerName: str
    Policy: str


class PutLifecyclePolicyInput(BaseValidatorModel):
    ContainerName: str
    LifecyclePolicy: str


class StartAccessLoggingInput(BaseValidatorModel):
    ContainerName: str


class StopAccessLoggingInput(BaseValidatorModel):
    ContainerName: str


class UntagResourceInput(BaseValidatorModel):
    Resource: str
    TagKeys: Sequence[str]


class CreateContainerInput(BaseValidatorModel):
    ContainerName: str
    Tags: Optional[Sequence[Tag]] = None


class TagResourceInput(BaseValidatorModel):
    Resource: str
    Tags: Sequence[Tag]


class GetContainerPolicyOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetCorsPolicyOutput(BaseValidatorModel):
    CorsPolicy: List[CorsRuleOutput]
    ResponseMetadata: ResponseMetadata


class GetLifecyclePolicyOutput(BaseValidatorModel):
    LifecyclePolicy: str
    ResponseMetadata: ResponseMetadata


class ListContainersOutput(BaseValidatorModel):
    Containers: List[Container]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ListContainersInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class MetricPolicyOutput(BaseValidatorModel):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: Optional[List[MetricPolicyRule]] = None


class MetricPolicy(BaseValidatorModel):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: Optional[Sequence[MetricPolicyRule]] = None


class CorsRuleUnion(BaseValidatorModel):
    pass


class PutCorsPolicyInput(BaseValidatorModel):
    ContainerName: str
    CorsPolicy: Sequence[CorsRuleUnion]


class GetMetricPolicyOutput(BaseValidatorModel):
    MetricPolicy: MetricPolicyOutput
    ResponseMetadata: ResponseMetadata


class MetricPolicyUnion(BaseValidatorModel):
    pass


class PutMetricPolicyInput(BaseValidatorModel):
    ContainerName: str
    MetricPolicy: MetricPolicyUnion


