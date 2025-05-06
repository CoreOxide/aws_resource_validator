from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class StepInputOutput(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[List[str]] = None
    mapOfStringValue: Optional[Dict[str, str]] = None


class TemplateSource(BaseValidatorModel):
    workflowId: Optional[str] = None


class CreateWorkflowStepGroupRequest(BaseValidatorModel):
    workflowId: str
    name: str
    description: Optional[str] = None
    next: Optional[List[str]] = None
    previous: Optional[List[str]] = None


class Tool(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None


class DeleteMigrationWorkflowRequest(BaseValidatorModel):
    id: str


class DeleteTemplateRequest(BaseValidatorModel):
    id: str


class DeleteWorkflowStepGroupRequest(BaseValidatorModel):
    workflowId: str
    id: str


class DeleteWorkflowStepRequest(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str


class GetMigrationWorkflowRequest(BaseValidatorModel):
    id: str


class GetMigrationWorkflowTemplateRequest(BaseValidatorModel):
    id: str


class TemplateInput(BaseValidatorModel):
    inputName: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


class GetTemplateStepGroupRequest(BaseValidatorModel):
    templateId: str
    id: str


class GetTemplateStepRequest(BaseValidatorModel):
    id: str
    templateId: str
    stepGroupId: str


class StepOutput(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


class GetWorkflowStepGroupRequest(BaseValidatorModel):
    id: str
    workflowId: str


class GetWorkflowStepRequest(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    id: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListMigrationWorkflowTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    name: Optional[str] = None


class TemplateSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None


class ListMigrationWorkflowsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None


class MigrationWorkflowSummary(BaseValidatorModel):
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


class ListPluginsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PluginSummary(BaseValidatorModel):
    pluginId: Optional[str] = None
    hostname: Optional[str] = None
    status: Optional[PluginHealthType] = None
    ipAddress: Optional[str] = None
    version: Optional[str] = None
    registeredTime: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTemplateStepGroupsRequest(BaseValidatorModel):
    templateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TemplateStepGroupSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None


class ListTemplateStepsRequest(BaseValidatorModel):
    templateId: str
    stepGroupId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TemplateStepSummary(BaseValidatorModel):
    id: Optional[str] = None
    stepGroupId: Optional[str] = None
    templateId: Optional[str] = None
    name: Optional[str] = None
    stepActionType: Optional[StepActionTypeType] = None
    targetType: Optional[TargetTypeType] = None
    owner: Optional[OwnerType] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None


class ListWorkflowStepGroupsRequest(BaseValidatorModel):
    workflowId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkflowStepGroupSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[OwnerType] = None
    status: Optional[StepGroupStatusType] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None


class ListWorkflowStepsRequest(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkflowStepSummary(BaseValidatorModel):
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


class PlatformCommand(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None


class PlatformScriptKey(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None


class RetryWorkflowStepRequest(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    id: str


class StartMigrationWorkflowRequest(BaseValidatorModel):
    id: str


class StepInput(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[List[str]] = None
    mapOfStringValue: Optional[Dict[str, str]] = None


class StopMigrationWorkflowRequest(BaseValidatorModel):
    id: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateTemplateRequest(BaseValidatorModel):
    id: str
    templateName: Optional[str] = None
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateWorkflowStepGroupRequest(BaseValidatorModel):
    workflowId: str
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    next: Optional[List[str]] = None
    previous: Optional[List[str]] = None


class WorkflowStepOutputUnionOutput(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[List[str]] = None


class WorkflowStepOutputUnion(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[List[str]] = None


class CreateTemplateResponse(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateWorkflowStepResponse(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadata


class DeleteMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RetryWorkflowStepResponse(BaseValidatorModel):
    stepGroupId: str
    workflowId: str
    id: str
    status: StepStatusType
    ResponseMetadata: ResponseMetadata


class StartMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStartTime: datetime
    ResponseMetadata: ResponseMetadata


class StopMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStopTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateTemplateResponse(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateWorkflowStepResponse(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadata


class CreateMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    templateId: str
    adsApplicationConfigurationId: str
    workflowInputs: Dict[str, StepInputOutput]
    stepTargets: List[str]
    status: MigrationWorkflowStatusEnumType
    creationTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    templateId: str
    adsApplicationConfigurationId: str
    workflowInputs: Dict[str, StepInputOutput]
    stepTargets: List[str]
    status: MigrationWorkflowStatusEnumType
    creationTime: datetime
    lastModifiedTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateTemplateRequest(BaseValidatorModel):
    templateName: str
    templateSource: TemplateSource
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateWorkflowStepGroupResponse(BaseValidatorModel):
    workflowId: str
    name: str
    id: str
    description: str
    tools: List[Tool]
    next: List[str]
    previous: List[str]
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class GetMigrationWorkflowResponse(BaseValidatorModel):
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
    tools: List[Tool]
    totalSteps: int
    completedSteps: int
    workflowInputs: Dict[str, StepInputOutput]
    tags: Dict[str, str]
    workflowBucket: str
    ResponseMetadata: ResponseMetadata


class GetTemplateStepGroupResponse(BaseValidatorModel):
    templateId: str
    id: str
    name: str
    description: str
    status: StepGroupStatusType
    creationTime: datetime
    lastModifiedTime: datetime
    tools: List[Tool]
    previous: List[str]
    next: List[str]
    ResponseMetadata: ResponseMetadata


class GetWorkflowStepGroupResponse(BaseValidatorModel):
    id: str
    workflowId: str
    name: str
    description: str
    status: StepGroupStatusType
    owner: OwnerType
    creationTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    tools: List[Tool]
    previous: List[str]
    next: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateWorkflowStepGroupResponse(BaseValidatorModel):
    workflowId: str
    name: str
    id: str
    description: str
    tools: List[Tool]
    next: List[str]
    previous: List[str]
    lastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class GetMigrationWorkflowTemplateResponse(BaseValidatorModel):
    id: str
    templateArn: str
    name: str
    description: str
    inputs: List[TemplateInput]
    tools: List[Tool]
    creationTime: datetime
    owner: str
    status: TemplateStatusType
    statusMessage: str
    templateClass: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListMigrationWorkflowTemplatesRequestPaginate(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMigrationWorkflowsRequestPaginate(BaseValidatorModel):
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPluginsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplateStepGroupsRequestPaginate(BaseValidatorModel):
    templateId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplateStepsRequestPaginate(BaseValidatorModel):
    templateId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowStepGroupsRequestPaginate(BaseValidatorModel):
    workflowId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowStepsRequestPaginate(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMigrationWorkflowTemplatesResponse(BaseValidatorModel):
    templateSummary: List[TemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMigrationWorkflowsResponse(BaseValidatorModel):
    migrationWorkflowSummary: List[MigrationWorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPluginsResponse(BaseValidatorModel):
    plugins: List[PluginSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTemplateStepGroupsResponse(BaseValidatorModel):
    templateStepGroupSummary: List[TemplateStepGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTemplateStepsResponse(BaseValidatorModel):
    templateStepSummaryList: List[TemplateStepSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkflowStepGroupsResponse(BaseValidatorModel):
    workflowStepGroupsSummary: List[WorkflowStepGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkflowStepsResponse(BaseValidatorModel):
    workflowStepsSummary: List[WorkflowStepSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StepAutomationConfiguration(BaseValidatorModel):
    scriptLocationS3Bucket: Optional[str] = None
    scriptLocationS3Key: Optional[PlatformScriptKey] = None
    command: Optional[PlatformCommand] = None
    runEnvironment: Optional[RunEnvironmentType] = None
    targetType: Optional[TargetTypeType] = None


class WorkflowStepAutomationConfiguration(BaseValidatorModel):
    scriptLocationS3Bucket: Optional[str] = None
    scriptLocationS3Key: Optional[PlatformScriptKey] = None
    command: Optional[PlatformCommand] = None
    runEnvironment: Optional[RunEnvironmentType] = None
    targetType: Optional[TargetTypeType] = None

StepInputUnion = Union[StepInput, StepInputOutput]


class WorkflowStepExtra(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionOutput] = None

WorkflowStepOutputUnionUnion = Union[WorkflowStepOutputUnion, WorkflowStepOutputUnionOutput]


class GetTemplateStepResponse(BaseValidatorModel):
    id: str
    stepGroupId: str
    templateId: str
    name: str
    description: str
    stepActionType: StepActionTypeType
    creationTime: str
    previous: List[str]
    next: List[str]
    outputs: List[StepOutput]
    stepAutomationConfiguration: StepAutomationConfiguration
    ResponseMetadata: ResponseMetadata


class CreateMigrationWorkflowRequest(BaseValidatorModel):
    name: str
    templateId: str
    inputParameters: Dict[str, StepInputUnion]
    description: Optional[str] = None
    applicationConfigurationId: Optional[str] = None
    stepTargets: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None


class UpdateMigrationWorkflowRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    inputParameters: Optional[Dict[str, StepInputUnion]] = None
    stepTargets: Optional[List[str]] = None


class GetWorkflowStepResponse(BaseValidatorModel):
    name: str
    stepGroupId: str
    workflowId: str
    stepId: str
    description: str
    stepActionType: StepActionTypeType
    owner: OwnerType
    workflowStepAutomationConfiguration: WorkflowStepAutomationConfiguration
    stepTarget: List[str]
    outputs: List[WorkflowStepExtra]
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
    ResponseMetadata: ResponseMetadata


class WorkflowStepOutput(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionUnion] = None

WorkflowStepUnion = Union[WorkflowStepOutput, WorkflowStepExtra]


class CreateWorkflowStepRequest(BaseValidatorModel):
    name: str
    stepGroupId: str
    workflowId: str
    stepActionType: StepActionTypeType
    description: Optional[str] = None
    workflowStepAutomationConfiguration: Optional[WorkflowStepAutomationConfiguration] = None
    stepTarget: Optional[List[str]] = None
    outputs: Optional[List[WorkflowStepUnion]] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None


class UpdateWorkflowStepRequest(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: Optional[str] = None
    description: Optional[str] = None
    stepActionType: Optional[StepActionTypeType] = None
    workflowStepAutomationConfiguration: Optional[WorkflowStepAutomationConfiguration] = None
    stepTarget: Optional[List[str]] = None
    outputs: Optional[List[WorkflowStepUnion]] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None
    status: Optional[StepStatusType] = None