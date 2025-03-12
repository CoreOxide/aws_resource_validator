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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class StepInputOutputTypeDef(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[List[str]] = None
    mapOfStringValue: Optional[Dict[str, str]] = None


class TemplateSourceTypeDef(BaseValidatorModel):
    workflowId: Optional[str] = None


class ToolTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None


class TemplateInputTypeDef(BaseValidatorModel):
    inputName: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


class StepOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListMigrationWorkflowTemplatesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    name: Optional[str] = None


class ListMigrationWorkflowsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None


class ListPluginsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PluginSummaryTypeDef(BaseValidatorModel):
    pluginId: Optional[str] = None
    hostname: Optional[str] = None
    status: Optional[PluginHealthType] = None
    ipAddress: Optional[str] = None
    version: Optional[str] = None
    registeredTime: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTemplateStepGroupsRequestTypeDef(BaseValidatorModel):
    templateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTemplateStepsRequestTypeDef(BaseValidatorModel):
    templateId: str
    stepGroupId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkflowStepGroupsRequestTypeDef(BaseValidatorModel):
    workflowId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkflowStepsRequestTypeDef(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PlatformCommandTypeDef(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None


class PlatformScriptKeyTypeDef(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None


class StepInputTypeDef(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringsValue: Optional[Sequence[str]] = None
    mapOfStringValue: Optional[Mapping[str, str]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class WorkflowStepOutputUnionOutputTypeDef(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[List[str]] = None


class WorkflowStepOutputUnionTypeDef(BaseValidatorModel):
    integerValue: Optional[int] = None
    stringValue: Optional[str] = None
    listOfStringValue: Optional[Sequence[str]] = None


class CreateTemplateResponseTypeDef(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTemplateResponseTypeDef(BaseValidatorModel):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTemplateRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateSource: TemplateSourceTypeDef
    templateDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ListMigrationWorkflowTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMigrationWorkflowsRequestPaginateTypeDef(BaseValidatorModel):
    templateId: Optional[str] = None
    adsApplicationConfigurationName: Optional[str] = None
    status: Optional[MigrationWorkflowStatusEnumType] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPluginsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTemplateStepGroupsRequestPaginateTypeDef(BaseValidatorModel):
    templateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTemplateStepsRequestPaginateTypeDef(BaseValidatorModel):
    templateId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkflowStepGroupsRequestPaginateTypeDef(BaseValidatorModel):
    workflowId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkflowStepsRequestPaginateTypeDef(BaseValidatorModel):
    workflowId: str
    stepGroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListMigrationWorkflowTemplatesResponseTypeDef(BaseValidatorModel):
    templateSummary: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MigrationWorkflowSummaryTypeDef(BaseValidatorModel):
    pass


class ListMigrationWorkflowsResponseTypeDef(BaseValidatorModel):
    migrationWorkflowSummary: List[MigrationWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPluginsResponseTypeDef(BaseValidatorModel):
    plugins: List[PluginSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TemplateStepGroupSummaryTypeDef(BaseValidatorModel):
    pass


class ListTemplateStepGroupsResponseTypeDef(BaseValidatorModel):
    templateStepGroupSummary: List[TemplateStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TemplateStepSummaryTypeDef(BaseValidatorModel):
    pass


class ListTemplateStepsResponseTypeDef(BaseValidatorModel):
    templateStepSummaryList: List[TemplateStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowStepGroupSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkflowStepGroupsResponseTypeDef(BaseValidatorModel):
    workflowStepGroupsSummary: List[WorkflowStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowStepSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkflowStepsResponseTypeDef(BaseValidatorModel):
    workflowStepsSummary: List[WorkflowStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class WorkflowStepExtraTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionOutputTypeDef] = None


class StepInputUnionTypeDef(BaseValidatorModel):
    pass


class CreateMigrationWorkflowRequestTypeDef(BaseValidatorModel):
    name: str
    templateId: str
    inputParameters: Mapping[str, StepInputUnionTypeDef]
    description: Optional[str] = None
    applicationConfigurationId: Optional[str] = None
    stepTargets: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class WorkflowStepOutputUnionUnionTypeDef(BaseValidatorModel):
    pass


class WorkflowStepOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    required: Optional[bool] = None
    value: Optional[WorkflowStepOutputUnionUnionTypeDef] = None


