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


# This class is the input for the 'create_workflow_step_group' function.
class CreateWorkflowStepGroupRequest(BaseValidatorModel):
    workflowId: str
    name: str
    description: Optional[str] = None
    next: Optional[List[str]] = None
    previous: Optional[List[str]] = None


class Tool(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None


# This class is the input for the 'delete_workflow' function.
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


# This class is the input for the 'get_workflow' function.
class GetMigrationWorkflowRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_template' function.
class GetMigrationWorkflowTemplateRequest(BaseValidatorModel):
    id: str


class TemplateInput(BaseValidatorModel):
    inputName: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


# This class is the input for the 'get_template_step_group' function.
class GetTemplateStepGroupRequest(BaseValidatorModel):
    templateId: str
    id: str


# This class is the input for the 'get_template_step' function.
class GetTemplateStepRequest(BaseValidatorModel):
    id: str
    templateId: str
    stepGroupId: str


class StepOutput(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


# This class is the input for the 'get_workflow_step_group' function.
class GetWorkflowStepGroupRequest(BaseValidatorModel):
    id: str
    workflowId: str


# This class is the input for the 'get_workflow_step' function.
class GetWorkflowStepRequest(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    id: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_templates' function.
class ListMigrationWorkflowTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    name: Optional[str] = None


class TemplateSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'list_workflows' function.
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


# This class is the input for the 'list_plugins' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_template_step_groups' function.
class ListTemplateStepGroupsRequest(BaseValidatorModel):
    templateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TemplateStepGroupSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    previous: Optional[List[str]] = None
    next: Optional[List[str]] = None


# This class is the input for the 'list_template_steps' function.
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


# This class is the input for the 'list_workflow_step_groups' function.
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


# This class is the input for the 'list_workflow_steps' function.
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


# This class is the input for the 'retry_workflow_step' function.
class RetryWorkflowStepRequest(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    id: str


# This class is the input for the 'start_workflow' function.
class StartMigrationWorkflowRequest(BaseValidatorModel):
    id: str


class StepInput(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[List[str]] = None
    mapOfStringValue: Optional[Dict[str, str]] = None


# This class is the input for the 'stop_workflow' function.
class StopMigrationWorkflowRequest(BaseValidatorModel):
    id: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_template' function.
class UpdateTemplateRequest(BaseValidatorModel):
    id: str
    templateName: Optional[str] = None
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_workflow_step_group' function.
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


# This class is the output for the 'create_template' function.
class CreateTemplateResponse(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workflow_step' function.
class CreateWorkflowStepResponse(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_workflow' function.
class DeleteMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'retry_workflow_step' function.
class RetryWorkflowStepResponse(BaseValidatorModel):
    stepGroupId: str
    workflowId: str
    id: str
    status: StepStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_workflow' function.
class StartMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStartTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_workflow' function.
class StopMigrationWorkflowResponse(BaseValidatorModel):
    id: str
    arn: str
    status: MigrationWorkflowStatusEnumType
    statusMessage: str
    lastStopTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_template' function.
class UpdateTemplateResponse(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_workflow_step' function.
class UpdateWorkflowStepResponse(BaseValidatorModel):
    id: str
    stepGroupId: str
    workflowId: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workflow' function.
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


# This class is the output for the 'update_workflow' function.
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


# This class is the input for the 'create_template' function.
class CreateTemplateRequest(BaseValidatorModel):
    templateName: str
    templateSource: TemplateSource
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_workflow_step_group' function.
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


# This class is the output for the 'get_workflow' function.
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


# This class is the output for the 'get_template_step_group' function.
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


# This class is the output for the 'get_workflow_step_group' function.
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


# This class is the output for the 'update_workflow_step_group' function.
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


# This class is the output for the 'get_template' function.
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


# This class is the output for the 'list_templates' function.
class ListMigrationWorkflowTemplatesResponse(BaseValidatorModel):
    templateSummary: List[TemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_workflows' function.
class ListMigrationWorkflowsResponse(BaseValidatorModel):
    migrationWorkflowSummary: List[MigrationWorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_plugins' function.
class ListPluginsResponse(BaseValidatorModel):
    plugins: List[PluginSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_template_step_groups' function.
class ListTemplateStepGroupsResponse(BaseValidatorModel):
    templateStepGroupSummary: List[TemplateStepGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_template_steps' function.
class ListTemplateStepsResponse(BaseValidatorModel):
    templateStepSummaryList: List[TemplateStepSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_workflow_step_groups' function.
class ListWorkflowStepGroupsResponse(BaseValidatorModel):
    workflowStepGroupsSummary: List[WorkflowStepGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_workflow_steps' function.
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


# This class is the output for the 'get_template_step' function.
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


# This class is the input for the 'create_workflow' function.
class CreateMigrationWorkflowRequest(BaseValidatorModel):
    name: str
    templateId: str
    inputParameters: Dict[str, StepInputUnion]
    description: Optional[str] = None
    applicationConfigurationId: Optional[str] = None
    stepTargets: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_workflow' function.
class UpdateMigrationWorkflowRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    inputParameters: Optional[Dict[str, StepInputUnion]] = None
    stepTargets: Optional[List[str]] = None


# This class is the output for the 'get_workflow_step' function.
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


# This class is the input for the 'create_workflow_step' function.
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


# This class is the input for the 'update_workflow_step' function.
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