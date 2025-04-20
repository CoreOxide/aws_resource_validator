from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.dsql.dsql_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ClusterSummary(BaseValidatorModel):
    identifier: str
    arn: str


class CreateClusterInput(BaseValidatorModel):
    deletionProtectionEnabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LinkedClusterProperties(BaseValidatorModel):
    deletionProtectionEnabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None


class DeleteClusterInput(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None


class DeleteMultiRegionClustersInput(BaseValidatorModel):
    linkedClusterArns: List[str]
    clientToken: Optional[str] = None


class GetClusterInput(BaseValidatorModel):
    identifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClustersInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateClusterInput(BaseValidatorModel):
    identifier: str
    deletionProtectionEnabled: Optional[bool] = None
    clientToken: Optional[str] = None


class CreateClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


class CreateMultiRegionClustersOutput(BaseValidatorModel):
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadata


class DeleteClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadata


class ListClustersOutput(BaseValidatorModel):
    clusters: List[ClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadata


class CreateMultiRegionClustersInput(BaseValidatorModel):
    linkedRegionList: List[str]
    witnessRegion: str
    clusterProperties: Optional[Dict[str, LinkedClusterProperties]] = None
    clientToken: Optional[str] = None


class GetClusterInputWaitExtra(BaseValidatorModel):
    identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetClusterInputWait(BaseValidatorModel):
    identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class ListClustersInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None