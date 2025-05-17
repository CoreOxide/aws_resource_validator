from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.amp.amp_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AlertManagerDefinitionStatus(BaseValidatorModel):
    statusCode: AlertManagerDefinitionStatusCodeType
    statusReason: Optional[str] = None


class AmpConfiguration(BaseValidatorModel):
    workspaceArn: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_logging_configuration' function.
class CreateLoggingConfigurationRequest(BaseValidatorModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None


class LoggingConfigurationStatus(BaseValidatorModel):
    statusCode: LoggingConfigurationStatusCodeType
    statusReason: Optional[str] = None


class RuleGroupsNamespaceStatus(BaseValidatorModel):
    statusCode: RuleGroupsNamespaceStatusCodeType
    statusReason: Optional[str] = None


class RoleConfiguration(BaseValidatorModel):
    sourceRoleArn: Optional[str] = None
    targetRoleArn: Optional[str] = None


class ScraperStatus(BaseValidatorModel):
    statusCode: ScraperStatusCodeType


# This class is the input for the 'create_workspace' function.
class CreateWorkspaceRequest(BaseValidatorModel):
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class WorkspaceStatus(BaseValidatorModel):
    statusCode: WorkspaceStatusCodeType


# This class is the input for the 'delete_alert_manager_definition' function.
class DeleteAlertManagerDefinitionRequest(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_logging_configuration' function.
class DeleteLoggingConfigurationRequest(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_rule_groups_namespace' function.
class DeleteRuleGroupsNamespaceRequest(BaseValidatorModel):
    name: str
    workspaceId: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_scraper' function.
class DeleteScraperRequest(BaseValidatorModel):
    scraperId: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_workspace' function.
class DeleteWorkspaceRequest(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


# This class is the input for the 'describe_alert_manager_definition' function.
class DescribeAlertManagerDefinitionRequest(BaseValidatorModel):
    workspaceId: str


# This class is the input for the 'describe_logging_configuration' function.
class DescribeLoggingConfigurationRequest(BaseValidatorModel):
    workspaceId: str


# This class is the input for the 'describe_rule_groups_namespace' function.
class DescribeRuleGroupsNamespaceRequest(BaseValidatorModel):
    name: str
    workspaceId: str


# This class is the input for the 'describe_scraper' function.
class DescribeScraperRequest(BaseValidatorModel):
    scraperId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_workspace' function.
class DescribeWorkspaceRequest(BaseValidatorModel):
    workspaceId: str


class EksConfigurationOutput(BaseValidatorModel):
    clusterArn: str
    subnetIds: List[str]
    securityGroupIds: Optional[List[str]] = None


class EksConfiguration(BaseValidatorModel):
    clusterArn: str
    subnetIds: List[str]
    securityGroupIds: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_rule_groups_namespaces' function.
class ListRuleGroupsNamespacesRequest(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_scrapers' function.
class ListScrapersRequest(BaseValidatorModel):
    filters: Optional[Dict[str, List[str]]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_workspaces' function.
class ListWorkspacesRequest(BaseValidatorModel):
    alias: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ScrapeConfigurationOutput(BaseValidatorModel):
    configurationBlob: Optional[bytes] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_logging_configuration' function.
class UpdateLoggingConfigurationRequest(BaseValidatorModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None


# This class is the input for the 'update_workspace_alias' function.
class UpdateWorkspaceAliasRequest(BaseValidatorModel):
    workspaceId: str
    alias: Optional[str] = None
    clientToken: Optional[str] = None


class AlertManagerDefinitionDescription(BaseValidatorModel):
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    status: AlertManagerDefinitionStatus


class Destination(BaseValidatorModel):
    ampConfiguration: Optional[AmpConfiguration] = None


# This class is the input for the 'create_alert_manager_definition' function.
class CreateAlertManagerDefinitionRequest(BaseValidatorModel):
    data: Blob
    workspaceId: str
    clientToken: Optional[str] = None


# This class is the input for the 'create_rule_groups_namespace' function.
class CreateRuleGroupsNamespaceRequest(BaseValidatorModel):
    data: Blob
    name: str
    workspaceId: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'put_alert_manager_definition' function.
class PutAlertManagerDefinitionRequest(BaseValidatorModel):
    data: Blob
    workspaceId: str
    clientToken: Optional[str] = None


# This class is the input for the 'put_rule_groups_namespace' function.
class PutRuleGroupsNamespaceRequest(BaseValidatorModel):
    data: Blob
    name: str
    workspaceId: str
    clientToken: Optional[str] = None


class ScrapeConfiguration(BaseValidatorModel):
    configurationBlob: Optional[Blob] = None


# This class is the output for the 'create_alert_manager_definition' function.
class CreateAlertManagerDefinitionResponse(BaseValidatorModel):
    status: AlertManagerDefinitionStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_workspace_alias' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDefaultScraperConfigurationResponse(BaseValidatorModel):
    configuration: bytes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_alert_manager_definition' function.
class PutAlertManagerDefinitionResponse(BaseValidatorModel):
    status: AlertManagerDefinitionStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_logging_configuration' function.
class CreateLoggingConfigurationResponse(BaseValidatorModel):
    status: LoggingConfigurationStatus
    ResponseMetadata: ResponseMetadata


class LoggingConfigurationMetadata(BaseValidatorModel):
    createdAt: datetime
    logGroupArn: str
    modifiedAt: datetime
    status: LoggingConfigurationStatus
    workspace: str


# This class is the output for the 'update_logging_configuration' function.
class UpdateLoggingConfigurationResponse(BaseValidatorModel):
    status: LoggingConfigurationStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_rule_groups_namespace' function.
class CreateRuleGroupsNamespaceResponse(BaseValidatorModel):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatus
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_rule_groups_namespace' function.
class PutRuleGroupsNamespaceResponse(BaseValidatorModel):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatus
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RuleGroupsNamespaceDescription(BaseValidatorModel):
    arn: str
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatus
    tags: Optional[Dict[str, str]] = None


class RuleGroupsNamespaceSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatus
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_scraper' function.
class CreateScraperResponse(BaseValidatorModel):
    arn: str
    scraperId: str
    status: ScraperStatus
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_scraper' function.
class DeleteScraperResponse(BaseValidatorModel):
    scraperId: str
    status: ScraperStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_scraper' function.
class UpdateScraperResponse(BaseValidatorModel):
    arn: str
    scraperId: str
    status: ScraperStatus
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workspace' function.
class CreateWorkspaceResponse(BaseValidatorModel):
    arn: str
    kmsKeyArn: str
    status: WorkspaceStatus
    tags: Dict[str, str]
    workspaceId: str
    ResponseMetadata: ResponseMetadata


class WorkspaceDescription(BaseValidatorModel):
    arn: str
    createdAt: datetime
    status: WorkspaceStatus
    workspaceId: str
    alias: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    prometheusEndpoint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class WorkspaceSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    status: WorkspaceStatus
    workspaceId: str
    alias: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DescribeScraperRequestWaitExtra(BaseValidatorModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeScraperRequestWait(BaseValidatorModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeWorkspaceRequestWaitExtra(BaseValidatorModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeWorkspaceRequestWait(BaseValidatorModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfig] = None


class SourceOutput(BaseValidatorModel):
    eksConfiguration: Optional[EksConfigurationOutput] = None


class Source(BaseValidatorModel):
    eksConfiguration: Optional[EksConfiguration] = None


class ListRuleGroupsNamespacesRequestPaginate(BaseValidatorModel):
    workspaceId: str
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScrapersRequestPaginate(BaseValidatorModel):
    filters: Optional[Dict[str, List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkspacesRequestPaginate(BaseValidatorModel):
    alias: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_alert_manager_definition' function.
class DescribeAlertManagerDefinitionResponse(BaseValidatorModel):
    alertManagerDefinition: AlertManagerDefinitionDescription
    ResponseMetadata: ResponseMetadata

ScrapeConfigurationUnion = Union[ScrapeConfiguration, ScrapeConfigurationOutput]


# This class is the output for the 'describe_logging_configuration' function.
class DescribeLoggingConfigurationResponse(BaseValidatorModel):
    loggingConfiguration: LoggingConfigurationMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_rule_groups_namespace' function.
class DescribeRuleGroupsNamespaceResponse(BaseValidatorModel):
    ruleGroupsNamespace: RuleGroupsNamespaceDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_rule_groups_namespaces' function.
class ListRuleGroupsNamespacesResponse(BaseValidatorModel):
    ruleGroupsNamespaces: List[RuleGroupsNamespaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_workspace' function.
class DescribeWorkspaceResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_workspaces' function.
class ListWorkspacesResponse(BaseValidatorModel):
    workspaces: List[WorkspaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ScraperDescription(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destination: Destination
    lastModifiedAt: datetime
    roleArn: str
    scrapeConfiguration: ScrapeConfigurationOutput
    scraperId: str
    source: SourceOutput
    status: ScraperStatus
    alias: Optional[str] = None
    roleConfiguration: Optional[RoleConfiguration] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ScraperSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destination: Destination
    lastModifiedAt: datetime
    roleArn: str
    scraperId: str
    source: SourceOutput
    status: ScraperStatus
    alias: Optional[str] = None
    roleConfiguration: Optional[RoleConfiguration] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

SourceUnion = Union[Source, SourceOutput]


# This class is the input for the 'update_scraper' function.
class UpdateScraperRequest(BaseValidatorModel):
    scraperId: str
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    destination: Optional[Destination] = None
    roleConfiguration: Optional[RoleConfiguration] = None
    scrapeConfiguration: Optional[ScrapeConfigurationUnion] = None


# This class is the output for the 'describe_scraper' function.
class DescribeScraperResponse(BaseValidatorModel):
    scraper: ScraperDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_scrapers' function.
class ListScrapersResponse(BaseValidatorModel):
    scrapers: List[ScraperSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_scraper' function.
class CreateScraperRequest(BaseValidatorModel):
    destination: Destination
    scrapeConfiguration: ScrapeConfigurationUnion
    source: SourceUnion
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    roleConfiguration: Optional[RoleConfiguration] = None
    tags: Optional[Dict[str, str]] = None