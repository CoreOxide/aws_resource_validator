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
from aws_resource_validator.pydantic_models.migrationhuborchestrator_constants import *

class StepInputTypeDef(BaseModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[Sequence[str]] = None
    mapOfStringValue: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TemplateSourceTypeDef(BaseModel):
    workflowId: Optional[str] = None

class CreateWorkflowStepGroupRequestRequestTypeDef(BaseModel):
    workflowId: str
    name: str
    description: Optional[str] = None
    next: Optional[Sequence[str]] = None
    previous: Optional[Sequence[str]] = None

class ToolTypeDef(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None

class DeleteMigrationWorkflowRequestRequestTypeDef(BaseModel):
    id: str

class DeleteTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DeleteWorkflowStepGroupRequestRequestTypeDef(BaseModel):
    workflowId: str
    id: str

class DeleteWorkflowStepRequestRequestTypeDef(BaseModel):
    id: str
    stepGroupId: str
    workflowId: str

class GetMigrationWorkflowRequestRequestTypeDef(BaseModel):
    id: str

class GetMigrationWorkflowTemplateRequestRequestTypeDef(BaseModel):
    id: str

class TemplateInputTypeDef(BaseModel):
    inputName: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None

class GetTemplateStepGroupRequestRequestTypeDef(BaseModel):
    templateId: str
    id: str

class GetTemplateStepRequestRequestTypeDef(BaseModel):
    id: str
    templateId: str
    stepGroupId: str

class StepOutputTypeDef(BaseModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None

class GetWorkflowStepGroupRequestRequestTypeDef(BaseModel):
    id: str
    workflowId: str

class GetWorkflowStepRequestRequestTypeDef(BaseModel):
    workflowId: str
    stepGroupId: str
    id: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListMigrationWorkflowTemplatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    name: Optional[str] = None

class TemplateSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None

class ListMigrationWorkflowsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None

class MigrationWorkflowSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    creationTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    statusMessage: Optional[str] = None
    completedSteps: Optional[int] = None
    totalSteps: Optional[int] = None

class ListPluginsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PluginSummaryTypeDef(BaseModel):
    pluginId: Optional[str] = None
    hostname: Optional[str] = None
    status: Optional[PluginHealthType] = None
    ipAddress: Optional[str] = None
    version: Optional[str] = None
    registeredTime: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTemplateStepGroupsRequestRequestTypeDef(BaseModel):
    templateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TemplateStepGroupSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None

class ListTemplateStepsRequestRequestTypeDef(BaseModel):
    templateId: str
    stepGroupId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TemplateStepSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    stepGroupId: Optional[str] = None
    templateId: Optional[str] = None
    name: Optional[str] = None
    stepActionType: Optional[StepActionTypeType] = None
    targetType: Optional[TargetTypeType] = None
    owner: Optional[OwnerType] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None

class ListWorkflowStepGroupsRequestRequestTypeDef(BaseModel):
    workflowId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class WorkflowStepGroupSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[OwnerType] = None
    status: Optional[StepGroupStatusType] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None

class ListWorkflowStepsRequestRequestTypeDef(BaseModel):
    workflowId: str
    stepGroupId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class WorkflowStepSummaryTypeDef(BaseModel):
    stepId: Optional[str] = None
    name: Optional[str] = None
    stepActionType: Optional[StepActionTypeType] = None
    owner: Optional[OwnerType] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None
    status: Optional[StepStatusType] = None
    statusMessage: Optional[str] = None
    noOfSrvCompleted: Optional[int] = None
    noOfSrvFailed: Optional[int] = None
    totalNoOfSrv: Optional[int] = None
    description: Optional[str] = None
    scriptLocation: Optional[str] = None

class PlatformCommandTypeDef(BaseModel):
    linux: Optional[str] = None
    windows: Optional[str] = None

class PlatformScriptKeyTypeDef(BaseModel):
    linux: Optional[str] = None
    windows: Optional[str] = None

class RetryWorkflowStepRequestRequestTypeDef(BaseModel):
    workflowId: str
    stepGroupId: str
    id: str

class StartMigrationWorkflowRequestRequestTypeDef(BaseModel):
    id: str

class StopMigrationWorkflowRequestRequestTypeDef(BaseModel):
    id: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateTemplateRequestRequestTypeDef(BaseModel):
    id: str
    templateName: Optional[str] = None
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateWorkflowStepGroupRequestRequestTypeDef(BaseModel):
    workflowId: str
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    next: Optional[Sequence[str]] = None
    previous: Optional[Sequence[str]] = None

class WorkflowStepOutputUnionTypeDef(BaseModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[Sequence[str]] = None

class CreateMigrationWorkflowRequestRequestTypeDef(BaseModel):
    name: str
    templateId: str
    inputParameters: Mapping[str, StepInputTypeDef]
    description: Optional[str] = None
    applicationConfigurationId: Optional[str] = None
    stepTargets: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateMigrationWorkflowRequestRequestTypeDef(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    inputParameters: Optional[Mapping[str, StepInputTypeDef]] = None
    stepTargets: Optional[Sequence[str]] = None

class CreateMigrationWorkflowResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    templateId: str
    adsApplicationConfigurationId: str
    workflowInputs: Dict[str, StepInputTypeDef]
    stepTargets: List[str]
    status: MigrationWorkflowStatusEnumType
    creationTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(BaseModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowStepResponseTypeDef(BaseModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMigrationWorkflowResponseTypeDef(BaseModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RetryWorkflowStepResponseTypeDef(BaseModel):
    stepGroupId: str
    workflowId: str
    id: str
    status: StepStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartMigrationWorkflowResponseTypeDef(BaseModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopMigrationWorkflowResponseTypeDef(BaseModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStopTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMigrationWorkflowResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    templateId: str
    adsApplicationConfigurationId: str
    workflowInputs: Dict[str, StepInputTypeDef]
    stepTargets: List[str]
    status: MigrationWorkflowStatusEnumType
    creationTime: datetime
    lastModifiedTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateResponseTypeDef(BaseModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkflowStepResponseTypeDef(BaseModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateRequestRequestTypeDef(BaseModel):
    templateName: str
    templateSource: TemplateSourceTypeDef
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateWorkflowStepGroupResponseTypeDef(BaseModel):
    workflowId: str
    name: str
    id: str
    description: str
    tools: List[ToolTypeDef]
    next: List[str]
    previous: List[str]
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMigrationWorkflowResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    templateId: str
    adsApplicationConfigurationId: str
    adsApplicationName: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    creationTime: datetime
    lastStartTime: datetime
    lastStopTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    tools: List[ToolTypeDef]
    totalSteps: int
    completedSteps: int
    workflowInputs: Dict[str, StepInputTypeDef]
    tags: Dict[str, str]
    workflowBucket: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateStepGroupResponseTypeDef(BaseModel):
    templateId: str
    id: str
    name: str
    description: str
    status: StepGroupStatusType
    creationTime: datetime
    lastModifiedTime: datetime
    tools: List[ToolTypeDef]
    previous: List[str]
    next: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowStepGroupResponseTypeDef(BaseModel):
    id: str
    workflowId: str
    name: str
    description: str
    status: StepGroupStatusType
    owner: OwnerType
    creationTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    tools: List[ToolTypeDef]
    previous: List[str]
    next: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkflowStepGroupResponseTypeDef(BaseModel):
    workflowId: str
    name: str
    id: str
    description: str
    tools: List[ToolTypeDef]
    next: List[str]
    previous: List[str]
    lastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMigrationWorkflowTemplateResponseTypeDef(BaseModel):
    id: str
    templateArn: str
    name: str
    description: str
    inputs: List[TemplateInputTypeDef]
    tools: List[ToolTypeDef]
    creationTime: datetime
    owner: str
    status: TemplateStatusType
    statusMessage: str
    templateClass: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMigrationWorkflowTemplatesRequestListTemplatesPaginateTypeDef(BaseModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationWorkflowsRequestListWorkflowsPaginateTypeDef(BaseModel):
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPluginsRequestListPluginsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateStepGroupsRequestListTemplateStepGroupsPaginateTypeDef(BaseModel):
    templateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateStepsRequestListTemplateStepsPaginateTypeDef(BaseModel):
    templateId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowStepGroupsRequestListWorkflowStepGroupsPaginateTypeDef(BaseModel):
    workflowId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowStepsRequestListWorkflowStepsPaginateTypeDef(BaseModel):
    workflowId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationWorkflowTemplatesResponseTypeDef(BaseModel):
    nextToken: str
    templateSummary: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMigrationWorkflowsResponseTypeDef(BaseModel):
    nextToken: str
    migrationWorkflowSummary: List[MigrationWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPluginsResponseTypeDef(BaseModel):
    nextToken: str
    plugins: List[PluginSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateStepGroupsResponseTypeDef(BaseModel):
    nextToken: str
    templateStepGroupSummary: List[TemplateStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateStepsResponseTypeDef(BaseModel):
    nextToken: str
    templateStepSummaryList: List[TemplateStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowStepGroupsResponseTypeDef(BaseModel):
    nextToken: str
    workflowStepGroupsSummary: List[WorkflowStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowStepsResponseTypeDef(BaseModel):
    nextToken: str
    workflowStepsSummary: List[WorkflowStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StepAutomationConfigurationTypeDef(BaseModel):
    scriptLocationS3Bucket: Optional[str] = None
    scriptLocationS3Key: Optional[PlatformScriptKeyTypeDef] = None
    command: Optional[PlatformCommandTypeDef] = None
    runEnvironment: Optional[RunEnvironmentType] = None
    targetType: Optional[TargetTypeType] = None

class WorkflowStepAutomationConfigurationTypeDef(BaseModel):
    scriptLocationS3Bucket: Optional[str] = None
    scriptLocationS3Key: Optional[PlatformScriptKeyTypeDef] = None
    command: Optional[PlatformCommandTypeDef] = None
    runEnvironment: Optional[RunEnvironmentType] = None
    targetType: Optional[TargetTypeType] = None

class WorkflowStepOutputTypeDef(BaseModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionTypeDef] = None

class GetTemplateStepResponseTypeDef(BaseModel):
    id: str
    stepGroupId: str
    templateId: str
    name: str
    description: str
    stepActionType: StepActionTypeType
    creationTime: str
    previous: List[str]
    next: List[str]
    outputs: List[StepOutputTypeDef]
    stepAutomationConfiguration: StepAutomationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowStepRequestRequestTypeDef(BaseModel):
    name: str
    stepGroupId: str
    workflowId: str
    stepActionType: StepActionTypeType
    description: Optional[str] = None
    workflowStepAutomationConfiguration: Optional[       WorkflowStepAutomationConfigurationTypeDef     ] = None
    stepTarget: Optional[Sequence[str]] = None
    outputs: Optional[Sequence[WorkflowStepOutputTypeDef]] = None
    previous: Optional[Sequence[str]] = None
    next: Optional[Sequence[str]] = None

class GetWorkflowStepResponseTypeDef(BaseModel):
    name: str
    stepGroupId: str
    workflowId: str
    stepId: str
    description: str
    stepActionType: StepActionTypeType
    owner: OwnerType
    workflowStepAutomationConfiguration: WorkflowStepAutomationConfigurationTypeDef
    stepTarget: List[str]
    outputs: List[WorkflowStepOutputTypeDef]
    previous: List[str]
    next: List[str]
    status: StepStatusType
    statusMessage: str
    scriptOutputLocation: str
    creationTime: datetime
    lastStartTime: datetime
    endTime: datetime
    noOfSrvCompleted: int
    noOfSrvFailed: int
    totalNoOfSrv: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkflowStepRequestRequestTypeDef(BaseModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: Optional[str] = None
    description: Optional[str] = None
    stepActionType: Optional[StepActionTypeType] = None
    workflowStepAutomationConfiguration: Optional[       WorkflowStepAutomationConfigurationTypeDef     ] = None
    stepTarget: Optional[Sequence[str]] = None
    outputs: Optional[Sequence[WorkflowStepOutputTypeDef]] = None
    previous: Optional[Sequence[str]] = None
    next: Optional[Sequence[str]] = None
    status: Optional[StepStatusType] = None

