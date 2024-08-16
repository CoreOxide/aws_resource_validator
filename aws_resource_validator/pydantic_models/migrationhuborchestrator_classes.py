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
from aws_resource_validator.pydantic_models.migrationhuborchestrator_constants import *

class StepInputTypeDef(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[Sequence[str]] = None
    mapOfStringValue: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TemplateSourceTypeDef(BaseValidatorModel):
    workflowId: Optional[str] = None

class CreateWorkflowStepGroupRequestRequestTypeDef(BaseValidatorModel):
    workflowId: str
    name: str
    description: Optional[str] = None
    next: Optional[Sequence[str]] = None
    previous: Optional[Sequence[str]] = None

class ToolTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None

class DeleteMigrationWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteWorkflowStepGroupRequestRequestTypeDef(BaseValidatorModel):
    workflowId: str
    id: str

class DeleteWorkflowStepRequestRequestTypeDef(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str

class GetMigrationWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetMigrationWorkflowTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class TemplateInputTypeDef(BaseValidatorModel):
    inputName: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None

class GetTemplateStepGroupRequestRequestTypeDef(BaseValidatorModel):
    templateId: str
    id: str

class GetTemplateStepRequestRequestTypeDef(BaseValidatorModel):
    id: str
    templateId: str
    stepGroupId: str

class StepOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None

class GetWorkflowStepGroupRequestRequestTypeDef(BaseValidatorModel):
    id: str
    workflowId: str

class GetWorkflowStepRequestRequestTypeDef(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    id: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListMigrationWorkflowTemplatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    name: Optional[str] = None

class TemplateSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None

class ListMigrationWorkflowsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None

class MigrationWorkflowSummaryTypeDef(BaseValidatorModel):
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

class ListPluginsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PluginSummaryTypeDef(BaseValidatorModel):
    pluginId: Optional[str] = None
    hostname: Optional[str] = None
    status: Optional[PluginHealthType] = None
    ipAddress: Optional[str] = None
    version: Optional[str] = None
    registeredTime: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTemplateStepGroupsRequestRequestTypeDef(BaseValidatorModel):
    templateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TemplateStepGroupSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None

class ListTemplateStepsRequestRequestTypeDef(BaseValidatorModel):
    templateId: str
    stepGroupId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TemplateStepSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    stepGroupId: Optional[str] = None
    templateId: Optional[str] = None
    name: Optional[str] = None
    stepActionType: Optional[StepActionTypeType] = None
    targetType: Optional[TargetTypeType] = None
    owner: Optional[OwnerType] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None

class ListWorkflowStepGroupsRequestRequestTypeDef(BaseValidatorModel):
    workflowId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class WorkflowStepGroupSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[OwnerType] = None
    status: Optional[StepGroupStatusType] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None

class ListWorkflowStepsRequestRequestTypeDef(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class WorkflowStepSummaryTypeDef(BaseValidatorModel):
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

class PlatformCommandTypeDef(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None

class PlatformScriptKeyTypeDef(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None

class RetryWorkflowStepRequestRequestTypeDef(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    id: str

class StartMigrationWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str

class StopMigrationWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str
    templateName: Optional[str] = None
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateWorkflowStepGroupRequestRequestTypeDef(BaseValidatorModel):
    workflowId: str
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    next: Optional[Sequence[str]] = None
    previous: Optional[Sequence[str]] = None

class WorkflowStepOutputUnionTypeDef(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[Sequence[str]] = None

class CreateMigrationWorkflowRequestRequestTypeDef(BaseValidatorModel):
    name: str
    templateId: str
    inputParameters: Mapping[str, StepInputTypeDef]
    description: Optional[str] = None
    applicationConfigurationId: Optional[str] = None
    stepTargets: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateMigrationWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    inputParameters: Optional[Mapping[str, StepInputTypeDef]] = None
    stepTargets: Optional[Sequence[str]] = None

class CreateMigrationWorkflowResponseTypeDef(BaseValidatorModel):
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

class CreateTemplateResponseTypeDef(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowStepResponseTypeDef(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMigrationWorkflowResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RetryWorkflowStepResponseTypeDef(BaseValidatorModel):
    stepGroupId: str
    workflowId: str
    id: str
    status: StepStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartMigrationWorkflowResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopMigrationWorkflowResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStopTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMigrationWorkflowResponseTypeDef(BaseValidatorModel):
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

class UpdateTemplateResponseTypeDef(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkflowStepResponseTypeDef(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateSource: TemplateSourceTypeDef
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateWorkflowStepGroupResponseTypeDef(BaseValidatorModel):
    workflowId: str
    name: str
    id: str
    description: str
    tools: List[ToolTypeDef]
    next: List[str]
    previous: List[str]
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMigrationWorkflowResponseTypeDef(BaseValidatorModel):
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

class GetTemplateStepGroupResponseTypeDef(BaseValidatorModel):
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

class GetWorkflowStepGroupResponseTypeDef(BaseValidatorModel):
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

class UpdateWorkflowStepGroupResponseTypeDef(BaseValidatorModel):
    workflowId: str
    name: str
    id: str
    description: str
    tools: List[ToolTypeDef]
    next: List[str]
    previous: List[str]
    lastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMigrationWorkflowTemplateResponseTypeDef(BaseValidatorModel):
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

class ListMigrationWorkflowTemplatesRequestListTemplatesPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationWorkflowsRequestListWorkflowsPaginateTypeDef(BaseValidatorModel):
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPluginsRequestListPluginsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateStepGroupsRequestListTemplateStepGroupsPaginateTypeDef(BaseValidatorModel):
    templateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateStepsRequestListTemplateStepsPaginateTypeDef(BaseValidatorModel):
    templateId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowStepGroupsRequestListWorkflowStepGroupsPaginateTypeDef(BaseValidatorModel):
    workflowId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowStepsRequestListWorkflowStepsPaginateTypeDef(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationWorkflowTemplatesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    templateSummary: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMigrationWorkflowsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    migrationWorkflowSummary: List[MigrationWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPluginsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    plugins: List[PluginSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateStepGroupsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    templateStepGroupSummary: List[TemplateStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateStepsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    templateStepSummaryList: List[TemplateStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowStepGroupsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    workflowStepGroupsSummary: List[WorkflowStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowStepsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    workflowStepsSummary: List[WorkflowStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StepAutomationConfigurationTypeDef(BaseValidatorModel):
    scriptLocationS3Bucket: Optional[str] = None
    scriptLocationS3Key: Optional[PlatformScriptKeyTypeDef] = None
    command: Optional[PlatformCommandTypeDef] = None
    runEnvironment: Optional[RunEnvironmentType] = None
    targetType: Optional[TargetTypeType] = None

class WorkflowStepAutomationConfigurationTypeDef(BaseValidatorModel):
    scriptLocationS3Bucket: Optional[str] = None
    scriptLocationS3Key: Optional[PlatformScriptKeyTypeDef] = None
    command: Optional[PlatformCommandTypeDef] = None
    runEnvironment: Optional[RunEnvironmentType] = None
    targetType: Optional[TargetTypeType] = None

class WorkflowStepOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionTypeDef] = None

class GetTemplateStepResponseTypeDef(BaseValidatorModel):
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

class CreateWorkflowStepRequestRequestTypeDef(BaseValidatorModel):
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

class GetWorkflowStepResponseTypeDef(BaseValidatorModel):
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

class UpdateWorkflowStepRequestRequestTypeDef(BaseValidatorModel):
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

