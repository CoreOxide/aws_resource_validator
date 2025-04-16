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

class CreateDeploymentInput(BaseValidatorModel):
    deploymentPatternName: str
    name: str
    specifications: Mapping[str, str]
    workloadName: str
    dryRun: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteDeploymentInput(BaseValidatorModel):
    deploymentId: str


class DeploymentConditionalField(BaseValidatorModel):
    comparator: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None


class DeploymentEventDataSummary(BaseValidatorModel):
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[EventStatusType] = None
    statusReason: Optional[str] = None
    timestamp: Optional[datetime] = None


class DeploymentFilter(BaseValidatorModel):
    name: Optional[DeploymentFilterKeyType] = None
    values: Optional[Sequence[str]] = None


class GetDeploymentInput(BaseValidatorModel):
    deploymentId: str


class GetWorkloadDeploymentPatternInput(BaseValidatorModel):
    deploymentPatternName: str
    workloadName: str


class GetWorkloadInput(BaseValidatorModel):
    workloadName: str


class WorkloadData(BaseValidatorModel):
    description: Optional[str] = None
    displayName: Optional[str] = None
    documentationUrl: Optional[str] = None
    iconUrl: Optional[str] = None
    status: Optional[WorkloadStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDeploymentEventsInput(BaseValidatorModel):
    deploymentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class ListWorkloadDeploymentPatternsInput(BaseValidatorModel):
    workloadName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkloadDeploymentPatternDataSummary(BaseValidatorModel):
    deploymentPatternName: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    status: Optional[WorkloadDeploymentPatternStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None
    workloadVersionName: Optional[str] = None


class ListWorkloadsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkloadDataSummary(BaseValidatorModel):
    displayName: Optional[str] = None
    workloadName: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateDeploymentOutput(BaseValidatorModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadata


class DeleteDeploymentOutput(BaseValidatorModel):
    status: DeploymentStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeploymentSpecificationsField(BaseValidatorModel):
    allowedValues: Optional[List[str]] = None
    conditionals: Optional[List[DeploymentConditionalField]] = None
    description: Optional[str] = None
    name: Optional[str] = None
    required: Optional[str] = None


class DeploymentDataSummary(BaseValidatorModel):
    pass


class ListDeploymentsOutput(BaseValidatorModel):
    deployments: List[DeploymentDataSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DeploymentData(BaseValidatorModel):
    pass


class GetDeploymentOutput(BaseValidatorModel):
    deployment: DeploymentData
    ResponseMetadata: ResponseMetadata


class ListDeploymentEventsOutput(BaseValidatorModel):
    deploymentEvents: List[DeploymentEventDataSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeploymentsInput(BaseValidatorModel):
    filters: Optional[Sequence[DeploymentFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetWorkloadOutput(BaseValidatorModel):
    workload: WorkloadData
    ResponseMetadata: ResponseMetadata


class ListDeploymentEventsInputPaginate(BaseValidatorModel):
    deploymentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentsInputPaginate(BaseValidatorModel):
    filters: Optional[Sequence[DeploymentFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkloadDeploymentPatternsInputPaginate(BaseValidatorModel):
    workloadName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkloadsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkloadDeploymentPatternsOutput(BaseValidatorModel):
    workloadDeploymentPatterns: List[WorkloadDeploymentPatternDataSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkloadsOutput(BaseValidatorModel):
    workloads: List[WorkloadDataSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkloadDeploymentPatternData(BaseValidatorModel):
    deploymentPatternName: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    specifications: Optional[List[DeploymentSpecificationsField]] = None
    status: Optional[WorkloadDeploymentPatternStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None
    workloadVersionName: Optional[str] = None


class GetWorkloadDeploymentPatternOutput(BaseValidatorModel):
    workloadDeploymentPattern: WorkloadDeploymentPatternData
    ResponseMetadata: ResponseMetadata


