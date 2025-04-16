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
from aws_resource_validator.pydantic_models.amp_constants import *

class AlertManagerDefinitionStatus(BaseValidatorModel):
    statusCode: AlertManagerDefinitionStatusCodeType
    statusReason: Optional[str] = None


class AmpConfiguration(BaseValidatorModel):
    workspaceArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class CreateWorkspaceRequest(BaseValidatorModel):
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class WorkspaceStatus(BaseValidatorModel):
    statusCode: WorkspaceStatusCodeType


class DeleteAlertManagerDefinitionRequest(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


class DeleteLoggingConfigurationRequest(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


class DeleteRuleGroupsNamespaceRequest(BaseValidatorModel):
    name: str
    workspaceId: str
    clientToken: Optional[str] = None


class DeleteScraperRequest(BaseValidatorModel):
    scraperId: str
    clientToken: Optional[str] = None


class DeleteWorkspaceRequest(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


class DescribeAlertManagerDefinitionRequest(BaseValidatorModel):
    workspaceId: str


class DescribeLoggingConfigurationRequest(BaseValidatorModel):
    workspaceId: str


class DescribeRuleGroupsNamespaceRequest(BaseValidatorModel):
    name: str
    workspaceId: str


class DescribeScraperRequest(BaseValidatorModel):
    scraperId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeWorkspaceRequest(BaseValidatorModel):
    workspaceId: str


class EksConfigurationOutput(BaseValidatorModel):
    clusterArn: str
    subnetIds: List[str]
    securityGroupIds: Optional[List[str]] = None


class EksConfiguration(BaseValidatorModel):
    clusterArn: str
    subnetIds: Sequence[str]
    securityGroupIds: Optional[Sequence[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRuleGroupsNamespacesRequest(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None


class ListScrapersRequest(BaseValidatorModel):
    filters: Optional[Mapping[str, Sequence[str]]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListWorkspacesRequest(BaseValidatorModel):
    alias: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ScrapeConfigurationOutput(BaseValidatorModel):
    configurationBlob: Optional[bytes] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateLoggingConfigurationRequest(BaseValidatorModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None


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


class Blob(BaseValidatorModel):
    pass


class CreateAlertManagerDefinitionRequest(BaseValidatorModel):
    data: Blob
    workspaceId: str
    clientToken: Optional[str] = None


class CreateRuleGroupsNamespaceRequest(BaseValidatorModel):
    data: Blob
    name: str
    workspaceId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class PutAlertManagerDefinitionRequest(BaseValidatorModel):
    data: Blob
    workspaceId: str
    clientToken: Optional[str] = None


class PutRuleGroupsNamespaceRequest(BaseValidatorModel):
    data: Blob
    name: str
    workspaceId: str
    clientToken: Optional[str] = None


class ScrapeConfiguration(BaseValidatorModel):
    configurationBlob: Optional[Blob] = None


class CreateAlertManagerDefinitionResponse(BaseValidatorModel):
    status: AlertManagerDefinitionStatus
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDefaultScraperConfigurationResponse(BaseValidatorModel):
    configuration: bytes
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutAlertManagerDefinitionResponse(BaseValidatorModel):
    status: AlertManagerDefinitionStatus
    ResponseMetadata: ResponseMetadata


class CreateLoggingConfigurationResponse(BaseValidatorModel):
    status: LoggingConfigurationStatus
    ResponseMetadata: ResponseMetadata


class LoggingConfigurationMetadata(BaseValidatorModel):
    createdAt: datetime
    logGroupArn: str
    modifiedAt: datetime
    status: LoggingConfigurationStatus
    workspace: str


class UpdateLoggingConfigurationResponse(BaseValidatorModel):
    status: LoggingConfigurationStatus
    ResponseMetadata: ResponseMetadata


class CreateRuleGroupsNamespaceResponse(BaseValidatorModel):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatus
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


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


class CreateScraperResponse(BaseValidatorModel):
    arn: str
    scraperId: str
    status: ScraperStatus
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeleteScraperResponse(BaseValidatorModel):
    scraperId: str
    status: ScraperStatus
    ResponseMetadata: ResponseMetadata


class UpdateScraperResponse(BaseValidatorModel):
    arn: str
    scraperId: str
    status: ScraperStatus
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


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
    filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkspacesRequestPaginate(BaseValidatorModel):
    alias: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAlertManagerDefinitionResponse(BaseValidatorModel):
    alertManagerDefinition: AlertManagerDefinitionDescription
    ResponseMetadata: ResponseMetadata


class DescribeLoggingConfigurationResponse(BaseValidatorModel):
    loggingConfiguration: LoggingConfigurationMetadata
    ResponseMetadata: ResponseMetadata


class DescribeRuleGroupsNamespaceResponse(BaseValidatorModel):
    ruleGroupsNamespace: RuleGroupsNamespaceDescription
    ResponseMetadata: ResponseMetadata


class ListRuleGroupsNamespacesResponse(BaseValidatorModel):
    ruleGroupsNamespaces: List[RuleGroupsNamespaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeWorkspaceResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


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


class ScrapeConfigurationUnion(BaseValidatorModel):
    pass


class UpdateScraperRequest(BaseValidatorModel):
    scraperId: str
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    destination: Optional[Destination] = None
    roleConfiguration: Optional[RoleConfiguration] = None
    scrapeConfiguration: Optional[ScrapeConfigurationUnion] = None


class DescribeScraperResponse(BaseValidatorModel):
    scraper: ScraperDescription
    ResponseMetadata: ResponseMetadata


class ListScrapersResponse(BaseValidatorModel):
    scrapers: List[ScraperSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SourceUnion(BaseValidatorModel):
    pass


class CreateScraperRequest(BaseValidatorModel):
    destination: Destination
    scrapeConfiguration: ScrapeConfigurationUnion
    source: SourceUnion
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    roleConfiguration: Optional[RoleConfiguration] = None
    tags: Optional[Mapping[str, str]] = None


