from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.dsql.dsql_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ClusterSummary(BaseValidatorModel):
    identifier: str
    arn: str


# This class is the input for the 'create_cluster' function.
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


# This class is the input for the 'delete_cluster' function.
class DeleteClusterInput(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_multi_region_clusters' function.
class DeleteMultiRegionClustersInput(BaseValidatorModel):
    linkedClusterArns: List[str]
    clientToken: Optional[str] = None


# This class is the input for the 'get_cluster' function.
class GetClusterInput(BaseValidatorModel):
    identifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_clusters' function.
class ListClustersInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'tag_resource' function.
class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_cluster' function.
class UpdateClusterInput(BaseValidatorModel):
    identifier: str
    deletionProtectionEnabled: Optional[bool] = None
    clientToken: Optional[str] = None


# This class is the output for the 'create_cluster' function.
class CreateClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_multi_region_clusters' function.
class CreateMultiRegionClustersOutput(BaseValidatorModel):
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster' function.
class DeleteClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cluster' function.
class GetClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_clusters' function.
class ListClustersOutput(BaseValidatorModel):
    clusters: List[ClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster' function.
class UpdateClusterOutput(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_multi_region_clusters' function.
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