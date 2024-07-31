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
from aws_resource_validator.pydantic_models.launch_wizard_constants import *

class CreateDeploymentInputRequestTypeDef(BaseModel):
    deploymentPatternName: str
    name: str
    specifications: Mapping[str, str]
    workloadName: str
    dryRun: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteDeploymentInputRequestTypeDef(BaseModel):
    deploymentId: str

class DeploymentConditionalFieldTypeDef(BaseModel):
    comparator: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None

class DeploymentDataSummaryTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    name: Optional[str] = None
    patternName: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    workloadName: Optional[str] = None

class DeploymentDataTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None
    deploymentArn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    patternName: Optional[str] = None
    resourceGroup: Optional[str] = None
    specifications: Optional[Dict[str, str]] = None
    status: Optional[DeploymentStatusType] = None
    tags: Optional[Dict[str, str]] = None
    workloadName: Optional[str] = None

class DeploymentEventDataSummaryTypeDef(BaseModel):
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[EventStatusType] = None
    statusReason: Optional[str] = None
    timestamp: Optional[datetime] = None

class DeploymentFilterTypeDef(BaseModel):
    name: Optional[DeploymentFilterKeyType] = None
    values: Optional[Sequence[str]] = None

class GetDeploymentInputRequestTypeDef(BaseModel):
    deploymentId: str

class GetWorkloadDeploymentPatternInputRequestTypeDef(BaseModel):
    deploymentPatternName: str
    workloadName: str

class GetWorkloadInputRequestTypeDef(BaseModel):
    workloadName: str

class WorkloadDataTypeDef(BaseModel):
    description: Optional[str] = None
    displayName: Optional[str] = None
    documentationUrl: Optional[str] = None
    iconUrl: Optional[str] = None
    status: Optional[WorkloadStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDeploymentEventsInputRequestTypeDef(BaseModel):
    deploymentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class ListWorkloadDeploymentPatternsInputRequestTypeDef(BaseModel):
    workloadName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkloadDeploymentPatternDataSummaryTypeDef(BaseModel):
    deploymentPatternName: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    status: Optional[WorkloadDeploymentPatternStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None
    workloadVersionName: Optional[str] = None

class ListWorkloadsInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkloadDataSummaryTypeDef(BaseModel):
    displayName: Optional[str] = None
    workloadName: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateDeploymentOutputTypeDef(BaseModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeploymentOutputTypeDef(BaseModel):
    status: DeploymentStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentSpecificationsFieldTypeDef(BaseModel):
    allowedValues: Optional[List[str]] = None
    conditionals: Optional[List[DeploymentConditionalFieldTypeDef]] = None
    description: Optional[str] = None
    name: Optional[str] = None
    required: Optional[str] = None

class ListDeploymentsOutputTypeDef(BaseModel):
    deployments: List[DeploymentDataSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentOutputTypeDef(BaseModel):
    deployment: DeploymentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentEventsOutputTypeDef(BaseModel):
    deploymentEvents: List[DeploymentEventDataSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsInputRequestTypeDef(BaseModel):
    filters: Optional[Sequence[DeploymentFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetWorkloadOutputTypeDef(BaseModel):
    workload: WorkloadDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentEventsInputListDeploymentEventsPaginateTypeDef(BaseModel):
    deploymentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsInputListDeploymentsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[DeploymentFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkloadDeploymentPatternsInputListWorkloadDeploymentPatternsPaginateTypeDef(BaseModel):
    workloadName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkloadsInputListWorkloadsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkloadDeploymentPatternsOutputTypeDef(BaseModel):
    nextToken: str
    workloadDeploymentPatterns: List[WorkloadDeploymentPatternDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkloadsOutputTypeDef(BaseModel):
    nextToken: str
    workloads: List[WorkloadDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WorkloadDeploymentPatternDataTypeDef(BaseModel):
    deploymentPatternName: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    specifications: Optional[List[DeploymentSpecificationsFieldTypeDef]] = None
    status: Optional[WorkloadDeploymentPatternStatusType] = None
    statusMessage: Optional[str] = None
    workloadName: Optional[str] = None
    workloadVersionName: Optional[str] = None

class GetWorkloadDeploymentPatternOutputTypeDef(BaseModel):
    workloadDeploymentPattern: WorkloadDeploymentPatternDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

