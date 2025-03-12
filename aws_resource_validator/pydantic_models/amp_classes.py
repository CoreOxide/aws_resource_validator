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

class AlertManagerDefinitionStatusTypeDef(BaseValidatorModel):
    statusCode: AlertManagerDefinitionStatusCodeType
    statusReason: Optional[str] = None


class AmpConfigurationTypeDef(BaseValidatorModel):
    workspaceArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None


class LoggingConfigurationStatusTypeDef(BaseValidatorModel):
    statusCode: LoggingConfigurationStatusCodeType
    statusReason: Optional[str] = None


class RuleGroupsNamespaceStatusTypeDef(BaseValidatorModel):
    statusCode: RuleGroupsNamespaceStatusCodeType
    statusReason: Optional[str] = None


class RoleConfigurationTypeDef(BaseValidatorModel):
    sourceRoleArn: Optional[str] = None
    targetRoleArn: Optional[str] = None


class ScraperStatusTypeDef(BaseValidatorModel):
    statusCode: ScraperStatusCodeType


class CreateWorkspaceRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class WorkspaceStatusTypeDef(BaseValidatorModel):
    statusCode: WorkspaceStatusCodeType


class DeleteAlertManagerDefinitionRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


class DeleteLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


class DeleteRuleGroupsNamespaceRequestTypeDef(BaseValidatorModel):
    name: str
    workspaceId: str
    clientToken: Optional[str] = None


class DeleteScraperRequestTypeDef(BaseValidatorModel):
    scraperId: str
    clientToken: Optional[str] = None


class DeleteWorkspaceRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None


class DescribeAlertManagerDefinitionRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class DescribeLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class DescribeRuleGroupsNamespaceRequestTypeDef(BaseValidatorModel):
    name: str
    workspaceId: str


class DescribeScraperRequestTypeDef(BaseValidatorModel):
    scraperId: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeWorkspaceRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class EksConfigurationOutputTypeDef(BaseValidatorModel):
    clusterArn: str
    subnetIds: List[str]
    securityGroupIds: Optional[List[str]] = None


class EksConfigurationTypeDef(BaseValidatorModel):
    clusterArn: str
    subnetIds: Sequence[str]
    securityGroupIds: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRuleGroupsNamespacesRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None


class ListScrapersRequestTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[str, Sequence[str]]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListWorkspacesRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ScrapeConfigurationOutputTypeDef(BaseValidatorModel):
    configurationBlob: Optional[bytes] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None


class UpdateWorkspaceAliasRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    alias: Optional[str] = None
    clientToken: Optional[str] = None


class AlertManagerDefinitionDescriptionTypeDef(BaseValidatorModel):
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    status: AlertManagerDefinitionStatusTypeDef


class DestinationTypeDef(BaseValidatorModel):
    ampConfiguration: Optional[AmpConfigurationTypeDef] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class CreateAlertManagerDefinitionRequestTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    workspaceId: str
    clientToken: Optional[str] = None


class CreateRuleGroupsNamespaceRequestTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    name: str
    workspaceId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class PutAlertManagerDefinitionRequestTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    workspaceId: str
    clientToken: Optional[str] = None


class PutRuleGroupsNamespaceRequestTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    name: str
    workspaceId: str
    clientToken: Optional[str] = None


class ScrapeConfigurationTypeDef(BaseValidatorModel):
    configurationBlob: Optional[BlobTypeDef] = None


class CreateAlertManagerDefinitionResponseTypeDef(BaseValidatorModel):
    status: AlertManagerDefinitionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetDefaultScraperConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: bytes
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutAlertManagerDefinitionResponseTypeDef(BaseValidatorModel):
    status: AlertManagerDefinitionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoggingConfigurationMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    logGroupArn: str
    modifiedAt: datetime
    status: LoggingConfigurationStatusTypeDef
    workspace: str


class UpdateLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRuleGroupsNamespaceResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutRuleGroupsNamespaceResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class RuleGroupsNamespaceDescriptionTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Optional[Dict[str, str]] = None


class RuleGroupsNamespaceSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Optional[Dict[str, str]] = None


class CreateScraperResponseTypeDef(BaseValidatorModel):
    arn: str
    scraperId: str
    status: ScraperStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteScraperResponseTypeDef(BaseValidatorModel):
    scraperId: str
    status: ScraperStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateScraperResponseTypeDef(BaseValidatorModel):
    arn: str
    scraperId: str
    status: ScraperStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkspaceResponseTypeDef(BaseValidatorModel):
    arn: str
    kmsKeyArn: str
    status: WorkspaceStatusTypeDef
    tags: Dict[str, str]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class WorkspaceDescriptionTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    status: WorkspaceStatusTypeDef
    workspaceId: str
    alias: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    prometheusEndpoint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class WorkspaceSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    status: WorkspaceStatusTypeDef
    workspaceId: str
    alias: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DescribeScraperRequestWaitExtraTypeDef(BaseValidatorModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeScraperRequestWaitTypeDef(BaseValidatorModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeWorkspaceRequestWaitExtraTypeDef(BaseValidatorModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeWorkspaceRequestWaitTypeDef(BaseValidatorModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class SourceOutputTypeDef(BaseValidatorModel):
    eksConfiguration: Optional[EksConfigurationOutputTypeDef] = None


class SourceTypeDef(BaseValidatorModel):
    eksConfiguration: Optional[EksConfigurationTypeDef] = None


class ListRuleGroupsNamespacesRequestPaginateTypeDef(BaseValidatorModel):
    workspaceId: str
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListScrapersRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkspacesRequestPaginateTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAlertManagerDefinitionResponseTypeDef(BaseValidatorModel):
    alertManagerDefinition: AlertManagerDefinitionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    loggingConfiguration: LoggingConfigurationMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRuleGroupsNamespaceResponseTypeDef(BaseValidatorModel):
    ruleGroupsNamespace: RuleGroupsNamespaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRuleGroupsNamespacesResponseTypeDef(BaseValidatorModel):
    ruleGroupsNamespaces: List[RuleGroupsNamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeWorkspaceResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListWorkspacesResponseTypeDef(BaseValidatorModel):
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ScraperDescriptionTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destination: DestinationTypeDef
    lastModifiedAt: datetime
    roleArn: str
    scrapeConfiguration: ScrapeConfigurationOutputTypeDef
    scraperId: str
    source: SourceOutputTypeDef
    status: ScraperStatusTypeDef
    alias: Optional[str] = None
    roleConfiguration: Optional[RoleConfigurationTypeDef] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ScraperSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destination: DestinationTypeDef
    lastModifiedAt: datetime
    roleArn: str
    scraperId: str
    source: SourceOutputTypeDef
    status: ScraperStatusTypeDef
    alias: Optional[str] = None
    roleConfiguration: Optional[RoleConfigurationTypeDef] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ScrapeConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateScraperRequestTypeDef(BaseValidatorModel):
    scraperId: str
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    destination: Optional[DestinationTypeDef] = None
    roleConfiguration: Optional[RoleConfigurationTypeDef] = None
    scrapeConfiguration: Optional[ScrapeConfigurationUnionTypeDef] = None


class DescribeScraperResponseTypeDef(BaseValidatorModel):
    scraper: ScraperDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListScrapersResponseTypeDef(BaseValidatorModel):
    scrapers: List[ScraperSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateScraperRequestTypeDef(BaseValidatorModel):
    destination: DestinationTypeDef
    scrapeConfiguration: ScrapeConfigurationUnionTypeDef
    source: SourceUnionTypeDef
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    roleConfiguration: Optional[RoleConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


