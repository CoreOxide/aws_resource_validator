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
from aws_resource_validator.pydantic_models.migrationhuborchestrator_constants import *

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


class Tool(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None


class TemplateInput(BaseValidatorModel):
    inputName: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


class StepOutput(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListMigrationWorkflowTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    name: Optional[str] = None


class ListMigrationWorkflowsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None


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


class ListTemplateStepsRequest(BaseValidatorModel):
    templateId: str
    stepGroupId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkflowStepGroupsRequest(BaseValidatorModel):
    workflowId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkflowStepsRequest(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PlatformCommand(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None


class PlatformScriptKey(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None


class StepInput(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[Sequence[str]] = None
    mapOfStringValue: Optional[Mapping[str, str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class WorkflowStepOutputUnionOutput(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[List[str]] = None


class WorkflowStepOutputUnion(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[Sequence[str]] = None


class CreateTemplateResponse(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateTemplateResponse(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateTemplateRequest(BaseValidatorModel):
    templateName: str
    templateSource: TemplateSource
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


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


class TemplateSummary(BaseValidatorModel):
    pass


class ListMigrationWorkflowTemplatesResponse(BaseValidatorModel):
    templateSummary: List[TemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MigrationWorkflowSummary(BaseValidatorModel):
    pass


class ListMigrationWorkflowsResponse(BaseValidatorModel):
    migrationWorkflowSummary: List[MigrationWorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPluginsResponse(BaseValidatorModel):
    plugins: List[PluginSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TemplateStepGroupSummary(BaseValidatorModel):
    pass


class ListTemplateStepGroupsResponse(BaseValidatorModel):
    templateStepGroupSummary: List[TemplateStepGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TemplateStepSummary(BaseValidatorModel):
    pass


class ListTemplateStepsResponse(BaseValidatorModel):
    templateStepSummaryList: List[TemplateStepSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkflowStepGroupSummary(BaseValidatorModel):
    pass


class ListWorkflowStepGroupsResponse(BaseValidatorModel):
    workflowStepGroupsSummary: List[WorkflowStepGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkflowStepSummary(BaseValidatorModel):
    pass


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


class WorkflowStepExtra(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionOutput] = None


class StepInputUnion(BaseValidatorModel):
    pass


class CreateMigrationWorkflowRequest(BaseValidatorModel):
    name: str
    templateId: str
    inputParameters: Mapping[str, StepInputUnion]
    description: Optional[str] = None
    applicationConfigurationId: Optional[str] = None
    stepTargets: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class WorkflowStepOutputUnionUnion(BaseValidatorModel):
    pass


class WorkflowStepOutput(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionUnion] = None


