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
from aws_resource_validator.pydantic_models.launch_wizard_constants import *

class CreateDeploymentInputTypeDef(BaseValidatorModel):
    deploymentPatternName: str
    name: str
    specifications: Mapping[str, str]
    workloadName: str
    dryRun: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteDeploymentInputTypeDef(BaseValidatorModel):
    deploymentId: str


class DeploymentConditionalFieldTypeDef(BaseValidatorModel):
    comparator: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None


class DeploymentEventDataSummaryTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[EventStatusType] = None
    statusReason: Optional[str] = None
    timestamp: Optional[datetime] = None


class DeploymentFilterTypeDef(BaseValidatorModel):
    name: Optional[DeploymentFilterKeyType] = None
    values: Optional[Sequence[str]] = None


class GetDeploymentInputTypeDef(BaseValidatorModel):
    deploymentId: str


class GetWorkloadDeploymentPatternInputTypeDef(BaseValidatorModel):
    deploymentPatternName: str
    workloadName: str


class GetWorkloadInputTypeDef(BaseValidatorModel):
    workloadName: str


class WorkloadDataTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    displayName: Optional[str] = None
    documentationUrl: Optional[str] = None
    iconUrl: Optional[str] = None
    status: Optional[WorkloadStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDeploymentEventsInputTypeDef(BaseValidatorModel):
    deploymentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class ListWorkloadDeploymentPatternsInputTypeDef(BaseValidatorModel):
    workloadName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkloadDeploymentPatternDataSummaryTypeDef(BaseValidatorModel):
    deploymentPatternName: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    status: Optional[WorkloadDeploymentPatternStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None
    workloadVersionName: Optional[str] = None


class ListWorkloadsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkloadDataSummaryTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    workloadName: Optional[str] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateDeploymentOutputTypeDef(BaseValidatorModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDeploymentOutputTypeDef(BaseValidatorModel):
    status: DeploymentStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentSpecificationsFieldTypeDef(BaseValidatorModel):
    allowedValues: Optional[List[str]] = None
    conditionals: Optional[List[DeploymentConditionalFieldTypeDef]] = None
    description: Optional[str] = None
    name: Optional[str] = None
    required: Optional[str] = None


class DeploymentDataSummaryTypeDef(BaseValidatorModel):
    pass


class ListDeploymentsOutputTypeDef(BaseValidatorModel):
    deployments: List[DeploymentDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DeploymentDataTypeDef(BaseValidatorModel):
    pass


class GetDeploymentOutputTypeDef(BaseValidatorModel):
    deployment: DeploymentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDeploymentEventsOutputTypeDef(BaseValidatorModel):
    deploymentEvents: List[DeploymentEventDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDeploymentsInputTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[DeploymentFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetWorkloadOutputTypeDef(BaseValidatorModel):
    workload: WorkloadDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDeploymentEventsInputPaginateTypeDef(BaseValidatorModel):
    deploymentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeploymentsInputPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[DeploymentFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkloadDeploymentPatternsInputPaginateTypeDef(BaseValidatorModel):
    workloadName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkloadsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkloadDeploymentPatternsOutputTypeDef(BaseValidatorModel):
    workloadDeploymentPatterns: List[WorkloadDeploymentPatternDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListWorkloadsOutputTypeDef(BaseValidatorModel):
    workloads: List[WorkloadDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkloadDeploymentPatternDataTypeDef(BaseValidatorModel):
    deploymentPatternName: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    specifications: Optional[List[DeploymentSpecificationsFieldTypeDef]] = None
    status: Optional[WorkloadDeploymentPatternStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None
    workloadVersionName: Optional[str] = None


class GetWorkloadDeploymentPatternOutputTypeDef(BaseValidatorModel):
    workloadDeploymentPattern: WorkloadDeploymentPatternDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


