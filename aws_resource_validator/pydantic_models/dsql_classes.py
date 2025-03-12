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
from aws_resource_validator.pydantic_models.dsql_constants import *

class ClusterSummaryTypeDef(BaseValidatorModel):
    identifier: str
    arn: str


class CreateClusterInputTypeDef(BaseValidatorModel):
    deletionProtectionEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LinkedClusterPropertiesTypeDef(BaseValidatorModel):
    deletionProtectionEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteClusterInputTypeDef(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None


class DeleteMultiRegionClustersInputTypeDef(BaseValidatorModel):
    linkedClusterArns: Sequence[str]
    clientToken: Optional[str] = None


class GetClusterInputTypeDef(BaseValidatorModel):
    identifier: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClustersInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateClusterInputTypeDef(BaseValidatorModel):
    identifier: str
    deletionProtectionEnabled: Optional[bool] = None
    clientToken: Optional[str] = None


class CreateClusterOutputTypeDef(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMultiRegionClustersOutputTypeDef(BaseValidatorModel):
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteClusterOutputTypeDef(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetClusterOutputTypeDef(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListClustersOutputTypeDef(BaseValidatorModel):
    clusters: List[ClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateClusterOutputTypeDef(BaseValidatorModel):
    identifier: str
    arn: str
    status: ClusterStatusType
    creationTime: datetime
    deletionProtectionEnabled: bool
    witnessRegion: str
    linkedClusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMultiRegionClustersInputTypeDef(BaseValidatorModel):
    linkedRegionList: Sequence[str]
    witnessRegion: str
    clusterProperties: Optional[Mapping[str, LinkedClusterPropertiesTypeDef]] = None
    clientToken: Optional[str] = None


class GetClusterInputWaitExtraTypeDef(BaseValidatorModel):
    identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetClusterInputWaitTypeDef(BaseValidatorModel):
    identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class ListClustersInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


