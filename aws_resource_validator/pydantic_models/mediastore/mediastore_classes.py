from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediastore.mediastore_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    AllowedOrigins: List[str]
    AllowedHeaders: List[str]
    AllowedMethods: Optional[List[MethodNameType]] = None
    MaxAgeSeconds: Optional[int] = None
    ExposeHeaders: Optional[List[str]] = None


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


# This class is the input for the 'describe_container' function.
class DescribeContainerInput(BaseValidatorModel):
    ContainerName: Optional[str] = None


# This class is the input for the 'get_container_policy' function.
class GetContainerPolicyInput(BaseValidatorModel):
    ContainerName: str


# This class is the input for the 'get_cors_policy' function.
class GetCorsPolicyInput(BaseValidatorModel):
    ContainerName: str


# This class is the input for the 'get_lifecycle_policy' function.
class GetLifecyclePolicyInput(BaseValidatorModel):
    ContainerName: str


# This class is the input for the 'get_metric_policy' function.
class GetMetricPolicyInput(BaseValidatorModel):
    ContainerName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_containers' function.
class ListContainersInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
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
    TagKeys: List[str]

CorsRuleUnion = Union[CorsRule, CorsRuleOutput]


# This class is the input for the 'create_container' function.
class CreateContainerInput(BaseValidatorModel):
    ContainerName: str
    Tags: Optional[List[Tag]] = None


class TagResourceInput(BaseValidatorModel):
    Resource: str
    Tags: List[Tag]


# This class is the output for the 'create_container' function.
class CreateContainerOutput(BaseValidatorModel):
    Container: Container
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_container' function.
class DescribeContainerOutput(BaseValidatorModel):
    Container: Container
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_container_policy' function.
class GetContainerPolicyOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cors_policy' function.
class GetCorsPolicyOutput(BaseValidatorModel):
    CorsPolicy: List[CorsRuleOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_lifecycle_policy' function.
class GetLifecyclePolicyOutput(BaseValidatorModel):
    LifecyclePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_containers' function.
class ListContainersOutput(BaseValidatorModel):
    Containers: List[Container]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
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
    MetricPolicyRules: Optional[List[MetricPolicyRule]] = None


class PutCorsPolicyInput(BaseValidatorModel):
    ContainerName: str
    CorsPolicy: List[CorsRuleUnion]


# This class is the output for the 'get_metric_policy' function.
class GetMetricPolicyOutput(BaseValidatorModel):
    MetricPolicy: MetricPolicyOutput
    ResponseMetadata: ResponseMetadata

MetricPolicyUnion = Union[MetricPolicy, MetricPolicyOutput]


class PutMetricPolicyInput(BaseValidatorModel):
    ContainerName: str
    MetricPolicy: MetricPolicyUnion