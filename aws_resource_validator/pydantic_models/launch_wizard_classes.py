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
from aws_resource_validator.pydantic_models.launch_wizard_constants import *

class CreateDeploymentInputRequestTypeDef(BaseValidatorModel):
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

class DeleteDeploymentInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str

class DeploymentConditionalFieldTypeDef(BaseValidatorModel):
    comparator: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None

class DeploymentDataSummaryTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    name: Optional[str] = None
    patternName: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    workloadName: Optional[str] = None

class DeploymentDataTypeDef(BaseValidatorModel):
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

class DeploymentEventDataSummaryTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[EventStatusType] = None
    statusReason: Optional[str] = None
    timestamp: Optional[datetime] = None

class DeploymentFilterTypeDef(BaseValidatorModel):
    name: Optional[DeploymentFilterKeyType] = None
    values: Optional[Sequence[str]] = None

class GetDeploymentInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str

class GetWorkloadDeploymentPatternInputRequestTypeDef(BaseValidatorModel):
    deploymentPatternName: str
    workloadName: str

class GetWorkloadInputRequestTypeDef(BaseValidatorModel):
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

class ListDeploymentEventsInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListWorkloadDeploymentPatternsInputRequestTypeDef(BaseValidatorModel):
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

class ListWorkloadsInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkloadDataSummaryTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    workloadName: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
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

class ListDeploymentsOutputTypeDef(BaseValidatorModel):
    deployments: List[DeploymentDataSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentOutputTypeDef(BaseValidatorModel):
    deployment: DeploymentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentEventsOutputTypeDef(BaseValidatorModel):
    deploymentEvents: List[DeploymentEventDataSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsInputRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[DeploymentFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetWorkloadOutputTypeDef(BaseValidatorModel):
    workload: WorkloadDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentEventsInputListDeploymentEventsPaginateTypeDef(BaseValidatorModel):
    deploymentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsInputListDeploymentsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[DeploymentFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkloadDeploymentPatternsInputListWorkloadDeploymentPatternsPaginateTypeDef(BaseValidatorModel):
    workloadName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkloadsInputListWorkloadsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkloadDeploymentPatternsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    workloadDeploymentPatterns: List[WorkloadDeploymentPatternDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkloadsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    workloads: List[WorkloadDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

